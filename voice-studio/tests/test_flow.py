"""End-to-end flow without a GPU: voice + consent → import → segments → review → dataset → TTS (test engine)."""
import importlib
import io
import math
import os
import shutil
import sys
import wave
from pathlib import Path

import numpy as np
import pytest

SAMPLE = os.environ.get("VSTUDIO_TEST_WAV")  # a short real speech recording (VAD ignores synthetic tones)
needs_speech = pytest.mark.skipif(not SAMPLE, reason="set VSTUDIO_TEST_WAV to a short speech recording (e.g. 10 s)")


def _synthetic_speech(path: Path, seconds: float = 12.0, sr: int = 16000) -> Path:
    """Voiced bursts separated by silences: enough for VAD and the pipeline mechanics."""
    t = np.arange(int(sr * seconds)) / sr
    y = np.zeros_like(t)
    for start in (0.5, 3.5, 6.5, 9.5):
        m = (t >= start) & (t < start + 2.2)
        f0 = 140 + 30 * np.sin(2 * math.pi * 3 * t[m])
        ph = 2 * math.pi * np.cumsum(f0) / sr
        y[m] = 0.3 * (np.sin(ph) + 0.5 * np.sin(2 * ph) + 0.25 * np.sin(3 * ph)) * (1 + 0.5 * np.sin(2 * math.pi * 4 * t[m]))
    y += 0.003 * np.random.default_rng(0).standard_normal(len(t))
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
        w.writeframes((np.clip(y, -1, 1) * 32767).astype("<i2").tobytes())
    return path


@pytest.fixture()
def client(tmp_path, monkeypatch):
    monkeypatch.setenv("VSTUDIO_DATA", str(tmp_path / "data"))
    assets = os.environ.get("VSTUDIO_TEST_ASSETS")
    if assets:
        (tmp_path / "data" / "assets").mkdir(parents=True)
        for f in Path(assets).glob("*.onnx"):
            shutil.copy(f, tmp_path / "data" / "assets" / f.name)
    for m in [m for m in list(sys.modules) if m.startswith("vstudio")]:
        del sys.modules[m]
    import vstudio.db as db
    db.reset_connection()
    from vstudio.pipeline import asr

    def fake_transcribe(audio16k, name, language=None, device="auto", prompt=None):
        return {"text": "テストの文です" if name.endswith("turbo") else "テストの文です", "lang": "ja",
                "lang_prob": 0.99, "avg_logprob": -0.2, "no_speech": 0.01}
    monkeypatch.setattr(asr, "transcribe", fake_transcribe)
    server = importlib.import_module("vstudio.server")
    from fastapi.testclient import TestClient
    with TestClient(server.app) as c:
        yield c
    db.reset_connection()


def _wait(c, job_id, timeout=120):
    import time
    t0 = time.time()
    while time.time() - t0 < timeout:
        j = c.get(f"/api/jobs/{job_id}").json()
        if j["status"] in ("done", "failed", "canceled"):
            return j
        time.sleep(0.3)
    raise AssertionError("job timeout")


@needs_speech
def test_full_flow(client, tmp_path):
    c = client
    v = c.post("/api/voices", json={"name": "我", "kind": "self", "languages": ["ja"]}).json()
    assert v["consent_ok"] is False
    # dataset refused without consent
    assert c.post("/api/datasets", json={"voice_id": v["id"]}).status_code in (400, 409)
    r = c.post(f"/api/voices/{v['id']}/consent",
               data={"signed_name": "測試者", "date": "2026-10-06", "agreed": "true", "scope": "train,generate"})
    assert r.json()["consent_ok"] is True

    wav = Path(SAMPLE) if SAMPLE else _synthetic_speech(tmp_path / "talk.wav")
    with open(wav, "rb") as fh:
        up = c.post("/api/sources/upload", files={"file": ("talk.wav", fh, "audio/wav")},
                    data={"voice_hint": v["id"], "language": "ja"}).json()
    job = _wait(c, up["job"]["id"])
    assert job["status"] == "done", job
    segs = c.get(f"/api/segments?voice_id={v['id']}").json()
    assert segs["total"] >= 1
    first = segs["items"][0]
    assert first["text"] == "テストの文です" and first["asr_agree"] == 1.0
    assert c.get(f"/api/segments/{first['id']}/audio").status_code == 200

    # review: approve all, edit one transcript
    c.post("/api/segments/bulk", json={"filter": {"voice_id": v["id"]}, "status": "approved"})
    p = c.patch(f"/api/segments/{first['id']}", json={"text": "テストの文章です"}).json()
    assert p["edited"] == 1

    ds = c.post("/api/datasets", json={"voice_id": v["id"], "name": "v1"}).json()
    assert ds["n_items"] == segs["total"] and ds["meta"]["consent"]["signed_name"] == "測試者"
    assert (Path(ds["path"]) / "train.jsonl").exists()

    # plan a cloud run (no network call needed)
    plan = c.post("/api/training/plan", json={"dataset_id": ds["id"], "engine": "mock", "preset": "quick"}).json()
    assert plan["estimate_usd"] >= 0

    # TTS with the test engine, 3 takes ranked
    m = c.post("/api/models/demo").json()
    out = c.post("/api/tts", json={"model_id": m["id"], "text": "[bright] こんにちは", "takes": 3}).json()
    assert len(out["outputs"]) == 3 and sum(o["score"].get("best", False) for o in out["outputs"]) == 1
    assert c.get(f"/api/outputs/{out['outputs'][0]['id']}/audio").status_code == 200

    # presets from the novel-lab sheets, then a scene script with casting
    imp = c.post("/api/presets/import-holoen").json()
    assert imp["created"] >= 30
    script = "@@scene t\n@@date 2026-10-06\nHoshimachi Suisei :: [focused, clipped] もう一回。\nROMAJI :: Mō ikkai.\nPAUSE :: 0.5\nMori Calliope :: [casual, fast] Okay.\n"
    parsed = c.post("/api/script/parse", json={"script": script}).json()
    assert {s["name"] for s in parsed["speakers"]} == {"Hoshimachi Suisei", "Mori Calliope"}
    job = c.post("/api/script/render", json={"script": script, "takes": 1,
                                             "cast": {"Hoshimachi Suisei": {"model_id": m["id"], "language": "ja"},
                                                      "Mori Calliope": {"model_id": m["id"], "language": "en"}}}).json()
    j = _wait(c, job["id"])
    assert j["status"] == "done", j

    sysinfo = c.get("/api/system").json()
    assert sysinfo["counts"]["voices"] >= 1


def test_secrets_never_returned(client):
    st = client.get("/api/settings").json()
    assert set(st["secrets"]) >= {"runpod_api_key"} and all(isinstance(v, bool) for v in st["secrets"].values())


def _approved_dataset(c, tmp_path):
    v = c.post("/api/voices", json={"name": "我", "kind": "self", "languages": ["ja"]}).json()
    c.post(f"/api/voices/{v['id']}/consent",
           data={"signed_name": "測試者", "date": "2026-10-06", "agreed": "true", "scope": "train,generate"})
    wav = Path(SAMPLE) if SAMPLE else _synthetic_speech(tmp_path / "talk.wav")
    with open(wav, "rb") as fh:
        up = c.post("/api/sources/upload", files={"file": ("talk.wav", fh, "audio/wav")},
                    data={"voice_hint": v["id"], "language": "ja"}).json()
    assert _wait(c, up["job"]["id"])["status"] == "done"
    c.post("/api/segments/bulk", json={"filter": {"voice_id": v["id"]}, "status": "approved"})
    return v, c.post("/api/datasets", json={"voice_id": v["id"], "name": "v1"}).json()


@needs_speech
def test_cloud_roundtrip_with_mock_pod(client, tmp_path):
    """Everything a pod does, run locally: package → train_entry.py (mock) → model.tar → install → scoring."""
    import json
    import subprocess
    import tarfile
    from vstudio import db, engines, training

    c = client
    v, ds = _approved_dataset(c, tmp_path)
    tid = db.new_id("tr")
    eng = engines.get("mock")
    db.insert("trainings", {"id": tid, "voice_id": v["id"], "dataset_id": ds["id"], "engine": "mock",
                            "preset": {"id": "quick", "params": {"steps": 4}, "name": ""}, "target": "runpod",
                            "status": "running", "gpu": "x", "remote_prefix": f"vs/jobs/{tid}", "progress": {},
                            "created_at": db.now()})
    work = tmp_path / "work"
    work.mkdir()
    tar_path, cfg = training.package_dataset(tid, work)
    pod_job = tmp_path / "pod" / "jobs" / tid
    pod_job.mkdir(parents=True)
    (pod_job / "config.json").write_text(json.dumps(cfg), encoding="utf-8")
    for name, text in eng.cloud_files().items():
        (pod_job / name).write_text(text, encoding="utf-8")
    with tarfile.open(tar_path) as t:
        t.extractall(tmp_path / "pod" / "vsdata", filter="data")
    samples = json.loads((tmp_path / "pod" / "vsdata" / "data" / "samples.json").read_text(encoding="utf-8"))
    assert samples["lines"] and samples["reference"]
    env = {**os.environ, "VS_WORK": str(tmp_path / "pod" / "work"), "VS_MOCK_DELAY": "0"}
    subprocess.run([sys.executable, str(pod_job / "train_entry.py"), "--config", str(pod_job / "config.json"),
                    "--data", str(tmp_path / "pod" / "vsdata")], check=True, env=env)
    prog = json.loads((pod_job / "progress.json").read_text())
    assert prog["phase"] == "package" and prog["total"] == 4
    m = training.install_model(tid, pod_job / "model.tar")
    assert m["meta"]["checkpoint"] == "step_0000004" and m["meta"]["references"]
    ev = db.query("SELECT * FROM jobs WHERE kind='evaluate_model'")[0]
    j = _wait(c, ev["id"])
    assert j["status"] == "done", j
    got = c.get(f"/api/models/{m['id']}").json()
    names = [r["name"] for r in got["metrics"]["checkpoints"]]
    assert names[0] == "base" and got["metrics"]["recommended"] in ("step_0000002", "step_0000004")
    assert c.get(f"/api/models/{m['id']}/samples/base/0_plain.wav").status_code == 200
    assert c.get(f"/api/models/{m['id']}/samples/../engine.json/x").status_code == 404
    from fastapi import HTTPException
    from vstudio.api.train import _safe_file
    with pytest.raises(HTTPException):
        _safe_file(Path(m["path"]), "samples/../../../studio.db")
    # pick a checkpoint by hand, then speak with a reference clip
    assert c.patch(f"/api/models/{m['id']}", json={"checkpoint": "step_0000002"}).json()["meta"]["checkpoint"] == "step_0000002"
    out = c.post("/api/tts", json={"model_id": m["id"], "text": "テストです", "mode": "ref"}).json()
    assert out["mode"] == "ref" and out["outputs"][0]["params"]["ref"] == "ref0"
    assert out["outputs"][0]["params"]["checkpoint"] == "step_0000002"

    # zero-shot model from approved segments
    seg = c.get(f"/api/segments?voice_id={v['id']}").json()["items"][0]
    z = c.post("/api/models/zeroshot", json={"voice_id": v["id"], "engine": "mock", "segment_ids": [seg["id"]]}).json()
    assert z["meta"]["mode"] == "zeroshot"
    assert c.post("/api/tts", json={"model_id": z["id"], "text": "Hello", "mode": "ref"}).status_code == 200


def test_real_engine_cloud_files_render(client, tmp_path):
    import py_compile
    from vstudio import engines
    for eid in ("voxcpm2", "qwen3"):
        eng = engines.get(eid)
        files = eng.cloud_files()
        assert {"setup_env.sh", "train_entry.py", "vs_common.py"} <= set(files)
        assert "{" not in files["setup_env.sh"].split("python - <<'PY'")[0].replace("${", "").replace("{ ", "")
        for name in ("train_entry.py", "vs_common.py"):
            f = tmp_path / f"{eid}_{name}"
            f.write_text(files[name], encoding="utf-8")
            py_compile.compile(str(f), doraise=True)
        assert eng.steps(3600, eng.presets[0].id) > 0
    vox = engines.get("voxcpm2")
    assert vox.steps(3600, "lora") == round(3600 // 16 * 2)
    est = vox.estimate(10, "lora", 1.09, n_train=3600)
    assert est["steps"] == 450 and 0.5 < est["hours"] < 3
    assert vox.estimate(10, "lora", 1.09, n_train=3600, s_per_step=20)["basis"] == "measured"


@needs_speech
def test_voxcpm_export_manifest(client, tmp_path):
    import json
    from vstudio import db, engines
    c = client
    v, ds = _approved_dataset(c, tmp_path)
    ds = db.get("datasets", ds["id"])
    info = engines.get("voxcpm2").export_dataset(ds, tmp_path / "exp", {"ref_fraction": 1.0})
    rows = [json.loads(x) for x in (tmp_path / "exp" / "train.jsonl").read_text(encoding="utf-8").splitlines()]
    assert rows and set(rows[0]) >= {"audio", "text", "duration", "lang"}
    assert all(r["audio"].startswith("wavs/") for r in rows)
    if len(rows) > 1:
        assert info["n_ref"] == len(rows) and all(r["ref_audio"] != r["audio"] for r in rows)

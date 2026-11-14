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
    with tarfile.open(pod_job / "model.tar") as t:
        names = t.getnames()
    assert "model/engine.json" in names and not any(n.endswith("optimizer.pth") for n in names)
    m = training.install_model(tid, pod_job / "model.tar", pod_job / "samples.tar")
    assert training.install_model(tid, pod_job / "model.tar")["id"] == m["id"]  # idempotent
    assert m["meta"]["checkpoint"] == "step_0000004" and m["meta"]["references"]
    ev = db.query("SELECT * FROM jobs WHERE kind='evaluate_model'")[0]
    j = _wait(c, ev["id"])
    assert j["status"] == "done", j
    got = c.get(f"/api/models/{m['id']}").json()
    rows = got["metrics"]["checkpoints"]
    assert rows[0]["name"] == "base" and "plain" in rows[0]["summary"]
    # this tiny dataset has no held-out lines, so there is no automatic recommendation, only a reason
    held = got["metrics"]["held_out_lines"]
    assert (got["metrics"]["recommended"] is None and got["metrics"]["reason"]) if held == 0 else True
    assert c.get(f"/api/models/{m['id']}/samples/base/0_plain.wav").status_code == 200
    assert c.get(f"/api/models/{m['id']}/samples/../engine.json/x").status_code == 404
    from fastapi import HTTPException
    from vstudio.api.train import _safe_file
    with pytest.raises(HTTPException):
        _safe_file(Path(m["path"]), "samples/../../../studio.db")
    with pytest.raises(KeyError):
        training.remove_reference(m["id"], "../../studio")
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
        import re
        assert not re.search(r"\{(engine|name|repo|commit|version|module|cls|extra_pip|post|recipe)\}", files["setup_env.sh"])
        assert re.search(r"\.ready-[0-9a-f]{12}-", files["setup_env.sh"])
        for name in ("train_entry.py", "vs_common.py"):
            f = tmp_path / f"{eid}_{name}"
            f.write_text(files[name], encoding="utf-8")
            py_compile.compile(str(f), doraise=True)
        assert eng.steps(3600, eng.presets[0].id) > 0
    vox = engines.get("voxcpm2")
    assert vox.steps(3600, "lora") == 450  # 1800 batches × 2 epochs ÷ 8 accumulation
    est = vox.estimate(10, "lora", 1.09, n_train=3600)
    assert est["steps"] == 450 and 0.5 < est["hours"] < 3
    eff = vox.effective_params("lora", {"epochs": 1}, 3600)
    assert eff["total_steps"] == 225 and eff["epochs_effective"] == 1.0
    with pytest.raises(ValueError):
        vox.effective_params("lora", None, 1)  # not even one batch
    small = vox.effective_params("lora", None, 18)  # 9 batches: accumulation carries across epochs
    assert small["total_steps"] == 3 and small["epochs_effective"] == 2.67
    with pytest.raises(ValueError):
        vox.effective_params("lora", {"lr": 1}, 3600)  # not user-adjustable
    with pytest.raises(ValueError):
        vox.effective_params("lora", {"epochs": 100}, 3600)  # out of range
    assert engines.get("qwen3").effective_params("sft", {"epochs": 1.6}, 100)["epochs"] == 2
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


def test_voxcpm_config_numbers_survive_yaml():
    """The official trainer reads its config with yaml.safe_load. json.dumps wrote full fine-tuning's learning rate
    as 1e-05, which YAML 1.1 reads as text, and training stopped at the optimizer (AdamW: float <= str)."""
    import importlib.util
    import json
    yaml = pytest.importorskip("yaml")
    path = Path(__file__).resolve().parents[1] / "vstudio" / "engines" / "remote" / "voxcpm2_train.py"
    spec = importlib.util.spec_from_file_location("voxcpm2_train_under_test", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    assert yaml.safe_load(json.dumps({"lr": 1e-5}))["lr"] == "1e-05"  # the trap itself
    for lr in (1e-4, 1e-5, 5e-5, 2e-6, 3e-4, -1e-7, 1e20):
        conf = {"pretrained_path": "/root/.cache/huggingface/VoxCPM2", "val_manifest": "", "batch_size": 2,
                "learning_rate": lr, "weight_decay": 0.01, "max_grad_norm": 1.0, "num_iters": 300,
                "lambdas": {"loss/diff": 1.0, "loss/stop": 1.0},
                "lora": {"enable_lm": True, "enable_proj": False, "r": 32, "dropout": 0.0}, "steps": [1e-5, 2]}
        text = mod.config_text(conf)
        back = yaml.safe_load(text)
        assert back == conf and type(back["learning_rate"]) is float, text
        assert json.loads(text) == conf  # still JSON as well


def test_lexicon_longest_first(client):
    from vstudio import config, tts
    config.save_settings({"lexicon": [{"from": "推し", "to": "おし", "lang": "ja"},
                                      {"from": "推しの子", "to": "おしのこ", "lang": "ja"},
                                      {"from": "AI", "to": "エーアイ", "lang": "ja"}]})
    assert tts.apply_lexicon("推しの子と推し", "ja") == "おしのことおし"
    assert tts.apply_lexicon("AI voice", "en") == "AI voice"


def test_guard_blocks_foreign_hosts_and_origins(client):
    c = client
    assert c.get("/api/voices").status_code == 200
    assert c.get("/api/voices", headers={"host": "evil.example"}).status_code == 403  # DNS rebinding
    r = c.post("/api/voices", json={"name": "x", "kind": "self"}, headers={"origin": "http://evil.example"})
    assert r.status_code == 403  # another website's page
    r = c.post("/api/voices", json={"name": "x", "kind": "self"}, headers={"origin": "http://testserver:9999"})
    assert r.status_code == 403  # same host, different port = different origin
    r = c.post("/api/voices", json={"name": "x", "kind": "self", "languages": []},
               headers={"origin": "http://testserver"})
    assert r.status_code == 200


def test_password_mode(tmp_path, monkeypatch):
    monkeypatch.setenv("VSTUDIO_DATA", str(tmp_path / "data"))
    monkeypatch.setenv("VSTUDIO_PASSWORD", "correct horse")
    for m in [m for m in list(sys.modules) if m.startswith("vstudio")]:
        del sys.modules[m]
    server = importlib.import_module("vstudio.server")
    from fastapi.testclient import TestClient
    with TestClient(server.app) as c:
        assert c.get("/api/voices").status_code == 401
        assert c.get("/api/voices", headers={"x-studio-password": "correct horse"}).status_code == 200
        c.cookies.set("studio_pw", "correct%20horse")
        assert c.get("/api/voices").status_code == 200
        assert c.get("/api/health").status_code == 200
    import vstudio.db as db
    db.reset_connection()


def test_migration_keeps_duplicate_models(tmp_path, monkeypatch):
    """An older database with two models for one training must still open (and keep both models)."""
    import sqlite3
    monkeypatch.setenv("VSTUDIO_DATA", str(tmp_path / "data"))
    (tmp_path / "data").mkdir()
    for m in [m for m in list(sys.modules) if m.startswith("vstudio")]:
        del sys.modules[m]
    import vstudio.db as db
    raw = sqlite3.connect(tmp_path / "data" / "studio.db")
    raw.executescript(db.SCHEMA)
    for i in range(2):
        raw.execute("INSERT INTO models (id, voice_id, engine, name, training_id, path, meta, metrics, created_at) "
                    "VALUES (?, 'v', 'mock', 'm', 'tr1', '/x', '{}', '{}', ?)", (f"m{i}", i))
    raw.commit()
    raw.close()
    c = db.connect()
    rows = c.execute("SELECT id, training_id, meta FROM models ORDER BY created_at").fetchall()
    assert [r[1] for r in rows] == ["tr1", None] and "duplicate_of_training" in rows[1][2]
    db.reset_connection()


def test_checkpoint_paths_stay_inside_model(tmp_path):
    from vstudio.engines.base import Engine
    meta = {"checkpoints": [{"name": "../../etc", "weights": True}]}
    with pytest.raises(ValueError):
        Engine.checkpoint_dir(tmp_path, meta, None)


def test_screen_device_follows_vram(client, monkeypatch):
    from vstudio import tts
    monkeypatch.setattr(tts, "gpu_total_gb", lambda: 10.0)   # RTX 3080 10GB
    assert tts.screen_device({"asr_screen_device": "auto"}) == "cpu"
    monkeypatch.setattr(tts, "gpu_total_gb", lambda: 24.0)
    assert tts.screen_device({"asr_screen_device": "auto"}) == "cuda"
    assert tts.screen_device({"asr_screen_device": "cpu"}) == "cpu"


def test_auto_review_rules():
    from vstudio.pipeline import autoreview as ar
    p = ar.PROFILES["balanced"]
    good = {"text": "今日はいい天気ですね", "lang": "ja", "duration": 3.0, "asr_agree": 0.97, "snr": 28.0, "clip": 0.0,
            "spk_sim": 0.8, "asr_logprob": -0.2, "no_speech": 0.02}
    assert ar.decide(good, p, 0.62, 0.05) == ("approve", [])
    assert ar.decide({**good, "asr_agree": 0.8}, p, 0.62, 0.05) == ("unsure", ["agree"])
    assert ar.decide({**good, "asr_agree": None}, p, 0.62, 0.05)[0] == "unsure"   # unmeasured never passes
    assert ar.decide({**good, "snr": 8.0}, p, 0.62, 0.05)[0] == "reject"
    assert ar.decide({**good, "spk_sim": 0.3}, p, 0.62, 0.05) == ("reject", ["speaker"])
    assert ar.decide(good, p, 0.62, 0.3) == ("unsure", ["window"])
    assert ar.decide(good, p, 0.62, 0.5)[0] == "reject"
    assert ar.decide({**good, "duration": 0.5}, p, 0.62, None)[0] == "reject"
    assert ar.decide(good, ar.PROFILES["strict"], 0.62, 0.05) == ("approve", [])
    assert ar.decide({**good, "snr": 20.0}, ar.PROFILES["strict"], 0.62, 0.05) == ("unsure", ["snr"])
    # speaking rate: 10 characters in 3 s is fine; in 0.2 s it is not a person talking
    assert ar.rate_ok("今日はいい天気ですね", "ja", 3.0) and not ar.rate_ok("今日はいい天気ですね", "ja", 0.5)
    assert ar.rate_ok("so I was thinking about it", "en", 2.5) and not ar.rate_ok("yes", "en", 12.0)
    # a person's decision on a spot check replaces the automatic flags and records the outcome
    assert ar.human_status(["auto_approved", "spot_check", "noisy"], "rejected") == ["noisy", "spot_fail"]
    assert ar.human_status(["auto_unsure", "auto:agree"], "approved") == []


def _tone(path: Path, parts: list[tuple[float, float]], sr: int = 16000) -> Path:
    y = np.concatenate([amp * np.sin(2 * math.pi * 200 * np.arange(int(sr * sec)) / sr) for sec, amp in parts])
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
        w.writeframes((y * 32767).astype("<i2").tobytes())
    return path


def test_auto_review_job_and_undo(client, tmp_path, monkeypatch):
    """Loud tone = the voice, quiet tone = someone else (a stand-in speaker embedding)."""
    from vstudio import db
    from vstudio.pipeline import speaker

    class FakeEmbedder:
        def embed(self, y):
            t = float(np.clip((0.19 - np.abs(y).mean()) / 0.16, 0, 1)) * math.pi / 2
            return np.array([math.cos(t), math.sin(t)], dtype=np.float32)
    monkeypatch.setattr(speaker, "Embedder", FakeEmbedder)
    vid = db.insert("voices", {"id": "v1", "name": "me", "kind": "self", "created_at": db.now()})["id"]
    db.insert("sources", {"id": "s1", "filename": "a.wav", "path": "a.wav", "status": "ready", "created_at": db.now()})
    d = tmp_path / "segs"
    d.mkdir()

    def seg(sid, parts, **kw):
        row = {"id": sid, "source_id": "s1", "voice_id": vid, "start": 0.0, "end": 1.0, "path": str(_tone(d / f"{sid}.wav", parts)),
               "duration": sum(p[0] for p in parts), "text": "テストの文です", "lang": "ja", "asr_agree": 0.98, "snr": 30.0,
               "clip": 0.0, "score": 0.9, "status": "pending", "flags": [], "asr_logprob": -0.2, "no_speech": 0.01}
        db.insert("segments", {**row, **kw})
    for i in range(8):
        seg(f"good{i}", [(3.0, 0.3)])
    seg("other", [(3.0, 0.05)], score=0.5)
    seg("noisy", [(3.0, 0.3)], snr=8.0, score=0.5)
    seg("unsure", [(3.0, 0.3)], asr_agree=0.8, score=0.6)
    seg("mixed", [(3.0, 0.3), (3.0, 0.05)], score=0.5)
    seg("edited", [(3.0, 0.05)], edited=1, score=0.5)
    seg("mine", [(3.0, 0.05)], status="approved", score=0.5)

    job = client.post(f"/api/auto-review/{vid}", json={"profile": "balanced"}).json()
    j = _wait(client, job["id"])
    assert j["status"] == "done", j
    st = {s["id"]: s for s in db.query("SELECT * FROM segments")}
    assert all(st[f"good{i}"]["status"] == "approved" and "auto_approved" in st[f"good{i}"]["flags"] for i in range(8))
    assert st["other"]["status"] == "rejected" and "auto:speaker" in st["other"]["flags"]
    assert st["noisy"]["status"] == "rejected" and "auto:snr" in st["noisy"]["flags"]
    assert st["unsure"]["status"] == "pending" and "auto_unsure" in st["unsure"]["flags"]
    assert st["mixed"]["status"] == "rejected" and "auto:window" in st["mixed"]["flags"]
    assert st["edited"]["status"] == "pending" and st["edited"]["flags"] == []      # a person edited it: untouched
    assert st["mine"]["status"] == "approved" and st["mine"]["flags"] == []         # a person decided it: untouched
    assert j["result"]["counts"] == {"approve": 8, "reject": 3, "unsure": 1}
    s = client.get(f"/api/auto-review/{vid}").json()
    assert s["unsure"] == 1 and s["spot_left"] == 8
    listed = client.get(f"/api/segments?voice_id={vid}&flag=auto_unsure&status=pending").json()
    assert [x["id"] for x in listed["items"]] == ["unsure"]

    # the person rejects one spot check and confirms another
    client.patch("/api/segments/good0", json={"status": "rejected"})
    client.patch("/api/segments/good1", json={"status": "approved"})
    s = client.get(f"/api/auto-review/{vid}").json()
    assert (s["spot_left"], s["spot_ok"], s["spot_fail"]) == (6, 1, 1)

    # undo: automatic decisions go back to pending, the person's decisions stay
    assert client.post(f"/api/auto-review/{vid}/undo").json()["reset"] >= 10
    st = {s["id"]: s for s in db.query("SELECT * FROM segments")}
    assert st["good2"]["status"] == "pending" and st["good2"]["flags"] == []
    assert st["other"]["status"] == "pending" and st["unsure"]["flags"] == []
    assert st["good0"]["status"] == "rejected" and st["good1"]["status"] == "approved"
    assert st["mine"]["status"] == "approved"


def test_emotion_words():
    from vstudio import emotions
    assert emotions.from_style("annoyed, sharp") == "annoyed" and emotions.from_style("angry, sharp") == "angry"
    assert emotions.from_style("I made it") is None          # "mad" is not inside "made"
    assert emotions.from_style("laughing softly") == "laughing"
    assert emotions.from_style("calm, then excited") == "neutral"   # the earliest word wins
    assert emotions.from_text_tags("[whispers] ねえ") == "whisper"
    assert emotions.valid("angry") == "angry" and emotions.valid("furious") is None


def _consented_voice(c, name="我"):
    v = c.post("/api/voices", json={"name": name, "kind": "self", "languages": ["ja", "en"]}).json()
    c.post(f"/api/voices/{v['id']}/consent",
           data={"signed_name": "測試者", "date": "2026-10-10", "agreed": "true", "scope": "train,generate"})
    return v


def _seg(db, vid, sid, text, d, seconds=6.0, amp=0.3, **kw):
    path = _tone(d / f"{sid}.wav", [(seconds, amp)], sr=48000)
    row = {"id": sid, "source_id": "s1", "voice_id": vid, "start": 0.0, "end": seconds, "path": str(path),
           "duration": seconds, "text": text, "text_alt": text, "lang": "ja", "asr_agree": 1.0, "snr": 30.0,
           "clip": 0.0, "score": 0.9, "status": "approved", "flags": []}
    return db.insert("segments", {**row, **kw})


def test_delete_voice_with_everything_under_it(client, tmp_path, monkeypatch):
    """Deleting a voice removes it and all its audio: recordings, clips, catchphrases, sound tags, datasets,
    trainings (also their cloud files), models, and speech made with them. Another voice's clips in a shared
    recording, and files outside the studio, stay. A running training blocks it; leftovers in the cloud are listed."""
    from vstudio import config, db
    from vstudio.cloud import runpod
    c = client
    a, b = _consented_voice(c, "Nerissa"), _consented_voice(c, "Other")
    outside = tmp_path / "交付總覽" / "original.wav"                    # a recording that was never copied in
    outside.parent.mkdir()
    _tone(outside, [(2.0, 0.3)])
    db.insert("sources", {"id": "own", "filename": "own.wav", "path": str(outside), "status": "ready",
                          "voice_hint": a["id"], "meta": {"copied": False}, "created_at": db.now()})
    db.insert("sources", {"id": "shared", "filename": "collab.wav", "path": "collab.wav", "status": "ready",
                          "created_at": db.now()})
    segdir = config.DATA / "segments" / "own"
    segdir.mkdir(parents=True)
    own = _seg(db, a["id"], "sa1", "私のクリップ", segdir, source_id="own")
    mine = _seg(db, a["id"], "sa2", "コラボの私", tmp_path, source_id="shared")
    theirs = _seg(db, b["id"], "sb1", "コラボの相手", tmp_path, source_id="shared")
    db.insert("sound_finds", {"id": "sf1", "voice_id": a["id"], "source_id": "shared", "start": 0.0, "end": 1.0,
                              "kind": "laugh", "how": "scan", "created_at": db.now()})
    ph = c.post(f"/api/voices/{a['id']}/phrases", json={"text": "やっほー", "lang": "ja"}).json()
    ds_dir = config.DATA / "datasets" / "dsA"
    ds_dir.mkdir(parents=True)
    db.insert("datasets", {"id": "dsA", "voice_id": a["id"], "name": "v1", "n_items": 1, "hours": 0.1,
                           "path": str(ds_dir), "created_at": db.now()})
    m_dir = config.DATA / "models" / "mA"
    m_dir.mkdir(parents=True)
    db.insert("models", {"id": "mA", "voice_id": a["id"], "engine": "mock", "name": "A", "path": str(m_dir),
                         "created_at": db.now()})
    out_dir = config.DATA / "outputs"
    out_dir.mkdir(parents=True, exist_ok=True)
    made = {}
    for oid, mid, batch in (("o1", "mA", "b1"), ("o2", "mA", "scene_x"), ("scene_x", None, "scene_x"),
                            ("o3", None, "other")):
        made[oid] = _tone(out_dir / f"{oid}.wav", [(1.0, 0.3)])
        db.insert("outputs", {"id": oid, "model_id": mid, "text": "t", "path": str(made[oid]), "batch": batch,
                              "created_at": db.now()})
    (out_dir / "scene_x.json").write_text("[]", encoding="utf-8")
    db.insert("performances", {"id": "pf1", "name": "p", "path": "x", "status": "done", "params": {"model_id": "mA"},
                               "result": {}, "created_at": db.now()})
    db.insert("presets", {"id": "pr1", "name": "Nerissa", "source": "novel-lab", "model_id": "mA", "data": {},
                          "created_at": db.now()})
    colab_root = tmp_path / "drive"
    (colab_root / "VoiceStudio" / "jobs" / "tr_00c0").mkdir(parents=True)
    for tid, target, prefix, storage in (("tr_00a1", "runpod", "vs/jobs/tr_00a1",  # datacenter recorded wrongly
                                          {"volume": "vol1", "datacenter": "EU-RO-1"}),
                                         ("tr_00b2", "runpod", "vs/jobs/tr_00b2", {"volume": "vol1"}),
                                         ("tr_00d3", "runpod", "vs/jobs/tr_00d3", {"volume": "volGone"}),
                                         ("tr_00c0", "colab", "jobs/tr_00c0",
                                          {"drive_root": str(colab_root), "folder": "VoiceStudio"})):
        db.insert("trainings", {"id": tid, "voice_id": a["id"], "dataset_id": "dsA", "engine": "mock",
                                "preset": {"id": "lora", "name": "第一次"}, "target": target, "status": "done",
                                "remote_prefix": prefix, "storage": storage, "progress": {}, "created_at": db.now()})
        (config.DATA / "jobs" / tid).mkdir(parents=True, exist_ok=True)
    gone_cloud = []

    def delete_run_folder(prefix, loc=None):
        if prefix.endswith("tr_00b2"):
            raise runpod.RunPodError("An error occurred (AccessDenied) when calling the ListObjectsV2 operation")
        gone_cloud.append((prefix, loc["datacenter"]))
        return 3
    monkeypatch.setattr(runpod, "delete_run_folder", delete_run_folder)
    monkeypatch.setattr(runpod, "volumes", lambda: [{"id": "vol1", "dataCenterId": "US-CA-2"}])  # volGone was deleted

    plan = c.get(f"/api/voices/{a['id']}/delete-plan").json()
    n = plan["counts"]
    assert (n["recordings"], n["shared_recordings"], n["segments"], n["phrases"], n["sounds"]) == (1, 1, 2, 1, 1)
    assert (n["datasets"], n["models"], n["trainings"], n["cloud_runpod"], n["cloud_colab"]) == (1, 1, 4, 3, 1)
    assert n["outputs"] == 3 and n["performances"] == 1 and not plan["blockers"]   # o1, o2 and the scene mix

    job = db.insert("jobs", {"id": "job_imp", "kind": "import_delivery", "queue": "io", "status": "running",
                             "message": "匯入交付資料夾", "params": {"voice_id": a["id"]}, "created_at": db.now()})
    assert "匯入交付資料夾" in c.get(f"/api/voices/{a['id']}/delete-plan").json()["blockers"][0]
    assert c.delete(f"/api/voices/{a['id']}").status_code == 409                # a job still uses it
    db.update("jobs", job["id"], {"status": "done"})
    db.update("trainings", "tr_00a1", {"status": "running"})                         # still training: refused
    r = c.delete(f"/api/voices/{a['id']}")
    assert r.status_code == 409 and "還在進行" in r.json()["detail"] and db.get("voices", a["id"])
    db.update("trainings", "tr_00a1", {"status": "done"})

    res = c.delete(f"/api/voices/{a['id']}").json()
    assert res["ok"] and len(res["left"]) == 1 and "tr_00b2" in res["left"][0]     # refused access: listed, in words
    assert "S3 金鑰沒有這個網路磁碟的權限" in res["left"][0] and "volGone" in res["notes"][0]  # a gone volume: a note
    assert gone_cloud == [("vs/jobs/tr_00a1", "US-CA-2")]                            # in the volume's real datacenter
    assert not (colab_root / "VoiceStudio" / "jobs" / "tr_00c0").exists()
    assert db.get("voices", a["id"]) is None and not (config.DATA / "voices" / a["id"]).exists()
    for table, i in (("segments", own["id"]), ("segments", mine["id"]), ("sources", "own"), ("sound_finds", "sf1"),
                     ("catchphrases", ph["id"]), ("datasets", "dsA"), ("models", "mA"), ("trainings", "tr_00a1"),
                     ("outputs", "o1"), ("outputs", "o2"), ("outputs", "scene_x"), ("performances", "pf1")):
        assert db.get(table, i) is None, (table, i)
    assert not Path(own["path"]).exists() and not Path(mine["path"]).exists()
    assert not ds_dir.exists() and not m_dir.exists() and not made["o1"].exists() and not made["scene_x"].exists()
    assert not (out_dir / "scene_x.json").exists() and not (config.DATA / "jobs" / "tr_00a1").exists()
    # what stays: the other voice and its clip in the shared recording, an unrelated output, the outside original
    assert db.get("voices", b["id"]) and db.get("segments", theirs["id"]) and Path(theirs["path"]).exists()
    assert db.get("sources", "shared") and db.get("outputs", "o3") and made["o3"].exists() and outside.exists()
    assert db.get("presets", "pr1")["model_id"] is None


def test_cloud_run_folder_delete_stays_inside_the_run(monkeypatch):
    """Only one run's folder is ever deleted on the network volume, never the shared environments next to it."""
    from vstudio.cloud import runpod
    keys = {"vs/jobs/tr_ab12/dataset.tar", "vs/jobs/tr_ab12/train.log", "vs/jobs/tr_ab123/model.tar",
            "vs/envs/voxcpm2/bin/python", "vs/hf/model.bin"}

    class Pages:
        def paginate(self, Bucket, Prefix):
            return [{"Contents": [{"Key": k} for k in sorted(keys) if k.startswith(Prefix)]}]

    class Client:
        def get_paginator(self, name):
            return Pages()

        def delete_object(self, Bucket, Key):
            keys.discard(Key)
    monkeypatch.setattr(runpod, "s3", lambda loc=None, fast=False: Client())
    monkeypatch.setattr(runpod, "bucket", lambda loc=None: "vol1")
    for bad in ("vs/envs", "vs/jobs", "vs/jobs/", "vs", "", "vs/jobs/tr_ab12/../../envs", "jobs/tr_ab12"):
        with pytest.raises(runpod.RunPodError):
            runpod.delete_run_folder(bad)
    assert runpod.delete_run_folder("vs/jobs/tr_ab12/") == 2
    assert keys == {"vs/jobs/tr_ab123/model.tar", "vs/envs/voxcpm2/bin/python", "vs/hf/model.bin"}


def test_emotion_labels_flow(client, tmp_path):
    from vstudio import db
    c = client
    v = _consented_voice(c)
    db.insert("sources", {"id": "s1", "filename": "a.wav", "path": "a.wav", "status": "ready", "created_at": db.now()})
    d = tmp_path / "segs"
    d.mkdir()
    for i in range(6):
        _seg(db, v["id"], f"calm{i}", "今日は静かに話します", d)
    for i in range(3):
        _seg(db, v["id"], f"ang{i}", "もういい加減にして", d, emotion="angry")
    # a recording-level label follows to its segments, except ones a person labelled differently
    c.patch("/api/segments/calm0", json={"emotion": "happy"})
    r = c.patch("/api/sources/s1", json={"emotion": "neutral"}).json()
    assert r["emotion"] == "neutral"
    st = {s["id"]: s["emotion"] for s in db.query("SELECT id, emotion FROM segments")}
    assert st["calm1"] == "neutral" and st["calm0"] == "happy" and st["ang0"] == "angry"
    assert c.patch("/api/segments/calm1", json={"emotion": "furious"}).status_code == 400
    # filter, bulk, per-voice minutes
    assert c.get(f"/api/segments?voice_id={v['id']}&emotion=angry").json()["total"] == 3
    c.post("/api/segments/bulk", json={"ids": ["calm2"], "emotion": ""})
    assert c.get(f"/api/segments?voice_id={v['id']}&emotion=none").json()["total"] == 1
    vv = c.get(f"/api/voices/{v['id']}").json()
    assert vv["emotions"]["angry"] == 0.3 and vv["emotions"][""] == 0.1
    # datasets record the spread and keep one reference per labelled emotion
    ds = c.post("/api/datasets", json={"voice_id": v["id"], "name": "e"}).json()
    assert ds["meta"]["emotions"]["angry"] == 0.3
    ref_emotions = {r.get("emotion") for r in ds["meta"]["reference_items"]}
    assert {"angry", "happy", "neutral"} <= ref_emotions
    # synthesis picks the reference of the wanted mood
    from vstudio import tts
    m = {"path": str(tmp_path), "meta": {"references": [
        {"id": "ref0", "file": "a.wav", "text": "x", "emotion": "neutral"},
        {"id": "ref1", "file": "b.wav", "text": "y", "emotion": "angry"}]}}
    assert tts.reference(m, None, "angry")["id"] == "ref1"
    assert tts.reference(m, "ref0", "angry")["id"] == "ref0"      # an explicit choice wins
    assert tts.reference(m, "auto", "sad")["id"] == "ref0"        # nothing of that mood: the first one


def test_label_lists(client, tmp_path, monkeypatch):
    from vstudio import jobs, labels
    # file names: bracket tags, a label at the start, but not a word that merely contains one
    assert labels.from_filename("0815直播[生氣].mp4") == {"emotion": "angry"}
    assert labels.from_filename("【開心】【日文】雜談.wav") == {"emotion": "happy", "language": "ja"}
    assert labels.from_filename("talk (whispering).wav")["emotion"] == "whisper"
    assert labels.from_filename("生氣_0815.wav")["emotion"] == "angry"
    assert labels.from_filename("搞笑_0815.wav") == {} and labels.from_filename("happy birthday.mp4") == {}
    assert labels.resolve("a.wav", None, None, None, ["生氣"])[::2] == ("angry", "folder")
    # a CSV saved by Excel in the Traditional Chinese code page, with a title row above the header
    csv = "我的清單\n檔名,情緒,語言\nA.WAV,生氣,日文\nsub/b.mp4,happy,auto\nc.wav,發呆,火星文\n".encode("cp950")
    out = labels.parse_list(csv, "list.csv")
    assert out["rows"]["a.wav"] == {"emotion": "angry", "language": "ja"} and out["rows"]["b.mp4"] == {"emotion": "happy"}
    assert len(out["errors"]) == 2 and out["count"] == 3
    # the list beats the file name, the file name beats the folder, the folder beats the form
    assert labels.resolve("a.wav", out["rows"], "sad", None, ["開心"]) == ("angry", "ja", "list")
    assert labels.resolve("x[難過].wav", out["rows"], "neutral", None, ["開心"])[::2] == ("sad", "filename")
    assert labels.resolve("x.wav", out["rows"], "neutral", "en")[::2] == ("neutral", "form")
    with pytest.raises(ValueError):
        labels.parse_list("名字,心情\na,b\n".encode(), "x.csv")
    # the clips.csv the screening AI hands over (chapter 10) reads as a list: "none" means no label, mixed = auto
    ai = labels.parse_list("file,stream,lang,emotion,bgm\nclean/ja/angry/x1.wav,s,ja,angry,none\n"
                           "clean/mixed/none/x2.wav,s,mixed,none,low\n".encode(), "clips.csv")
    assert ai["errors"] == [] and ai["rows"] == {"x1.wav": {"emotion": "angry", "language": "ja"}, "x2.wav": {}}
    # and its folder layout labels files by itself: clean/<lang>/<emotion>/
    assert labels.resolve("x1.wav", None, None, None, ["ja", "angry"]) == ("angry", "ja", "folder")
    assert labels.resolve("x2.wav", None, None, None, ["mixed", "none"]) == (None, None, "")
    assert labels.resolve("x3.wav", None, None, None, ["bgm", "en", "soft"]) == ("soft", "en", "folder")

    monkeypatch.setattr(jobs, "submit", lambda *a, **k: None)
    c = client
    # Excel list uploaded on the import page, then used for the files that follow
    import openpyxl
    wb = openpyxl.Workbook()
    wb.active.append(["檔名", "情緒"])
    wb.active.append(["one.wav", "笑著說"])
    buf = io.BytesIO()
    wb.save(buf)
    r = c.post("/api/import-labels", files={"file": ("情緒清單.xlsx", buf.getvalue())}).json()
    assert r["count"] == 1 and r["emotions"] == {"laughing": 1}
    up = c.post("/api/sources/upload", files={"file": ("one.wav", b"RIFF")},
                data={"labels_id": r["id"], "process": "false", "emotion": "sad"}).json()
    assert up["source"]["emotion"] == "laughing" and up["label_from"] == "list"
    up = c.post("/api/sources/upload", files={"file": ("two.wav", b"RIFF")},
                data={"relpath": "錄音/開心/two.wav", "process": "false"}).json()
    assert up["source"]["emotion"] == "happy" and up["label_from"] == "folder"
    assert c.post("/api/sources/upload", files={"file": ("x.wav", b"RIFF")}, data={"labels_id": "../x"}).status_code == 400
    t = c.get("/api/import-labels/template.csv")
    assert t.content.startswith("\ufeff檔名".encode()) and labels.parse_list(t.content, "t.csv")["errors"] == []
    # a folder with a list inside and an emotion subfolder
    root = tmp_path / "rec"
    (root / "生氣").mkdir(parents=True)
    for f in ("a.wav", "plain.wav", "生氣/loud.wav", "x[難過].wav"):
        (root / f).write_bytes(b"RIFF")
    (root / "情緒清單.csv").write_text("檔名,情緒,語言\na.wav,開心,英文\n", encoding="utf-8-sig")
    r = c.post("/api/sources/import-path", json={"path": str(root)}).json()
    assert r["created"] == 4 and r["list"] == "情緒清單.csv" and r["labelled"] == {"list": 1, "folder": 1, "filename": 1}
    got = {s["filename"]: (s["emotion"], s["language"]) for s in r["sources"]}
    assert got == {"a.wav": ("happy", "en"), "plain.wav": (None, None), "loud.wav": ("angry", None),
                   "x[難過].wav": ("sad", None)}


def test_catchphrases(client, tmp_path):
    from vstudio import db, phrases
    c = client
    v = _consented_voice(c)
    db.insert("sources", {"id": "s1", "filename": "a.wav", "path": "a.wav", "status": "ready", "created_at": db.now()})
    d = tmp_path / "segs"
    d.mkdir()
    _seg(db, v["id"], "a", "やっほー、今日もやるよ", d)
    _seg(db, v["id"], "b", "ヤッホー！元気？", d, text_alt="ヤッホー！元気？", flags=["auto_approved", "spot_check"])
    _seg(db, v["id"], "c", "Let's gooo, okay", d)
    ph = c.post(f"/api/voices/{v['id']}/phrases", json={"text": "やっほー", "variants": ["ヤッホー"], "lang": "ja"}).json()
    en = c.post(f"/api/voices/{v['id']}/phrases", json={"text": "Let's gooo", "lang": "en"}).json()
    assert c.post(f"/api/voices/{v['id']}/phrases", json={"text": "やっほー"}).status_code == 400
    lst = {p["text"]: p for p in c.get(f"/api/voices/{v['id']}/phrases").json()}
    assert lst["やっほー"]["counts"] == {"segments": 1, "approved": 1, "other_spellings": 1}
    assert phrases.asr_prompt(v["id"], "ja") == "やっほー。" and phrases.asr_prompt(v["id"], "en") == "Let's gooo."
    # unify: both transcripts rewritten, automatic-review marks kept, not marked as a person's edit
    assert c.post(f"/api/phrases/{ph['id']}/unify").json()["changed"] == 1
    b = db.get("segments", "b")
    assert b["text"] == "やっほー！元気？" and b["text_alt"] == "やっほー！元気？" and b["edited"] == 0
    assert "auto_approved" in b["flags"] and "spot_check" in b["flags"]
    # English spellings match whole words, any case
    assert [h[2]["text"] for h in phrases.find("LET'S GOOO now", [en])] == ["Let's gooo"]
    assert phrases.find("Let's goooo", [en]) == []

    # original recordings: upload a file, cut one from a segment
    clip = _tone(tmp_path / "clip.wav", [(0.3, 0.0), (0.8, 0.3), (0.3, 0.0)], sr=48000)
    with open(clip, "rb") as fh:
        r = c.post(f"/api/phrases/{ph['id']}/clips", files={"file": ("clip.wav", fh, "audio/wav")}, data={"emotion": "happy"})
    assert r.status_code == 200, r.text
    clips = r.json()["clips"]
    assert len(clips) == 1 and 0.8 <= clips[0]["duration"] <= 0.95      # leading/trailing silence trimmed
    r = c.post(f"/api/phrases/{ph['id']}/clips", data={"segment_id": "a", "start": "0.0", "end": "1.0", "emotion": "angry"})
    assert r.status_code == 200 and len(r.json()["clips"]) == 2
    assert c.get(f"/api/phrases/{ph['id']}/clips/{clips[0]['id']}/audio").status_code == 200
    ph = phrases.get(ph["id"])
    assert phrases.pick_clip(ph, "angry")["emotion"] == "angry"
    assert phrases.pick_clip(ph, "sad")["emotion"] in ("happy", "angry")

    # the plan of a line: phrase recording + continuation; punctuation stays with the phrase
    parts = phrases.plan("やっほー！今日もやるよ。", [ph])
    assert [p["kind"] for p in parts] == ["clip", "tts"] and parts[0]["said"] == "やっほー！"
    assert phrases.plan("今日も、やっほー", [ph])[-1]["kind"] == "clip"
    assert phrases.plan("関係ない文", [ph]) == []

    # synthesis with the test engine: the recording is spliced in, and can be turned off
    m = c.post("/api/models/demo").json()
    db.update("models", m["id"], {"voice_id": v["id"]})
    out = c.post("/api/tts", json={"model_id": m["id"], "text": "やっほー！今日もやるよ", "emotion": "angry"}).json()
    o = out["outputs"][0]
    assert o["params"]["phrases"] and o["params"]["phrases"][0]["emotion"] == "angry" and o["params"]["emotion"] == "angry"
    only = c.post("/api/tts", json={"model_id": m["id"], "text": "やっほー"}).json()["outputs"][0]
    assert only["params"]["phrases"] and only["duration"] < 1.2               # just the recording
    off = c.post("/api/tts", json={"model_id": m["id"], "text": "やっほー！今日もやるよ", "phrases": False}).json()
    assert not off["outputs"][0]["params"]["phrases"]

    # how the model says each phrase on its own
    job = c.post(f"/api/voices/{v['id']}/phrases/check", json={"model_id": m["id"]}).json()
    j = _wait(c, job["id"])
    assert j["status"] == "done", j
    chk = phrases.get(ph["id"])["checks"][m["id"]]
    assert chk["output_id"] and chk["dur_ratio"] is not None
    # deleting a phrase removes its recordings
    folder = phrases._dir(ph)
    assert folder.exists()
    c.delete(f"/api/phrases/{ph['id']}")
    assert not folder.exists()


def test_splice_continues_from_the_recording(tmp_path, monkeypatch):
    """With an engine that can continue from a prompt, the text after a catchphrase is spoken as a continuation of
    the original recording (full-clone mode with the recording and what was said in it)."""
    monkeypatch.setenv("VSTUDIO_DATA", str(tmp_path / "data"))
    for m in [m for m in list(sys.modules) if m.startswith("vstudio")]:
        del sys.modules[m]
    from vstudio import tts
    from vstudio.engines.base import Synthesis
    clip = _tone(tmp_path / "clip.wav", [(0.6, 0.1)], sr=48000)
    calls = []

    class Eng:
        def synthesize(self, h, text, language=None, style="", mode="plain", reference=None, seed=None, **kw):
            calls.append({"text": text, "mode": mode, "ref": reference})
            return Synthesis(np.full(24000, 0.3, dtype=np.float32), 24000, {"checkpoint": "ck"})

    ph = {"id": "p", "voice_id": "v", "text": "やっほー", "variants": [], "clips": [{"id": "c1", "emotion": ""}]}
    monkeypatch.setattr(tts.phrases, "clip_path", lambda p, cid: clip)
    parts = tts.phrases.plan("前置き、やっほー！今日もやるよ", [ph])
    timbre = {"path": tmp_path / "ref.wav"}
    y, sr, info, used = tts._spliced(Eng(), {"checkpoint": "ck"}, parts, "ja", "plain", lambda e: None, timbre, 1,
                                     None, 0, ["plain", "ref", "hifi"])
    assert [c["mode"] for c in calls] == ["plain", "hifi"]
    assert calls[0]["text"] == "前置き、" and calls[1]["text"] == "今日もやるよ"
    assert calls[1]["ref"]["path"] == clip and calls[1]["ref"]["text"] == "やっほー！"
    assert calls[1]["ref"]["timbre_path"] == timbre["path"]
    assert sr == 24000 and used == [{"phrase": "やっほー", "clip": "c1", "emotion": ""}]
    # two synthesized seconds + the recording + punctuation pauses
    assert 2.5 < len(y) / sr < 3.2

    # a recording over 15 s is still played, but the words after it are not continued from it
    calls.clear()
    ph["clips"] = [{"id": "c1", "emotion": "", "duration": 20.0}]
    tts._spliced(Eng(), {"checkpoint": "ck"}, tts.phrases.plan("前置き、やっほー！今日もやるよ", [ph]), "ja", "plain",
                 lambda e: None, timbre, 1, None, 0, ["plain", "ref", "hifi"])
    assert [c["mode"] for c in calls] == ["plain", "plain"]


def test_colab_roundtrip(client, tmp_path):
    """Studio → synced Drive folder → runner (as on Colab, test engine) → Drive folder → studio installs the model."""
    import json
    import subprocess
    from vstudio import db
    from vstudio.cloud import colab

    c = client
    v, ds = _approved_dataset(c, tmp_path)
    drive = tmp_path / "MyDrive"
    drive.mkdir()
    st = c.post("/api/colab/setup", json={"drive_root": str(drive), "folder": "VoiceStudio"}).json()
    assert st["ok"] and st["notebook"]
    nb = json.loads((drive / "VoiceStudio" / colab.NOTEBOOK_NAME).read_text(encoding="utf-8"))
    assert nb["metadata"]["colab"]["gpuType"] == "A100" and 'runner["main"]' in "".join(nb["cells"][1]["source"])
    assert c.post("/api/colab/setup", json={"drive_root": str(drive), "folder": "a/b"}).status_code == 400

    body = {"dataset_id": ds["id"], "engine": "mock", "preset": "quick", "target": "colab"}
    plan = c.post("/api/training/plan", json=body).json()
    assert plan["estimate_usd"] == 0 and plan["gpu"] == "Colab" and plan["compute_units"]
    tr = c.post("/api/training", json=body).json()
    assert _wait(c, tr["job_id"])["status"] == "done"
    tid = tr["id"]
    assert db.get("trainings", tid)["status"] == "waiting"
    d = drive / "VoiceStudio" / "jobs" / tid
    for f in ("job.json", "dataset.tar", "config.json", "setup_env.sh", "train_entry.py", "vs_common.py"):
        assert (d / f).exists(), f
    row = next(t for t in c.get("/api/training").json() if t["id"] == tid)
    assert row["phase"]["label"] and row["colab_path"].endswith(colab.NOTEBOOK_NAME)

    def run_runner():
        code = (f"import runpy; r = runpy.run_path({str(drive / 'VoiceStudio' / 'colab_runner.py')!r}); "
                f"r['main'](folder='VoiceStudio', drive_root={str(drive)!r}, auto_disconnect=False)")
        env = {**os.environ, "VS_COLAB_LOCAL": str(tmp_path / "content"), "VS_MOCK_DELAY": "0"}
        return subprocess.run([sys.executable, "-c", code], env=env, timeout=300, capture_output=True, text=True)

    r = run_runner()
    assert r.returncode == 0, r.stdout + r.stderr
    done = json.loads((d / "done.json").read_text())
    assert done["rc"] == 0 and done["sizes"]["model.tar"] > 0 and (d / "claim.json").exists()
    colab.poll()
    tr = db.get("trainings", tid)
    assert tr["status"] in ("downloading", "done")
    assert _wait(c, tr["job_id"])["status"] == "done"
    tr = db.get("trainings", tid)
    assert tr["status"] == "done", tr
    m = db.query("SELECT * FROM models WHERE training_id=?", (tid,))[0]
    assert m["meta"]["checkpoint"] and (Path(m["path"]) / "samples").exists()
    assert not (d / "dataset.tar").exists() and not (d / "model.tar").exists() and (d / "train.log").exists()
    assert "packaged model.tar" in c.get(f"/api/training/{tid}").json()["log"]

    # a second run, cancelled before anyone runs it: the runner leaves it alone
    tr2 = c.post("/api/training", json=body).json()
    assert _wait(c, tr2["job_id"])["status"] == "done"
    c.post(f"/api/training/{tr2['id']}/cancel")
    d2 = drive / "VoiceStudio" / "jobs" / tr2["id"]
    assert db.get("trainings", tr2["id"])["status"] == "canceled" and (d2 / "cancel.json").exists()
    r = run_runner()
    assert r.returncode == 0 and not (d2 / "claim.json").exists()

    # a runtime that went silent: the run goes back to waiting so the notebook can be run again
    tr3 = c.post("/api/training", json=body).json()
    assert _wait(c, tr3["job_id"])["status"] == "done"
    d3 = drive / "VoiceStudio" / "jobs" / tr3["id"]
    (d3 / "claim.json").write_text(json.dumps({"gpu": "NVIDIA A100-SXM4-40GB"}))
    (d3 / "heartbeat.json").write_text(json.dumps({"t": 1.0}))
    colab.poll()
    t3 = db.get("trainings", tr3["id"])
    assert t3["status"] == "waiting" and "斷線" in t3["note"] and not (d3 / "claim.json").exists()


def _phrased(path: Path, parts: list[tuple[float, float, float, float]], sr: int = 48000) -> Path:
    """(start, end, f0, amplitude) voiced stretches with silence between them."""
    y = np.zeros(int(sr * (parts[-1][1] + 0.6)), dtype=np.float32)
    for a, b, f0, amp in parts:
        t = np.arange(int(sr * (b - a))) / sr
        ph = 2 * math.pi * np.cumsum(f0 * (1 + 0.04 * np.sin(2 * math.pi * 4 * t))) / sr
        y[int(sr * a): int(sr * a) + len(t)] = amp * (np.sin(ph) + 0.5 * np.sin(2 * ph) + 0.25 * np.sin(3 * ph)) / 1.75
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
        w.writeframes((y * 32767).astype("<i2").tobytes())
    return path


def test_perform_follows_a_recording(client, tmp_path, monkeypatch):
    """照著念: phrases and pauses from word times, delivery guesses, editing, rendering with the trained voice."""
    from vstudio import db, perform
    from vstudio.pipeline import asr
    c = client
    ref = _phrased(tmp_path / "ref.wav", [(0.4, 1.6, 150, 0.15), (2.4, 3.6, 150, 0.15), (4.6, 5.6, 210, 0.6),
                                          (6.4, 7.6, 150, 0.15)])
    words = [("今日は", 0.4, 0.9), ("いい天気。", 0.95, 1.6), ("散歩に", 2.4, 3.0), ("行こう", 3.05, 3.6),
             ("すごい！", 4.6, 5.6), ("ほんとに", 6.4, 7.6)]

    def fake_words(audio16k, name, language=None, device="auto"):
        assert abs(len(audio16k) / 16000 - 8.2) < 0.1
        return {"lang": "ja", "words": [{"word": w, "start": a, "end": b, "prob": 0.9} for w, a, b in words]}
    monkeypatch.setattr(asr, "transcribe_words", fake_words)

    # word grouping on its own: pauses, sentence ends, very long phrases
    sp = perform.split_phrases([{"word": w, "start": a, "end": b} for w, a, b in words])
    assert [p["text"] for p in sp] == ["今日はいい天気。", "散歩に行こう", "すごい！", "ほんとに"]
    long = [{"word": "あ", "start": i * 0.5, "end": i * 0.5 + 0.45 + (0.1 if i == 13 else 0)} for i in range(30)]
    assert all(p["end"] - p["start"] <= perform.MAX_PHRASE for p in perform.split_phrases(long))

    with open(ref, "rb") as fh:
        rec = c.post("/api/perform", files={"file": ("台詞.wav", fh, "audio/wav")}, data={"language": "ja"}).json()
    assert _wait(c, rec["job"]["id"])["status"] == "done"
    rec = c.get(f"/api/perform/{rec['id']}").json()
    assert rec["status"] == "ready" and rec["lang"] == "ja" and len(rec["phrases"]) == 4
    assert not Path(rec["path"]).exists()                           # the upload is decoded once, then removed
    p0, p2 = rec["phrases"][0], rec["phrases"][2]
    assert p0["pause"] == 0.8 and rec["phrases"][-1]["pause"] == 0.0
    assert {"loud", "high"} <= set(p2["tags"]) and p2["emotion"] == "excited" and "loud" in p2["style"]
    assert "大聲" in p2["labels"] and p0["emotion"] == ""
    assert c.get(f"/api/perform/{rec['id']}/phrase/2/source").status_code == 200

    # the person corrects the guesses
    r = c.patch(f"/api/perform/{rec['id']}", json={"phrases": [{"i": 0, "emotion": "sad", "style": "slow"},
                                                               {"i": 3, "skip": True}, {"i": 1, "pause": 1.5}]})
    assert r.status_code == 200 and r.json()["phrases"][0]["emotion"] == "sad"
    assert c.patch(f"/api/perform/{rec['id']}", json={"phrases": [{"i": 0, "emotion": "furious"}]}).status_code == 400

    # render with a trained voice (the test engine); the recording itself is never a voice prompt
    v = _consented_voice(c)
    m = c.post("/api/models/demo").json()
    db.update("models", m["id"], {"voice_id": v["id"]})
    before = len(db.query("SELECT id FROM outputs"))
    job = c.post(f"/api/perform/{rec['id']}/render", json={"model_id": m["id"], "takes": 2}).json()
    j = _wait(c, job["id"])
    assert j["status"] == "done", j
    rec = c.get(f"/api/perform/{rec['id']}").json()
    res = rec["result"]
    assert rec["status"] == "done" and len(res["phrases"]) == 3     # the skipped phrase is left out
    assert len(db.query("SELECT id FROM outputs")) == before + 1     # only the joined result, not every take
    assert all(0.8 <= s["stretch"] <= 1.25 for s in res["phrases"]) and res["phrases"][0]["emotion"] == "sad"
    out = db.get("outputs", res["output_id"])
    assert out["params"]["perform"] == rec["id"] and out["duration"] > 4
    assert c.get(f"/api/perform/{rec['id']}/phrase/0/output").status_code == 200
    # redo one phrase: the others are reused, the old result replaced
    job = c.post(f"/api/perform/{rec['id']}/render", json={"model_id": m["id"], "takes": 1, "only": [1]}).json()
    assert _wait(c, job["id"])["status"] == "done"
    res2 = c.get(f"/api/perform/{rec['id']}").json()["result"]
    assert res2["output_id"] != res["output_id"] and db.get("outputs", res["output_id"]) is None
    assert res2["phrases"][0]["match"] == res["phrases"][0]["match"]
    # a voice without consent cannot be used
    db.update("voices", v["id"], {"consent": {"agreed": False}})
    db.update("models", m["id"], {"engine": "voxcpm2"})
    assert c.post(f"/api/perform/{rec['id']}/render", json={"model_id": m["id"]}).status_code == 400
    c.delete(f"/api/perform/{rec['id']}")
    assert not perform.folder(rec["id"]).exists() and db.get("outputs", res2["output_id"]) is None


def test_audio_check_detectors():
    """The pieces of the pre-import check on signals with known answers (no speech detector needed)."""
    from vstudio import audiocheck as ac
    sr, rng = 48000, np.random.default_rng(1)
    t = np.arange(int(0.5 * sr)) / sr
    feats = lambda y: ac.block_features(y.astype(np.float32), sr)
    noise = 0.01 * rng.standard_normal(len(t))
    chord = sum(0.05 * np.sin(2 * np.pi * f * t) for f in (261.6, 329.6, 392.0)) * np.exp(-3 * t)
    hum = sum(0.02 * np.sin(2 * np.pi * 60 * k * t) / k for k in range(1, 6)) + 0.0005 * rng.standard_normal(len(t))
    fan = np.convolve(0.05 * rng.standard_normal(len(t)), np.ones(30) / 30, "same")
    clicks = 0.0005 * rng.standard_normal(len(t))
    for c in (0.05, 0.2, 0.35):
        clicks[int(c * sr): int(c * sr) + 200] += 0.3 * rng.standard_normal(200)
    assert ac.classify_block(feats(noise), -30, 0.0) == "noise"
    assert ac.classify_block(feats(chord), -30, 0.0) == "music"
    assert ac.classify_block(feats(hum), -30, 0.0) == "hum"
    assert ac.classify_block(feats(fan), -30, 0.0) == "noise"          # a fan's rumble is not mains hum
    assert ac.classify_block(feats(clicks), -30, 0.0) == "transient"
    assert ac.classify_block(feats(noise), -55, 0.0) == "quiet"
    assert ac.classify_block(feats(noise), -30, 0.6) == "voice"
    # bandwidth: a cliff at 4 kHz (phone) versus sound up to the top
    from scipy.signal import butter, sosfilt
    x = rng.standard_normal(sr * 4) * 0.1
    phone = sosfilt(butter(12, 4000, fs=sr, output="sos"), x)
    spec, freqs = ac.ltas(phone, sr, np.ones(395, dtype=bool))
    assert 3500 <= ac.cutoff(spec, freqs) <= 5000
    spec, freqs = ac.ltas(x, sr, np.ones(395, dtype=bool))
    assert ac.cutoff(spec, freqs) >= 23000
    # echo: a level that falls 60 dB in 0.2 s versus in 1 s, from the end of a phrase
    for rt, lo, hi in ((0.2, 0.1, 0.35), (1.0, 0.8, 1.3)):
        fdb = np.full(300, -80.0)
        fdb[:100] = -20.0
        fdb[100:] = np.maximum(-20 - 60 * np.arange(200) * 0.01 / rt, -80)
        assert lo <= ac.decay_time(fdb, 0.01, 1.0, 1.5, -80.0) <= hi
    assert ac.verdict([{"level": "pass"}, {"level": "unknown"}]) == "pass"
    assert ac.verdict([{"level": "pass"}, {"level": "warn"}]) == "warn"
    assert ac.verdict([{"level": "warn"}, {"level": "fail"}]) == "fail"


@needs_speech
def test_audio_check_flow(client, tmp_path):
    """Upload, check, hear a problem spot, import only what passed."""
    from vstudio import audio, db
    c = client
    x, sr = audio.load(Path(SAMPLE), 48000)
    gap = np.zeros(int(2.5 * sr), np.float32)
    speech = np.concatenate([x, gap, x, gap, x]) / max(1e-6, float(np.max(np.abs(x)))) * 0.5
    t = np.arange(len(speech)) / sr
    music = sum(np.sin(2 * np.pi * f * t) for f in (261.6, 329.6, 392.0)) * (0.5 + 0.5 * np.sin(2 * np.pi * 2 * t))
    loud_music = speech + 0.03 * music
    clipped = np.clip(speech * 4, -1, 1)
    files = {"music.wav": loud_music, "clipped.wav": clipped}
    b = c.post("/api/checks/batches").json()["id"]
    for name, y in files.items():
        audio.save(tmp_path / name, y.astype(np.float32), sr)
        with open(tmp_path / name, "rb") as fh:
            assert c.post("/api/checks/upload", files={"file": (name, fh, "audio/wav")}, data={"batch": b}).status_code == 200
    job = db.query("SELECT id FROM jobs WHERE kind='audio_check' ORDER BY created_at DESC LIMIT 1")[0]
    assert _wait(c, job["id"])["status"] == "done"
    batch = next(x for x in c.get("/api/checks").json() if x["id"] == b)
    items = {i["filename"]: i for i in batch["items"]}
    assert all(i["status"] == "done" for i in items.values())
    checks = {i: {k["key"]: k for k in items[i]["result"]["checks"]} for i in items}
    assert checks["music.wav"]["background"]["level"] == "fail" and checks["music.wav"]["background"]["ranges"]
    assert items["music.wav"]["verdict"] == "fail"
    assert checks["clipped.wav"]["clipping"]["level"] == "fail" and checks["clipped.wav"]["clipping"]["ranges"]
    a, e = checks["music.wav"]["background"]["ranges"][0]
    r = c.get(f"/api/checks/{items['music.wav']['id']}/audio?start={a}&end={e}")
    assert r.status_code == 200 and r.content[:4] == b"RIFF"
    assert len(c.get("/api/checks/criteria").json()) >= 8
    # import: the upload moves into the studio's sources; checking the folder in place does not copy
    r = c.post("/api/checks/import", json={"ids": [items["clipped.wav"]["id"]], "language": "en"}).json()
    assert r["created"] == 1
    src = db.query("SELECT * FROM sources WHERE filename='clipped.wav'")[0]
    assert "_uploads" in src["path"] and Path(src["path"]).exists() and src["language"] == "en"
    folder = tmp_path / "rec" / "生氣"
    folder.mkdir(parents=True)
    audio.save(folder / "a.wav", speech.astype(np.float32), sr)
    r = c.post("/api/checks/path", json={"path": str(tmp_path / "rec")}).json()
    assert r["count"] == 1
    job = db.query("SELECT id FROM jobs WHERE kind='audio_check' ORDER BY created_at DESC LIMIT 1")[0]
    assert _wait(c, job["id"])["status"] == "done"
    item = next(x for x in c.get("/api/checks").json() if x["id"] == r["batch"])["items"][0]
    assert item["status"] == "done" and item["copied"] == 0
    c.post("/api/checks/import", json={"ids": [item["id"]]})
    src = db.query("SELECT * FROM sources WHERE filename='a.wav'")[0]
    assert src["path"] == str(folder / "a.wav") and src["emotion"] == "angry"     # folder name still labels it
    # deleting a batch removes uploaded copies but never the user's own files
    c.delete(f"/api/checks/batch/{r['batch']}")
    c.delete(f"/api/checks/batch/{b}")
    assert (folder / "a.wav").exists() and Path(src["path"]).exists()
    assert not db.query("SELECT id FROM audio_checks")


def test_quiet_bgm_import(client, tmp_path):
    """bgm/ recordings: fine when the deep check finds the music 20 dB under the voice; imported with separation."""
    from vstudio import audiocheck, db
    ok = {"checks": [{"key": "background", "level": "fail"}, {"key": "noise", "level": "warn"},
                     {"key": "under", "level": "warn"}]}
    assert audiocheck.quiet_bgm(ok)
    assert not audiocheck.quiet_bgm({"checks": [{"key": "background", "level": "fail"}]})            # no deep check
    assert not audiocheck.quiet_bgm({"checks": [{"key": "under", "level": "fail"}]})                 # music too loud
    assert not audiocheck.quiet_bgm({"checks": [{"key": "under", "level": "pass"}, {"key": "clipping", "level": "fail"}]})
    f = tmp_path / "bgm.wav"
    f.write_bytes(b"RIFF")
    db.insert("audio_checks", {"id": "ac_1", "batch": "chk_1", "filename": "bgm.wav", "path": str(f), "root": None,
                               "copied": 0, "status": "done", "verdict": "fail", "result": ok, "meta": {},
                               "created_at": db.now()})
    item = client.get("/api/checks").json()[0]["items"][0]
    assert item["bgm_ok"] is True
    assert client.post("/api/checks/import", json={"ids": ["ac_1"], "separate": True}).json()["created"] == 1
    job = db.query("SELECT params FROM jobs WHERE kind='prepare_source'")[0]
    assert job["params"]["separate"] is True


def test_bulk_assign_and_delete(client, tmp_path):
    """Import page: say who speaks in many recordings at once, and delete many at once."""
    from vstudio import db, jobs
    c = client
    me, other = _consented_voice(c, "我"), _consented_voice(c, "朋友")
    d = tmp_path / "segs"
    d.mkdir()
    for sid, status in (("s1", "ready"), ("s2", "new")):
        db.insert("sources", {"id": sid, "filename": f"{sid}.wav", "path": str(tmp_path / f"{sid}.wav"),
                              "status": status, "meta": {"copied": False}, "created_at": db.now()})
    _seg(db, None, "a", "一", d, source_id="s1", status="pending")
    _seg(db, None, "b", "二", d, source_id="s1", status="pending")
    _seg(db, None, "x", "三", d, source_id="s1", status="rejected")       # marked as nobody's: stays so
    _seg(db, other["id"], "o", "四", d, source_id="s1", status="pending")  # someone else's: untouched
    r = c.post("/api/sources/bulk-assign", json={"ids": ["s1", "s2"], "voice_id": me["id"]}).json()
    assert r == {"segments": 2, "waiting": 1}
    got = {s["id"]: s["voice_id"] for s in db.query("SELECT id, voice_id FROM segments")}
    assert got == {"a": me["id"], "b": me["id"], "x": None, "o": other["id"]}
    assert db.get("sources", "s2")["voice_hint"] == me["id"]                # used when it gets processed
    assert c.post("/api/sources/bulk-assign", json={"ids": ["s1"], "voice_id": "nope"}).status_code == 400
    # deleting stops the waiting import job; a job that starts anyway finds nothing to do
    job = db.insert("jobs", {"id": "job_t", "kind": "prepare_source", "queue": "held", "status": "queued",
                             "params": {"source_id": "s2"}, "result": {}, "created_at": db.now()})
    assert c.post("/api/sources/bulk-delete", json={"ids": ["s1", "s2"]}).json()["deleted"] == 2
    assert not db.query("SELECT id FROM sources") and not db.query("SELECT id FROM segments")
    assert db.get("jobs", job["id"])["status"] == "canceled"
    assert jobs.run_inline("prepare_source", {"source_id": "s2"})["status"] == "done"


def test_auto_review_trusted(client, tmp_path):
    """Material already screened (by an AI or the person): one click approves it; only doubtful transcripts and
    plainly unusable clips are held back. No voiceprint needed, no spot checks."""
    from vstudio import db, jobs
    from vstudio.pipeline import autoreview
    v = _consented_voice(client)
    db.insert("sources", {"id": "s1", "filename": "a.wav", "path": "a.wav", "status": "ready", "created_at": db.now()})
    d = tmp_path / "segs"
    d.mkdir()
    _seg(db, v["id"], "ok", "今日はいい天気ですね", d, status="pending", seconds=3.0, snr=14.0, spk_sim=None)
    _seg(db, v["id"], "doubt", "今日はいい天気ですね", d, status="pending", seconds=3.0, asr_agree=0.7)
    _seg(db, v["id"], "laugh", "", d, status="pending", seconds=3.0)
    _seg(db, v["id"], "mine", "人が直した", d, status="pending", seconds=3.0, asr_agree=0.2, edited=1)
    r = client.post(f"/api/auto-review/{v['id']}", json={"profile": "trusted"}).json()
    j = _wait(client, r["id"])
    assert j["status"] == "done" and j["result"]["spot_checks"] == 0, j
    st = {s["id"]: s["status"] for s in db.query("SELECT id, status FROM segments")}
    assert st == {"ok": "approved", "doubt": "pending", "laugh": "rejected", "mine": "pending"}
    assert "auto_unsure" in db.get("segments", "doubt")["flags"]
    # the usual profiles still need a voiceprint and still check the speaker
    seg = {"text": "this is a fine line", "lang": "en", "duration": 3, "asr_agree": 1, "snr": 30, "spk_sim": None}
    assert autoreview.decide(seg, autoreview.PROFILES["balanced"], 0.62, None) == ("unsure", ["speaker"])
    assert autoreview.decide(seg, autoreview.PROFILES["trusted"], 0.62, None) == ("approve", [])
    assert jobs  # imported for the job handlers


def test_long_text_line_by_line(client):
    """Long text: up to 20,000 characters split into lines; each line's emotion beats its [tag], which beats the
    default; one line can be redone; the whole text comes out as one file."""
    from vstudio import db, perform
    c = client
    lines = perform.split_text("[excited] やっほー！今日はね、すごいニュースがあるの。えっと。聞いて聞いて！\n\n"
                               "これは秘密だよ…誰にも言わないでね。\nHello everyone. This is a test! Yes.")
    assert [l["text"] for l in lines] == ["[excited] やっほー！今日はね、すごいニュースがあるの。",
                                          "[excited] えっと。聞いて聞いて！", "これは秘密だよ…", "誰にも言わないでね。",
                                          "Hello everyone. This is a test! Yes."]
    assert [l["pause"] for l in lines] == [0.35, 0.8, 0.35, 0.8, 0.0]
    long = "。".join(["とても長い文章ですね"] * 40)
    assert all(len(l["text"]) <= 130 for l in perform.split_text("、".join([long] * 3)))
    assert c.post("/api/perform/text", json={"text": "あ" * 20001}).status_code == 400

    v = _consented_voice(c)
    m = c.post("/api/models/demo").json()
    db.update("models", m["id"], {"voice_id": v["id"]})
    d = c.post("/api/perform/text", json={"text": "[whispers] ひみつ、ひみつ、内緒の話。\n普通の文章です、こんにちは。\n"
                                                  "三番目の文章です、よろしく。", "language": "ja"}).json()
    assert d["status"] == "ready" and len(d["phrases"]) == 3 and d["meta"]["kind"] == "text"
    assert [x["id"] for x in c.get("/api/perform?kind=text").json()] == [d["id"]]
    assert all(x["id"] != d["id"] for x in c.get("/api/perform").json())        # not in 照著念's list
    c.patch(f"/api/perform/{d['id']}", json={"phrases": [{"i": 2, "emotion": "sad"}]})
    job = c.post(f"/api/perform/{d['id']}/render", json={"model_id": m["id"], "takes": 1, "emotion": "happy",
                                                         "keep_pauses": True, "match_timing": False,
                                                         "follow_level": False}).json()
    assert _wait(c, job["id"])["status"] == "done"
    res = c.get(f"/api/perform/{d['id']}").json()["result"]
    assert [l["emotion"] for l in res["phrases"]] == ["whisper", "happy", "sad"]
    assert db.get("outputs", res["output_id"])["params"]["perform"] == d["id"]
    job = c.post(f"/api/perform/{d['id']}/render", json={"model_id": m["id"], "takes": 1, "only": [1]}).json()
    assert _wait(c, job["id"])["status"] == "done"
    res2 = c.get(f"/api/perform/{d['id']}").json()["result"]
    assert res2["output_id"] != res["output_id"] and res2["phrases"][2]["emotion"] == "sad"
    r = c.put(f"/api/perform/{d['id']}/text", json={"text": "新しい一文です。もう一つの文です。"}).json()
    assert len(r["phrases"]) == 2 and r["result"] == {}


def test_sound_tags(client, tmp_path):
    """Breaths, sighs and panting: [tags] by their Chinese names, a scan of the voice's recordings for candidates,
    keeping one as the person's own recording of a sound tag, and playing it where the tag is written."""
    import soundfile as sf
    from scipy import signal
    from vstudio import config, db, perform, phrases, sounds
    from vstudio.engines.base import Engine
    c = client

    # tags by their Chinese / Japanese names steer the delivery; one-off sounds are not carried through a paragraph
    assert Engine().render_tags("[喘氣] はぁ…待って") == ("はぁ…待って", "breathless, panting")
    assert Engine().render_tags("[呢喃]ねえ")[1] == "murmuring softly, half to themself"
    assert [x["text"] for x in perform.split_text("[吸氣][whispers] ねえ、聞いて。これは秘密だよ。")] == \
        ["[吸氣][whispers] ねえ、聞いて。", "[whispers] これは秘密だよ。"]

    # a recording: breath before speech, a sigh in the transcript, panting, a wordless "んっ"
    v = _consented_voice(c)
    sr, rng = 48000, np.random.default_rng(3)
    t = lambda s: int(s * sr)  # noqa: E731
    x = (rng.standard_normal(t(10.5)) * 1e-4).astype(np.float32)
    tone = lambda a, b, amp=0.3: x.__setitem__(slice(t(a), t(b)), amp * np.sin(2 * np.pi * 200 * np.arange(t(b) - t(a)) / sr))  # noqa: E731
    bb, ba = signal.butter(2, [400 / (sr / 2), 2600 / (sr / 2)], "band")
    def breath(a, b, rel_db):
        n = t(b) - t(a)
        z = signal.lfilter(bb, ba, rng.standard_normal(n)) * np.sin(np.linspace(0, np.pi, n)) ** 0.7
        x[t(a):t(b)] = z / np.sqrt(np.mean(z ** 2)) * 0.3 / np.sqrt(2) * 10 ** (rel_db / 20)
    breath(1.0, 1.6, -18)
    tone(1.7, 3.7)
    for k in range(4):
        breath(4.7 + 0.45 * k, 4.95 + 0.45 * k, -14)
    tone(6.6, 7.6)
    tone(8.6, 9.4, 0.2)
    db.insert("sources", {"id": "s1", "filename": "a.wav", "path": "a.wav", "status": "ready", "voice_hint": v["id"],
                          "created_at": db.now()})
    master = config.DATA / "sources" / "s1" / "master.wav"
    master.parent.mkdir(parents=True)
    sf.write(str(master), x, sr)
    d = tmp_path / "segs"
    d.mkdir()
    for sid, a, b, text in (("A", 1.6, 3.8, "こんにちは、今日は"), ("B", 6.5, 7.7, "はぁ…疲れた"), ("C", 8.5, 9.5, "んっ")):
        sf.write(str(d / f"{sid}.wav"), x[t(a):t(b)], sr)
        db.insert("segments", {"id": sid, "source_id": "s1", "voice_id": v["id"], "start": a, "end": b,
                               "path": str(d / f"{sid}.wav"), "duration": b - a, "text": text, "text_alt": text,
                               "lang": "ja", "asr_agree": 1.0, "snr": 40.0, "clip": 0.0, "score": 0.9,
                               "status": "rejected" if sid == "C" else "approved", "flags": []})
    assert sounds.text_kind("はぁ…疲れた") == "sigh" and sounds.text_kind("はぁ、はぁ、はぁ") == "pant"
    assert sounds.wordless("んっ…") and sounds.wordless("mm, ah") and not sounds.wordless("はい") \
        and not sounds.wordless("home")

    job = c.post(f"/api/voices/{v['id']}/sounds/scan").json()
    assert _wait(c, job["id"])["status"] == "done"
    res = c.get(f"/api/voices/{v['id']}/sounds").json()
    assert {k: res["counts"].get(k, 0) > 0 for k in ("breath", "pant", "sigh", "voice")} == \
        {"breath": True, "pant": True, "sigh": True, "voice": True}, res["counts"]
    br = next(f for f in res["items"] if f["kind"] == "breath")
    assert 0.9 <= br["start"] <= 1.1 and 1.5 <= br["end"] <= 1.7 and br["meta"]["where"] == "before"
    pant = next(f for f in res["items"] if f["kind"] == "pant")
    assert pant["start"] < 4.8 and pant["end"] > 6.0
    wav = c.get(f"/api/sounds/{br['id']}/audio")
    assert wav.status_code == 200 and abs(sf.info(io.BytesIO(wav.content)).duration - (br["clip_end"] - br["clip_start"])) < 0.05

    # keep the breath as [吸氣] (a new sound tag); dismiss the panting; neither comes back on a new scan
    r = c.post(f"/api/sounds/{br['id']}/keep", json={"tag": "［吸氣］"})
    assert r.status_code == 200, r.text
    ph = r.json()
    assert ph["text"] == "[吸氣]" and len(ph["clips"]) == 1 and ph["clips"][0]["speech_rms"] > 0
    c.post(f"/api/sounds/{pant['id']}/dismiss")
    job = c.post(f"/api/voices/{v['id']}/sounds/scan").json()
    assert _wait(c, job["id"])["status"] == "done"
    again = c.get(f"/api/voices/{v['id']}/sounds").json()
    assert not again["counts"].get("pant") and not any(f["kind"] == "breath" and f["start"] < 2 for f in again["items"])
    assert c.get(f"/api/voices/{v['id']}/sounds?status=kept").json()["items"][0]["meta"]["phrase"] == ph["id"]

    # a sound tag is not a catchphrase: no speech-recognition hint, no counts, matched only as a tag
    assert c.post(f"/api/voices/{v['id']}/phrases", json={"text": "[吸氣]"}).status_code == 400
    hello = phrases.create(v["id"], "hello")
    assert phrases.asr_prompt(v["id"], "en") == "hello."
    assert [h[2]["text"] for h in phrases.find("[ 吸氣 ] [hello there] hello", [phrases.get(ph["id"]), hello])] == \
        ["[吸氣]", "hello"]
    assert phrases.create(v["id"], "[喘氣]", variants=["panting"])["variants"] == ["[panting]"]

    # synthesis: the tag plays the recording (not also a style hint); an unregistered tag stays a style hint
    m = c.post("/api/models/demo").json()
    db.update("models", m["id"], {"voice_id": v["id"]})
    o = c.post("/api/tts", json={"model_id": m["id"], "text": "[吸氣] こんにちは [嘆氣]"}).json()["outputs"][0]
    assert o["params"]["phrases"] == [{"phrase": "[吸氣]", "clip": ph["clips"][0]["id"], "emotion": "", "sound": True}]
    assert o["params"]["style"] == "with a sigh"
    alone = c.post("/api/tts", json={"model_id": m["id"], "text": "[吸氣]"}).json()["outputs"][0]
    assert alone["params"]["phrases"] and alone["duration"] < 1.0

    # level: a kept sound keeps its level next to speech; an uploaded one is only turned down
    y = np.full(4800, 0.05, np.float32)
    near = [np.full(4800, 0.2, np.float32)]
    assert abs(float(phrases.match_level(y, 48000, near, {"speech_rms": 0.4}).max()) - 0.025) < 1e-3
    assert float(phrases.match_level(y, 48000, near, {}).max()) == pytest.approx(0.05)
    assert float(phrases.match_level(np.full(4800, 0.5, np.float32), 48000, near, {}).max()) == pytest.approx(0.2)

    # deleting the recording removes its candidates
    c.delete("/api/sources/s1")
    assert not db.query("SELECT 1 FROM sound_finds")


def test_tag_catalogue_and_pieces(client, tmp_path):
    """Every tag by any of its names; tags apply to the text after them; pauses are silence; the nearest mood is
    used when there is no reference or recording of the wanted one; the reference page and the UI stay in step."""
    import re as _re
    from vstudio import db, emotions, labels, phrases, sounds, tags, tts
    root = Path(__file__).resolve().parents[1]

    # the catalogue: valid labels, one meaning per name, the docs page and the interface list in step
    seen = {}
    for t in tags.CATALOGUE:
        assert t.group in tags.GROUPS and (t.emotion is None or t.emotion in emotions.EMOTIONS), t
        for n in (t.key, t.zh, *t.names):
            assert seen.setdefault(tags._norm(n), t.key) == t.key, (n, t.key, seen[tags._norm(n)])
    assert len(tags.CATALOGUE) >= 150
    doc = (root / "docs" / "14-tags.md").read_text(encoding="utf-8")
    assert doc.split("<!-- tags:start -->\n")[1].split("<!-- tags:end -->")[0] == tags.markdown()
    ui = (root / "web" / "src" / "api.ts").read_text(encoding="utf-8")
    block = ui.split("export const EMOTIONS")[1].split("];")[0]
    assert _re.findall(r'\["(\w+)", "', block) == list(emotions.EMOTIONS)
    assert c_get(client, "/api/tags")["groups"][0]["tags"][0]["key"] == tags.CATALOGUE[0].key

    # names in three languages, pauses with seconds, free descriptions
    assert tags.lookup("照れて").key == tags.lookup("害羞").key == tags.lookup("Embarrassed").key == "embarrassed"
    assert tags.lookup("ドヤ顔").emotion == "smug" and tags.lookup("はぁはぁ").key == "panting"
    assert [tags.pause_seconds(x) for x in ("pause", "間", "停頓 1.5秒", "pause 2s", "1.2秒", "長停頓", "開心")] == \
        [0.5, 0.5, 1.5, 2.0, 1.2, 1.2, None]
    assert tags.style_of("like a pirate") == "like a pirate" and not tags.is_event("like a pirate")
    assert labels.emotion_of("照れて") == "embarrassed" and labels.emotion_of("不耐煩") == "annoyed"
    assert emotions.from_text_tags("[照れて] もう…") == "embarrassed"

    # a line in pieces: each tag rules the text after it; ways of speaking carry on, sounds and pauses do not
    parts = tts.compose("[happy] やった！[sad] でも…[pause 1s][sighs] まあいいか [laughs]", [])
    assert [p["kind"] for p in parts] == ["tts", "tts", "pause", "tts"]
    assert [p.get("emotion") for p in parts] == ["happy", "sad", None, "sad"]
    assert parts[0]["style"] == "happy, cheerful" and parts[2]["seconds"] == 1.0
    assert parts[3]["style"] == "with a sigh, sad, subdued, with a laugh"     # the trailing [laughs] colours it
    assert [p["text"] for p in parts if p["kind"] == "tts"] == ["やった！", "でも…", "まあいいか"]
    assert {p.get("emotion") for p in tts.compose("[happy] あ [sad] い", [], emotion="angry") if p["kind"] == "tts"} \
        == {"angry"}                                                         # the line's own choice wins
    assert tts.compose("[whispers] ねえ [sighs] 聞いて", [])[1]["style"] == "with a sigh, whispering"
    snd = {"id": "p", "text": "[喘氣]", "variants": [], "clips": [{"id": "c", "emotion": ""}]}
    assert [p["kind"] for p in tts.compose("[panting] 待って", [snd])] == ["clip", "tts"]
    assert tts.compose("[はぁはぁ]", [snd])[0]["phrase"] is snd

    # the nearest mood: an embarrassed line takes the soft reference, a recording falls back the same way
    m = {"path": str(tmp_path), "meta": {"references": [{"id": "r_n", "file": "a.wav", "emotion": "neutral"},
                                                        {"id": "r_s", "file": "b.wav", "emotion": "soft"}]}}
    assert tts.reference(m, None, "embarrassed")["id"] == "r_s" and tts.reference(m, None, "angry")["id"] == "r_n"
    ph = {"clips": [{"id": "a", "emotion": "angry"}, {"id": "b", "emotion": "happy"}]}
    assert phrases.pick_clip(ph, "annoyed")["id"] == "a" and phrases.pick_clip(ph, "excited")["id"] == "b"

    # synthesis: pieces joined, a real pause in between
    v = _consented_voice(client)
    mo = client.post("/api/models/demo").json()
    db.update("models", mo["id"], {"voice_id": v["id"]})
    one = client.post("/api/tts", json={"model_id": mo["id"], "text": "やった！でも…", "takes": 1}).json()["outputs"][0]
    two = client.post("/api/tts", json={"model_id": mo["id"], "text": "[happy] やった！[停頓 1.5秒][sad] でも…",
                                        "takes": 1}).json()["outputs"][0]
    assert one["params"]["pieces"] == 1 and two["params"]["pieces"] == 3 and two["params"]["emotion"] == "happy"
    assert two["duration"] > one["duration"] + 1.2
    assert client.post("/api/tts", json={"model_id": mo["id"], "text": "[sighs]"}).status_code == 400

    # transcripts: English descriptions and interjections, Japanese and Chinese sounds
    kinds = {x: sounds.text_kind(x) for x in ("(laughs) no way", "*sighs*", "[Laughter]", "(clears throat) So",
                                             "Ugh.", "Achoo!", "Pfft", "ゴホッゴホッ", "くしゅん", "唉，算了",
                                             "she sighed and left", "うーん、どうだろう")}
    assert kinds == {"(laughs) no way": "laugh", "*sighs*": "sigh", "[Laughter]": "laugh",
                     "(clears throat) So": "throat", "Ugh.": "groan", "Achoo!": "sneeze", "Pfft": "scoff",
                     "ゴホッゴホッ": "cough", "くしゅん": "sneeze", "唉，算了": "sigh", "she sighed and left": None,
                     "うーん、どうだろう": None}
    assert sounds.wordless("(laughs)") and sounds.wordless("mm-hmm") and not sounds.wordless("home")
    assert all(tags.lookup(sug[1:-1]) for _, sug in sounds.KINDS.values() if sug)


def c_get(c, url):
    r = c.get(url)
    assert r.status_code == 200, r.text
    return r.json()


def test_sound_recording_check(client, tmp_path):
    """Recordings for sound tags are measured on upload (clipping, level, background, bandwidth, format, length);
    the emotion can come from the file name; the spec page names only tags the catalogue knows."""
    import re as _re
    import soundfile as sf
    from scipy import signal
    from vstudio import audio, phrases, tags
    c = client
    v = _consented_voice(c)
    ph = c.post(f"/api/voices/{v['id']}/phrases", json={"text": "[嘆氣]"}).json()
    rng = np.random.default_rng(5)
    sr = 48000
    def sigh(peak, noise=1e-4, dur=1.0, lo=300, hi=6000, rate=sr):
        n = int(rate * dur)
        bb, ba = signal.butter(2, [lo / (rate / 2), hi / (rate / 2)], "band")
        z = signal.lfilter(bb, ba, rng.standard_normal(n)) * np.sin(np.linspace(0, np.pi, n)) ** 0.7
        quiet = rng.standard_normal(int(rate * 0.4)) * noise
        y = np.concatenate([quiet, z / np.abs(z).max() * peak, quiet]).astype(np.float32)
        return y
    def up(name, y, rate=sr, **form):
        p = tmp_path / name
        sf.write(str(p), y, rate)
        with open(p, "rb") as fh:
            r = c.post(f"/api/phrases/{ph['id']}/clips", files={"file": (name, fh, "audio/wav")}, data=form)
        assert r.status_code == 200, r.text
        return r.json()["clips"][-1]

    good = up("tired_01.wav", sigh(0.3), emotion_from_name="true")
    assert good["check"]["warnings"] == [] and good["emotion"] == "tired"
    assert good["check"]["floor_db"] is not None and good["check"]["floor_db"] < -60
    named = up("[害羞] 2.wav", sigh(0.3), emotion_from_name="true", emotion="sad")
    plain = up("take3.wav", sigh(0.3), emotion_from_name="true", emotion="sad")
    assert named["emotion"] == "embarrassed" and plain["emotion"] == "sad"
    clipped = sigh(1.0)
    clipped = np.clip(clipped * 1.6, -1, 1)
    assert any("爆音" in w for w in up("hot.wav", clipped)["check"]["warnings"])
    assert any("太小聲" in w for w in up("faint.wav", sigh(0.01, noise=1e-6))["check"]["warnings"])
    assert any("背景噪音" in w for w in up("fan.wav", sigh(0.3, noise=0.01))["check"]["warnings"])
    assert any("取樣率" in w for w in up("phone.wav", sigh(0.3, hi=3500, rate=8000), rate=8000)["check"]["warnings"])
    def brickwall(y, hz):  # what a lossy codec or a phone line leaves: nothing above a hard edge
        f = np.fft.rfft(y)
        f[np.fft.rfftfreq(len(y), 1 / sr) > hz] = 0
        return np.fft.irfft(f, len(y)).astype(np.float32)
    assert any("高頻" in w for w in up("muffled.wav", brickwall(sigh(0.3, hi=12000), 7000))["check"]["warnings"])
    assert any("有點長" in w for w in up("long.wav", sigh(0.3, dur=7.0))["check"]["warnings"])
    # a catchphrase recording gets the same measurements, but no length note
    word = phrases.check_clip(sigh(0.3, dur=7.0), sr, sound=False)
    assert not any("有點長" in w for w in word["warnings"])

    doc = (Path(__file__).resolve().parents[1] / "docs" / "15-sound-recording.md").read_text(encoding="utf-8")
    named_tags = set(_re.findall(r"`\[([^\]`]+)\]`", doc))
    assert named_tags and all(tags.lookup(t) for t in named_tags), [t for t in named_tags if not tags.lookup(t)]
    assert audio.MASTER_SR == sr


def _tone_file(path: Path, seconds: float, sr: int = 44100, f0: float = 180.0) -> Path:
    t = np.arange(int(sr * seconds)) / sr
    y = 0.25 * np.sin(2 * math.pi * f0 * t) * (0.6 + 0.4 * np.sin(2 * math.pi * 3 * t))
    y += 0.002 * np.random.default_rng(1).standard_normal(len(t))
    path.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
        w.writeframes((np.clip(y, -1, 1) * 32767).astype("<i2").tobytes())
    return path


def _delivery_folder(root: Path) -> Path:
    """A small delivery folder in the agreed layout (交付 / 常用語 / 素材庫)."""
    p = root / "EN" / "Gen X" / "Alice"
    d = p / "交付"
    rows = [("clean/en/happy/20250101_vidA_10.00-12.00.wav", "Hello there friends"),
            ("clean/en/angry/20250101_vidA_20.00-22.50.wav", "Why would you do that"),
            ("clean/ja/neutral/20250102_vid-B_c_5.00-7.00.wav", "今日はいい天気です"),
            ("bgm/en/sad/20250103_vidC_1.00-3.00.wav", "I miss it already"),
            ("bgm/en/neutral/20250103_vidC_30.00-32.00.wav", "Okay let's go on")]
    for f, _ in rows:
        a, b = [float(x) for x in f.rsplit("_", 1)[1][:-4].split("-")]
        _tone_file(d / f, b - a)
    _tone_file(d / "clean_去背景音樂/en/sad/20250103_vidC~sep_1.00-3.00.wav", 2.0, f0=200)
    (d / "clips.csv").write_text("file,stream,date,url,start,end,lang,emotion,bgm,transcript,notes\n" + "".join(
        f"{f},s,20250101,https://youtu.be/x,0,1,{f.split('/')[1]},{f.split('/')[2]},{'yes' if f.startswith('bgm') else 'no'},{t},\n"
        for f, t in rows), encoding="utf-8-sig")
    _tone_file(d / "phrases/yippee/happy_20250101_vidA_40.00-40.80.wav", 0.8)
    _tone_file(d / "phrases/yippee/excited_20250102_vid-B_c_9.00-9.70.wav", 0.7)
    (d / "phrases.csv").write_text("phrase,variants,kind,lang,count,file,emotion\n"
                                   "yippee,yipee|yippie,口頭禪,en,2,phrases/yippee/happy_20250101_vidA_40.00-40.80.wav,happy\n",
                                   encoding="utf-8")
    c = p / "常用語"
    _tone_file(c / "原音/開場招呼/001_Hello everyone/neutral_20250101_vidA_0.50-2.00.wav", 1.5)
    _tone_file(c / "原音/開場招呼/001_Hello everyone/neutral_20250104_vidD_0.40-1.90.wav", 1.5)
    _tone_file(c / "已去背景音樂/開場招呼/001_Hello everyone/neutral_20250104_vidD_0.40-1.90.wav", 1.5, f0=210)
    _tone_file(c / "原音/口頭禪/002_Cut off/happy_20250105_vidE_3.00-4.00.wav", 1.0)
    _tone_file(c / "原音/口頭禪/003_Hello there/happy_20250101_vidA_10.20-11.90.wav", 1.7)
    # as delivered: the file column is 檔案 (6th), a path from 常用語\ (the same file name under 原音 and 已去背景音樂)
    h = "原音/開場招呼/001_Hello everyone"
    (c / "常用語.csv").write_text(
        "編號,類型,原文,中文意思,處理方式,檔案,情緒,語言,句子完整度,聲紋相似度\n"
        f"001,開場招呼,Hello everyone!,大家好,原音,{h}/neutral_20250101_vidA_0.50-2.00.wav,neutral,en,完整,0.91\n"
        f"001,開場招呼,Hello everyone!,大家好,原音,{h}/neutral_20250104_vidD_0.40-1.90.wav,neutral,en,完整,0.88\n"
        "001,開場招呼,Hello everyone!,大家好,已去背景音樂,"
        "已去背景音樂/開場招呼/001_Hello everyone/neutral_20250104_vidD_0.40-1.90.wav,neutral,en,完整,0.86\n"
        "002,口頭禪,Cut off line,斷掉,原音,原音/口頭禪/002_Cut off/happy_20250105_vidE_3.00-4.00.wav,happy,en,不完整,0.80\n"
        "003,口頭禪,Hello there,你好,原音,原音/口頭禪/003_Hello there/happy_20250101_vidA_10.20-11.90.wav,happy,en,完整,0.90\n",
        encoding="utf-8-sig")
    m = p / "素材庫"
    _tone_file(m / "原音/聲音/笑聲/20250101_vidA_50.00-50.80.wav", 0.8)
    _tone_file(m / "原音/聲音/呼吸/20250101_vidA_60.00-60.60.wav", 0.6)
    _tone_file(m / "原音/情緒/開心/20250101_vidA_70.00-72.00.wav", 2.0)
    (m / "tags.csv").write_text("file,處理方式,大類,標籤,長度,文字\n"
                                "原音/情緒/開心/20250101_vidA_70.00-72.00.wav,原音,情緒,開心,2.0,This is so fun\n"
                                "原音/聲音/笑聲/20250101_vidA_50.00-50.80.wav,原音,聲音,笑聲,0.8,\n", encoding="utf-8")
    (p / "delivered.json").write_text("{}", encoding="utf-8")
    return p


def test_delivery_import(client, tmp_path):
    from vstudio import delivery
    assert delivery.parse_name("20250102_vid-B_c_5.00-7.00") == {
        "emo": "", "date": "20250102", "vid": "vid-B_c", "sep": False, "start": 5.0, "end": 7.0}
    assert delivery.parse_name("happy_20250103_vidC~sep_1.00-3.00")["sep"] is True
    assert not delivery.is_complete("不完整") and delivery.is_complete("") and not delivery.is_complete("0.5")
    # CSV rows by path from the CSV's folder; a file name shared by two folders is never matched by name alone
    rows = delivery.by_file([{"檔案": "原音\\a\\x.wav", "n": "1"}, {"檔案": "已去背景音樂/a/x.wav", "n": "2"},
                             {"檔案": "y.wav", "n": "3"}])
    base = tmp_path / "常用語"
    assert delivery.row_for(rows, base, base / "已去背景音樂" / "a" / "x.wav")["n"] == "2"
    assert delivery.row_for(rows, base, base / "原音" / "a" / "x.wav")["n"] == "1"
    assert delivery.row_for(rows, base, base / "原音" / "b" / "x.wav") == {}
    assert delivery.row_for(rows, base, base / "原音" / "b" / "y.wav")["n"] == "3"

    c = client
    person = _delivery_folder(tmp_path / "交付總覽")
    v = c.post("/api/voices", json={"name": "alice", "kind": "other", "languages": ["en", "ja"]}).json()

    s = c.post("/api/delivery/scan", json={"path": str(tmp_path / "交付總覽")}).json()
    assert [x["name"] for x in s["people"]] == ["Alice"]
    a = s["people"][0]
    assert a["group"] == "EN / Gen X"
    assert a["voice"] == {"id": v["id"], "name": "alice", "consent_ok": False}
    assert a["delivery"]["clean"]["count"] == 3 and a["delivery"]["bgm"]["count"] == 2 and a["delivery"]["sep"]["count"] == 1
    # 5 delivery clips (the bgm clip with a music-removed copy counts once), 2 common phrases (the cut-off one and the
    # one overlapping a delivery clip are left out), 1 library clip with text
    assert a["training"]["count"] == 8, a["training"]
    assert a["training"]["skipped"]["incomplete"] == 1 and a["training"]["skipped"]["duplicate"] == 1
    assert a["phrases"]["count"] == 4 and a["sounds"]["names"] == ["[呼吸]", "[笑聲]"]

    # no consent, no import
    r = c.post("/api/delivery/import", json={"path": str(person), "voice_id": v["id"]})
    assert r.status_code == 409
    c.post(f"/api/voices/{v['id']}/consent", data={"signed_name": "Alice", "date": "2026-11-08", "agreed": "true",
                                                  "scope": "train,generate", "document_note": "signed copy in drawer"})
    assert c.post("/api/delivery/import", json={"path": str(tmp_path), "voice_id": v["id"]}).status_code == 400

    j = _wait(c, c.post("/api/delivery/import", json={"path": str(person), "voice_id": v["id"]}).json()["id"])
    assert j["status"] == "done", j
    res = j["result"]
    assert res["added"] == 8 and res["dataset_id"], res
    segs = c.get(f"/api/segments?voice_id={v['id']}&limit=100").json()
    segs = segs["items"] if isinstance(segs, dict) else segs
    by_text = {x["text"]: x for x in segs}
    assert by_text["Hello there friends"]["emotion"] == "happy" and by_text["Hello there friends"]["lang"] == "en"
    assert by_text["今日はいい天気です"]["lang"] == "ja"
    sad = by_text["I miss it already"]
    assert "separated" in sad["flags"] and sad["emotion"] == "sad"            # the music-removed copy was used
    assert "bgm" in by_text["Okay let's go on"]["flags"]                       # no copy: the original, flagged
    assert by_text["This is so fun"]["emotion"] == "happy"                     # library tag 開心 → happy
    assert "Cut off line" not in by_text
    assert all(x["status"] == "approved" for x in segs)
    srcs = {x["source_id"] for x in segs}
    assert len(srcs) == 4                                                      # one recording per stream: A, B, C, D
    ds = [d for d in c.get(f"/api/datasets?voice_id={v['id']}").json() if d["id"] == res["dataset_id"]][0]
    assert ds["n_items"] == 8

    ph = {p["text"]: p for p in c.get(f"/api/voices/{v['id']}/phrases").json()}
    assert sorted(ph) == ["Hello everyone!", "Hello there", "[呼吸]", "[笑聲]", "yippee"]
    assert len(ph["yippee"]["clips"]) == 2 and ph["yippee"]["variants"] == ["yipee", "yippie"]
    assert {x["emotion"] for x in ph["yippee"]["clips"]} == {"happy", "excited"}
    assert len(ph["Hello everyone!"]["clips"]) == 2                            # vidA, and vidD once (not twice)
    assert len(ph["[笑聲]"]["clips"]) == 1

    # a second import of the same folder adds nothing and keeps what was there
    j2 = _wait(c, c.post("/api/delivery/import", json={"path": str(person), "voice_id": v["id"], "build": False}).json()["id"])
    assert j2["result"]["added"] == 0 and j2["result"]["phrase_clips"] == 0
    assert c.post(f"/api/sources/{segs[0]['source_id']}/process", json={}).status_code == 400


def test_voice_manager_button(client, tmp_path, monkeypatch):
    from vstudio import launcher
    c = client
    vm = tmp_path / "HololiveVoiceManager"
    (vm / "app").mkdir(parents=True)
    for f in ("Start Manager.bat", "install.bat", "readme.txt", "app/VoiceManager.exe"):
        (vm / f).write_text("x", encoding="utf-8")
    monkeypatch.setattr(launcher, "DEFAULT_DIR", vm)
    opened: list[str] = []
    monkeypatch.setattr(launcher, "launch", lambda t: opened.append(t))

    s = c.get("/api/launcher/voice-manager").json()
    assert s["resolved"] is None and s["target"] == ""
    assert s["candidates"] == [str(vm / "Start Manager.bat"), str(vm / "app" / "VoiceManager.exe")]  # no installer
    assert c.post("/api/launcher/voice-manager/open", json={}).status_code == 409   # nothing chosen yet
    assert c.post("/api/launcher/voice-manager/open", json={"target": str(vm / "readme.txt")}).status_code == 400

    r = c.post("/api/launcher/voice-manager/open", json={"target": f'"{vm / "Start Manager.bat"}"'}).json()
    assert r["url"] is None and opened == [str(vm / "Start Manager.bat")]
    assert c.get("/api/launcher/voice-manager").json()["resolved"] == str(vm / "Start Manager.bat")
    c.post("/api/launcher/voice-manager/open", json={})                           # remembered: one click
    assert opened[-1] == str(vm / "Start Manager.bat")

    r = c.post("/api/launcher/voice-manager/open", json={"target": "http://127.0.0.1:8000"}).json()
    assert r["url"] == "http://127.0.0.1:8000" and len(opened) == 2               # a web address is opened by the page

    # with nothing set and exactly one program in the folder, that one is used
    c.put("/api/settings", json={"voice_manager": ""})
    (vm / "app" / "VoiceManager.exe").unlink()
    assert c.get("/api/launcher/voice-manager").json()["resolved"] == str(vm / "Start Manager.bat")


def test_long_phrases_and_clips(client, tmp_path):
    """Whole sentences up to ~30 s can be catchphrases with their recordings; only short ones hint speech recognition;
    delivery clips outside 1–30 s are imported but wait for a person."""
    from vstudio import phrases
    c = client
    v = _consented_voice(c)
    long_text = "彗星のごとく現れたスターの原石、バーチャルアイドルの星街すいせいでーす、今日も一日よろしくお願いします" * 2
    assert 60 < len(long_text) <= phrases.MAX_TEXT
    r = c.post(f"/api/voices/{v['id']}/phrases", json={"text": long_text, "lang": "ja"})
    assert r.status_code == 200, r.text
    c.post(f"/api/voices/{v['id']}/phrases", json={"text": "やっほー", "lang": "ja"})
    assert phrases.asr_prompt(v["id"], "ja") == "やっほー。"          # the long sentence stays out of the hint
    pid = r.json()["id"]
    for seconds, ok in ((15.0, True), (29.0, True), (31.0, False)):
        f = _tone_file(tmp_path / f"long_{seconds:g}.wav", seconds)
        with open(f, "rb") as fh:
            res = c.post(f"/api/phrases/{pid}/clips", files={"file": (f.name, fh, "audio/wav")}, data={"emotion": ""})
        assert (res.status_code == 200) == ok, (seconds, res.status_code, res.text)
    assert len(phrases.get(pid)["clips"]) == 2

    from vstudio import delivery
    person = tmp_path / "Bob"
    _tone_file(person / "交付/clean/en/happy/20250101_vidZ_0.00-12.00.wav", 12.0)
    _tone_file(person / "交付/clean/en/happy/20250101_vidZ_100.00-135.00.wav", 35.0)
    (person / "交付/clips.csv").write_text(
        "file,transcript\nclean/en/happy/20250101_vidZ_0.00-12.00.wav,A twelve second line\n"
        "clean/en/happy/20250101_vidZ_100.00-135.00.wav,A very long thirty five second line\n", encoding="utf-8")
    res = delivery.run(str(person), v["id"], build=False)
    assert res["added"] == 2
    got = c.get(f"/api/segments?voice_id={v['id']}&limit=100").json()
    segs = {s["text"]: s for s in (got["items"] if isinstance(got, dict) else got)}
    assert segs["A twelve second line"]["status"] == "approved"
    assert segs["A very long thirty five second line"]["status"] == "pending"


GPU_CATALOG = {"gpus": [  # the shape of api.runpod.io/v2/catalog/gpus?include=AVAILABILITY
    {"id": "NVIDIA L40S", "name": "L40S", "memory": 48, "price": {"secure": 0.86},
     "dataCenters": [{"id": "US-IL-1", "availability": "HIGH"}]},
    {"id": "NVIDIA H100 80GB HBM3", "name": "H100 SXM", "memory": 80, "price": {"secure": 3.99},
     "dataCenters": [{"id": "US-CA-2", "availability": "LOW"}]},
    {"id": "NVIDIA A100-SXM4-80GB", "name": "A100 SXM", "memory": 80, "price": {"secure": 1.79},
     "dataCenters": [{"id": "US-CA-2", "availability": "NONE"}]},
    {"id": "AMD Instinct MI300X OAM", "name": "MI300X", "memory": 192, "price": {"secure": 2.39},
     "dataCenters": [{"id": "US-CA-2", "availability": "HIGH"}]},
]}


def _fake_gpu_catalog(monkeypatch, runpod, fail=False, payload=None):
    """Serve the GPU catalog from memory (GPU_CATALOG, or payload, which a test may change as it goes): no key, no
    network."""
    import types
    import httpx

    class Client:
        def __init__(self, *a, **kw):
            pass

        def __enter__(self):
            return self

        def __exit__(self, *a):
            return False

        def get(self, url, **kw):
            if fail:
                raise httpx.ConnectError("[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed")
            assert url.endswith("/v2/catalog/gpus")
            return types.SimpleNamespace(status_code=200, json=lambda: payload or GPU_CATALOG)

    monkeypatch.setattr(runpod, "_h", lambda: {})
    monkeypatch.setattr(runpod, "httpx", types.SimpleNamespace(Client=Client))


def test_gpu_stock_in_the_volume_datacenter(client, monkeypatch):
    """Only cards the volume's datacenter has can be rented; a bigger known card stands in for missing ones."""
    from vstudio import config, training
    from vstudio.cloud import runpod
    _fake_gpu_catalog(monkeypatch, runpod)
    config.save_settings({"runpod_datacenter": "US-CA-2"})
    cat = runpod.gpu_catalog("US-CA-2")
    by = {g["id"]: g for g in cat["gpus"]}
    assert cat["live"] and "AMD Instinct MI300X OAM" not in by                    # the engine images are CUDA
    assert by["NVIDIA H100 80GB HBM3"]["availability"] == "LOW"
    assert by["NVIDIA L40S"]["availability"] == "NONE"                             # sold elsewhere, not here

    res = client.get("/api/cloud/gpus?engine=voxcpm2&preset=lora").json()
    ids = [o["id"] for o in res["offers"]]
    assert res["live"] and res["datacenter"] == "US-CA-2" and res["default"] == "NVIDIA H100 80GB HBM3" == ids[0]
    assert not res["offers"][0]["recommended"] and res["offers"][0]["vram"] == 80  # LoRA's own 48 GB cards: none here
    assert {"NVIDIA L40S", "NVIDIA RTX 6000 Ada Generation"} <= set(ids)          # still listed, as sold out
    assert all(o["availability"] == "NONE" for o in res["offers"][1:])
    assert "NVIDIA GeForce RTX 4090" not in ids                                   # 24 GB is too small for LoRA
    assert client.get("/api/cloud/gpus?engine=nope&preset=x").status_code == 404

    assert training._stock_problem("voxcpm2", "lora", "NVIDIA H100 80GB HBM3", "US-CA-2") is None
    msg = training._stock_problem("voxcpm2", "lora", "NVIDIA L40S", "US-CA-2")
    assert "L40S" in msg and "H100 SXM" in msg                                    # says what can be rented instead
    assert training._stock_problem("voxcpm2", "lora", "NVIDIA GeForce RTX 4090", "US-CA-2")


def test_gpu_stock_unreadable_is_said_not_hidden(client, monkeypatch):
    from vstudio import training
    from vstudio.cloud import runpod
    _fake_gpu_catalog(monkeypatch, runpod, fail=True)
    res = training.gpu_offers("voxcpm2", "lora")
    assert not res["live"] and "CERTIFICATE_VERIFY_FAILED" in res["error"]
    assert res["default"] == "NVIDIA L40S" and all(o["availability"] is None for o in res["offers"])
    assert training._stock_problem("voxcpm2", "lora", "NVIDIA L40S", "US-CA-2") is None  # unknown stock: renting is tried


def test_sold_out_gpu_stops_before_upload_and_retry_reuses_upload(client, monkeypatch, tmp_path):
    from vstudio import config, db, training
    from vstudio.cloud import runpod
    c = client
    _fake_gpu_catalog(monkeypatch, runpod)
    config.save_settings({"runpod_datacenter": "US-CA-2", "runpod_volume_id": "vol1"})
    v = c.post("/api/voices", json={"name": "我", "kind": "self", "languages": ["ja"]}).json()
    c.post(f"/api/voices/{v['id']}/consent",
           data={"signed_name": "測試者", "date": "2026-10-06", "agreed": "true", "scope": "train,generate"})
    ds = db.insert("datasets", {"id": db.new_id("ds"), "voice_id": v["id"], "name": "v1", "n_items": 40, "hours": 1.0,
                                "path": str(tmp_path / "ds"), "created_at": db.now(),
                                "meta": {"n_train": 40, "consent": db.get("voices", v["id"])["consent"],
                                         "voice": {"name": "我"}}})
    calls = {"upload": 0, "put": {}, "pods": []}
    monkeypatch.setattr(runpod, "exists", lambda key, loc=None, fast=False: key.endswith("/dataset.tar"))
    monkeypatch.setattr(runpod, "size", lambda key, loc=None: 1234)
    monkeypatch.setattr(runpod, "upload", lambda *a, **kw: calls.update(upload=calls["upload"] + 1))
    monkeypatch.setattr(runpod, "put_text", lambda key, text, loc=None: calls["put"].update({key.rsplit("/", 1)[1]: text}))
    monkeypatch.setattr(runpod, "list_pods", lambda name=None, volume=None: [])
    monkeypatch.setattr(runpod, "get_text", lambda *a, **kw: "")

    def create_pod(name, image, gpu_type, *a, **kw):
        calls["pods"].append(gpu_type)
        raise runpod.RunPodError("RunPod POST /pods: 500 There are no instances currently available")
    monkeypatch.setattr(runpod, "create_pod", create_pod)

    # a sold-out card is refused before anything is uploaded or a run is recorded
    r = c.post("/api/training", json={"dataset_id": ds["id"], "engine": "voxcpm2", "preset": "lora", "gpu": "NVIDIA L40S"})
    assert r.status_code == 400 and "H100 SXM" in r.json()["detail"]
    assert not db.query("SELECT * FROM trainings") and calls["upload"] == 0

    # a run that uploaded its data and then got no GPU: another card, without uploading again
    tid = db.new_id("tr")
    db.insert("trainings", {"id": tid, "voice_id": v["id"], "dataset_id": ds["id"], "engine": "mock",
                            "preset": {"id": "quick", "params": {"steps": 4}, "name": ""}, "target": "runpod",
                            "status": "failed", "gpu": "NVIDIA GeForce RTX 4090", "remote_prefix": f"vs/jobs/{tid}",
                            "storage": {"volume": "vol1", "datacenter": "US-CA-2", "cloud": "SECURE"},
                            "progress": {}, "created_at": db.now(), "uploaded_at": db.now()})
    assert next(t for t in c.get("/api/training").json() if t["id"] == tid)["can_retry_gpu"]
    r = c.post(f"/api/training/{tid}/retry-gpu", json={"gpu": "NVIDIA L40S"})
    assert r.status_code == 400 and "H100 SXM" in r.json()["detail"]
    tr = c.post(f"/api/training/{tid}/retry-gpu", json={"gpu": "NVIDIA H100 80GB HBM3", "usd_h": 3.99}).json()
    assert tr["gpu"] == "NVIDIA H100 80GB HBM3" and tr["cost_estimate"] > 0
    j = _wait(c, tr["job_id"])
    assert j["status"] == "failed" and "換一張 GPU 重試" in j["message"]
    assert calls["upload"] == 0 and calls["pods"] == [["NVIDIA H100 80GB HBM3"]]   # reused, then tried the new card
    assert "config.json" not in calls["put"] and '"status":"done","bytes":0,"total":1234' in calls["put"]["upload.json"]
    assert training.can_retry_gpu(db.get("trainings", tid))                        # and can try yet another one

    # a run that never uploaded (or whose data is gone) cannot be retried this way
    db.update("trainings", tid, {"uploaded_at": None})
    assert c.post(f"/api/training/{tid}/retry-gpu", json={"gpu": "NVIDIA H100 80GB HBM3"}).status_code == 400


def test_gpu_is_rented_before_the_dataset_is_uploaded(client, monkeypatch, tmp_path):
    """A scarce GPU is held first: the pod is rented, then the dataset goes up while the pod sets up and waits for it."""
    import tarfile
    from vstudio import config, db, training
    from vstudio.cloud import runpod
    c = client
    _fake_gpu_catalog(monkeypatch, runpod)
    config.save_settings({"runpod_datacenter": "US-CA-2", "runpod_volume_id": "vol1", "runpod_max_hours": 2})
    v = c.post("/api/voices", json={"name": "我", "kind": "self", "languages": ["ja"]}).json()
    c.post(f"/api/voices/{v['id']}/consent",
           data={"signed_name": "測試者", "date": "2026-10-06", "agreed": "true", "scope": "train,generate"})
    (tmp_path / "ds" / "wavs").mkdir(parents=True)
    (tmp_path / "ds" / "wavs" / "a.wav").write_bytes(b"\0" * 300_000)
    ds = db.insert("datasets", {"id": db.new_id("ds"), "voice_id": v["id"], "name": "v1", "n_items": 40, "hours": 1.0,
                                "path": str(tmp_path / "ds"), "created_at": db.now(),
                                "meta": {"n_train": 40, "consent": db.get("voices", v["id"])["consent"]}})
    body = {"dataset_id": ds["id"], "engine": "mock", "preset": "quick", "gpu": "NVIDIA H100 80GB HBM3", "target": "runpod"}
    plan = c.post("/api/training/plan", json=body).json()
    assert plan["upload"] and plan["upload"]["minutes"] is None              # upload speed not measured yet
    config.save_settings({"upload_bps": 1000})                                # 300 kB at 1 kB/s = 5 minutes, billed
    plan2 = c.post("/api/training/plan", json=body).json()
    assert plan2["upload"]["minutes"] == 5.0 and plan2["estimate_hours"] > plan["estimate_hours"]
    config.save_settings({"upload_bps": 0})

    def package(tid, work):
        tar = work / "dataset.tar"
        with tarfile.open(tar, "w") as t:
            t.add(tmp_path / "ds" / "wavs", arcname="data/wavs")
        return tar, {"training_id": tid}
    monkeypatch.setattr(training, "package_dataset", package)
    events: list = []
    monkeypatch.setattr(runpod, "exists", lambda key, loc=None, fast=False: False)
    monkeypatch.setattr(runpod, "put_text", lambda key, text, loc=None: events.append(("put", key.rsplit("/", 1)[1], text)))
    monkeypatch.setattr(runpod, "list_pods", lambda name=None, volume=None: [])
    monkeypatch.setattr(runpod, "get_text", lambda *a, **kw: "")
    monkeypatch.setattr(runpod, "remove_pod", lambda pod_id: events.append(("remove", pod_id)))

    def create_pod(name, image, gpu_type, env, *a, **kw):
        events.append(("pod", gpu_type, env))
        return {"id": "pod1", "costPerHr": 3.99}

    def upload(local, key, progress=None, loc=None):
        events.append(("upload", db.query("SELECT status FROM trainings")[0]["status"]))  # the GPU is already held
        progress(0.5), progress(1.0)
    monkeypatch.setattr(runpod, "create_pod", create_pod)
    monkeypatch.setattr(runpod, "upload", upload)
    # the pod then reports a training error, which ends the run quickly
    monkeypatch.setattr(runpod, "get_json", lambda key, loc=None, fast=False:
                        {"status": "error", "stage": "train"} if key.endswith("error.json") else None)

    tr = c.post("/api/training", json=body).json()
    tid = tr["id"]
    j = _wait(c, tr["job_id"])
    assert j["status"] == "failed" and "訓練" in j["message"]
    beats = [i for i, e in enumerate(events) if e[:2] == ("put", "upload.json")]
    rent = next(i for i, e in enumerate(events) if e[0] == "pod")
    sent = next(i for i, e in enumerate(events) if e[0] == "upload")
    assert beats[0] < rent < sent < beats[-1] and events[sent][1] == "uploading"  # waiting → rent → upload → done
    assert '"status":"waiting"' in events[beats[0]][2] and '"status":"done"' in events[beats[-1]][2]
    env = events[rent][2]
    assert env["VS_WAIT_UPLOAD"] == "1" and int(env["VS_MAX_SECONDS"]) >= 2 * 3600 + 1800  # time for the upload too
    t = db.get("trainings", tid)
    assert t["uploaded_at"] and t["pod_id"] == "pod1" and ("remove", "pod1") in events and not training.can_retry_gpu(t)


def test_auto_grab_waits_renting_nothing_then_grabs(client, monkeypatch, tmp_path):
    """Auto-grab: while its cards are sold out the run only waits (nothing rented); a card taken at the last moment
    sends it back to waiting; then it rents the first card of its list in stock; it stops on time or on request."""
    import copy
    import tarfile
    import time
    from vstudio import config, db, training
    from vstudio.cloud import runpod
    c = client
    monkeypatch.setattr(config, "get_secret", lambda name: None)  # the server's own waiter thread stays out of this
    stock = copy.deepcopy(GPU_CATALOG)
    _fake_gpu_catalog(monkeypatch, runpod, payload=stock)
    config.save_settings({"runpod_datacenter": "US-CA-2", "runpod_volume_id": "vol1"})
    v = c.post("/api/voices", json={"name": "我", "kind": "self", "languages": ["ja"]}).json()
    c.post(f"/api/voices/{v['id']}/consent",
           data={"signed_name": "測試者", "date": "2026-10-06", "agreed": "true", "scope": "train,generate"})
    (tmp_path / "ds" / "wavs").mkdir(parents=True)
    (tmp_path / "ds" / "wavs" / "a.wav").write_bytes(b"\0" * 1000)
    ds = db.insert("datasets", {"id": db.new_id("ds"), "voice_id": v["id"], "name": "v1", "n_items": 40, "hours": 1.0,
                                "path": str(tmp_path / "ds"), "created_at": db.now(),
                                "meta": {"n_train": 40, "consent": db.get("voices", v["id"])["consent"]}})

    def package(tid, work):
        tar = work / "dataset.tar"
        with tarfile.open(tar, "w") as t:
            t.add(tmp_path / "ds" / "wavs", arcname="data/wavs")
        return tar, {"training_id": tid}
    pods, taken = [], [True]

    def create_pod(name, image, gpu_type, env, *a, **kw):
        pods.append(list(gpu_type))
        if taken[0]:
            raise runpod.RunPodError("RunPod POST /pods: 500 There are no instances currently available")
        return {"id": "pod1", "machine": {"gpuTypeId": gpu_type[0]},
                "costPerHr": 2.49 if gpu_type[0] == "NVIDIA A100-SXM4-80GB" else 0.86}
    monkeypatch.setattr(training, "package_dataset", package)
    monkeypatch.setattr(runpod, "create_pod", create_pod)
    monkeypatch.setattr(runpod, "exists", lambda key, loc=None, fast=False: False)
    monkeypatch.setattr(runpod, "put_text", lambda *a, **kw: None)
    monkeypatch.setattr(runpod, "upload", lambda local, key, progress=None, loc=None: progress(1.0))
    monkeypatch.setattr(runpod, "list_pods", lambda name=None, volume=None: [])
    monkeypatch.setattr(runpod, "get_text", lambda *a, **kw: "")
    monkeypatch.setattr(runpod, "remove_pod", lambda pod_id: None)
    monkeypatch.setattr(runpod, "get_json", lambda key, loc=None, fast=False:
                        {"status": "error", "stage": "train"} if key.endswith("error.json") else None)

    l40s, a100 = "NVIDIA L40S", "NVIDIA A100-SXM4-80GB"
    body = {"dataset_id": ds["id"], "engine": "voxcpm2", "preset": "lora", "target": "runpod",
            "gpus": [l40s, a100], "wait_hours": 1}
    r = c.post("/api/training", json={**body, "gpus": ["NVIDIA GeForce RTX 4090"]})
    assert r.status_code == 400 and "RTX 4090" in r.json()["detail"]          # 24 GB: not enough for LoRA
    tr = c.post("/api/training", json=body).json()
    tid = tr["id"]
    assert tr["status"] == "waiting_gpu" and tr["wait"]["gpus"] == [l40s, a100] and not tr.get("job_id")
    assert training.wait_for_gpus() == [] and not pods                        # both sold out: nothing rented
    w = db.get("trainings", tid)["wait"]
    assert w["checks"] >= 1 and w["seen"] == {l40s: "NONE", a100: "NONE"}

    for g in stock["gpus"]:  # both come in stock in US-CA-2 ...
        if g["id"] in (l40s, a100):
            g["dataCenters"] = [{"id": "US-CA-2", "availability": "LOW"}]
    assert training.wait_for_gpus() == [tid]                                  # ... but are taken at the last moment
    assert _wait(c, db.get("trainings", tid)["job_id"])["status"] == "done"
    t = db.get("trainings", tid)
    assert t["status"] == "waiting_gpu" and t["wait"]["misses"] == 1 and pods == [[l40s, a100]]

    taken[0] = False                                                          # next time it works, on the A100:
    for g in stock["gpus"]:                                                   # the L40S is gone again
        if g["id"] == l40s:
            g["dataCenters"] = [{"id": "US-CA-2", "availability": "NONE"}]
    est_first = db.get("trainings", tid)["cost_estimate"]                     # quoted for the L40S
    db.update("trainings", tid, {"created_at": time.time() - 3 * 3600})       # after waiting 3 hours
    assert training.wait_for_gpus() == [tid]
    _wait(c, db.get("trainings", tid)["job_id"])                              # (ends here on the pod's train error)
    t = db.get("trainings", tid)
    assert pods[-1] == [a100] and t["pod_id"] == "pod1" and t["gpu"] == a100 and t["uploaded_at"]
    assert t["cost_estimate"] == training._estimate_usd(t, a100, 2.49, upload=True) != est_first  # follows the card
    assert t["progress"]["wall_s"] < 600                                      # the 3 hours of waiting are not counted

    late = c.post("/api/training", json=body).json()                          # waiting time over: stops by itself
    db.update("trainings", late["id"], {"wait": {**late["wait"], "until": time.time() - 1}})
    training.wait_for_gpus()
    t = db.get("trainings", late["id"])
    assert t["status"] == "failed" and "沒有計費" in t["note"]
    stop = c.post("/api/training", json=body).json()                          # and can be stopped
    c.post(f"/api/training/{stop['id']}/cancel")
    assert db.get("trainings", stop["id"])["status"] == "canceled" and training.wait_for_gpus() == []

    # the studio is closed while a grabbed run uploads onto its pod: at start-up the pod goes and the run waits again
    removed = []
    monkeypatch.setattr(runpod, "remove_pod", lambda pod_id: removed.append(pod_id))
    closed = c.post("/api/training", json=body).json()
    job = db.insert("jobs", {"id": db.new_id("job"), "kind": "cloud_train", "queue": "io", "status": "failed",
                             "params": {"training_id": closed["id"]}, "result": {}, "created_at": db.now()})
    db.update("trainings", closed["id"], {"status": "uploading", "pod_id": "pod9", "pod_state": "running",
                                          "job_id": job["id"], "started_at": time.time()})
    assert training.resume_interrupted() == []
    t = db.get("trainings", closed["id"])
    assert removed == ["pod9"] and t["status"] == "waiting_gpu" and not t["pod_id"] and "重新等卡" in t["wait"]["note"]


def test_https_is_verified_also_with_many_connections_at_once(tmp_path):
    """HTTPS goes through one CA file (Windows: certifi + the roots Windows trusts) that OpenSSL verifies against;
    ssl.SSLContext is not patched. A server with an untrusted certificate is refused on every connection, also with
    many at once, as boto3's parallel transfers make them (with the truststore patch, some of those were checked
    while another handshake had verification switched off)."""
    import datetime
    import http.server
    import ipaddress
    import ssl
    import threading
    from concurrent.futures import ThreadPoolExecutor
    pytest.importorskip("cryptography")
    from cryptography import x509
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import ec
    from cryptography.x509.oid import NameOID

    key = ec.generate_private_key(ec.SECP256R1())
    name = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, "127.0.0.1")])
    now = datetime.datetime.now(datetime.timezone.utc)
    cert = (x509.CertificateBuilder().subject_name(name).issuer_name(name).public_key(key.public_key())
            .serial_number(x509.random_serial_number()).not_valid_before(now - datetime.timedelta(minutes=5))
            .not_valid_after(now + datetime.timedelta(days=1))
            .add_extension(x509.SubjectAlternativeName([x509.IPAddress(ipaddress.ip_address("127.0.0.1"))]),
                           critical=False).sign(key, hashes.SHA256()))
    (tmp_path / "cert.pem").write_bytes(cert.public_bytes(serialization.Encoding.PEM))
    (tmp_path / "key.pem").write_bytes(key.private_bytes(serialization.Encoding.PEM,
                                                         serialization.PrivateFormat.PKCS8,
                                                         serialization.NoEncryption()))
    import vstudio  # noqa: F401  (sets up HTTPS on import)
    assert ssl.SSLContext.__module__ == "ssl"
    if os.name == "nt":
        bundle = Path(os.environ["AWS_CA_BUNDLE"])
        assert os.environ["SSL_CERT_FILE"] == os.environ["REQUESTS_CA_BUNDLE"] == str(bundle)
        assert bundle.read_text(encoding="utf-8").count("BEGIN CERTIFICATE") > 100

    sctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    sctx.load_cert_chain(tmp_path / "cert.pem", tmp_path / "key.pem")
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), http.server.BaseHTTPRequestHandler)
    srv.socket = sctx.wrap_socket(srv.socket, server_side=True, do_handshake_on_connect=False)
    srv.handle_error = lambda *a: None
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    import boto3
    from botocore.config import Config
    s3 = boto3.client("s3", aws_access_key_id="x", aws_secret_access_key="y", region_name="us-east-1",
                      endpoint_url=f"https://127.0.0.1:{srv.server_address[1]}",
                      config=Config(retries={"max_attempts": 1}, connect_timeout=5, read_timeout=5,
                                    max_pool_connections=8))

    def one(_):
        try:
            s3.list_buckets()
            return True                     # got through: the certificate was not verified
        except Exception:
            return False
    with ThreadPoolExecutor(8) as ex:
        accepted = sum(ex.map(one, range(32)))
    srv.shutdown()
    assert accepted == 0


def _bash() -> str | None:
    """A real bash for running bootstrap.sh (Git Bash on Windows, not the WSL launcher)."""
    import shutil
    cands = [shutil.which("bash")] + ([r"C:\Program Files\Git\bin\bash.exe"] if os.name == "nt" else [])
    return next((b for b in cands if b and os.path.exists(b) and "system32" not in b.lower()), None)


@pytest.mark.skipif(_bash() is None, reason="needs bash")
def test_bootstrap_waits_for_the_upload_and_gives_up_without_word(tmp_path):
    """bootstrap.sh on a rented pod: it waits for upload.json to say done (with the right size), and a pod that hears
    nothing from the studio stops and removes itself instead of waiting on rented time."""
    import json
    import subprocess
    import tarfile
    from vstudio import training

    def sh(p) -> str:  # a path as bash sees it (Git Bash: /c/..., so tar does not take "C:" for a remote host)
        s = p.as_posix()
        return f"/{s[0].lower()}{s[2:]}" if os.name == "nt" and s[1:2] == ":" else s

    def run(case: str, upload: str | None, tar: bool) -> dict:
        root = tmp_path / case
        job = root / "vs" / "jobs" / "t1"
        job.mkdir(parents=True)
        (job / "setup_env.sh").write_text("exit 0\n", encoding="utf-8", newline="\n")
        (root / "bin").mkdir()
        ctl = root / "bin" / "runpodctl"
        ctl.write_text(f'#!/bin/bash\necho "$@" >> "{sh(root / "ctl.log")}"\n', encoding="utf-8", newline="\n")
        ctl.chmod(0o755)
        (root / "vs" / "envs" / "mock" / "bin").mkdir(parents=True)
        (root / "vs" / "envs" / "mock" / "bin" / "activate").write_text("", encoding="utf-8")
        if tar:
            (root / "x.txt").write_text("x", encoding="utf-8")
            with tarfile.open(job / "dataset.tar", "w") as t:
                t.add(root / "x.txt", arcname="data/x.txt")
        if upload:
            (job / "upload.json").write_text(upload.replace("SIZE", str((job / "dataset.tar").stat().st_size)),
                                             encoding="utf-8")
        script = job / "bootstrap.sh"
        script.write_bytes(training.BOOTSTRAP.encode("utf-8"))
        env = {**os.environ, "PATH": str(root / "bin") + os.pathsep + os.environ.get("PATH", ""),
               "VS_ROOT": sh(root / "vs"), "VS_WORK": sh(root / "work"), "VS_DATA": sh(root / "data"),
               "VS_TRAINING_ID": "t1", "VS_ENGINE": "mock", "RUNPOD_POD_ID": "pod1", "VS_WAIT_UPLOAD": "1",
               "VS_UPLOAD_STALL": "3", "VS_UPLOAD_POLL": "1", "VS_FINISH_SLEEP": "0", "VS_KILL_GRACE": "0",
               "VS_RETRY_SLEEP": "0", "VS_MAX_SECONDS": "120"}
        subprocess.run([_bash(), sh(script)], env=env, timeout=90, stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL)
        err = json.loads((job / "error.json").read_text(encoding="utf-8"))
        return {"stage": err["stage"], "removed": "remove pod pod1" in (root / "ctl.log").read_text(encoding="utf-8"),
                "log": (job / "train.log").read_text(encoding="utf-8", errors="replace")}

    silent = run("silent", None, tar=False)                    # the studio never says anything
    assert silent["stage"] == "upload" and silent["removed"] and "giving up" in silent["log"]
    short = run("short", '{"status":"done","bytes":1,"total":999999999,"t":1}', tar=True)  # size does not match yet
    assert short["stage"] == "upload" and short["removed"]
    done = run("done", '{"status":"done","bytes":SIZE,"total":SIZE,"t":1}', tar=True)
    assert done["stage"] == "train" and done["removed"] and "dataset uploaded" in done["log"]  # went on past the wait


def test_unusable_volume_is_flagged_and_stops_start(client, monkeypatch, tmp_path):
    """A deleted volume, or one in a datacenter without the S3 API, is named on the pages and refused before upload."""
    from vstudio import config, db
    from vstudio.cloud import runpod
    c = client
    vols = [{"id": "tx", "name": "better_plum_gibbon", "dataCenterId": "US-TX-3", "size": 150},
            {"id": "wa", "name": "fine", "dataCenterId": "US-WA-1", "size": 150}]
    monkeypatch.setattr(runpod, "_req", lambda method, path, **kw: vols if path == "/networkvolumes" else {})

    def problem(volume, dc):
        config.save_settings({"runpod_volume_id": volume, "runpod_datacenter": dc})
        return c.get("/api/cloud/check").json()

    chk = problem("gone", "US-CA-2")
    assert [v["s3"] for v in chk["volumes"]] == [False, True] and "gone" in chk["problem"]
    assert "US-TX-3" in problem("tx", "US-TX-3")["problem"]                # no S3 endpoint there
    assert "US-WA-1" in problem("wa", "US-CA-2")["problem"]                # datacenter does not match the volume
    assert problem("wa", "US-WA-1")["problem"] == ""

    v = c.post("/api/voices", json={"name": "我", "kind": "self", "languages": ["ja"]}).json()
    c.post(f"/api/voices/{v['id']}/consent",
           data={"signed_name": "測試者", "date": "2026-10-06", "agreed": "true", "scope": "train,generate"})
    ds = db.insert("datasets", {"id": db.new_id("ds"), "voice_id": v["id"], "name": "v1", "n_items": 40, "hours": 1.0,
                                "path": str(tmp_path / "ds"), "created_at": db.now(),
                                "meta": {"n_train": 40, "consent": db.get("voices", v["id"])["consent"]}})
    problem("gone", "US-CA-2")
    r = c.post("/api/training", json={"dataset_id": ds["id"], "engine": "voxcpm2", "preset": "lora", "gpu": "NVIDIA L40S"})
    assert r.status_code == 400 and "gone" in r.json()["detail"] and not db.query("SELECT * FROM trainings")


def test_unmeasured_gpu_estimate_scales_a_measured_speed(client, tmp_path):
    """A faster card is never estimated slower: an unmeasured card uses another card's measured speed, scaled."""
    from vstudio import config, db, training
    c = client
    v = c.post("/api/voices", json={"name": "我", "kind": "self", "languages": ["ja"]}).json()
    c.post(f"/api/voices/{v['id']}/consent",
           data={"signed_name": "測試者", "date": "2026-10-06", "agreed": "true", "scope": "train,generate"})
    ds = db.insert("datasets", {"id": db.new_id("ds"), "voice_id": v["id"], "name": "v1", "n_items": 3600, "hours": 10.0,
                                "path": str(tmp_path / "ds"), "created_at": db.now(),
                                "meta": {"n_train": 3600, "consent": db.get("voices", v["id"])["consent"]}})
    rtx, h100 = "NVIDIA RTX 6000 Ada Generation", "NVIDIA H100 80GB HBM3"

    def plan(gpu):
        return c.post("/api/training/plan", json={"dataset_id": ds["id"], "engine": "voxcpm2", "preset": "lora",
                                                  "gpu": gpu, "target": "runpod"}).json()
    g_rtx, g_h100 = plan(rtx), plan(h100)                       # nothing measured: the first guess, per card
    assert g_rtx["estimate_basis"] == g_h100["estimate_basis"] == "guess"
    assert g_h100["estimate_hours"] < g_rtx["estimate_hours"]

    config.save_settings({"speed": {f"voxcpm2:lora:{rtx}": {"s_per_step": 2.0, "at": 1.0}}})
    m_rtx, s_h100 = plan(rtx), plan(h100)
    assert m_rtx["estimate_basis"] == "measured" and m_rtx["s_per_step"] == 2.0
    assert s_h100["estimate_basis"] == "scaled" and s_h100["estimate_from"] == "RTX 6000 Ada 48GB"
    assert s_h100["s_per_step"] == 0.8 and s_h100["estimate_hours"] < m_rtx["estimate_hours"]  # 2.0 s × 0.8 / 2.0

    # the card's own measurement wins; the latest other measurement is the one scaled; Colab is never scaled
    config.save_settings({"speed": {f"voxcpm2:lora:{rtx}": {"s_per_step": 2.0, "at": 1.0},
                                    f"voxcpm2:lora:{h100}": {"s_per_step": 1.1, "at": 2.0},
                                    "voxcpm2:lora:NVIDIA A100-SXM4-80GB": {"s_per_step": 1.5, "at": 3.0}}})
    assert training._speed("voxcpm2", "lora", h100) == (1.1, "measured", h100)
    assert training._speed("voxcpm2", "lora", "NVIDIA L40S")[1:] == ("scaled", "NVIDIA A100-SXM4-80GB")
    assert training._speed("voxcpm2", "lora", "Colab") == (None, "guess", "")

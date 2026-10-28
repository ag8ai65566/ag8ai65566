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
    assert emotions.from_style("annoyed, sharp") == "angry"
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
    y, sr, info, used = tts._spliced(Eng(), {"checkpoint": "ck"}, parts, "ja", "calm", "plain", None, timbre, 1, None,
                                     None, 0, ["plain", "ref", "hifi"])
    assert [c["mode"] for c in calls] == ["plain", "hifi"]
    assert calls[0]["text"] == "前置き、" and calls[1]["text"] == "今日もやるよ"
    assert calls[1]["ref"]["path"] == clip and calls[1]["ref"]["text"] == "やっほー！"
    assert calls[1]["ref"]["timbre_path"] == timbre["path"]
    assert sr == 24000 and used == [{"phrase": "やっほー", "clip": "c1", "emotion": ""}]
    # two synthesized seconds + the recording + punctuation pauses
    assert 2.5 < len(y) / sr < 3.2


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

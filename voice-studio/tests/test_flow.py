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

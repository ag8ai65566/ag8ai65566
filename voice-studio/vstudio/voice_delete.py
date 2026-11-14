"""Deleting a voice together with everything recorded or made from it.

What goes: the voice and its consent record and enrollment clips; its recordings (a recording other voices also
speak in keeps their clips and loses only this voice's); its clips, catchphrases and sound tags; its datasets,
trainings and models; speech generated with its models (single lines, character performances, and scene mixes
that include it); the training files on the cloud (the RunPod network volume or the Google Drive folder).
What stays: files outside Voice Studio (a delivery folder, the original of a recording that was not copied in).

plan() says what would go and what blocks it (a training or job still working with the voice); remove() does it
and lists what could not be deleted (for example the cloud was unreachable), with where it is.
"""
from __future__ import annotations

import json
import shutil
from pathlib import Path

from . import config, datasets, db, phrases, training
from .cloud import colab, runpod

ACTIVE_TRAINING = ("queued", "waiting_gpu", "starting", "uploading", "running", "downloading")


class Blocked(Exception):
    pass


def _owned(voice_id: str) -> dict:
    """The ids of everything that belongs to the voice."""
    sids = {r["source_id"] for r in db.query("SELECT DISTINCT source_id FROM segments WHERE voice_id=?", (voice_id,))}
    sids |= {r["id"] for r in db.query("SELECT id FROM sources WHERE voice_hint=?", (voice_id,))}
    whole, shared = [], []
    for sid in sorted(sids):
        other = db.connect().execute("SELECT COUNT(*) FROM segments WHERE source_id=? AND voice_id IS NOT NULL "
                                     "AND voice_id != ?", (sid, voice_id)).fetchone()[0]
        (shared if other else whole).append(sid)
    models = [r["id"] for r in db.query("SELECT id FROM models WHERE voice_id=?", (voice_id,))]
    outs = db.query(f"SELECT id, path, batch FROM outputs WHERE model_id IN ({','.join('?' * len(models))})",
                    models) if models else []
    scenes = sorted({o["batch"] for o in outs if (o.get("batch") or "").startswith("scene")})
    scene_rows = db.query(f"SELECT id, path, batch FROM outputs WHERE id IN ({','.join('?' * len(scenes))})",
                          scenes) if scenes else []
    perfs = [p["id"] for p in db.query("SELECT id, params FROM performances")
             if (p.get("params") or {}).get("model_id") in models]
    return {"whole": whole, "shared": shared, "models": models, "outputs": outs + scene_rows, "performances": perfs,
            "datasets": [r["id"] for r in db.query("SELECT id FROM datasets WHERE voice_id=?", (voice_id,))],
            "trainings": db.query("SELECT * FROM trainings WHERE voice_id=?", (voice_id,)),
            "phrases": [r["id"] for r in db.query("SELECT id FROM catchphrases WHERE voice_id=?", (voice_id,))]}


def _blockers(voice_id: str, own: dict) -> list[str]:
    out = [f"訓練「{(t.get('preset') or {}).get('name') or t['id']}」還在進行（{t['status']}）"
           for t in own["trainings"] if t["status"] in ACTIVE_TRAINING]
    ids = [voice_id, *own["models"], *own["datasets"], *(t["id"] for t in own["trainings"])]
    for j in db.query("SELECT id, kind, message, params FROM jobs WHERE status IN ('queued', 'running')"):
        if j["kind"] == "prepare_source":  # importing one of its recordings: cancelled with the recording
            continue
        if j["kind"] == "cloud_train" and any(t["id"] == (j["params"] or {}).get("training_id")
                                              for t in own["trainings"] if t["status"] in ACTIVE_TRAINING):
            continue  # already listed as its training
        params = json.dumps(j["params"] or {})
        if any(i and i in params for i in ids):
            out.append(f"工作「{j['message'] or j['kind']}」還在跑")
    return out


def plan(voice_id: str) -> dict:
    v = db.get("voices", voice_id)
    if not v:
        raise KeyError(voice_id)
    own = _owned(voice_id)
    seg = db.connect().execute("SELECT COUNT(*), COALESCE(SUM(duration), 0) FROM segments WHERE voice_id=?",
                               (voice_id,)).fetchone()
    cloud = [t for t in own["trainings"] if t.get("remote_prefix")]
    return {"voice": {"id": v["id"], "name": v["name"]},
            "counts": {"recordings": len(own["whole"]), "shared_recordings": len(own["shared"]),
                       "segments": seg[0], "minutes": round(seg[1] / 60, 1), "phrases": len(own["phrases"]),
                       "sounds": db.connect().execute("SELECT COUNT(*) FROM sound_finds WHERE voice_id=?",
                                                      (voice_id,)).fetchone()[0],
                       "datasets": len(own["datasets"]), "trainings": len(own["trainings"]),
                       "models": len(own["models"]), "outputs": len(own["outputs"]),
                       "performances": len(own["performances"]),
                       "cloud_runpod": sum(1 for t in cloud if t.get("target") != "colab"),
                       "cloud_colab": sum(1 for t in cloud if t.get("target") == "colab")},
            "blockers": _blockers(voice_id, own)}


def _volumes() -> dict[str, str] | None:
    """The account's RunPod network volumes (id → datacenter); None when they cannot be listed."""
    try:
        return {v.get("id"): v.get("dataCenterId") or "" for v in runpod.volumes()}
    except Exception:
        return None


def _delete_cloud(tr: dict, vols: dict[str, str] | None) -> tuple[str | None, str | None]:
    """The run's files in the cloud: (still there: where and why, note). A volume the account no longer has took its
    files with it (RunPod's S3 API answers AccessDenied for it, not "not found"), so that is a note, not a failure.
    A volume that exists is reached in the datacenter RunPod lists it in, not the one recorded at the time."""
    vol = (tr.get("storage") or {}).get("volume") or ""
    where = (f"Google 雲端硬碟的 jobs/{tr['id']}" if tr.get("target") == "colab" else
             f"RunPod 網路磁碟 {vol} 的 {tr['remote_prefix']}/")
    try:
        if tr.get("target") == "colab":
            d = colab.job_dir(tr)
            shutil.rmtree(d, ignore_errors=True)
            return (f"Google 雲端硬碟 {d}（刪不掉，請手動刪除）" if d.exists() else None), None
        loc = dict(training._loc(tr))
        if vols is not None:
            if loc.get("volume") not in vols:
                return None, f"RunPod 網路磁碟 {loc.get('volume')} 已經不在你的帳號裡，上面的訓練檔案已經跟著磁碟刪掉了。"
            loc["datacenter"] = vols[loc["volume"]] or loc.get("datacenter")
        runpod.delete_run_folder(tr["remote_prefix"], loc)
        return None, None
    except Exception as e:
        why = ("RunPod 的 S3 金鑰沒有這個網路磁碟的權限；請到 runpod.io → Storage 確認磁碟還在，再到設定 → 雲端 GPU 檢查金鑰"
               if "AccessDenied" in str(e) else str(e)[:160])
        return f"{where}（{why}）", None


def _delete_output(o: dict) -> None:
    p = Path(o["path"])
    for f in (p, p.with_suffix(".mp3"), p.with_suffix(".json")):
        f.unlink(missing_ok=True)
    db.delete("outputs", o["id"])


def remove(voice_id: str) -> dict:
    from .api.data import _delete_source  # the recordings page's own delete (cancels its import, keeps outside files)
    from .api.perform import delete as delete_performance
    p = plan(voice_id)
    if p["blockers"]:
        raise Blocked("還有東西在用這個聲音，請先停止：" + "；".join(p["blockers"]))
    own = _owned(voice_id)
    left, notes = [], []
    vols = _volumes() if any(t.get("remote_prefix") and t.get("target") != "colab" for t in own["trainings"]) else None
    for tr in own["trainings"]:
        if tr.get("remote_prefix"):
            problem, note = _delete_cloud(tr, vols)
            left += [problem] if problem else []
            notes += [note] if note and note not in notes else []
        shutil.rmtree(config.DATA / "jobs" / tr["id"], ignore_errors=True)  # local work folder (dataset.tar, logs)
    for pid in own["performances"]:
        delete_performance(pid)
    for o in own["outputs"]:
        _delete_output(o)
    with db.tx() as c:
        if own["models"]:
            c.execute(f"UPDATE presets SET model_id=NULL WHERE model_id IN ({','.join('?' * len(own['models']))})",
                      own["models"])
    for mid in own["models"]:
        training.remove_model(mid)
    for did in own["datasets"]:
        datasets.remove(did)
    for pid in own["phrases"]:
        phrases.delete(pid)
    for sid in own["whole"]:
        _delete_source(sid)
    for s in db.query("SELECT path FROM segments WHERE voice_id=?", (voice_id,)):  # its clips in shared recordings
        Path(s["path"]).unlink(missing_ok=True)
    with db.tx() as c:
        c.execute("DELETE FROM segments WHERE voice_id=?", (voice_id,))
        c.execute("DELETE FROM sound_finds WHERE voice_id=?", (voice_id,))
        c.execute("DELETE FROM trainings WHERE voice_id=?", (voice_id,))
        c.execute("UPDATE sources SET voice_hint=NULL WHERE voice_hint=?", (voice_id,))
    shutil.rmtree(config.DATA / "voices" / voice_id, ignore_errors=True)  # consent document, enrollment, phrases
    db.delete("voices", voice_id)
    return {"ok": True, "deleted": p["counts"], "left": left, "notes": notes}


"""SQLite storage. One file (data/studio.db), one connection per thread, JSON columns for flexible fields."""
from __future__ import annotations

import json
import sqlite3
import threading
import time
import uuid
from contextlib import contextmanager

from . import config

SCHEMA = """
CREATE TABLE IF NOT EXISTS voices (
  id TEXT PRIMARY KEY, name TEXT NOT NULL, kind TEXT NOT NULL, languages TEXT NOT NULL DEFAULT '[]',
  notes TEXT NOT NULL DEFAULT '', consent TEXT, consent_doc TEXT, enrollment TEXT NOT NULL DEFAULT '[]',
  created_at REAL NOT NULL
);
CREATE TABLE IF NOT EXISTS sources (
  id TEXT PRIMARY KEY, filename TEXT NOT NULL, path TEXT NOT NULL, duration REAL, status TEXT NOT NULL,
  voice_hint TEXT, language TEXT, meta TEXT NOT NULL DEFAULT '{}', created_at REAL NOT NULL
);
CREATE TABLE IF NOT EXISTS segments (
  id TEXT PRIMARY KEY, source_id TEXT NOT NULL, voice_id TEXT, start REAL NOT NULL, "end" REAL NOT NULL,
  path TEXT NOT NULL, duration REAL NOT NULL, text TEXT NOT NULL DEFAULT '', text_alt TEXT NOT NULL DEFAULT '',
  lang TEXT, asr_agree REAL, spk_sim REAL, snr REAL, clip REAL, cluster INTEGER, score REAL,
  status TEXT NOT NULL DEFAULT 'pending', flags TEXT NOT NULL DEFAULT '[]', edited INTEGER NOT NULL DEFAULT 0
);
CREATE INDEX IF NOT EXISTS seg_voice ON segments(voice_id, status);
CREATE INDEX IF NOT EXISTS seg_source ON segments(source_id);
CREATE TABLE IF NOT EXISTS datasets (
  id TEXT PRIMARY KEY, voice_id TEXT NOT NULL, name TEXT NOT NULL, n_items INTEGER NOT NULL, hours REAL NOT NULL,
  path TEXT NOT NULL, meta TEXT NOT NULL DEFAULT '{}', created_at REAL NOT NULL
);
CREATE TABLE IF NOT EXISTS jobs (
  id TEXT PRIMARY KEY, kind TEXT NOT NULL, queue TEXT NOT NULL, status TEXT NOT NULL, progress REAL NOT NULL DEFAULT 0,
  message TEXT NOT NULL DEFAULT '', params TEXT NOT NULL DEFAULT '{}', result TEXT NOT NULL DEFAULT '{}',
  created_at REAL NOT NULL, started_at REAL, finished_at REAL, cancel INTEGER NOT NULL DEFAULT 0
);
CREATE TABLE IF NOT EXISTS trainings (
  id TEXT PRIMARY KEY, voice_id TEXT NOT NULL, dataset_id TEXT NOT NULL, engine TEXT NOT NULL, preset TEXT NOT NULL,
  target TEXT NOT NULL, status TEXT NOT NULL, pod_id TEXT, gpu TEXT, remote_prefix TEXT, progress TEXT NOT NULL DEFAULT '{}',
  cost_estimate REAL, job_id TEXT, created_at REAL NOT NULL, finished_at REAL
);
CREATE TABLE IF NOT EXISTS models (
  id TEXT PRIMARY KEY, voice_id TEXT NOT NULL, engine TEXT NOT NULL, name TEXT NOT NULL, training_id TEXT,
  path TEXT NOT NULL, meta TEXT NOT NULL DEFAULT '{}', metrics TEXT NOT NULL DEFAULT '{}', created_at REAL NOT NULL
);
CREATE TABLE IF NOT EXISTS outputs (
  id TEXT PRIMARY KEY, model_id TEXT, text TEXT NOT NULL, params TEXT NOT NULL DEFAULT '{}', path TEXT NOT NULL,
  duration REAL, score TEXT NOT NULL DEFAULT '{}', favorite INTEGER NOT NULL DEFAULT 0, batch TEXT, created_at REAL NOT NULL
);
CREATE TABLE IF NOT EXISTS catchphrases (
  id TEXT PRIMARY KEY, voice_id TEXT NOT NULL, text TEXT NOT NULL, variants TEXT NOT NULL DEFAULT '[]', lang TEXT,
  clips TEXT NOT NULL DEFAULT '[]', checks TEXT NOT NULL DEFAULT '{}', created_at REAL NOT NULL
);
CREATE INDEX IF NOT EXISTS phrase_voice ON catchphrases(voice_id);
CREATE TABLE IF NOT EXISTS presets (
  id TEXT PRIMARY KEY, name TEXT NOT NULL, source TEXT NOT NULL, model_id TEXT, data TEXT NOT NULL, created_at REAL NOT NULL
);
"""

JSON_COLS = {"languages", "consent", "enrollment", "meta", "flags", "params", "result", "preset", "progress",
             "metrics", "score", "data", "storage", "variants", "clips", "checks"}

_local = threading.local()


def connect() -> sqlite3.Connection:
    c = getattr(_local, "conn", None)
    if c is None:
        f = config.path("studio.db")
        c = sqlite3.connect(f, timeout=30, check_same_thread=False)
        c.row_factory = sqlite3.Row
        c.execute("PRAGMA journal_mode=WAL")
        c.execute("PRAGMA foreign_keys=ON")
        c.executescript(SCHEMA)
        _migrate(c)
        _local.conn = c
    return c


# columns added after the first release: (table, column, declaration)
MIGRATIONS = [
    ("trainings", "storage", "TEXT NOT NULL DEFAULT '{}'"),   # volume + datacenter frozen at start
    ("trainings", "deadline", "REAL"),                        # absolute time the pod must be gone by
    ("trainings", "pod_state", "TEXT"),                       # creating / running / removed / remove_failed
    ("trainings", "started_at", "REAL"),
    ("trainings", "cost_per_hr", "REAL"),
    ("trainings", "note", "TEXT NOT NULL DEFAULT ''"),
    ("segments", "asr_logprob", "REAL"),                      # primary ASR confidence (average log-probability)
    ("segments", "no_speech", "REAL"),                        # primary ASR: probability the clip is not speech
    ("segments", "emotion", "TEXT"),                          # emotion / delivery label (see emotions.py)
    ("sources", "emotion", "TEXT"),                           # label applied to every segment of the recording
]


def _migrate(c: sqlite3.Connection) -> None:
    for table, col, decl in MIGRATIONS:
        cols = {r[1] for r in c.execute(f"PRAGMA table_info({table})")}
        if col not in cols:
            c.execute(f"ALTER TABLE {table} ADD COLUMN {col} {decl}")
    if not c.execute("SELECT 1 FROM sqlite_master WHERE type='index' AND name='models_training'").fetchone():
        # older databases may hold two models for one training (the bug this index prevents): keep the first as
        # the training's model, keep the others as models too, recording the link in their meta instead
        dups = c.execute("SELECT id, training_id, meta FROM models WHERE training_id IN (SELECT training_id FROM models "
                         "WHERE training_id IS NOT NULL GROUP BY training_id HAVING COUNT(*) > 1) "
                         "ORDER BY training_id, created_at").fetchall()
        seen: set = set()
        for mid, tid, meta in dups:
            if tid in seen:
                m = json.loads(meta or "{}")
                m["duplicate_of_training"] = tid
                c.execute("UPDATE models SET training_id=NULL, meta=? WHERE id=?", (json.dumps(m, ensure_ascii=False), mid))
            seen.add(tid)
        c.execute("CREATE UNIQUE INDEX models_training ON models(training_id) WHERE training_id IS NOT NULL")
    c.commit()


def reset_connection() -> None:
    c = getattr(_local, "conn", None)
    if c is not None:
        c.close()
        _local.conn = None


@contextmanager
def tx():
    c = connect()
    try:
        yield c
        c.commit()
    except Exception:
        c.rollback()
        raise


def new_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:12]}"


def now() -> float:
    return time.time()


def row(r: sqlite3.Row | None) -> dict | None:
    if r is None:
        return None
    d = dict(r)
    for k in JSON_COLS & d.keys():
        if isinstance(d[k], str):
            try:
                d[k] = json.loads(d[k])
            except json.JSONDecodeError:
                pass
    return d


def rows(rs) -> list[dict]:
    return [row(r) for r in rs]


def dump(v):
    return json.dumps(v, ensure_ascii=False) if not isinstance(v, str) else v


def insert(table: str, data: dict) -> dict:
    cols = list(data)
    vals = [dump(data[k]) if k in JSON_COLS else data[k] for k in cols]
    q = f'INSERT INTO {table} ({", ".join(chr(34) + c + chr(34) for c in cols)}) VALUES ({", ".join("?" * len(cols))})'
    with tx() as c:
        c.execute(q, vals)
    return get(table, data["id"])


def update(table: str, id_: str, data: dict) -> dict | None:
    if not data:
        return get(table, id_)
    cols = list(data)
    vals = [dump(data[k]) if k in JSON_COLS else data[k] for k in cols]
    q = f'UPDATE {table} SET {", ".join(chr(34) + c + chr(34) + "=?" for c in cols)} WHERE id=?'
    with tx() as c:
        c.execute(q, vals + [id_])
    return get(table, id_)


def get(table: str, id_: str) -> dict | None:
    return row(connect().execute(f"SELECT * FROM {table} WHERE id=?", (id_,)).fetchone())


def query(sql: str, args=()) -> list[dict]:
    return rows(connect().execute(sql, args).fetchall())


def delete(table: str, id_: str) -> None:
    with tx() as c:
        c.execute(f"DELETE FROM {table} WHERE id=?", (id_,))

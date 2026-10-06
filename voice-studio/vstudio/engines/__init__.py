"""Engine registry. Real engines are added here as adapters (see base.Engine)."""
from __future__ import annotations

from .base import MODES, Engine
from .mock import MockEngine
from .qwen3 import Qwen3Engine
from .voxcpm2 import VoxCPM2Engine

REGISTRY: dict[str, Engine] = {}


def register(engine: Engine) -> None:
    REGISTRY[engine.id] = engine


def get(engine_id: str) -> Engine:
    if engine_id not in REGISTRY:
        raise KeyError(f"未知的引擎：{engine_id}")
    return REGISTRY[engine_id]


def all_engines() -> list[Engine]:
    return list(REGISTRY.values())


register(VoxCPM2Engine())
register(Qwen3Engine())
register(MockEngine())

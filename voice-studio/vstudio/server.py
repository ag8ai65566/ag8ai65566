"""The web app: API under /api, the built web UI everywhere else."""
from __future__ import annotations

import ipaddress
import os
import secrets as _secrets
import webbrowser
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse

from . import __version__, config, db, evaluate, jobs, training, tts  # noqa: F401  (modules register job handlers)
from .api import data, docs, speak, system, train, voices
from .engines import install  # noqa: F401  (registers install_engine)
from .pipeline import prepare  # noqa: F401  (registers prepare_source / enroll_voice)

WEB = config.ROOT / "web" / "dist"


def create_app() -> FastAPI:
    config.ensure_dirs()
    db.connect()

    @asynccontextmanager
    async def lifespan(_app):
        jobs.start()
        try:
            training.resume_interrupted()
        except Exception:  # never block start-up on the cloud
            pass
        yield
        jobs.stop()

    app = FastAPI(title="Voice Studio", version=__version__, lifespan=lifespan)
    for r in (voices.router, data.router, train.router, speak.router, system.router, docs.router):
        app.include_router(r)

    password = os.environ.get("VSTUDIO_PASSWORD", "")

    @app.middleware("http")
    async def guard(request: Request, call_next):
        """Loopback is trusted. Any other client needs VSTUDIO_PASSWORD (when the studio is opened to a network)."""
        host = request.client.host if request.client else "127.0.0.1"
        try:
            local = ipaddress.ip_address(host).is_loopback
        except ValueError:
            local = host in ("localhost", "testclient")
        if not local:
            given = request.headers.get("x-studio-password") or request.cookies.get("studio_pw") or ""
            if not password or not _secrets.compare_digest(given, password):
                return JSONResponse({"detail": "需要密碼"}, status_code=401)
        return await call_next(request)

    @app.get("/api/health")
    def health():
        return {"ok": True, "version": __version__}

    @app.get("/{full_path:path}")
    def spa(full_path: str):
        if full_path.startswith("api/"):
            return JSONResponse({"detail": "Not Found"}, status_code=404)
        f = (WEB / full_path).resolve()
        if full_path and f.is_file() and WEB.resolve() in f.parents:
            return FileResponse(f)
        index = WEB / "index.html"
        if index.exists():
            return FileResponse(index)
        return JSONResponse({"detail": "web UI not built: run `npm run build` in web/"}, status_code=404)

    return app


app = create_app()


def main() -> None:
    import uvicorn
    st = config.load_settings()
    host, port = os.environ.get("VSTUDIO_HOST", st["host"]), int(os.environ.get("VSTUDIO_PORT", st["port"]))
    if os.environ.get("VSTUDIO_NO_BROWSER") != "1":
        import threading
        threading.Timer(1.5, lambda: webbrowser.open(f"http://127.0.0.1:{port}")).start()
    uvicorn.run(app, host=host, port=port, log_level="warning")


if __name__ == "__main__":
    main()

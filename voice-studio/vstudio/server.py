"""The web app: API under /api, the built web UI everywhere else."""
from __future__ import annotations

import os
import secrets as _secrets
import webbrowser
from contextlib import asynccontextmanager
from urllib.parse import unquote

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse

from . import __version__, config, db, evaluate, jobs, training, tts  # noqa: F401  (modules register job handlers)
from .api import data, docs, speak, system, train, voices
from .engines import install  # noqa: F401  (registers install_engine)
from .pipeline import prepare  # noqa: F401  (registers prepare_source / enroll_voice)

WEB = config.ROOT / "web" / "dist"


def _quiet(fn) -> None:
    try:
        fn()
    except Exception:
        pass


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
        import threading  # retry failed pod removals and look for orphaned pods, without delaying start-up
        threading.Thread(target=lambda: _quiet(training.reap), name="reap", daemon=True).start()
        yield
        jobs.stop()

    app = FastAPI(title="Voice Studio", version=__version__, lifespan=lifespan)
    for r in (voices.router, data.router, train.router, speak.router, system.router, docs.router):
        app.include_router(r)

    password = os.environ.get("VSTUDIO_PASSWORD", "")
    local_hosts = {"localhost", "127.0.0.1", "[::1]", "testserver"}
    extra_hosts = {h.strip().lower() for h in os.environ.get("VSTUDIO_ALLOWED_HOSTS", "").split(",") if h.strip()}

    def _hostname(value: str) -> str:
        v = value.strip().lower()
        if v.startswith("["):
            return v.split("]")[0] + "]"
        return v.rsplit(":", 1)[0] if v.count(":") == 1 else v

    @app.middleware("http")
    async def guard(request: Request, call_next):
        """Who may use the API.

        - Default (only this computer): the Host header must name this computer, which blocks DNS-rebinding pages,
          and requests from another website's page (a foreign Origin) are refused, so no site can drive the API.
        - Network mode (VSTUDIO_PASSWORD set): every API request needs the password, whatever its address.
        The web page itself (not /api) is served to anyone who can reach the port, so the login prompt can load."""
        host = _hostname(request.headers.get("host", ""))
        is_api = request.url.path.startswith("/api/")
        if not password and host not in local_hosts | extra_hosts:
            return JSONResponse({"detail": "不允許的主機名稱"}, status_code=403)
        origin = request.headers.get("origin")
        if origin and request.method not in ("GET", "HEAD", "OPTIONS"):
            if _hostname(origin.split("://", 1)[-1]) != host:
                return JSONResponse({"detail": "不允許跨網站的請求"}, status_code=403)
        if password and is_api and request.url.path != "/api/health":
            given = request.headers.get("x-studio-password") or unquote(request.cookies.get("studio_pw") or "")
            if not _secrets.compare_digest(given, password):
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

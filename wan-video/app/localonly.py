"""Only this app's own page may tell it to do things.

Why this exists
---------------
The server listens on 127.0.0.1, which keeps other computers out - but not
other web pages open in the same browser. Any page can send a "simple" POST
(no CORS preflight) to http://127.0.0.1:8000, and FastAPI runs a POST that has
no body with the endpoint's defaults. So a page you merely visited could have
emptied the library, queued 40GB of downloads, opened a PowerShell window or
started a paid cloud GPU. DNS rebinding goes further: a site that points its
own name at 127.0.0.1 is "same origin" with this server and can read the
answers too.

Two checks close both, and they only apply to browsers, because only a browser
can be made to send a request by a page someone else wrote:

* **Host** must be this machine as the browser addressed it: ``localhost``,
  an IP address, or a name listed in ``ALLOWED_HOSTS``. Rebinding needs the
  attacker's own domain name in Host, so this refuses it whatever the method.
* **Where the request came from.** Sec-Fetch-Site (sent by every current
  browser, and impossible for a page to forge) must say same-origin - except
  for simply opening the app from a link or bookmark. Anything that changes
  something must also carry an Origin, when there is one, equal to the Host.

The drop-folder watcher, curl and other scripts send none of the browser
headers and pass untouched - in Docker the watcher reaches the app as
``app:8000``, which a Host rule for browsers must not break.

``ALLOWED_HOSTS=*`` switches the Host check off, for people who put the app
behind their own reverse proxy and know why.
"""

from __future__ import annotations

import ipaddress
import json
import os
from urllib.parse import urlsplit

SAFE_METHODS = frozenset({"GET", "HEAD", "OPTIONS"})


def _hostname(host: str) -> str:
    """The name part of a Host header: no port, no IPv6 brackets."""
    host = host.strip().lower()
    if host.startswith("["):
        return host[1:].split("]", 1)[0]
    if host.count(":") == 1:
        return host.split(":", 1)[0]
    return host


def extra_hosts() -> set[str]:
    raw = os.environ.get("ALLOWED_HOSTS", "")
    return {h.strip().lower() for h in raw.split(",") if h.strip()}


def host_allowed(host: str) -> bool:
    extra = extra_hosts()
    if "*" in extra:
        return True
    name = _hostname(host)
    if not name:
        return False
    if name == "localhost" or name.endswith(".localhost") or name in extra:
        return True
    try:
        ipaddress.ip_address(name)
        return True
    except ValueError:
        return False


def from_browser(headers: dict[str, str]) -> bool:
    return ("sec-fetch-site" in headers or "origin" in headers
            or headers.get("user-agent", "").startswith("Mozilla/"))


def problem(method: str, headers: dict[str, str]) -> str | None:
    """Why this request is refused, or None. `headers` has lower-case names."""
    if not from_browser(headers):
        return None
    host = headers.get("host", "")
    if not host_allowed(host):
        return (f"這個 app 只接受用本機位址打開（例如 http://127.0.0.1:8000）。"
                f"「{_hostname(host)}」不是。如果你是刻意用這個名字連進來的，"
                "在 .env 加一行 ALLOWED_HOSTS=這個名字。")
    site = headers.get("sec-fetch-site")
    if site in ("cross-site", "same-site"):
        opening = method in SAFE_METHODS and headers.get("sec-fetch-mode") == "navigate"
        if not opening:
            return "這個請求是別的網站送來的，已經擋下。請直接在這個 app 的頁面上操作。"
    if method not in SAFE_METHODS:
        origin = headers.get("origin")
        if origin is not None:
            if origin == "null" or urlsplit(origin).netloc.lower() != host.strip().lower():
                return "這個請求是別的網站送來的，已經擋下。請直接在這個 app 的頁面上操作。"
    return None


class LocalOnly:
    """ASGI middleware around the whole app (pages, API and files alike)."""

    def __init__(self, app) -> None:
        self.app = app

    async def __call__(self, scope, receive, send) -> None:
        if scope.get("type") == "http":
            headers = {k.decode("latin-1").lower(): v.decode("latin-1")
                       for k, v in scope.get("headers") or []}
            reason = problem(scope.get("method", "GET"), headers)
            if reason:
                body = json.dumps({"detail": reason}, ensure_ascii=False).encode("utf-8")
                await send({"type": "http.response.start", "status": 403,
                            "headers": [(b"content-type", b"application/json; charset=utf-8"),
                                        (b"content-length", str(len(body)).encode("ascii"))]})
                await send({"type": "http.response.body", "body": body})
                return
        await self.app(scope, receive, send)

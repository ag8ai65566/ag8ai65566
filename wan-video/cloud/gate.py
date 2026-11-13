#!/usr/bin/env python3
"""The front door of ComfyUI on the rented machine.

Why this exists
---------------
A Runpod address (``https://<pod>-8188.proxy.runpod.net``) is reachable by
anyone on the internet who has it, and ComfyUI has no login of any kind. Left
as it is, whoever learns the address can queue their own jobs on a card the
user is paying for by the second, and can read every picture and clip the
machine has produced.

So ComfyUI is started listening on this machine only (127.0.0.1), and this
file is the one thing that listens to the outside. It lets a request through
when it carries the token the app generated for this machine, and answers 401
to everything else. It is not clever: it does not understand ComfyUI's API, it
copies bytes in both directions, websocket included.

It runs inside ComfyUI's own Python environment, because that already has
aiohttp - ComfyUI is built on it - so there is nothing extra to install.

The token is the same one the agent uses. It is read from the environment and
never written to a log.
"""

from __future__ import annotations

import argparse
import asyncio
import hmac
import os

import aiohttp
from aiohttp import web

VERSION = "1"

# Headers that describe one hop of the connection rather than the request, plus
# the two this file must not forward: the token itself (ComfyUI has no use for
# it, and its logs should never see it) and Origin (ComfyUI refuses a request
# whose Origin does not match the address it is listening on, which behind a
# proxy it never does).
DROP_REQUEST = {
    "connection", "keep-alive", "proxy-authenticate", "proxy-authorization", "te",
    "trailers", "transfer-encoding", "upgrade", "host", "content-length",
    "x-wan-token", "authorization", "origin",
    "sec-websocket-key", "sec-websocket-version", "sec-websocket-extensions",
    "sec-websocket-protocol", "sec-websocket-accept",
}
DROP_RESPONSE = {
    "connection", "keep-alive", "proxy-authenticate", "proxy-authorization", "te",
    "trailers", "transfer-encoding", "upgrade", "content-length", "content-encoding",
}


def presented(request: web.Request) -> str:
    """The token a request carries, from either header it may be in.

    Two headers because the request crosses somebody else's proxy on the way
    here: if one of them were ever stripped in transit, the other still works.
    """
    given = request.headers.get("X-Wan-Token") or ""
    if given:
        return given
    bearer = request.headers.get("Authorization") or ""
    return bearer[7:].strip() if bearer.lower().startswith("bearer ") else ""


def make_app(token: str, upstream: str) -> web.Application:
    async def start(app: web.Application) -> None:
        # No total timeout: a websocket lives as long as a render does. Nothing
        # is decompressed either - bytes are passed on exactly as received.
        app["session"] = aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=None, sock_connect=10),
            auto_decompress=False)

    async def stop(app: web.Application) -> None:
        await app["session"].close()

    async def websocket(request: web.Request, headers: dict) -> web.StreamResponse:
        session: aiohttp.ClientSession = request.app["session"]
        outside = web.WebSocketResponse(max_msg_size=0)
        await outside.prepare(request)
        try:
            inside = await session.ws_connect(
                f"ws://{upstream}{request.rel_url}", headers=headers, max_msg_size=0)
        except aiohttp.ClientError:
            await outside.close(code=1011, message=b"ComfyUI is not up")
            return outside

        async def pump(source, sink) -> None:
            async for message in source:
                if message.type == aiohttp.WSMsgType.TEXT:
                    await sink.send_str(message.data)
                elif message.type == aiohttp.WSMsgType.BINARY:
                    await sink.send_bytes(message.data)
                else:
                    break

        # Whichever side hangs up first ends both; a half-open pair would hold
        # a connection to ComfyUI that nobody is reading.
        tasks = [asyncio.ensure_future(pump(outside, inside)),
                 asyncio.ensure_future(pump(inside, outside))]
        try:
            await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
        finally:
            for task in tasks:
                task.cancel()
            await inside.close()
            await outside.close()
        return outside

    async def handle(request: web.Request) -> web.StreamResponse:
        if not hmac.compare_digest(presented(request).encode(), token.encode()):
            return web.json_response({"error": "token 不對"}, status=401)
        headers = {k: v for k, v in request.headers.items() if k.lower() not in DROP_REQUEST}
        if request.headers.get("Upgrade", "").lower() == "websocket":
            return await websocket(request, headers)

        session: aiohttp.ClientSession = request.app["session"]
        body = request.content if request.can_read_body else None
        try:
            async with session.request(request.method, f"http://{upstream}{request.rel_url}",
                                       headers=headers, data=body,
                                       allow_redirects=False) as answer:
                response = web.StreamResponse(status=answer.status, headers={
                    k: v for k, v in answer.headers.items()
                    if k.lower() not in DROP_RESPONSE})
                # Content-Encoding was dropped above along with the length; put
                # it back, since the bytes are forwarded still compressed.
                if "Content-Encoding" in answer.headers:
                    response.headers["Content-Encoding"] = answer.headers["Content-Encoding"]
                await response.prepare(request)
                async for chunk in answer.content.iter_chunked(1 << 16):
                    await response.write(chunk)
                await response.write_eof()
                return response
        except aiohttp.ClientConnectorError:
            return web.json_response(
                {"error": "ComfyUI 還沒起來（或正在重新啟動）"}, status=502)

    app = web.Application(client_max_size=1 << 30)
    app.on_startup.append(start)
    app.on_cleanup.append(stop)
    app.router.add_route("*", "/{tail:.*}", handle)
    return app


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument("--port", type=int, default=int(os.environ.get("WAN_COMFY_PORT", "8188")))
    parser.add_argument("--host", default="0.0.0.0")
    parser.add_argument("--upstream", default="127.0.0.1:8187")
    args = parser.parse_args()

    token = (os.environ.get("WAN_AGENT_TOKEN") or "").strip()
    if len(token) < 16:
        # Same rule as the agent: with no token this would be an open door, and
        # an open door is exactly what this file exists to prevent.
        raise SystemExit("WAN_AGENT_TOKEN is missing or too short; refusing to start.")
    print(f"wan gate {VERSION} on {args.host}:{args.port} -> {args.upstream}", flush=True)
    web.run_app(make_app(token, args.upstream), host=args.host, port=args.port,
                print=None, access_log=None)


if __name__ == "__main__":
    main()

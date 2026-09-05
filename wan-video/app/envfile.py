"""Reading and writing the `.env` file the start scripts feed into the process.

The CivitAI API key was the one setting the app told you to go and edit a file
for, then restart, with no explanation of how. That is a bad enough experience
for the one setting that gates every download, so it gets a text box instead -
which means something has to write the file back without destroying whatever
else is in it.

Rewriting is line-based on purpose. A parse-and-regenerate would silently drop
the comments the file ships with, and those comments are the documentation for
every other setting.
"""

from __future__ import annotations

import os
import re
from pathlib import Path

# Only these can be set from the browser. An open key/value writer into the
# process environment is a much larger thing than a settings box.
WRITABLE = {
    "CIVITAI_API_KEY": {
        "label": "CivitAI API key",
        "secret": True,
        "restart": False,   # civitai.api_key() reads os.environ on every call
        "help": "到 civitai.com → 右上頭像 → Account settings → API Keys → 產生一個貼進來。"
                "沒有它可以搜尋，但不能下載任何 LoRA 或模型。",
    },
    "HF_TOKEN": {
        "label": "Hugging Face access token",
        "secret": True,
        "restart": False,   # downloader reads os.environ on every request
        "help": "只有**閘門式（gated）**的模型需要，例如 LTX-2.5。"
                "到 huggingface.co → 右上頭像 → Settings → Access Tokens → "
                "New token（read 權限就夠）。"
                "**拿到 token 還不夠**：還要去那個模型的頁面按一次同意授權，"
                "否則一樣是 401。",
    },
    "COMFY_ARGS": {
        "label": "ComfyUI 啟動參數",
        "secret": False,
        "restart": True,    # only read when ComfyUI is launched
        "help": "顯存不夠時填 --lowvram，差很多就填 --novram。改完要重開 ComfyUI 才生效。",
    },
}

LINE = re.compile(r"^\s*(?:export\s+)?([A-Za-z_][A-Za-z0-9_]*)\s*=(.*)$")


def path() -> Path:
    """Where `.env` lives: next to the start scripts, above app/."""
    return Path(os.environ.get("ENV_FILE") or (Path(__file__).resolve().parents[1] / ".env"))


def _strip(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def read(file: Path | None = None) -> dict[str, str]:
    target = file or path()
    out: dict[str, str] = {}
    try:
        text = target.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeDecodeError):
        return out
    for line in text.splitlines():
        if line.lstrip().startswith("#"):
            continue
        if m := LINE.match(line):
            out[m.group(1)] = _strip(m.group(2))
    return out


def mask(value: str) -> str:
    """Enough to recognise which key it is, not enough to use it."""
    value = (value or "").strip()
    if not value:
        return ""
    if len(value) <= 8:
        return "•" * len(value)
    return f"{value[:4]}{'•' * 8}{value[-4:]}"


def write(name: str, value: str, file: Path | None = None) -> None:
    """Set one variable, keeping every other line - comments included - as-is.

    An empty value removes the line rather than leaving `KEY=`, because an empty
    string and an unset variable read the same to os.environ but only one of
    them looks deliberate when you open the file later.
    """
    if name not in WRITABLE:
        raise ValueError(f"不能從網頁設定這個：{name}")
    value = (value or "").strip()
    if "\n" in value or "\r" in value:
        raise ValueError("這個值不能有換行")

    target = file or path()
    try:
        text = target.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeDecodeError):
        text = ""
    # Windows editors and the start script both cope with \n, and mixing the two
    # inside one file is what produces a stray blank line every other save.
    newline = "\r\n" if "\r\n" in text else "\n"
    lines = text.splitlines()

    replaced = False
    out: list[str] = []
    for line in lines:
        m = LINE.match(line)
        if m and m.group(1) == name and not line.lstrip().startswith("#"):
            if replaced:
                continue           # a duplicate of a key we already rewrote
            if value:
                out.append(f"{name}={value}")
            replaced = True
            continue
        out.append(line)
    if value and not replaced:
        if out and out[-1].strip():
            out.append("")
        out.append(f"{name}={value}")

    target.parent.mkdir(parents=True, exist_ok=True)
    body = newline.join(out).rstrip(newline) + (newline if out else "")
    # Written next door and moved into place, so a full disk or a crash cannot
    # leave a half-written .env - which would take every other setting with it.
    temp = target.with_name(target.name + ".tmp")
    temp.write_text(body, encoding="utf-8", newline="")
    temp.replace(target)

    if value:
        os.environ[name] = value
    else:
        os.environ.pop(name, None)


def state(file: Path | None = None) -> list[dict]:
    """What the settings page shows: set or not, masked, and what it needs."""
    stored = read(file)
    out = []
    for name, meta in WRITABLE.items():
        # The live process value wins: it is what the app is actually using,
        # and it may have been set in the shell rather than in the file.
        live = (os.environ.get(name) or "").strip() or stored.get(name, "")
        out.append({
            "name": name, "label": meta["label"], "help": meta["help"],
            "secret": meta["secret"], "needs_restart": meta["restart"],
            "set": bool(live),
            "value": mask(live) if meta["secret"] else live,
        })
    return out

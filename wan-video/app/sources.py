"""Where a model file comes from, given only its name.

Why this exists
---------------
A rented machine starts with no models. When a graph is checked against it,
ComfyUI's answer is a list of filenames it does not have - and that is all it
is, a list of names. Something has to turn `wan2.2_vae.safetensors` back into
"this URL, this folder, this many bytes".

Every catalogue in this app already holds that - video models, image
checkpoints, upscalers, frame interpolators, ControlNets - each in its own
module. This file is the one place that reads all of them by filename, so the
cloud path does not grow a fifth copy of the list.

Two kinds of answer
-------------------
* **A download.** The file is in a catalogue, so the machine fetches it itself
  at data-centre speed. This is the normal case and the fast one.
* **An upload.** The file is not in any catalogue - a LoRA the user trained or
  installed by hand - but it is on this computer, so it is pushed up from here.
  Slower, bounded by the user's own connection, and always exactly the file
  they have rather than something with the same name.

If it is neither, there is no answer, and the caller says so by name rather
than starting a job that will fail on the first loader node.

Credentials
-----------
The headers attached to a download are the same ones the local downloader
would send, built by the same functions: the Hugging Face token goes only to
Hugging Face files, the CivitAI key only to CivitAI ones.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import civitai
import controlnets
import downloader
import images
import registry
import upscalers

MODEL_SUFFIXES = (".safetensors", ".gguf", ".sft", ".ckpt", ".pt", ".pth", ".bin", ".onnx")


@dataclass(frozen=True)
class Source:
    """One file the rented machine needs, and how it gets there."""

    name: str
    folder: str
    size: int = 0
    url: str = ""                 # set for a download
    headers: tuple[tuple[str, str], ...] = ()
    local: Path | None = None     # set for an upload
    label: str = ""

    @property
    def is_upload(self) -> bool:
        return self.local is not None

    def public(self) -> dict:
        """For the progress line. Never includes the headers."""
        return {"name": self.name, "folder": self.folder, "size": self.size,
                "how": "upload" if self.is_upload else "download"}


def looks_like_model_file(value: str) -> bool:
    return str(value).lower().endswith(MODEL_SUFFIXES)


def _from_model_file(file: registry.ModelFile, label: str = "") -> Source:
    return Source(name=file.name, folder=file.folder, size=file.size,
                  url=downloader.url_for(file),
                  headers=tuple(downloader.headers_for(file).items()), label=label)


def catalogue() -> dict[str, Source]:
    """Every file any catalogue knows how to fetch, keyed by filename.

    Built on each call rather than cached: the headers carry whatever token is
    in the environment *now*, and a key pasted into settings a minute ago has
    to be the one that gets used.
    """
    found: dict[str, Source] = {}

    def add(source: Source) -> None:
        # First one wins. The same file is shared between models on purpose
        # (one text encoder, one VAE), and every listing of it is identical.
        found.setdefault(source.name, source)

    for model in registry.MODELS:
        for file in model.all_files:
            add(_from_model_file(file, model.label))

    for model in images.IMAGE_MODELS:
        for file in model.all_files:
            if model.civitai_version and file is model.file:
                key = civitai.api_key()
                headers = (("User-Agent", civitai.UA), ("Authorization", f"Bearer {key}")) if key else ()
                add(Source(
                    name=file.name, folder=file.folder, size=file.size,
                    url=f"https://civitai.com/api/download/models/{model.civitai_version}",
                    headers=headers, label=model.label))
            elif file.repo:
                add(_from_model_file(file, model.label))

    for item in upscalers.UPSCALERS:
        add(_from_model_file(item.file, item.label))
    for item in upscalers.INTERPOLATORS:
        add(_from_model_file(item.file, item.label))
    for item in controlnets.CONTROLNETS:
        add(_from_model_file(item.file, item.label))
    return found


def needs_civitai_key(source: Source) -> bool:
    return "civitai.com" in source.url and not source.headers


def on_disk(value: str, models_dir: Path) -> Source | None:
    """A file the user has locally, as something that can be pushed up.

    `value` is what the graph says, which for a file in a subfolder is a
    relative path (`anime/style.safetensors`). The folder on the machine is
    wherever it sits here, relative to the models directory - ComfyUI's layout
    is the same on both ends, so mirroring it is the whole mapping.
    """
    wanted = str(value).replace("\\", "/").strip("/")
    if not wanted or not models_dir.is_dir():
        return None
    base = wanted.rsplit("/", 1)[-1]
    for path in sorted(models_dir.rglob(base)):
        if not path.is_file():
            continue
        relative = path.relative_to(models_dir).as_posix()
        if relative == wanted or relative.endswith("/" + wanted):
            return Source(name=path.name,
                          folder=path.parent.relative_to(models_dir).as_posix(),
                          size=path.stat().st_size, local=path, label="你電腦上的檔案")
    return None


def find(value: str, models_dir: Path) -> Source | None:
    """How to get this file onto the machine, or None if nobody knows.

    A file on this computer wins over the catalogue when both exist *and* the
    catalogue has no size to check it against - but a catalogued file is
    always downloaded rather than uploaded, because the machine can fetch
    38GB in the time this connection uploads one.
    """
    base = str(value).replace("\\", "/").rsplit("/", 1)[-1]
    known = catalogue().get(base)
    if known is not None:
        return known
    return on_disk(value, models_dir)

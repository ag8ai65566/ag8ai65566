#!/usr/bin/env python3
"""Check every catalogued file size against what Hugging Face actually serves.

Why this is a script and not a test
-----------------------------------
A wrong size is not cosmetic. `downloader.file_status` compares the bytes on
disk to the catalogued number *exactly*, so a file that is off by even one byte
downloads completely, is judged "partial" forever, and gets fetched again on
every run - and the model it belongs to never reports as installed.

That is exactly what happened to the LTX-2.3 spatial upscaler: catalogued as
1002438656, actually 995743560. Nobody would have found it by reading the file.

It is not part of the test suite because it needs the network and hits ~100
URLs, which would make the suite slow and flaky. Run it after touching the
registry, and whenever a download refuses to finish:

    python scripts/verify_sizes.py

Gated repositories answer 401 to an anonymous request even though the file is
there. Those are reported separately: a gated file is expected to be
unreachable here, and is only a problem if the entry does not say `gated=True`.
"""

from __future__ import annotations

import concurrent.futures as futures
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

import images  # noqa: E402
import registry  # noqa: E402

TIMEOUT = 45


def served_size(repo: str, path: str) -> int:
    """What Hugging Face says the file is, or -1 if it would not say."""
    url = f"https://huggingface.co/{repo}/resolve/main/{path}"
    try:
        with urllib.request.urlopen(
                urllib.request.Request(url, method="HEAD"), timeout=TIMEOUT) as r:
            return int(r.headers.get("content-length") or 0)
    except Exception:  # noqa: BLE001 - any failure means "could not check"
        return -1


def main() -> int:
    jobs = []
    for model in list(registry.MODELS) + list(images.IMAGE_MODELS):
        for f in model.all_files:
            if getattr(f, "repo", ""):
                jobs.append((model.id, f))

    print(f"checking {len(jobs)} catalogued files against huggingface…\n")
    wrong: list[str] = []
    unchecked: list[str] = []
    with futures.ThreadPoolExecutor(max_workers=12) as pool:
        submitted = {pool.submit(served_size, f.repo, f.path): (mid, f)
                     for mid, f in jobs}
        for done in futures.as_completed(submitted):
            model_id, f = submitted[done]
            served = done.result()
            if served <= 0:
                line = f"{model_id:16s} {f.name[:56]:56s} unreachable"
                (unchecked if f.gated else wrong).append(
                    line + ("  (gated - expected)" if f.gated else
                            "  NOT MARKED GATED"))
                continue
            # Exact, because file_status is exact.
            if served != f.size:
                wrong.append(f"{model_id:16s} {f.name[:56]:56s} "
                             f"catalogued={f.size} served={served} "
                             f"(off by {served - f.size:+d})")

    for line in sorted(unchecked):
        print("  skipped   ", line)
    if unchecked:
        print()
    if wrong:
        print(f"{len(wrong)} PROBLEM(S):")
        for line in sorted(wrong):
            print("  ", line)
        print("\nA wrong size means the file downloads in full and is then judged")
        print("incomplete forever - fix the number in app/registry.py.")
        return 1
    print("every catalogued size matches what Hugging Face serves.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

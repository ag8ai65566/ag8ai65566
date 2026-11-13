"""Stands in for sd-scripts in tests: progress lines like tqdm, then a LoRA file.

Run by the agent as `python fake_trainer.py <out_dir> <name> <total_steps>`
when WAN_TRAIN_CMD points here. FAKE_TRAIN_FAIL=1 makes it exit non-zero.
"""
import os
import sys
import time
from pathlib import Path

out_dir, name, total = Path(sys.argv[1]), sys.argv[2], int(sys.argv[3])
for step in range(0, total + 1, max(1, total // 4)):
    print(f"steps: {step * 100 // total:3d}%|####| {step}/{total} [00:01<00:01, 1.00it/s]", flush=True)
    time.sleep(0.05)
if os.environ.get("FAKE_TRAIN_FAIL"):
    print("CUDA out of memory", flush=True)
    sys.exit(3)
(out_dir / f"{name}.safetensors").write_bytes(b"\0" * 4096)
print("model saved.", flush=True)

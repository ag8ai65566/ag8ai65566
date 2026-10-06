"""Optional vocal separation (removes background music and game audio) with python-audio-separator.

The default model is BS-RoFormer (vocals), the strongest open separator in common use; it runs on the GPU. Turn it
on per import when a recording has music, game sound or a TV in the background. Clean voice-only recordings do not
need it, and separation can add its own artefacts.
"""
from __future__ import annotations

from pathlib import Path

DEFAULT_MODEL = "model_bs_roformer_ep_317_sdr_12.9755.ckpt"


def vocals(src: Path, out_dir: Path, model_name: str = DEFAULT_MODEL) -> Path:
    from audio_separator.separator import Separator  # installed with the "prep" extra
    from .. import config
    out_dir.mkdir(parents=True, exist_ok=True)
    sep = Separator(output_dir=str(out_dir), model_file_dir=str(config.DATA / "assets" / "separator"),
                    output_single_stem="Vocals", output_format="WAV")
    sep.load_model(model_filename=model_name)
    files = sep.separate(str(src))
    paths = [out_dir / Path(f).name for f in files]
    for p in paths:
        if "vocals" in p.name.lower():
            return p
    return paths[0]

"""VoxCPM2 (OpenBMB, 2026-04): the studio's primary engine.

Why it is the default (research of 2026-10, with GPT): Apache-2.0 code and weights; official LoRA and full
fine-tuning; Japanese and English among 30 languages; the highest speaker similarity of the open models in the
shared MiniMax multilingual comparison (ja SIM 82.8, en 85.4); 48 kHz output; about 8 GB of VRAM for inference.
Its weak spot is a somewhat higher word error rate than Qwen3-TTS, which the studio's best-of-N screening and
checkpoint scoring are there to catch.

Synthesis modes
- plain: the fine-tuned model alone; a parenthesised style note may lead the text, e.g. "(quiet, unhurried)…".
- ref:   adds a reference clip for timbre; style notes still work.
- hifi:  "ultimate cloning": reference clip + its exact transcript, the model continues from it, keeping rhythm,
         accent and habits closest to the recording. Style notes are ignored in this mode.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path

from . import export, remote
from .base import Engine, Synthesis, TrainPreset

REPO = "https://github.com/OpenBMB/VoxCPM.git"
COMMIT = "f0c787f0937dc1c9a8f4f64d9a332d9c5da2e629"  # main on 2026-09-30, after release 2.0.3
VERSION = "2.0.3.post1"
BASE = "openbmb/VoxCPM2"
IMAGE = "runpod/pytorch:2.8.0-py3.11-cuda12.8.1-cudnn-devel-ubuntu22.04"
GPU_48 = ["NVIDIA L40S", "NVIDIA RTX 6000 Ada Generation", "NVIDIA A100 80GB PCIe", "NVIDIA A100-SXM4-80GB"]
GPU_80 = ["NVIDIA A100 80GB PCIe", "NVIDIA A100-SXM4-80GB", "NVIDIA H100 PCIe", "NVIDIA H100 80GB HBM3"]


class VoxCPM2Engine(Engine):
    id = "voxcpm2"
    name = "VoxCPM2"
    summary = ("OpenBMB 2026 年 4 月發表，20 億參數、48 kHz、支援日文與英文等 30 種語言。公開評測中音色相似度最高，"
               "有官方 LoRA 與完整微調。「完整複製」模式會接著參考錄音說下去，最能保留口音、節奏和說話習慣。")
    license = "Apache-2.0"
    license_note = "程式與權重皆為 Apache-2.0，個人與商業使用都可以；聲音本人的同意另外記錄在平台裡。"
    languages = ("ja", "en", "zh", "ko", "fr", "de", "es", "it", "pt", "ru")
    supports_instruct = True
    infer_vram_gb = 8
    image = IMAGE
    presets = [
        TrainPreset("lora", "LoRA 微調（建議先跑這個）",
                    "官方 LoRA 設定（rank 32、學習率 1e-4、有效批次 16），跑 2 個 epoch，途中存 6 個檢查點，"
                    "每個檢查點都會念同一批沒看過的句子讓你比較。適合 30 分鐘到 20 小時的資料。",
                    {"mode": "lora", "epochs": 2, "lr": 1e-4, "batch_size": 2, "grad_accum": 8, "rank": 32,
                     "alpha": 32, "saves": 6, "max_batch_tokens": 8192, "ref_fraction": 0.4},
                    GPU_48, hours_per_data_hour=0.12, s_per_step=7.0, disk_gb=80, min_hours=0.3, recommended=True),
        TrainPreset("full", "完整微調（資料 5 小時以上）",
                    "官方完整微調設定（學習率 1e-5、有效批次 16），跑 1.5 個 epoch，保留最後 3 個檢查點的權重。"
                    "資料多時可能比 LoRA 更像，但模型檔約 8 GB、需要 80 GB 顯示卡。建議先跑 LoRA 當對照。",
                    {"mode": "full", "epochs": 1.5, "lr": 1e-5, "batch_size": 2, "grad_accum": 8, "saves": 6,
                     "keep_full": 3, "max_batch_tokens": 8192, "ref_fraction": 0.4},
                    GPU_80, hours_per_data_hour=0.15, s_per_step=9.0, disk_gb=250, min_hours=5.0),
    ]

    # --- dataset & training ---------------------------------------------------------------------------------
    def export_dataset(self, ds: dict, out_dir: Path, params: dict | None = None) -> dict:
        frac = float((params or {}).get("ref_fraction", 0.4))
        return export.write(ds, out_dir, ref_fraction=frac)

    def cloud_files(self) -> dict[str, str]:
        return {"setup_env.sh": remote.setup_script(self.id, "VoxCPM2", REPO, COMMIT, VERSION, "voxcpm"),
                "train_entry.py": remote.read("voxcpm2_train.py"), "vs_common.py": remote.read("vs_common.py")}

    def steps(self, n_train: int, preset_id: str) -> int:
        p = self.preset(preset_id).params
        per_epoch = max(1, n_train // (p["batch_size"] * p["grad_accum"]))
        return max(150, round(per_epoch * p["epochs"]))

    # --- inference ------------------------------------------------------------------------------------------
    def install_spec(self) -> dict:
        return {"pip": [f"voxcpm @ https://github.com/OpenBMB/VoxCPM/archive/{COMMIT}.zip"],
                "env": {"SETUPTOOLS_SCM_PRETEND_VERSION": VERSION}, "module": "voxcpm",
                "download": [BASE]}

    def available(self):
        if importlib.util.find_spec("voxcpm") is None:
            return False, "尚未安裝（設定 → 引擎 → 安裝）"
        try:
            import torch
            if not torch.cuda.is_available():
                return True, "已安裝，但沒有偵測到 NVIDIA GPU（可以用，但很慢）"
            total = torch.cuda.mem_get_info()[1] / 1e9
            if total < self.infer_vram_gb:
                return True, f"已安裝；顯示卡記憶體 {total:.0f} GB，低於建議的 {self.infer_vram_gb} GB"
        except Exception:
            pass
        return True, "已安裝"

    def modes(self, meta: dict) -> list[str]:
        return ["plain", "ref", "hifi"] if meta.get("mode") != "zeroshot" else ["ref", "hifi"]

    def load(self, model_dir: Path, checkpoint: str | None = None):
        from voxcpm import VoxCPM
        meta = self.model_meta(model_dir)
        kw = {"load_denoiser": False, "optimize": False}
        ck = self.checkpoint_dir(model_dir, meta, checkpoint)
        if meta.get("mode") == "lora" and ck:
            m = VoxCPM.from_pretrained(meta.get("base") or BASE, lora_weights_path=str(ck), **kw)
        elif meta.get("mode") == "full" and ck:
            m = VoxCPM.from_pretrained(str(ck), **kw)
        else:
            m = VoxCPM.from_pretrained(BASE, **kw)
        return {"model": m, "meta": meta, "checkpoint": ck.name if ck else None}

    def synthesize(self, handle, text, language=None, style="", mode="plain", reference=None, seed=None, **kw):
        m = handle["model"]
        args = {"cfg_value": float(kw.get("cfg", 2.0)), "inference_timesteps": int(kw.get("timesteps", 10)),
                "seed": seed}
        ref_path = str(reference["path"]) if reference and reference.get("path") else None
        if mode == "hifi" and ref_path and reference.get("text"):
            args.update(text=text, prompt_wav_path=ref_path, prompt_text=reference["text"],
                        reference_wav_path=ref_path)
        else:
            args["text"] = f"({style}){text}" if style else text
            if mode in ("ref", "hifi") and ref_path:
                args["reference_wav_path"] = ref_path
        wav = m.generate(**args)
        return Synthesis(wav, m.tts_model.sample_rate, {"mode": mode, "checkpoint": handle.get("checkpoint")})

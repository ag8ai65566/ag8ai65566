"""Qwen3-TTS-12Hz-1.7B-Base (Alibaba Qwen, 2026-01): the studio's second engine.

Why it is here: Apache-2.0; official single-speaker fine-tuning; the lowest word error rate of the open models in
the shared comparison (en WER 0.93 %, ja 3.82 %), so it is the one to try when VoxCPM2 mispronounces or skips words.
Its speaker similarity trails VoxCPM2 in the same comparison. The fine-tuned model is a full copy (~4 GB).

Modes: a fine-tuned model speaks on its own (plain), optionally with a style instruction (not guaranteed to work after
fine-tuning the Base model). A zero-shot model clones from a reference clip (ref) or clip + transcript (hifi).
"""
from __future__ import annotations

import importlib.util
from pathlib import Path

from . import export, remote
from .base import Engine, Synthesis, TrainPreset

REPO = "https://github.com/QwenLM/Qwen3-TTS.git"
COMMIT = "022e286b98fbec7e1e916cb940cdf532cd9f488e"  # main on 2026-03-17 (package 0.1.1)
VERSION = "0.1.1"
BASE = "Qwen/Qwen3-TTS-12Hz-1.7B-Base"
IMAGE = "runpod/pytorch:2.8.0-py3.11-cuda12.8.1-cudnn-devel-ubuntu22.04"
FLASH_WHEEL = ("https://github.com/Dao-AILab/flash-attention/releases/download/v2.8.3/"
               "flash_attn-2.8.3+cu12torch2.8cxx11abiTRUE-cp311-cp311-linux_x86_64.whl")
LANG = {"ja": "Japanese", "en": "English", "zh": "Chinese", "ko": "Korean", "de": "German", "fr": "French",
        "ru": "Russian", "pt": "Portuguese", "es": "Spanish", "it": "Italian"}


def _flash_ok() -> bool:
    """The CUDA extension has to load, not just be installed (a mismatched build fails at import)."""
    if importlib.util.find_spec("flash_attn") is None:
        return False
    try:
        import flash_attn  # noqa: F401
        import flash_attn_2_cuda  # noqa: F401
        return True
    except Exception:
        return False


class Qwen3Engine(Engine):
    id = "qwen3"
    name = "Qwen3-TTS 1.7B"
    summary = ("阿里巴巴 Qwen 2026 年 1 月發表，17 億參數、10 種語言（含日文、英文）。公開評測中念錯字最少，"
               "有官方單一說話者微調。音色相似度略低於 VoxCPM2；當 VoxCPM2 念錯或漏字時拿來對照。")
    license = "Apache-2.0"
    license_note = "程式與權重皆為 Apache-2.0，個人與商業使用都可以。"
    languages = tuple(LANG)
    supports_instruct = True
    infer_vram_gb = 8
    image = IMAGE
    presets = [
        TrainPreset("sft", "官方微調（完整）",
                    "官方 finetuning 流程：先抽出 12 Hz 音訊碼，再做完整微調 3 個 epoch（學習率 2e-5、批次 2、"
                    "梯度累積 4），每個 epoch 一個檢查點，保留最後 2 個。",
                    {"epochs": 3, "lr": 2e-5, "batch_size": 2, "keep": 2},
                    ["NVIDIA A100 80GB PCIe", "NVIDIA A100-SXM4-80GB", "NVIDIA L40S", "NVIDIA H100 PCIe"],
                    hours_per_data_hour=0.12, s_per_step=0.5, disk_gb=120, ram_gb=64, min_hours=0.5,
                    recommended=True),
    ]

    def export_dataset(self, ds: dict, out_dir: Path, params: dict | None = None) -> dict:
        return export.write(ds, out_dir, ref_fraction=0.0)

    def cloud_files(self) -> dict[str, str]:
        post = (f'pip install -q --no-deps "{FLASH_WHEEL}" '
                '|| echo "[vs] FlashAttention wheel not available; training will use PyTorch SDPA"\n'
                'python -c "import flash_attn, flash_attn_2_cuda" 2>/dev/null || '
                '{ echo "[vs] FlashAttention unusable on this image; removing it (SDPA will be used)"; '
                'pip uninstall -q -y flash-attn || true; }')
        setup = remote.setup_script(self.id, "Qwen3-TTS", REPO, COMMIT, VERSION, "qwen_tts", "Qwen3TTSModel", post=post)
        return {"setup_env.sh": setup,
                "train_entry.py": remote.read("qwen3_train.py"), "vs_common.py": remote.read("vs_common.py")}

    def schedule(self, n_train: int, params: dict) -> dict:
        """The official trainer saves one checkpoint per whole epoch, so epochs are whole numbers."""
        epochs = max(1, round(float(params["epochs"])))
        if n_train < int(params["batch_size"]):
            raise ValueError(f"資料太少：至少需要 {params['batch_size']} 段訓練片段")
        return {"epochs": epochs, "total_steps": -(-n_train // int(params["batch_size"])) * epochs,
                "epochs_effective": float(epochs)}

    def steps(self, n_train: int, preset_id: str, params: dict | None = None) -> int:
        p = params or self.preset(preset_id).params
        return -(-n_train // int(p["batch_size"])) * int(p["epochs"])

    # --- inference ------------------------------------------------------------------------------------------
    def install_spec(self) -> dict:
        return {"pip": [f"qwen-tts @ https://github.com/QwenLM/Qwen3-TTS/archive/{COMMIT}.zip"], "env": {},
                "module": "qwen_tts", "cls": "Qwen3TTSModel", "download": [BASE, "Qwen/Qwen3-TTS-Tokenizer-12Hz"]}

    def available(self):
        if importlib.util.find_spec("qwen_tts") is None:
            return False, "尚未安裝（設定 → 引擎 → 安裝）"
        try:
            import torch
            if not torch.cuda.is_available():
                return True, "已安裝，但沒有偵測到 NVIDIA GPU（可以用，但很慢）"
        except Exception:
            pass
        return True, "已安裝"

    def modes(self, meta: dict) -> list[str]:
        return ["plain"] if meta.get("mode") == "sft" else ["ref", "hifi"]

    def load(self, model_dir: Path, checkpoint: str | None = None):
        import torch
        from qwen_tts import Qwen3TTSModel
        meta = self.model_meta(model_dir)
        ck = self.checkpoint_dir(model_dir, meta, checkpoint)
        cuda = torch.cuda.is_available()
        attn = "flash_attention_2" if cuda and _flash_ok() else "sdpa"
        src = str(ck) if (meta.get("mode") == "sft" and ck) else BASE
        m = Qwen3TTSModel.from_pretrained(src, device_map="cuda:0" if cuda else "cpu",
                                          dtype=torch.bfloat16 if cuda else torch.float32, attn_implementation=attn)
        return {"model": m, "meta": meta, "checkpoint": ck.name if ck and src != BASE else None, "prompts": {}}

    def synthesize(self, handle, text, language=None, style="", mode="plain", reference=None, seed=None, **kw):
        import torch
        m, meta = handle["model"], handle["meta"]
        lang = LANG.get(language or "", "Auto")
        if seed is not None:
            torch.manual_seed(seed)
        if meta.get("mode") == "sft":
            # the official SFT recipe trains with the auto-language prompt, so inference uses it too
            spk = meta.get("speaker", "vs_speaker")
            sft_lang = meta.get("sft_language", "Auto")
            try:
                wavs, sr = m.generate_custom_voice(text=text, language=sft_lang, speaker=spk, instruct=style or None)
            except TypeError:
                wavs, sr = m.generate_custom_voice(text=text, language=sft_lang, speaker=spk)
        else:
            if not reference or not reference.get("path"):
                raise ValueError("零樣本模型需要參考片段")
            hifi = mode == "hifi" and bool(reference.get("text"))
            key = (str(reference["path"]), hifi)
            if key not in handle["prompts"]:
                handle["prompts"][key] = m.create_voice_clone_prompt(
                    ref_audio=str(reference["path"]), ref_text=reference.get("text") if hifi else None,
                    x_vector_only_mode=not hifi)
            wavs, sr = m.generate_voice_clone(text=text, language=lang, voice_clone_prompt=handle["prompts"][key])
        return Synthesis(wavs[0], sr, {"mode": mode, "checkpoint": handle.get("checkpoint")})

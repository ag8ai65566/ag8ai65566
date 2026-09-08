"""Catalogue of installable models.

Every filename, repo path and byte size here was read from the Hugging Face
API, and every node name and parameter value in the builders was validated
against a real ComfyUI 0.33.0 /object_info. Sampler numbers come from the
official ComfyUI workflow templates for each model.
"""

from __future__ import annotations

from dataclasses import dataclass, field

WAN_REPO = "Comfy-Org/Wan_2.2_ComfyUI_Repackaged"
# Spelled once each: they appear on a dozen files apiece further down.
QWEN_TTS_REPO = "Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice"
COSY_REPO = "FunAudioLLM/Fun-CosyVoice3-0.5B-2512"
HY_REPO = "Comfy-Org/HunyuanVideo_1.5_repackaged"
GGUF_REPO = "QuantStack/Wan2.2-I2V-A14B-GGUF"
LTX25_REPO = "Lightricks/LTX-2.5"

# The negative prompt shipped with the official Wan workflows. Kept verbatim -
# it is tuned for this model family and beats an English equivalent.
WAN_NEGATIVE = (
    "色调艳丽，过曝，静态，细节模糊不清，字幕，风格，作品，画作，画面，静止，"
    "整体发灰，最差质量，低质量，JPEG压缩残留，丑陋的，残缺的，多余的手指，"
    "画得不好的手部，画得不好的脸部，畸形的，毁容的，形态畸形的肢体，手指融合，"
    "静止不动的画面，杂乱的背景，三条腿，背景人很多，倒着走"
)
HY_NEGATIVE = "pc game, console game, video game, cartoon, childish, ugly, static, blurry, watermark, subtitles"


@dataclass(frozen=True)
class ModelFile:
    repo: str
    path: str
    folder: str  # ComfyUI models/<folder>
    size: int
    # Some repos publish everything as `diffusion_pytorch_model.safetensors`,
    # so the basename would collide between models and tell the user nothing in
    # the loader's dropdown. This is the name it lands under instead.
    save_as: str = ""
    # Hugging Face "gated" repos answer 401 to an anonymous request even though
    # the weights are free: you have to be logged in *and* have clicked accept
    # on the model page. Flagged here so the UI can say that before a 40GB
    # download fails at the first byte, rather than after.
    gated: bool = False

    @property
    def name(self) -> str:
        return self.save_as or self.path.rsplit("/", 1)[-1]


@dataclass(frozen=True)
class Licence:
    """A licence with terms the user has to see before downloading.

    Separate from `ModelFile.gated`, which is about whether Hugging Face will
    serve the bytes. This is about whether the person is allowed to use them,
    which the download cannot answer and which this project should not answer
    on their behalf - so it is surfaced, not enforced.
    """

    name: str
    url: str
    # Places the licence excludes outright. Empty for the permissive ones.
    excluded: tuple[str, ...] = ()
    note: str = ""

    @property
    def restricted(self) -> bool:
        return bool(self.excluded or self.note)

    def public(self) -> dict:
        return {"name": self.name, "url": self.url,
                "excluded": list(self.excluded), "note": self.note,
                "restricted": self.restricted}


@dataclass
class ModelDef:
    id: str
    label: str
    family: str  # wan22_14b | wan22_5b | hunyuan15 | files_only
    vram_gb: int  # realistic minimum
    files: list[ModelFile]
    tiers: dict[str, tuple[int, int]]
    fps: int = 16
    length: int = 81
    steps: int = 20
    cfg: float = 3.5
    shift: float = 8.0
    sampler: str = "euler"
    scheduler: str = "simple"
    negative: str = WAN_NEGATIVE
    # wan22_14b only: which step the high-noise expert hands off to the low one
    boundary: int | None = None
    # Optional speed LoRAs, downloaded with the model and toggleable per job.
    lightning: tuple[ModelFile, ...] = ()
    lightning_steps: int = 4
    lightning_cfg: float = 1.0
    lightning_shift: float = 5.0
    supports_lora: bool = True
    # Which of the drama page's shot methods THIS APP can build for this model.
    # Not the model's own capabilities: Wan 2.2 has an official
    # `WanFirstLastFrameToVideo` route, but there is no builder for it here, so
    # Wan says i2v only. It exists so the drama page can refuse a route it
    # cannot build, instead of letting you pick it and find out twenty shots
    # later with a video that is not the one you asked for.
    #
    # Empty used to mean "all of them", which read as a convenience and behaved
    # as a trap: every runnable model except H3 was empty, so routing 說話 or
    # 動作轉移 at Wan passed every check and then built a plain image-to-video
    # graph. Every runnable model now says what it can do; empty means "nothing
    # declared", which is what a files-only entry honestly is.
    methods: tuple[str, ...] = ()
    # Pixel granularity the sampler needs. 16 covers every VAE here (they
    # downsample by 8 or 16). MiniMax H3 needs 32: its DiT patchifies the
    # latent in 2x2 blocks (`patch_size=(1, 2, 2)` in comfy/ldm/minimax/
    # model.py) and reshapes `lat_h // 2, 2, lat_w // 2, 2`, so an odd latent
    # side is a shape error, not a soft-edged output. A vertical drama shot
    # snapped to 16 came out 848x1232 - latent 53x77, both odd - which is
    # every portrait shot at the 768p tier.
    dim_multiple: int = 16
    # The frame grid this family snaps to: n * period + phase. 4n+1 for every
    # model whose VAE compresses time 4:1; MiniMax H3 is 17n+5 at 24fps. The
    # page used to derive frames from seconds with 4n+1 written into it, so
    # picking 5 seconds of H3 quoted 121 frames while the graph built 124.
    frame_period: int = 4
    frame_phase: int = 1
    # What this entry is for. Everything in this catalogue is downloadable from
    # the models tab, but only the video ones belong in a "which model makes
    # the clip" picker - the TTS bundles were being offered there, which is a
    # dead end that looks like a choice.
    role: str = "video"
    # Exact CivitAI baseModel strings, best match first. Filters the in-app
    # LoRA browser to things that stand a chance of working with this model.
    civitai_bases: tuple[str, ...] = ()
    # Trained for a neighbouring model; often works, sometimes not.
    civitai_bases_loose: tuple[str, ...] = ()
    # Set when the licence restricts who may use the weights. Shown before the
    # download button rather than after it. An absent licence means there is
    # nothing to warn about - Wan 2.2 is Apache 2.0.
    licence: Licence | None = None
    note: str = ""

    @property
    def vram_note(self) -> str:
        """VRAM here is a recommendation, never a limit - said in one place."""
        return (
            f"建議 {self.vram_gb}GB 顯存。低於這個數字仍然跑得動 —— "
            "ComfyUI 會把權重換到系統記憶體，只是慢很多。"
        )

    @property
    def all_files(self) -> list[ModelFile]:
        return [*self.files, *self.lightning]

    @property
    def download_bytes(self) -> int:
        return sum(f.size for f in self.all_files)

    @property
    def gated_repos(self) -> list[str]:
        """Repos that need a Hugging Face token plus an accepted licence."""
        return sorted({f.repo for f in self.all_files if f.gated})

    @property
    def runnable(self) -> bool:
        """Whether this app ships a verified graph for the model.

        A catalogue fact, and deliberately not the whole answer: a user can
        import their own ComfyUI workflow for a files-only model, and then it
        *is* generatable here. That combination is computed in the server,
        where the imported workflows live - the catalogue should not have to
        know what is on this particular machine.
        """
        return self.family != "files_only"

    @property
    def family_runnable(self) -> bool:
        """Alias, for callers that mean the catalogue fact specifically."""
        return self.runnable


# Licences that restrict *where* the weights may be used. Read from the LICENSE
# file in each repo rather than from a summary: HunyuanVideo's opens with "THIS
# LICENSE AGREEMENT DOES NOT APPLY IN THE EUROPEAN UNION, UNITED KINGDOM AND
# SOUTH KOREA", and MiniMax's excludes the United States on top of those.
HUNYUAN_LICENCE = Licence(
    name="Tencent Hunyuan Community License",
    url="https://huggingface.co/tencent/HunyuanVideo-1.5/blob/main/LICENSE",
    excluded=("歐盟", "英國", "韓國"),
    note="月活躍使用者超過 1 億要另外向騰訊申請授權（授不授權由他們決定）；"
         "另附 Acceptable Use Policy。",
)

LTX_LICENCE = Licence(
    name="LTX-2 Community License",
    url="https://huggingface.co/Lightricks/LTX-2.5",
    note="自訂社群授權：年營收達 1000 萬美元的實體要另外購買商用授權，"
         "衍生出來的 LoRA 也受同一份授權約束。",
)


# -- shared component sets ---------------------------------------------------

WAN_TE = ModelFile(WAN_REPO, "split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors", "text_encoders", 6735906897)
WAN21_VAE = ModelFile(WAN_REPO, "split_files/vae/wan_2.1_vae.safetensors", "vae", 253815318)
WAN22_VAE = ModelFile(WAN_REPO, "split_files/vae/wan2.2_vae.safetensors", "vae", 1409400960)
WAN_LIGHTNING = (
    ModelFile(WAN_REPO, "split_files/loras/wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors", "loras", 1226977424),
    ModelFile(WAN_REPO, "split_files/loras/wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors", "loras", 1226977424),
)

HY_COMMON = [
    ModelFile(HY_REPO, "split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors", "text_encoders", 9384670680),
    ModelFile(HY_REPO, "split_files/text_encoders/byt5_small_glyphxl_fp16.safetensors", "text_encoders", 438643184),
    ModelFile(HY_REPO, "split_files/vae/hunyuanvideo15_vae_fp16.safetensors", "vae", 2521292758),
    ModelFile(HY_REPO, "split_files/clip_vision/sigclip_vision_patch14_384.safetensors", "clip_vision", 856505640),
]

# CivitAI baseModel strings, verified against live search results.
WAN22_I2V_BASES = ("Wan Video 2.2 I2V-A14B",)
WAN22_I2V_LOOSE = (
    "Wan Video 2.2 T2V-A14B",
    "Wan Video 14B i2v 480p",
    "Wan Video 14B i2v 720p",
    "Wan Video 14B t2v",
    "Wan Video",
)

WAN_TIERS = {"480p": (832, 480), "720p": (1280, 720)}
HY_TIERS = {"480p": (848, 480), "720p": (1280, 720)}


def _gguf(quant: str, size: int) -> list[ModelFile]:
    return [
        ModelFile(GGUF_REPO, f"HighNoise/Wan2.2-I2V-A14B-HighNoise-{quant}.gguf", "unet", size),
        ModelFile(GGUF_REPO, f"LowNoise/Wan2.2-I2V-A14B-LowNoise-{quant}.gguf", "unet", size),
    ]


MODELS: list[ModelDef] = [
    ModelDef(
        id="wan22-14b-fp8",
        label="Wan 2.2 I2V 14B — fp8（畫質最好）",
        methods=("i2v",),
        family="wan22_14b",
        vram_gb=24,
        files=[
            ModelFile(WAN_REPO, "split_files/diffusion_models/wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors", "diffusion_models", 14294742832),
            ModelFile(WAN_REPO, "split_files/diffusion_models/wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors", "diffusion_models", 14294742832),
            WAN_TE,
            WAN21_VAE,
        ],
        tiers=WAN_TIERS,
        fps=16,
        length=81,
        steps=20,
        cfg=3.5,
        shift=8.0,
        boundary=10,
        lightning=WAN_LIGHTNING,
        civitai_bases=WAN22_I2V_BASES,
        civitai_bases_loose=WAN22_I2V_LOOSE,
        note="NSFW LoRA 生態最完整的選擇。",
    ),
    ModelDef(
        id="wan22-14b-q8",
        label="Wan 2.2 I2V 14B — GGUF Q8（接近 fp8）",
        methods=("i2v",),
        family="wan22_14b",
        vram_gb=16,
        files=[*_gguf("Q8_0", 15406608896), WAN_TE, WAN21_VAE],
        tiers=WAN_TIERS,
        fps=16,
        length=81,
        steps=20,
        cfg=3.5,
        shift=8.0,
        boundary=10,
        lightning=WAN_LIGHTNING,
        civitai_bases=WAN22_I2V_BASES,
        civitai_bases_loose=WAN22_I2V_LOOSE,
        note="需要 ComfyUI-GGUF 節點（安裝腳本已含）。",
    ),
    ModelDef(
        id="wan22-14b-q4",
        label="Wan 2.2 I2V 14B — GGUF Q4_K_M（省顯存）",
        methods=("i2v",),
        family="wan22_14b",
        vram_gb=12,
        files=[*_gguf("Q4_K_M", 9651728896), WAN_TE, WAN21_VAE],
        tiers=WAN_TIERS,
        fps=16,
        length=81,
        steps=20,
        cfg=3.5,
        shift=8.0,
        boundary=10,
        lightning=WAN_LIGHTNING,
        civitai_bases=WAN22_I2V_BASES,
        civitai_bases_loose=WAN22_I2V_LOOSE,
        note="12GB 顯卡的主力選擇。畫質略降但動態仍好。",
    ),
    ModelDef(
        id="wan22-5b",
        label="Wan 2.2 TI2V 5B（輕量、原生 720p）",
        methods=("i2v",),
        family="wan22_5b",
        vram_gb=12,
        files=[
            ModelFile(WAN_REPO, "split_files/diffusion_models/wan2.2_ti2v_5B_fp16.safetensors", "diffusion_models", 9999658848),
            WAN_TE,
            WAN22_VAE,
        ],
        tiers={"480p": (832, 480), "704p": (1280, 704)},
        fps=24,
        length=121,
        steps=20,
        cfg=5.0,
        shift=8.0,
        sampler="uni_pc",
        civitai_bases=("Wan Video 2.2 TI2V-5B",),
        civitai_bases_loose=("Wan Video",),
        note="單一模型、下載量小。畫質明顯輸 14B，但快很多。",
    ),
    ModelDef(
        # The one thing a short drama cannot be made without: a character who
        # talks. S2V is audio-driven - the audio goes in and the lip movement
        # comes out of the same pass, rather than being pasted on afterwards by
        # a separate lip-sync model. That ordering matters in practice: the
        # audio has to exist first, and its length decides the shot's length.
        id="wan22-s2v",
        label="Wan 2.2 S2V 14B — 說話鏡頭（音訊驅動，原生口型）",
        family="files_only",
        vram_gb=16,
        files=[
            ModelFile(WAN_REPO, "split_files/diffusion_models/wan2.2_s2v_14B_fp8_scaled.safetensors",
                      "diffusion_models", 16394832474),
            # S2V listens through wav2vec, so the audio encoder is not optional.
            ModelFile(WAN_REPO, "split_files/audio_encoders/wav2vec2_large_english_fp16.safetensors",
                      "audio_encoders", 630997322),
            WAN_TE,
            WAN21_VAE,
        ],
        tiers={},
        fps=16,
        supports_lora=False,
        civitai_bases=("Wan Video 2.2 I2V-A14B",),
        note="**短劇有台詞的鏡頭就是靠這個。** 音檔進去、對好口型的影片出來，"
             "不是事後再貼一層 lip-sync。所以順序是**先做音檔再生影片** —— "
             "音檔長度直接決定鏡頭長度，反過來做就要重跑。"
             "下載完在 ComfyUI（:8188）用 Workflow → Browse Templates → Wan 2.2 S2V。",
    ),
    ModelDef(
        # Motion retargeting: take the pose and expression out of a driving
        # video and put them on your character. For short drama this is an asset
        # play, not a one-off - the genre runs on the same handful of beats
        # (a slap, a turn, a door slammed, an embrace), so one good driving clip
        # gets reused across characters and episodes.
        id="wan22-animate",
        label="Wan 2.2 Animate 14B — 動作轉移（把參考影片的動作套到你的角色）",
        family="files_only",
        vram_gb=16,
        files=[
            ModelFile(WAN_REPO, "split_files/diffusion_models/wan2.2_animate_14B_int8_convrot.safetensors",
                      "diffusion_models", 18413068672),
            # Relight LoRA: without it the character keeps the lighting of the
            # plate they came from and looks pasted into the scene.
            ModelFile(WAN_REPO, "split_files/loras/wan2.2_animate_14B_relight_lora_bf16.safetensors",
                      "loras", 1436673432),
            WAN_TE,
            WAN21_VAE,
        ],
        tiers={},
        fps=16,
        supports_lora=False,
        civitai_bases=("Wan Video 2.2 I2V-A14B",),
        note="**動作也可以當資產。** 短劇的動作是高度重複的（甩巴掌、轉身、摔門、"
             "擁抱），錄一次或找一段參考影片，就能套到不同角色身上重複用。"
             "附的 relight LoRA 會把角色的光線重打成場景的光線，不加會像貼上去的。"
             "下載完在 ComfyUI（:8188）用 Workflow → Browse Templates → Wan 2.2 Animate。",
    ),
    # -- text to speech. Downloadable and catalogued; NOT generatable from
    # here. This app has no TTS pipeline and has never run one, so these are
    # `files_only` for the same reason LTX and H3 are: the honest state is
    # "here are the weights and where the official code is", not a button.
    #
    # Chosen after a round with a second model. Both are Apache 2.0 - which
    # matters more than it sounds, because two popular alternatives are not:
    # IndexTTS is a custom bilibili licence with use restrictions, and F5-TTS's
    # code is MIT while its Chinese weights are CC-BY-NC.
    # Both entries list the *whole* repository, at its real byte sizes read
    # from the Hugging Face API. Two reasons, both learned the hard way here:
    # a single weights file is not a loadable model - Qwen3-TTS needs its
    # tokenizer and its speech tokenizer, CosyVoice3 needs its flow, hift and
    # ONNX tokenisers - and both projects' official instructions are a
    # whole-repo snapshot_download, so anything less is this project inventing
    # a subset. The filenames are kept exactly as upstream publishes them,
    # because the official loaders look for them by name.
    ModelDef(
        id="qwen3-tts",
        role="tts",
        label="Qwen3-TTS 0.6B CustomVoice — 中文語音（只下載檔案）",
        family="files_only",
        vram_gb=8,
        files=[
            ModelFile(QWEN_TTS_REPO, "model.safetensors",
                      "tts/qwen3-tts", 1_811_626_576),
            ModelFile(QWEN_TTS_REPO, "config.json", "tts/qwen3-tts", 4_908),
            ModelFile(QWEN_TTS_REPO, "generation_config.json",
                      "tts/qwen3-tts", 245),
            ModelFile(QWEN_TTS_REPO, "preprocessor_config.json",
                      "tts/qwen3-tts", 127),
            ModelFile(QWEN_TTS_REPO, "tokenizer_config.json",
                      "tts/qwen3-tts", 7_344),
            ModelFile(QWEN_TTS_REPO, "vocab.json", "tts/qwen3-tts", 2_776_833),
            ModelFile(QWEN_TTS_REPO, "merges.txt", "tts/qwen3-tts", 1_671_839),
            # The speech tokeniser is what turns audio into the tokens the
            # model predicts. Without it there is nothing to decode.
            ModelFile(QWEN_TTS_REPO, "speech_tokenizer/model.safetensors",
                      "tts/qwen3-tts/speech_tokenizer", 682_293_092),
            ModelFile(QWEN_TTS_REPO, "speech_tokenizer/config.json",
                      "tts/qwen3-tts/speech_tokenizer", 2_336),
            ModelFile(QWEN_TTS_REPO, "speech_tokenizer/configuration.json",
                      "tts/qwen3-tts/speech_tokenizer", 76),
            ModelFile(QWEN_TTS_REPO, "speech_tokenizer/preprocessor_config.json",
                      "tts/qwen3-tts/speech_tokenizer", 234),
        ],
        tiers={},
        supports_lora=False,
        note="**短劇的台詞要有聲音就需要這個。** 內建音色，不需要參考音訊 —— "
             "所以不會用到任何真實人物的聲音。Apache 2.0，支援中文等十種語言。"
             "整包約 2.5GB（權重 1.8GB ＋ 語音 tokenizer 0.68GB ＋ 詞表）—— "
             "**少一個都跑不起來**，所以這裡列的是官方倉庫的全部檔案。"
             "官方沒有公布保證的最低顯存數字，0.6B 屬於消費級跑得動的尺寸，"
             "但這是尺寸推論不是官方保證。"
             "**這個 app 不會跑它** —— 官方程式在 "
             "github.com/QwenLM/Qwen3-TTS，社群也有 ComfyUI 節點（非官方，"
             "有相依衝突的回報）。生成好的音檔用短劇分頁每顆鏡頭的「上傳音檔」掛上去。",
    ),
    ModelDef(
        id="cosyvoice3",
        role="tts",
        label="Fun-CosyVoice3 0.5B — 中文語音、可複製音色（只下載檔案）",
        family="files_only",
        vram_gb=8,
        files=[
            ModelFile(COSY_REPO, "llm.pt", "tts/cosyvoice3", 2_024_669_519),
            ModelFile(COSY_REPO, "llm.rl.pt", "tts/cosyvoice3", 2_024_682_701),
            ModelFile(COSY_REPO, "flow.pt", "tts/cosyvoice3", 1_329_116_148),
            ModelFile(COSY_REPO, "flow.decoder.estimator.fp32.onnx",
                      "tts/cosyvoice3", 1_326_216_933),
            ModelFile(COSY_REPO, "hift.pt", "tts/cosyvoice3", 83_202_622),
            ModelFile(COSY_REPO, "campplus.onnx", "tts/cosyvoice3", 28_303_423),
            ModelFile(COSY_REPO, "speech_tokenizer_v3.onnx",
                      "tts/cosyvoice3", 969_451_503),
            ModelFile(COSY_REPO, "speech_tokenizer_v3.batch.onnx",
                      "tts/cosyvoice3", 969_451_579),
            ModelFile(COSY_REPO, "cosyvoice3.yaml", "tts/cosyvoice3", 6_934),
            ModelFile(COSY_REPO, "config.json", "tts/cosyvoice3", 2),
            ModelFile(COSY_REPO, "configuration.json", "tts/cosyvoice3", 47),
            ModelFile(COSY_REPO, "CosyVoice-BlankEN/model.safetensors",
                      "tts/cosyvoice3/CosyVoice-BlankEN", 988_097_824),
            ModelFile(COSY_REPO, "CosyVoice-BlankEN/config.json",
                      "tts/cosyvoice3/CosyVoice-BlankEN", 659),
            ModelFile(COSY_REPO, "CosyVoice-BlankEN/generation_config.json",
                      "tts/cosyvoice3/CosyVoice-BlankEN", 242),
            ModelFile(COSY_REPO, "CosyVoice-BlankEN/tokenizer_config.json",
                      "tts/cosyvoice3/CosyVoice-BlankEN", 1_287),
            ModelFile(COSY_REPO, "CosyVoice-BlankEN/vocab.json",
                      "tts/cosyvoice3/CosyVoice-BlankEN", 2_776_833),
            ModelFile(COSY_REPO, "CosyVoice-BlankEN/merges.txt",
                      "tts/cosyvoice3/CosyVoice-BlankEN", 1_402_109),
        ],
        tiers={},
        supports_lora=False,
        note="另一條中文 TTS 路線，Apache 2.0，支援中文方言、零樣本音色複製、"
             "情緒與語速指令。官方有公布中文 CER 與音色相似度評測 —— "
             "那是**模型作者自己的測試**，本專案沒有重現。"
             "**整包約 9.7GB**，比 Qwen3-TTS 大很多：官方的安裝方式是把整個倉庫"
             "snapshot_download 下來，所以這裡列的是全部檔案，沒有替你挑。"
             "（`llm.rl.pt` 和 `speech_tokenizer_v3.batch.onnx` 看起來是替代版本，"
             "但官方沒說哪些可以不下載，本專案不猜。）"
             "**這個 app 不會跑它** —— 官方程式在 github.com/FunAudioLLM/CosyVoice，"
             "還需要它的 GitHub 原始碼和 submodule。"
             "**音色複製只用在虛構角色、你自己的聲音，或你有明確授權的參考音。**",
    ),

    # MiniMax H3. Added after a round with a second model; we agreed on the
    # shape - files_only, FL2VA only, and the licence shown before the download
    # button rather than under it.
    #
    # Why files_only when this one *does* have a ComfyUI template: the same
    # reason as LTX and Wan S2V. This project has no GPU and has never produced
    # a frame, so an in-app graph would be a guess wearing a button. The
    # official template is maintained by people who can test it.
    #
    # Ref2VA (multi-image character reference) is deliberately absent. It is a
    # second ~21GB transformer, and bundling it would mean everybody downloads
    # it to find out whether they wanted it.
    ModelDef(
        id="minimax-h3",
        label="MiniMax H3 — 圖生影片，自帶同步聲音",
        # Both, through one node: MiniMaxH3ImageToVideo takes a first frame and
        # an *optional* last frame. An earlier version of this entry said H3 had
        # no plain image-to-video mode at all, which was simply wrong - ComfyUI
        # ships `video_minimax_h3_i2v` as a built-in template.
        methods=("i2v", "flf"),
        family="minimax_h3",
        vram_gb=24,
        files=[
            # int8_convrot for the diffusion model, which the repo's README
            # states outright is the preferred build.
            ModelFile("Comfy-Org/MiniMax-H3",
                      "diffusion_models/minimax_h3_fl2va_pruned_int8_convrot.safetensors",
                      "diffusion_models", 20970379616),
            # nvfp4 for the text encoder: 15.7GB against int8's 27.1GB, and the
            # official README says in as many words that it "does not require
            # Blackwell GPU to use". This entry used to download the int8 build
            # on the strength of a note claiming NVFP4 needed an RTX 50-series
            # card - that was simply wrong, and it cost 11.4GB of download and
            # the VRAM to match.
            ModelFile("Comfy-Org/MiniMax-H3",
                      "text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors",
                      "text_encoders", 15687142551),
            # Two VAEs, because the audio comes out of the same pass.
            ModelFile("Comfy-Org/MiniMax-H3",
                      "vae/minimax_h3_video_vae_fp16.safetensors", "vae", 5207808496),
            ModelFile("Comfy-Org/MiniMax-H3",
                      "vae/minimax_h3_audio_vae_fp32.safetensors", "vae", 605254808),
            # The turbo LoRA moved to `lightning` - it is the template's
            # "Enable Lightning LoRA" switch, and listing it in both places
            # made `all_files` hand the downloader the same file twice.
        ],
        # Straight from the official template's own widget values: 1344x768,
        # res_multistep / simple, 20 steps, and 6 with the turbo LoRA.
        # 768p is the model's own canvas: `adapt_canvas` in ComfyUI's
        # nodes_minimax_h3.py derives every reference canvas at short edge 768
        # with a 768*1344 area cap, and 1344x768 is exactly that cap. The I2V
        # path does not run that function - it uses what you pass, verbatim -
        # so 540p really is 960x544 rather than being silently resized. It is
        # below the short edge the model works at, though, so it is a way to
        # fit a smaller card and not a mode the model advertises.
        tiers={"768p": (1344, 768), "540p": (960, 544)},
        # 2x2 patchify - see ModelDef.dim_multiple.
        dim_multiple=32,
        frame_period=17,
        frame_phase=5,
        fps=24,
        # 124 frames at 24fps is the node's own default (~5.2s). ComfyUI's
        # tooltip puts the trained range at 124-362 frames, i.e. roughly 5 to
        # 15 seconds - shorter than that is outside what the model was trained
        # on, which is worth knowing before blaming the prompt.
        length=124,
        steps=20,
        cfg=1.0,          # BasicGuider: the graph has no negative prompt at all
        shift=1.0,        # unused - H3 has no ModelSamplingSD3 in its graph
        sampler="res_multistep",
        scheduler="simple",
        lightning=(
            ModelFile("Comfy-Org/MiniMax-H3",
                      "loras/minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16.safetensors",
                      "loras", 1956193000),
        ),
        lightning_steps=6,
        lightning_cfg=1.0,
        lightning_shift=1.0,
        supports_lora=False,
        civitai_bases=("MiniMax H3",),
        licence=Licence(
            name="MiniMax H3 Community License",
            url="https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/LICENSE",
            # The only licence in this catalogue that excludes the United
            # States, which is not what anyone expects and is easy to miss.
            excluded=("美國", "歐盟", "英國", "韓國"),
            note="年營收超過 2000 萬美元要另外向 MiniMax 申請授權；"
                 "商用產品的介面上還要標示「MiniMax H3」。",
        ),
        note="**權重是真的開放的**，不像 Seedance 那樣只有 API —— "
             "但這是目錄裡最大的一個（約 44GB），而且光文字編碼器"
             "（Qwen3-VL 32B）就 16GB，塞不進 24GB 顯存，一定要大量 offload。"
             "**這個 app 現在可以直接跑它**（圖生影片，也支援首尾幀）—— "
             "工作流是照 ComfyUI 內建範本 `video_minimax_h3_i2v` 一比一組的，"
             "但**本專案沒有 GPU，沒有實跑驗證過**。"
             "聲音是它自己**生出來的**，不是你放進去的。"
             "訓練長度是 124–362 幀（約 5–15 秒），比 5 秒短是在訓練範圍外面。"
             "**顯卡不夠大就別選這個**：光文字編碼器就 16GB，24GB 顯卡也要大量 offload，"
             "10GB 的卡基本上跑不動 —— 一般真人動作鏡頭先用 HunyuanVideo 1.5 480p，"
             "那個的 DiT 是 8.3B，整包約 21.5GB，只吃一張圖。"
             "多圖角色參考的 Ref2VA 是另外 21GB，沒有收進這個下載包。",
    ),
    ModelDef(
        id="hy15-480p",
        label="HunyuanVideo 1.5 480p — fp8 cfg-distilled（最省顯存）",
        methods=("i2v",),
        family="hunyuan15",
        vram_gb=10,
        files=[
            ModelFile(HY_REPO, "split_files/diffusion_models/hunyuanvideo1.5_480p_i2v_cfg_distilled_fp8_scaled.safetensors", "diffusion_models", 8330399746),
            *HY_COMMON,
        ],
        tiers={"480p": (848, 480)},
        fps=24,
        length=121,
        steps=20,
        cfg=1.0,  # CFG is distilled into the weights; a real cfg would double the cost
        shift=7.0,
        negative=HY_NEGATIVE,
        # CivitAI's "Hunyuan Video" is the original architecture, not 1.5,
        # so those LoRAs are a gamble rather than a match.
        civitai_bases_loose=("Hunyuan Video",),
        licence=HUNYUAN_LICENCE,
        note="主模型（DiT）8.3GB，但**要全部下載完才能跑**：加上文字編碼器、VAE、視覺編碼器一共約 21.5GB。人臉與物理最自然，NSFW 生態比 Wan 少。",
    ),
    ModelDef(
        id="hy15-720p",
        label="HunyuanVideo 1.5 720p — fp8 cfg-distilled",
        methods=("i2v",),
        family="hunyuan15",
        vram_gb=12,
        files=[
            ModelFile(HY_REPO, "split_files/diffusion_models/hunyuanvideo1.5_720p_i2v_cfg_distilled_fp8_scaled.safetensors", "diffusion_models", 8330399746),
            *HY_COMMON,
        ],
        tiers=HY_TIERS,
        fps=24,
        length=121,
        steps=20,
        cfg=1.0,
        shift=7.0,
        negative=HY_NEGATIVE,
        civitai_bases_loose=("Hunyuan Video",),
        licence=HUNYUAN_LICENCE,
    ),
    ModelDef(
        id="hy15-720p-hq",
        label="HunyuanVideo 1.5 720p — fp16（品質優先）",
        methods=("i2v",),
        family="hunyuan15",
        vram_gb=20,
        files=[
            ModelFile(HY_REPO, "split_files/diffusion_models/hunyuanvideo1.5_720p_i2v_fp16.safetensors", "diffusion_models", 16653368128),
            *HY_COMMON,
        ],
        tiers=HY_TIERS,
        fps=24,
        length=121,
        steps=20,
        cfg=6.0,  # official template value for the non-distilled build
        shift=7.0,
        negative=HY_NEGATIVE,
        civitai_bases_loose=("Hunyuan Video",),
        licence=HUNYUAN_LICENCE,
        note="官方範例的設定（cfg 6 / shift 7 / 20 步）。",
    ),
    # Files only: LTX-2.3's official pipeline is a ~50 node graph with two-pass
    # sampling, latent upscaling and a joint audio/video latent. Reproducing it
    # in code would be guesswork this stack cannot verify, so the manager
    # downloads the weights and you drive them from ComfyUI's own built-in
    # template (or export that template and drop it in workflows/).
    ModelDef(
        id="ltx23",
        label="LTX-2.3 22B — 只下載檔案（用 ComfyUI 內建範例跑）",
        family="files_only",
        vram_gb=24,
        files=[
            ModelFile("Lightricks/LTX-2.3-fp8", "ltx-2.3-22b-dev-fp8.safetensors", "checkpoints", 29145431166),
            ModelFile("Comfy-Org/ltx-2", "split_files/text_encoders/gemma_3_12B_it_fp4_mixed.safetensors", "text_encoders", 9447702218),
            ModelFile("Comfy-Org/ltx-2.3", "split_files/loras/ltx_2.3_22b_distilled_1.1_lora_dynamic_fro09_avg_rank_111_bf16.safetensors", "loras", 2741024390),
            ModelFile("Comfy-Org/ltx-2", "split_files/loras/gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors", "loras", 628203616),
            ModelFile("Lightricks/LTX-2.3", "ltx-2.3-spatial-upscaler-x2-1.1.safetensors", "latent_upscale_models", 995743560),
        ],
        tiers={},
        supports_lora=False,
        civitai_bases=("LTXV 2.3",),
        licence=LTX_LICENCE,
        note="影音同步一次生成。下載完在 ComfyUI（:8188）用 Workflow → Browse Templates → LTX-2.3 I2V。",
    ),
    ModelDef(
        # The current LTX generation, and the newest open-weight video model in
        # this catalogue. Worth stating why it is here at all: the models people
        # ask for by name - Seedance, Wan 2.5 - are closed APIs with no weights
        # to download, so "the latest" and "runs on your machine" have stopped
        # being the same list. This is the newest thing that is actually both.
        id="ltx25",
        label="LTX-2.5 22B — 只下載檔案（用 ComfyUI 內建範例跑）",
        family="files_only",
        vram_gb=24,
        files=[
            # The int8 "convrot" builds are the ones ComfyUI's own LTX-2.5 page
            # lists. The bf16 transformer is 42GB and the distilled one is what
            # the documented workflow loads, so the extra 20GB buys nothing here.
            ModelFile(LTX25_REPO,
                      "diffusion_models/ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors",
                      "diffusion_models", 21504034224, gated=True),
            # Not interchangeable with LTX-2.3's Gemma 3: the projection is baked
            # in and the loader checks the encoder version against the one the
            # checkpoint was trained with, so this exact file or nothing.
            ModelFile(LTX25_REPO,
                      "text_encoders/gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors",
                      "text_encoders", 15372969374, gated=True),
            ModelFile(LTX25_REPO, "vae/ltx-2.5-video-vae-bf16.safetensors",
                      "vae", 1472223346, gated=True),
            # Audio is generated in the same pass as the picture, so its VAE is
            # not optional the way an upscaler is.
            ModelFile(LTX25_REPO, "vae/ltx-2.5-audio-vae-bf16.safetensors",
                      "vae", 364866540, gated=True),
            ModelFile(LTX25_REPO,
                      "latent_upscale_models/ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0.safetensors",
                      "latent_upscale_models", 995778752, gated=True),
        ],
        tiers={},
        supports_lora=False,
        civitai_bases=("LTXV 2.5",),
        licence=LTX_LICENCE,
        civitai_bases_loose=("LTXV 2.3",),
        note="影音同步一次生成，官方說支援到 4K HDR / 50fps。"
             "**這個倉庫是 gated**：要先到 huggingface.co/Lightricks/LTX-2.5 按同意授權，"
             "再到「設定」分頁貼上 Hugging Face token，否則下載會直接 401。"
             "下載完在 ComfyUI（:8188）用 Workflow → Browse Templates → LTX-2.5。",
    ),
]

BY_ID = {m.id: m for m in MODELS}


def get(model_id: str) -> ModelDef | None:
    return BY_ID.get(model_id)


def runnable() -> list[ModelDef]:
    return [m for m in MODELS if m.runnable]


@dataclass
class Lora:
    name: str
    strength: float = 1.0


@dataclass
class GenParams:
    """Per-job sampling parameters, seeded from the model then overridden."""

    steps: int
    cfg: float
    shift: float
    sampler: str
    scheduler: str
    length: int
    fps: int
    boundary: int | None = None
    lightning: bool = False
    weight_dtype: str = "default"
    loras: list[Lora] = field(default_factory=list)
    loras_high: list[Lora] = field(default_factory=list)
    loras_low: list[Lora] = field(default_factory=list)
    # Post-processing on the decoded frames. Neither changes what the model
    # generates; both are applied after it, so they cost no VRAM during sampling.
    interpolate: int = 1  # frame multiplier; 1 = off
    interpolate_model: str = ""
    upscaler: str = ""  # a file in models/upscale_models, "" = leave as rendered

    @classmethod
    def defaults_for(cls, model: ModelDef, lightning: bool = False) -> "GenParams":
        use_lightning = lightning and bool(model.lightning)
        return cls(
            steps=model.lightning_steps if use_lightning else model.steps,
            cfg=model.lightning_cfg if use_lightning else model.cfg,
            shift=model.lightning_shift if use_lightning else model.shift,
            sampler=model.sampler,
            scheduler=model.scheduler,
            length=model.length,
            fps=model.fps,
            boundary=(model.lightning_steps // 2) if use_lightning else model.boundary,
            lightning=use_lightning,
        )

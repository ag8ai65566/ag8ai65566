## Ranking

**My recommendation is VoxCPM2 as the primary training candidate, with Qwen3-TTS-12Hz-1.7B-Base as the fallback.** Qwen remains a strong choice, but the earlier suggestion that it is simply “the best” is not supported by the available evidence.

**Checked date: 2026-10-06 for every linked source and table entry below.** This is source-based research; I did not run GPU training or conduct listening tests. Hardware budgets and proposed experimental settings are explicitly distinguished from published measurements.

The central limitation is that **zero-shot cloning results do not establish which model wins after 1–50 hours of single-speaker fine-tuning**. I found no controlled public comparison covering that entire use case. The ranking therefore combines published quality evidence, actual training support, Japanese/English coverage, licensing, and deployment practicality.

Definitions:

- **Zero-shot:** a reference recording conditions generation without updating weights.
- **Fine-tuning:** speaker recordings update model weights or train an adapter. Saving a reference embedding is not fine-tuning.
- **Official:** training code published by the model’s maintainers.
- **NR:** no sufficiently documented, version-specific VRAM measurement verified.
- **E:** my planning allocation, not a measured minimum.
- Language support alone does not establish accent or prosody fidelity.

**The first four entries are ordered by suitability for this platform. Subsequent entries are conditional challengers or alternatives, rather than a fabricated universal quality ranking.**

| Model / relevant release | Release date | True fine-tuning support | Japanese quality/evidence | English quality/evidence | Fidelity assessment | Code / weights license | Training VRAM | Inference VRAM | Sources |
|---|---|---|---|---|---|---|---|---|---|
| **1. VoxCPM2** | 2026-04 | **Official full training and LoRA** | Competitive multilingual results; particularly strong speaker SIM | Strong SIM; more transcription errors than Qwen in shared evaluation | Best initial candidate when identity preservation leads | Apache-2.0 / Apache-2.0 | Author estimates: **~20 GB LoRA; ~40 GB full** | Author estimate **~8 GB** | [Project](https://github.com/OpenBMB/VoxCPM), [training](https://voxcpm.readthedocs.io/en/latest/finetuning/finetune.html), [weights](https://huggingface.co/openbmb/VoxCPM2) |
| **2. Qwen3-TTS-12Hz-1.7B-Base** | 2026-01-22 | **Official single-speaker fine-tuning** | Strong measured intelligibility | Particularly strong measured intelligibility | Excellent fallback; speaker SIM trails VoxCPM2 in the comparison below | Apache-2.0 / Apache-2.0 | **48–80 GB E** for an uncomplicated training setup; optimized community implementations use less | **12–24 GB E** | [Project](https://github.com/QwenLM/Qwen3-TTS), [training](https://github.com/QwenLM/Qwen3-TTS/tree/main/finetuning), [weights](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-Base) |
| **3. CosyVoice 3, 0.5B-2512** | Weights 2025-12; continued 2026 development | **Official training recipes** | Supported and benchmarked | Supported and benchmarked | Strong practical alternative, especially if Mandarin becomes important | Apache-2.0 / Apache-2.0 | NR | NR | [Project](https://github.com/FunAudioLLM/CosyVoice), [released checkpoint](https://huggingface.co/FunAudioLLM/Fun-CosyVoice3-0.5B-2512) |
| **4. GPT-SoVITS v2ProPlus / v4** | v4: 2025-04-22; v2Pro series: 2025-06-06 | **Official GPT and SoVITS training, integrated UI** | Practical Japanese adaptation candidate; no convincing current head-to-head victory established | Supported; evaluate against newer multilingual models | Author says v2Pro can outperform v4; v4 relies more heavily on reference timbre | MIT / MIT for official checkpoint repository | NR; varies substantially by branch | NR | [Project and branch differences](https://github.com/RVC-Boss/GPT-SoVITS), [releases](https://github.com/RVC-Boss/GPT-SoVITS/releases), [weights](https://huggingface.co/lj1995/GPT-SoVITS) |
| **Fish Speech / OpenAudio S1-mini → S2 Pro** | S1 generation: 2025; S2: 2026-03 | **Official training code**, but important RL fine-tuning warning | Excellent reported intelligibility | Excellent reported intelligibility and expressive controls | Serious quality challenger; less attractive as the default training platform | Current repository and S2 weights: **Fish Audio Research License** | NR for a dependable S2 recipe | Official guidance recommends **24 GB+** | [Project](https://github.com/fishaudio/fish-speech), [paper](https://arxiv.org/abs/2603.08823), [training caveats](https://speech.fish.audio/finetune/), [license](https://github.com/fishaudio/fish-speech/blob/main/LICENSE) |
| **MOSS-TTS / v1.5 family** | 2026-02; v1.5 updates 2026-05/06 | **Official training and adaptation support; check architecture-specific recipe** | Supported | Supported | Promising expressive alternative; larger deployment footprint for larger variants | Apache-2.0 / Apache-2.0 | NR | Variant-dependent; quantized configurations available | [Project](https://github.com/OpenMOSS/MOSS-TTS), [weights](https://huggingface.co/OpenMOSS-Team/MOSS-TTS) |
| **OmniVoice** | 2026-04 | **Official training, evaluation and fine-tuning pipeline** | Supported; broad multilingual coverage | Supported | Useful diffusion-model challenger; not established as the large-data speaker winner | Apache-2.0 / **CC-BY-NC** | NR | NR; Apple Silicon supported | [Project](https://github.com/k2-fsa/OmniVoice), [model and license](https://huggingface.co/k2-fsa/OmniVoice) |
| **IndexTTS2 → IndexTTS2.5** | 2: 2025-09-08; **2.5: 2026-08-10** | Official inference verified; official speaker-training pipeline **not verified** | **2.5 adds Japanese**; do not attribute this to original 2 | Supported | Attractive emotion/reference controls; training workflow remains the obstacle | Custom **Bilibili Model Use License** | NR | NR | [Project](https://github.com/index-tts/index-tts), [license](https://github.com/index-tts/index-tts/blob/main/LICENSE) |
| **Higgs Audio v2 → Higgs TTS 3** | v2: 2025-07; v3: 2026-06 | Community adaptation exists; official complete speaker-training recipe not verified | v3 includes Japanese; v2 evidence less clear | Expressive conversational synthesis | Strong control candidate; restrictive v3 platform licensing | v2 code Apache-2.0; weights custom. v3 weights **research/noncommercial with creator exception** | NR | NR | [v2 project](https://github.com/boson-ai/higgs-audio), [v3 card and terms](https://huggingface.co/bosonai/higgs-tts-3-4b) |
| **Chatterbox Multilingual V3** | Original: 2025-05; V3 available in 2026 | Community fine-tuning; no general official training pipeline verified | Supported; evaluate exact V3 checkpoint | Supported; Turbo/Nano are separate English-focused variants | Accessible cloning; no established large-data superiority | MIT / MIT | NR | NR; Nano supports CPU, but is English-only | [Official family](https://github.com/resemble-ai/chatterbox), [community training](https://github.com/gokhaneraslan/chatterbox-finetuning) |
| **Zonos 0.1 → ZONOS2** | 0.1: 2025-02; 2: 2026-06 | Official inference; official speaker-training pipeline not verified | Supported in ZONOS2 | Supported | New multilingual cloning contender; not currently my training-first choice | Apache-2.0 / Apache-2.0 | NR | Backend/quantization-dependent; CPU/Metal implementation exists | [ZONOS2](https://github.com/Zyphra/ZONOS2), [weights](https://huggingface.co/Zyphra/ZONOS2), [C++ inference](https://github.com/Zyphra/zonos2.cpp) |
| **Tencent AuK / AuK-Flash** | **2026-09-09** | **Official fine-tuning pipeline** | Adequate Japanese evaluation not verified | Strong reported EN/ZH generation and editing | Important September release; insufficient JA evidence to promote above the finalists | MIT / MIT for released AuK components | NR | Published short-input test: **~25 GiB**, or **~17 GiB with CPU offload** | [Project](https://github.com/Tencent-Hunyuan/AuK), [training](https://github.com/Tencent-Hunyuan/AuK/blob/main/docs/FINETUNING.md), [paper](https://arxiv.org/abs/2609.08936) |
| **Irodori-TTS v4.1-Small** | 2026; current v4.1 checkpoint | **Official full training and PEFT/LoRA** | Japanese-specific; reading benchmarks published | **Japanese-only** | Worth testing for a separate JA engine; short-reference similarity has documented limitations | MIT / MIT, with stated consent restrictions | NR | NR; quantized variants available | [Project](https://github.com/Aratako/Irodori-TTS), [model and limitations](https://huggingface.co/Aratako/Irodori-TTS-v4.1-Small) |
| **Sarashina2.2-TTS** | **2026-04-28**; report June | Official zero-shot inference; fine-tuning pipeline not verified | Strong Japanese-specific reading and cloning research | Supported | Valuable Japanese evaluation baseline | Custom **Sarashina Model NonCommercial License** | NR | Official Docker guidance: **~6 GB**, more for vLLM | [Project](https://github.com/sbintuitions/sarashina2.2-tts), [paper](https://arxiv.org/abs/2606.25369), [license](https://github.com/sbintuitions/sarashina2.2-tts/blob/main/LICENSE) |
| **F5-TTS v1 / E2-TTS reproduction** | Initial: 2024-10; F5 v1: 2025-03-12 | **Official training and fine-tuning UI** | Community Japanese checkpoints; stock models are not a turnkey JA choice | Established baseline | Useful training research baseline; less compelling bilingual starting point | MIT code / **CC-BY-NC-4.0 pretrained weights** | Recipe-dependent; NR here | NR | [Project](https://github.com/SWivid/F5-TTS), [community checkpoints](https://github.com/SWivid/F5-TTS/blob/main/src/f5_tts/infer/SHARED.md) |
| **Microsoft VibeVoice / Realtime** | Original: 2025-08; Realtime: 2025-12 | Official **TTS** fine-tuning not verified; ASR training is a different task | Original mainly EN/ZH; experimental realtime Japanese voices are not proof of mature JA adaptation | Strong long-form/realtime focus | Less suitable for this training-first bilingual platform | MIT for released components; inspect model-specific notices | NR | NR | [Current project and release history](https://github.com/microsoft/VibeVoice), [original weights](https://huggingface.co/microsoft/VibeVoice-1.5B) |
| **MegaTTS 3** | 2025-03 | Official training not verified; **reference encoder withheld** | Not an official target language | Supported | Cannot provide complete arbitrary-speaker enrollment locally from the official release | Apache-2.0 for released code/weights | — | GPU or CPU; NR | [Project](https://github.com/bytedance/MegaTTS3), [encoder restriction](https://huggingface.co/ByteDance/MegaTTS3) |
| **Spark-TTS** | 2025-03 | Community adaptation; official release primarily inference | Not officially supported | Supported | EN/ZH cloning/design baseline | Apache-2.0 code / **CC-BY-NC-SA-4.0 weights** | NR | NR | [Project](https://github.com/SparkAudio/Spark-TTS), [weight license](https://huggingface.co/SparkAudio/Spark-TTS-0.5B) |
| **Llasa** | 2025-02; training release 2025-06 | **Official author training/fine-tuning repository** | Depends on checkpoint; no compelling official JA result established here | Supported | Flexible research platform, less turnkey | Training repository and relevant weights **CC-BY-NC-4.0** | Model-dependent: 1B/3B/8B | NR | [Training](https://github.com/zhenye234/LLaSA_training), [weights](https://huggingface.co/HKUSTAudio/Llasa-3B) |
| **Orpheus** | 2025-03-18 | **Official training/fine-tuning code** | Not established for the main English checkpoint | Expressive English focus | Reasonable English adaptation baseline; weaker fit for the bilingual requirement | Apache-2.0 as published; inspect bundled dependencies | NR | NR | [Project](https://github.com/canopyai/Orpheus-TTS), [checkpoint](https://huggingface.co/canopylabs/orpheus-3b-0.1-ft) |
| **StyleTTS 2** | 2023 | **Official training/fine-tuning** | Requires additional Japanese frontend/model work | Strong established English research baseline | Useful controlled single-speaker system; more engineering for JA | MIT code; **weights vary**, LibriTTS has additional restrictions | Recipe-dependent | NR | [Project](https://github.com/yl4579/StyleTTS2), [author’s license clarification](https://github.com/yl4579/StyleTTS2/discussions/152) |
| **Kokoro-82M v1.0** | 2025-01-27 | No official turnkey speaker-cloning/training workflow | Preset Japanese voices | Strong lightweight preset synthesis | **Does not meet custom trained-voice requirement** | Apache-2.0 | — | CPU-capable | [Model card](https://huggingface.co/hexgrad/Kokoro-82M) |
| **Breeze-TTS-2** | **Weights: 2026-08-25** | Official inference verified; speaker training not verified | **No Japanese** | Strong English preference-ranking evidence | Interesting EN/ZH inference option, not the bilingual training solution | Apache-2.0 code / custom **research/noncommercial weights** | NR | Published: **7.7 GiB eager**, **14.4 GiB accelerated** | [Project and terms](https://github.com/breezeblue-ai/breeze-tts), [preference leaderboard](https://artificialanalysis.ai/text-to-speech/leaderboard/provider-voice) |
| **Voxtral TTS** | 2026-03-23 | Official speaker fine-tuning not verified | **No Japanese** | Supported | Excluded by language requirement | Weights **CC-BY-NC-4.0** | NR | NR | [Official release](https://mistral.ai/news/voxtral-tts/) |

The many “NR” entries are deliberate: architecture size, a successful Colab notebook, and a vendor’s minimum loading requirement are different things. They should not be presented as interchangeable training-memory measurements.

**What the measurable comparison actually says**

The following is zero-shot performance on **MiniMax-MLS-Test**, reproduced in VoxCPM2’s report. Lower WER is better; higher SIM is better. These are author-reported comparisons, not my measurements. [VoxCPM2 report, Tables 6–7](https://arxiv.org/html/2606.06928v1)

| Model | Japanese WER ↓ | Japanese SIM ↑ | English WER ↓ | English SIM ↑ |
|---|---:|---:|---:|---:|
| Qwen3-TTS | 3.82% | 78.8 | **0.93%** | 77.5 |
| Fish Audio S2 | **2.76%** | 79.6 | 1.62% | 79.7 |
| VoxCPM2 | 4.63% | **82.8** | 2.29% | **85.4** |

This supports a **similarity-versus-text-accuracy tradeoff**, not a universal winner. Speaker embedding similarity also does not directly measure Japanese pitch accent, habitual pauses, or whether a familiar listener recognizes the speaker’s mannerisms.

| Requested criterion | Defensible conclusion |
|---|---|
| **Speaker similarity** | VoxCPM2 leads the three-model comparison above. Whether that survives equal-data fine-tuning remains untested publicly. |
| **Accent and prosody fidelity** | No defensible comprehensive ranking after large-data adaptation. Prioritize testing VoxCPM2’s continuation conditioning and Qwen’s transcript-conditioned cloning. Qwen explicitly distinguishes richer contextual conditioning from speaker-embedding-only cloning. [Qwen report](https://arxiv.org/html/2601.15621v1) |
| **Verbal habits** | Separate **acoustic habits**—rhythm, breathiness, phrase endings—from **lexical habits**—favorite expressions and fillers. The latter belong in the supplied script; unwanted invented words should count as errors. This is my evaluation recommendation, consistent with these systems’ text-conditioned interfaces. [VoxCPM interface](https://voxcpm.readthedocs.io/en/latest/usage_guide.html) |
| **Japanese quality** | Fish leads WER among the three above; Qwen follows. Also test Japanese-specific reading with Sarashina’s benchmark rather than relying exclusively on multilingual ASR scores. [Sarashina research](https://arxiv.org/abs/2606.25369) |
| **English quality** | Qwen leads WER in the displayed comparison. English listener-preference rankings answer a different question: Breeze’s strong ranking does not establish speaker-training superiority. [Preference leaderboard](https://artificialanalysis.ai/text-to-speech/leaderboard/provider-voice) |
| **Naturalness** | No trustworthy single MOS ranking spans these versions, languages, and adapted speakers. Different listener pools and tests make cross-paper MOS subtraction misleading. Use blinded listening on the author’s target voice. |
| **Stability** | Fish reports SEED-TTS English WER **0.99%** and Chinese CER **0.54%**; these do not measure every repetition, omission, or long-form failure. Qwen is another strong text-adherence candidate. [Fish S2 report](https://arxiv.org/abs/2603.08823) |
| **Emotion/style control** | Fish S2 and Higgs 3 offer expressive inline controls; IndexTTS2.5 offers dedicated emotion controls. VoxCPM2 supports descriptions but has a fidelity/control mode distinction. Qwen capabilities depend on the checkpoint variant. [Fish](https://github.com/fishaudio/fish-speech), [Higgs](https://huggingface.co/bosonai/higgs-tts-3-4b), [Index](https://github.com/index-tts/index-tts), [Qwen](https://github.com/QwenLM/Qwen3-TTS) |

## Recommendation

**Primary: VoxCPM2, starting with LoRA and comparing it against full fine-tuning.**

My confidence is **moderate**, not conclusive. It combines a favorable identity-preservation signal, official adaptation options, Japanese/English/Mandarin coverage, and straightforward commercial licensing. The official training implementation supports both adapters and complete model checkpoints, allowing the platform to compare them without changing model families. [Training implementation](https://github.com/OpenBMB/VoxCPM/blob/main/scripts/train_voxcpm_finetune.py), [model card](https://huggingface.co/openbmb/VoxCPM2)

Its principal weakness is equally concrete: **higher text error in the comparison above**, plus documented long-input instability. Therefore, promote a trained VoxCPM2 voice only if it passes the same pronunciation and omission tests as Qwen. [Usage limitations](https://voxcpm.readthedocs.io/en/latest/usage_guide.html)

**Fallback: Qwen3-TTS-12Hz-1.7B-Base.**

Qwen’s report includes actual target-speaker adaptation, not just zero-shot cloning. For the released 12Hz 1.7B configuration, its target-speaker multilingual table reports **English WER 0.899% and Japanese WER 4.924%**. The often-highlighted Japanese **3.875%** belongs to a different 25Hz configuration; it should not be attributed to the downloadable 12Hz model. This experiment supports Qwen’s candidacy but does not establish superiority on the author’s speaker. [Qwen report, Table 9](https://arxiv.org/html/2601.15621v1)

Use the correct Qwen variant:

- **Base:** reference cloning and the documented speaker fine-tuning route.
- **CustomVoice:** supplied named voices; the 1.7B model supports delivery instructions.
- **VoiceDesign:** creates a voice from a description.
- Fine-tuning Base into a custom speaker does **not automatically reproduce all instruction-following behavior** of the separately trained CustomVoice or VoiceDesign models. [Official model descriptions](https://github.com/QwenLM/Qwen3-TTS), [fine-tuning code](https://github.com/QwenLM/Qwen3-TTS/tree/main/finetuning)

**Why not Fish as the primary?** Its quality evidence deserves attention, and personal noncommercial experimentation is possible under its terms. However, the current license restricts commercial use of both the released software and models, while its fine-tuning documentation warns that adapting RL-trained models can degrade performance. The guide also still contains S1-mini-specific examples, so “training code exists” is not enough to assume a polished S2 training recipe. [License](https://github.com/fishaudio/fish-speech/blob/main/LICENSE), [fine-tuning guide](https://speech.fish.audio/finetune/)

**Why retain GPT-SoVITS in testing?** It is a useful Japanese-oriented practical challenger with an integrated preparation/training workflow. Its maintainers explicitly distinguish v2Pro’s learned-voice behavior from v3/v4’s stronger reference dependence. That is relevant when the user wants a model to absorb a substantial recording collection. [Maintainer’s branch comparison](https://github.com/RVC-Boss/GPT-SoVITS)

Community evidence is useful mainly for identifying failures and backend differences. The reproducible samples and local timings in [tts-bench](https://github.com/5uck1ess/tts-bench) are more useful than unsourced “best TTS” lists, but its small listening comparisons do not substitute for a controlled Japanese/English adaptation study.

**Finalist licenses**

| Finalist | Code | Weights | Personal use | Commercial platform/use |
|---|---|---|---|---|
| VoxCPM2 | Apache-2.0 | Apache-2.0 | Permitted under license terms | Permitted; preserve required notices when distributing relevant artifacts |
| Qwen3-TTS-12Hz-1.7B-Base | Apache-2.0 | Apache-2.0 | Permitted under license terms | Permitted; preserve required notices when distributing relevant artifacts |

These conclusions concern model licensing; speaker and recording permissions remain separate. Sources: [VoxCPM license](https://github.com/OpenBMB/VoxCPM/blob/main/LICENSE), [VoxCPM2 weights](https://huggingface.co/openbmb/VoxCPM2), [Qwen repository](https://github.com/QwenLM/Qwen3-TTS), [Qwen weights](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-Base).

## Training recipe (primary)

**1. Build an audition dataset before processing all 50 hours.**

My proposed progression is:

| Usable, consented recordings | Purpose |
|---|---|
| **1 hour** | Initial adaptation and pipeline test; not a promise of maximum fidelity |
| **5–10 hours** | First serious comparison of VoxCPM2 LoRA, VoxCPM2 full tuning, and Qwen |
| **10–20 hours** | Practical target when recordings cover the intended languages and delivery styles |
| **20–50+ hours** | Add material when it contributes missing phonetics, accents, moods, or recording situations; measure whether it helps |

These are **engineering recommendations**, not published minimum requirements. VoxCPM’s documentation allows much smaller adaptation sets but also warns about diminishing returns and early overfitting. [Training guide](https://voxcpm.readthedocs.io/en/latest/finetuning/finetune.html)

For a bilingual speaker, include actual recordings in **both languages**. Do not interpret successful cross-language synthesis as evidence that the model has recovered that particular person’s unrecorded Japanese accent.

**2. Prepare clips and transcripts.**

Use clean mono WAV working files while retaining untouched originals. VoxCPM2’s encoder operates at **16 kHz**, while its decoder produces **48 kHz**; use the model’s prescribed configuration rather than changing the training sample rate to match the output. Its loader can resample recordings. Recommended clip lengths are **3–30 seconds**, with exact transcripts and short trailing silence. [Data requirements](https://voxcpm.readthedocs.io/en/latest/finetuning/finetune.html)

Example manifest, with original illustrative content:

```jsonl
{"audio":"wav/ja_0001.wav","text":"今日は、少しゆっくり話してみます。","duration":4.3}
{"audio":"wav/en_0001.wav","text":"Well, I thought we could try again tomorrow.","duration":4.8,"ref_audio":"wav/en_0042.wav","ref_duration":7.2}
```

`ref_audio` should be another permitted recording of the same speaker. The guide recommends including reference conditioning in approximately **30–50%** of examples. [Manifest specification](https://voxcpm.readthedocs.io/en/latest/finetuning/finetune.html)

My Japanese preparation rules:

- Keep natural Japanese orthography; do not convert the entire corpus to romaji.
- Correct ASR output manually, including omitted fillers, repetitions, particles, and sentence endings.
- Maintain a pronunciation dictionary for names, counters, dates, abbreviations, and ambiguous kanji.
- Keep the displayed script separately from any pronunciation-adjusted synthesis text.
- Use the supplied tokenizer; do not train a replacement tokenizer for ordinary Japanese adaptation.

These are proposed preparation choices. The official model accepts regular text; its documented phoneme overrides concern Chinese and English, so I would not assume an equivalent Japanese phoneme interface. [Text-input documentation](https://voxcpm.readthedocs.io/en/latest/usage_guide.html)

Split data **by recording session**, not randomly among adjacent clips. My starting allocation is 90% training, 5% validation, and 5% held-out evaluation, with languages and delivery styles represented in each.

**3. Start from the official recipes.**

The repository’s current configurations provide the following starting points:

| Setting | LoRA | Full fine-tuning |
|---|---:|---:|
| Learning rate | `1e-4` | `1e-5` |
| Microbatch | 2 | 2 |
| Gradient accumulation | 8 | 8 |
| Effective batch on one GPU | 16 | 16 |
| Weight decay | `0.01` | `0.01` |
| Gradient clipping | `1.0` | `1.0` |
| Maximum batch tokens | `8192` | `8192` |
| LoRA rank / alpha | 32 / 32 | Not applicable |
| Adaptation targets | LM and diffusion transformer; projections disabled initially | Full recipe |

Sources: [official LoRA configuration](https://github.com/OpenBMB/VoxCPM/blob/main/conf/voxcpm_v2/voxcpm_finetune_lora.yaml), [official full configuration](https://github.com/OpenBMB/VoxCPM/blob/main/conf/voxcpm_v2/voxcpm_finetune_all.yaml).

Set actual training/validation manifests and checkpoint paths. The examples use 1,000 updates and 100 warmup updates; **do not blindly reuse that schedule for every dataset size**. The trainer counts optimizer updates after gradient accumulation. [Trainer implementation](https://github.com/OpenBMB/VoxCPM/blob/main/scripts/train_voxcpm_finetune.py)

The documented launch entry point is:

```bash
python scripts/train_voxcpm_finetune.py --config_path conf/speaker_lora.yaml
```

For a short pilot, I would validate and save approximately every quarter epoch, then compare checkpoints around **1–3 epochs**. The official troubleshooting guidance warns that overtraining can make the model ignore new text and reproduce memorized utterances. [Fine-tuning FAQ](https://voxcpm.readthedocs.io/en/latest/finetuning/faq.html)

**4. Choose training hardware conservatively.**

The author’s approximate VRAM figures are **20 GB for LoRA and 40 GB for full tuning**, under specified batching assumptions—not universal minima. [Hardware guidance](https://voxcpm.readthedocs.io/en/latest/finetuning/finetune.html)

My allocation:

- **RTX 4090, 24 GB:** first LoRA pilot; reduce microbatch/clip length if necessary.
- **L40S, 48 GB:** comfortable LoRA experiments; full tuning needs a measured memory check.
- **A100, 80 GB:** recommended first full-tuning rental, providing room for references and longer clips.
- **H100, 80 GB:** evaluate by total job cost; a higher hourly rate is worthwhile only if throughput compensates.

**5. Estimate time from a measured pilot, not a model-size guess.**

I did not find a reproducible VoxCPM2 wall-clock measurement matching this exact 1–50-hour bilingual task. A defensible estimate comes from 100 warmed-up optimizer updates on the intended GPU.

With average **10-second clips** and effective batch **16**:

| Audio | Approximate clips | Updates per epoch |
|---|---:|---:|
| 1 hour | 360 | 23 |
| 10 hours | 3,600 | 225 |
| 50 hours | 18,000 | 1,125 |

These are calculated approximations before filtering and dynamic batching. Training time is:

**updates × measured seconds per update ÷ 3,600.**

For illustration only, **if** the pilot measures 10 seconds per optimizer update, three epochs would take approximately **1.9 hours for 10 hours of audio**, or **9.4 hours for 50 hours**. This is not a published performance prediction; preprocessing, validation, checkpointing, and failed experiments add time.

Current rental prices give the following budget:

| GPU | RunPod displayed hourly price | Eight-hour allocation |
|---|---:|---:|
| RTX 4090 24 GB | $0.74 | $5.92 |
| L40S 48 GB | $1.09 | $8.72 |
| A100 PCIe 80 GB | $1.59 | $12.72 |
| H100 PCIe 80 GB | $2.89 | $23.12 |
| H100 SXM 80 GB | $3.49 | $27.92 |

Prices are from the page updated **2026-09-27**, checked **2026-10-06**; availability and storage charges are additional considerations. [RunPod pricing](https://www.runpod.io/pricing)

Modal lists GPU-only equivalents of approximately **$2.50/hour for A100 80 GB**, **$3.95/hour for H100**, and **$1.95/hour for L40S**, with CPU, memory, and other resources charged separately. Thus, eight A100 GPU-hours are approximately **$20** before those additions. [Modal pricing](https://modal.com/pricing)

**6. Evaluate the trained voice, not just the training loss.**

My proposed acceptance suite:

| Test | What to measure |
|---|---|
| Unseen normal sentences | English WER; Japanese CER and reading-normalized kana CER |
| Difficult text | Names, counters, dates, long vowels, gemination, code-switching |
| Voice identity | Speaker-embedding similarity **plus blinded human similarity judgments** |
| Accent/prosody | Japanese pitch-accent errors, mora timing, English stress/vowel realization, habitual phrase endings |
| Naturalness | Blinded ratings against held-out human recordings and the untuned model |
| Stability | Repetition, skipped text, invented speech, premature stopping, runaway duration |
| Expressive fidelity | Neutral, conversational, excited, subdued, whispered—only where suitable consented examples exist |
| Overfitting | New-text performance deteriorating while training loss improves; memorized phrases; lost bilingual ability |

Use the same texts, references, and sampling policy across models. Keep unseen **text** tests separate from acoustic reconstruction tests. VoxCPM’s own guidance notes that lower validation loss need not correspond to better perceived quality. [Training walkthrough](https://voxcpm.readthedocs.io/en/latest/finetuning/walkthrough.html), [failure modes](https://voxcpm.readthedocs.io/en/latest/finetuning/faq.html)

## Inference and control

**VoxCPM2 fits the requested consumer-GPU deployment.** The project reports approximately **8 GB VRAM**, RTX 4090 RTF around **0.30** in its standard implementation, and approximately **0.13** with accelerated serving. These are author-reported figures, not guaranteed performance for every fine-tuned checkpoint or workload. RTF 0.30 means roughly three seconds of computation for ten seconds of audio. [Official performance summary](https://github.com/OpenBMB/VoxCPM)

For deployment, I would allocate **12 GB for one modest worker** or **24 GB for more headroom**, then measure peak memory with the actual reference lengths and concurrency. Those allocations are my recommendations.

The official Python runtime supports **CUDA, Apple MPS, and CPU**. A separate C++ implementation supports GGUF inference on CPU/Metal/CUDA/Vulkan. The project reports **RTF about 1.76 on M4 Pro/Metal** for one Q8 configuration—slower than real time. Compatibility of a particular trained checkpoint or adapter with a converted backend still needs testing. [Python devices](https://voxcpm.readthedocs.io/en/latest/quickstart.html), [C++ backend](https://github.com/tc-mb/llama.cpp-omni)

**Streaming:** VoxCPM2 can stream generated audio chunks, but its documented API does **not** support continuously arriving text tokens during the same generation. Buffer complete sentences, then stream their audio. [Streaming documentation](https://voxcpm.readthedocs.io/en/latest/usage_guide.html)

For Qwen, the report gives **RTF 0.313 and 101 ms first-packet latency** for the 1.7B 12Hz model in its optimized setup. The widely repeated **97 ms** figure belongs to the 0.6B variant. Neither is a promise for an ordinary consumer-GPU Python installation. [Qwen streaming evaluation](https://arxiv.org/html/2601.15621v1)

**Control syntax is model-specific.**

| System | How control is supplied | Important limitation |
|---|---|---|
| **VoxCPM2 controllable clone** | Reference audio plus a parenthesized description, e.g. `(quiet, unhurried delivery)` | This is a style instruction, not a guarantee of exact acoustic imitation |
| **VoxCPM2 Hi-Fi clone** | Prompt audio plus exact prompt transcript, optionally alongside the reference | **Control instructions are ignored in this mode** |
| **Qwen 1.7B CustomVoice** | Separate natural-language `instruct` argument | Do not assume equivalent control survives ordinary Base speaker fine-tuning |
| **Fish S2** | Inline expressive tags/descriptions | Supported syntax differs from ElevenLabs; training and license caveats remain |
| **Higgs TTS 3** | Inline emotion, style, pause and sound-effect controls | Platform embedding/hosting requires careful license review |
| **ElevenLabs v4** | Audio tags including laughter and whispered delivery | Tags are model-specific, not a portable standard |

Sources: [VoxCPM modes](https://voxcpm.readthedocs.io/en/latest/usage_guide.html), [Qwen controls](https://github.com/QwenLM/Qwen3-TTS), [Fish S2](https://github.com/fishaudio/fish-speech), [Higgs controls](https://huggingface.co/bosonai/higgs-tts-3-4b), [ElevenLabs v3/v4 tags](https://elevenlabs.io/docs/help-center/product/core-capabilities/text-to-speech/how-do-audio-tags-work-with-eleven-v3-and-v4).

My platform design would expose **“preserve recorded delivery”** and **“direct a new delivery”** as separate choices. For maximum resemblance, maintain a small library of the consenting speaker’s neutral, energetic, subdued, and other permitted reference recordings. Do not pass ElevenLabs tags through unchanged and assume they work.

## Building blocks to reuse

**Start with the official VoxCPM implementation as the correctness reference, then adopt an accelerated server after checkpoint compatibility tests.**

| Component | Reuse | Maintenance assessment as checked |
|---|---|---|
| **Official VoxCPM Python package and `app.py`** | Inference, reference conditioning, Gradio audition UI | Maintained release line; latest verified package release **2.0.3, 2026-05-11**, includes runtime and streaming fixes. [Releases](https://github.com/OpenBMB/VoxCPM/releases) |
| **Official `lora_ft_webui.py` and training script** | Prototype training interface, checkpoints, validation | Maintained within the same project; 2.0.3 explicitly fixes LoRA UI issues and adds manifest validation. [Release notes](https://github.com/OpenBMB/VoxCPM/releases) |
| **NanoVLLM-VoxCPM** | Async generation, concurrent requests, FastAPI serving, LoRA examples | Community project recommended upstream. Current code exists, but unresolved reports include differences from native inference and LoRA/CUDA-graph problems; recent commit cadence was not independently established. [Repository](https://github.com/a710128/nanovllm-voxcpm), [issues](https://github.com/a710128/nanovllm-voxcpm/issues) |
| **vLLM-Omni** | Larger serving deployment and OpenAI-compatible speech endpoint | Actively maintained: **v0.30.0 released 2026-09-25**. Verify the exact VoxCPM/Qwen checkpoint and adapter path before adoption. [Releases](https://github.com/vllm-project/vllm-omni/releases), [VoxCPM integration](https://github.com/OpenBMB/VoxCPM) |
| **llama.cpp-omni** | Optional local CPU/Apple deployment | Available and linked upstream; conversion and feature parity require testing. [Repository](https://github.com/tc-mb/llama.cpp-omni) |

For Qwen fallback support, reuse its official **`qwen-tts-demo`** for auditioning and the documented training entry points; put the platform’s own job lifecycle around them. [Official Qwen repository](https://github.com/QwenLM/Qwen3-TTS)

**Data preparation**

| Need | Suggested building block | Practical qualification |
|---|---|---|
| Voice activity detection | [Silero VAD](https://github.com/snakers4/silero-vad) | Detect boundaries on a supported-rate working copy, retaining the original recording |
| Fast Japanese/English ASR | [faster-whisper](https://github.com/SYSTRAN/faster-whisper) | Efficient transcript generation; human correction still required |
| Word alignment and ASR pipeline | [WhisperX](https://github.com/m-bain/whisperX) | Uses language-specific alignment models; check Japanese alignment behavior |
| Alternative multilingual ASR | [Qwen3-ASR](https://github.com/QwenLM/Qwen3-ASR) | 2026 release with ASR and forced-alignment components; choose the correct task/model |
| Speaker diarization | [pyannote Community-1](https://huggingface.co/pyannote/speaker-diarization-community-1) | Initial access conditions apply; can run locally after download. Diarization is not consent verification |
| Desktop separation/cleanup | [Ultimate Vocal Remover](https://github.com/Anjok07/ultimatevocalremovergui) | Useful audition interface; check individual model licenses |
| Batch separation, including RoFormer models | [Music-Source-Separation-Training](https://github.com/ZFTurbo/Music-Source-Separation-Training) | Supports multiple architectures, including Mel-Band RoFormer; checkpoint licenses vary |
| Integrated annotation workflow | [GPT-SoVITS tools](https://github.com/RVC-Boss/GPT-SoVITS) | Its slicing, ASR and proofreading tools can be useful independently of the selected TTS model |

**Demucs should not be described as actively maintained upstream:** Meta’s repository was archived in January 2025, and its README explains the maintenance situation. Existing models may remain useful, but I would not make that repository the only cleanup dependency. [Demucs status](https://github.com/facebookresearch/demucs)

My preparation default is to leave clean studio recordings untreated. Compare cleaned and original audio before accepting denoising: preserving breaths, consonant edges, and delivery matters for this task. VoxCPM itself notes that denoising can alter voice characteristics. [Denoising guidance](https://voxcpm.readthedocs.io/en/latest/usage_guide.html)

**Platform features I recommend implementing**

These are design proposals for the binding consent requirement:

- A **voice registry** linking each speaker to signed training permission, allowed purposes, languages, distribution rights, retention terms, and revocation status.
- A recording manifest containing provenance, upload date, hashes, speaker assignment, and the applicable consent version.
- Training jobs that reject recordings without an eligible consent record.
- Private storage, authenticated access, and separate preparation, training, and inference workers.
- A model registry recording base-model revision, license, data manifest, training configuration, evaluation results, and consent dependencies.
- Revocation controls that disable affected voices and initiate the agreed deletion procedure for recordings, adapters, checkpoints, and backups.
- An audition page offering blinded comparisons and displaying the checkpoint/reference combination used.

The permitted inventory remains the author’s own voice, explicitly consenting hired actors, and original designed voices whose source terms permit the intended training. **No hololive talent stream or song recordings enter this workflow.** COVER’s published guidelines also explicitly prohibit extracting talent voices from songs for speech generation. [COVER guidelines](https://hololivepro.com/en/terms/)

## Risks and open questions

**Recent developments that a mid-2026 answer could miss**

- **IndexTTS2.5 arrived in August and adds Japanese.** Advice describing the entire Index family as Chinese/English-only is now outdated. Its official training availability still needs separate verification. [Current release](https://github.com/index-tts/index-tts)
- **AuK arrived in September with published fine-tuning code**, followed by memory reductions and additional local backends. It is worth monitoring, but its strong EN/ZH results do not establish Japanese suitability. [Release history](https://github.com/Tencent-Hunyuan/AuK)
- **Breeze-TTS-2’s August weights and strong English preference results** change the English inference landscape, but neither Japanese support nor an unrestricted commercial training platform follows from that ranking. [Project](https://github.com/breezeblue-ai/breeze-tts)
- **Qwen-Audio-3.0-TTS has a July report.** I verified the report and hosted-product documentation, but not downloadable successor weights with a speaker-training pipeline. Do not silently substitute API capabilities for Qwen3-TTS open-weight capabilities. [Report](https://arxiv.org/abs/2607.23938), [hosted model documentation](https://docs.qwencloud.com/developer-guides/speech/tts-models)
- **Fish S2.1 Pro is a newer hosted offering.** Its announcement is not evidence that the same model’s weights and training recipe are downloadable. [Fish announcement](https://fish.audio/blog/s2-1-pro-free-api/)
- **Luna-TTS’s August report is relevant**, but I did not verify a complete public weights/license/training package; it therefore does not enter the deployable shortlist. [Technical report](https://arxiv.org/abs/2608.11593)

**Other consequential pitfalls**

1. **Fine-tuning can reduce fidelity or stability.** More epochs and more recordings are not automatically improvements. Retain untuned baselines and early checkpoints. [VoxCPM training FAQ](https://voxcpm.readthedocs.io/en/latest/finetuning/faq.html)

2. **The Qwen starter trainer needs production hardening.** The inspected script lacks a full held-out evaluation loop, and its documentation contains differing example hyperparameters. Pin a revision and implement your evaluation externally. [Training README](https://github.com/QwenLM/Qwen3-TTS/blob/main/finetuning/README.md), [trainer](https://github.com/QwenLM/Qwen3-TTS/blob/main/finetuning/sft_12hz.py)

3. **License labels on older comparison charts can be wrong.** Current Fish licensing covers code as well as weights; Spark’s weights are noncommercial/share-alike despite Apache code; Higgs 3’s monetized-creator exception does not generally authorize embedding the model in a platform. [Fish terms](https://github.com/fishaudio/fish-speech/blob/main/LICENSE), [Spark weights](https://huggingface.co/SparkAudio/Spark-TTS-0.5B), [Higgs terms](https://huggingface.co/bosonai/higgs-tts-3-4b)

4. **A model can be nominally downloadable without enabling the complete local workflow.** MegaTTS3’s withheld reference encoder is the clearest example. [Official restriction](https://huggingface.co/ByteDance/MegaTTS3)

5. **“48 kHz output” does not prove better voice identity.** VoxCPM2 encodes references at 16 kHz and reconstructs 48 kHz output. Evaluate the resulting voice, rather than ranking models by output sample rate. [Architecture/data documentation](https://voxcpm.readthedocs.io/en/latest/finetuning/finetune.html)

**Open questions to settle during the pilot**

- Does the same consenting speaker have substantial Japanese **and** English recordings?
- Is the target standard Japanese, a regional dialect, or a particular bilingual accent?
- Must one checkpoint cover both languages, or may Japanese use a separate specialist?
- Is local hardware NVIDIA 12–24 GB, Apple Silicon, or CPU-only?
- Will the platform remain personal, or eventually serve others or commercial work?

My proposed first decision point is a **matched 5–10-hour audition**: VoxCPM2 LoRA, VoxCPM2 full fine-tuning, and Qwen3-TTS Base, evaluated on identical unseen Japanese and English scripts. That experiment can establish the author’s actual best model; the public benchmarks cannot yet do so.
# Research request: the best open-weight TTS to fine-tune and run locally (as of 2026-10-06)

You are GPT, researching together with Claude for novel-lab's author. Use live web search. Work read-only and answer
in English. Today is 2026-10-06; prefer sources from 2026 and give every claim a URL and a checked date.

## Context

The author is replacing ElevenLabs with a self-hosted text-to-speech stack:
- a personal web platform where they upload training audio;
- fine-tuning on rented cloud GPUs;
- text-to-speech generation from the trained voices.

They want the model that reproduces a trained voice's accent, speaking habits and intonation most faithfully when
given a large amount of audio. The languages are Japanese and English, possibly Mandarin. GPT suggested earlier that
"Qwen" may be the best; verify or refute that.

**Binding boundary.** The platform is for voices with documented consent: the author's own voice, hired voice actors
who signed a training consent, or original synthetic or designed voices. It must not clone real people without their
consent. That includes the hololive talents the project writes about: COVER's derivative-works guidelines forbid AI
training on talent voices. Do not propose training on talent stream audio. Recommend consent-recording features
where they fit.

## Questions

1. **Ranking.** Which open-weight TTS models are the state of the art as of October 2026 for fine-tuning on a single
   speaker with a lot of data (1–50+ hours), judged on each of the following?
   - speaker similarity
   - accent and prosody fidelity
   - capture of verbal habits
   - Japanese quality
   - English quality
   - naturalness
   - stability (hallucination, skipped words)
   - emotion and style control

   Consider at least, and add any newer ones you find:
   - Qwen TTS: Qwen3-TTS and any 2026 successor, including voice-design and voice-clone variants and whether fine-tuning is officially supported
   - IndexTTS2 and successors
   - CosyVoice 3 and successors
   - Fish Speech / OpenAudio S1 and successors
   - GPT-SoVITS (v4 and later), which is popular for Japanese
   - F5-TTS and E2
   - Microsoft VibeVoice
   - Higgs Audio v2
   - Chatterbox
   - MegaTTS 3
   - Spark-TTS
   - Llasa
   - Zonos
   - Orpheus
   - StyleTTS 2
   - Kokoro, which has no cloning
   - any 2026 open releases

   Separate zero-shot cloning from true fine-tuning, and say which models publish training or fine-tuning code.
2. **Primary and fallback.** For this use case (Japanese plus English, maximum fidelity, large data, cloud-GPU
   training, local inference), recommend one primary model and one fallback, and justify both with evidence: papers,
   benchmarks (SEED-TTS eval, CER/WER, SIM, MOS), credible community comparisons and known weaknesses.
3. **Licenses.** Give the license of the weights and the code for each finalist, and say what it means for personal
   and commercial use.
4. **Training recipe for the primary.**
   - data format (sample rate, segment length, transcripts, tokenizer or text normalization for Japanese);
   - minimum and recommended hours of data;
   - hyperparameters or official recipes;
   - expected training time;
   - GPU type and VRAM (for example A100 80GB, H100, L40S, RTX 4090);
   - rough cost on RunPod, Vast.ai or Modal;
   - how to evaluate overfitting and quality.
5. **Inference.** VRAM, speed (real-time factor) and streaming support; whether it runs on consumer GPUs (12–24 GB)
   or on CPU or Apple Silicon; and how emotion or style instructions are given, compared with ElevenLabs v4 inline
   tags such as [laughs] and [whispers].
6. **Platform building blocks.** Are there maintained WebUIs or servers (official or community) for the primary model
   that a platform should wrap instead of reinventing? Name and link them, and say whether they are maintained.
   Also name data-preparation tools for Japanese and English: VAD slicing, ASR with WhisperX, faster-whisper or
   Qwen ASR, speaker diarization, and denoising or separation such as Demucs, UVR or Mel-RoFormer.
7. **Risks.** Give known pitfalls and anything that changed recently (2026) that Claude's knowledge, which ends in
   mid-2026, may have missed.

## Output format

- `## Ranking`: a table with model, release date, fine-tune support, JA quality, EN quality, fidelity, license,
  training VRAM, inference VRAM and sources.
- `## Recommendation`: the primary and the fallback, with reasons.
- `## Training recipe (primary)`
- `## Inference and control`
- `## Building blocks to reuse`
- `## Risks and open questions`

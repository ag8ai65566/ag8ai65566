# ElevenLabs v4 Performance Sheet: Ninomae Ina'nis

> Source voice fields SHA-256 (Name, Dialogue Style, Catchphrases, Voice & Delivery, Audio Tags): `b5bc6aac9ecbcd753f621e5b0129c0be0cfff3e98238f7928d2ade77be1e5b8e` — reviewed 2026-10-04: Claude 2026-10-04: voice audits v1-v4 merged (research/qa/voice-audit-dispositions.md); attestation research/qa/voice-delivery.md; author decisions 2026-10-04 (quote inventory B; JP members speak Japanese)
> Built from `bible/characters/Ninomae-Inanis.md` (2026-09-30). Original designed voice matched only to
> register and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER
> Derivative Works Guidelines). Guide: `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)

The prompt's timbre, laughter and delivery details are provisional creative choices for the original voice. Performance tags throughout this sheet propose readings; they do not certify how an archived quotation sounded. Regional accents require a separate in-scope listening check.
"Perfect audio quality. Young adult woman, English speech with no prescribed regional accent, soft and calm mid-range voice,
slow unhurried pace with small pauses, gentle and warm, quiet little giggles, occasionally cracking on
excited words."
- Register basis (sample observations from the audio check, not synthesis targets): mid pitch (≈223–232 Hz in 2026 chat) and slow in chat (≈81–95 words per
  minute of speech; a 2021 game stream ran faster). [ASR I29]

## 2. Settings (untested starting choices; verify endpoint behavior)
- `eleven_v4`. Stability **60%** (API `0.60`) (calm consistency). Similarity **75%** (API `0.75`). v4 has no speed slider: slowness
  comes from the designed voice, `[unhurried]` and punctuation.

## 3. Write these habits into the script
- Hedges everywhere: "like," "I think," "you know," "I guess," "maybe," "right?"
- Micro-pauses as ellipses; tangents closed with "Anyways."
- Puns delivered flat, then a pause (new sentence), maybe a small giggle.
- Sweet-voiced threats; rarely swears.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[warm, unhurried]` → `[brighter]` | "Good morning, afternoon, evening, everyone. Could this be Tako time?" |
| Pun | `[flat, quick]` → `[short pause]` → `[small giggle]` | (the pun, then silence) |
| Chatting | `[soft, meandering]` | Style demo: "I had a point... anyways." |
| Mock-scold | `[sweet, dead calm]` | "…We don't say that in public." (about the "Forbidden WAH") |
| Teasing chat | `[sweet, dead calm]` | "I'll bonk you. With a crowbar. Don't do it." (SECONDARY transcription, answering a hair-squishing prompt) |
| Startled | `[sudden, high, voice cracks]` → `[embarrassed]` | "Tomorrow!" (SECONDARY transcription) and, separately, "Sorry, I got a little excited there." (ASR) |
| Hyped | `[excited]` | "WAH!" |
| Sincere | `[quiet, gentle]` | "Live without regrets." (SECONDARY transcription; a sincere reading is proposed) |
| Sign-off | `[warm]` | "have a wonderful rest of the morning, afternoon, evening" (ASR excerpt) |

Additional proposed scene directions from the card's Audio Tags (untested): `[soft, unhurried]`, `[calm, amused, unhurried]`, `[sly, setting up a pun]`, `[warm, punny]`, `[protective, gentle]`, `[patient, unbothered]`, `[polite Japanese, shy]`.

## 5. Signature sounds
- "WAH!": `[excited] WAH!` (sometimes a droopy one at the end: `[deflated] wah…`)
- Small giggles mid-sentence: `[small giggle]`.

## 6. Pronunciation (provisional; test)
- Ninomae Ina'nis — にのまえ いなにす (provisional, untested; surname first) · Takodachi `/tɑkoˈdɑtʃi/` ·
  WAH `/wɑː/`

## 7. Don't
- Loud, fast, or constantly shouted delivery; frequent swearing; a crack on every exclamation; an ominous
  priestess voice as default (it is an occasional bit).

## 8. Example
```
[warm, unhurried] Good morning, afternoon, evening, everyone. [brighter] Could this be Tako time?
[soft, meandering] I had a point... anyways.
[sweet, dead calm] …We don't say that in public.
```
(The "I had a point... anyways." line is a **Style demo**, not a quotation; voice audit v1.)

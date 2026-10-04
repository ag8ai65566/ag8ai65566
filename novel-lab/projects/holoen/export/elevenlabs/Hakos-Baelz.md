# ElevenLabs v4 Performance Sheet: Hakos Baelz

> Source voice fields SHA-256 (Name, Dialogue Style, Catchphrases, Voice & Delivery, Audio Tags): `732efc356f1a82151f42214200dacb57be77b1a4e2c4a26faf13eda877ece90d` — reviewed 2026-10-04: Claude 2026-10-04: voice audits v1-v4 merged (research/qa/voice-audit-dispositions.md); attestation research/qa/voice-delivery.md; author decisions 2026-10-04 (quote inventory B; JP members speak Japanese)
> Built from `bible/characters/Hakos-Baelz.md` (2026-10-02). Original designed voice matched only to
> register and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER
> Derivative Works Guidelines). Bae is active at the 2026 baseline. Guide: `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, English speech with no prescribed regional accent, bright, punchy mid-range voice; fast, loud and
run-on when telling a story; louder and higher for jokes, flat and deadpan for a dry 'bruh'; warm and sincere
when cheering someone on."
- Register and energy are creative choices for an original voice; the recording measurements in
  `research/audio-check/bae.md` are not synthesis targets. A regional accent remains unassigned pending an in-scope listening
  check; the secondary description is not a synthesis instruction.

## 2. Settings (untested starting choices; verify endpoint behavior)
- `eleven_v4`. Stability **40%** (API `0.40`) and Similarity **75%** (API `0.75`) are untested starting
  choices (she swings between loud storytelling, deadpan and warmth); Similarity refers only to the selected
  original voice.
- Pace comes from the designed voice plus `[energetic, fast]` or `[warm, sincere]`; v4 has no speed slider.

## 3. Write these habits into the script
- "like," "yeah," "okay," "oh my god," "crazy" (first-model word counts, not quotations); "senpai" for seniors
  even in English.
- Thanking gifts: rhythmic, repeated thanks ("thank you so much").
- Sign-off: "okey dokey" … "bye-bye" (two short spans both transcripts share).
- Small failures blamed on sabotage: "It was sabotage." "It's a conspiracy."
- Answering her own questions: "Who would think that's a good idea? Me."
- A flat "bruh" for absurdity; warm "You're doing great" for someone who is struggling.
- Casual swearing: "hell yeah" (shared span); milder curses are first-model observations only.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Greeting | `[loud, theatrical]` | "WAZZUP!! It's your worldwide Rat Idol --- Hakos Baelz!" (official) |
| Telling a story | `[fast, self-mocking]` | "Who would think that's a good idea? Me." |
| A small failure | `[mock outrage]` | "It was sabotage." |
| Mock scandal | `[gasps]` → `[theatrical]` | "Does she really think that me, of all people, is trying to clout chase by using her?" |
| Absurdity | `[deadpan]` | "Bruh." (shared ASR span) |
| Thanking gifts | `[quick, warm]` | "Welcome to the Rat Pack, welcome, welcome." |
| Cheering someone | `[warm, sincere]` | "Everything gets better. If you're at the bottom, you can only go up. You're doing great." |
| Horror game | `[panicked]` | "I don't like this. I wanna leave." (wiki, secondary) |

With people (provisional): IRyS `[bickering, affectionate]`; Kronii `[teasing]`; Calli and IRyS on CHADCast
`[loud, chaotic]`; Bijou `[playful]`.

## 5. Signature sounds
- "Bruh." (spoken, deadpan).
- `[laughs]`, `[gasps]` (tag only; proposed performance choices, not listening observations).

## 6. Pronunciation
- Untested: listen to how the chosen voice says "Baelz," "Hakos," "Bae" and "Febaerary" and adjust the spelling
  in the script if needed. No phonetic guide is given until a listening check exists.

## 7. Don't
- A slow, sleepy or breathy default; cruelty; a villain voice outside a clear bit; an accent caricature; a
  laugh after every line.

## 8. Example
```
[loud, theatrical] WAZZUP!! It's your worldwide Rat Idol!
[mock outrage] It was sabotage.
[fast, self-mocking] Who would think that's a good idea? Me.
[deadpan] Bruh.
[warm, sincere] Everything gets better. If you're at the bottom, you can only go up. You're doing great.
```
(Line 1 is a shortened official greeting; line 4 is a wiki-listed word; the rest are her lines, quoted only
where both transcripts agree. The delivery tags are proposed performance directions.)

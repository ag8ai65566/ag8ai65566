# ElevenLabs v4 Performance Sheet: Ouro Kronii

> Built from `bible/characters/Ouro-Kronii.md` (2026-09-30). The voice is an **original designed voice**
> matched only to register and energy. Do not clone or imitate the member's real voice (ElevenLabs Use
> Policy §5; COVER Derivative Works Guidelines). The directions below preserve documented wording and propose
> comic timing for an original voice; they do not aim to reproduce her identifiable vocal delivery. Guide: `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)

The prompt's timbre, laughter and delivery details are provisional creative choices for the original voice. Performance tags throughout this sheet propose readings; they do not certify how an archived quotation sounded. Regional accents require a separate in-scope listening check.
"Perfect audio quality. Young adult woman, English speech with no prescribed regional accent, low alto speaking voice, dry and
deadpan, relaxed medium pace, controlled and a little smoky, capable of a sudden high startled squawk and
of breaking into laughter."
- Register basis (sample observations from the audio check, not synthesis targets): low (median ≈177–188 Hz in chat)
  at a medium pace (≈120–127 words per minute of speech). [ASR K36]

## 2. Settings (starting points; adjust by ear)
- Model `eleven_v4`. Stability **55%** (API `0.55`) (deadpan needs consistency; drop to 45% for horror scenes). Similarity **75%** (API `0.75`).

## 3. Write these habits into the script
- Short, plain statements; understatement over exclamation. Self-praise stated as fact ("It's me, perfection.").
- A beat before a punchline: use an ellipsis or a new sentence, not an exclamation mark.
- Owns mistakes out loud: "Okay, that was my bad." / "that's on me."
- Swears when startled or frustrated, written as-is ("what the fuck").
- ASR establishes the cheers "Yay!" and "Yippee!"; a brief, lightly cheerful reading is a provisional option, not a verified flat or ironic default.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[relaxed]` | Style demo: "Hello. Kroniichiwa! Yay!" |
| Bragging | `[deadpan, flat, slow]` | "It's me, perfection." |
| Jump scare | `[startled squawk]` → `[trying to stay calm]` | "GWAK! …I was observing. Loudly." (second line: Style demo) |
| Misplay | `[dry]` | "Okay, that was my bad." |
| Frustrated | `[irritated, short]` | "No. No— what the fuck was that?" (Style demo) |
| Praised | `[deadpan]` / `[flustered, quick]` | "I know." |
| Self-roast | `[dry, amused]` | "I'm so funny. I can't read this." |
| Scared, narrated | `[low, uneasy]` | "Oh my god, that hand scared me." |
| Sincere | `[plain, warm, unhurried]` | (no joke attached) |
| Good night | `[softer]` | "KroYasumi~" |

## 5. Signature sounds
- GWAK: `[startled squawk] GWAK!` (the squawk is sharp and higher than her voice; if the tag fails, try `[sudden bird-like shriek]`).
- Explosive noises when hit in games: `[yelps]`, `[grunts]`.

## 6. Pronunciation (provisional; test with your voice)
- Ouro Kronii `/ˈoʊɹoʊ ˈkɹoʊni/` · Kroniichiwa `/ˌkɹoʊniˈtʃiːwɑ/` · Kronies `/ˈkɹoʊniz/` · GWAK `/ɡwɑk/`

## 7. Don't
- `[giggles]`, `[bubbly]`, `[cheerful]` as a default; breathy seduction as her normal voice; elaborate
  time metaphors in every line; a flawless dominator who never slips.

## 8. Example (assembled performance exercise)

These are separately sourced components arranged for performance, not a recorded exchange. The opening is a Style
demo using the secondary greeting form; self-introduction and GWAK are secondary-recorded components. The misplay
and frightened-hand sentences are independent ASR excerpts. All tags are proposed.
```
[relaxed] Hello. Kroniichiwa! [lightly cheerful] Yay.
[deadpan] It's me, perfection. [short pause] …Okay, that was my bad.
[startled squawk] GWAK! [trying to stay calm] Oh my god, that hand scared me.
```

# ElevenLabs v4 Performance Sheet: Nakiri Ayame

> Built from `bible/characters/Nakiri-Ayame.md` (2026-10-02). Original designed voice matched only to register
> and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Ayame is active at the 2026 baseline. She streams in Japanese; lines below are romanized with
> English glosses, and the voice works for Japanese, English or Chinese dialogue. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice; provisional design choices)
"Perfect audio quality. Young woman, soft and cute mid-high voice with a playful, mock-haughty edge; chatty and
unhurried, dissolving into quick giggles; shaky and breathless when frightened."
- Giggles are a provisional performance choice (secondary description), not a listening observation.
- This is an original voice-design choice. Mixed-recording F0 and ASR character-rate measurements are
  descriptive research data, not synthesis targets or evidence of the member's isolated vocal range.

## 2. Settings (untested starting choices; verify endpoint behavior)
- `eleven_v4`. Stability **40%** (API `0.40`) (giggles and mood swings). Similarity **75%** (API `0.75`).
- Pace comes from the designed voice plus `[playful, warm]` or `[scared, shaky]`; v4 has no speed slider.

## 3. Write these habits into the script
- "Yo" (余) for "I" and "ningen-sama" for her viewers; "Konnakiri!" and "Yo da yo!" (secondary transcription; not audio-verified).
- Polite at first ("Kikoete orimasu deshō ka?"), casual within minutes ("maji de," "meccha").
- Pouting scolds: "Urusai!"; separately, "Komatta hitotachi." (two ASR excerpts, not one spoken turn).
- In horror: "Koe ga furuechau," "Ochitsuite, ochitsuite."

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Greeting | `[bright, playful]` | "Konnakiri!" (secondary transcription) |
| The oni act | `[mock-haughty]` | "Yo da yo!" (secondary transcription; not verified by the two-model audio check) |
| Opening a stream | `[polite, careful]` | "Kikoete orimasu deshō ka?" |
| Teasing chat | `[pouting]` | "Urusai!" (ASR); separately, "Komatta hitotachi." (ASR) |
| Horror game | `[scared, shaky]` | "Ima odorokasaretara hontō ni shinzō ga tomarisō." |
| FPS clutch | `[focused, quick]` | **Style demo:** "Mikata, ikeru yo!" ("Team, we can do this!") |
| A bad pun | `[giggles]` → `[laughs harder]` | (tag only) |

With people (proposed scene directions, not observed conversational defaults): Fubuki and Mio `[comfortable, giggly]`;
Okayu `[teasing]`; Kiara `[polite, excited]`.

Additional proposed scene directions from the card's Audio Tags (untested): `[shy, careful]`.

## 5. Signature sounds
- `[giggles]` (tag only); **Style demo:** "Mō~" (spoken).

## 6. Pronunciation (provisional; test)
- Japanese reading: なきり あやめ; こんなきり; 余＝よ. Regional accent and pitch-accent patterns are unverified.
  Listen to how the chosen voice says them and adjust.

## 7. Don't
- A cruel or menacing oni; a cold, superior read; a monotone.

## 8. Example
```
[polite, careful] Kikoete orimasu deshō ka?
[bright, playful] Konnakiri!
[pouting] Urusai!
[pouting] Komatta hitotachi.
[scared, shaky] Koe ga furuechau.
[scared, shaky] Ima odorokasaretara hontō ni shinzō ga tomarisō.
```
(Line 2 is her greeting as a secondary transcription. Lines 1 and 3–6 are separate shared ASR excerpts, not one
conversation. Their delivery tags are proposed performance directions, not listening findings.)

# ElevenLabs v4 Performance Sheet: AZKi

> Built from `bible/characters/AZKi.md` (2026-10-02). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). AZKi is active at the 2026 baseline. She streams in Japanese; lines below are romanized with
> English glosses, and the voice works for Japanese, English or Chinese dialogue. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice; provisional design choices)
"Perfect audio quality. Young woman, clear and warm mid-range singer's voice; poised
and friendly when she talks, a playful lilt for jokes, a bright shout of triumph when she wins a guessing game."
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.

## 2. Settings (starting points)
- `eleven_v4`. Stability **50%** (API `0.50`) (poised delivery with occasional bursts; an untested starting choice).
  Similarity **75%** (API `0.75`).
- Pace comes from the designed voice plus `[warm, clear]` or `[focused, quick]`; v4 has no speed slider.

## 3. Write these habits into the script
- A soft "hai" to close a topic; a drawn-out "e~?" when surprised; "chotto chotto" when flustered.
- Grand narration of her own losses: "Senryakuteki tettai" ("strategic retreat").
- 「ゲース！」 ("Gēsu!") when locking in an answer; "Yuka!" / "Tenjō!" ("Floor!" / "Ceiling!") for strong feelings.
- Puns and mock-villain flourishes; a following giggle is an optional, provisional performance choice.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Introduction | `[poised, diva]` | "I'm the Virtual Diva AZKi! I love music and singing!" (official) |
| Chat knows too much (debut parody) | `[mock-flustered]` | "Chotto chotto, naande sonna minna jōhō o motteru no?" |
| Mock villain (debut parody) | `[mock-menacing]` (a following `[giggles]` is optional and provisional) | "Kono mojisū ni kyōfu suru ga ii." |
| Losing a fight | `[mock-dignified]` | "Senryakuteki tettai." |
| A shop price | `[indignant, playful]` | "Bottakuri!" |
| Overwhelmed | `[overjoyed]` | "Yuka!" (official word) |

With people (proposed scene directions, not observed conversational defaults): Suisei `[relaxed, teasing]`;
FUWAMOCO `[cheerful]`; IRyS `[friendly]`.

## 5. Signature sounds
- `[giggles]` (tag only; a provisional performance choice); "e~?" (spoken).

## 6. Pronunciation (provisional; test)
- Reading guide (untested): あずき; かいたくしゃ. Listen to how the chosen voice says them and adjust.

## 7. Don't
- A cold, aloof diva; constant shouting; a babyish voice.

## 8. Example
```
[poised, diva] Bācharu dībā AZKi, kasō sekai no utahime desu.
[mock-flustered] Chotto chotto, naande sonna minna jōhō o motteru no?
[mock-menacing] Kono mojisū ni kyōfu suru ga ii.
[mock-dignified] Senryakuteki tettai.
[overjoyed] Yuka!
```
(Line 5 is official profile wording. Lines 1–3 are shared ASR excerpts from her April Fools 2026 debut parody; line 4 is a shared ASR excerpt from a game. These are separate examples. Their delivery tags are proposed performance directions, not listening findings.)

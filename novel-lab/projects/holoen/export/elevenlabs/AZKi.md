# ElevenLabs v4 Performance Sheet: AZKi

> Built from `bible/characters/AZKi.md` (2026-10-02). Original designed voice matched only to register and
> energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). AZKi is active at the 2026 baseline. She streams in Japanese; lines below are romanized with
> English glosses, and the voice works for Japanese, English or Chinese dialogue. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, clear and warm mid-range singer's voice with careful diction; measured
and friendly when she talks, a playful lilt for jokes, a bright shout of triumph when she wins a guessing game."
- Register basis: a 2026 RPG window measured about 244 Hz median (`research/audio-check/azki.md`); her April
  Fools "new VTuber" act ran much higher, so do not design from it.

## 2. Settings (starting points)
- `eleven_v4`. Stability **50%** (API `0.50`) (measured, poised delivery with occasional bursts).
  Similarity **75%** (API `0.75`).
- Pace comes from the designed voice plus `[warm, clear]` or `[focused, quick]`; v4 has no speed slider.

## 3. Write these habits into the script
- A soft "hai" to close a topic; a drawn-out "e~?" when surprised; "chotto chotto" when flustered.
- Grand narration of her own losses: "Senryakuteki tettai" ("strategic retreat").
- "Guess!" when locking in an answer; "Yuka!" / "Tenjō!" ("Floor!" / "Ceiling!") for strong feelings.
- Puns and mock-villain flourishes, then a giggle.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Introduction | `[poised, diva]` | "I'm the Virtual Diva AZKi! I love music and singing!" (official) |
| Chat knows too much | `[mock-flustered]` | "Chotto chotto, naande sonna minna jōhō o motteru no?" |
| Mock villain | `[mock-menacing]` → `[giggles]` | "Kono mojisū ni kyōfu suru ga ii." |
| Losing a fight | `[mock-dignified]` | "Senryakuteki tettai." |
| A shop price | `[indignant, playful]` | "Bottakuri!" |
| Overwhelmed | `[overjoyed]` | "Yuka!" (official word) |

With people (provisional): Suisei `[relaxed, teasing]`; FUWAMOCO `[cheerful, big-sister]`; IRyS `[friendly]`.

## 5. Signature sounds
- `[giggles]` (tag only); "e~?" (spoken).

## 6. Pronunciation (provisional; test)
- AZKi `/ˈɑzuki/` ("ah-zoo-kee") · Kaitakusha `/kaɪˈtɑkuʃɑ/`

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
(Line 5 is her official word; lines 1–4 are her lines, quoted only where both transcripts agree.)

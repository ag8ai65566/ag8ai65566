# ElevenLabs v4 Performance Sheet: Hoshimachi Suisei

> Built from `bible/characters/Hoshimachi-Suisei.md` (2026-10-02). Original designed voice matched only to
> register and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER
> Derivative Works Guidelines). Suisei is active at the 2026 baseline. She streams in Japanese; lines below are
> romanized with English glosses, and the voice works for Japanese, English or Chinese dialogue. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice; provisional design choices)
"Perfect audio quality. Young woman, clear and bright mid-high voice, polished and confident; quick and fluent
when chatting, sing-song and stretched when she calls herself cute, crisp and clipped when competing."
- A bright laugh is a provisional performance choice, not a listening observation.
- The original voice's register is an independent design choice; mixed-recording pitch estimates are not synthesis targets.

## 2. Settings (starting points)
- `eleven_v4`. Stability **45%** (API `0.45`) (polished by default, playful swings for the signature line).
  Similarity **75%** (API `0.75`).
- Pace comes from the designed voice plus `[quick, enthusiastic]` or `[focused, clipped]`; v4 has no speed
  slider.

## 3. Write these habits into the script
- Third person for herself: "Sui-chan"; the stretched signature "Sui-chan wa~ kyō mo kawaii~."
- Quick "e?" reactions; "chotto matte" ("wait a sec"); fillers "nanka," "mā," "ne."
- Mock innocence when caught: "Iya iya iya, watashi wa warukunai." Separately, a mock-rough "Ore wa warukunē." (two ASR excerpts nine seconds apart, not one spoken turn).
- Occasional short English ("Hi, honey!", a secondary transcription associated with her Duolingo stream).

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Introduction | `[polished, idol-bright]` | "A shooting star that appeared from diamonds in the rough; I'm the virtual idol Hoshimachi Suisei!" (official) |
| Signature line | `[sing-song, playful]` | "Sui-chan wa~ kyō mo kawaii~" |
| Caught in a mistake | `[mock-innocent]` → `[mock-gruff]` | Separate ASR excerpts, not one spoken turn: "Iya iya iya, watashi wa warukunai." (00:05:39); "Ore wa warukunē." (00:05:48). |
| Age joke | `[breezy, firm]` | "Sui-chan wa jūhassai da yo." |
| Tales tangent | `[quick, enthusiastic]` | "Kore wa Teiruzu ga daisuki na hanashi desu." |
| Competitive game | `[focused, clipped]` | "Mō ikkai. Kondo wa kateru." (style demo) |

With people (proposed scene directions, not observed conversational defaults): Calli `[gracious, amused]`; AZKi `[relaxed, teasing]`; Miko `[playful bickering]`.

## 5. Signature sounds
- `[laughs]` (tag only); "e?" (spoken).

## 6. Pronunciation (provisional; test)
- Reading guide (untested): ほしまち すいせい; すいちゃん; ほしよみ. Listen to how the chosen voice says them and adjust.

## 7. Don't
- A breathy or babyish idol voice; a cold, menacing read (the "psychopath" bit is a joke); mumbling.

## 8. Example
```
[polished, idol-bright] Bācharu aidoru no Hoshimachi Suisei desu!
[sing-song, playful] Sui-chan wa~ kyō mo kawaii~
[mock-innocent] Iya iya iya, watashi wa warukunai.
[breezy, firm] Sui-chan wa jūhassai da yo.
[focused, clipped] Mō ikkai. Kondo wa kateru.
```
(Line 1 is built on her official introduction; line 5 is a style demo; lines 2–4 are her lines, quoted only
where both transcripts agree.)

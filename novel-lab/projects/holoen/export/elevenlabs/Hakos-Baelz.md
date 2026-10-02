# ElevenLabs v4 Performance Sheet: Hakos Baelz

> Built from `bible/characters/Hakos-Baelz.md` (2026-10-02). Original designed voice matched only to
> register and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER
> Derivative Works Guidelines). Bae is active at the 2026 baseline. Guide: `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, Australian accent, bright, punchy mid-range voice; fast, loud and
run-on when telling a story; louder and higher for jokes, flat and deadpan for a dry 'bruh'; warm and sincere
when cheering someone on."
- Register basis: 2026 chat windows measured lower than most of her kouhai (window medians about 200–233 Hz;
  `research/audio-check/bae.md`). Keep the accent natural, never a caricature.

## 2. Settings (starting points)
- `eleven_v4`. Stability **40%** (API `0.40`) (she swings between loud storytelling, deadpan and warmth).
  Similarity **75%** (API `0.75`).
- Pace comes from the designed voice plus `[energetic, fast]` or `[warm, sincere]`; v4 has no speed slider.

## 3. Write these habits into the script
- "like," "yeah," "okay," "oh my god," "That's crazy"; "senpai" for seniors even in English.
- Thanking gifts: "thank you so much" plus "boom, boom, boom."
- Small failures blamed on sabotage: "It was sabotage." "It's a conspiracy."
- Answering her own questions: "Who would think that's a good idea? Me."
- A flat "bruh" for absurdity; warm "You're doing great" for someone who is struggling.
- Casual swearing ("damn," "God damn it," "hell yeah").

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Greeting | `[loud, theatrical]` | "WAZZUP!! It's your worldwide Rat Idol --- Hakos Baelz!" (official) |
| Telling a story | `[fast, self-mocking]` | "Who would think that's a good idea? Me." |
| A small failure | `[mock outrage]` | "It was sabotage." |
| Mock scandal | `[gasps]` → `[theatrical]` | "Does she really think that me, of all people, is trying to clout chase by using her?" |
| Absurdity | `[deadpan]` | "Bruh." (wiki, secondary) |
| Thanking gifts | `[quick, warm]` | "Welcome to the Rat Pack, welcome, welcome." |
| Cheering someone | `[warm, sincere]` | "Everything gets better. If you're at the bottom, you can only go up. You're doing great." |
| Horror game | `[panicked]` | "I don't like this. I wanna leave." (wiki, secondary) |

With people (provisional): IRyS `[bickering, affectionate]`; Kronii `[teasing]`; Calli and IRyS on CHADCast
`[loud, chaotic]`; Bijou `[playful]`.

## 5. Signature sounds
- "boom, boom, boom" (spoken, while thanking).
- `[laughs]`, `[gasps]` (tag only).

## 6. Pronunciation (provisional; test)
- Baelz `/bɛlz/` ("bells"; many members say `/beɪlz/`) · Hakos `/ˈheɪkɒs/` ("hake-oss") · Bae `/beɪ/` ·
  Febaerary `/ˈfɛbeɪˌɛɹi/` (unverified)

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
(Line 1 is a style demo built on her official greeting; line 4 is a wiki-listed word; the rest are her lines,
quoted only where both transcripts agree.)

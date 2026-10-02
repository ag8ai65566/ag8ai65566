# ElevenLabs v4 Performance Sheet: Nekomata Okayu

> Built from `bible/characters/Nekomata-Okayu.md` (2026-10-02). Original designed voice matched only to register
> and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Okayu is active at the 2026 baseline. She streams in Japanese; lines below are romanized with
> English glosses, and the voice works for Japanese, English or Chinese dialogue. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, soft, relaxed, boyish voice that sits low; lazy and warm, unhurried with
trailing vowels, a playful low purr when teasing, a laugh that climbs high."
- Register basis: 2026 game windows measured about 261–262 Hz window medians with a low floor (p10 about
  131–155 Hz) (`research/audio-check/okayu.md`). "Low" is a style choice; keep it natural.

## 2. Settings (starting points)
- `eleven_v4`. Stability **50%** (API `0.50`) (relaxed and steady). Similarity **75%** (API `0.75`).
- Pace comes from the designed voice plus `[relaxed, low]` or `[playful, low purr]`; v4 has no speed slider.

## 3. Write these habits into the script
- "Boku" for "I"; "Mogu mogu~ Okayu~!" to greet; "Onigiryā" for her fans.
- "Nori de" (by vibes); "Rettsura gō!"; a pleased "nya nya nya".
- Narrating her own play in long, relaxed sentences; agreeing with everyone.
- Flirty teasing kept light and non-explicit.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Greeting | `[lazy, warm]` | "Mogu mogu~ Okayu~!" (official) |
| Starting a game | `[breezy]` | "Hai, nori de aite o buttaoshitai to omoimāsu." |
| Exploring a new game | `[contented, chatty]` | "Atarashii gēmu dakara, minna to issho ni tesaguri tansaku na no tanoshii nā." |
| A move that feels good | `[pleased]` | "Nya nya nya nya." |
| Teasing a member | `[playful, low purr]` | "Kawaii nē." (style demo) |
| Laughing hard | `[laughs harder]` | (tag only) |

With people (provisional): Korone `[comfortable, fond]`; Ina `[mellow]`; FUWAMOCO `[fond senpai, teasing]`.

## 5. Signature sounds
- "mogu mogu" (spoken); "nya nya nya" (spoken); `[laughs]` (tag only).

## 6. Pronunciation (provisional; test)
- Nekomata Okayu `/nɛkoʊˈmɑtɑ oʊˈkɑju/` · Onigiryā `/oʊniˈɡiɾjɑː/`

## 7. Don't
- A high, sugary voice; harsh or aggressive delivery; explicit flirting.

## 8. Example
```
[lazy, warm] Mogu mogu~ Okayu~!
[breezy] Hai, nori de aite o buttaoshitai to omoimāsu.
[contented, chatty] Atarashii gēmu dakara, minna to issho ni tesaguri tansaku na no tanoshii nā.
[pleased] Nya nya nya nya.
[playful, low purr] Kawaii nē.
```
(Line 1 is her official greeting; line 5 is a style demo; lines 2–4 are her lines, quoted only where both
transcripts agree.)

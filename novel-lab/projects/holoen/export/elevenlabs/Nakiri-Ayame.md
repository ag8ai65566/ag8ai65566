# ElevenLabs v4 Performance Sheet: Nakiri Ayame

> Built from `bible/characters/Nakiri-Ayame.md` (2026-10-02). Original designed voice matched only to register
> and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Ayame is active at the 2026 baseline. She streams in Japanese; lines below are romanized with
> English glosses, and the voice works for Japanese, English or Chinese dialogue. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, soft and cute mid-high voice with a playful, mock-haughty edge; chatty and
unhurried, dissolving into quick giggles; shaky and breathless when frightened."
- Register basis: 2026 chat windows measured about 244–263 Hz window medians, higher when scared
  (`research/audio-check/ayame.md`).

## 2. Settings (starting points)
- `eleven_v4`. Stability **40%** (API `0.40`) (giggles and mood swings). Similarity **75%** (API `0.75`).
- Pace comes from the designed voice plus `[playful, warm]` or `[scared, shaky]`; v4 has no speed slider.

## 3. Write these habits into the script
- "Yo" (余) for "I" and "ningen-sama" for her viewers; "Konnakiri!" and "Yo da yo!".
- Polite at first ("Kikoete orimasu deshō ka?"), casual within minutes ("maji de," "meccha").
- Pouting scolds: "Urusai!" … "Komatta hitotachi."
- In horror: "Koe ga furuechau," "Ochitsuite, ochitsuite."

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Greeting | `[bright, playful]` | "Konnakiri!" |
| The oni act | `[mock-haughty]` | "Yo da yo!" |
| Opening a stream | `[polite, careful]` | "Kikoete orimasu deshō ka?" |
| Teasing chat | `[pouting]` | "Urusai!" … "Komatta hitotachi." |
| Horror game | `[scared, shaky]` | "Ima odorokasaretara hontō ni shinzō ga tomarisō." |
| A bad pun | `[giggles]` → `[laughs harder]` | (tag only) |

With people (provisional): Fubuki and Mio `[comfortable, giggly]`; Okayu `[teasing]`; Kiara `[polite, excited]`.

## 5. Signature sounds
- `[giggles]` (tag only); "Mō~" (spoken).

## 6. Pronunciation (provisional; test)
- Nakiri Ayame `/nɑˈkiɾi ɑˈjɑmeɪ/` · Konnakiri `/kɔnːɑˈkiɾi/` · Yo (余) `/joʊ/`

## 7. Don't
- A cruel or menacing oni; a cold, superior read; a monotone.

## 8. Example
```
[polite, careful] Kikoete orimasu deshō ka?
[bright, playful] Konnakiri!
[pouting] Urusai! … Komatta hitotachi.
[scared, shaky] Koe ga furuechau.
[scared, shaky] Ima odorokasaretara hontō ni shinzō ga tomarisō.
```
(Line 2 is her greeting from the wiki; lines 1, 3–5 are her lines, quoted only where both transcripts agree.)

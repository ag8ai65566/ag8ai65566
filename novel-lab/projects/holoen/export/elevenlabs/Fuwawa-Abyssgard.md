# ElevenLabs v4 Performance Sheet: Fuwawa Abyssgard

> Built from `bible/characters/Fuwawa-Abyssgard.md` (promoted 2026-10-01). Original designed voice matched
> only to register and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5;
> COVER Derivative Works Guidelines). Fuwawa is active at the 2026 baseline; she shares the FUWAMOCO channel
> with Mococo (world card "FUWAMOCO"). Guide: `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice; provisional design choices)
"Perfect audio quality. Young woman, English-speaking, very high, soft, sweet, fluffy voice; gentle
and a little airy; unhurried and chatty; bounces up, bouncy and boisterous, when excited; turns mock-stern
when teasing."
- Register basis: qualitative only. Her solo-stream numbers include game audio and are kept in
  `research/audio-check/fuwamoco.md`, not used as targets.
- Design her voice as clearly distinct from Mococo's (see §7): softer and airier, where Mococo is brighter
  and squeakier.

## 2. Settings (starting points)
- `eleven_v4`. Stability **50%** (API `0.50`) (soft and steady by default). Similarity **75%** (API `0.75`).
- Pace comes from the designed voice plus `[gentle, chatty]` or `[rapid, flustered]`; v4 has no speed slider.

## 3. Write these habits into the script
- "okay," tag questions ("…right?"), "maybe," "you know," "hmm," "in you go," "oh my gosh."
- Strings of "no, no, no, no" when things go wrong.
- Narrates what she is doing and asks herself and chat questions as she goes.
- "Moco-chan" for her sister, always; "Ruffians" for fans; "bau bau" for nearly anything.
- Confident nonsense words ("Refridgator!") delivered with total certainty.
- Teasing Mococo is sweet and mock-evil, never cold. No swearing or crude jokes.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Introduction | `[bright, sing-song]` | "I'm not a chihuahua, I'm Fuwawa!" (wiki, secondary) |
| Chatting | `[gentle, chatty]` | (style demo) "Okay, so we go this way, right? Maybe?" |
| Sneaking | `[whispering, polite]` | "Hello, ma'am. Nice day, ma'am." |
| Second-guessing | `[nervous, giggly]` | "Should I run? Is running suspicious?" |
| Wanting something | `[pleading, cute]` | "Can I have one? I like one. Can I have one?" |
| Confident nonsense | `[proud, certain]` | "Refridgator!" (wiki, secondary) |
| Teasing Mococo | `[sweetly mischievous]` | (style demo) "Moco-chan, are you sure? Hmm?" |
| Panicking | `[rapid, flustered]` | "No, no, no, no!" |
| Cheering someone on | `[warm, encouraging]` | "…go to the gym and be the main character of the gym." |
| Sign-off | `[warm, cheerful]` | "It was a lot of fun!" |

With people (provisional): Mococo `[doting, teasing]`; Nerissa `[playful]` ("Newissa"); Marine `[starstruck]`.

## 5. Signature sounds
- `[cheerful] bau bau!` (spoken).

## 6. Pronunciation (provisional; test)
- Fuwawa `フワワ (provisional kana guide; untested)` · Abyssgard `/ˈæbɪsɡɑɹd/` ("AB-iss-gard") · bau `/baʊ/` · Ruffians `/ˈɹʌfiənz/`; she
  sometimes softens the R ("Wuffians"), so write "Wuffians" only where you want it.

## 7. Don't
- A low or husky voice; brisk, crisp efficiency; swearing or crude jokes; a genuinely cold "evil twin."
- Never merge the twins: in a FUWAMOCO scene each line belongs to one twin unless they speak in sync, and
  then give both voices the same line.

## 8. Example
```
[bright, sing-song] I'm not a chihuahua, I'm Fuwawa!
[whispering, polite] Hello, ma'am. Nice day, ma'am.
[nervous, giggly] Should I run? Is running suspicious?
[warm, encouraging] So go do that, go to the gym and be the main character of the gym.
[warm, cheerful] It was a lot of fun!
[playful] Bau bau!
```
(Line 1 uses the wiki's secondary transcription of her introduction; it is not audio-verified; the closing "Bau bau!" line
is a style demo; the rest are her lines, quoted only where both transcripts agree.)

# ElevenLabs v4 Performance Sheet: Shiori Novella

> Built from `bible/characters/Shiori-Novella.md` (promoted 2026-10-01). Original designed voice matched only
> to register and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER
> Derivative Works Guidelines). Shiori is active at the 2026 baseline. Guide: `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, neutral American accent, clear, mid-high, chatty voice; fast and bubbly
when excited, piling reactions on top of each other; drops into a flat, deadpan aside for jokes; a playful,
teasing lilt; can let out a piercing horror-movie scream."
- Register basis: qualitative only. The sampled recordings mix in trailer narrators, game dialogue and co-op
  players, so their numbers are not used as targets here (see `research/audio-check/shiori.md`).

## 2. Settings (starting points)
- `eleven_v4`. Stability **40%** (API `0.40`) (fast swings between excitement and deadpan). Similarity **75%** (API `0.75`).
- Pace comes from the designed voice plus `[rapid, excited]` or `[deadpan]`; v4 has no speed slider.

## 3. Write these habits into the script
- Hedges and fillers: "like," "actually," "kind of," "sort of," "genuinely," "if that makes sense."
- She talks to "guys," rarely "chat."
- Restarts mid-thought and stacks reactions ("This looks like a movie! I genuinely like the look of this!").
- Lore defenses opened with "In my defense…" or "For the record…"; the menace is always a joke.
- Exclamations: "oh my god," "oh heavens," "oh shoot," "Oh nyo…"
- Profanity is situational and can include strong words; when she snaps at someone, a quick apology can
  follow that one exchange. It is not her default, and not every frustrated line gets an apology.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[bright, quick]` | "Shiori~n! Shiori Novella here at your service!" (official) |
| Excited commentary | `[rapid, excited]` | "This looks like a movie! I genuinely like the look of this!" |
| Lore defense | `[deadpan, mock-innocent]` | "For the record, I did not sacrifice anyone." |
| Thirst bit | `[teasing, goofy]` | "Whoa, wait, who is that hot thing? Is that a vampire?" |
| Tangent | `[rambling, amused]` | (style demo) "Okay, so, actually, wait, that's kind of a whole thing…" |
| Horror | `[nervous, quiet]` → `[screams]` | "I would be too scared to play this myself." |
| Comforting | `[gentle, warm]` | "Aw, it's okay! There, there!" |
| Cheering someone | `[warm, delighted]` | "Your Blender skills are so cool. I'm so happy for you." |
| Annoyed | `[snappy]` → `[apologetic, quick]` | "I'm so sorry. I shouldn't say that." |
| Sign-off | `[warm, quick]` | "Alright, bye guys! See you later!" |

With people (provisional): Nerissa `[teasing, playing hard to get]`; Bijou `[amused, big-sister]`;
FUWAMOCO `[playful]`; Calli `[dry, conspiratorial]`.

## 5. Signature sounds
- `[ear-piercing scream]` (tag only; don't also spell it out).
- `[intrigued] ooooh` and `[startled] whoa` (spoken).

## 6. Pronunciation (provisional; test)
- Shiori `/ʃiˈoʊɹi/` · Novella `/noʊˈvɛlə/` · Novelites `/ˈnɑvəliːts/` ("novel-eets") · Yorick `/ˈjɔɹɪk/`

## 7. Don't
- A slow, ominous villain voice as the default (her menace is a joke); prim or formal speech; constant
  swearing; a whispery, seductive read of the thirst bits (keep them goofy).

## 8. Example
```
[bright, quick] Shiori~n! Shiori Novella here at your service!
[rapid, excited] Okay guys, this looks like a movie! I genuinely like the look of this!
[deadpan, mock-innocent] For the record, I did not sacrifice anyone.
[nervous, quiet] I would be too scared to play this myself. [screams]
[warm, quick] Alright, bye guys! See you later!
```
(Line 1 is her official greeting; "Okay guys," in line 2 is a style demo; the rest are her lines, quoted only
where both transcripts agree.)

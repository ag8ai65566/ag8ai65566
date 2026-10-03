# ElevenLabs v4 Performance Sheet: Shiori Novella

> Built from `bible/characters/Shiori-Novella.md` (promoted 2026-10-01). Original designed voice matched only
> to register and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER
> Derivative Works Guidelines). Shiori is active at the 2026 baseline. Guide: `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice; provisional design choices)
"Perfect audio quality. Young woman, English-speaking, clear, mid-high, chatty voice; fast and bubbly
when excited, piling reactions on top of each other; drops into a flat, deadpan aside for jokes; a playful,
teasing lilt; can let out a piercing horror-movie scream."
- Register basis: qualitative only. The sampled recordings mix in trailer narrators, game dialogue and co-op
  players, so their numbers are not used as targets here (see `research/audio-check/shiori.md`).

## 2. Settings (untested audition choices; verify endpoint behavior)
- `eleven_v4`. Stability **40%** (API `0.40`) (fast swings between excitement and deadpan). Similarity **75%** (API `0.75`).
- Pace comes from the designed voice plus `[rapid, excited]` or `[deadpan]`; v4 has no speed slider.

## 3. Write these habits into the script
- Hedges and fillers: "like," "actually," "kind of," "sort of," "genuinely," "if that makes sense."
- She talks to "guys," rarely "chat."
- Restarts mid-thought and stacks reactions ("This looks like a movie! I genuinely like the look of this!").
- Lore defenses opened with "In my defense…" or "For the record…"; the menace is always a joke.
- Exclamations: "oh my god," "oh heavens," "oh shoot," "Oh nyo…" (secondary transcription)
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
| Horror-trailer commentary | `[nervous, quiet]` | "I would be too scared to play this myself." |
| Comforting | `[gentle, warm]` | "Aw, it's okay! There, there!" (secondary transcription) |
| Cheering someone | `[warm, delighted]` | "Your Blender skills are so cool. I'm so happy for you." |
| Annoyed | `[snappy]` → `[apologetic, quick]` | "Go fuck yourself. I'm so sorry. I shouldn't say that." (ASR shared span from one moderation exchange; delivery tags are proposed) |
| Sign-off | `[warm, quick]` | "Alright, bye guys! See you later!" |

With people (proposed scene directions, not observed defaults or relationship claims): Nerissa `[teasing, mock-evasive]` for an explicitly scripted public-persona joke; Bijou `[amused, big-sister]`;
FUWAMOCO `[playful]`; Calli `[dry, conspiratorial]`.

Additional proposed scene directions from the card's Audio Tags (untested): `[bright, chatty]`, `[screams]`.

## 5. Signature sounds
- `[ear-piercing scream]` (tag only; don't also spell it out).
- `[intrigued] ooooh` and `[startled] whoa` (spoken).

## 6. Pronunciation (provisional; test)
- Shiori `シオリ (provisional kana guide; untested)` · Novella `/noʊˈvɛlə/` · Novelites `/ˈnɑvəliːts/` ("novel-eets") · Yorick `/ˈjɔɹɪk/`

## 7. Don't
- A slow, ominous villain voice as the default (her menace is a joke); prim or formal speech; constant
  swearing; a whispery, seductive read of the thirst bits (keep them goofy).

## 8. Example
```
[bright, quick] Shiori~n! Shiori Novella here at your service!
[rapid, excited] This looks like a movie! I genuinely like the look of this!
[deadpan, mock-innocent] For the record, I did not sacrifice anyone.
[nervous, quiet] I would be too scared to play this myself.
[warm, quick] Alright, bye guys! See you later!
```
(Line 1 is an official written introduction. Lines 2–5 use ASR shared wording. All delivery tags are provisional performance directions, not verified descriptions of these recordings.)

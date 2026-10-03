# ElevenLabs v4 Performance Sheet: Cecilia Immergreen

> Built from `bible/characters/Cecilia-Immergreen.md` (2026-10-01). Original designed voice matched only to
> register and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER
> Derivative Works Guidelines). Cecilia is active at the 2026 baseline. Guide: `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice; provisional design choices)
"Perfect audio quality. Young woman, English-speaking, clear mid-high voice; dry and sarcastic as a baseline;
long talkative stretches; loud and giddy when excited; grand and theatrical for mock-villain lines; warm and
self-mocking when thanking people."
- Register basis: qualitative; see `research/audio-check/cecilia.md`. She is an automaton by lore, not by
  voice: no robotic effects.

## 2. Settings (untested audition choices; verify endpoint behavior)
- `eleven_v4`. Stability **40%** (API `0.40`) (fast, with sharp swings). Similarity **75%** (API `0.75`).
- Default tags `[dry, conversational]`. Pace comes from the designed voice plus `[rapid, rambling]` or
  `[deadpan]`; v4 has no speed slider.

## 3. Write these habits into the script
- "like" and "okay" in runs ("okay, okay, okay"; "easy, easy, easy").
- "I hate…" announcements (the Immerhater bit), delivered dry.
- Smug self-praise after luck: "Oh my god, I'm so smart." "My memory is really good."
- German words for jokes ("In German he says…"); light swearing now and then.
- Teases Gigi ("idiot"; "FREAK" in the wiki's transcription); the teasing runs both ways.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Greeting | `[bright, giddy]` | "Hiya!!! It's me!" (official interview) |
| Explaining a story | `[rapid, rambling]` | "…every cool story needs a trio." |
| Hating something | `[deadpan, emphatic]` | (style demo) "I hate Tuesdays. I hate them." |
| Smug after luck | `[mock-proud]` | "Oh my god, I'm so smart." |
| Hard moment in a game | `[tense, repeating]` | "Okay, okay, okay … easy, easy, easy." |
| Panic | `[panicked]` | "It's over for me." |
| Villain moment | `[theatrical, grand]` | "Come then, die by my hands, you foolish mortals!" |
| With Gigi | `[exasperated, teasing]` | "Ew! Get away from me, you FREAK!" (wiki, secondary) |
| Sign-off | `[warm]` | "Thank you very much for spending time with me today." (one ASR shared excerpt) |

With people (provisional): Gigi `[teasing]`; Raora `[warm]`; Kiara `[playful, switching to German]`.

Additional proposed scene directions from the card's Audio Tags (untested): `[warm, self-mocking]`.

## 5. Signature sounds
- `[mock-dramatic] dun dun dun` (spoken; a style demo, not a transcribed line).
- `[laughs]` (tag only).

## 6. Pronunciation (provisional; test)
- Cecilia `/sɛˈsiːliə/` · Immergreen `/ˈɪməɹɡɹiːn/` · Otomos `/oʊˈtoʊmoʊz/` · Immerheim `/ˈɪməɹhaɪm/`

## 7. Don't
- A robotic monotone; a meek, servile maid voice; real cruelty in the "hate" bits; sarcasm in every line.

## 8. Example
```
[bright, giddy] Hiya!!! It's me!
[rapid, rambling] Okay, okay, okay, so every cool story needs a trio, right?
[mock-proud] Oh my god, I'm so smart.
[theatrical, grand] Come then, die by my hands, you foolish mortals!
[warm] Thank you very much for spending time with me today.
```
(Line 1 is an official written greeting. Line 2 is a Style demo incorporating an ASR-supported phrase. Lines 3–5 use individual ASR shared excerpts. All delivery tags are proposed.)

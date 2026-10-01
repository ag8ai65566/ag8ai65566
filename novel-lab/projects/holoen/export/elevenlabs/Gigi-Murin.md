# ElevenLabs v4 Performance Sheet: Gigi Murin

> Built from `bible/characters/Gigi-Murin.md` (2026-10-01). Original designed voice matched only to register
> and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER Derivative Works
> Guidelines). Gigi is active at the 2026 baseline. Guide: `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, American accent, bright, energetic mid-high voice, animated and chatty;
fast run-on chatter; jumps into whiny, mock-dramatic or shouting registers for a specific joke and drops flat
for the punchline; soft and plain when sincere."
- Register basis: qualitative; see `research/audio-check/gigi.md`. Her game window mixes in voiced
  characters and is not used.

## 2. Settings (starting points)
- `eleven_v4`. Stability **35%** (API `0.35`) (big, sudden swings). Similarity **75%** (API `0.75`).
- Default tags `[animated, conversational]`; escalate only for a specific bit. Pace comes from the designed
  voice plus `[chatty, quick]` or `[deadpan]`; v4 has no speed slider.

## 3. Write these habits into the script
- "like" everywhere, "okay," "sure," "hold on," "yay"; she talks to "grems."
- Deadpan comebacks: "I require context."; "I'm sure that's true."; "If it works 51% of the time, that's
  enough."
- Bits that escalate by repetition; a begging whine ("pleeease"); an emphatic "MORI CALLIOPE!"
- Casual swearing now and then; crude jokes stay jokes.
- A sudden soft sincerity ("Thanks for coming to see me!").

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Greeting | `[sing-song, loud]` | "Gi Murin!" (official interview) |
| Chatting | `[chatty, quick]` | (style demo) "Hold on, hold on. Who did this? Was it me?" |
| Superchat reading | `[chatty, quick]` → `[deadpan]` | "I require context." |
| A bit | `[grave, theatrical]` → `[laughs]` | "We're still trying to find the killer…" |
| Bad luck | `[exasperated]` | "I feel like someone hired an Etsy witch to curse me and to hex me." |
| Begging | `[whiny, escalating]` | (style demo) "Pleeease, please, please?" |
| Sincere | `[soft, sincere]` | "Thanks for coming to see me!" (official interview) |
| Sign-off | `[bright, quick]` | "I'll be back tomorrow. You'll see me again." |

With people (provisional): Cecilia `[teasing]`; Mori Calliope `[excited, emphatic]`.

## 5. Signature sounds
- `[whining] pleeease` (spoken).
- `[laughs]`, `[sound effects]` (percussive vocal noises), `[humming]` (tag only; no spelled-out sounds).

## 6. Pronunciation (provisional; test)
- Gigi `/ˈdʒiːdʒiː/` (like "GG") · Murin `/ˈmʊɹɪn/` · grems `/ɡɹɛmz/`

## 7. Don't
- Continuous shouting; a quiet, demure voice as default; cruel teasing; anything sexual beyond a crude joke.

## 8. Example
```
[sing-song, loud] Gi Murin!
[chatty, quick] Okay, okay, superchats. [deadpan] I require context.
[grave, theatrical] We're still trying to find the killer. [laughs]
[exasperated] I feel like someone hired an Etsy witch to curse me and to hex me.
[bright, quick] I'll be back tomorrow. You'll see me again.
```
(Line 1 is her official greeting; "Okay, okay, superchats." is a style demo; the rest are her lines, quoted
only where both transcripts agree.)

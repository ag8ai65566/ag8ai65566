# ElevenLabs v4 Performance Sheet: Watson Amelia

> Built from `bible/characters/Watson-Amelia.md` (2026-09-30). Original designed voice matched only to
> register and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER
> Derivative Works Guidelines). Ame is an affiliate since 2024-09-30. Guide: `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)

The prompt's timbre, laughter and delivery details are provisional creative choices for the original voice. Performance tags throughout this sheet propose readings; they do not certify how an archived quotation sounded. Regional accents require a separate in-scope listening check.
"Perfect audio quality. Young adult woman, English speech with no prescribed regional accent, light and playful upper-range voice,
middling pace that trips over itself with restarts and fillers, mischievous, can drop into a lower gremlin
voice for jokes, high-pitched wheezing screech when losing."
- Register basis (sample observations from the audio check, not synthesis targets): upper range (≈248–276 Hz), middle pace (≈114–133 words per minute of speech). [ASR A23]

## 2. Settings (starting points)
- `eleven_v4`. Stability **40%** (API `0.40`). Similarity **75%** (API `0.75`).

## 3. Write these habits into the script
- "okay" constantly; "oh," "like," "uh," "yeah"; "all right" to move on; "oh yeah, oh yeah" when a lost
  thought comes back.
- Sweet setup, then a crude turn, said as if nothing happened (the ground-pound joke).
- Rage builds through repeated questions to a shout, then may deflate into an apology or "That was a bad
  play on my part."
- Caster-style play-by-play when spectating.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Crude joke | `[innocent]` → `[lower, gremlin voice]` | "…you guys know that's actually what I did to your mom last night." |
| Tilted | `[frustrated, rising]` → `[shouting]` | "Why do my team die so fast?" (ASR) |
| Rage-quit | `[fed up, rapid]` | "This game fucking sucks. It sucks. I'm done. I'm done." |
| Trash talk | `[smug]` | "I bet I could 1v1 at least 80% of you and kick your ass." |
| Owning it | `[plain]` | "That was a bad play on my part." |
| Spectating | `[caster, excited]` | "Let's see if she can pull off a 1v4, full health." (ASR) |
| 2024 nostalgia | `[warm, playful]` | "I'm four years old! I can barely talk!" |
| Gremlin bit | `[mischievous]` | "I'm gonna connect the world with my fist. I'm gonna connect the world by force." |
| Sign-off | `[cheerful]` | "Alright, bye-bye!" |

## 5. Signature sounds
- Gremlin laugh "NEHEHEHEHE!" (secondary spelling): `[gremlin cackle] NEHEHEHEHE!`
- Screech: `[high-pitched wheezing screech]`; hiccups: `[hiccups]` (an optional sparse scene effect).

## 6. Pronunciation (provisional; test)
- Watson Amelia `/ˈwɑtsən əˈmiːliə/` · Teamates `/ˈtiːmˌmeɪts/`

## 7. Don't
- Polished, serene idol phrasing; "chat" as her default address (she says "you guys"); an invented branded
  sign-off; unlimited time travel that solves a scene (it is a bit).

## 8. Example

Independent performance excerpts, not one recorded exchange: line 1 is Amelia reading game tutorial text; line 2 is a separate shared ASR excerpt of her response; line 3 is a proposed spoken cackle using the secondary spelling; line 4 is a separate ASR sign-off. Tags are proposed. No actual family relationship is asserted by the stock mom joke.
```
[innocent, reading] Nothing beats a ground pound.
[lower, gremlin voice] Uh, you guys know that's actually what I did to your mom last night.
[gremlin cackle] NEHEHEHEHE!
[cheerful] Alright, bye-bye!
```

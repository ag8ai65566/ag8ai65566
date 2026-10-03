# ElevenLabs v4 Performance Sheet: Mori Calliope

> Built from `bible/characters/Mori-Calliope.md` (2026-09-30). Original designed voice matched only to
> register and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER
> Derivative Works Guidelines). Guide: `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)

The prompt's timbre, laughter and delivery details are provisional creative choices for the original voice. Performance tags throughout this sheet propose readings; they do not certify how an archived quotation sounded. Regional accents require a separate in-scope listening check.
"Perfect audio quality. Young adult woman, English speech with no prescribed regional accent, low mezzo-alto voice with a slightly
husky edge, fast and loose conversational pace, confident swagger, dorky and self-deprecating underneath,
able to burst into loud laughter or shouting."
- Register basis (sample observations from the audio check, not synthesis targets): low (≈197–214 Hz in chat) and fast (≈161–186 words
  per minute of speech). [ASR C30]

## 2. Settings (untested starting choices; verify endpoint behavior)
- `eleven_v4`. Stability **40%** (API `0.40`) (she swings from deadpan to bursts). Similarity **75%** (API `0.75`).

## 3. Write these habits into the script
- Contractions and loose phrasing: "cuz," "wanna," "gonna"; "y'all," "chat," "Dead Beats."
- Grabs the floor before knowing how the sentence ends; restarts (SECONDARY transcription: "Well... listen. Listen.").
- Casual swearing mid-sentence ("Let's try this shit."); bigger bursts at a breaking point.
- Deadpan setup, then explosion; repeats a question when she can't believe it.
- Sincere lines short and plain.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Settling in | `[casual, fast]` | "I'm here, I got my yum-yum drink." |
| Greeting fans | `[hyped]` | "What's up, Dead Beats?!" |
| Annoyed at a game | `[exasperated, rapid]` | "Oh my god. I'm gonna lose it. What an annoying guy." |
| Tilted | `[shouting]` → `[flat, deflated]` | "WAIT A MINUTE, WAIT A MINUTE!!!" … "whatever, man." |
| Stalling / flustered | `[hesitant]` | SECONDARY transcription: "Well... listen. Listen." |
| Teasing | `[smug, mock-menacing]` | "Let me kill him." |
| After a drink | `[comic gasp]` | "Guh." |
| Sincere | `[plain, warm]` | "Please take care of yourselves first." |
| Sign-off | `[casual, trailing off]` | "All right, take care everybody. I'll see you soon." (ASR; one contiguous excerpt) |

Additional proposed scene directions from the card's Audio Tags (untested): `[confident]`, `[gruff, embarrassed]`, `[warm]`, `[gruff, deflecting]`, `[softening, warm]`, `[groaning at the pun]`, `[mock-feuding, smug]`, `[loud, chaotic]`, `[exasperated]`.

## 5. Signature sounds
- "Guh." after a drink: `[comic gasp] Guh.`
- Laughs first at her own mess-ups: `[laughs]`, `[laughs harder]`.

## 6. Pronunciation (provisional; test)
- Mori Calliope — Japanese reading guide: もり カリオペ (provisional, untested) · kusotori `/kusoˈtoɾi/` · Kronster `/ˈkɹɑnstɚ/`

## 7. Don't
- A sugary idol voice as default; nonstop shouting or a gangsta caricature; an imposed caricature when switching languages
  (Japanese pronunciation remains provisional and untested); every sentence a death pun.

## 8. Example
```
[casual, fast] I'm here, I got my yum-yum drink. [comic gasp] Guh.
[exasperated, rapid] Oh my god. I'm gonna lose it. What an annoying guy.
[laughs] Let's try this shit.
```

# ElevenLabs v4 Performance Sheet: Takanashi Kiara

> Built from `bible/characters/Takanashi-Kiara.md` (2026-09-30). Original designed voice matched only to
> register and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER
> Derivative Works Guidelines). Guide: `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young adult woman, neutral English accent, bright upper-mid voice,
fast and chatty with sudden accelerations, highly expressive, prone to sharp excited cries and loud
laughter, warm when sincere."
- Register basis (sample observations from the audio check, not synthesis targets): upper-middle pitch (≈245–300 Hz, game audio inflates it) and fast in chat (≈133–179 words
  per minute of speech). [ASR T23] Her card gives no accent; German lines come out native in v4 (cross-language generation uses a native accent). [Official T1]

## 2. Settings (starting points)
- `eleven_v4`. Stability **35** (big swings). Similarity **75**.

## 3. Write these habits into the script
- Self-interrupting restarts ("I— I'll go— I'll go and check"); triple repetition ("Okay. Okay. Okay.").
- Flags a tangent, then dives in ("Do you want to hear a tangent to start?").
- Third person when proud or roasting herself: "Look at Wawa…"
- Casual swearing in games: "Holy shit, they're all cracked." "What the fuck am I supposed to do with 16?"
- All-caps shouts inside a sentence ("WAIT. WAIT.").
- German bits: the sign-off lesson ("In German we say auf Wiedersehen."), "danke schön."

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[bright rooster-like cry]` → `[chatty]` | "Kikkeriki! Do you want to hear a tangent to start?" |
| Hyped | `[excited, rapid]` | "Holy shit, they're all cracked, they all look so good." |
| Game surprise | `[shocked]` | "Vault dwellers? What the fuck is there? The wasteland?" |
| Tilted | `[shrieks]` → `[angry, rapid]` → `[flat]` | "No no no no— It's the game that makes it too janky. Don't blame me." |
| KFP manager | `[brisk, faux-authoritative]` | "Welcome to KFP, are you here to order or to apply for a job?" |
| Hosting | `[measured, clear]` | (contained questions, room for the answer) |
| Sincere | `[plain, warm]` | "I hope you guys will still not get tired of me…" |
| Tired | `[flat, still chatty]` | "I don't have much energy today." |
| Sign-off | `[playful]` | "In German we say auf Wiedersehen. Good night!" |

## 5. Signature sounds
- "Kikkeriki!": `[bright rooster-like cry] Kikkeriki!`
- Short cartoonish screams at deaths: `[short scream]`; loud laughter: `[laughs loudly]`.

## 6. Pronunciation (provisional; test)
- Takanashi Kiara `/tɑkɑˈnɑʃi kiˈɑːɹə/` · Kikkeriki `/ˌkɪkəʁiˈkiː/` · Wawa `/ˈwɑwɑ/` ·
  auf Wiedersehen `/aʊ̯f ˈviːdɐˌzeːən/` · KFP spelled out.

## 7. Don't
- Constant screaming that erases the host who lets guests answer; a polite corporate tone with no
  swearing; "ara ara"; every line a bird joke.

## 8. Example
```
[bright rooster-like cry] Kikkeriki! [chatty] Okay okay okay, do you want to hear a tangent to start?
[excited, rapid] You guys are thinking, oh my god, Wawa is really good at making Miis, but everybody is fucking good at making Miis.
[playful] In German we say auf Wiedersehen!
```

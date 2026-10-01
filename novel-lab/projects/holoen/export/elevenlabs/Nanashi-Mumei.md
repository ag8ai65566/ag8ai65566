# ElevenLabs v4 Performance Sheet: Nanashi Mumei

> Built from `bible/characters/Nanashi-Mumei.md` (promoted 2026-10-01). Original designed voice matched only
> to register and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER
> Derivative Works Guidelines). Mumei graduated on 2025-04-27 (04-28 JST); in the 2026 baseline she appears
> in memories and pre-2025 stories. Guide: `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice)
"Perfect audio quality. Young woman, neutral American accent, soft, small, sweet voice in a relatively high
register, a little sleepy and low-energy by default, quick and scattered when chatting, able to break into a
sudden high screech; says dark jokes in the same cute, cheerful tone."
- Register basis (sample observations from the audio check, not synthesis targets): relatively high
  (≈284–311 Hz in 2025 Q&A and game windows), fast when chatting (≈156–168 words per minute of speech),
  sparse commentary in games. [ASR M20]
- Her singing voice is a separate register; this sheet covers speech only.

## 2. Settings (starting points)
- `eleven_v4`. Stability **45** (scattered and spontaneous, but the soft base must hold). Similarity **75**.
- Pace comes from the designed voice plus `[quick, scattered]` or `[murmuring, focused]`; v4 has no speed slider.

## 3. Write these habits into the script
- "okay" in threes ("okay, okay, okay"), "anyways" to cut a tangent, "sorry," "I guess," "you know,"
  "I don't know."
- "yippee" and "hooray," often sarcastic; "oh dear," "uh oh," "oh shoot," "oh my gosh," "oh my goodness."
- Losing the thread mid-sentence and saying so, then starting again.
- Grand guardian claims stated flatly, then undercut ("…but what do I know? Everything.").
- Mild exclamations predominate ("shoot," "heck").
- Goodbyes that repeat a dozen times ("bye-bye, bye-bye…").

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[soft, caught off guard]` | "Oh hi! Hoo's this? Nanashi Mumei!" (official greeting) |
| Chatting | `[quick, scattered]` | "I love talking about myself. Yippee, yippee. Hooray." |
| Losing the thread | `[distracted]` → `[apologetic]` | "Oh, dear. … I guess I already started it, so I'm in the middle of it now." |
| Guardian authority | `[mock-grand, deadpan]` | "…I decide everything for humanity." |
| Macabre teasing | `[light, matter-of-fact]` | "Civilization is temporary…" (wiki, secondary) |
| Startled | `[screeching]` | (tag only) |
| Shooter game | `[murmuring, focused]` → `[bright]` | "Oh dear, that was pointless." |
| Hurt in a game | `[whiny]` | "Owie! Owie! Owie!" |
| Superchats | `[warm]` → `[brisk]` | "don don!" |
| Philosophical | `[soft, matter-of-fact]` | "Sometimes you go through life just not knowing stuff." |
| Sign-off | `[warm, sing-song]`, repeated | "Goodbye for now. I'll see you probably tomorrow, probably tomorrow." |

## 5. Signature sounds
- `[high-pitched screech]` (tag only; don't also spell it out).
- `[gavel call] don don!` (spoken).
- `[sing-song humming]` to fill a silence.

## 6. Pronunciation (provisional; test)
- Mumei `/muːˈmeɪ/` · Nanashi `/nəˈnɑːʃi/` · Hoomans `/ˈhuːmənz/` · moom `/muːm/` · yowai `/joʊˈwaɪ/`

## 7. Don't
- A booming or aggressive voice; heavy swearing; a deep, sinister villain voice for the dark jokes (the joke
  is that she says them cutely); constant high energy.

## 8. Example
```
[soft, caught off guard] Oh hi! Hoo's this? Nanashi Mumei!
[quick, scattered] Okay, okay, okay, so today we're, um, wait. Where was I? Sorry. Anyways.
[mock-grand, deadpan] I decide everything for humanity. [light, matter-of-fact] Civilization is temporary, after all.
[soft, matter-of-fact] It's okay not to know stuff sometimes. Yeah, unless you're me.
[warm, sing-song] Goodbye for now. I'll see you probably tomorrow, probably tomorrow. Bye-bye, bye-bye!
```
(Line 2 and the second half of line 3 are style demos built from her habits; line 1 is her official
written greeting; the others are her lines, quoted only where both transcripts agree.)

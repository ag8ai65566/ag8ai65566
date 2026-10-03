# ElevenLabs v4 Performance Sheet: Mococo Abyssgard

> Built from `bible/characters/Mococo-Abyssgard.md` (promoted 2026-10-01). Original designed voice matched
> only to register and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5;
> COVER Derivative Works Guidelines). Mococo is active at the 2026 baseline; she shares the FUWAMOCO channel with Fuwawa (world card "FUWAMOCO").
> Guide: `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice; provisional design choices)
"Perfect audio quality. Young woman, English-speaking, very high, bright, energetic voice, a little
squeaky; quick when excited; warm and earnest when encouraging someone, building to a cheer; comic timing
on her own name."
- Register basis: qualitative only. Her solo sample is thin and the duo recordings mix both twins, so no
  numbers are used (see `research/audio-check/fuwamoco.md`). Her notes rest mainly on wiki descriptions; a
  2026-10-02 search of the archived channel found no other window where she can be heard alone, so treat every
  direction here as provisional and settle it in your own voice tests.
- Design her voice as clearly distinct from Fuwawa's (see §7): brighter and squeakier, where Fuwawa is softer
  and airier.

## 2. Settings (untested starting choices; verify endpoint behavior)
- `eleven_v4`. Stability **40%** (API `0.40`) (energetic, with quick jumps into a cheer). Similarity **75%** (API `0.75`).
- Pace comes from the designed voice plus `[rapid, excited]` or `[earnest, encouraging]`; v4 has no speed slider.

## 3. Write these habits into the script
- "bau bau" everywhere; short exclamations ("What?", "Haeh?", "This is good!").
- She refers to herself by name ("What about Mococo?"; "I'm not silly. I'm Mococo!").
- Pup Talks: short, sincere encouragement that builds step by step to a cheer ("That means you're
  unstoppable!"; "Not tomorrow! Today!").
- Running the show: she reads "#" aloud ("hashtag hashtag FWMCMORNING").
- Only her own name and nicknames: Mococo, Moco-chan, Mogogo, Mogojyan.
- A drawn-out vowel sometimes tails a word. Fans spell it "Noæ" or "Whæt"; that is fan spelling, not IPA.
  For v4, write the plain word and stretch it ("Nooo!", "Whaaat?"), then test.
- No swearing; no sarcasm in a Pup Talk.

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Introduction | `[bright, comic timing]` | "I'm not... Fuwawa, I'm Mococo!" (wiki, secondary) |
| Pup Talk | `[earnest, encouraging]` → `[cheering]` | "Not tomorrow! Today!" (wiki, secondary) |
| Surprised | `[squeaky]` | (Style demo) "Whaaat?" |
| After a sneeze | `[embarrassed, small]` | (Style demo) "Nooo!" |
| Running the show | `[bright, brisk]` | "Please tweet your thoughts to the hashtag, hashtag FWMCMORNING." (wiki, secondary) |
| Overexcited | `[rapid, excited]` | "I'm the danger!" (wiki, secondary) |
| Scared in a game | `[nervous, quiet]` → `[reckless]` | "If I die, I die." |
| Playful | `[giggles]` → `[bright]` | "Ehehe, it's play time, whether you're ready or not!" (official) |

With people (provisional): Fuwawa `[close, a little bossy]`; Polka `[starstruck]`; Gigi `[playful]`.

Additional proposed scene directions from the card's Audio Tags (untested): `[bright, energetic]`.

## 5. Signature sounds
- `[sneezes]` (tag only), then `[embarrassed] Nooo!`
- `[giggles] ehehe` and `[cheerful] bau bau!` (spoken).

## 6. Pronunciation (provisional; test)
- Mococo `モココ (provisional kana guide; untested)` · Mogogo `/moʊˈɡoʊɡoʊ/` · Mogojyan `/moʊɡoʊˈdʒɑn/` · Abyssgard `/ˈæbɪsɡɑɹd/`

## 7. Don't
- A low or lazy voice; sarcasm in a Pup Talk; swearing; any nickname she has not approved.
- Never merge the twins: in a FUWAMOCO scene each line belongs to one twin unless they speak in sync, and
  then give both voices the same line.

## 8. Example
```
[bright, comic timing] I'm not... Fuwawa, I'm Mococo!
[giggles] Ehehe, it's play time, whether you're ready or not!
[nervous, quiet] Okay... [reckless] If I die, I die.
[sneezes] [embarrassed, small] Nooo!
[earnest, encouraging] Even if things don't go your way, you get back up and do your best. [cheering] That means you're unstoppable!
```
(Line 1 is the wiki's transcription of her introduction; line 2 is her official line; "If I die, I die" is
quoted where both transcripts agree; "Okay..." and "Nooo!" are style demos; line 5 is a Style demo inspired by a secondary account of a Pup Talk, not a quotation.)

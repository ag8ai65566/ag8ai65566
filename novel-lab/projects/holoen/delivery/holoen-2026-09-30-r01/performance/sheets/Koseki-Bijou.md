# ElevenLabs v4 Performance Sheet: Koseki Bijou

> Source voice fields SHA-256 (Name, Dialogue Style, Catchphrases, Voice & Delivery, Audio Tags): `c747997fcb95615ed99b9d039ee07054fd7cfb78b2a385fd31ed44d74f135cb5` — reviewed 2026-10-04: Claude 2026-10-04: voice audits v1-v4 merged (research/qa/voice-audit-dispositions.md); attestation research/qa/voice-delivery.md; author decisions 2026-10-04 (quote inventory B; JP members speak Japanese)
> Built from `bible/characters/Koseki-Bijou.md` (promoted 2026-10-01). Original designed voice matched only
> to register and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5; COVER
> Derivative Works Guidelines). Bijou is active at the 2026 baseline. Guide: `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice; provisional design choices)
"Perfect audio quality. Young woman, English-speaking, small, bright, bubbly, high voice; quick and
bouncy when excited or hosting; goes calm, quiet and flat under pressure; sudden squeaky bursts of laughter;
playful, childlike energy."
- Register basis: qualitative only. The sampled gameplay recordings mix in game audio, so their numbers are
  not used as targets here (see `research/audio-check/bijou.md`).

## 2. Settings (untested starting choices; verify endpoint behavior)
- `eleven_v4`. Stability **45%** (API `0.45`) (bubbly swings, but the calm gaming voice must hold). Similarity **75%** (API `0.75`).
- Pace comes from the designed voice plus `[excited, bouncy]` or `[focused, calm]`; v4 has no speed slider.

## 3. Write these habits into the script
- "okay," "yeah," and runs of "yes, yes, yes"; repeats for emphasis ("over here, over here").
- Talks to "everyone" and "Pebbles," with playful orders ("Make a heart!").
- Gen Alpha slang ("skibidi," "rizz," "gyatt," "67"), used as a joke.
- Swears are replaced with "beep," in the rhythm of the word it replaces ("don't be super beeping early");
  "dang it!" for frustration. Write no real swear words for her.
- Mock-solemn lore lines followed by a giggle; mock outrage, never real rage.
- Now and then she turns a hard G into a J on purpose ("Jerudo").

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[excited, bouncy]` | "BIBOO BIBOO! I'm Koseki Bijou, sparkling gem of hololive English -Advent-!" (official) |
| Hosting Pebbles | `[playful, commanding]` | "Welcome to my birthday world! We're gonna save the city!" |
| Mock solemn | `[grave, theatrical]` → `[giggles]` | "…worthy sacrifice, I will remember you." |
| Calm gaming | `[focused, calm]` | "Managing my resources like a pro." |
| Mock outrage | `[indignant, fast]` | "…circus! Everyone's dumb!" |
| Caught out | `[deadpan]` | "You saw nothing. I saw nothing." |
| Frustrated | `[mildly annoyed]` | "dang it!" |
| Sincere thanks | `[warm]` | (style demo) "Thank you, everyone, really." |
| Sign-off | `[cheerful, quick]` | "Thank you everyone! I will finish RE4 next time!" |

With people (provisional): Shiori `[cheeky]`; Kiara `[hyped, meme-y]`; Kaela `[comfortable, playful]`;
IRyS `[excited teammate]`; FUWAMOCO `[silly]`.

Additional proposed scene directions from the card's Audio Tags (untested): `[bright, bubbly]`, `[delighted]`.

## 5. Signature sounds
- `[squeaky laugh] ha ha ha ha` and `[giggles] hehehe` (spoken).
- `[censoring herself] beep` (spoken, in place of a swear).
- `[deflated] bweh` (spoken).
- `[humming]` to fill a quiet stretch (tag only).

## 6. Pronunciation (provisional; test)
- Bijou `/biˈʒuː/` ("bi-joo") · Biboo `/ˈbiːbuː/` · Koseki `コセキ (provisional kana guide; untested)` · Gerudo as "Jerudo" `/dʒəˈɹuːdoʊ/`
  (her quirk, on purpose)

## 7. Don't
- Any real swearing (she says "beep"); a deep or growly voice; rage when losing (her calm is the point);
  a cold, menacing "evil" voice unless it is obviously the Oobib bit.

## 8. Example
```
[excited, bouncy] BIBOO BIBOO! I'm Koseki Bijou, sparkling gem of hololive English -Advent-!
[playful, commanding] Welcome to my birthday world! We're gonna save the city!
[grave, theatrical] …Worthy sacrifice, I will remember you. [giggles]
[deadpan] You saw nothing. I saw nothing.
[cheerful, quick] Thank you everyone! I will finish RE4 next time!
```
(Line 1 is her official introduction; the rest are her lines, quoted only where both transcripts agree (line 3
starts mid-sentence).)

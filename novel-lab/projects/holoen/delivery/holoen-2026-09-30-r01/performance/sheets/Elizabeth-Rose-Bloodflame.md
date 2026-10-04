# ElevenLabs v4 Performance Sheet: Elizabeth Rose Bloodflame

> Source voice fields SHA-256 (Name, Dialogue Style, Catchphrases, Voice & Delivery, Audio Tags): `d80dc9dcdaa93be2b4ef12641d1a3430b52bc24926181de01f7e6056668529d2` — reviewed 2026-10-04: Claude 2026-10-04: voice audits v1-v4 merged (research/qa/voice-audit-dispositions.md); attestation research/qa/voice-delivery.md; author decisions 2026-10-04 (quote inventory B; JP members speak Japanese)
> Built from `bible/characters/Elizabeth-Rose-Bloodflame.md` (2026-10-01). Original designed voice matched
> only to register and energy; never clone or imitate the member's real voice (ElevenLabs Use Policy §5;
> COVER Derivative Works Guidelines). Elizabeth is active at the 2026 baseline. Guide:
> `novel-lab/docs/elevenlabs-v4.md`.

## 1. Voice Design prompt (original voice; provisional design choices)
"Perfect audio quality. Young woman, English-speaking, warm, mid-to-low, well-supported singer's speaking voice;
polite and gentle by default; grand and theatrical for royal proclamations, with a haughty 'oh-ho-ho' laugh;
quick to switch into playful character voices."
- Register basis: qualitative. Her cleanest sample (a 2025 after-party chat) is lower than the other Justice
  members'; the 2026 game windows mix in game voices, so no numbers are used as targets (see
  `research/audio-check/elizabeth.md`).

## 2. Settings (untested starting choices; verify endpoint behavior)
- `eleven_v4`. Stability **50%** (API `0.50`) (warm and steady, with theatrical peaks). Similarity **75%** (API `0.75`).
- Pace comes from the designed voice plus `[warm, polite]` or `[grand, theatrical]`; v4 has no speed slider.

## 3. Write these habits into the script
- British words: "Ello," "Soz," "bits and bobs," "for funsies," "willy-nilly," "whilst," "gosh," "cheeky,"
  "lovely"; plenty of "like" and "okay."
- Minced oaths, not swears: "What the frick?", "What the Frigg!", "friggin'," "mothertrucker."
- TV-host framing: "Lovely to see you, to see you LOVELY!"; "Please do not swear."; "let my voice be your strength" (ASR); separately, "Huzzah!" (ASR)
- "Aww" and "adorable" at anything cute; humming or a sung phrase between sentences.
- Gentle self-mockery (Style demo: "Workaholic? Me? Never."); warm thanks to "Rosarians."

## 4. Tag palette by situation
| Situation | Tags | Line |
|---|---|---|
| Opening | `[warm, theatrical]` | "Lovely to see you, to see you LOVELY!" (official interview) |
| Fictional character bit | `[playful, theatrical]` | (Style demo) "Stand back, everyone. I shall handle this!" |
| Royal proclamation | `[grand, haughty]` → `[laughs]` | "By royal decree, my sweet Rosarians…" (her post) |
| Cute moment | `[soft, cooing]` | (style demo) "Aww, that's adorable." |
| Startled | `[startled]` | "What the frick? Oh my god, you scared them." |
| About singing | `[enthusiastic, sincere]` | "…singing is good for the soul." |
| Teasing herself | `[dry, amused]` | (style demo) "Workaholic? Me? Never." |
| Sign-off | `[warm]` → `[rallying cry]` | "let my voice be your strength" (ASR); separately, "Huzzah!" (ASR) |

Default: `[warm, conversational]`; save the royal flourish for bits.

With people (provisional): Nerissa `[affectionate, playful rivalry]`; Kureiji Ollie `[admiring]`.

## 5. Signature sounds
- `[haughty laugh] Oh~hohoho!` and `[cheering] Huzzah!` (spoken).
- `[humming]` (tag only).

## 6. Pronunciation (provisional; test)
- Elizabeth `/ɪˈlɪzəbəθ/` · Bloodflame `/ˈblʌdfleɪm/` · Rosarians `/ɹoʊˈzɛəɹiənz/` · Exardia `/ɛɡˈzɑːdiə/`

## 7. Don't
- A cold, haughty aristocrat as default (the queen is a bit; she is kind); real
  swearing; a shrill voice.

## 8. Example
```
[warm, theatrical] Ello, Rosarians! Lovely to see you, to see you lovely!
[enthusiastic, sincere] I sing too much everywhere I go, there's always Liz noises.
[startled] What the frick? Oh my god, you scared them.
[dry, amused] Sorry, I just brought you into a random stranger's house and just had you listen to them sleep.
[warm] Let my voice be your strength!
```
(Lines 2–5 use ASR shared wording. Line 4 comments on a fictional scene in Tomodachi Life, not anyone's private life. All delivery tags are proposed; "Ello, Rosarians!" in line 1 is a style demo
joined to her official catchphrase.)

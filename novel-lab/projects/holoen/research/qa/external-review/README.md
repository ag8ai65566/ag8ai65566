# External review of holoen r02 (Gemini Neon)

## Author decision (2026-11-27)
「不用給codex審核了，可以去給桌面版的Gemini Neon複審」: the Codex/GPT review of the r02 additions is dropped; the work is
re-reviewed by Gemini Neon (desktop app) instead. This applies to the r02 work that Claude did alone (FLOW GLOW,
hololive GAMERS, the outfits on all character cards, and the ties added to existing cards). The framework's general GPT
rule (`.claude/skills/novel-lab`) is not changed by this decision.

Claude cannot operate the desktop app from the cloud session where the decision was made (computer use was not
available there), so the author runs the review: give each packet to Gemini Neon and paste its reply back to Claude.

## Packets
| File | What Gemini checks |
|---|---|
| `gemini-r02-A-new-members.md` | The seven new character cards, the FLOW GLOW and hololive GAMERS world cards, their performance sheets, the two audio-check reports and the two self-check audits |
| `gemini-r02-B-outfits-and-ties.md` | Part 1: every outfit description on the 40 character cards against the official gallery images (URLs listed); Part 2: the FLOW GLOW and GAMERS ties added to existing cards |

Each packet starts with the instructions and the reply format (a verdict line, a findings table with P0/P1/P2
severities, "Could not verify" and "Notes"). The packets were generated from the working files on 2026-11-27; a packet
is a snapshot, so regenerate it after any edit that should be reviewed.

## Merging the reply
Claude checks every finding against its evidence before changing a card (a reviewer can be wrong too), records each
disposition (fixed, rejected with the reason, or left open) in `research/qa/audit-flowglow.md` and
`research/qa/audit-gamers.md` (and, for outfit and tie findings on other cards, in those cards' evidence notes), re-runs
the export and validation, and builds the next delivery (r03). The cards' "Gemini Neon review pending" notes change to
the review date only after the merge.

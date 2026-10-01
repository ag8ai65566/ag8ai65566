# Sudowrite Style: audio-ready dialogue (ElevenLabs v4)

Paste the block below into Sudowrite's **Story Bible → Style** box (under the project's own style notes,
about 115 words). It tells Sudowrite to write ElevenLabs v4 tags into every line of dialogue, using
each character's **Audio Tags** trait (exported as the `Audio Tags` column of `characters.csv`).

```text
Audio-ready dialogue for ElevenLabs v4: inside every line of spoken dialogue, put one to three performance tags in square brackets right before the words they shape, e.g. "[deadpan] It's me, perfection." Take tags from the speaker's Audio Tags trait; change tags mid-line when her mood turns. Write signature sounds as tag plus word ([startled squawk] GWAK!). Keep her real fillers, restarts, repetitions and swears in the words; use ellipses for pauses, dashes for interruptions, CAPS for stress. Plain-language tags only: no SSML, no tags in narration except [pause]. Each character keeps her own pace and register; never make two characters sound alike.
```

## Notes
- Tags are performance directions for an **original** designed voice. Do not clone or imitate any member's
  real voice (ElevenLabs Use Policy §5; COVER Derivative Works Guidelines).
- Before sending to ElevenLabs, split narration (narrator voice) from dialogue (one voice per character),
  and keep each Text to Dialogue request under about 2,000 characters.
- If Sudowrite overuses tags, lower it to "one or two tags" in the Style text; if it drifts to generic
  tags ([happy], [sad]), add "Use only tags listed in the speaker's Audio Tags trait."
- Guide: `novel-lab/docs/elevenlabs-v4.md`.

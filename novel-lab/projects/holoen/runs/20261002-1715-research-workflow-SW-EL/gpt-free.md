## Verified platform facts

**The workflow is viable with Eleven v4. The package needs a strict script format, an offline converter, synchronized tag palettes, and honest runtime-test reporting.** The character baseline remains **2026-09-30**; platform documentation was checked on **2026-10-02**.

| Platform | Feature | What it does now | Source URL | Checked | What our docs say | Agree? |
|---|---|---|---|---|---|---|
| Sudowrite | Story Bible structure | Braindump introduces the premise; Genre supplies thematic direction; Style controls prose; Synopsis summarizes the story; Characters and Worldbuilding store cards; Outline organizes chapters. | [Braindump](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/braindump/bgfrku4qGdfbiFH3ar9PE2), [Genre](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/genre/hCJPQqQYtUQm7ntdcRFJHg), [Style](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/style/4gqKgVVjdN6XTKo71HChqV), [Synopsis](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/synopsis/r4GGUdR23VKcK2WrQVdheb) | 2026-10-02 | Same seven sections. | Yes. |
| Sudowrite | Character fields | Name and Role, plus default traits Pronouns, Groups, Other Names, Personality, Background, Physical Description and Dialogue Style. Custom traits are supported. `Audio Tags` is our custom instruction field, not a native audio integration. | [Characters](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/characters/a7tdE1ZB8KvAwMD3Mopwpd) | 2026-10-02 | Matching CSV columns and custom traits. | Yes. Every project character must retain `Protagonist`. |
| Sudowrite | Worldbuilding fields | Named elements have configurable types and traits, including aliases. Structured CSV imports preserve supplied data. | [Worldbuilding](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/worldbuilding/uc5NfWSz4x8Wm3S19LZeo8) | 2026-10-02 | `Name,Role,Other Names,Description` plus custom fields. | Supported in principle; official downloadable template could not be fetched again. |
| Sudowrite | Published limits | Braindump and Synopsis: 4,000 words each. Style Examples: 1,000 words. Characters: 2,000 cards. Outline: no documented word/chapter limit. | [Limit update](https://feedback.sudowrite.com/changelog/three-big-improvements), [Muse](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/sudowrite-muse/4k9bFDMSyic6mFPkYFHrkZ), [Outline](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/outline/3owKyHXUm1bCdp41b2Npjk) | 2026-10-02 | Matching hard limits; additional local soft limits. | Yes, with distinctions below. |
| Sudowrite | Unpublished limits | No public numerical limits located for individual traits, Genre, Style, Scenes or Extra Instructions. The project’s approximately 120-word Style target is local guidance. | [Style](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/style/4gqKgVVjdN6XTKo71HChqV), [Scenes & Draft](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/scenes--draft/49p5MTVxTKkVFEC5rVUzpY) | 2026-10-02 | Correctly labels these unpublished. Worldbuilding’s 2,000-element claim comes from its CSV template. | Mostly. Worldbuilding count ceiling was not independently reverified. |
| Sudowrite | Visibility | Whole cards or individual traits can be hidden. Hidden material is unavailable to all AI features, including Plugins. Default visibility is on. | [Visibility](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/visibility-settings/4KL8gFeLZP6ep8keUhKVGp) | 2026-10-02 | Hide Secrets after import, before generation. | Yes. Treat visibility as an import checklist item. |
| Sudowrite | Import routes | Characters/Worldbuilding: header `••• → Import`, then CSV. Unstructured imports use AI, accept up to 60,000 words and identify up to 30 items per operation; CSV bypasses that extraction. Outline accepts pasted text/files or a two-column CSV. Document, Novel and Scrivener imports serve different purposes. | [Importing files](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/importing-files/rbGUgrZM6tNuXFG1hjDFyS) | 2026-10-02 | Uses CSV for cards and paste for story fields. | Yes. Do not use Import Novel to load this curated bible. |
| Sudowrite | Write | Continues existing text; Auto, Guided and Tone Shift modes. Generates 1–6 alternatives; length settings range from roughly 50–1,500 words, with model-dependent Max Words up to about 2,000. | [Write](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/write/pvxUvbQqYybfEosqx1sXjY) | 2026-10-02 | Same. | Yes. These are prose word counts, not ElevenLabs character budgets. |
| Sudowrite | Draft and chapter planning | Linked Outline summaries generate Scenes; Draft uses Scenes and bible context to draft a chapter. Scene count influences length. Detection underlines show recognized cards. Extra Instructions can reinforce output format. | [Scenes & Draft](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/scenes--draft/49p5MTVxTKkVFEC5rVUzpY) | 2026-10-02 | Outline → Scenes → Draft. | Yes. A generated chapter still needs conversion into bounded audio scenes. |
| Sudowrite | Rewrite and Describe | Rewrite accepts selections up to 6,000 words. Its current article says short selections can use Synopsis, but contains an older contradictory transcript. Describe suggests sensory details/metaphors using local context. Neither promises preservation of script syntax. | [Rewrite](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/rewrite/9hkeezeUsCiUCG4dRdEqjS), [Describe](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/describe/aTHZdZBjRmH8AspqrPdPcP) | 2026-10-02 | Rewrite limit documented; no structured-script safeguards. | Add mandatory lint after either tool changes a script. |
| Sudowrite | Plugins | Prompt-based tools generate, analyze or transform text. Bible variables include `characters`, `worldbuilding`, their `_raw` variants, Style and chapter scenes. `_raw` bypasses relevance filtering, not visibility. | [Building Plugins](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/how-do-i-build-plugins/a3iVxJb4UZLKfSxf8BG3mY) | 2026-10-02 | Same. | Yes. A Plugin may format scripts; it does not replace deterministic validation. |
| Sudowrite | Models | Muse 1.5 remains the documented default for Write/Draft. The newer official changelog identifies Excellent as Ballad 1.1, superseding the older page naming Claude 3.7. Experimental selections vary. | [Muse](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/sudowrite-muse/4k9bFDMSyic6mFPkYFHrkZ), [Ballad update](https://feedback.sudowrite.com/changelog/even-more-excellent-prose), [Model page](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/prose-modes--models/2X5FuivhsbwUiMNym5eUqm) | 2026-10-02 | Muse and Ballad; extensive experimental-model list. | Core choices agree. Full current selector roster and tag reliability were not verified. |
| Sudowrite | Export and API | Documents export as DOCX; projects as ZIP or merged DOCX. These exclude Story Bible. Characters, Worldbuilding and Outline export separately as CSV. No documented public Sudowrite API was located. | [Exporting files](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/exporting-files/3NtVWXcnwYaRCmPW2iwcCB), [Plugin documentation](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/how-do-i-build-plugins/a3iVxJb4UZLKfSxf8BG3mY) | 2026-10-02 | Correct export warning; no implemented bridge. | Use an explicit copy-to-UTF-8-file handoff. API absence is unverified, not proven. |
| ElevenLabs | Current model | Eleven v4: `eleven_v4`. Realtime variant: `eleven_v4_turbo`. Both support 90+ languages. | [Models](https://elevenlabs.io/docs/overview/models), [Eleven v4](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4) | 2026-10-02 | Same names and IDs. | Yes. Use `eleven_v4` for this package. |
| ElevenLabs | Audio tags | Inline square-bracket natural-language directions. They are not a closed official enum. Tags affect delivery; `voice_id` selects the speaker. Following a direction is not guaranteed. | [Text to Dialogue](https://elevenlabs.io/docs/overview/capabilities/text-to-dialogue) | 2026-10-02 | Natural-language and compound tags; provisional palettes. | Yes. Our allowlists are project controls, not a complete platform tag catalogue. |
| ElevenLabs | Dialogue in app | Selecting multiple speakers on the website enables Dialogue mode. Assign a saved voice to each turn. | [Dialogue mode](https://elevenlabs.io/docs/help-center/product/core-capabilities/text-to-speech/what-is-dialogue-mode) | 2026-10-02 | Recommends Text to Dialogue. | Yes. Importing our JSON into the app was not verified. |
| ElevenLabs | Dialogue API | `POST /v1/text-to-dialogue`; body contains `inputs`, each with `text` and `voice_id`. Set `model_id` explicitly: the reference still defaults to `eleven_v3`. | [Create dialogue](https://elevenlabs.io/docs/api-reference/text-to-dialogue/convert) | 2026-10-02 | No request schema. | Material omission. Converter below supplies it. |
| ElevenLabs | Request limits | Endpoint reference: at most ten unique voice IDs; keep total input text at or below 2,000 characters for reliable generation. The overview’s “unlimited speakers” statement conflicts with the endpoint. The broader model table’s 10,000-character figure does not override this dialogue guidance. | [Create dialogue](https://elevenlabs.io/docs/api-reference/text-to-dialogue/convert), [Dialogue quickstart](https://elevenlabs.io/docs/eleven-api/guides/cookbooks/text-to-dialogue), [Models](https://elevenlabs.io/docs/overview/models) | 2026-10-02 | Approximately 2,000 characters; no speaker cap. | Add an exact project ceiling and ten-ID check. |
| ElevenLabs | Settings | V4 exposes Stability and Similarity, without Style/Speed sliders or SSML. The generic voice-settings API documents `stability` and `similarity_boost` on 0–1 scales. | [V4 controls](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4), [Voice settings API](https://elevenlabs.io/docs/api-reference/voices/settings/update) | 2026-10-02 | Correct percentage/decimal conversions; per-character starting choices. | Values are audition proposals. Per-turn settings serialization/inheritance was not verified; converter does not invent it. |
| ElevenLabs | Voice Design | App: Voices → My Voices → Add a new voice → Voice Design. Generates previews, then saves a chosen voice. API design accepts a 20–1,000-character description and optional 100–1,000-character preview text; its design model is separate from the synthesis model. Save the chosen preview to obtain a persistent `voice_id`. | [Voice Design](https://elevenlabs.io/docs/eleven-creative/voices/voice-design), [Design API](https://elevenlabs.io/docs/api-reference/text-to-voice/design?explorer=true), [Save voice](https://elevenlabs.io/docs/api-reference/text-to-voice/create) | 2026-10-02 | Design original voices, then map IDs. | Yes, but remove instructions to derive designs from member measurements. |
| ElevenLabs | Pronunciation | V4 supports inline slash-delimited IPA and alias/phoneme dictionaries. Dictionaries are case-sensitive; API requests can attach up to three versioned locators. SSML phoneme/break tags are not the v4 route. | [Pronunciation guide, October 1](https://elevenlabs.io/blog/pronunciation-dictionary-guide), [Best practices](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices) | 2026-10-02 | Mainly inline IPA and provisional reading notes. | Expand to versioned dictionaries; preserve Japanese reading notes separately. |
| ElevenLabs | Studio / projects | Studio provides long-form organization and timeline assembly. It accepts uploaded audio and separate SFX. Studio project creation also has an API. Current Studio documentation imposes additional distribution restrictions on uploaded audio and some export routes. | [Studio](https://elevenlabs.io/docs/eleven-creative/products/studio), [Studio API](https://elevenlabs.io/docs/api-reference/studio/add-project), [Audiobooks](https://elevenlabs.io/docs/eleven-creative/products/audiobooks) | 2026-10-02 | Mentions Studio without assembly instructions. | Incomplete. Use downloadable assembly as the initial delivery target. |
| ElevenLabs | Output formats | Dialogue defaults to `mp3_44100_128`; output format is a query parameter. Other supported codecs include PCM/WAV and telephony formats; higher-quality options depend on subscription. A WAV container does not by itself establish lossless source quality. | [Create dialogue](https://elevenlabs.io/docs/api-reference/text-to-dialogue/convert), [Studio](https://elevenlabs.io/docs/eleven-creative/products/studio) | 2026-10-02 | Not specified. | Add format and source-quality records. |
| ElevenLabs | Voice rights and library | Unauthorized replication, harmful impersonation and deceptive use are prohibited. Voice Design voices work with v4, but current documentation says generated voices cannot be publicly shared through Voice Library. | [Use Policy](https://elevenlabs.io/use-policy), [Voices](https://elevenlabs.io/docs/overview/capabilities/voices), [Terms](https://elevenlabs.io/terms-of-use) | 2026-10-02 | No cloning or member imitation. | Correct project rule; add distribution and disclosure instructions. |
| COVER | Fan works and synthetic voice | Overall guidelines govern applicable fan fiction: hobby scope, no misleading official presentation, and other content/right restrictions. Music guidelines expressly prohibit extracting talent vocals from songs for speech generation. | [Derivative Works Guidelines — OFFICIAL](https://hololivepro.com/en/terms/) | 2026-10-02 | Correct song-extraction warning; some wording overgeneralizes it. | Distinguish the express song restriction, ElevenLabs policy, and our broader no-imitation rule. |

**Local findings:** the working export contains **28 character rows**, all `Protagonist`, and **27 worldbuilding rows**; their Secrets fields are empty. There are **33 working performance sheets**. Those counts describe this snapshot, not a newly approved roster. The release builder must continue shipping only sheets corresponding to included cards.

**Coverage:** no account UI, import, paid generation or listening test was performed. Official CSV downloads were inaccessible; nested dialogue-settings behavior and the complete current Sudowrite experimental-model menu remain unverified. Existing character quotations were not re-audited, and no new spoken quotation is accepted here. All example dialogue below is labelled invented Style demo material.

## End-to-end workflow

Use two separate roots:

- **Immutable package:** `delivery/<release>/`, containing the reviewed bible, instructions and tools.
- **Production workspace:** `production/<story>/`, containing drafts, private voice mappings, requests, takes and results. Never write production records into an already hashed release.

0. **Setup — author and package maintainer.**  
   **Inputs:** `manifest.json`, `validation.json`, `00-START-HERE.md`, author promotion decisions.  
   **Actions:** identify the package version; create the production workspace; record the baseline, intended languages, narration choice and distribution scope. Copy `performance/voice-map.example.json` to `production/<story>/voice-map.json`; retain only planned speakers, with pending values initially.  
   **Outputs:** `production.json`, `voice-map.json`, `test-results.csv`.  
   **Checks:** draft status is visible; package counts match the manifest; promotions remain author decisions.  
   **Failure/fix:** a draft package is mistaken for a tested release → record its unresolved checks and keep runtime status `not_run`.

1. **Load the bible into Sudowrite — writer.**  
   **Inputs:** `sudowrite/characters.csv`, `worldbuilding.csv`, `style.txt`, `paste.md`.  
   **Actions:** import each combined CSV once into a test project; inspect custom traits and separate Fuwawa/Mococo cards; paste Style; enter story-specific Braindump and Genre; leave Synopsis genuinely empty until ready. Check visibility before generation.  
   **Outputs:** Sudowrite project plus `imports.md` and an import-test row.  
   **Checks:** counts, Unicode, multiline fields, `Audio Tags`, Role values and hidden traits.  
   **Failure/fix:** duplicate cards after reimport → remove duplicates; update existing fields from `paste.md`. Do not assume name-based merging.

2. **Plan a scene — writer, with author decisions where needed.**  
   **Inputs:** `scene-setup.md`, relevant cards, story Outline, `scene-prompt.txt`.  
   **Actions:** specify scene date, exact participants, relevant world elements, each participant’s immediate objective, the change that occurs, and the exit condition. Separate invented scene events from factual background. For earlier scenes, mute later information in a project copy.  
   **Outputs:** `scenes/s001.plan.md`; linked Sudowrite chapter and Scenes entry.  
   **Checks:** recognized names, allowed factual scope, chronology, no unsupported private-life additions.  
   **Failure/fix:** a card is absent from generation context → correct names/visibility, reduce irrelevant context and inspect generation history.

3. **Draft dialogue with tags — writer using Sudowrite.**  
   **Inputs:** scene plan, Style, scene-format prompt and relevant Audio Tags traits.  
   **Actions:** draft one bounded audio scene using Draft or Guided Write; maintain exact speaker labels. Put Japanese pronunciation notes outside spoken text. After Rewrite or Describe, check the format again.  
   **Outputs:** `scenes/s001.scene.txt`, UTF-8, and `scenes/s001.provenance.md`.  
   **Checks:** invented dialogue is not presented as a real quotation; established profanity remains uncensored; no forced catchphrase quota.  
   **Failure/fix:** purported real quotations lack the required shared ASR span → move them to `quote-candidates.tsv` with video, timestamp and approximate words for Claude’s two-model check.

4. **Lint the script — writer, then voice director.**  
   **Inputs:** script, planned voice-map keys and packaged performance sheets.  
   **Actions:** run the converter with `--lint-only`; pending IDs may be reviewed warnings during this stage. Resolve unknown names, unsupported palette tags, malformed brackets and missing romanization. Separate a long dramatic scene into successive audio scene IDs when needed.  
   **Outputs:** `lint/s001.txt`, corrected script and warning-resolution notes.  
   **Checks:** one speaker per turn; request budget; no duplicate nonverbal rendering; all excluded cues survive on the listening sheet.  
   **Failure/fix:** a valid card tag fails sheet validation → reconcile the source card and sheet, re-export and rerun. Do not silently whitelist every bracketed expression.

5. **Design the original voices — voice director.**  
   **Inputs:** scoped performance directions and invented audition lines.  
   **Actions:** write an independent Voice Design brief without member names, recordings, likeness requests, measured targets or biographical inferences. Audition neutral delivery, an emotional change, a nonverbal event and Japanese material where relevant. Save a chosen voice and enter its persistent ID.  
   **Outputs:** `voices/<speaker-stem>.design.md`, `voice-map.json`, audition audio and `pronunciation-locators.json` if used.  
   **Checks:** originality, intelligibility, expressiveness and suitability for the fictional script—not resemblance to the member.  
   **Failure/fix:** accidental recognizable imitation → reject that design and change its independent characteristics. Incorrect pronunciation → test ordinary spelling first, then a documented dictionary rule.

6. **Generate in ElevenLabs — voice director.**  
   **Inputs:** finalized scripts, complete voice map, sheets and tested dictionary versions.  
   **Actions:** run the converter normally. For API use, submit each generated JSON body through the director’s authorized client to `POST /v1/text-to-dialogue`; keep credentials outside the package. Record the output-format query separately. For app use, follow the listening sheet and assign each saved voice manually.  
   **Outputs:** `requests/s001.json`, `requests/s001.listening.txt`, `takes/s001.take01.mp3` or the supported chosen format, and `takes/s001.take01.json`.  
   **Checks:** explicit `eleven_v4`, correct turn order, persistent IDs, actual generation settings and complete output.  
   **Failure/fix:** validation error or truncated audio → inspect aggregate input length and speaker count; subdivide the scene. Do not silently switch models.

7. **Listen and fix — voice director; writer approves wording changes.**  
   **Inputs:** audio, listening sheet and script.  
   **Actions:** check every turn for speaker assignment, pronunciation, omitted words, spoken tags, duplicate sounds, unwanted additions and joins. Change one variable at a time. Edit the source script before regenerating requests.  
   **Outputs:** `listening/s001.review.md`, revised script/request and accepted-take record.  
   **Checks:** both sentence-level delivery and the complete conversation; Japanese checked by a competent listener.  
   **Failure/fix:** weak direction → simplify or revise a listed tag, then audition again. A seed is an aid to consistency, not an audio-reproduction guarantee.

8. **Assemble and deliver — voice director/editor.**  
   **Inputs:** accepted takes, listening-sheet PAUSE/SFX/STAGE cues and original/licensed ancillary assets.  
   **Actions:** assemble in Studio or an audio editor; insert exact silence, overlaps and SFX there. Preserve accepted speech clips. Produce the chosen downloadable deliverable and disclosure.  
   **Outputs:** `assembly/`, `deliverables/<story>.wav` or `.mp3`, `credits.txt`, `disclosure.txt`, `delivery-manifest.json`.  
   **Checks:** full beginning-to-end listen, cue placement, intelligibility, clipping, output format and rights.  
   **Failure/fix:** a Studio publishing route omits or disallows uploaded audio/SFX → use a supported download/export route or external assembly; do not assume all Studio distribution paths are equivalent.

9. **Version and archive — maintainer and author.**  
   **Inputs:** accepted source, request bodies, take records, runtime tests and delivery files.  
   **Actions:** archive the package version, converter version/hash, script hashes, voice IDs/design briefs, dictionary versions, model, endpoint, settings, seed, generation date/request IDs and accepted audio hashes. Keep future takes in a new revision.  
   **Outputs:** `archive/<production-revision>/`, `CHANGELOG.md`, final production manifest.  
   **Checks:** every delivered clip traces to its source and selected take; factual additions return through the existing research/review process.  
   **Failure/fix:** later regeneration differs → retain the accepted audio as the reproducible artifact. Parameters alone cannot guarantee identical synthesis.

## Script format spec

The following is the proposed content of `docs/scene-script-format.md`. This is a **project format**, not a native Sudowrite or ElevenLabs import format.

| Element | Required syntax and behavior |
|---|---|
| Encoding | UTF-8 plain text. One physical line per turn or metadata item. No Markdown fences in the saved script. |
| Scene boundary | `@@scene s001`; lowercase ASCII letters, digits, `_` and `-`, maximum 80 characters. IDs must be unique. Each identifies one output request. |
| Scene date | `@@date 2026-09-30`, before scene content. The date is metadata, never spoken. |
| Speaker | `Mori Calliope :: text`; exact canonical card/voice-map name. No aliases, combined speakers or inferred attribution. |
| Tags | One to three directions in the original spoken turn, immediately before affected words. `[casual, fast]` is one complete palette entry; the converter does not automatically permit its components separately. |
| Allowed palette | Bracketed directions in performance-sheet sections **2, 4 and 5**. Section 7 prohibitions and section 8 examples do not grant permission. Case and repeated whitespace are normalized for comparison. |
| Nonverbal sound | A permitted sound tag such as `[laughs]` can occupy a whole turn. Do not also write its vocalization. Duplicate detection is heuristic and requires listening review. |
| Spoken interjection | Write the intended word once with an appropriate delivery direction. The project’s distinction between an interjection and a nonverbal sound is not an acoustic guarantee. |
| Narration | `narrator :: text`, always untagged. Default: excluded from synthesis. `--narrator include` routes it through the map’s `narrator` voice. |
| Stage direction | `STAGE :: description`; retained for the director, excluded from synthesis. Parenthetical directions placed inside a spoken turn remain speech input. |
| SFX | `SFX :: cue description`; excluded from dialogue generation and implemented during assembly. |
| Precise pause | `PAUSE :: 0.4`, in seconds, greater than zero and at most 60. An assembly instruction, not SSML or an API timing guarantee. Conversational pauses within speech use punctuation. |
| Japanese | Spoken text retains Japanese characters. Immediately follow it with `ROMAJI :: ...`; optional `GLOSS :: ...`. Neither is synthesized. Other intended code-switching remains in the spoken turn. |
| Pronunciation override | Prefer a tested versioned dictionary. A tested inline `/IPA/` substitution is allowed; do not append IPA as a second spoken copy of the name. |
| Turn length | Aim below 500 characters including tags. Longer turns are split at sentence/space/Japanese-character boundaries. Tags and slash-delimited pronunciation spans remain intact. Directions are not automatically replayed on continuation fragments. |
| Request length | Project ceiling: 2,000 aggregate text units, conservatively counted as UTF-16 units; ten unique voice IDs maximum. A longer scene must become successive IDs such as `s001a`, `s001b`. |
| Interruptions/overlap | Separate speaker turns remain ordered. Use punctuation for a cut-off; put intentional overlap instructions in STAGE and implement precise overlap during assembly. |
| Comments | `# note`; not spoken. Use a comment to label calibration material as `Style demo: invented lines, not quotations.` |
| Explicit-content marker | Any `【Sudowrite 處理】` marker blocks conversion. It is a hold marker, not material to synthesize. |

Short **Style demo—entirely invented, not quotations**:

```text
@@scene demo
@@date 2026-09-30
# Style demo: invented calibration lines, not quotations.
STAGE :: A game map appears.
Mori Calliope :: [hesitant] Okay, whose map is this?
AZKi :: [mock-dignified] これは練習です。
ROMAJI :: Kore wa renshū desu.
GLOSS :: This is practice.
PAUSE :: 0.4
narrator :: The cursor stops.
Mori Calliope :: [laughs]
```

Proposed `framework/templates/audio-scene-prompt.txt`:

```text
Draft the supplied scene in the novel-lab scene-script format.

Return plain text only, without Markdown fences or an explanatory preface.
Begin with @@scene followed by the supplied unique scene ID, then @@date YYYY-MM-DD.
Use each participant's exact supplied canonical name followed by " :: ".
Write one speaker per physical line. Put one to three directions from that
speaker's Audio Tags trait inside each original spoken turn.
Use "narrator :: " for untagged narration.
Use separate STAGE, SFX and PAUSE metadata lines; never put production
instructions inside words intended to be spoken.
After a Japanese turn, add ROMAJI metadata and optionally GLOSS metadata.
Keep romanization and translations out of the spoken turn.
Use a sound tag without also spelling out the same nonverbal sound.
Keep each audio scene below 2,000 characters including tags and punctuation.
When more space is needed, use successive scene IDs at a natural dramatic boundary.
Preserve established wording habits and uncensored profanity without forcing them.
Treat all newly written dialogue as fictional dialogue, not a real quotation.
Use only the supplied public-persona facts and author-approved fictional premise.
Do not add prohibited private-life information or imitation instructions.
For any held explicit-content scene, output only the non-explicit handoff marker
【Sudowrite 處理】; it must not proceed to audio conversion.
```

Proposed replacement Style block, **105 whitespace-delimited words**:

> Write dialogue for original designed voices, never to reproduce a member's identifiable voice. Follow the supplied scene-script format and exact speaker names. Put one to three listed Audio Tags inside each spoken turn, before the affected words. Preserve established fillers, restarts, repetitions, code-switching and uncensored swears when the scene warrants them. Use tags alone for nonverbal sounds; do not also spell out the same sound. Spoken interjections remain words with delivery directions. Keep narration untagged. Put stage directions, sound effects, romanization and glosses on separate metadata lines. Use punctuation for conversational pauses. Tags are provisional until tested. Write English dialogue with Japanese phrases where specified.

## Converter

Proposed `novel-lab/tools/scene_to_elevenlabs.py` follows. It makes **no network calls**, accepts no keys, refuses overwrites, and validates all scenes before writing outputs.

The JSON contains only request-body fields. Endpoint, output-format query, credentials and take records belong to the director’s generation client. Per-voice settings are deliberately not serialized using an unverified request shape.

```python
#!/usr/bin/env python3
"""Convert the novel-lab scene format to offline Eleven v4 request bodies."""
import argparse
import datetime
import hashlib
import json
import re
import sys
import unicodedata
from pathlib import Path

TAG = re.compile(r"\[([^\[\]\n]+)\]")
JAPANESE = re.compile(r"[\u3040-\u30ff\u3400-\u9fff]")
SCENE_ID = re.compile(r"[a-z0-9][a-z0-9_-]{0,79}")
RESERVED = {"STAGE", "SFX", "PAUSE", "ROMAJI", "GLOSS"}
MARKER = "【Sudowrite 處理】"
# Heuristics, not linguistic proof. A director must review every warning.
DUPLICATES = [
    (r"(?:laughs?(?: harder)?|laughing|giggles?|giggling|chuckles?|chuckling)",
     r"\b(?:ha(?:[\s,-]*ha)+|he(?:[\s,-]*he)+|laughs?|giggles?|chuckles?)\b"),
    (r"(?:sighs?|sighing)", r"\b(?:sighs?|sighing)\b"),
    (r"(?:gasps?|gasping)", r"\b(?:gasps?|gasping)\b"),
    (r"(?:sobs?|sobbing|crying)", r"\b(?:sobs?|sob(?:[\s,-]*sob)+)\b"),
    (r"(?:screams?|screaming)", r"\b(?:screams?|a{3,}h*)\b"),
    (r"(?:snorts?|snorting)", r"\b(?:snorts?|snorting)\b"),
]


def norm(tag):
    return " ".join(tag.split()).casefold()


def unique_object(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise ValueError("Duplicate JSON key: " + key)
        out[key] = value
    return out


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8-sig"),
                      object_pairs_hook=unique_object)


def sheet_policy(text):
    """Only positive sections 2, 4 and 5; never examples or Don't."""
    title = re.search(r"^# ElevenLabs v4 Performance Sheet: (.+)$", text, re.M)
    if not title:
        return None
    allowed = set()
    for number in (2, 4, 5):
        section = re.search(
            r"^## " + str(number) + r"\.[^\n]*\n(.*?)(?=^## |\Z)",
            text, re.M | re.S)
        if section:
            allowed.update(norm(t) for t in TAG.findall(section.group(1)))
    if not allowed:
        raise ValueError("No positive tag palette for " + title.group(1))
    return title.group(1).strip(), allowed


def load_policies(directory):
    policies, hashes = {}, {}
    for path in sorted(directory.glob("*.md")):
        data = path.read_bytes()
        policy = sheet_policy(data.decode("utf-8-sig"))
        if policy is None:
            continue
        name, tags = policy
        if name in policies:
            raise ValueError("Duplicate performance sheet for " + name)
        policies[name] = tags
        hashes[name] = hashlib.sha256(data).hexdigest()
    return policies, hashes


def parse_script(text):
    if MARKER in text:
        raise ValueError("HOLD: marked scene cannot enter audio conversion")
    scenes, current, last_turn = [], None, None
    ids = set()
    for number, raw in enumerate(text.splitlines(), 1):
        line = raw.strip()
        if not line:
            continue
        if line.startswith("#"):
            if current is not None:
                current["events"].append(
                    {"kind": "NOTE", "text": line[1:].strip(), "line": number})
            continue
        if line.startswith("@@scene "):
            name = line[len("@@scene "):].strip()
            if not SCENE_ID.fullmatch(name) or name in ids:
                raise ValueError(f"Line {number}: invalid/duplicate scene ID")
            ids.add(name)
            current = {"id": name, "date": None, "events": []}
            scenes.append(current)
            last_turn = None
            continue
        if current is None:
            raise ValueError(f"Line {number}: content before @@scene")
        if line.startswith("@@date "):
            if current["date"] is not None or any(
                    e["kind"] != "NOTE" for e in current["events"]):
                raise ValueError(f"Line {number}: date must precede scene content")
            value = line[len("@@date "):].strip()
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
                raise ValueError(f"Line {number}: use YYYY-MM-DD")
            datetime.date.fromisoformat(value)
            current["date"] = value
            continue
        if " :: " not in line:
            raise ValueError(f"Line {number}: expected LABEL :: content")
        label, value = line.split(" :: ", 1)
        label, value = label.strip(), value.strip()
        if not value:
            raise ValueError(f"Line {number}: empty content")
        if label in {"ROMAJI", "GLOSS"}:
            if last_turn is None or label in last_turn:
                raise ValueError(f"Line {number}: orphan/duplicate {label}")
            last_turn[label] = value
            continue
        kind = label if label in RESERVED else "TURN"
        if kind == "PAUSE":
            if not re.fullmatch(r"\d+(?:\.\d+)?", value) or not 0 < float(value) <= 60:
                raise ValueError(f"Line {number}: PAUSE must be 0 < seconds <= 60")
        event = {"kind": kind, "speaker": label, "text": value, "line": number}
        current["events"].append(event)
        last_turn = event if kind == "TURN" else None
    if not scenes:
        raise ValueError("No scenes")
    for scene in scenes:
        if scene["date"] is None:
            raise ValueError(scene["id"] + ": missing @@date")
    return scenes


def check_text(text, allowed, location, require_tag=False):
    tags = [norm(t) for t in TAG.findall(text)]
    plain = TAG.sub("", text)
    if "[" in plain or "]" in plain:
        raise ValueError(location + ": malformed/nested brackets")
    if re.search(r"<[^>]*>", text):
        raise ValueError(location + ": XML/SSML is outside this format")
    unknown = set(tags) - allowed
    if unknown:
        raise ValueError(location + ": unlisted tags: " + ", ".join(sorted(unknown)))
    warnings = []
    if require_tag and not tags:
        raise ValueError(location + ": spoken turn needs a listed delivery tag")
    if len(tags) > 3:
        warnings.append(location + ": more than three directions")
    if not plain.strip() and not any(
            re.fullmatch(kind, tag) for kind, _ in DUPLICATES for tag in tags):
        raise ValueError(location + ": delivery-only turn has no spoken text")
    for tag in tags:
        for kind, spelled in DUPLICATES:
            if re.fullmatch(kind, tag) and re.search(spelled, plain, re.I):
                warnings.append(location + ": possible duplicate nonverbal " + tag)
    return warnings


def split_turn(text, maximum):
    """Preserve order and protected tags/IPA; trim only boundary whitespace."""
    protected = [(m.start(), m.end()) for m in
                 re.finditer(r"\[[^\[\]\n]+\]|/[^/\n]+/", text)]

    def safe(position):
        if any(a < position < b for a, b in protected):
            return False
        return (position == len(text) or
                (not unicodedata.combining(text[position]) and
                 text[position] != "\u200d" and text[position - 1] != "\u200d"))

    sentence = [m.end() for m in re.finditer(
        r'(?:[.!?](?:["”’])?(?=\s|$)|[。！？…](?:["”’」』])?)', text)]
    spaces = [m.end() for m in re.finditer(r"\s+", text)]
    japanese = [i for i in range(1, len(text)) if JAPANESE.search(text[i - 1:i])]
    groups = [[i for i in points if safe(i)] for points in (sentence, spaces, japanese)]
    pieces, start = [], 0
    while len(text) - start > maximum:
        cut = None
        for points in groups:
            possible = [i for i in points if start < i <= start + maximum]
            if possible:
                cut = max(possible)
                break
        if cut is None:
            raise ValueError("Unsplittable token exceeds turn limit; edit the source")
        piece = text[start:cut].strip()
        if not piece:
            raise ValueError("Cannot split an empty turn")
        pieces.append(piece)
        start = cut
        while start < len(text) and text[start].isspace():
            start += 1
    if text[start:].strip():
        pieces.append(text[start:].strip())
    return pieces


def valid_voice_id(value):
    return (isinstance(value, str) and
            re.fullmatch(r"[A-Za-z0-9_-]+", value) is not None and
            value.casefold() not in {"todo", "pending", "placeholder"})


def compile_script(text, voices, policies, *, narrator="exclude",
                   max_turn=500, seed=None, dictionaries=None, lint_only=False):
    if not isinstance(voices, dict) or any(
            not isinstance(v, str) for k, v in voices.items() if k != "_about"):
        raise ValueError("Voice map must be speaker -> voice_id strings")
    if not 80 <= max_turn <= 2000:
        raise ValueError("max_turn must be between 80 and 2000")
    if seed is not None and (type(seed) is not int or not 0 <= seed <= 4294967295):
        raise ValueError("seed must be an integer from 0 through 4294967295")
    dictionaries = [] if dictionaries is None else dictionaries
    if not isinstance(dictionaries, list) or len(dictionaries) > 3:
        raise ValueError("Dictionary locators must be a list of at most three")
    for item in dictionaries:
        if (not isinstance(item, dict) or
            set(item) != {"pronunciation_dictionary_id", "version_id"} or
            any(not isinstance(v, str) or not v.strip() for v in item.values())):
            raise ValueError("Each dictionary needs pronunciation_dictionary_id and version_id")

    products, warnings = {}, []
    for scene in parse_script(text):
        inputs, used = [], {}
        listening = [f"SCENE {scene['id']} | DATE {scene['date']}",
                     "MODEL eleven_v4 | request order below",
                     "STAGE/SFX/PAUSE/ROMAJI/GLOSS/NOTE are not synthesized."]
        for event in scene["events"]:
            kind, value, line = event["kind"], event["text"], event["line"]
            if kind != "TURN":
                listening.append(f"L{line} {kind} :: {value}")
                continue
            speaker = event["speaker"]
            location = f"{scene['id']}:L{line}:{speaker}"
            if speaker == "narrator":
                if TAG.search(value):
                    raise ValueError(location + ": narration must be untagged")
                if narrator == "exclude":
                    listening.append(f"L{line} OMITTED narrator :: {value}")
                    for key in ("ROMAJI", "GLOSS"):
                        if key in event:
                            listening.append(f"    {key} (not spoken) :: {event[key]}")
                    continue
                allowed = set()
            else:
                if speaker not in policies:
                    raise ValueError(location + ": no matching performance sheet")
                allowed = policies[speaker]
            if speaker not in voices:
                raise ValueError(location + ": missing speaker in voice map")
            voice_id = voices[speaker]
            if not valid_voice_id(voice_id):
                if not lint_only:
                    raise ValueError(location + ": unresolved/invalid voice_id")
                warnings.append(location + ": voice_id pending; lint only")
            used[speaker] = voice_id
            warnings.extend(check_text(value, allowed, location, speaker != "narrator"))
            if JAPANESE.search(TAG.sub("", value)) and "ROMAJI" not in event:
                raise ValueError(location + ": Japanese text requires ROMAJI metadata")
            pieces = split_turn(value, max_turn)
            if len(pieces) > 1:
                warnings.append(location + ": split turn; check delivery at every join")
            for index, piece in enumerate(pieces, 1):
                check_text(piece, allowed, location)
                inputs.append({"text": piece, "voice_id": voice_id})
                listening.append(
                    f"{len(inputs):03d} L{line} {speaker} part {index}/{len(pieces)}"
                    f" | voice_id={voice_id}\n    {piece}")
            for key in ("ROMAJI", "GLOSS"):
                if key in event:
                    listening.append(f"    {key} (not spoken) :: {event[key]}")
        if not inputs:
            raise ValueError(scene["id"] + ": no audio turns")
        total = sum(len(item["text"].encode("utf-16-le")) // 2 for item in inputs)
        if total > 2000:
            raise ValueError(
                f"{scene['id']}: {total} characters; split at a dramatic boundary "
                "into separate @@scene IDs, each <= 2000")
        if len(set(used.values())) > 10:
            raise ValueError(scene["id"] + ": more than ten unique voice IDs")
        if not lint_only and len(set(used.values())) != len(used):
            raise ValueError(scene["id"] + ": distinct speakers need distinct designed voices")
        body = {"model_id": "eleven_v4", "inputs": inputs}
        if seed is not None:
            body["seed"] = seed
        if dictionaries:
            body["pronunciation_dictionary_locators"] = dictionaries
        listening.append(f"TOTAL {total} characters | {len(inputs)} inputs")
        products[scene["id"]] = (body, "\n".join(listening) + "\n")
    return products, warnings


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("script", type=Path)
    ap.add_argument("--voice-map", required=True, type=Path)
    ap.add_argument("--sheets", required=True, type=Path)
    ap.add_argument("--out", type=Path)
    ap.add_argument("--narrator", choices=("exclude", "include"), default="exclude")
    ap.add_argument("--max-turn", type=int, default=500)
    ap.add_argument("--seed", type=int)
    ap.add_argument("--dictionaries", type=Path)
    ap.add_argument("--lint-only", action="store_true")
    ap.add_argument("--allow-warnings", action="store_true")
    args = ap.parse_args()
    try:
        if not args.sheets.is_dir():
            raise ValueError("Sheets directory does not exist")
        voices = read_json(args.voice_map)
        policies, sheet_hashes = load_policies(args.sheets)
        script = args.script.read_text(encoding="utf-8-sig")
        dictionaries = read_json(args.dictionaries) if args.dictionaries else None
        products, warnings = compile_script(
            script, voices, policies, narrator=args.narrator,
            max_turn=args.max_turn, seed=args.seed, dictionaries=dictionaries,
            lint_only=args.lint_only)
        for warning in warnings:
            print("WARNING: " + warning, file=sys.stderr)
        if warnings and not args.allow_warnings:
            raise ValueError("Review warnings; edit the script or use --allow-warnings")
        if args.lint_only:
            print(f"Lint complete: {len(products)} scene(s); no requests written")
            return 0
        if args.out is None:
            raise ValueError("--out is required unless --lint-only")
        provenance = {
            "converter_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "script_sha256": hashlib.sha256(args.script.read_bytes()).hexdigest(),
            "voice_map_sha256": hashlib.sha256(args.voice_map.read_bytes()).hexdigest(),
            "sheet_sha256": sheet_hashes,
            "narrator": args.narrator, "max_turn": args.max_turn,
            "warnings": warnings,
        }
        files = {}
        for scene_id, (body, listening) in products.items():
            files[scene_id + ".json"] = json.dumps(body, ensure_ascii=False, indent=2) + "\n"
            files[scene_id + ".listening.txt"] = (
                listening + "\nBUILD RECORD\n" +
                json.dumps(provenance, ensure_ascii=False, indent=2) + "\n")
        # Preflight every target before creating any output. Never overwrite.
        for filename in files:
            if (args.out / filename).exists():
                raise ValueError("Output already exists: " + str(args.out / filename))
        args.out.mkdir(parents=True, exist_ok=True)
        for filename, content in files.items():
            with (args.out / filename).open("x", encoding="utf-8", newline="\n") as fh:
                fh.write(content)
        print(f"Wrote {len(products)} request(s) and listening sheets")
        return 0
    except (OSError, UnicodeError, ValueError) as exc:
        print("ERROR: " + str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
```

Minimal executable test, including sample input and expected JSON, for `novel-lab/tools/test_scene_to_elevenlabs.py`:

```python
"""Offline smoke/regression test; no files or network."""
from scene_to_elevenlabs import compile_script, sheet_policy

voice_map = {"Mori Calliope": "original_voice_A", "AZKi": "original_voice_B"}
sheets = [
    "# ElevenLabs v4 Performance Sheet: Mori Calliope\n"
    "## 4. Tag palette by situation\n[hesitant]\n"
    "## 5. Signature sounds\n[laughs]\n"
    "## 7. Don't\n[angry]\n",
    "# ElevenLabs v4 Performance Sheet: AZKi\n"
    "## 4. Tag palette by situation\n[mock-dignified]\n"
]
palettes = dict(sheet_policy(text) for text in sheets)
script = """@@scene demo
@@date 2026-09-30
# Style demo: invented lines, not quotations.
STAGE :: A game map appears.
Mori Calliope :: [hesitant] Okay, whose map is this?
AZKi :: [mock-dignified] これは練習です。
ROMAJI :: Kore wa renshū desu.
GLOSS :: This is practice.
PAUSE :: 0.4
narrator :: The cursor stops.
Mori Calliope :: [laughs]
"""
expected = {
    "model_id": "eleven_v4",
    "inputs": [
        {"text": "[hesitant] Okay, whose map is this?", "voice_id": "original_voice_A"},
        {"text": "[mock-dignified] これは練習です。", "voice_id": "original_voice_B"},
        {"text": "[laughs]", "voice_id": "original_voice_A"}
    ]
}
result, warnings = compile_script(script, voice_map, palettes)
assert result["demo"][0] == expected
assert not warnings
assert "Kore wa renshū desu." in result["demo"][1]
assert "PAUSE :: 0.4" in result["demo"][1]
assert "angry" not in palettes["Mori Calliope"]
for broken in (
    script.replace("[hesitant]", "[unknown]"),
    script.replace("Mori Calliope ::", "Calli ::"),
    script.replace("ROMAJI :: Kore wa renshū desu.\n", ""),
    script.replace("@@scene demo", "@@scene ../../escape"),
):
    try:
        compile_script(broken, voice_map, palettes)
    except ValueError:
        pass
    else:
        raise AssertionError("Invalid script was accepted")
_, warnings = compile_script(
    script.replace("[laughs]", "[laughs] Ha ha!"), voice_map, palettes)
assert any("duplicate nonverbal" in warning for warning in warnings)
print("PASS")
```

Example invocation from the repository root:

`python3 tools/scene_to_elevenlabs.py production/story/scenes/s001.scene.txt --voice-map production/story/voice-map.json --sheets projects/holoen/export/elevenlabs --out production/story/requests/r01`

For a delivered package, use its `performance/tools/scene_to_elevenlabs.py` and `performance/sheets/`. Add `--narrator include`, `--seed 17`, or `--dictionaries production/story/pronunciation-locators.json` as applicable. `--allow-warnings` records acknowledged warnings; it does not bypass errors.

**Verification performed:** executed the converter and test in memory without writing files; loaded all 33 actual sheet palettes; checked malformed tags, unknown speakers, placeholder/duplicate voice IDs, narration inclusion, dictionary locators, seed, splitting, protected pronunciation spans, excess speakers, oversized requests and the explicit-content marker. The final code also passed the conservative UTF-16 budget check.

**Limits:** the converter cannot verify that an ID exists, belongs to the director or represents an original voice. It does not establish quote provenance, pronunciation correctness or policy compliance. Nonverbal duplication detection covers common forms, not every possible vocalization.

## Package gap analysis

Paths below are relative to `novel-lab/`. `∅` means a new file. References to a complete block above specify its verbatim contents without Markdown fences; they are not requests to invent missing implementation. Apply source changes first, then regenerate CSV/paste outputs and review sheet freshness.

| ID | Priority | File + section | Exact old text | Problem | Exact replacement | Evidence |
|---|---|---|---|---|---|---|
| WF-001 | P0 | `tools/scene_to_elevenlabs.py` | ∅ | No deterministic script-to-request handoff. | Complete first Python block in **Converter**, verbatim. | Offline tests reported above; [dialogue API](https://elevenlabs.io/docs/api-reference/text-to-dialogue/convert). |
| WF-002 | P1 | `tools/test_scene_to_elevenlabs.py` | ∅ | No executable conversion fixture. | Complete second Python block in **Converter**, verbatim. | Executed in memory: PASS. |
| WF-003 | P0 | `docs/scene-script-format.md` | ∅ | Speaker attribution, metadata and audio boundaries are unspecified. | The **Script format spec** section above, from its opening paragraph through the demo script, excluding the later prompt and replacement Style block. | Project integration requirement. |
| WF-004 | P1 | `framework/templates/audio-scene-prompt.txt` | ∅ | Style alone cannot carry the complete grammar. | Complete `audio-scene-prompt.txt` block above, verbatim. | [Draft Extra Instructions](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/scenes--draft/49p5MTVxTKkVFEC5rVUzpY). |
| WF-005 | P1 | `projects/holoen/export/elevenlabs/sudowrite-style.md`, fenced Style block | Write dialogue for original designed voices, never to reproduce a member's identifiable voice. Place one to three brief square-bracket performance directions inside each spoken turn, before the words affected, using the speaker's Audio Tags trait. Change delivery only when the scene warrants it. Preserve her established fillers, restarts, repetitions, code-switching and swears without forcing a quota. Distinguish spoken interjections ([startled squawk] GWAK!) from nonverbal sounds ([laughs]); never render the same sound twice. Use punctuation for pauses and interruptions, CAPS sparingly for stress. Keep narration untagged. Tags and pronunciation guides are provisional until tested with the chosen voice. Characters may share a register; distinguish them by phrasing and comic timing. | Does not specify the structured handoff or excluded reading notes. | Write dialogue for original designed voices, never to reproduce a member's identifiable voice. Follow the supplied scene-script format and exact speaker names. Put one to three listed Audio Tags inside each spoken turn, before the affected words. Preserve established fillers, restarts, repetitions, code-switching and uncensored swears when the scene warrants them. Use tags alone for nonverbal sounds; do not also spell out the same sound. Spoken interjections remain words with delivery directions. Keep narration untagged. Put stage directions, sound effects, romanization and glosses on separate metadata lines. Use punctuation for conversational pauses. Tags are provisional until tested. Write English dialogue with Japanese phrases where specified. | Fits the existing 120-word soft target; preserves V17’s required phrases. |
| WF-006 | P0 | Same file, Notes | - Before sending to ElevenLabs, split narration (narrator voice) from dialogue (one voice per character),<br>  and keep each Text to Dialogue request under about 2,000 characters. | Approximate budget; narration choice and speaker cap missing. | - Run the scene converter before generation. Narration is excluded unless `--narrator include` is selected. Each request must satisfy the converter's 2,000-unit budget and ten-voice limit. Longer dramatic scenes use successive audio scene IDs. | [Endpoint limits](https://elevenlabs.io/docs/api-reference/text-to-dialogue/convert). |
| WF-007 | P1 | `docs/elevenlabs-v4.md`, design advice | 好消息：你要的「口吻、習慣、抑揚頓挫」大部分**不在音色裡，而在文字和表演指示裡**，v4 正好最擅長這個。<br>做法是：用 Voice Design 做一個**原創聲音**，只取她的「音域和能量」（例如 Calli＝低的女中音、講話快），<br>然後把她的說話習慣全部寫進腳本和標籤。 | Encourages deriving a design from member voice characteristics. | Voice Design briefs define independent fictional voices. Choose articulation, texture and emotional range for the scene without matching a member's identifiable voice or measured vocal characteristics. Public-persona wording habits belong in the script; performance directions remain proposed and subject to audition. | Task’s original-voice rule; [Use Policy](https://elevenlabs.io/use-policy). |
| WF-008 | P1 | Same file, mapping table | 實測音高／語速（[ASR] 量測）、Voice & Delivery | Routes measurements into synthesis design. | Independent original-voice design brief; scoped Voice & Delivery directions | Task prohibits synthesis targets derived from pitch/F0 or speaking-rate measurements. |
| WF-009 | P1 | Same table, corresponding destination cell | **Voice Design 描述**（原創聲音的音域、能量、語速） | Keeps the measurement-derived mapping after WF-008. | **Voice Design prompt** (independently selected texture, articulation and emotional range) | Same. |
| WF-010 | P1 | Same file, workflow generation step | 4. **生成**：多人場景用 Text to Dialogue（每次 2,000 字元以內），單人長段用 Text to Speech 或 Studio；<br>   同一場景盡量一次生成，讓 v4 讀到上下文。每段生成幾個版本挑最好的；需要一致時用 seed。 | Does not distinguish dramatic scenes from bounded requests or establish reproducibility records. | 4. **Generate:** convert each bounded audio scene to a request with explicit `model_id: eleven_v4`. Retain the generated JSON and listening sheet. Record the endpoint, output-format query, actual settings, dictionary versions, seed, generation date, request ID and selected take. Split long scenes at dramatic boundaries. A seed does not guarantee identical audio. | [Quickstart](https://elevenlabs.io/docs/eleven-api/guides/cookbooks/text-to-dialogue), [API](https://elevenlabs.io/docs/api-reference/text-to-dialogue/convert). |
| WF-011 | P1 | Same file, limitations | - 跨語言時口音會變成母語口音：Calli 講日語可能太標準；需要「美國人講日語」的感覺就加標籤試。 | Converts a model behavior discussion into a performer-language inference. | - Audition cross-language delivery with the original designed voice. Accent directions describe audible fictional performance only; they establish no nationality, mother tongue or personal language history. | Binding scope; [v4 language behavior](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4). |
| WF-012 | P1 | `projects/holoen/export/elevenlabs/Mori-Calliope.md`, section 7 | flawless native Japanese<br>  (her Japanese should sound learned); | Personal-language inference in synthesis directions. | DELETE | Task’s scope rules. |
| WF-013 | P1 | `projects/holoen/bible/characters/Mori-Calliope.md`, Audio Tags | (learned, not native) | Same inference in the source card. | (a proposed accent feature for the original designed voice) | Task permits accents only as voice features. |
| WF-014 | P1 | Same field | Kobo [dad-like, exasperated] | Family-role shorthand is unnecessary in this workflow. | Kobo [exasperated] | Binding scope; retains a non-biographical scene direction. |
| WF-015 | P1 | `projects/holoen/export/elevenlabs/Mori-Calliope.md`, before section 5 | ## 5. Signature sounds | Card-listed directions are absent from the parsed sheet palette. | Additional proposed scene directions, untested: `[American-accented Japanese]`, `[confident]`, `[exasperated]`, `[groaning at the pun]`, `[gruff, deflecting]`, `[gruff, embarrassed]`, `[loud, chaotic]`, `[mock-feuding, smug]`, `[softening, warm]`, `[starstruck, flustered, polite Japanese]`, `[warm]`.<br><br>## 5. Signature sounds | Direct card/sheet set comparison; apply WF-014 first. These are scene proposals, not observed partner defaults. |
| WF-016 | P1 | `projects/holoen/export/elevenlabs/AZKi.md`, before section 5 | ## 5. Signature sounds | Five card directions are absent from the sheet. | Additional proposed scene directions, untested: `[mock-indignant]`, `[nervous]`, `[playful]`, `[soft, gentle]`, `[triumphant]`.<br><br>## 5. Signature sounds | Direct card/sheet comparison. |
| WF-017 | P1 | `projects/holoen/bible/characters/AZKi.md`, Audio Tags, final clause | Not as default: cold or aloof delivery; constant shouting; a babyish voice. | Four sheet directions are unavailable in the imported Audio Tags field. | Additional proposed scene directions: [indignant, playful]; [mock-dignified]; [mock-flustered]; [mock-menacing]. Not as default: cold or aloof delivery; constant shouting; a babyish voice. | Direct card/sheet comparison. |
| WF-018 | P1 | Performance sheets, section 2 heading | ## 2. Settings (starting points) | Settings can be mistaken for tested endpoint behavior. | ## 2. Settings (untested audition choices; verify endpoint behavior) | No runtime evidence was supplied or generated. |
| WF-019 | P0 | `tools/release.py`, V20 | `    R.add("V20", "not_applicable", "block", "Audio turn handoff", ["no derived turn list in this release"])` | A required handoff is explicitly exempted. | **V20 replacement block below**, verbatim. | Exact source anchor checked; replacement compiled in memory. |
| WF-020 | P1 | `tools/release.py`, V24 | `        st = "warn" if all(r["outcome"] == "not_run" for r in rows) else "pass"`<br>`        R.add("V24", st, "warn", "Runtime evidence", ["statically validated; runtime untested"] if st == "warn" else [])` | Any non-`not_run` result—including failure—can pass. | **V24 replacement block below**, verbatim. | Exact source anchor checked; replacement compiled in memory. |
| WF-021 | P1 | `tools/release.py`, runtime-test initialization | `        for t in ("sudowrite-import", "sudowrite-generation", "elevenlabs-3-line"):` | No Japanese runtime test. | `        for t in ("sudowrite-import", "sudowrite-generation", "elevenlabs-3-line", "elevenlabs-japanese"):` | Required multilingual workflow. |
| WF-022 | P1 | `tools/release.py`, package counts | `                "snapshot": snapshot2, "counts": dict(EXPECT),` | Draft manifest can report target roster counts rather than files actually shipped. | `                "snapshot": snapshot2, "counts": {"characters": len(in_chars), "world": len(in_world), "sheets": len(in_chars)},` | Snapshot contains fewer cards than the complete working sheet roster; builder filters sheets by included cards. |
| WF-023 | P1 | `framework/templates/start-here-en.md` | ∅ | Delivery quick-start is not English and lacks the executable handoff. | Complete content of **Writer’s quick-start** below, excluding that section’s heading. | Task requirement. |
| WF-024 | P1 | `tools/release.py`, START_HERE | `START_HERE = (ROOT / "framework" / "templates" / "start-here-zh.md").read_text(encoding="utf-8")` | Builder still selects the old instructions. | `START_HERE = (ROOT / "framework" / "templates" / "start-here-en.md").read_text(encoding="utf-8")` | Direct source inspection. |
| WF-025 | P1 | `tools/release.py`, package creation | `    (pkg / "performance" / "sheets").mkdir(parents=True)` | Converter, test, grammar, prompt and platform notes are not shipped. | **Package-copy replacement block below**, verbatim. | Existing package layout inspection. |
| WF-026 | P1 | `tools/release.py`, V22 required files | `                "reference/sources-and-claims.jsonl", "reference/coverage.md"]` | New workflow components would not be checked. | `                "reference/sources-and-claims.jsonl", "reference/coverage.md",`<br>`                "performance/tools/scene_to_elevenlabs.py", "performance/tools/test_scene_to_elevenlabs.py",`<br>`                "performance/script-format.md", "sudowrite/scene-prompt.txt",`<br>`                "reference/platform-docs/sudowrite-2026-09.md", "reference/platform-docs/elevenlabs-v4.md"]` | Required delivery files introduced by this task. |
| WF-027 | P1 | `tools/release.py`, V01 input list | `                     ROOT / "tools" / "qa_packets.py", proj / "project.md"]):` | New executable and instruction inputs would not affect the source snapshot. | `                     ROOT / "tools" / "qa_packets.py", proj / "project.md",`<br>`                     ROOT / "tools" / "scene_to_elevenlabs.py", ROOT / "tools" / "test_scene_to_elevenlabs.py",`<br>`                     ROOT / "docs" / "scene-script-format.md", ROOT / "docs" / "sudowrite-2026-09.md",`<br>`                     ROOT / "docs" / "elevenlabs-v4.md", ROOT / "framework" / "templates" / "audio-scene-prompt.txt",`<br>`                     ROOT / "framework" / "templates" / "start-here-en.md"]):` | Existing snapshot hashes omit these inputs. |
| WF-028 | P1 | `docs/elevenlabs-v4.md`, pronunciation mapping | **IPA** 或拼音式寫法；日語片語直接寫 | Does not distinguish spoken text, reading notes and reusable rules. | Tested dictionary rules or an audited inline IPA substitution; Japanese characters remain in spoken text, while romanization and glosses stay in non-spoken metadata. `pronunciation.tsv` is an incomplete provisional index; consult every relevant sheet's section 6, including Japanese reading guides. | `pronunciation_rows()` only extracts the IPA-formatted clause and omits reading-guide-only entries. |
| WF-029 | P2 | `docs/sudowrite-2026-09.md`, immediately before sources | ## 來源 | No explicit integration boundary or uncertainty record. | ## Workflow integration note — checked 2026-10-02<br><br>The supported package handoff is CSV/paste into Sudowrite, then a UTF-8 scene script passed to the offline converter. No documented public Sudowrite API was located. Do not assume direct ElevenLabs integration or guaranteed preservation of script syntax by prose tools. Record the actual model selected for each generation. Official downloadable CSV templates and the complete current experimental-model selector were not reverified in this check.<br><br>## 來源 | Official documentation check and disclosed coverage. |

V20 replacement:

```python
    from scene_to_elevenlabs import TAG as AUDIO_TAG, norm as audio_norm, load_policies
    handoff_errors = []
    try:
        palettes, _ = load_policies(sheets_dir)
        for stem, card in chars.items():
            name = card["fields"]["Name"]
            missing_tags = {audio_norm(t) for t in AUDIO_TAG.findall(
                card["fields"].get("Audio Tags", ""))} - palettes.get(name, set())
            if name not in palettes or missing_tags:
                handoff_errors.append(f"{stem}: missing sheet/palette tags {sorted(missing_tags)}")
        smoke = subprocess.run(
            [sys.executable, str(ROOT / "tools" / "test_scene_to_elevenlabs.py")],
            capture_output=True, text=True)
        if smoke.returncode:
            handoff_errors.append(smoke.stderr or smoke.stdout or "converter test failed")
    except (OSError, ValueError) as exc:
        handoff_errors.append(str(exc))
    R.add("V20", "fail" if handoff_errors else "pass", "block",
          "Audio turn handoff", handoff_errors or ["converter fixture and card-to-sheet palettes passed"])
```

V24 replacement:

```python
        required_tests = {"sudowrite-import", "sudowrite-generation",
                          "elevenlabs-3-line", "elevenlabs-japanese"}
        latest = {r["test"]: r for r in rows}
        failed = sorted(t for t, r in latest.items() if r.get("outcome") == "fail")
        complete = required_tests <= set(latest) and all(
            latest[t].get("outcome") == "pass" and
            all(latest[t].get(k) for k in ("release", "date", "tester", "model_or_voice", "observations"))
            for t in required_tests)
        st = "fail" if failed else ("pass" if complete else "warn")
        R.add("V24", st, "block" if failed else "warn", "Runtime evidence",
              [f"failed tests: {failed}"] if failed else
              ([] if complete else ["required runtime evidence incomplete; do not label runtime-tested"]))
```

Package-copy replacement:

```python
    (pkg / "performance" / "sheets").mkdir(parents=True)
    (pkg / "performance" / "tools").mkdir()
    for filename in ("scene_to_elevenlabs.py", "test_scene_to_elevenlabs.py"):
        shutil.copy2(ROOT / "tools" / filename, pkg / "performance" / "tools" / filename)
    shutil.copy2(ROOT / "docs" / "scene-script-format.md",
                 pkg / "performance" / "script-format.md")
    shutil.copy2(ROOT / "framework" / "templates" / "audio-scene-prompt.txt",
                 pkg / "sudowrite" / "scene-prompt.txt")
    (pkg / "reference" / "platform-docs").mkdir(parents=True)
    for filename in ("sudowrite-2026-09.md", "elevenlabs-v4.md"):
        shutil.copy2(ROOT / "docs" / filename,
                     pkg / "reference" / "platform-docs" / filename)
```

**Integration order:** add the tool/spec/template files; reconcile scoped card and sheet directions; regenerate exports; review and stamp changed sheets; run existing checks plus the revised V20; build a new candidate. The two representative palettes above are not a claim that all remaining palettes already match—V20 must enumerate those differences for correction.

V13 and V14 remain necessary for quotation and scope review. Successful conversion does not replace them. Runtime records belong in the production workspace; an immutable package initially marked untested stays accurately marked until a subsequent release explicitly incorporates reviewed evidence.

## Writer's quick-start

**Start here — holoen {rev}**  
Baseline: {baseline}. Included: {nchar} characters and {nworld} world elements. Check `manifest.json` for draft status and `validation.json` for unresolved checks. Work in a separate production folder.

**Writer**

1. Import `sudowrite/characters.csv` and `worldbuilding.csv` once into a test project; verify counts and custom traits.
2. Inspect visibility before using AI; Secrets are not automatically hidden.
3. Paste `sudowrite/style.txt`; supply your Braindump and Genre; leave Synopsis empty until ready.
4. Plan the scene date, exact participants, relevant world elements and one concrete change.
5. Supply `sudowrite/scene-prompt.txt` as generation instructions; follow `performance/script-format.md`.
6. Save the result as UTF-8 `scenes/s001.scene.txt`; keep Japanese romanization and glosses outside speech.
7. Lint after every revision. Resolve factual/quotation issues separately; preserve established profanity.
8. Hand the script, plan and provenance notes to the voice director. Update existing cards field by field.

**Voice director**

1. Read the relevant `performance/sheets/`; design independent original voices without member recordings or likeness requests.
2. Save each voice and fill `voice-map.json` with canonical speaker names and persistent voice IDs.
3. Audition speech, an emotional shift, a nonverbal sound and Japanese where relevant; record results.
4. Run `performance/tools/scene_to_elevenlabs.py` with the script, `--voice-map`, `--sheets` and a new `--out` directory.
5. Submit each JSON body through your authorized API client, or follow its listening sheet in the app; select `eleven_v4`.
6. Keep generation settings, dictionary versions, request IDs and every accepted take; listen for spoken tags and duplicate sounds.
7. Assemble pauses, overlaps and SFX from the listening sheet; preserve the accepted speech audio.
8. Deliver the audio with an unofficial-fan-work/synthetic-voice disclosure and archive the production manifest.

**Maintainer**

1. Ship tools, grammar, prompt and platform notes with every package; include them in snapshot hashes.
2. Require card-to-sheet palette checks and converter tests; record runtime failures as failures.
3. Regenerate exports and review changed sheets before stamping them.
4. Keep author promotion decisions separate from technical validation and audio acceptance.

## Risks and policy

**Voice identity:** the project’s rule is stricter than merely obtaining a technically usable voice ID: no cloning, deliberate imitation, member reference audio or matching targets. Do not use member clips in Voice Design, Voice Changer or Actor Mode. ElevenLabs separately prohibits unauthorized replication and harmful or deceptive impersonation. [ElevenLabs Use Policy](https://elevenlabs.io/use-policy)

**Disclosure:** place a clear notice with distributed audio: *“Unofficial fan fiction. Performed with original AI-generated voices; no talent participated in or endorsed this recording.”* This is the proposed project disclosure standard, not a claim that one sentence resolves every jurisdiction’s obligations.

**COVER:** keep applicable works within the guidelines’ permitted fan/hobby scope; avoid misleading official presentation and prohibited harmful content. The express synthetic-speech restriction concerns extracting vocals from songs. It should not be misquoted as a comprehensive statement about every possible synthetic voice; our no-imitation rule covers this project more broadly. [COVER guidelines](https://hololivepro.com/en/terms/)

**Distribution:** an ElevenLabs paid plan does not grant rights to COVER characters or other third-party material. Generated voices are currently not publicly shareable through Voice Library; distribute permitted finished audio and production documentation without promising transferable voice assets. Applicable regional terms and the selected publication route still govern. [Voices documentation](https://elevenlabs.io/docs/overview/capabilities/voices), [Terms](https://elevenlabs.io/terms-of-use)

**Content:** profanity and non-explicit public-persona humor remain intact. Explicit content is not written or included in this audio pipeline; held material receives `【Sudowrite 處理】` without explicit content. The converter rejects that marker. Public-persona evidence must never become private-life inference, and scene directions must never become claims about observed partner behavior.

## Open questions for the author

1. **Primary audio language:** English with Japanese phrases / Japanese with English reading notes?
2. **Narration default:** exclude / include an original narrator voice?
3. **Generation route:** API request files / manual app generation?
4. **Initial delivery:** private listening files / publicly shared hobby fan work?
5. **Assembly preference:** ElevenLabs Studio / external audio editor?
## 1. Agreement and adjustments

**AGREE-WITH-CHANGES.** Keep the proposed architecture, sequential GPT schedule, full-card default, optional historical worksheet, and “statically validated; runtime untested” release label. Deferring the shared Audio Tags rewrite to task 09 is sensible.

I accept dropping the exhaustive `claims.jsonl`, subject to these adjustments:

- **Incoming claims must include aliases, unit names, table rows and list items**, with enough surrounding text to resolve pronouns. Sentence matching alone will miss claims.
- Give every packet a source-file inventory and SHA-256 map. Split oversized packets deterministically; never truncate required coverage. Parallel edits invalidate affected excerpts until reconciled.
- Add **directional credits and relationship records** to the registry where needed for bridge checking. Retain claim locators and evidence references. This remains a bounded registry, not a transcription of every dossier.
- Define `reference/sources-and-claims.jsonl` as an export of registry facts and audited findings, explicitly marked **non-exhaustive**.
- Preserve each sheet’s chosen settings; the scale clarification does not mean changing every character to 55/75.
- Separate **finding priority** from **validation severity**. Runtime unavailability can warn; unresolved P0 findings, stale sheets, and material contradictions block.
- Build a release candidate before task 11. Final publication requires acceptance tied to that candidate’s manifest hash.

Author-decision promotion must remain distinct from GPT approval and source verification. It cannot silently waive the current privacy rules or turn unsupported claims into established facts.

## 2. Complete cohort-audit prompt

Save the following block verbatim as `framework/prompts/gpt-cohort-audit.md`.

```markdown
# Task 04 — Cohort consistency audit

You are GPT, the senior architect and QA reviewer for novel-lab’s holoen project.
Use the project-required GPT-6 model at xhigh. Work read-only and answer in English.
This is a cross-file consistency audit, not another single-card review.
Run sequentially; do not launch parallel GPT audits.

Cohort: {{cohort}}
Packet: {{packet_path}}
Registry: {{registry_path}}

## Binding rules

{{rules}}

Read projects/holoen/project.md and framework/prompts/shared-rules.md.
The supplied task’s stricter scope restrictions also apply. Read the packet,
registry, research/qa/manifest.json and research/qa/resolutions.md when present.
A missing required input is a coverage gap, never permission to invent its contents.

Never read projects/*/runs/, including files linked from otherwise permitted files.
Do not modify files. Return the complete audit in your final response.

The factual baseline is 2026-09-30. Later verification may establish what was true
by that date; it must not silently advance the baseline.

Use only official fictional lore and publicly presented persona behavior.
Exclude the performer’s identity, appearance, past activities, private life,
health, real family, breaks or their reasons, trips, audition history, nationality
and mother tongue—even when publicly discussed. Accents may be described only
as audible voice features. Preserve clearly fictional families, avatar lore,
in-game travel and public event locations without inferring personal travel.

Do not infer intimacy, sexuality, private closeness or hidden psychology.
Preserve supported swearing, crude jokes and performed bits without sanitizing
them or presenting them as real relationships. No lyrics, long transcripts,
explicit sexual material, voice cloning or identifiable real-voice imitation.
Original calibration lines must say “Style demonstration.”

## Ownership and scope

Use the packet inventory to resolve exact paths. Primary ownership is:

- Myth: Calliope, Kiara, Ina, Amelia, Gura; Myth, TakaMori, TakoTori, AmeSame,
  Bone Bros, Myth-and-Kronii Other Pairs.
- Promise: Kronii, IRyS, Fauna, Mumei; Promise, Time Duo, Time and Death,
  OctoClock, Fauna-and-Mumei Pairs, IRyS-and-Nerissa Pairs.
- Advent: Shiori, Bijou, Nerissa, Fuwawa, Mococo; Advent, Advent Pairs, FUWAMOCO.
- Justice: Elizabeth, Gigi, Cecilia, Raora; Justice, Justice Pairs.
- Global: hololive, Streaming Life, VTuber Persona and Lore, Cross-Branch Friends,
  Concerts and Live Events, both History cards.

Together these cover 18 character and 24 world cards. Baelz, Sana and other
external participants may be referenced; do not create their character cards.

Audit the selected cohort’s complete [SW] fields, Relationship Map, Background
Timeline and Hard Facts, plus incoming claims from every other card. Inspect
relevant source passages when needed. Packets are navigation aids, not exclusive
evidence. Search permitted bible files using canonical names, aliases and units;
include table rows, bullets and antecedents needed to interpret pronouns.

Prioritize dates, status, rosters, participants, credits, units, aliases and
directional relationships. Compare outgoing and incoming claims. Missing
reciprocal coverage is not automatically a contradiction.

Do not re-litigate previously reviewed isolated claims unless another file
contradicts them. Log apparent staleness for task 06 or 08; investigate it here
only where necessary to settle current consistency. Flag newly encountered
scope violations immediately. Detailed voice enrichment belongs to task 09.

## Evidence and quotation rules

Classify evidence, independently from claim status:

- OFFICIAL: agency profiles, announcements, event reports and official written
  copy. Quote only short exact written excerpts; distinguish lore from public
  factual announcements. An official video is not automatically a transcript.
- PRIMARY: a member’s public post, stream or other firsthand public material.
  Written posts may be quoted briefly as written. Spoken quotations require
  the ASR gate below. Distinguish performed bits from assertions.
- ARCHIVE_METADATA: title, description, timestamps and explicitly listed credits
  or participants. Quote brief metadata as metadata, never as spoken dialogue.
  Upload dates and scheduled rosters do not alone prove event dates or attendance.
- SECONDARY: wikis, fan transcripts, clips and mirrors. Attribute paraphrases.
  Short quotations of a secondary author’s prose must remain attributed to that
  author; fan transcription cannot establish a member’s exact spoken words.
- ASR: machine transcription of identified public audio. A spoken quote must
  match an explicit contiguous approved span shared by both models for the same
  audio window, with independently supported speaker attribution. Record both
  model names, timestamp, source and approved span. Punctuation/case normalization
  may be documented; never delete repetitions, alter words or stitch separated
  spans. “Agrees” without an explicit span is insufficient. Agreement is not
  human listening and does not establish speaker identity, tone or recurrence.

Keep quotations short; quote no lyrics and no more than 25 words from any one
external non-lyrical source in this audit. Prefer paraphrase plus locators.
Separate Official setting, Public-behavior observation, Author-approved adaptation
and Unverified. Unsupported assertions do not become facts in [SW] fields.

Use existing cited evidence first. Use live search only where files disagree or
a claim appears stale. Prefer official pages, then primary material. Open the
supporting page before claiming fresh verification. Label inherited evidence
“not reopened”; record inaccessible sources and distinguish absence of evidence
from disproof. Give actual checked dates, separately from event dates.

## Procedure and priority

1. Verify packet and registry hashes against their source inventory. Report
   missing, truncated or changed inputs. Reconcile changed passages or mark the
   affected coverage incomplete; never claim a clean audit of mixed snapshots.
2. Group related assertions under existing registry keys. Compare dates with
   zones, status at the relevant date, membership, attendance, unit evidence level,
   naming and directional credits. Keep announcements separate from held events.
3. Preserve older supported bits as shared memory. Use recent eligible evidence
   for present speaking defaults; alumni use their last active period. Historical
   scene status must not be inferred from the present-day roster.
4. Produce minimal exact patches and enumerate every affected file/field.
   Do not rewrite entire cards or add enrichment merely to fill a quota.

Priorities:
P0 — must resolve before delivery: scope breaches, fabricated attribution,
unapproved spoken quotations, or defects preventing a trustworthy usable release.
P1 — priority factual correction, material consistency issue or evidenced coverage gap.
P2 — optional clarity, retrieval or usability improvement.

Priority is separate from release-gate severity. A material contradiction can
block validation even when assigned P1.

“Author decision” means an explicit editorial choice between valid alternatives,
such as optional compression or accepting a disclosed evidence limitation.
It is not model approval, source verification, or permission to override binding
scope. Give a concrete question and recommendation. Do not escalate routine fixes.

IDs: {COHORT}-{TYPE}-{NNN}, with COHORT = MYTH, PROMISE, ADVENT, JUSTICE or GLOBAL.
Use TYPE = DATE, STATUS, EVENT, ROSTER, TIE, CREDIT, UNIT, ALIAS, SCOPE, QUOTE,
VOICE, EXPORT or COVERAGE. Continue numbering from the resolution ledger.
Reuse existing IDs for the same finding; never renumber or duplicate it.
Claim keys identify facts; finding IDs identify problems.

## Exact output format

Use exactly these four top-level headings:

## Coverage

Snapshot hash; packet/registry hashes; source-hash manifest reference; files and
fields examined; incoming-claim search coverage; exclusions; unresolved evidence;
missing inputs; snapshot changes. Distinguish “examined” from “freshly verified.”

## Findings

| ID | Priority | Claim key | File + field/line | Exact old text | Problem | Exact replacement | Evidence URL + type + checked date | Propagate to | Author decision? |
|---|---|---|---|---|---|---|---|---|---|

Use one actionable finding per row. For multi-file changes, add linked patch rows
under the same ID. Copy exact old text; use DELETE for deletion. Preserve field
names and provide paste-ready replacement prose. Escape table pipes and use <br>
for internal newlines. If evidence cannot support replacement facts, propose
deletion or appropriately limited wording. If there are no findings, say “None.”

## New verified facts

Use the same table columns. Use “—” for absent old text and an exact insertion
locator. Include only directly useful facts verified during permitted checking;
otherwise write “None.” Distinguish a sourced candidate from an accepted addition.

## Merge handoff

List dependencies, unresolved conflicts, propagation order, and existing finding
IDs recommended for acceptance, rejection, deferral or further evidence. These
are recommendations, not claims that Claude merged them. Identify required
registry/packet regeneration and downstream audit owners.

End this section with “Open questions” containing at most five genuine author
decisions or unresolved input questions; write “None” when there are none.
```

## 3. Complete bridge-audit prompt

Save the following block verbatim as `framework/prompts/gpt-bridge-audit.md`.

```markdown
# Task 05 — Cross-cohort bridge audit

You are GPT, senior architect and QA reviewer for novel-lab’s holoen project.
Use the project-required GPT-6 model at xhigh. Work read-only, answer in English,
and run sequentially without parallel GPT audits.

Bridge: {{bridge}} — must be events or ties
Packet: {{packet_path}}
Registry: {{registry_path}}

## Binding rules and inputs

{{rules}}

Read projects/holoen/project.md, framework/prompts/shared-rules.md, the packet,
registry, research/qa/manifest.json, research/qa/resolutions.md, and available
research/qa/audit-*.md reports relevant to the bridge. Reports outside runs are
permitted. Never read projects/*/runs/, even through links. Modify no files.

The baseline is 2026-09-30. Use later verification only to establish baseline-era
facts. Cover all 18 character and 24 world cards through relevant cross-file
claims. External participants may remain reference-only; create no new cards.

Use official fictional lore and public persona behavior only. Exclude performer
identity, private appearance, past activities, private life, health, real family,
breaks and reasons, trips, auditions, nationality and mother tongue. Public
disclosure does not remove these exclusions. Describe accents only as audible
features. Distinguish fictional families, avatar lore and in-game travel from
real-life information; public event locations do not establish personal travel.

No inferred intimate relationships, sexuality or hidden psychology; no lyrics,
long transcripts, explicit sexual content, real-voice cloning or identifiable
imitation. Preserve evidenced swearing and performed jokes without sanitizing
them. Label invented calibration lines “Style demonstration.”

Do not reopen isolated claims already reviewed unless they conflict across files.
This audit groups claims by shared event or relationship, checks previous fixes
and catches propagation failures. Broad recency research, X completeness and
detailed voice enrichment belong to tasks 06, 08 and 09. Newly encountered scope
violations must still be reported.

## Evidence and quotation

OFFICIAL means agency profiles, announcements, reports or official written copy.
Short exact written excerpts may be quoted; distinguish lore, announcements and
post-event reporting.

PRIMARY means firsthand public posts, streams or other public material.
Short written posts may be quoted as written. Audio-derived quotations require
the ASR gate below, regardless of channel ownership.

ARCHIVE_METADATA supports only its stated title, description, dates, listed
participants and credits. Quote it as metadata, never dialogue. Scheduled names
do not prove actual participation; upload time does not necessarily date the event.

SECONDARY means wikis, fan transcripts, clips or mirrors. Use attributed
paraphrases. Short quotations of secondary prose remain attributed to its author.
A fan’s transcript cannot establish the performer’s exact spoken words.

ASR is machine transcription, not listening. Spoken quotations require explicit
contiguous approved spans shared by two models transcribing the same public
audio window. Record source, timestamp, both models and separate speaker
attribution. Document punctuation/case normalization only; preserve wording,
repetitions and order. Never stitch separated spans or treat semantic agreement
as verbatim agreement. Two-model agreement cannot establish who spoke, tone,
relationship strength or recurring usage.

No lyrics; keep quotations brief and total external quotations within 25 words
per non-lyrical source. Distinguish Official setting, Public-behavior observation,
Author-approved adaptation and Unverified. Unverified assertions cannot enter
[SW] fields as facts.

Use local evidence first. Search live only to resolve disagreement or apparent
staleness; prefer official pages, then primary sources. Open supporting sources
before claiming fresh verification. Label inherited evidence “not reopened.”
Record inaccessible sources without treating inaccessibility as disproof.
Separate source publication date, event date and actual verification date.

## Common procedure

Check source hashes before auditing and reconcile changes before concluding.
Packets are focus aids: inspect permitted canonical files and related research
when necessary. Match canonical names, aliases and units; inspect complete
bullets/table rows and relevant pronoun antecedents. Report extraction gaps.

Group claims under stable registry keys across cohorts. Check the resolution
ledger before creating findings. Verify implemented changes against canonical
text; a “resolved” label alone proves nothing. Track all propagation destinations.

Treat the registry as an index requiring evidence, not an authority that overrides
sources. Preserve uncertainty and date precision rather than inventing detail.

## If bridge = events

Compare both histories, Concerts, unit cards, character timelines, Background,
Relationships and all other relevant exported claims.

Check event identity; announcement versus event dates; source time zones;
genuine multi-day schedules versus time-zone conversions; scheduled versus held
events; actual participants versus historical unit membership; debut, graduation
and affiliate intervals; date-bound organization names; release and performance
credits; milestone counts.

Do not infer current activity from an old appearance or current unit membership
from historical participation. A later guest appearance need not reverse an
affiliate/graduation status. Record exceptions with evidence.

Check status boundaries at the source’s supported precision. Never invent a
midnight transition or time zone. Describe factual departures without excluded
reasons. Flag optional coverage gaps separately from contradictory dates.

## If bridge = ties

Compare character Relationships and Groups, world descriptions and aliases,
Relationship Maps, concert units and incoming claims across every cohort.

Check canonical endpoints, unit membership, named-event context, official versus
fan/performed naming, alias ownership, and directional verbs: who invited,
supported, credited, performed with or publicly praised whom.

A collaboration supports participation, not private friendship strength.
Do not reverse directional claims, rank closeness by archive counts, infer mutual
feelings or convert a performed pairing into a real relationship.
A missing reciprocal mention is a coverage question, not automatically an error.

Keep multi-person unit aliases on suitable world cards and memberships in Groups;
do not make the unit an individual’s Other Names alias. Review collisions without
automatically deleting valid aliases. Keep Fuwawa and Mococo distinct.

## Priorities, decisions and IDs

P0: resolve before delivery—scope breaches, fabricated attribution, unapproved
spoken quotations, or defects preventing a trustworthy usable release.
P1: priority factual correction, material inconsistency or evidenced coverage gap.
P2: optional clarity, retrieval or usability improvement.

Finding priority does not determine validation severity by itself; material
contradictions can block even when P1.

“Author decision” is an explicit editorial choice between valid alternatives,
including optional enrichment or a disclosed limitation. It is neither GPT
approval nor factual verification, and cannot waive the current scope.
Recommend a concrete choice; handle routine corrections without escalation.

Use BR-{TYPE}-{NNN}: TYPE = DATE, STATUS, EVENT, ROSTER, TIE, CREDIT, UNIT, ALIAS,
SCOPE, QUOTE, VOICE, EXPORT or COVERAGE. Both bridge passes share this namespace.
Continue ledger numbering. Reuse cohort IDs for the same underlying issue;
create a new BR ID only for a distinct cross-cohort problem and link related IDs.

## Exact output format

Use exactly these four top-level headings:

## Coverage

Snapshot hash; packet/registry hashes; source-hash manifest reference; bridge;
files/fields and claim keys examined; cohort findings checked; exclusions;
unresolved evidence; missing inputs; snapshot changes.
Distinguish examined material from freshly verified evidence.

## Findings

| ID | Priority | Claim key | File + field/line | Exact old text | Problem | Exact replacement | Evidence URL + type + checked date | Propagate to | Author decision? |
|---|---|---|---|---|---|---|---|---|---|

One actionable finding per row; use linked patch rows for different replacements
under one ID. Supply exact old text and paste-ready replacements, or DELETE.
Escape pipes; represent internal newlines with <br>. If unsupported, recommend
deletion or limited wording rather than inventing a replacement. Write “None”
when there are no findings.

## New verified facts

Use the identical table columns; absent old text is “—”. Give insertion locators.
Include only useful facts verified during permitted checking. Distinguish
candidates from accepted additions. Otherwise write “None.”

## Merge handoff

List dependencies, unresolved conflicts, propagation order, registry updates,
and finding IDs recommended for acceptance, rejection, deferral or more evidence.
Do not claim edits were applied. Name downstream tasks needing the result.

End with “Open questions”: at most five genuine author decisions or unresolved
input questions, or “None.”
```

## 4. Release validation specification

`validate` should produce machine-readable `validation.json`. Each result needs `check_id`, `status` (`pass/fail/warn/not_applicable`), severity, file/field locator, evidence, finding IDs and input hashes. A missing required semantic review is a failure, not an automatic pass.

Use two phases: **candidate validation**, then **final release validation** including V25. A failed blocking check prevents publication. Warnings remain visible in the manifest. Static validation does not require account credentials or network access.

1. **V01 — Source snapshot.**  
   **Check/how:** Inventory canonical cards, rules, schemas, generator code and performance dependencies; SHA-256 their bytes. Define the snapshot hash as SHA-256 of canonical JSON containing the sorted relative-path/hash map. Recheck before publication.  
   **Pass:** Every reviewed input matches; changed dependencies have been reconciled. **Severity: block.**

2. **V02 — Authorized inventory.**  
   **Check/how:** Compare canonical names, kinds, destinations and counts against the approved inventory.  
   **Pass:** Exactly 18 Characters, 24 Worldbuilding elements and 18 performance sheets; separate twins; reference-only people do not become cards. Any expansion has explicit authorization. **Severity: block.**

3. **V03 — Schema and headings.**  
   **Check/how:** Parse front matter and `[SW]` headings using the configured schema; detect duplicates before constructing dictionaries.  
   **Pass:** Correct kind/section mapping, all required and optional headings present, required values nonempty, names matching front matter, every character Role exactly `Protagonist`. **Severity: block.**

4. **V04 — Placeholders and field names.**  
   **Check/how:** Scan for unresolved template markers, duplicate names, merge debris and unknown fields. Review unknown fields against an explicit custom-trait allowlist.  
   **Pass:** No accidental placeholders, misspelled fields or collisions. Deliberately empty story fields and documented example-map placeholders remain allowed. **Severity: block; unreviewed custom-field candidates warn pending disposition.**

5. **V05 — CSV integrity.**  
   **Check/how:** Strict UTF-8 decoding and CSV parsing; unique headers, uniform row widths and duplicate-row checks. Include meaningful fixtures containing commas, quotes and embedded newlines.  
   **Pass:** Every record parses without loss, shifting or replacement characters. **Severity: block.**

6. **V06 — Export equality.**  
   **Check/how:** Compare parsed canonical fields with combined CSVs, individual CSVs, paste blocks and packaged reference cards. Permit only documented empty-value and newline normalization.  
   **Pass:** Identical values and record sets; no missing, extra or stale exports. Never normalize away wording differences. **Severity: block.**

7. **V07 — Sizes and platform limits.**  
   **Check/how:** Apply the configured counter and versioned limit metadata, recording units and documentation provenance.  
   **Pass:** Documented hard limits respected; local targets reported separately. Braindump/Synopsis are 4,000 words; ordinary trait targets and combined Style’s 120-word target are warnings. Never apply smart-import batch limits to structured CSV. **Severity: block for established hard violations; warn for soft targets or uncertain counting.** [Sudowrite limits](https://feedback.sudowrite.com/en/changelog/three-big-improvements)

8. **V08 — Alias ownership.**  
   **Check/how:** Compare names, aliases and Groups using Unicode normalization, case folding, whitespace and punctuation variants while preserving originals.  
   **Pass:** Every collision/common-word candidate has a disposition; confirmed wrong ownership is fixed. No automatic alias deletion. **Severity: warn for candidates; block for unresolved confirmed defects.**

9. **V09 — Units and retrieval coverage.**  
   **Check/how:** Join unit records to membership fields and appropriate world aliases; inspect official, fan and event-specific classifications.  
   **Pass:** Membership and aliases agree with evidence; multi-person units are not individual aliases. Missing optional reciprocal detail is explicitly classified. **Severity: block for false membership; warn for coverage gaps.**

10. **V10 — Dates, zones and status.**  
    **Check/how:** Validate interval ordering and compare event/status records against audit dispositions. Preserve precision; use half-open intervals only where boundaries are established.  
    **Pass:** No contradictory status at the same supported date; announcements, scheduled events, held events, upload dates and time-zone conversions remain distinct. **Severity: block for contradictions; warn for disclosed unknown precision.**

11. **V11 — Participants and directional facts.**  
    **Check/how:** Join event rosters, relationship endpoints and directed credit records to their cited passages. Require hash-bound bridge-review results.  
    **Pass:** No invented attendance, reversed credit, false “all members,” or unsupported relationship escalation. **Severity: block.**

12. **V12 — Evidence records.**  
    **Check/how:** Validate source URLs, evidence types, checked dates, claim keys and locators for registry facts and audited changes. Mark the evidence export non-exhaustive.  
    **Pass:** Records resolve; inherited, inaccessible and freshly checked evidence are distinguished. **Severity: block for fabricated provenance; warn for disclosed access limitations.**

13. **V13 — Quotations and ASR.**  
    **Check/how:** Match exported spoken quotations to explicit approved spans, both model outputs, shared audio windows and separate speaker attribution. Check written quotations against attributed text.  
    **Pass:** No unsupported wording, stitched spans, inferred speakers, lyrics or mislabeled demonstrations. **Severity: block.**

14. **V14 — Scope screening.**  
    **Check/how:** Scan cards, active supporting research, sheets and release payload, followed by semantic review of candidates. Record review dispositions against hashes.  
    **Pass:** No excluded real-life material; legitimate avatar lore, fictional family and game travel survive. Do not distribute obsolete rejected excerpts merely for completeness. **Severity: block.**

15. **V15 — Card usability and fidelity.**  
    **Check/how:** Consume editorial review attestations for changed fields. Check tense, third-person descriptions, evidence labels and author-facing instructions.  
    **Pass:** Exported prose is usable; uncertain claims are not asserted as facts; supported language is not sanitized. **Severity: block for meaning/scope defects; warn for stylistic improvements.**

16. **V16 — Secrets and visibility.**  
    **Check/how:** Inventory nonempty Secrets and inspect visible fields for duplicated restricted content.  
    **Pass:** This release’s empty values match the guide. Any future nonempty value has explicit pre-generation hiding instructions and reviewed visible clues. **Severity: block for missing controls or misleading instructions.**

17. **V17 — Style handoff.**  
    **Check/how:** Compare the canonical production Style source, `style.txt` and the leading paste-sheet block. Review combined literary/audio Style.  
    **Pass:** Exact agreement; original-voice instruction, spoken/nonverbal distinction and untagged narration retained; unchosen story fields remain blank. **Severity: block; length-target excess warns.**

18. **V18 — Performance freshness and settings.**  
    **Check/how:** Require each sheet’s source-card SHA-256 and additional dependency hashes; compare settings numerically.  
    **Pass:** All match reviewed inputs; updating a hash alone cannot replace review. UI percentages equal API fractions, using each sheet’s chosen values. **Severity: block.** [ElevenLabs settings](https://elevenlabs.io/docs/api-reference/voices/settings/get)

19. **V19 — Voice and pronunciation claims.**  
    **Check/how:** Review original-voice descriptions, provisional pronunciation records and acoustic-measurement usage.  
    **Pass:** No cloning directions or measured F0 treated as a synthesis target; untested pronunciations remain provisional. Unsupported model controls are removed. **Severity: block for false instructions; warn for disclosed untested delivery.** [ElevenLabs model controls](https://elevenlabs.io/docs/eleven-creative/playground/text-to-speech)

20. **V20 — Audio turn handoff.**  
    **Check/how:** Validate any derived turn list against readable text and a separate speaker map; check pronunciation substitutions and chunk counts.  
    **Pass:** Each turn has the correct speaker; tags do not select voices; substitutions avoid duplicate pronunciation; unison has an explicit production instruction. **Severity: block for mapping errors; warn above the 2,000-character reliability recommendation.** [Text to Dialogue](https://elevenlabs.io/docs/overview/capabilities/text-to-dialogue)

21. **V21 — Findings and provenance.**  
    **Check/how:** Join audit IDs, card Merge Records, resolution ledger, actual changed fields and promotion records.  
    **Pass:** No unresolved P0; dispositions have reasons and evidence; accepted fixes are actually applied. Author decisions, GPT approvals and later audited amendments remain distinguishable. **Severity: block.**

22. **V22 — Package integrity.**  
    **Check/how:** Validate the agreed layout, relative links, counts, build time, baseline, commit, dirty-worktree status and SHA-256 map. Include `validation.json`.  
    **Pass:** All payload files accounted for; release resides outside `export/`. Manifest excludes itself from its file-hash map; its hash is recorded externally. **Severity: block.**

23. **V23 — Changelog and supporting views.**  
    **Check/how:** Compute field-level differences from the previous release; regenerate index, coverage and optional scene-date worksheet from canonical records.  
    **Pass:** Additions, deletions and replacements are complete; derived views agree; no claim that historical worksheets automatically change AI context. **Severity: block for misleading/missing changes; warn for optional coverage.**

24. **V24 — Runtime evidence.**  
    **Check/how:** Inspect separate import, generation and audio results: release hash, date, tester, model/voice identifiers, settings, observations and outcome.  
    **Pass:** Truthful status. Unavailable tests remain `not_run`; tested failures remain `failed`. Missing access permits the disclosed static release; known failures require remediation or an explicit restricted-use disposition. **Severity: warn for unavailable tests; block for fabricated success or unresolved release-critical failures.**

25. **V25 — Final acceptance and publication.**  
    **Check/how:** Read task-11 acceptance outside `runs/`, bound to the candidate manifest SHA-256. Revalidate bytes immediately before publishing.  
    **Pass:** `APPROVE`, or a separately recorded explicit author-decision release, with all blocking validation checks satisfied. Publish by promoting the unchanged candidate; never overwrite an existing release. **Severity: block.**

## 5. `00-START-HERE.md` outline and exact smoke tests

Claude should write these sections in Chinese, retaining English field names.

**Release identity and contents.** State baseline, revision, 18/24 counts, full-card default, unresolved warnings, and separate static/runtime results. Link the index, changelog, CSVs, paste sheet, performance sheets and validation report.

**Ten-minute fresh-project smoke test.** Treat ten minutes as a target; record unfinished steps as untested.

1. Create a disposable project named `holoen-rNN-smoke`. Do not test repeated import in the author’s working project.
2. In Story Bible → Characters → `•••` → Import, upload `sudowrite/characters.csv`. Confirm **18 cards**. Import `worldbuilding.csv` through Worldbuilding’s corresponding menu; confirm **24 elements**. Import each combined CSV once. [Characters import](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/characters/a7tdE1ZB8KvAwMD3Mopwpd), [Worldbuilding import](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/worldbuilding/uc5NfWSz4x8Wm3S19LZeo8)
3. Open Fuwawa, Mococo and one other character. Confirm separate twins, `Role: Protagonist`, and populated custom traits including `Audio Tags`. Compare a multiline field and punctuation-containing text against the paste sheet. Open FUWAMOCO and one History card.
4. Confirm Secrets are empty. If the release inventory identifies nonempty Secrets, hide those traits before any AI generation; check the crossed-out eye indicator.
5. Paste `style.txt` into Style. For this disposable test, enter Genre `Light comic fantasy` and Braindump `Fuwawa Abyssgard and Mococo Abyssgard compare a map inside a fictional game.` Leave Synopsis empty. Set third-person POV and past tense.
6. Create a test chapter/Scene: `Scene date: 2026-09-30. Fuwawa Abyssgard and Mococo Abyssgard, the members of FUWAMOCO, compare a map inside a fictional game. Keep their speaking turns distinct.`
7. Check detection underlines for both characters and FUWAMOCO. Record missing or incorrect detections; inspect names and visibility before retrying. Detection is evidence of recognition, not proof that every trait influenced the output. [Detection and visibility](https://feedback.sudowrite.com/changelog/mag-story-bible-detection-and-visibility-update)
8. Generate the smallest practical sample. Check speaker separation, usable delivery tags and untagged narration. Record import and generation outcomes separately, including model and release revision. Preserve the disposable project for diagnosis if anything fails.

**Three-line original-voice test.** Use two clearly distinct original designed voices, mapped A/B/A. Label these lines “Style demonstration; not quotations”:

```text
A: [calm] We can check the map again.
B: [startled] Ah! That door moved.
A: [laughs] Fuwawa, Mococo—your turn.
```

Select `eleven_v4`; use the corresponding sheets’ starting settings. Put each line’s text and voice in its own turn. Listen for correct routing, delivery changes, unwanted reading of tags, duplicated laughter and name pronunciation. If testing IPA, replace the name in a second audio copy; do not append a second pronunciation. Record results as specific observations, not “all voices validated.” Pronunciation remains voice-dependent. [Pronunciation guidance](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices)

**Writing and historical scenes.** Explain scene dates, named participants, relevant world elements and the optional worksheet. For historical work, review date-sensitive cards in a project copy and suppress later facts before generation.

**Updates and troubleshooting.** Use the field-level changelog to update existing cards while preserving author edits. Do not assume repeat CSV import merges names. Explain how to report the release revision, affected field, test outcome and minimal reproduction. Keep completed runtime logs outside the immutable release.

## 6. Required handoff before 04a

No further architectural discussion is needed. Before launching Myth, Claude should provide:

- The Myth packet, registry and source-hash manifest, including alias-aware incoming claims and any deterministic packet parts.
- A resolution ledger assigning stable IDs to the round-1 findings, with **applied**, **pending** or **deferred** dispositions.
- A bounded registry schema covering event precision, status intervals, evidence references, directional credits and reference-only entities.
- Exported promotion provenance outside `runs/`, distinguishing original promotion from subsequent canonical amendments.
- A stable Myth audit snapshot: finish overlapping P0 edits first, or supply explicit changed-file reconciliation.

`research/qa/` was absent during this inspection, so these are preparation requirements, not artifacts I have verified. The compact-card preference can remain pending; it need not delay 04a.
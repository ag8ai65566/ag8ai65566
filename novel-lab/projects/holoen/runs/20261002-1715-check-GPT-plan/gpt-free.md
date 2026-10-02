## Gaps in the queue

The queue covers research and initial audits, but it does not yet establish a reliable path to release r01. Keep its sequential execution, author-controlled merging, and one-round-per-card rule. Add explicit verification of merged changes and repair the release gates before treating their results as release evidence.

The stored validation, dated **2026-10-02 12:30 UTC**, reports nine blockers: **V02, V10–V15, V18 and V19**. The authorized destination is **33 character cards, 28 world cards and 33 performance sheets**. The snapshot contains **28 character cards, 27 world cards and 33 sheets**; the five holoX cards and their world card remain absent from the bible. These are snapshot observations, not claims about subsequent queue progress.

| Gap | Why it matters | Required closure |
|---|---|---|
| **Post-merge verification has no scheduled owner.** Most queued audits can finish before Claude merges their findings or the new research. | An internally consistent source snapshot can still produce conflicting replacements during merging. | Verify accepted changes, their propagation and dependent artifacts against the merged snapshot. Preserve earlier reviews for unchanged material. |
| **holoX cohort and voice-v4 audits are deferred without an executable dependency gate.** | The present holoX packet is only **460 characters** because its owned cards are absent. Completing an empty packet must never count as coverage. | Require E/F dispositions, author-controlled promotions and all six canonical cards before constructing the cohort audit; require five matching sheets before voice-v4. |
| **World-card coverage is assigned, but final coverage is incomplete.** | All 28 planned world cards have cohort owners. However, packets omit fields such as Sensory Details and Secrets; new research primarily targets character cards. | Maintain field-level coverage and propagation records for world cards, including shared histories, units, pair cards and cross-branch material. Do not launch another blanket review of already-reviewed world cards. |
| **Voice fixes can be invalidated by later research.** | R1–R6 can change catchphrases, current defaults and relationships after v1–v3 have inspected their inputs. | Perform voice audits after accepted voice-affecting additions where possible; otherwise verify only their changed dependencies after merging. Stamp sheets last. |
| **The quotation gate is incomplete.** | `span_check.py` checks selected overlapping quotations against partial-report rows; short, unmatched or otherwise unrepresented quotations can escape it. A zero result does not establish complete quotation provenance. | Inventory every exported quotation and example, classify its origin, and bind spoken quotations to source-specific shared spans and separate speaker attribution. |
| **CSV, paste-sheet and packaged-card equality is only partially checked.** | V06 skips canonical fields absent from a CSV row and searches for paste values anywhere in the file. Misplaced, missing or duplicate fields can escape detection. | Compare complete records keyed by card identity and field, including empty values, individual CSVs and packaged reference cards. |
| **Cross-card retrieval is not exhaustive.** | Packet extraction selects certain fields, rows and bullets; pronouns, unlisted names and prose can be missed. Claims naming more than three people are diverted into `ties-groups.md`. | Account for changed multi-person claims and extraction gaps explicitly. Missing reciprocal text remains a coverage issue, not proof of a factual error. |
| **Research dates can drift beyond the baseline.** | The prompts request “2025–2026” material and later verification without consistently separating announcement, event and publication dates. | Freeze persona facts at **2026-09-30**. Keep later events outside r01. Preserve eligible earlier bits while weighting current defaults toward recent eligible evidence. |
| **W1 proposes a converter without a downstream implementation audit.** | Once derived dialogue requests exist, V20 can no longer be hard-coded `not_applicable`. Splitting individual turns also does not bound a whole request. | Review implemented converter behavior, speaker mapping, pronunciation handling, chunking and listening-sheet equality. |
| **Release attestations do not establish closure.** | Several checks pass when a report file merely exists; they do not inspect its verdict, unresolved findings, coverage or input hashes. | Require structured attestations with explicit scope, dependencies, dispositions and matching hashes. |
| **The candidate-to-publication step is unfinished.** | Final validation does not receive a package path; acceptance is checked only for file existence; the builder does not require final acceptance. | Validate a specified immutable candidate and publish those same bytes only after hash-bound acceptance and final validation. |

Two concrete findings show why the tooling work is necessary:

- The draft manifest declares **33/28/33**, while its actual CSVs and character sheets contain **28/27/28**. Its listed payload hashes match. Byte integrity therefore does not establish inventory correctness. The builder still writes expected roster counts at [release.py:538](/tmp/novel-lab-snap-od9xx4mo/novel-lab/tools/release.py:538).
- The V24 expression returns `pass` for `failed`, or for a mixture of `failed` and `not_run`. This follows directly from [release.py:360](/tmp/novel-lab-snap-od9xx4mo/novel-lab/tools/release.py:360) and was confirmed with a read-only logic probe.

Live official documentation also supports separate delivery checks. Sudowrite treats structured Worldbuilding CSV as direct structured input, while hidden cards and traits are unavailable to its AI. CSV fidelity and visibility instructions therefore need separate verification. [Sudowrite Worldbuilding](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/worldbuilding/uc5NfWSz4x8Wm3S19LZeo8), [Visibility Settings](https://docs.sudowrite.com/using-sudowrite/1ow1qkGqof9rtcyGnrWUBS/visibility-settings/4KL8gFeLZP6ep8keUhKVGp)

## Post-merge verification plan

Claude merges only after the author’s order. Card promotions remain author decisions. None of the rounds below creates a second full editorial review of a card.

A **merge spot check** compares an accepted finding with the resulting field, verifies its evidence and propagation, and checks affected dependencies. It does not reopen unchanged isolated claims or repeat their original claim-check review. New cross-card contradictions and newly exposed scope violations remain actionable.

Before these rounds, Claude should prepare:

- A frozen merged-input manifest and an explicit authorized inventory.
- Review results and relevant evidence outside `runs/`.
- A change register: finding ID, original input hash, target card/field, accepted replacement, resulting hash, propagation destinations and disposition.
- A coverage register distinguishing unchanged inherited review, changed material, never-covered material and incomplete coverage.
- Separate records for author decisions, GPT findings and technical release acceptance.

Use a common report format for all rounds except final acceptance: **Coverage**, **Findings**, **Merge handoff**. Include a machine-readable attestation containing the round ID, verdict (`PASS`, `CHANGES` or `INCOMPLETE`), input hashes, covered fields, finding IDs and unresolved dependencies. These are release-review verdicts, not card-promotion approvals.

Each row below reserves **one quota window, approximately 200k tokens maximum**. Keep the initial packet near 8,000 tokens, generally use 8–12 batched tool calls, and reserve capacity for the final report. If a packet exceeds the budget, divide it into non-overlapping claim groups before launch; each resulting task gets its own window.

| Order / round | Inputs and checks | Output and exit criteria |
|---|---|---|
| **M0 — Release tooling and merge provenance** | P1/W1 dispositions; implemented validator, exporter and converter changes; validation spec; inventory; ledger; promotion records. Check the release defects identified here and the merge application contract. | Common report plus a regression-case matrix. Exit when false-pass paths are closed, inventory authority is explicit, and accepted findings can be traced to actual resulting fields. |
| **M1a — EN merge closure** | Deltas for the 19 authorized EN character cards, original audit coverage, accepted research and incoming changes. Verify replacements, surviving evidence, source classes, current-default wording and propagation. | Common report plus finding-to-field closure table. Exit when every accepted EN change is applied or explicitly disposed of, with no unresolved blocking conflict. **Merge spot check.** |
| **M1b — Existing JP additions: merge closure** | Deltas for the nine promoted JP/DEV_IS additions, their research results and incoming changes. Apply the same checks, including Japanese text/gloss distinctions. | Same output and exit rule as M1a. **Merge spot check.** |
| **H1 — holoX cohort audit** | E/F review dispositions, author promotion records, five canonical character cards, holoX world card, complete fresh packets and incoming claims. | Normal cohort report, saved outside `runs/`, with per-field coverage. Exit when the full intended inventory is present and cross-card issues are resolved. This is the missing **first cohort consistency audit**, not another E/F claim review. |
| **M2 — World-card and shared-unit merge closure** | Deltas and coverage gaps across all 28 world cards; related character fields; alias/unit registry; R1–R7 propagation register. Include fields omitted from packet extracts and world-facing additions lacking an owner. | Common report plus a 28-card coverage/disposition matrix. Exit when accepted changes reach all required destinations and unit/alias ownership is coherent. **Merge and cross-card check.** |
| **M3 — Events, status and recency closure** | Merged histories, event/status records, bridge-events findings, accepted milestone additions and current-default evidence changes. | Common report plus event/claim table recording publication date, event date, zone/precision, baseline eligibility and evidence status. Exit when conflicting dates/statuses are resolved and no later fact silently advances the baseline. **Checks merged shared facts.** |
| **M4 — Relationship and multi-person claim closure** | R7 changes, cohort/bridge dispositions, external ties, changed or uncovered `ties-groups` claims, directional credits and incoming/outgoing deltas. | Common report plus endpoint/participant closure table. Exit when changed relationships retain the supported direction and participants, with no inferred closeness or invented reciprocity. Do not demand a filled relationship matrix. |
| **M5a — Voice-v1 merge closure** | v1 findings; changed EN voice fields, sheets and audio evidence; final shared Style and verified platform contract. | Common report plus per-sheet verdicts and dependency hashes. Exit when fixes agree across cards and sheets and quotation provenance is complete for the affected material. **Merge spot check.** |
| **M5b — Voice-v2 merge closure** | Corresponding v2 inputs, including separately supported attribution where required. | Same output and exit rule. **Merge spot check.** |
| **M5c — Voice-v3 merge closure** | Corresponding v3 inputs, Japanese quotations, reading guides and original-voice directions. | Same output and exit rule. **Merge spot check.** |
| **H2 — Voice-v4 audit** | Five merged holoX cards and sheets, their audio reports, final Style and platform contract. | First voice-layer audit, with source-bound quotation and sheet attestations. Exit when each sheet is cleared or its blocking defects are fixed and checked. Do not repeat E/F’s unrelated card claims. |
| **M6 — Sudowrite and audio handoff integration** | Regenerated combined/individual CSVs, paste sheet, Style, story-field files, sheets, pronunciation export, implemented converter and original-voice map fixtures. | Common report plus machine-check results and expected-versus-actual fixtures. Exit when exports match canonical fields and script conversion preserves speaker, text, tags, order and supported pronunciation handling. |
| **M7 — Candidate acceptance** | Immutable candidate, complete manifest/hash map, candidate validation, all closure attestations, ledger, promotion provenance and runtime records. | `research/qa/release-acceptance.md`: first line **APPROVE** or **CHANGES**, followed by candidate manifest SHA-256, coverage, blockers and disclosed warnings. Exit on hash-bound acceptance and final package validation. Publication preserves the accepted bytes. |

This reserves **13 windows**, including the two already-identified missing holoX audits. A merge-closure round with no changed or uncovered dependencies can be closed through hash-based carry-forward without spending another GPT window. Do not rerun completed voice or cohort audits merely to obtain newer timestamps.

After voice closure, Claude stamps **only cleared sheets**. After candidate acceptance, store acceptance and final validation externally to the immutable candidate to avoid circular hashes. Recheck the candidate immediately before publication; any payload change invalidates its acceptance.

Runtime tests are a distinct status:

- If available, record Sudowrite import, generation and ElevenLabs listening results separately.
- If unavailable, retain `not_run` and release only with the explicit static-validation limitation.
- A known release-critical failure requires remediation or a concrete restricted-use disposition; it cannot become a warning merely because other tests were not run.

For M6, chunking must consider the **sum of all `inputs[].text` lengths in each request**. ElevenLabs currently recommends at most 2,000 characters for reliable Text to Dialogue generation. Treat this as a reliability recommendation, separately from verified hard API limits. Pronunciation and tag behavior still require testing with the chosen original voice. [Text to Dialogue](https://elevenlabs.io/docs/overview/capabilities/text-to-dialogue), [ElevenLabs best practices](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices)

## Release criteria

**r01 is done when the authorized 33/28/33 inventory is delivered, every applicable blocking condition is cleared, warnings have explicit dispositions, and the published bytes match the accepted candidate.** A report’s existence, a zero-candidate scan or an author promotion alone does not clear a semantic gate.

V07, V08, V09 and V24 have conditional blocking cases. V20 may be inapplicable only when the actual delivered payload contains no derived audio-turn handoff. V25 is intentionally inapplicable during candidate validation, but mandatory for publication.

| Check | Clearing run or round | “Done” for r01 |
|---|---|---|
| **V01 — Source snapshot** | M0; all round attestations; M7 | Canonical cards, relevant rules/schema, generators, platform contract, evidence, sheets and other dependencies have explicit hashes. Reviewed inputs match, or changed dependencies have closure records. Final validation compares the specified candidate and current approved inputs. |
| **V02 — Authorized inventory** | E/F author-controlled promotions; H1; M0/M7 | Exactly **33 characters, 28 world cards and 33 matching character sheets**; separate Fuwawa and Mococo cards; no unauthorized/reference-only character cards. Manifest counts equal actual shipped records. |
| **V03 — Schema and headings** | M0 implementation; M6 | Correct file-kind mapping; required and optional headings; no duplicate headings; matching names; every character Role exactly `Protagonist`. Unknown kinds cannot bypass required-field checks. |
| **V04 — Placeholders and field names** | M0; M6 | No accidental template markers, merge debris, duplicate identity or misspelled fields. Custom traits have explicit dispositions; intentional example-map placeholders are documented. |
| **V05 — CSV integrity** | W1 implementation; M0/M6 | Strict UTF-8/CSV handling, exact headers and row widths, unique card identities and correct escaping. Meaningful comma, quote, Unicode and embedded-newline fixtures pass. |
| **V06 — Export equality** | M6; M7 | Exact record and field equality across bible, combined CSVs, individual CSVs, paste blocks and packaged cards, including empty values. Only documented normalization is allowed. No extra, misplaced or stale records. |
| **V07 — Sizes and limits** | W1 platform verification; M6 | Verified hard limits pass with recorded units and provenance. Local targets, including Relationships’ configured 350-word target, remain distinguishable from platform limits. Uncertain counting is disclosed. |
| **V08 — Alias ownership** | Cohort/global findings; M2/M4 | Every collision/common-word candidate has a disposition; confirmed incorrect ownership is fixed. Existing `baerys` and `chadcast` warnings are resolved or justified individually. |
| **V09 — Units and retrieval** | Cohorts; M2/M4 | Membership and unit classification match evidence; multi-person unit names are not individual aliases. False membership blocks; optional retrieval gaps are disclosed. |
| **V10 — Dates, zones and status** | bridge-events; M3 | Announced, scheduled, held and uploaded dates remain distinct; time zones and supported precision are preserved; status claims agree at the factual baseline. |
| **V11 — Participants and direction** | All 11 cohort scopes, including H1; ties-external; M4 | Changed and uncovered claims have supported endpoints, rosters and directional credits. Multi-person claims have an explicit owner. No invented attendance, reversed credit or unsupported relationship escalation. |
| **V12 — Evidence records** | Cohorts; R1–R7 dispositions; M1–M4 | Important accepted changes have URL, evidence class, claim locator and checked date. Fresh, inherited and inaccessible evidence are distinguished. Registry export remains explicitly non-exhaustive. |
| **V13 — Quotations and ASR** | v1–v3; H2; M5a–c; M6 | Every exported quotation/example has an origin classification. Spoken quotations bind to a contiguous shared span from both models for the same window, with separate speaker support. No stitching, unsupported wording, lyrics or mislabeled demonstrations. |
| **V14 — Scope screening** | Cohorts; H1/H2; M1–M6; M7 payload check | The task’s complete exclusion list applies across exported fields, packaged dossiers, sheets and included support material. No obsolete excluded excerpts are distributed through process notes or evidence copies. |
| **V15 — Usability and fidelity** | Original card reviews; cohort coverage; M1–M2/M5–M6 | Changed prose remains directly usable, correctly attributed and consistent in tense/person. Uncertainty is not asserted as fact; supported profanity and crude humor are preserved. No uncovered semantic field is silently attested. |
| **V16 — Secrets and visibility** | M2/M6 | Empty Secrets agree with the guide. Any accepted nonempty value has reviewed visible clues and explicit pre-generation hiding instructions; duplicated restricted material is addressed. Missing controls block. |
| **V17 — Style handoff** | W1; M5/M6 | Canonical Style, paste-sheet leading block and packaged `style.txt` agree. Original designed voices, the written/nonverbal convention and untagged narration remain clear. Unchosen production story fields stay blank. |
| **V18 — Performance freshness** | M5a–c/H2; targeted stamping; M6 | Each shipped sheet matches reviewed card fields, its own reviewed content and relevant Style/platform/evidence dependencies. Settings conversions are correct where applicable. A fresh stamp cannot substitute for review. |
| **V19 — Voice/pronunciation claims** | W1; v1–v3/H2; M5 | Original-voice directions contain no imitation or measured pitch/rate targets. Partner tags are proposed scene directions. Unsupported controls are removed; untested pronunciation stays provisional. |
| **V20 — Audio turn handoff** | W1 converter implementation; M6 | If delivered, every turn maps to the intended speaker/voice, preserves text order and avoids duplicate pronunciation substitutions. Tags do not select voices; unison has explicit production handling. Otherwise, N/A has a payload-based reason. |
| **V21 — Findings and provenance** | M0; all closure rounds; M7 | No unresolved P0 or other release-blocking finding. Accepted fixes are present; dispositions have reasons and evidence; author promotions remain distinguishable from GPT review and subsequent amendments. |
| **V22 — Package integrity** | M6/M7 | Required files, actual counts, relative links, build metadata, validation and complete payload hashes are checked. Manifest excludes itself; its full SHA-256 is recorded externally. No existing release is overwritten. |
| **V23 — Changelog/supporting views** | M6/M7 | r01 accurately identifies all shipped cards as initial additions. Index, coverage, pronunciation and scene-date views agree with canonical data. Historical worksheets make no claim to alter AI context automatically. |
| **V24 — Runtime evidence** | M6/M7 | Import, generation and audio outcomes are truthfully recorded with tested artifact hash, date, tester and applicable settings/model/voice IDs. `not_run` is disclosed; `failed` never counts as pass. |
| **V25 — Acceptance/publication** | M7; final publication check | Acceptance names the exact candidate manifest hash and says `APPROVE`, or a separate explicit author release decision exists. All blocking checks still pass. Publication promotes the unchanged candidate. |

The following implementation gaps must be closed to make that table enforceable:

| Implementation location | Required correction |
|---|---|
| [release.py:123](/tmp/novel-lab-snap-od9xx4mo/novel-lab/tools/release.py:123) | Expand the dependency inventory beyond the current selected cards, sheets and code. Bind semantic review to relevant evidence, rules, templates and generated inputs without introducing circular hashes. |
| [release.py:180](/tmp/novel-lab-snap-od9xx4mo/novel-lab/tools/release.py:180) | Validate complete CSV schemas and records. Replace paste substring presence with identity-and-field comparison. Check extra individual CSVs and packaged copies. |
| [release.py:268](/tmp/novel-lab-snap-od9xx4mo/novel-lab/tools/release.py:268) | Replace report-existence attestations with verdict, coverage, finding-disposition and dependency-hash validation. |
| [release.py:297](/tmp/novel-lab-snap-od9xx4mo/novel-lab/tools/release.py:297) | Evaluate Secrets controls; a nonempty field with missing controls must fail rather than receive an unconditional warning. |
| [release.py:317](/tmp/novel-lab-snap-od9xx4mo/novel-lab/tools/release.py:317) and [release.py:392](/tmp/novel-lab-snap-od9xx4mo/novel-lab/tools/release.py:392) | Include additional sheet dependencies and restrict stamping to explicitly cleared sheets. The present stamp command stamps every matching card/sheet. |
| [release.py:334](/tmp/novel-lab-snap-od9xx4mo/novel-lab/tools/release.py:334) | Determine V20 applicability from the delivered artifacts. |
| [release.py:336](/tmp/novel-lab-snap-od9xx4mo/novel-lab/tools/release.py:336) | Read structured priority/severity and dispositions. Searching for `P0` in an ID misses IDs such as `VOICE-V1-NNN`; mixed prose statuses also escape the manifest’s pending/deferred extraction. |
| [release.py:347](/tmp/novel-lab-snap-od9xx4mo/novel-lab/tools/release.py:347) | Verify package hashes, counts, validation file and substantive runtime outcomes. File presence alone does not clear V22/V23. |
| [release.py:384](/tmp/novel-lab-snap-od9xx4mo/novel-lab/tools/release.py:384) and [release.py:442](/tmp/novel-lab-snap-od9xx4mo/novel-lab/tools/release.py:442) | Add explicit candidate selection for final validation. Stage candidates separately from published releases, check post-build failures, inspect acceptance content/hash, and publish without rebuilding. |

## Recommended changes to the queue

1. **Express dependencies, not only a numbered list.**  
   At [GPT-PROGRAM.md:14](/tmp/novel-lab-snap-od9xx4mo/novel-lab/projects/holoen/GPT-PROGRAM.md:14), distinguish research-ready, review-ready, merge-pending and release-ready tasks. The author’s merge hold remains binding. While it lasts, audits examine their recorded snapshots; they cannot certify future merged content.

   Preferred dependency order after an authorized merge becomes possible:

   **E/F and independent research → accepted changes merged → cohort consistency → events/ties closure → final voice/sheet work → exports/converter integration → immutable candidate → acceptance/publication.**

   Preserve already-completed work and verify its changed dependencies instead of restarting it.

2. **Make holoX prerequisites explicit.**  
   Replace the informal deferral at [GPT-PROGRAM.md:26](/tmp/novel-lab-snap-od9xx4mo/novel-lab/projects/holoen/GPT-PROGRAM.md:26) with H1/H2 readiness requirements. Missing owned cards must produce `INCOMPLETE`, never a clean audit of a reduced roster.

3. **Split W1 into two bounded tasks.**  
   [mk_gpt_program.py:222](/tmp/novel-lab-snap-od9xx4mo/novel-lab/tools/mk_gpt_program.py:222) combines platform research, workflow design, full converter code, tests, package patches and quick-start writing.

   - **W1a:** verify platform facts and produce the versioned workflow/script/API contract.
   - **W1b:** use that contract to produce converter code, meaningful fixtures and package/documentation changes.

   M0/M6 review the implementation. Require the converter to reject unresolved example voice IDs and unknown speakers, preserve Japanese text, and distinguish spoken text from reading aids. Define the tag list as the project’s permitted palette, rather than implying it is an exhaustive vendor-supported vocabulary.

4. **Rebalance R5/R6 and bound R7.**  
   The two seven-member groups at [mk_gpt_program.py:36](/tmp/novel-lab-snap-od9xx4mo/novel-lab/tools/mk_gpt_program.py:36) should become three groups matching downstream ownership: **JP first four**, **JP second five**, **holoX five**. Keep the existing 8-proposal figure as a ceiling, not a target.

   R7 currently invites exploration across 33 members—**528 possible unordered pairs**. At [mk_gpt_program.py:190](/tmp/novel-lab-snap-od9xx4mo/novel-lab/tools/mk_gpt_program.py:190), require a declared bounded candidate list, checked/unchecked coverage and evidence-based stopping. Do not merge R7 with ties-external: one discovers additions; the other audits existing claims.

5. **Make temporal eligibility explicit in every research prompt.**  
   Amend [mk_gpt_program.py:118](/tmp/novel-lab-snap-od9xx4mo/novel-lab/tools/mk_gpt_program.py:118) and [mk_gpt_program.py:163](/tmp/novel-lab-snap-od9xx4mo/novel-lab/tools/mk_gpt_program.py:163):

   > Record publication date, event date, verification date and baseline eligibility separately. Material learned after September 30 may verify an earlier fact. A future event announced by September 30 is eligible only as an announcement, never as a held event. Events after the baseline remain outside r01 unless the author changes its scope.

   Apply the same rule to R7, which lacks the dedicated after-baseline section.

6. **Regenerate all review inputs at launch, or bind them explicitly to their earlier snapshot.**  
   Only QA runs carrying `qa.json` receive automatic preparation in [lab.py:468](/tmp/novel-lab-snap-od9xx4mo/novel-lab/tools/lab.py:468). Research and voice prompts capture data when their generators run.

   Add equivalent preparation metadata for those tasks. Fix [mk_gpt_program.py:76](/tmp/novel-lab-snap-od9xx4mo/novel-lab/tools/mk_gpt_program.py:76), which always selects holoX drafts: once canonical cards exist, later research should use them. Preserve the actual earlier inputs for completed runs.

7. **Replace nominal packet splitting with a total prompt budget.**  
   At [qa_packets.py:329](/tmp/novel-lab-snap-od9xx4mo/novel-lab/tools/qa_packets.py:329), splitting owned and incoming material does not reduce a run’s input because [qa_runs.py:99](/tmp/novel-lab-snap-od9xx4mo/novel-lab/tools/qa_runs.py:99) includes both inline.

   Current examples:

   | Packet scope | Combined characters |
   |---|---:|
   | Promise | 148,010 |
   | Global | 112,085 |
   | Myth1 | 106,338 |
   | Bridge events | 101,823 |

   Budget the complete prompt, including rules and ledger. Partition oversized work by stable claim groups with explicit cross-references and a shared coverage manifest. Reusing a reference is preferable to repeating its full text.

8. **Correct stale ownership and finding-ID instructions.**  
   [gpt-cohort-audit.md:43](/tmp/novel-lab-snap-od9xx4mo/novel-lab/framework/prompts/gpt-cohort-audit.md:43) still describes 18/24 and treats Baelz as reference-only. [gpt-bridge-audit.md:20](/tmp/novel-lab-snap-od9xx4mo/novel-lab/framework/prompts/gpt-bridge-audit.md:20) repeats those counts. [qa_runs.py:54](/tmp/novel-lab-snap-od9xx4mo/novel-lab/tools/qa_runs.py:54) claims seven cohorts have already compared all relevant ties.

   Generate these statements from the authorized roster and actual coverage records. Use cohort-specific finding namespaces such as `MYTH1`, `MYTH3`, `JP2` and `HOLOX`; otherwise separately queued audits can reuse IDs from an unchanged ledger.

9. **Close the quotation loophole in the voice prompt.**  
   [gpt-voice-audit.md:24](/tmp/novel-lab-snap-od9xx4mo/novel-lab/framework/prompts/gpt-voice-audit.md:24) permits a “labelled secondary transcription” among acceptable examples, despite the later rule that fan transcription cannot establish exact speech.

   Replace that allowance with:

   > Spoken quotations require the two-model shared-span gate. Secondary transcription supplies a candidate for Claude’s audio check only. Official written text and original Style demonstrations must be labeled as those separate categories.

   Also replace the fixed “0 candidates” assertion at line 30 with the current scan result and its limitations. Japanese orthographic equivalence needs a documented mapping; it must not excuse lexical changes or removed repetitions.

10. **Assign ownership for omitted fields and multi-person claims.**  
    At [qa_packets.py:83](/tmp/novel-lab-snap-od9xx4mo/novel-lab/tools/qa_packets.py:83), declare which review covers every omitted field. The voice audit alone does not cover Personality, Motivation, Physical Description or all dossier material.

    At [qa_packets.py:415](/tmp/novel-lab-snap-od9xx4mo/novel-lab/tools/qa_packets.py:415), ensure every diverted group claim has a recorded review owner. Avoid another exhaustive ties-cast run; inspect changed, contradictory or previously uncovered claims.

11. **Harden the merge application contract.**  
    [qa_runs.py:126](/tmp/novel-lab-snap-od9xx4mo/novel-lab/tools/qa_runs.py:126) accepts a narrow locator form, `` `C/<stem>.md` `` or `` `W/<stem>.md` ``, while other generators use different forms. Align the schemas.

    Apply only dispositioned changes, with expected input hash, field locator and exact old text. Simulate overlapping edits cumulatively during dry runs. Use an explicit changed-card allowlist rather than promoting every differing latest run through [qa_runs.py:165](/tmp/novel-lab-snap-od9xx4mo/novel-lab/tools/qa_runs.py:165).

12. **Update the validation spec and outstanding ledger entries.**  
    [validation-spec.md:13](/tmp/novel-lab-snap-od9xx4mo/novel-lab/projects/holoen/research/qa/validation-spec.md:13) still specifies 18/24/18. Replace that with the versioned authorized inventory. Apply this task’s stricter scope rules consistently across all prompts and release checks.

    Give explicit closure owners to:

    - `CONSULT-P1-007`: quotation attribution/provisional directions.
    - `CONSULT-P1-008`: reviewed sheet dependencies and stamping.
    - `CONSULT-P2-002`: distinguishing cues before repeated tag boilerplate.
    - `CONSULT-R2-005`: immutable candidate and hash-bound acceptance.
    - `TASK-06`: accepted refresh changes and held candidates.
    - `AUTHOR-2026-10-02`: reconcile its stale “in progress” description with actual promotion provenance.

    Do not mark these resolved merely because another file says the surrounding work is complete.

## Risks

| Risk | Control |
|---|---|
| **Quota exhaustion** | Budget total prompt size and repeated context, not just search count. Split oversized scopes before launch. Incomplete required coverage remains explicit and prevents its gate from clearing. |
| **Evidence staleness during a long queue** | Separate the persona baseline from platform verification dates. Recheck volatile workflow claims before packaging; revisit persona evidence only where changed claims or contradictions require it. |
| **Conflicting edits to the same fields** | R1–R7, voice and cohort audits can all alter Relationships or voice fields. Merge by claim/field with original hashes and conflict dispositions; reject blind last-writer-wins replacements. |
| **False confidence from automation** | A matching hash proves identity, not truth. A zero-result regex scan proves only that its patterns found nothing. Pair mechanical checks with scoped semantic attestations. |
| **Scope reintroduction through supporting files** | Apply the same restrictions to packaged dossiers, sheet examples, evidence exports and process notes. Record exclusions generically; do not restate deliberately omitted details. |
| **Overstated voice evidence** | ASR agreement establishes neither speaker identity nor recurrence, timbre or delivery. Keep those evidence requirements separate and all synthesis directions for original designed voices. |
| **Relationship inflation** | Do not infer mutual closeness from co-occurrence, fill every empty pair, or turn retrieval counts into member comparisons. Preserve event-specific and directional wording. |
| **Release scope growth** | Separate optional enrichment from corrections needed for r01. Freeze accepted content before final integration; defer optional additions with reasons instead of perpetually refreshing the release. |
| **Acceptance invalidation** | Any payload edit after acceptance—including revised test records inside the package—changes its hash. Keep post-freeze records external or create a new candidate and verify the affected changes. |

**Coverage:** This audit inspected the queue, project rules, requested QA files, release and audit tooling, prompt generators/templates, current inventories and draft-package metadata. All **55 canonical source hashes** in the QA manifest matched; the draft’s listed payload hashes also matched. Live official Sudowrite and ElevenLabs documentation was checked on **2026-10-02**.

No files were modified and no `projects/*/runs/` files were read. No writing validator, builder, exporter or stamp command was executed. This was a program/tooling audit: individual member claims, audio windows, authenticated imports, generation and listening tests were not re-reviewed or performed.
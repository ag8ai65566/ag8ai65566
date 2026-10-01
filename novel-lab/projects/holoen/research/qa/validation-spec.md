# Release validation spec (GPT, consult round 2, 2026-10-01)

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

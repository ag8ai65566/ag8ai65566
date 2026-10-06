CHANGES

I reviewed the supplied code and live upstream sources on **2026-10-06**, and ran read-only, in-memory reproductions. This workspace still lacks `voice-studio/`; I could not rerun Claude’s tests or verify the actual image.

1. **Finding status table**

Paths below are relative to `vstudio/`.

| # | Status | Evidence and remaining work |
|---|---|---|
| 1 | partly fixed | `bootstrap.sh::finish` adds traps, process termination and retries. However, `server.py::lifespan` calls `reap()` only once; `training.py::reap` ignores overdue active runs. Persistent independent cleanup remains missing. |
| 2 | partly fixed | `training.py::_cloud_train` persists intent, but its creation-exception branch unconditionally records `removed`, including after empty reconciliation or failed deletion. Duplicate pod IDs are not persisted. |
| 3 | partly fixed | `remote/qwen3_train.py::main` correctly creates mono 24-kHz reference audio, satisfying the [pinned input contract](https://github.com/QwenLM/Qwen3-TTS/blob/022e286b98fbec7e1e916cb940cdf532cd9f488e/finetuning/dataset.py#L97-L127). Missing/invalid references still fail only after rental and downloads. |
| 4 | fixed | `remote/qwen3_train.py::sample_all` and `engines/qwen3.py::synthesize` use `Auto` for SFT outputs. |
| 5 | fixed | `remote/voxcpm2_train.py::prune_optimizer_states` preserves the newest directory during training and performs final pruning after trainer exit, respecting [upstream publication order](https://github.com/OpenBMB/VoxCPM/blob/f0c787f0937dc1c9a8f4f64d9a332d9c5da2e629/scripts/train_voxcpm_finetune.py#L764-L775). |
| 6 | fixed | `remote/voxcpm2_train.py::main` removes the duplicate final-iteration save before retention and correctly maps checkpoint labels to completed updates. |
| 7 | partly fixed | Both trainers publish weights before sampling. Initial archive failure can still destroy the only trained weights; optional sample retrieval can prevent registration. Disk budgets remain approximate and container allocations fixed. |
| 8 | partly fixed | `training.py::plan/start` shares effective parameters; `runpod.py::create_pod` requests one GPU and records returned pricing fields supported by [REST v1](https://docs.runpod.io/api-reference/pods/POST/pods). Parameter validation, storage charges and configuration-specific speed keys remain missing. `max_usd` is not a spending ceiling. |
| 9 | partly fixed | `VoxCPM2Engine.schedule` removes the 150-update floor and applies the cap. Remote epoch metadata uses a truncated denominator; scheduling still ignores [upstream token filtering](https://github.com/OpenBMB/VoxCPM/blob/f0c787f0937dc1c9a8f4f64d9a332d9c5da2e629/scripts/train_voxcpm_finetune.py#L142-L173). |
| 10 | partly fixed | Frozen storage/deadlines, direct object deletion and uniqueness are present. `get_json` still treats malformed JSON as missing; failed downloads become terminal failures excluded from recovery. Migration has an upgrade defect below. |
| 11 | partly fixed | `evaluate.py::evaluate_model` rejects missing clips/ASR and retries individual failures, but `_mean` silently removes non-finite scores while `complete` accepts them. |
| 12 | partly fixed | Conditions are separated and seen lines excluded. There are no language-specific summaries or reference-mode recommendations. `improved_over_base=False` still allows automatic checkpoint switching; Qwen has no comparable base/plain result. |
| 13 | fixed | Both trainers record resolved asset commits; `VoxCPM2Engine.load` downloads the recorded base snapshot before loading LoRA. |
| 14 | partly fixed | `tts.py::generate` includes loading inside the lock; `Engine.unload` clears ownership. TTS remains resident during ASR, and complete scoring ownership cannot be verified without `jobs.py` and the embedding/ASR implementations. |
| 15 | partly fixed | Native FlashAttention probing, removal fallback and restart guidance improve installation. Cloud probing omits trainer execution/imports; local probing omits audio decoding. The stamp lacks image identity, and cache hits skip probes. |
| 16 | partly fixed | `server.py::guard` blocks ordinary foreign hosts and enforces configured passwords. Origin comparison ignores scheme/port; a network bind without a password still permits forged local Host headers. |
| 17 | partly fixed | `tts.py::_generate` and cloud entry recheck current consent. Add another check immediately before audio upload, validate dataset consent snapshots, and verify talent exclusion in the omitted eligibility code. |
| 18 | partly fixed | `training.py::remove_reference` fixes the deletion escape. `install_model`’s new checkpoint validator accepts `.` and `..`; resolved checkpoint containment is not checked. |

2. **Defects in the fixes, most severe first**

**A. Blocker — uncertain creation and failed cleanup can be falsely closed.**

In `_cloud_train`, both an empty pod list and unsuccessful removals reach `_set(..., pod_state="removed")`. One startup reaper invocation cannot catch a pod appearing later. Also, stopping the pod after three failed removals stops the process that was supposed to keep retrying deletion.

**Patch:** remove that unconditional assignment. Persist an unresolved creation state and every discovered pod ID, with deletion state per pod. Match the actual training environment value—remove `_find_pods`’s default-to-`tid` fallback. Run reconciliation periodically, including terminal runs and overdue active runs. Keep uncertain requests pending across empty listings and restarts; [pod names are not unique](https://docs.runpod.io/api-reference/pods/GET/pods).

Enforce deadlines outside S3 polling: its exception branch currently skips the deadline check, and SDK retries can greatly exceed the claimed ten minutes. The external watcher must continue after the training container stops.

**B. Major — optional samples still gate recovery of valid weights.**

`_cloud_train` downloads `model.tar`, then an exception checking/downloading `samples.tar` prevents `install_model`. The wrapper marks the training failed, and startup excludes it. Local deadline expiry likewise bypasses archive recovery.

**Patch:** make weight recovery a separate resumable phase, independent of pod existence. Install valid weights even when sample retrieval fails; persist a separate sample-retry state and support idempotent sample attachment. Route timeout/error outcomes through durable-artifact recovery after cleanup. Retry malformed JSON as a storage error rather than returning `None`.

First-archive failure also needs protection: retain completed checkpoints on durable storage until packaging succeeds, with capacity budgeted for that overlap.

**C. Major — the new guard has authentication and Origin gaps.**

A listener bound to `0.0.0.0` without a password accepts a non-browser client sending `Host: localhost`. I also reproduced acceptance of different localhost ports and schemes; those are distinct [origins](https://html.spec.whatwg.org/multipage/browsers.html#same-origin). Non-ASCII passwords raise `TypeError` in `compare_digest`.

**Patch:** refuse non-loopback binding without authentication, validate configured hosts in both modes, and compare normalized `(scheme, hostname, effective_port)` tuples. Require a session token for local mutations. Compare password bytes:

```python
_secrets.compare_digest(given.encode("utf-8"), password.encode("utf-8"))
```

**D. Major — the uniqueness migration can prevent startup.**

`db.py::_migrate` raises `IntegrityError` when an older database contains duplicate `models.training_id` values—the condition this fix addresses. I reproduced this.

**Patch:** migrate duplicates transactionally before creating the index. Preserve every model and directory; retain one canonical training association, and move redundant associations into provenance metadata while setting their indexed `training_id` to `NULL`. Then create the unique index.

**E. Major — non-finite scores can still produce a recommendation.**

Two expected clips with scores `[0.97, NaN]` produce `agree=0.97`, `n=2`, `complete=True`. The candidate qualifies. Non-finite similarity behaves similarly.

**Patch:** validate every expected clip before aggregation:

```python
expected = {i for i, line in enumerate(lines) if not line.get("seen")}
complete = (
    bool(expected)
    and {c["line"] for c in cs} == expected
    and all(
        c[k] is not None and math.isfinite(c[k])
        for c in cs for k in ("sim", "agree")
    )
)
```

Apply eligibility per condition and language. Before changing the default, compare against a complete matched base result using accuracy and similarity; return “no improvement” when appropriate. Treat Qwen’s cross-condition base comparison as unmeasured.

**F. Major — sampling failures are reported as complete.**

Both `sample_all` implementations catch individual synthesis exceptions and return normally. Their callers then write `sampling="complete"`; bootstrap reports success merely because `samples.tar` exists.

**Patch:** return expected/successful clip counts and failures from `sample_all`. Mark incomplete whenever a required clip is absent, and propagate that metadata into the training note. An existing archive proves publication, not complete sampling.

**G. Moderate — checkpoint validation permits directory aliases.**

The new regex accepts `.`, `..`, and, with `match`, a valid prefix followed by a trailing newline.

**Patch:** require an actual string, use `fullmatch`, reject `.`/`..`, and verify each resolved checkpoint remains directly under the intended checkpoint directory. Check containment after relocation too, including archive symlinks.

**H. Moderate — epoch reporting disagrees with the quote.**

For 18 clips, batch 2 and accumulation 8, the quote reports 2.67 effective epochs while remote metadata reports 3.00. `per_epoch = batches // accum` causes this.

**Patch:** use `updates * accum / batches` consistently. Reject only an empty dataloader; the [pinned trainer accumulates across epoch boundaries](https://github.com/OpenBMB/VoxCPM/blob/f0c787f0937dc1c9a8f4f64d9a332d9c5da2e629/scripts/train_voxcpm_finetune.py#L258-L284), so requiring a whole accumulation window within one epoch is unnecessary. Recompute after filtering.

3. **Ready for a first paid run?**

**No, as submitted.** Fix cleanup and artifact recovery before renting. The first run should then be a supervised integration pilot.

I accept tokenizer batch **32 on an 80-GB GPU** and **12 evaluation lines** for that pilot; neither establishes memory fit or evaluation reliability. Plain HTTP is acceptable under the stated trusted-LAN limitation once authentication is enforced. Manual volume-capacity verification is acceptable for the pilot; add a mounted-volume space check before training where quota information is exposed. RunPod documents fixed capacity and possible out-of-space failures in its [S3 limitations](https://docs.runpod.io/storage/s3-api#known-issues-and-limitations).

Author checklist:

1. Pass added fault tests: delayed pod appearance, failed deletion, S3 outage across the deadline, failed sample download, and restart during recovery.
2. Use loopback access. Verify consent, readable reference audio, volume/datacenter, free capacity and the actual hourly price.
3. Set a **45–60-minute deadline**, with an independent watcher and RunPod console available. Keep the computer awake.
4. Run one tiny job: VoxCPM LoRA with **16 training clips and `max_steps_cap=2`**, plus held-out JA/EN clips. For a separate Qwen pilot, use **80 GB, batch 2, one epoch**.
5. Verify actual trainer imports/audio decoding, checkpoint reload, synthesized output, archive recovery and exactly one model registration. Record peak RAM/VRAM/disk.
6. Exercise deliberate failure/timeout, confirm the training process ends, and independently confirm **every associated pod is deleted** before proceeding to a longer run.
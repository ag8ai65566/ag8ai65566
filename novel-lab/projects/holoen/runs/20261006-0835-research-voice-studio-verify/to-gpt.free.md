# Verification request: Voice Studio fixes (commit 58723ff)

You are GPT. In run 20261006-0755 you reviewed Claude's Voice Studio code and reported 18 findings plus a defaults
table. Claude has applied fixes. Verify them. Use live web search for upstream checks where needed (same pinned
commits as before: VoxCPM `f0c787f0937dc1c9a8f4f64d9a332d9c5da2e629`, Qwen3-TTS
`022e286b98fbec7e1e916cb940cdf532cd9f488e`, RunPod REST v1 / S3 API). Work read-only; answer in English.
Today is 2026-10-06.

What Claude ran locally (no GPU, no RunPod account):
- 8 end-to-end tests pass, including a simulated pod round trip (mock engine's train_entry.py → model.tar +
  samples.tar → idempotent install → per-condition scoring), the Host/Origin guard, password mode, schedule maths
  and setup-script rendering;
- `bootstrap.sh` executed in a scratch root with a fake `runpodctl` for five cases: success, training failure,
  failure after model.tar (partial), timeout (training process verified killed), and removal failing 4 times
  (retries, `stop` after the third failure, then removal).
Not done: anything needing a GPU, the real image, or a RunPod account.

Deliberately not changed (tell Claude if you disagree):
- Qwen tokenizer preparation batch stays at the upstream constant 32 (no CLI flag; first run uses an 80 GB GPU).
- No HTTPS for LAN mode; docs say LAN-only, http, password not encrypted on the wire.
- Network-volume capacity is not checked by the studio (no free-space API); docs give sizes.
- Sample lines raised from 6 to 12 (you suggested 24).

## Output format

1. **Finding status table** — one row per original finding 1–18: fixed / partly fixed / not fixed / wrong fix, with
   one line of evidence (file + function) and what is still missing.
2. **Regressions or new defects** introduced by the fixes, most severe first, each with a concrete patch.
3. **Ready for a first paid run?** yes/no, and the exact short checklist the author should follow for it.

Be concise; do not restate code that is fine.

## Your original review (run 20261006-0755)

**1. Verdict**

**Not ready for an unattended paid run.** The main blockers are incomplete pod cleanup/recovery and Qwen’s unchecked reference-audio sample rate. There are also defects in checkpoint retention, cost estimates, evaluation, and local GPU ownership. I checked the pinned upstream files and live documentation on **2026-10-06**. This workspace does not contain `voice-studio/`, so the application review uses the supplied code; I ran small, read-only logic reproductions, but no installation, GPU training, or RunPod integration test. The omitted `jobs`, API routes, ASR, and speaker-embedding implementations remain unverified.

**2. Findings**

1. **Blocker — `cloud/bootstrap/bootstrap.sh::finish`, `training.py::cloud_train`: failed cleanup can leave a chargeable pod without further retries.**

   `finish()` suppresses both CLI failures and exits successfully. The watchdog calls the same function, so it is not an independent safeguard. Studio-side deletion failures can likewise be swallowed before the training becomes `failed`; startup recovery excludes final states. There are no bootstrap exit/signal traps, and the timeout subprocess does not terminate training if pod deletion fails.

   The legacy `runpodctl remove pod` command itself exists; the defect is treating an unsuccessful removal as completion. See [RunPod’s command implementation, lines 11–21](https://github.com/runpod/runpodctl/blob/main/cmd/pod/removePod.go#L11-L21).

   **Fix:** keep cleanup pending until deletion is confirmed, retry it across application restarts, and install bootstrap exit/signal handling. Replace the removal portion of `finish()` with bounded calls and persistent retries:

   ```bash
   timeout 15s sync || true
   until timeout 30s runpodctl remove pod "${RUNPOD_POD_ID:?}"; do
     echo "[vs] pod removal failed; retrying"
     sleep 10
   done
   exit 0
   ```

   Run setup/training in a supervised process group that the watchdog terminates before cleanup. Persist an absolute deadline and arrange a reaper outside the training container: an in-container watchdog cannot cover failure to start, container death, or a wedged container. Never report the configured time limit as a guaranteed spending ceiling until this is verified.

2. **Blocker — `training.py::_cloud_train`, `resume_interrupted`: pod creation has an orphan window.**

   RunPod can accept `POST /pods` while the response is lost. Another window exists between receiving the response and saving `pod_id`. In either case, recovery sees no ID and marks the run failed, although the pod may exist. A container that never reaches bootstrap has no watchdog.

   RunPod supports listing pods by name and network volume; names are not unique. See [List Pods](https://docs.runpod.io/api-reference/pods/GET/pods).

   **Fix:** persist creation intent, storage location, and deadline before POST. Reconcile an uncertain creation before retrying or declaring failure:

   ```python
   pods = runpod._req(
       "GET", "/pods",
       params={
           "name": f"voice-studio-{tid}",
           "networkVolumeId": saved_volume_id,
       },
   )
   matches = [
       pod for pod in pods
       if (pod.get("env") or {}).get("VS_TRAINING_ID") == tid
   ]
   ```

   Save and reconcile every matching pod, including duplicates. Continue reconciliation after an initially empty result; an immediate GET does not prove a timed-out POST was rejected.

3. **Blocker for non-24-kHz datasets — `remote/qwen3_train.py::main`: reference audio violates the trainer’s input contract.**

   The adapter passes the original reference WAV unchanged. Upstream loads it at its native sample rate and asserts **24,000 Hz** before computing its mel spectrogram. A 16-kHz or 48-kHz reference therefore fails on the first training batch, after model download and audio-code preparation. See [pinned `dataset.py`, lines 40–46 and 97–128](https://github.com/QwenLM/Qwen3-TTS/blob/022e286b98fbec7e1e916cb940cdf532cd9f488e/finetuning/dataset.py#L97-L128).

   **Fix:** create one normalized training reference before writing `train_raw.jsonl`:

   ```python
   import librosa
   import soundfile as sf

   ref24 = job.work / "reference_24k.wav"
   y, _ = librosa.load(ref_abs, sr=24000, mono=True)
   sf.write(ref24, y, 24000, subtype="PCM_16")
   ref_abs = str(ref24)
   ```

   Validate nonempty audio and duration before renting the GPU. The supplied preparation code is insufficient to establish that existing dataset references are already 24 kHz.

4. **Major — `remote/qwen3_train.py::main`, `engines/qwen3.py::synthesize`: training and inference use different language conditioning.**

   The pinned dataset reads `language` but discards it; its collator constructs the language-auto prefix. The adapter then explicitly supplies Japanese or English during checkpoint sampling and local SFT inference. Upstream generation constructs a different prefix for explicit languages. This is a confirmed conditioning mismatch; its audible impact requires testing. See [pinned dataset, lines 111–185](https://github.com/QwenLM/Qwen3-TTS/blob/022e286b98fbec7e1e916cb940cdf532cd9f488e/finetuning/dataset.py#L111-L185) and [generation, lines 1941–1978](https://github.com/QwenLM/Qwen3-TTS/blob/022e286b98fbec7e1e916cb940cdf532cd9f488e/qwen_tts/core/models/modeling_qwen3_tts.py#L1941-L1978).

   **Fix for the unchanged official recipe:** use auto conditioning for SFT outputs, while retaining JA/EN labels for ASR evaluation:

   ```python
   wavs, sr = m.generate_custom_voice(
       text=line["text"], speaker=SPEAKER, language="Auto"
   )
   ```

   Apply the same change to the local SFT branch. Keep explicit language selection available as an experimental override, or implement and test a language-aware collator.

5. **Major — `remote/voxcpm2_train.py::prune_optimizer_states`: pruning races with upstream checkpoint publication.**

   `training_state.json` is not a completion marker. Upstream writes it **before** copying the checkpoint into `latest`. The log-tail thread can delete optimizer files during that copy, leaving `latest` incomplete. See [pinned trainer, lines 765–775](https://github.com/OpenBMB/VoxCPM/blob/f0c787f0937dc1c9a8f4f64d9a332d9c5da2e629/scripts/train_voxcpm_finetune.py#L765-L775).

   **Fix:** during training, never prune the newest step directory. Older directories cannot still be the source of the serial trainer’s current copy:

   ```python
   dirs = sorted(
       (d for d in ckpt.glob("step_*") if d.is_dir()),
       key=lambda d: int(d.name.split("_")[1]),
   )
   victims = dirs[:-1] if keep_latest else dirs
   for d in victims:
       for filename in ("optimizer.pth", "scheduler.pth"):
           (d / filename).unlink(missing_ok=True)
   ```

   Perform the final prune only after the trainer exits. A stronger solution is an explicit completion marker written after upstream finishes publishing `latest`.

6. **Major — `remote/voxcpm2_train.py::main`: the last two saved checkpoints contain identical weights.**

   Upstream saves at the final loop iteration, then saves again after the loop without another update. Consequently, `steps[-3:]` retains only two distinct training states. With `total=150`, the current schedule produces eight directories, including identical final weights at steps 149 and 150—not six distinct checkpoints. See [pinned trainer, lines 349–353](https://github.com/OpenBMB/VoxCPM/blob/f0c787f0937dc1c9a8f4f64d9a332d9c5da2e629/scripts/train_voxcpm_finetune.py#L349-L353).

   **Fix:** remove the redundant final-iteration directory before sampling and selecting retained weights:

   ```python
   if len(steps) >= 2:
       last = int(steps[-1].name.split("_")[1])
       previous = int(steps[-2].name.split("_")[1])
       if last == total and previous == total - 1:
           redundant = steps.pop(-2)
           shutil.rmtree(redundant)
   ```

   Report actual checkpoint counts. Also distinguish completed updates from the trainer’s zero-based step labels.

7. **Major — both remote trainers, `vs_common.py::Job.package`: successful training can be lost during sampling or packaging.**

   Checkpoints remain under `/root/vswork`; the first durable model archive is written only after all sampling. A model-load failure, disk exhaustion, or timeout during that phase causes bootstrap to delete the pod and its trained weights. RunPod documents container storage as ephemeral. See [storage options](https://docs.runpod.io/pods/storage/types).

   Fixed container sizes also omit explicit budgets for checkpoint duplication, copied retained models, extracted audio, and network-volume capacity. A larger container does not increase network-volume space.

   **Fix:** publish retained weights before optional sampling:

   ```python
   # Build ck_meta and copy retained checkpoints first.
   job.package({**meta, "sampling_status": "pending"})
   try:
       generate_checkpoint_samples()
   except Exception as exc:
       log(f"sampling incomplete: {exc}")
       sampling_status = "incomplete"
   else:
       sampling_status = "complete"
   job.package({**meta, "sampling_status": sampling_status})
   ```

   Here `generate_checkpoint_samples()` is a proposed extraction of the existing sampling code. Publish a separate `weights_ready.json` marker so the studio can recover weights even if the later phase fails.

   Calculate required bytes for each filesystem and check both before expensive work. Do not automatically raise every disk allocation without measuring the actual artifact sizes.

8. **Major — `training.py::plan/start`, `runpod.py::create_pod`: the quoted configuration and price are not the configuration necessarily purchased.**

   Overrides are merged **after** planning, so changed epochs/batch size do not affect the quote. The pod request includes more expensive fallback GPUs, but pricing and speed calibration use the originally selected GPU. Furthermore, RunPod defaults `gpuTypePriority` to availability, so list order is not enforced. See [Create Pod: GPU priority and returned costs](https://docs.runpod.io/api-reference/pods/POST/pods).

   **Fix:** construct and validate one effective parameter dictionary before estimation, persist it, and use it remotely. For the first implementation, rent only the GPU covered by the quote:

   ```python
   body["gpuTypeIds"] = gpu_types[:1]
   body["gpuTypePriority"] = "custom"
   ```

   Record the actual returned GPU and hourly charge. Include disk/storage charges separately, and store speed observations against the actual GPU, batch/accumulation settings, attention backend, and representative sequence lengths.

9. **Major — `voxcpm2.py::steps`, `remote/voxcpm2_train.py::main`: the 150-update floor silently overrides the epoch target.**

   For one hour of eight-second clips with approximately 2% validation, about 441 clips remain. The floor runs 2,400 clip presentations: approximately **5.44 epochs**, despite the two-epoch description. This increases overfitting risk and makes the preset misleading. The local estimator also omits the remote 30,000-step cap.

   **Fix:** share the same scheduling function between planning and execution, default the floor to one, and expose effective epochs:

   ```python
   batches_per_epoch = n_train // bs
   if batches_per_epoch == 0:
       raise ValueError("Not enough training clips for this batch size")

   total = math.ceil(batches_per_epoch * epochs / accum)
   total = max(1, min(total, max_steps_cap))
   effective_epochs = total * accum / batches_per_epoch
   ```

   Recompute against the retained dataset if token-length filtering removes samples. The official LoRA configuration provides recipe values, not evidence that 150 updates is appropriate at every dataset size. See [pinned LoRA configuration](https://github.com/OpenBMB/VoxCPM/blob/f0c787f0937dc1c9a8f4f64d9a332d9c5da2e629/conf/voxcpm_v2/voxcpm_finetune_lora.yaml#L6-L18).

10. **Major — `runpod.py::get_json`, `training.py::_cloud_train/resume_interrupted`: storage failures and restart state are mishandled.**

    `get_json()` converts authentication failures, timeouts, malformed JSON, and missing objects into the same `None`. A completed, self-deleted pod can therefore be reported as unexpectedly lost during a transient S3 failure.

    Recovery also uses current settings for bucket/datacenter/deadline and uses training creation time as the resumed start time. Changing settings or spending a long time queued/uploading changes recovery behavior. Registration is not idempotent: a crash after inserting a model but before marking training done can register it again.

    **Fix:** return `None` only for a missing object; propagate other errors to bounded retry logic:

    ```python
    from botocore.exceptions import ClientError

    def get_json(key: str):
        try:
            response = s3().get_object(Bucket=bucket(), Key=key)
            with response["Body"] as stream:
                return json.loads(stream.read())
        except ClientError as exc:
            if exc.response["Error"]["Code"] in {"NoSuchKey", "404"}:
                return None
            raise
    ```

    Freeze storage coordinates and an absolute deadline in the training row. Resume downloading independently of pod existence, enforce uniqueness on `models.training_id`, and distinguish a failed download from failed training.

    For deleting the two known archives, use `delete_object` directly instead of listing a prefix. RunPod documents potentially slow listing/checksum behavior for files produced through the mounted filesystem. See [S3 limitations](https://docs.runpod.io/storage/s3-api#known-issues-and-limitations).

11. **Major — `evaluate.py::evaluate_model`: missing ASR results can win the recommendation.**

    One ASR exception disables ASR for all remaining samples. Candidates with `agree=None` explicitly pass the accuracy filter. A checkpoint with similarity 0.90 and no accuracy score beats one with similarity 0.70 and accuracy 0.95; I reproduced this using the supplied rule. Partial sample sets also qualify.

    **Fix:** require complete, finite scores for the selected comparison condition:

    ```python
    eligible = [
        r for r in cands
        if r["agree"] is not None
        and np.isfinite(r["agree"])
        and np.isfinite(r["sim"])
        and len(r["clips"]) == expected_clip_count
        and all(c["agree"] is not None for c in r["clips"])
    ]

    rec = None
    if eligible:
        best_agree = max(r["agree"] for r in eligible)
        acceptable = [
            r for r in eligible
            if r["agree"] >= best_agree - 0.05
        ]
        rec = max(acceptable, key=lambda r: r["sim"])["name"]
    ```

    Retry/report ASR failures per clip. Incomplete evaluation must leave the selected checkpoint unchanged and say that no recommendation was produced.

12. **Major — `evaluate.py`, both remote sample generators: the aggregate recommendation mixes different questions.**

    VoxCPM averages unassisted and reference-assisted speech. A strong reference can conceal weak speaker learning in the checkpoint. Qwen’s “base/plain” sample actually uses reference cloning, usually with a transcript, while its trained “plain” sample uses a stored speaker identity. These are useful listening comparisons, but they are not equivalent conditions.

    The evaluator also always chooses among retained trained checkpoints, even if all regress against the base. Six sentences and one seed give weak evidence for a universal recommendation.

    **Fix:** store the actual generation condition and calculate separate summaries:

    ```python
    # Example metadata attached to each generated sample:
    sample_meta = {
        "mode": "hifi",
        "reference_id": ref.get("id"),
        "seed": SEED,
        "seen_in_training": bool(line.get("seen")),
    }

    # Aggregate by checkpoint, mode, and language.
    comparison_key = (checkpoint_name, sample_meta["mode"], line["lang"])
    ```

    Recommend separately for `plain` and `ref`; assess `hifi` separately if it is offered locally. Exclude `seen=True` samples from automatic selection. Report base regression and permit “no improvement” rather than always changing the default.

    Label cosine as **speaker-embedding similarity**, not probability or percentage identity. Rename `ground_truth_sim` to “real-audio similarity baseline”; it is not a mathematical ceiling. I cannot certify that `asr.agreement()` represents WER/CER because its implementation was not supplied.

13. **Major — `remote/voxcpm2_train.py`, `voxcpm2.py::load`, Qwen model downloads: code is pinned, model assets are not reliably pinned.**

    VoxCPM training accepts `base_revision`, but local LoRA loading ignores it and downloads the current base. A LoRA can therefore be applied to different weights/tokenizer assets from those used in training. Qwen’s base and tokenizer revisions are also unrecorded.

    Do **not** fix VoxCPM by adding `revision=` to its wrapper: the pinned wrapper forwards extra arguments to its constructor rather than to `snapshot_download`. See [pinned `core.py`, lines 97–161](https://github.com/OpenBMB/VoxCPM/blob/f0c787f0937dc1c9a8f4f64d9a332d9c5da2e629/src/voxcpm/core.py#L97-L161).

    **Fix:** record resolved snapshot commits and load the matching local snapshot:

    ```python
    # Training metadata:
    resolved_revision = Path(base_path).name

    # Local LoRA loading:
    base_path = snapshot_download(
        meta["base"], revision=meta["base_revision"]
    )
    m = VoxCPM.from_pretrained(
        base_path,
        lora_weights_path=str(ck),
        load_denoiser=False,
        optimize=False,
    )
    ```

    Store the resolved commit, not an optional branch name or `None`. Record Qwen’s base and tokenizer commits similarly.

14. **Major — `tts.py::_handle/generate`, `base.py::unload`, `evaluate.py`: GPU ownership does not cover model loading and scoring.**

    `_handle()` loads outside `GPU_LOCK`. Concurrent requests can load a second model while the first is synthesizing. A request retains its handle even after another request switches `_loaded`. ASR screening can also run while TTS weights remain resident.

    `del handle` only removes the callee’s reference; garbage collection and `empty_cache()` run while the caller still owns the model. This does not prove a permanent leak in serial execution, but it does make cleanup occur at the wrong time.

    **Fix:** serialize model acquisition, loading, inference, unloading, and GPU-based scoring through one GPU executor. Release owned objects before collection:

    ```python
    def unload(self, handle):
        import gc
        import torch

        handle.clear()  # Current adapters return owned handle dictionaries.
        gc.collect()
        torch.cuda.empty_cache()
    ```

    Apply this only after the ownership/locking fix; otherwise it could invalidate an active request. Move `_handle()` inside the same critical section as synthesis, and account for persistent ASR/embedding models before claiming that an 8-GB GPU is sufficient.

15. **Major — `remote/__init__.py::SETUP_TEMPLATE`, `install.py::install_engine`, `qwen3.py`: package discovery is being mistaken for a working installation.**

    `find_spec()` succeeds for packages whose native extensions cannot load. Thus a broken FlashAttention installation can be selected rather than falling back to SDPA, and Windows installation can report success despite DLL failures. The cloud package check does not exercise the trainer or audio decoder.

    The setup script also tests only `ffmpeg`, so an existing FFmpeg executable skips installation of a missing SoX executable. Package-install failures are suppressed. Finally, a readiness stamp keyed only by upstream commit survives changes to the setup recipe and image ABI.

    The wheel URL names an existing release asset; compatibility must still be checked against the actual interpreter, Torch build, and ABI. See [FlashAttention release assets](https://github.com/Dao-AILab/flash-attention/releases/expanded_assets/v2.8.3). TorchCodec requires FFmpeg shared libraries, which matters on Windows. See [TorchCodec installation](https://github.com/meta-pytorch/torchcodec#installing-torchcodec).

    **Fix:**

    ```bash
    if ! command -v ffmpeg >/dev/null || ! command -v sox >/dev/null; then
      apt-get update -qq
      DEBIAN_FRONTEND=noninteractive apt-get install -y -qq ffmpeg sox
    fi
    ```

    Use an actual native-extension probe before selecting FlashAttention:

    ```python
    try:
        import flash_attn
        import flash_attn_2_cuda
    except (ImportError, OSError, RuntimeError):
        attn = "sdpa"
    else:
        attn = "flash_attention_2"
    ```

    Remove an unusable optional installation if it also breaks Transformers import. Before stamping readiness, run public-class imports and decode a short WAV in a fresh subprocess. Key the stamp by recipe hash, image digest, Python/Torch versions, and upstream commit. For local installation, require an application restart after dependency changes; invalidating import caches does not reload already imported libraries.

16. **Major — `server.py::guard`: loopback bypass is not sufficient authentication for a browser-accessible application.**

    The guard trusts any loopback-origin connection without validating its `Host` or browser `Origin`. This leaves a DNS-rebinding exposure; a local reverse proxy can also turn remote clients into trusted loopback clients, depending on forwarding configuration. LAN passwords are transmitted over plain HTTP in the shown server configuration.

    **Fix:** validate allowed hosts, reject foreign browser origins on state-changing requests, and require authentication independently of apparent client IP when network access is enabled:

    ```python
    from starlette.middleware.trustedhost import TrustedHostMiddleware

    app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=["localhost", "127.0.0.1", "[::1]"],
        www_redirect=False,
    )
    ```

    Add only explicitly configured LAN hostnames/IPs. Use a local session token or authenticated session for mutating API requests, and HTTPS for password-bearing LAN access. Do not assume a direct LAN client can spoof forwarded headers under default Uvicorn settings; that depends on the trusted-proxy configuration. See [Starlette’s host validation](https://github.com/encode/starlette/blob/master/starlette/middleware/trustedhost.py) and [Uvicorn proxy settings](https://uvicorn.dev/settings/#http).

17. **Major — `tts.py::generate`, `training.py::_cloud_train`: consent checks do not follow queued work and existing models.**

    Consent is checked when training is submitted or a zero-shot model is created. Generation does not recheck it, and queued training can upload audio after consent has been withdrawn. This conflicts with the stated consent boundary.

    **Fix:** recheck current consent before model loading, before upload, and before pod creation:

    ```python
    voice = db.get("voices", m["voice_id"])
    if not voice or not datasets.consent_ok(voice):
        raise datasets.ConsentMissing(
            "Current consent does not permit synthesis."
        )
    ```

    Use the analogous check with `tr["voice_id"]` for cloud work. Validate the dataset’s consent snapshot as well. Keep the “no talent audio” restriction explicit in voice eligibility; the supplied code does not show how that restriction is represented.

18. **Major at the function boundary — `training.py::remove_reference`: `ref_id` can escape the references directory.**

    The function constructs a deletion path directly from the argument, even if that ID does not exist in the model’s references. An argument containing `../` can target another `.wav` file. I reproduced the path escape; whether an API route currently permits such input cannot be established from the supplied files.

    **Fix:** require a registered reference and constrain the resolved path:

    ```python
    refs = m["meta"].get("references", [])
    ref = next((r for r in refs if r["id"] == ref_id), None)
    if ref is None:
        raise KeyError(ref_id)

    root = (Path(m["path"]) / "references").resolve()
    target = (Path(m["path"]) / ref["file"]).resolve()
    if target.parent != root:
        raise ValueError("Invalid reference path")
    target.unlink(missing_ok=True)
    ```

    Validate checkpoint names and reference paths when importing `engine.json` too. Safe tar extraction does not validate paths later read from metadata.

**3. Defaults table**

These are proposed first-run settings and implementation changes, not claims of measured optimal training quality.

| Parameter | Old value | Proposed value | Reason |
|---|---:|---:|---|
| VoxCPM minimum updates | 150 | 1; derive updates from requested epochs | Avoid silently multiplying small-dataset exposure. |
| VoxCPM full retention | Last 3 directories | Last 3 **distinct** checkpoints | Final two upstream directories duplicate weights. |
| Qwen training reference rate | Unchecked | Mono, 24,000 Hz | Required by the pinned dataset loader. |
| Qwen SFT inference language | Explicit JA/EN | `Auto` by default | Match the unchanged training prefix. |
| Qwen tokenizer preparation batch | Upstream constant 32 | 4 for the first memory probe; increase after measurement | Bound preparation memory independently of training batch size. This requires an adapter patch, not an invented CLI flag. |
| GPU fallback | Entire preset list | Selected GPU only initially | Keep the purchase within the quote. |
| Minimum host RAM | Omitted; API default 8 GB | 32 GB LoRA; 64 GB full/SFT initially | Provide room for CPU weights, checkpoint conversion, and preprocessing; verify peaks. |
| Container disk | Fixed 80/250/120 GB | `max(preset_size, calculated_peak_with_margin)` | Budget extracted data, live saves, `latest`, and packaging copies. |
| Network-volume capacity | Not checked | Independent capacity budget and free-space check | Models, environments, caches, and archives use this filesystem. |
| Evaluation text count | 6 total | 24 total, balanced JA/EN | More useful coverage; expand across recordings and difficult text. |
| Automatic recommendation | Allows missing/partial ASR | Complete matched samples required | Prevent unsupported recommendations. |
| Initial integration-run deadline | 12 hours | 45–60 minutes, with verified independent cleanup | Test installation, a few updates, packaging, and recovery before a long run. |

The requested GPU VRAM classes are plausible starting points, but neither “48 GB fits LoRA” nor “80 GB fits full training” is established by the recipes alone. Host RAM, audio/reference length, attention backend, validation, and checkpoint-writing peaks must be measured.

**4. Open questions**

| Question requiring the target runtime | Cheapest useful experiment |
|---|---|
| Does the exact RunPod image install, run the pinned trainers, and self-delete with its pod-scoped credentials? | After fixing cleanup, run one short pod with four consented clips, two updates, one checkpoint reload, and one synthesized line. Test success and deliberate failure; confirm deletion from an independent watcher. |
| What are actual VRAM, host-RAM, disk, and step-time requirements? | Run 10–20 updates on the longest target/reference pairs: VoxCPM LoRA on the selected 48-GB GPU, then full/SFT on 80 GB. Measure preparation, validation, saving, and inference peaks separately. |
| Does Qwen SFT retain reliable JA/EN output and useful style control? | Train one short balanced subset for one epoch. Compare `Auto` against explicit JA/EN on identical held-out text and seeds. Test style instructions separately from the accuracy comparison. |
| Does fine-tuning improve this speaker over reference cloning, and which checkpoint/mode is best? | Start with the smallest representative consented dataset. Keep distinct checkpoints and compare matched modes on held-out recordings, with ASR scores and blind listening. Expand training only if the pilot shows benefit. |
| Does Windows inference work within the user’s actual memory budget? | Install into a disposable Windows environment; import both public model classes, decode a WAV, synthesize one line per mode, switch models repeatedly, and run ASR screening. Observe DLL errors and peak/residual VRAM. |

## The fixed code (voice-studio/, commit 58723ff)

### `vstudio/cloud/bootstrap/bootstrap.sh`

```bash
#!/bin/bash
# Voice Studio cloud training bootstrap. Runs as the pod's start command on RunPod.
# Everything lives on the network volume under /workspace/vs, so the engine environment is installed only once
# and the outputs survive the pod. The pod removes itself when it finishes, fails, is signalled or hits the time
# limit; removal is retried until RunPod confirms it. The studio and its orphan check remove it too.
set -uo pipefail
set -m   # background jobs get their own process group, so the watchdog can stop all of the work at once
VS_ROOT="${VS_ROOT:-/workspace/vs}"   # the network volume (overridable only for local tests)
JOB="$VS_ROOT/jobs/${VS_TRAINING_ID}"
export VS_ROOT HF_HOME="$VS_ROOT/hf" PYTHONUNBUFFERED=1 VS_SRC="$VS_ROOT/src/${VS_ENGINE}" VS_WORK="${VS_WORK:-/root/vswork}"
mkdir -p "$JOB"
exec > >(tee -a "$JOB/train.log") 2>&1
echo "[vs] start $(date -u +%FT%TZ) pod=${RUNPOD_POD_ID:-?} gpu=$(nvidia-smi --query-gpu=name,memory.total --format=csv,noheader 2>/dev/null) disk=$(df -h /root | tail -1 | awk '{print $4}') free"

VS_DATA="${VS_DATA:-/root/vsdata}"
STAGE_FILE="${VS_WORK}.stage"
WORK_PID=""
FINISHING=0

finish() {
  [ "$FINISHING" = 1 ] && return
  FINISHING=1
  echo "[vs] finishing: $1"
  if [ -n "$WORK_PID" ]; then
    kill -TERM -- "-$WORK_PID" 2>/dev/null; sleep "${VS_KILL_GRACE:-5}"; kill -KILL -- "-$WORK_PID" 2>/dev/null
  fi
  timeout 30s sync || true
  local n=0
  until timeout 30s runpodctl remove pod "${RUNPOD_POD_ID:?}"; do
    n=$((n + 1))
    echo "[vs] pod removal failed (attempt $n); retrying"
    # stopping releases the GPU (the expensive part) even if deletion keeps failing
    [ "$n" = 3 ] && timeout 30s runpodctl stop pod "${RUNPOD_POD_ID}"
    sleep $(( n < 6 ? ${VS_RETRY_SLEEP:-10} : 60 ))
  done
  sleep "${VS_FINISH_SLEEP:-300}"   # the pod is being deleted; never fall through to restarting work
  exit 0
}
fail() {
  printf '{"status":"error","stage":"%s","at":"%s"}\n' "$1" "$(date -u +%FT%TZ)" > "$JOB/error.json"
  finish "error in $1"
}
on_timeout() {
  printf '{"status":"timeout","stage":"%s","at":"%s"}\n' "$(cat $STAGE_FILE 2>/dev/null)" "$(date -u +%FT%TZ)" > "$JOB/error.json"
  finish timeout
}
trap on_timeout USR1
trap 'finish signal' TERM INT HUP
trap 'finish exit' EXIT

run_work() {
  echo setup > $STAGE_FILE
  echo '{"phase":"setup"}' > "$JOB/progress.json"
  bash "$JOB/setup_env.sh" || return 1
  echo unpack > $STAGE_FILE
  echo '{"phase":"unpack"}' > "$JOB/progress.json"
  mkdir -p "$VS_DATA" && tar -xf "$JOB/dataset.tar" -C "$VS_DATA" || return 1
  echo train > $STAGE_FILE
  # shellcheck disable=SC1090
  source "$VS_ROOT/envs/${VS_ENGINE}/bin/activate" || return 1
  python "$JOB/train_entry.py" --config "$JOB/config.json" --data "$VS_DATA"
}

# hard time limit, independent of the training process
( sleep "${VS_MAX_SECONDS:-43200}"; kill -USR1 $$ ) &

run_work &
WORK_PID=$!
wait "$WORK_PID"
rc=$?
WORK_PID=""

# model.tar is written atomically as soon as the weights are ready, before the optional sample phase,
# so a failure while sampling still delivers the trained model
if [ -f "$JOB/model.tar" ]; then
  printf '{"status":"done","rc":%d,"samples":%s,"at":"%s"}\n' "$rc" \
    "$([ -f "$JOB/samples.tar" ] && echo true || echo false)" "$(date -u +%FT%TZ)" > "$JOB/done.json"
  finish done
fi
fail "$(cat $STAGE_FILE 2>/dev/null || echo unknown)"

```

### `vstudio/engines/remote/__init__.py`

```python
"""Files the engines upload next to bootstrap.sh for a cloud training run."""
from __future__ import annotations

import hashlib
from pathlib import Path

HERE = Path(__file__).parent

SETUP_TEMPLATE = r"""#!/bin/bash
# Installs the {name} training environment on the network volume. It runs at the start of every training run but
# installs only once per pinned version: later runs find the stamp file and skip straight to training.
set -euo pipefail
ENV="${{VS_ROOT:-/workspace/vs}}/envs/{engine}"
SRC="${{VS_ROOT:-/workspace/vs}}/src/{engine}"
# the stamp names the exact recipe (this script), the image's Python/torch build and the upstream commit
STAMP="$ENV/.ready-{recipe}-$(python3 -c 'import sys,torch;print(f"py{{sys.version_info[0]}}{{sys.version_info[1]}}-torch{{torch.__version__}}")' 2>/dev/null)"

# system packages live on the container disk, so they are checked on every run (fast when present)
if ! command -v ffmpeg >/dev/null 2>&1 || ! command -v sox >/dev/null 2>&1; then
  apt-get update -qq && DEBIAN_FRONTEND=noninteractive apt-get install -y -qq ffmpeg sox >/dev/null
fi

if [ -f "$STAMP" ]; then echo "[vs] {engine} environment ready"; exit 0; fi
echo "[vs] installing {engine} environment (first run only, about 10 minutes)"
rm -rf "$ENV" "$SRC"
python3 -m venv --system-site-packages "$ENV" || {{ pip install -q virtualenv && python3 -m virtualenv --system-site-packages "$ENV"; }}
source "$ENV/bin/activate"
python -m pip install -q --upgrade pip wheel
# keep the image's CUDA build of torch; never let a dependency replace it
python - <<'PY' > "$ENV/constraints.txt"
import torch, torchaudio
t = torch.__version__.split("+")[0]
print(f"torch=={{t}}"); print(f"torchaudio=={{torchaudio.__version__.split('+')[0]}}")
codec = {{"2.6": "0.2.*", "2.7": "0.5.*", "2.8": "0.7.*", "2.9": "0.8.*"}}.get(".".join(t.split(".")[:2]))
if codec: print(f"torchcodec=={{codec}}")
PY
cat "$ENV/constraints.txt"
mkdir -p "$SRC" && cd "$SRC"
git init -q && git fetch -q --depth 1 {repo} {commit} && git checkout -q FETCH_HEAD
export SETUPTOOLS_SCM_PRETEND_VERSION={version}
pip install -q -c "$ENV/constraints.txt" -e "$SRC" {extra_pip}
{post}
# smoke test in a fresh interpreter: the public model class imports and audio decodes
python - <<'PY'
import numpy as np, soundfile as sf, librosa
from {module} import {cls}
sf.write("/tmp/vs_probe.wav", np.zeros(16000, dtype="float32"), 16000)
y, sr = librosa.load("/tmp/vs_probe.wav", sr=24000)
assert len(y) == 24000, len(y)
print("[vs] {module}.{cls} import and audio decode ok")
PY
touch "$STAMP"
"""


def setup_script(engine: str, name: str, repo: str, commit: str, version: str, module: str, cls: str,
                 extra_pip: str = "", post: str = "") -> str:
    fields = dict(engine=engine, name=name, repo=repo, commit=commit, version=version, module=module, cls=cls,
                  extra_pip=extra_pip, post=post)
    recipe = hashlib.sha256(SETUP_TEMPLATE.format(recipe="", **fields).encode()).hexdigest()[:12]
    return SETUP_TEMPLATE.format(recipe=recipe, **fields)


def read(name: str) -> str:
    return (HERE / name).read_text(encoding="utf-8")

```

### `vstudio/engines/remote/vs_common.py`

```python
"""Helpers shared by the engines' cloud training entry points.

This file runs on the rented GPU machine (inside the engine's environment), not on your PC. It is uploaded next to
bootstrap.sh for every training run. It only uses the standard library so it works in any engine environment.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tarfile
import threading
import time
from pathlib import Path

LANG_NAMES = {"ja": "Japanese", "en": "English", "zh": "Chinese", "ko": "Korean", "de": "German", "fr": "French",
              "ru": "Russian", "pt": "Portuguese", "es": "Spanish", "it": "Italian"}


def log(msg: str) -> None:
    print(f"[vs] {msg}", flush=True)


class Job:
    """One training run: paths, parameters, progress reporting and packaging."""

    def __init__(self) -> None:
        argv = sys.argv
        self.config_path = Path(argv[argv.index("--config") + 1]).resolve()
        self.dir = self.config_path.parent                      # on the network volume (visible to the studio)
        self.data = Path(argv[argv.index("--data") + 1]) / "data"  # unpacked dataset (container disk)
        self.cfg = json.loads(self.config_path.read_text(encoding="utf-8"))
        self.params: dict = self.cfg.get("params", {})
        self.work = Path(os.environ.get("VS_WORK", "/root/vswork"))
        self.work.mkdir(parents=True, exist_ok=True)
        self.out = self.work / "model"                           # becomes model.tar → model/
        self.out.mkdir(parents=True, exist_ok=True)
        self._t0 = time.time()
        self._train_t0: float | None = None
        self._train_s0 = 0
        self._state: dict = {}

    # progress.json is read by the studio every 30 s over the S3 API
    def progress(self, **kw) -> None:
        self._state.update(kw)
        now = time.time()
        self._state["elapsed_s"] = int(now - self._t0)
        if kw.get("phase") == "train":  # measured speed, used by the studio to calibrate future estimates
            if self._train_t0 is None:
                self._train_t0, self._train_s0 = now, int(kw.get("step") or 0)
            elif (kw.get("step") or 0) > self._train_s0 + 2:
                self._state["s_per_step"] = round((now - self._train_t0) / (kw["step"] - self._train_s0), 3)
        tmp = self.dir / "progress.json.tmp"
        tmp.write_text(json.dumps(self._state), encoding="utf-8")
        os.replace(tmp, self.dir / "progress.json")

    def read_jsonl(self, name: str) -> list[dict]:
        f = self.data / name
        if not f.exists():
            return []
        return [json.loads(x) for x in f.read_text(encoding="utf-8").splitlines() if x.strip()]

    def run(self, cmd: list[str], cwd: Path | None = None, on_line=None, env: dict | None = None) -> None:
        """Run a command, echo its output to train.log and feed each line to on_line; raise on failure."""
        log("$ " + " ".join(str(c) for c in cmd))
        p = subprocess.Popen([str(c) for c in cmd], cwd=str(cwd) if cwd else None, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT, text=True, bufsize=1, env={**os.environ, **(env or {})},
                             errors="replace")
        assert p.stdout is not None
        for line in p.stdout:
            sys.stdout.write(line)
            if on_line:
                try:
                    on_line(line.rstrip("\n"))
                except Exception as e:  # progress parsing must never stop training
                    log(f"progress parse: {e}")
        code = p.wait()
        if code != 0:
            raise RuntimeError(f"command failed with exit code {code}: {cmd[:3]}")

    def package(self, meta: dict, name: str = "model.tar", entries: list[tuple[Path, str]] | None = None) -> None:
        """Write engine.json and pack an archive on the network volume (atomic rename).

        model.tar (weights + engine.json) is written first, as soon as the weights are final; samples.tar
        (sample clips + the final engine.json) follows after the optional sample phase. The studio needs only
        model.tar, so a failure while sampling never loses a trained model."""
        meta = {**meta, "training_id": self.cfg.get("training_id"), "params": self.params,
                "train_seconds": int(time.time() - self._t0)}
        (self.out / "engine.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
        self.progress(phase="package")
        skip = {"optimizer.pth", "scheduler.pth", "training_state.json"}

        def keep(ti: tarfile.TarInfo):
            return None if Path(ti.name).name in skip else ti

        tmp = self.dir / f"{name}.tmp"
        with tarfile.open(tmp, "w") as t:
            for src, arc in entries if entries is not None else [(self.out, "model")]:
                t.add(src, arcname=arc, filter=keep)
            if entries is not None:
                t.add(self.out / "engine.json", arcname="model/engine.json")
        os.replace(tmp, self.dir / name)
        log(f"packaged {name}: {(self.dir / name).stat().st_size / 1e9:.2f} GB")


def sample_plan(job: Job) -> dict:
    """The held-out lines every checkpoint reads aloud, so checkpoints can be compared by ear and by score."""
    f = job.data / "samples.json"
    return json.loads(f.read_text(encoding="utf-8")) if f.exists() else {"lines": [], "reference": None}


def free_gb(path: str = "/root") -> float:
    return shutil.disk_usage(path).free / 1e9


def need_disk(gb: float, path: str = "/root") -> None:
    """Fail early (before paying for hours of training) when the container disk cannot hold the outputs."""
    have = free_gb(path)
    if have < gb:
        raise RuntimeError(f"not enough disk on {path}: {have:.0f} GB free, about {gb:.0f} GB needed")


def resolved_revision(snapshot_path: str) -> str:
    """huggingface_hub snapshot folders are named after the commit, so the exact base weights can be re-fetched."""
    return Path(snapshot_path).name


class LogTail(threading.Thread):
    """Follow a log file written by a trainer and call on_line for each new line."""

    def __init__(self, path: Path, on_line) -> None:
        super().__init__(daemon=True)
        self.path, self.on_line, self.stop = path, on_line, threading.Event()

    def run(self) -> None:
        pos = 0
        while not self.stop.is_set():
            if self.path.exists():
                with self.path.open("r", encoding="utf-8", errors="replace") as f:
                    f.seek(pos)
                    for line in f:
                        try:
                            self.on_line(line.rstrip("\n"))
                        except Exception:
                            pass
                    pos = f.tell()
            self.stop.wait(2)


METRIC = re.compile(r"([\w/]+):\s*(-?[\d.]+(?:e-?\d+)?)")


def parse_metrics(s: str) -> dict:
    return {k: float(v) for k, v in METRIC.findall(s)}

```

### `vstudio/engines/remote/voxcpm2_train.py`

```python
#!/usr/bin/env python3
"""VoxCPM2 fine-tuning on the cloud GPU (runs inside /workspace/vs/envs/voxcpm2).

1. writes a training config from the studio's effective parameters (LoRA or full fine-tuning, official recipe);
2. runs the official trainer (scripts/train_voxcpm_finetune.py from the pinned VoxCPM commit);
3. publishes model.tar with the distinct checkpoints as soon as training ends;
4. every checkpoint, plus the untrained base model, reads the same held-out lines aloud (model only, and with a
   reference clip), so checkpoints can be compared by ear and scored by the studio; these go into samples.tar.
"""
from __future__ import annotations

import json
import math
import os
import shutil
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vs_common import Job, LogTail, log, need_disk, parse_metrics, resolved_revision, sample_plan  # noqa: E402

SRC = Path(os.environ.get("VS_SRC", "/workspace/vs/src/voxcpm2"))
BASE = "openbmb/VoxCPM2"
SEED = 1234


def count_lines(p: Path) -> int:
    return sum(1 for x in p.read_text(encoding="utf-8").splitlines() if x.strip())


def schedule(n_train: int, p: dict) -> tuple[int, int]:
    """(updates per epoch, total updates). The studio computes the same numbers for its quote and sends
    total_steps; this fallback is only used when it is missing."""
    bs, accum = int(p.get("batch_size", 2)), int(p.get("grad_accum", 8))
    batches = n_train // bs  # the trainer drops the last incomplete batch
    if batches < accum:
        raise RuntimeError(f"only {n_train} training clips: need at least {bs * accum} for one update")
    per_epoch = batches // accum
    total = int(p.get("total_steps") or max(1, math.ceil(batches * float(p.get("epochs", 2)) / accum)))
    return per_epoch, min(total, int(p.get("max_steps_cap", 30000)))


def step_of(d: Path) -> int:
    return int(d.name.split("_")[1])


def main() -> None:
    job = Job()
    p = job.params
    mode = p.get("mode", "lora")
    from huggingface_hub import snapshot_download

    job.progress(phase="download")
    base_path = snapshot_download(BASE, revision=p.get("base_revision") or None)
    revision = resolved_revision(base_path)
    log(f"base model {BASE}@{revision}")

    train_manifest, val_manifest = job.data / "train.jsonl", job.data / "val.jsonl"
    n_train = count_lines(train_manifest)
    per_epoch, total = schedule(n_train, p)
    n_saves = int(p.get("saves", 6))
    save_every = max(10, math.ceil(total / n_saves))
    # full fine-tuning: each checkpoint ~8 GB of weights, plus optimizer state in `latest` and the archive copy
    need_disk(25 if mode == "lora" else 9 * (n_saves + 2) + 30)
    ckpt = job.work / "ckpt"
    conf = {
        "pretrained_path": base_path,
        "train_manifest": str(train_manifest),
        "val_manifest": str(val_manifest) if val_manifest.exists() and count_lines(val_manifest) else "",
        "sample_rate": 16000,
        "out_sample_rate": 48000,
        "batch_size": int(p.get("batch_size", 2)),
        "grad_accum_steps": int(p.get("grad_accum", 8)),
        "num_workers": 4,
        "preprocessing_num_workers": 4,
        "num_iters": total,
        "max_steps": total,
        "log_interval": 5,
        "valid_interval": save_every,
        "save_interval": save_every,
        "learning_rate": float(p.get("lr", 1e-4 if mode == "lora" else 1e-5)),
        "weight_decay": 0.01,
        "warmup_steps": max(1, min(100, total // 10)),
        "max_batch_tokens": int(p.get("max_batch_tokens", 8192)),
        "max_grad_norm": 1.0,
        "save_path": str(ckpt),
        "tensorboard": str(job.work / "tb"),
        "lambdas": {"loss/diff": 1.0, "loss/stop": 1.0},
    }
    if mode == "lora":
        conf["lora"] = {"enable_lm": True, "enable_dit": True, "enable_proj": bool(p.get("lora_proj", False)),
                        "r": int(p.get("rank", 32)), "alpha": int(p.get("alpha", 32)), "dropout": 0.0}
    conf_path = job.work / "train_conf.yaml"
    conf_path.write_text(json.dumps(conf, indent=2), encoding="utf-8")  # JSON is valid YAML
    log(f"{mode}: {n_train} clips, {per_epoch} updates/epoch, {total} updates "
        f"({total / per_epoch:.2f} epochs), save every {save_every}")
    job.progress(phase="train", step=0, total=total, per_epoch=per_epoch, mode=mode)

    metrics_f = (job.out / "train_metrics.jsonl").open("w", encoding="utf-8")

    def on_line(line: str) -> None:
        # "[train] step 120: loss/diff: 0.41, loss/stop: 0.01, lr: ..., epoch: 1.2, grad_norm: ..."
        if line.startswith("[train] step ") or line.startswith("[val] step "):
            split = line[1:line.index("]")]
            step = int(line.split("step ", 1)[1].split(":", 1)[0])
            m = parse_metrics(line.split(":", 1)[1])
            metrics_f.write(json.dumps({"split": split, "step": step + 1, **m}) + "\n")
            metrics_f.flush()
            loss = m.get("loss/diff", 0) + m.get("loss/stop", 0)
            if split == "train":
                job.progress(phase="train", step=step + 1, total=total, loss=round(loss, 4),
                             epoch=round(m.get("epoch", 0), 2))
            else:
                job.progress(val_loss=round(loss, 4))
        if mode == "full":
            prune_optimizer_states(ckpt, keep_newest=True)

    tail = LogTail(ckpt / "train.log", on_line)
    tail.start()
    job.run([sys.executable, SRC / "scripts" / "train_voxcpm_finetune.py", "--config_path", conf_path], cwd=SRC)
    tail.stop.set()
    tail.join(5)
    metrics_f.close()
    prune_optimizer_states(ckpt, keep_newest=False)

    # The trainer saves at step 0 (after one update), every save_every, at the last loop step (total-1) and once
    # more after the loop (total) with identical weights. Keep distinct, trained checkpoints only.
    steps = sorted((d for d in ckpt.iterdir() if d.is_dir() and d.name.startswith("step_")), key=step_of)
    if len(steps) >= 2 and step_of(steps[-1]) == total and step_of(steps[-2]) == total - 1:
        shutil.rmtree(steps.pop(-2), ignore_errors=True)
    if len(steps) >= 2 and step_of(steps[0]) == 0:
        shutil.rmtree(steps.pop(0), ignore_errors=True)
    if not steps:
        raise RuntimeError("trainer produced no checkpoints")
    keep = steps if mode == "lora" else steps[-int(p.get("keep_full", 3)):]
    log(f"checkpoints: {[d.name for d in steps]}; keeping weights of {[d.name for d in keep]}")
    # step_N holds the weights after N+1 updates (zero-based loop counter), except the final save at `total`
    updates = {d.name: (step_of(d) if step_of(d) == total else step_of(d) + 1) for d in steps}
    ck_meta = [{"name": d.name, "step": updates[d.name], "epoch": round(updates[d.name] / per_epoch, 2),
                "weights": d in keep} for d in steps]
    meta = {"engine": "voxcpm2", "mode": mode, "base": BASE, "base_revision": revision, "checkpoints": ck_meta,
            "samples": sample_plan(job), "sample_rate": 48000, "total_steps": total, "per_epoch": per_epoch,
            "seed": SEED, "sampling": "pending"}
    job.package(meta, "model.tar", [(job.out / "train_metrics.jsonl", "model/train_metrics.jsonl")]
                + [(d, f"model/checkpoints/{d.name}") for d in keep])

    try:
        conditions = sample_all(job, base_path, mode, steps)
        meta.update(sampling="complete", sample_conditions=conditions)
    except Exception as e:  # the model is already safe in model.tar
        log(f"sampling incomplete: {e}")
        meta.update(sampling="incomplete", sampling_error=str(e)[:300])
    if (job.out / "samples").exists():
        job.package(meta, "samples.tar", [(job.out / "samples", "model/samples")])


def sample_all(job: Job, base_path: str, mode: str, steps: list[Path]) -> dict:
    """Each checkpoint (and the base) reads the held-out lines: 'plain' = the model alone, 'ref' = with the same
    reference clip. Seeds are fixed so the only difference between clips is the checkpoint."""
    plan = sample_plan(job)
    ref = plan.get("reference")
    ref_path = str(job.data / ref["audio"]) if ref else None
    import soundfile as sf
    from voxcpm import VoxCPM

    job.progress(phase="samples", step=0, total=len(steps) + 1)

    def speak(model, name: str) -> None:
        d = job.out / "samples" / name
        d.mkdir(parents=True, exist_ok=True)
        for i, line in enumerate(plan.get("lines", [])):
            for kind in ("plain", "ref"):
                if kind == "ref" and not ref_path:
                    continue
                try:
                    wav = model.generate(text=line["text"], reference_wav_path=ref_path if kind == "ref" else None,
                                         cfg_value=2.0, inference_timesteps=10, seed=SEED)
                    sf.write(str(d / f"{i}_{kind}.wav"), wav, model.tts_model.sample_rate)
                except Exception as e:
                    log(f"sample {name}/{i}_{kind} failed: {e}")

    if mode == "lora":
        model = VoxCPM.from_pretrained(base_path, load_denoiser=False, optimize=False,
                                       lora_weights_path=str(steps[0]))
        model.set_lora_enabled(False)
        speak(model, "base")
        model.set_lora_enabled(True)
        for i, d in enumerate(steps):
            model.load_lora(str(d))
            speak(model, d.name)
            job.progress(phase="samples", step=i + 2, total=len(steps) + 1)
        del model
    else:
        model = VoxCPM.from_pretrained(base_path, load_denoiser=False, optimize=False)
        speak(model, "base")
        del model
        for i, d in enumerate(steps):
            model = VoxCPM.from_pretrained(str(d), load_denoiser=False, optimize=False)
            speak(model, d.name)
            del model
            job.progress(phase="samples", step=i + 2, total=len(steps) + 1)
    return {"plain": {"mode": "plain", "seed": SEED},
            "ref": {"mode": "ref", "reference": (ref or {}).get("id"), "seed": SEED}}


def prune_optimizer_states(ckpt: Path, keep_newest: bool) -> None:
    """Full fine-tuning saves ~3× the model size of optimizer state per checkpoint. While training runs, the newest
    step folder may still be being copied into `latest`, so it is left alone; older ones are safe to trim."""
    if not ckpt.exists():
        return
    dirs = sorted((d for d in ckpt.glob("step_*") if d.is_dir()), key=step_of)
    for d in dirs[:-1] if keep_newest else dirs:
        for f in ("optimizer.pth", "scheduler.pth"):
            (d / f).unlink(missing_ok=True)
    if not keep_newest:
        shutil.rmtree(ckpt / "latest", ignore_errors=True)


if __name__ == "__main__":
    main()

```

### `vstudio/engines/remote/qwen3_train.py`

```python
#!/usr/bin/env python3
"""Qwen3-TTS-12Hz-1.7B-Base single-speaker fine-tuning on the cloud GPU (runs inside /workspace/vs/envs/qwen3).

Follows the official finetuning/ recipe of the pinned Qwen3-TTS commit:
prepare_data.py (extract 12 Hz audio codes) → sft_12hz.py (full SFT, one checkpoint per epoch).
model.tar is published right after training; then every epoch's checkpoint reads the held-out lines aloud
(samples.tar), next to the untrained base model cloning from the reference clip, for comparison.

Notes from the pinned code:
- dataset.py loads ref_audio at its native rate and asserts 24 kHz, so the reference is resampled first;
- dataset.py reads `language` but does not use it (the prompt prefix is the auto-language one), so checkpoints
  are sampled with language="Auto" to match how they were trained.
"""
from __future__ import annotations

import importlib.util
import json
import math
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vs_common import LANG_NAMES, Job, log, need_disk, resolved_revision, sample_plan  # noqa: E402

SRC = Path(os.environ.get("VS_SRC", "/workspace/vs/src/qwen3"))
BASE = "Qwen/Qwen3-TTS-12Hz-1.7B-Base"
TOKENIZER = "Qwen/Qwen3-TTS-Tokenizer-12Hz"
SPEAKER = "vs_speaker"
SEED = 1234


def flash_attention_works() -> bool:
    """find_spec() is not enough: the CUDA extension must actually load."""
    if importlib.util.find_spec("flash_attn") is None:
        return False
    try:
        import flash_attn  # noqa: F401
        import flash_attn_2_cuda  # noqa: F401
        return True
    except Exception as e:  # ImportError, OSError (missing .so symbols), RuntimeError
        log(f"FlashAttention present but unusable ({e}); using SDPA")
        return False


def main() -> None:
    job = Job()
    p = job.params
    from huggingface_hub import snapshot_download

    job.progress(phase="download")
    base_path = snapshot_download(BASE, revision=p.get("base_revision") or None)
    tok_path = snapshot_download(TOKENIZER, revision=p.get("tokenizer_revision") or None)
    attn = "flash_attention_2" if flash_attention_works() else "sdpa"
    log(f"base {BASE}@{resolved_revision(base_path)} tokenizer @{resolved_revision(tok_path)} attention {attn}")
    keep_n = int(p.get("keep", 2))
    need_disk(20 + 5 * (int(p.get("epochs", 3)) + keep_n))

    plan = sample_plan(job)
    ref = plan.get("reference") or {}
    if not ref.get("audio"):
        raise RuntimeError("dataset has no reference clip")
    import librosa
    import soundfile as sf
    y, _ = librosa.load(str(job.data / ref["audio"]), sr=24000, mono=True)
    if len(y) < 24000:
        raise RuntimeError("reference clip is shorter than one second")
    ref24 = job.work / "reference_24k.wav"
    sf.write(str(ref24), y, 24000, subtype="PCM_16")

    raw = job.work / "train_raw.jsonl"
    items = job.read_jsonl("train.jsonl")
    with raw.open("w", encoding="utf-8") as f:
        for it in items:  # the recipe recommends one fixed ref_audio for every line
            f.write(json.dumps({"audio": str(job.data / it["audio"]), "text": it["text"], "ref_audio": str(ref24),
                                "language": LANG_NAMES.get(it.get("lang") or "", "Auto")}, ensure_ascii=False) + "\n")

    job.progress(phase="prepare")
    codes = job.work / "train_with_codes.jsonl"
    ft = SRC / "finetuning"
    job.run([sys.executable, ft / "prepare_data.py", "--device", "cuda:0", "--tokenizer_model_path", tok_path,
             "--input_jsonl", raw, "--output_jsonl", codes], cwd=ft)

    # the official trainer hard-codes FlashAttention 2; fall back to PyTorch SDPA when it does not load
    script = (ft / "sft_12hz.py").read_text(encoding="utf-8")
    if attn != "flash_attention_2":
        script = script.replace('"flash_attention_2"', '"sdpa"')
    (ft / "sft_vs.py").write_text(script, encoding="utf-8")

    bs, epochs = int(p.get("batch_size", 2)), int(p.get("epochs", 3))
    per_epoch = math.ceil(len(items) / bs)
    total = per_epoch * epochs
    out = job.work / "out"
    job.progress(phase="train", step=0, total=total, per_epoch=per_epoch, mode="sft")
    pat = re.compile(r"Epoch (\d+) \| Step (\d+) \| Loss: ([\d.]+)")
    metrics_f = (job.out / "train_metrics.jsonl").open("w", encoding="utf-8")

    def on_line(line: str) -> None:
        m = pat.search(line)
        if m:
            e, s, loss = int(m.group(1)), int(m.group(2)), float(m.group(3))
            step = e * per_epoch + s + 1
            metrics_f.write(json.dumps({"split": "train", "step": step, "loss": loss, "epoch": e}) + "\n")
            metrics_f.flush()
            job.progress(phase="train", step=step, total=total, loss=round(loss, 4),
                         epoch=round(step / per_epoch, 2))

    job.run([sys.executable, "sft_vs.py", "--init_model_path", base_path, "--output_model_path", out,
             "--train_jsonl", codes, "--batch_size", bs, "--lr", float(p.get("lr", 2e-5)),
             "--num_epochs", epochs, "--speaker_name", SPEAKER], cwd=ft, on_line=on_line)
    metrics_f.close()

    ckpts = sorted((d for d in out.iterdir() if d.name.startswith("checkpoint-epoch-")),
                   key=lambda d: int(d.name.rsplit("-", 1)[1]))
    if not ckpts:
        raise RuntimeError("trainer produced no checkpoints")
    keep = ckpts[-keep_n:]
    ck_meta = [{"name": d.name, "step": (int(d.name.rsplit("-", 1)[1]) + 1) * per_epoch,
                "epoch": int(d.name.rsplit("-", 1)[1]) + 1, "weights": d in keep} for d in ckpts]
    meta = {"engine": "qwen3", "mode": "sft", "base": BASE, "base_revision": resolved_revision(base_path),
            "tokenizer_revision": resolved_revision(tok_path), "speaker": SPEAKER, "checkpoints": ck_meta,
            "samples": plan, "total_steps": total, "per_epoch": per_epoch, "attn": attn, "seed": SEED,
            "sft_language": "Auto", "sampling": "pending"}
    job.package(meta, "model.tar", [(job.out / "train_metrics.jsonl", "model/train_metrics.jsonl")]
                + [(d, f"model/checkpoints/{d.name}") for d in keep])

    try:
        sample_all(job, base_path, ckpts, plan, ref24, ref.get("text") or "", attn)
        meta.update(sampling="complete", sample_conditions={
            "plain": {"mode": "plain", "language": "Auto", "seed": SEED},
            "ref": {"mode": "hifi" if ref.get("text") else "ref", "reference": ref.get("id"), "seed": SEED,
                    "note": "base model only (zero-shot clone)"}})
    except Exception as e:
        log(f"sampling incomplete: {e}")
        meta.update(sampling="incomplete", sampling_error=str(e)[:300])
    if (job.out / "samples").exists():
        job.package(meta, "samples.tar", [(job.out / "samples", "model/samples")])


def sample_all(job: Job, base_path: str, ckpts: list[Path], plan: dict, ref24: Path, ref_text: str,
               attn: str) -> None:
    import soundfile as sf
    import torch
    from qwen_tts import Qwen3TTSModel

    job.progress(phase="samples", step=0, total=len(ckpts) + 1)
    lines = plan.get("lines", [])

    def write(name: str, fname: str, wavs, sr) -> None:
        d = job.out / "samples" / name
        d.mkdir(parents=True, exist_ok=True)
        sf.write(str(d / fname), wavs[0], sr)

    # the untrained base can only clone from a reference, so its clips are filed as "ref", not "plain"
    base = Qwen3TTSModel.from_pretrained(base_path, device_map="cuda:0", dtype=torch.bfloat16,
                                         attn_implementation=attn)
    prompt = base.create_voice_clone_prompt(ref_audio=str(ref24), ref_text=ref_text or None,
                                            x_vector_only_mode=not ref_text)
    for i, line in enumerate(lines):
        try:
            torch.manual_seed(SEED)
            wavs, sr = base.generate_voice_clone(text=line["text"], language=LANG_NAMES.get(line.get("lang"), "Auto"),
                                                 voice_clone_prompt=prompt)
            write("base", f"{i}_ref.wav", wavs, sr)
        except Exception as e:
            log(f"base sample {i} failed: {e}")
    del base
    torch.cuda.empty_cache()
    for k, d in enumerate(ckpts):
        m = Qwen3TTSModel.from_pretrained(str(d), device_map="cuda:0", dtype=torch.bfloat16, attn_implementation=attn)
        for i, line in enumerate(lines):
            try:
                torch.manual_seed(SEED)
                wavs, sr = m.generate_custom_voice(text=line["text"], speaker=SPEAKER, language="Auto")
                write(d.name, f"{i}_plain.wav", wavs, sr)
            except Exception as e:
                log(f"sample {d.name}/{i} failed: {e}")
        del m
        torch.cuda.empty_cache()
        job.progress(phase="samples", step=k + 2, total=len(ckpts) + 1)


if __name__ == "__main__":
    main()

```

### `vstudio/engines/base.py`

```python
"""The engine interface: one adapter per TTS model family.

An engine knows how to
- turn a studio dataset into its own training format (export_dataset);
- describe the cloud job that fine-tunes it (setup script, training entry point, container image, GPU sizes);
- load a fine-tuned model and synthesize speech locally (load / synthesize);
- translate the project's bracket performance tags ([deadpan], [laughs]) into its own control format.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import numpy as np


@dataclass
class TrainPreset:
    id: str
    label: str           # shown in the UI (zh-TW)
    description: str
    params: dict
    gpu: list[str]       # RunPod gpuTypeIds, in order of preference
    hours_per_data_hour: float  # rough wall-clock estimate per hour of training audio (before calibration)
    s_per_step: float = 0.0     # first guess of seconds per training step, replaced by measured speed after a run
    disk_gb: int = 80           # pod container disk
    ram_gb: int = 32            # minimum host RAM (RunPod minRAMPerGPU; its default of 8 GB is too small)
    vcpu: int = 8               # minimum vCPUs (data loading and audio preprocessing workers)
    min_hours: float = 0.0      # recommended minimum amount of approved audio
    recommended: bool = False


MODES = {"plain": "只用模型", "ref": "參考音色", "hifi": "完整複製"}

# ElevenLabs v3/v4 sound tags → delivery descriptions ("" drops a tag that has no spoken equivalent)
TAG_STYLE = {
    "laughs": "with light laughter", "laughing": "with light laughter", "chuckles": "with a soft chuckle",
    "giggles": "giggling", "sighs": "with a sigh", "exhales": "with a slow exhale", "whispers": "whispering",
    "whispering": "whispering", "shouts": "shouting", "shouting": "shouting", "yelling": "shouting",
    "crying": "tearful", "sobbing": "tearful", "sniffles": "tearful", "gasps": "with a gasp",
    "clears throat": "", "pause": "", "short pause": "", "long pause": "",
}


@dataclass
class Synthesis:
    audio: np.ndarray
    sr: int
    info: dict = field(default_factory=dict)


class Engine:
    id = "base"
    name = "Base"
    summary = ""
    license = ""
    license_note = ""
    languages: tuple[str, ...] = ()
    supports_tags = False       # inline bracket tags understood natively
    supports_instruct = False   # free-text style instruction
    needs_reference = False     # synthesis needs a reference clip
    infer_vram_gb = 0.0
    image = ""                  # container image for cloud training
    presets: list[TrainPreset] = []

    # --- dataset & training ---------------------------------------------------------------------------------
    def export_dataset(self, ds: dict, out_dir: Path, params: dict | None = None) -> dict:
        """Write the engine's training files for dataset `ds` into out_dir; return info for config.json."""
        raise NotImplementedError

    def cloud_files(self) -> dict[str, str]:
        """Remote file name → contents (setup_env.sh, train_entry.py …) placed next to bootstrap.sh."""
        raise NotImplementedError

    def schedule(self, n_train: int, params: dict) -> dict:
        """Engine-specific derived values (e.g. total_steps) stored with the run's parameters."""
        return {}

    def effective_params(self, preset_id: str, overrides: dict | None, n_train: int) -> dict:
        """Preset + user overrides + derived schedule: exactly what is quoted, stored and sent to the pod."""
        params = {**self.preset(preset_id).params, **(overrides or {})}
        return {**params, **self.schedule(n_train, params)}

    def steps(self, n_train: int, preset_id: str, params: dict | None = None) -> int:
        """Training steps the cloud script will run for n_train clips (0 = unknown)."""
        return 0

    def estimate(self, data_hours: float, preset_id: str, usd_h: float, n_train: int = 0,
                 s_per_step: float | None = None, params: dict | None = None) -> dict:
        """Wall-clock and cost estimate. Uses the measured speed of an earlier run when there is one."""
        p = self.preset(preset_id)
        steps = self.steps(n_train, preset_id, params) if n_train else 0
        sps = s_per_step or p.s_per_step
        if steps and sps:
            train_h = steps * sps / 3600
            basis = "measured" if s_per_step else "guess"
        else:
            train_h = data_hours * p.hours_per_data_hour
            basis = "guess"
        hours = max(0.2, train_h) + 0.45  # + environment check, model download, samples, packaging
        return {"hours": round(hours, 2), "usd": round(hours * usd_h, 2), "steps": steps, "basis": basis}

    def preset(self, preset_id: str) -> TrainPreset:
        for p in self.presets:
            if p.id == preset_id:
                return p
        return self.presets[0]

    # --- inference ------------------------------------------------------------------------------------------
    def available(self) -> tuple[bool, str]:
        """Whether this machine can run the engine locally (packages installed, GPU memory)."""
        return False, "未安裝"

    def install_spec(self) -> dict:
        """pip requirements (and environment) to install the engine locally for inference."""
        return {}

    def modes(self, meta: dict) -> list[str]:
        """Synthesis modes a model supports: plain (model only), ref (reference timbre), hifi (reference + transcript)."""
        return ["plain"]

    def load(self, model_dir: Path, checkpoint: str | None = None):
        raise NotImplementedError

    def synthesize(self, handle, text: str, language: str | None = None, style: str = "", mode: str = "plain",
                   reference: dict | None = None, seed: int | None = None, **kw) -> Synthesis:
        """reference: {"path": wav, "text": transcript or ""}"""
        raise NotImplementedError

    def unload(self, handle) -> None:
        """Drop the model the handle owns, then collect, so the VRAM is actually released."""
        try:
            if isinstance(handle, dict):
                handle.clear()
            import gc
            gc.collect()
            import torch
            torch.cuda.empty_cache()
        except Exception:
            pass

    # --- helpers for model folders -------------------------------------------------------------------------
    @staticmethod
    def model_meta(model_dir: Path) -> dict:
        """engine.json written by the cloud script; zero-shot models have none (or mode=zeroshot)."""
        import json
        f = Path(model_dir) / "engine.json"
        return json.loads(f.read_text(encoding="utf-8")) if f.exists() else {"mode": "zeroshot", "checkpoints": []}

    @staticmethod
    def checkpoint_dir(model_dir: Path, meta: dict, checkpoint: str | None) -> Path | None:
        cks = [c for c in meta.get("checkpoints", []) if c.get("weights")]
        if not cks:
            return None
        names = [c["name"] for c in cks]
        name = checkpoint if checkpoint in names else names[-1]
        return Path(model_dir) / "checkpoints" / name

    # --- tags -----------------------------------------------------------------------------------------------
    def render_tags(self, text_with_tags: str) -> tuple[str, str]:
        """Return (text for the engine, style instruction). Default: strip tags into a style instruction.
        ElevenLabs-style sound tags from the novel-lab sheets ([laughs], [sighs]…) become delivery descriptions,
        because instruction-following engines describe manner rather than insert sound effects."""
        import re
        tags = [t.strip() for group in re.findall(r"\[([^\[\]]+)\]", text_with_tags) for t in group.split(",")]
        text = re.sub(r"\s*\[[^\[\]]+\]\s*", " ", text_with_tags).strip()
        style = ", ".join(dict.fromkeys(TAG_STYLE.get(t.lower(), t) for t in tags if t and TAG_STYLE.get(t.lower(), t)))
        return text, style

    def info(self) -> dict:
        ok, why = self.available()
        return {"id": self.id, "name": self.name, "summary": self.summary, "license": self.license,
                "license_note": self.license_note, "languages": list(self.languages),
                "supports_tags": self.supports_tags, "supports_instruct": self.supports_instruct,
                "needs_reference": self.needs_reference, "infer_vram_gb": self.infer_vram_gb,
                "available": ok, "available_note": why,
                "install": bool(self.install_spec()),
                "presets": [{"id": p.id, "label": p.label, "description": p.description, "gpu": p.gpu,
                             "params": p.params, "min_hours": p.min_hours, "recommended": p.recommended}
                            for p in self.presets]}

```

### `vstudio/engines/voxcpm2.py`

```python
"""VoxCPM2 (OpenBMB, 2026-04): the studio's primary engine.

Why it is the default (research of 2026-10, with GPT): Apache-2.0 code and weights; official LoRA and full
fine-tuning; Japanese and English among 30 languages; the highest speaker similarity of the open models in the
shared MiniMax multilingual comparison (ja SIM 82.8, en 85.4); 48 kHz output; about 8 GB of VRAM for inference.
Its weak spot is a somewhat higher word error rate than Qwen3-TTS, which the studio's best-of-N screening and
checkpoint scoring are there to catch.

Synthesis modes
- plain: the fine-tuned model alone; a parenthesised style note may lead the text, e.g. "(quiet, unhurried)…".
- ref:   adds a reference clip for timbre; style notes still work.
- hifi:  "ultimate cloning": reference clip + its exact transcript, the model continues from it, keeping rhythm,
         accent and habits closest to the recording. Style notes are ignored in this mode.
"""
from __future__ import annotations

import importlib.util
import math
from pathlib import Path

from . import export, remote
from .base import Engine, Synthesis, TrainPreset

REPO = "https://github.com/OpenBMB/VoxCPM.git"
COMMIT = "f0c787f0937dc1c9a8f4f64d9a332d9c5da2e629"  # main on 2026-09-30, after release 2.0.3
VERSION = "2.0.3.post1"
BASE = "openbmb/VoxCPM2"
IMAGE = "runpod/pytorch:2.8.0-py3.11-cuda12.8.1-cudnn-devel-ubuntu22.04"
GPU_48 = ["NVIDIA L40S", "NVIDIA RTX 6000 Ada Generation", "NVIDIA A100 80GB PCIe", "NVIDIA A100-SXM4-80GB"]
GPU_80 = ["NVIDIA A100 80GB PCIe", "NVIDIA A100-SXM4-80GB", "NVIDIA H100 PCIe", "NVIDIA H100 80GB HBM3"]


class VoxCPM2Engine(Engine):
    id = "voxcpm2"
    name = "VoxCPM2"
    summary = ("OpenBMB 2026 年 4 月發表，20 億參數、48 kHz、支援日文與英文等 30 種語言。公開評測中音色相似度最高，"
               "有官方 LoRA 與完整微調。「完整複製」模式會接著參考錄音說下去，最能保留口音、節奏和說話習慣。")
    license = "Apache-2.0"
    license_note = "程式與權重皆為 Apache-2.0，個人與商業使用都可以；聲音本人的同意另外記錄在平台裡。"
    languages = ("ja", "en", "zh", "ko", "fr", "de", "es", "it", "pt", "ru")
    supports_instruct = True
    infer_vram_gb = 8
    image = IMAGE
    presets = [
        TrainPreset("lora", "LoRA 微調（建議先跑這個）",
                    "官方 LoRA 設定（rank 32、學習率 1e-4、有效批次 16），跑 2 個 epoch，途中存 6 個檢查點，"
                    "每個檢查點都會念同一批沒看過的句子讓你比較。適合 30 分鐘到 20 小時的資料。",
                    {"mode": "lora", "epochs": 2, "lr": 1e-4, "batch_size": 2, "grad_accum": 8, "rank": 32,
                     "alpha": 32, "saves": 6, "max_batch_tokens": 8192, "ref_fraction": 0.4},
                    GPU_48, hours_per_data_hour=0.12, s_per_step=7.0, disk_gb=80, min_hours=0.3, recommended=True),
        TrainPreset("full", "完整微調（資料 5 小時以上）",
                    "官方完整微調設定（學習率 1e-5、有效批次 16），跑 1.5 個 epoch，保留最後 3 個檢查點的權重。"
                    "資料多時可能比 LoRA 更像，但模型檔約 8 GB、需要 80 GB 顯示卡。建議先跑 LoRA 當對照。",
                    {"mode": "full", "epochs": 1.5, "lr": 1e-5, "batch_size": 2, "grad_accum": 8, "saves": 6,
                     "keep_full": 3, "max_batch_tokens": 8192, "ref_fraction": 0.4},
                    GPU_80, hours_per_data_hour=0.15, s_per_step=9.0, disk_gb=250, ram_gb=64, min_hours=5.0),
    ]

    # --- dataset & training ---------------------------------------------------------------------------------
    def export_dataset(self, ds: dict, out_dir: Path, params: dict | None = None) -> dict:
        frac = float((params or {}).get("ref_fraction", 0.4))
        return export.write(ds, out_dir, ref_fraction=frac)

    def cloud_files(self) -> dict[str, str]:
        return {"setup_env.sh": remote.setup_script(self.id, "VoxCPM2", REPO, COMMIT, VERSION, "voxcpm", "VoxCPM"),
                "train_entry.py": remote.read("voxcpm2_train.py"), "vs_common.py": remote.read("vs_common.py")}

    def schedule(self, n_train: int, params: dict) -> dict:
        """The one place the update count is decided: the quote, the stored run parameters and the cloud script
        all use it. The trainer drops the last incomplete batch and counts optimizer updates."""
        bs, accum = int(params["batch_size"]), int(params["grad_accum"])
        batches = n_train // bs
        if batches < accum:
            raise ValueError(f"資料太少：這個設定至少需要 {bs * accum} 段訓練片段（目前 {n_train} 段）")
        total = min(int(params.get("max_steps_cap", 30000)),
                    max(1, math.ceil(batches * float(params["epochs"]) / accum)))
        return {"per_epoch": batches // accum, "total_steps": total, "epochs_effective": round(total * accum / batches, 2)}

    def steps(self, n_train: int, preset_id: str, params: dict | None = None) -> int:
        try:
            return self.schedule(n_train, params or self.preset(preset_id).params)["total_steps"]
        except ValueError:
            return 0

    # --- inference ------------------------------------------------------------------------------------------
    def install_spec(self) -> dict:
        return {"pip": [f"voxcpm @ https://github.com/OpenBMB/VoxCPM/archive/{COMMIT}.zip"],
                "env": {"SETUPTOOLS_SCM_PRETEND_VERSION": VERSION}, "module": "voxcpm", "cls": "VoxCPM",
                "download": [BASE]}

    def available(self):
        if importlib.util.find_spec("voxcpm") is None:
            return False, "尚未安裝（設定 → 引擎 → 安裝）"
        try:
            import torch
            if not torch.cuda.is_available():
                return True, "已安裝，但沒有偵測到 NVIDIA GPU（可以用，但很慢）"
            total = torch.cuda.mem_get_info()[1] / 1e9
            if total < self.infer_vram_gb:
                return True, f"已安裝；顯示卡記憶體 {total:.0f} GB，低於建議的 {self.infer_vram_gb} GB"
        except Exception:
            pass
        return True, "已安裝"

    def modes(self, meta: dict) -> list[str]:
        return ["plain", "ref", "hifi"] if meta.get("mode") != "zeroshot" else ["ref", "hifi"]

    def load(self, model_dir: Path, checkpoint: str | None = None):
        from voxcpm import VoxCPM
        meta = self.model_meta(model_dir)
        kw = {"load_denoiser": False, "optimize": False}
        ck = self.checkpoint_dir(model_dir, meta, checkpoint)
        if meta.get("mode") == "lora" and ck:
            # the adapter must sit on exactly the base weights it was trained on (recorded snapshot commit)
            from huggingface_hub import snapshot_download
            base = snapshot_download(meta.get("base") or BASE, revision=meta.get("base_revision") or None)
            m = VoxCPM.from_pretrained(base, lora_weights_path=str(ck), **kw)
        elif meta.get("mode") == "full" and ck:
            m = VoxCPM.from_pretrained(str(ck), **kw)
        else:
            m = VoxCPM.from_pretrained(BASE, **kw)
        return {"model": m, "meta": meta, "checkpoint": ck.name if ck else None}

    def synthesize(self, handle, text, language=None, style="", mode="plain", reference=None, seed=None, **kw):
        m = handle["model"]
        args = {"cfg_value": float(kw.get("cfg", 2.0)), "inference_timesteps": int(kw.get("timesteps", 10)),
                "seed": seed}
        ref_path = str(reference["path"]) if reference and reference.get("path") else None
        if mode == "hifi" and ref_path and reference.get("text"):
            args.update(text=text, prompt_wav_path=ref_path, prompt_text=reference["text"],
                        reference_wav_path=ref_path)
        else:
            args["text"] = f"({style}){text}" if style else text
            if mode in ("ref", "hifi") and ref_path:
                args["reference_wav_path"] = ref_path
        wav = m.generate(**args)
        return Synthesis(wav, m.tts_model.sample_rate, {"mode": mode, "checkpoint": handle.get("checkpoint")})

```

### `vstudio/engines/qwen3.py`

```python
"""Qwen3-TTS-12Hz-1.7B-Base (Alibaba Qwen, 2026-01): the studio's second engine.

Why it is here: Apache-2.0; official single-speaker fine-tuning; the lowest word error rate of the open models in
the shared comparison (en WER 0.93 %, ja 3.82 %), so it is the one to try when VoxCPM2 mispronounces or skips words.
Its speaker similarity trails VoxCPM2 in the same comparison. The fine-tuned model is a full copy (~4 GB).

Modes: a fine-tuned model speaks on its own (plain), optionally with a style instruction (not guaranteed to work after
fine-tuning the Base model). A zero-shot model clones from a reference clip (ref) or clip + transcript (hifi).
"""
from __future__ import annotations

import importlib.util
from pathlib import Path

from . import export, remote
from .base import Engine, Synthesis, TrainPreset

REPO = "https://github.com/QwenLM/Qwen3-TTS.git"
COMMIT = "022e286b98fbec7e1e916cb940cdf532cd9f488e"  # main on 2026-03-17 (package 0.1.1)
VERSION = "0.1.1"
BASE = "Qwen/Qwen3-TTS-12Hz-1.7B-Base"
IMAGE = "runpod/pytorch:2.8.0-py3.11-cuda12.8.1-cudnn-devel-ubuntu22.04"
FLASH_WHEEL = ("https://github.com/Dao-AILab/flash-attention/releases/download/v2.8.3/"
               "flash_attn-2.8.3+cu12torch2.8cxx11abiTRUE-cp311-cp311-linux_x86_64.whl")
LANG = {"ja": "Japanese", "en": "English", "zh": "Chinese", "ko": "Korean", "de": "German", "fr": "French",
        "ru": "Russian", "pt": "Portuguese", "es": "Spanish", "it": "Italian"}


def _flash_ok() -> bool:
    """The CUDA extension has to load, not just be installed (a mismatched build fails at import)."""
    if importlib.util.find_spec("flash_attn") is None:
        return False
    try:
        import flash_attn  # noqa: F401
        import flash_attn_2_cuda  # noqa: F401
        return True
    except Exception:
        return False


class Qwen3Engine(Engine):
    id = "qwen3"
    name = "Qwen3-TTS 1.7B"
    summary = ("阿里巴巴 Qwen 2026 年 1 月發表，17 億參數、10 種語言（含日文、英文）。公開評測中念錯字最少，"
               "有官方單一說話者微調。音色相似度略低於 VoxCPM2；當 VoxCPM2 念錯或漏字時拿來對照。")
    license = "Apache-2.0"
    license_note = "程式與權重皆為 Apache-2.0，個人與商業使用都可以。"
    languages = tuple(LANG)
    supports_instruct = True
    infer_vram_gb = 8
    image = IMAGE
    presets = [
        TrainPreset("sft", "官方微調（完整）",
                    "官方 finetuning 流程：先抽出 12 Hz 音訊碼，再做完整微調 3 個 epoch（學習率 2e-5、批次 2、"
                    "梯度累積 4），每個 epoch 一個檢查點，保留最後 2 個。",
                    {"epochs": 3, "lr": 2e-5, "batch_size": 2, "keep": 2},
                    ["NVIDIA A100 80GB PCIe", "NVIDIA A100-SXM4-80GB", "NVIDIA L40S", "NVIDIA H100 PCIe"],
                    hours_per_data_hour=0.12, s_per_step=0.5, disk_gb=120, ram_gb=64, min_hours=0.5,
                    recommended=True),
    ]

    def export_dataset(self, ds: dict, out_dir: Path, params: dict | None = None) -> dict:
        return export.write(ds, out_dir, ref_fraction=0.0)

    def cloud_files(self) -> dict[str, str]:
        post = (f'pip install -q --no-deps "{FLASH_WHEEL}" '
                '|| echo "[vs] FlashAttention wheel not available; training will use PyTorch SDPA"\n'
                'python -c "import flash_attn, flash_attn_2_cuda" 2>/dev/null || '
                '{ echo "[vs] FlashAttention unusable on this image; removing it (SDPA will be used)"; '
                'pip uninstall -q -y flash-attn || true; }')
        setup = remote.setup_script(self.id, "Qwen3-TTS", REPO, COMMIT, VERSION, "qwen_tts", "Qwen3TTSModel", post=post)
        return {"setup_env.sh": setup,
                "train_entry.py": remote.read("qwen3_train.py"), "vs_common.py": remote.read("vs_common.py")}

    def steps(self, n_train: int, preset_id: str, params: dict | None = None) -> int:
        p = params or self.preset(preset_id).params
        return -(-n_train // int(p["batch_size"])) * int(p["epochs"])

    # --- inference ------------------------------------------------------------------------------------------
    def install_spec(self) -> dict:
        return {"pip": [f"qwen-tts @ https://github.com/QwenLM/Qwen3-TTS/archive/{COMMIT}.zip"], "env": {},
                "module": "qwen_tts", "cls": "Qwen3TTSModel", "download": [BASE, "Qwen/Qwen3-TTS-Tokenizer-12Hz"]}

    def available(self):
        if importlib.util.find_spec("qwen_tts") is None:
            return False, "尚未安裝（設定 → 引擎 → 安裝）"
        try:
            import torch
            if not torch.cuda.is_available():
                return True, "已安裝，但沒有偵測到 NVIDIA GPU（可以用，但很慢）"
        except Exception:
            pass
        return True, "已安裝"

    def modes(self, meta: dict) -> list[str]:
        return ["plain"] if meta.get("mode") == "sft" else ["ref", "hifi"]

    def load(self, model_dir: Path, checkpoint: str | None = None):
        import torch
        from qwen_tts import Qwen3TTSModel
        meta = self.model_meta(model_dir)
        ck = self.checkpoint_dir(model_dir, meta, checkpoint)
        cuda = torch.cuda.is_available()
        attn = "flash_attention_2" if cuda and _flash_ok() else "sdpa"
        src = str(ck) if (meta.get("mode") == "sft" and ck) else BASE
        m = Qwen3TTSModel.from_pretrained(src, device_map="cuda:0" if cuda else "cpu",
                                          dtype=torch.bfloat16 if cuda else torch.float32, attn_implementation=attn)
        return {"model": m, "meta": meta, "checkpoint": ck.name if ck and src != BASE else None, "prompts": {}}

    def synthesize(self, handle, text, language=None, style="", mode="plain", reference=None, seed=None, **kw):
        import torch
        m, meta = handle["model"], handle["meta"]
        lang = LANG.get(language or "", "Auto")
        if seed is not None:
            torch.manual_seed(seed)
        if meta.get("mode") == "sft":
            # the official SFT recipe trains with the auto-language prompt, so inference uses it too
            spk = meta.get("speaker", "vs_speaker")
            sft_lang = meta.get("sft_language", "Auto")
            try:
                wavs, sr = m.generate_custom_voice(text=text, language=sft_lang, speaker=spk, instruct=style or None)
            except TypeError:
                wavs, sr = m.generate_custom_voice(text=text, language=sft_lang, speaker=spk)
        else:
            if not reference or not reference.get("path"):
                raise ValueError("零樣本模型需要參考片段")
            hifi = mode == "hifi" and bool(reference.get("text"))
            key = (str(reference["path"]), hifi)
            if key not in handle["prompts"]:
                handle["prompts"][key] = m.create_voice_clone_prompt(
                    ref_audio=str(reference["path"]), ref_text=reference.get("text") if hifi else None,
                    x_vector_only_mode=not hifi)
            wavs, sr = m.generate_voice_clone(text=text, language=lang, voice_clone_prompt=handle["prompts"][key])
        return Synthesis(wavs[0], sr, {"mode": mode, "checkpoint": handle.get("checkpoint")})

```

### `vstudio/engines/export.py`

```python
"""Dataset export shared by the real engines: training manifests plus the held-out lines every checkpoint reads."""
from __future__ import annotations

import json
import random
from pathlib import Path

from .. import datasets

MANIFEST_KEYS = ("audio", "text", "duration", "lang")


def _row(it: dict) -> dict:
    return {k: it[k] for k in MANIFEST_KEYS}


def pick_samples(val: list[dict], n: int = 12) -> list[dict]:
    """Up to n held-out lines, balanced across languages, preferring 3–12 s clips with good scores."""
    by_lang: dict[str, list[dict]] = {}
    for it in sorted(val, key=lambda i: (not 3 <= i["duration"] <= 12, -(i.get("score") or 0))):
        by_lang.setdefault(it.get("lang") or "", []).append(it)
    out: list[dict] = []
    while len(out) < n and any(by_lang.values()):
        for lang in list(by_lang):
            if by_lang[lang] and len(out) < n:
                out.append(by_lang[lang].pop(0))
    return [{"id": i["id"], "text": i["text"], "lang": i.get("lang") or "", "audio": i["audio"]} for i in out]


def write(ds: dict, out_dir: Path, ref_fraction: float = 0.0, seed: int = 11) -> dict:
    """train.jsonl / val.jsonl / samples.json in out_dir (paths relative to it; the wavs travel as wavs/).

    ref_fraction > 0 adds a reference clip of the same voice to that share of training lines (VoxCPM recommends
    30–50 % so the model keeps reference-based cloning), taken from a different recording where possible."""
    out_dir.mkdir(parents=True, exist_ok=True)
    train, val = datasets.load_items(ds, "train"), datasets.load_items(ds, "val")
    rnd = random.Random(seed)
    pool = [i for i in train if 3.0 <= i["duration"] <= 15.0]
    if len(pool) < 2:
        pool = train
    n_ref = 0
    with open(out_dir / "train.jsonl", "w", encoding="utf-8") as f:
        for it in train:
            row = _row(it)
            if ref_fraction and rnd.random() < ref_fraction and len(pool) > 1:
                others = [p for p in pool if p["id"] != it["id"] and p.get("source") != it.get("source")]
                ref = rnd.choice(others or [p for p in pool if p["id"] != it["id"]])
                row.update(ref_audio=ref["audio"], ref_duration=ref["duration"])
                n_ref += 1
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    with open(out_dir / "val.jsonl", "w", encoding="utf-8") as f:
        for it in val:
            f.write(json.dumps(_row(it), ensure_ascii=False) + "\n")
    refs = ds["meta"].get("reference_items") or [{"audio": a, "text": ""} for a in ds["meta"].get("reference", [])]
    lines = pick_samples(val)
    if not lines:  # tiny datasets have no held-out lines; fall back to training lines (marked as seen)
        lines = [{**x, "seen": True} for x in pick_samples(train, 3)]
    samples = {"lines": lines, "reference": refs[0] if refs else None}
    (out_dir / "samples.json").write_text(json.dumps(samples, ensure_ascii=False, indent=2), encoding="utf-8")
    return {"n_train": len(train), "n_val": len(val), "n_ref": n_ref, "files": ["train.jsonl", "val.jsonl",
                                                                               "samples.json"]}

```

### `vstudio/engines/install.py`

```python
"""Install a real engine into the studio's own Python environment (for local text to speech), then download its
base weights. Runs as a background job so the page stays usable; the full pip output goes to the job log."""
from __future__ import annotations

import importlib
import importlib.util
import os
import shutil
import subprocess
import sys

from .. import config, jobs
from . import get

TORCHCODEC = {"2.6": "0.2.*", "2.7": "0.5.*", "2.8": "0.7.*", "2.9": "0.8.*"}


def _constraints() -> str:
    """Pin the installed CUDA build of torch so no engine dependency can swap it for a CPU build."""
    import torch
    lines = [f"torch=={torch.__version__.split('+')[0]}"]
    try:
        import torchaudio
        lines.append(f"torchaudio=={torchaudio.__version__.split('+')[0]}")
    except ImportError:
        pass
    codec = TORCHCODEC.get(".".join(torch.__version__.split(".")[:2]))
    if codec:
        lines.append(f"torchcodec=={codec}")
    f = config.path("tmp", "constraints.txt")
    f.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return str(f)


@jobs.handler("install_engine", queue="io")
def install_engine(ctx: jobs.JobContext) -> dict:
    eng = get(ctx.params["engine"])
    spec = eng.install_spec()
    if not spec:
        return {"message": "這個引擎不需要安裝"}
    if importlib.util.find_spec("torch") is None:
        raise RuntimeError("還沒有安裝 PyTorch。請關掉 Voice Studio，重新執行 install.bat（會安裝 GPU 版 PyTorch）。")
    ctx.progress(0.05, "準備安裝", force=True)
    cons = _constraints()
    uv = shutil.which("uv")
    base = [uv, "pip", "install", "--python", sys.executable] if uv else [sys.executable, "-m", "pip", "install",
                                                                         "--progress-bar", "off"]
    cmd = [*base, "-c", cons, *spec["pip"]]
    ctx.log("$ " + " ".join(cmd))
    env = {**os.environ, **spec.get("env", {})}
    flags = getattr(subprocess, "CREATE_NO_WINDOW", 0)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, env=env, errors="replace",
                         creationflags=flags)
    assert p.stdout is not None
    n = 0
    for line in p.stdout:
        ctx.log(line)
        n += 1
        ctx.progress(min(0.6, 0.05 + n * 0.004), "安裝套件：" + line.strip()[:60])
    if p.wait() != 0:
        raise RuntimeError("安裝失敗，詳細訊息在工作紀錄。常見原因：網路中斷、磁碟空間不足。")
    # a fresh interpreter proves the native parts load (find_spec alone succeeds for broken DLLs)
    probe = subprocess.run([sys.executable, "-c", f"import torch; from {spec['module']} import {spec['cls']}; print('ok')"],
                           capture_output=True, text=True, creationflags=flags)
    ctx.log(probe.stdout + probe.stderr[-3000:])
    if probe.returncode != 0:
        raise RuntimeError("套件裝好了但載入失敗（詳見工作紀錄）。常見原因：PyTorch 不是 GPU 版，或缺少 Visual C++ 執行階段。")
    importlib.invalidate_caches()
    from huggingface_hub import snapshot_download
    repos = spec.get("download", [])
    for k, repo in enumerate(repos):
        ctx.progress(0.6 + 0.4 * k / max(1, len(repos)), f"下載模型權重 {repo}（數 GB，請稍候）", force=True)
        ctx.log(f"download {repo}")
        snapshot_download(repo, token=config.get_secret("hf_token") or None)
    return {"message": f"{eng.name} 已安裝。請關掉並重新開啟 Voice Studio，再開始合成。", "restart": True}

```

### `vstudio/training.py`

```python
"""Training runs: cloud (RunPod) fine-tuning, the model registry and zero-shot (no training) models."""
from __future__ import annotations

import json
import shutil
import tarfile
import time
from pathlib import Path

from . import config, datasets, db, engines, evaluate, jobs  # noqa: F401  (evaluate registers evaluate_model)
from .cloud import runpod

BOOTSTRAP = (Path(__file__).parent / "cloud" / "bootstrap" / "bootstrap.sh").read_text(encoding="utf-8")


def _speed_key(engine_id: str, preset_id: str, gpu: str) -> str:
    return f"{engine_id}:{preset_id}:{gpu}"


def _require_consent(voice_id: str) -> None:
    """Consent is re-checked at every step that uses the voice: building, uploading, renting, synthesizing."""
    voice = db.get("voices", voice_id)
    if not voice or not datasets.consent_ok(voice):
        raise datasets.ConsentMissing("這個聲音目前沒有有效的同意紀錄（可能已撤回），已停止。")


def plan(dataset_id: str, engine_id: str, preset_id: str, gpu: str | None = None, usd_h: float | None = None,
         params: dict | None = None) -> dict:
    """What a run will use and roughly cost, shown before the user confirms. The parameters returned here are the
    exact ones that start() stores and the pod receives."""
    ds = db.get("datasets", dataset_id)
    if not ds:
        raise KeyError(dataset_id)
    eng = engines.get(engine_id)
    p = eng.preset(preset_id)
    gpu = gpu or p.gpu[0]
    usd_h = usd_h or runpod.GPUS.get(gpu, {}).get("usd_h", 1.5)
    st = config.load_settings()
    n_train = int(ds["meta"].get("n_train") or ds["n_items"])
    warnings, blocked = [], None
    try:
        eff = eng.effective_params(p.id, params, n_train)
    except ValueError as e:
        eff, blocked = {**p.params, **(params or {})}, str(e)
    measured = (st.get("speed") or {}).get(_speed_key(eng.id, p.id, gpu), {}).get("s_per_step")
    est = eng.estimate(ds["hours"], p.id, usd_h, n_train=n_train, s_per_step=measured, params=eff)
    limit = float(st.get("runpod_max_hours") or 12)
    if ds["hours"] < p.min_hours:
        warnings.append(f"這個設定建議至少 {p.min_hours:g} 小時已核可語音，目前只有 {ds['hours']:.2f} 小時。")
    if (eff.get("epochs_effective") or 0) > 3:
        warnings.append(f"實際會跑約 {eff['epochs_effective']} 個 epoch，資料少時容易「背答案」。")
    if est["hours"] > limit:
        warnings.append(f"預估時間超過你設定的上限 {limit:g} 小時，訓練會在上限時被強制停止。請到設定調高上限。")
    if not ds["meta"].get("reference_items") and not ds["meta"].get("reference"):
        warnings.append("資料集沒有 5–12 秒的參考片段，樣本比較會比較不準。")
    return {"engine": eng.id, "preset": p.id, "gpu": gpu, "usd_per_hour": usd_h, "data_hours": ds["hours"],
            "n_train": n_train, "steps": est["steps"], "epochs_effective": eff.get("epochs_effective"),
            "estimate_hours": est["hours"], "estimate_usd": est["usd"], "estimate_basis": est["basis"],
            "max_hours": limit, "max_usd": round(limit * usd_h, 2), "disk_gb": p.disk_gb, "ram_gb": p.ram_gb,
            "params": eff, "warnings": warnings, "blocked": blocked}


def start(dataset_id: str, engine_id: str, preset_id: str, gpu: str | None = None, name: str = "",
          params: dict | None = None, usd_h: float | None = None) -> dict:
    ds = db.get("datasets", dataset_id)
    _require_consent(ds["voice_id"])
    pl = plan(dataset_id, engine_id, preset_id, gpu, usd_h, params)
    if pl["blocked"]:
        raise ValueError(pl["blocked"])
    loc = runpod.location()
    tid = db.new_id("tr")
    db.insert("trainings", {"id": tid, "voice_id": ds["voice_id"], "dataset_id": dataset_id, "engine": engine_id,
                            "preset": {"id": pl["preset"], "params": pl["params"], "name": name},
                            "target": "runpod", "status": "queued", "gpu": pl["gpu"], "storage": loc,
                            "remote_prefix": f"vs/jobs/{tid}", "progress": {}, "cost_estimate": pl["estimate_usd"],
                            "created_at": db.now()})
    job = jobs.submit("cloud_train", {"training_id": tid}, message="準備上傳")
    return db.update("trainings", tid, {"job_id": job["id"]})


def _set(tid: str, **kw) -> None:
    db.update("trainings", tid, kw)


def _loc(tr: dict) -> dict:
    return tr.get("storage") or runpod.location()


def package_dataset(tid: str, work: Path) -> tuple[Path, dict]:
    """Export the dataset in the engine's format and pack it with its audio into dataset.tar."""
    tr = db.get("trainings", tid)
    ds = db.get("datasets", tr["dataset_id"])
    eng = engines.get(tr["engine"])
    exp = work / "export"
    shutil.rmtree(exp, ignore_errors=True)
    info = eng.export_dataset(ds, exp, tr["preset"]["params"])
    tar_path = work / "dataset.tar"
    with tarfile.open(tar_path, "w") as t:
        t.add(exp, arcname="data")
        t.add(Path(ds["path"]) / "wavs", arcname="data/wavs")
        t.add(Path(ds["path"]) / "meta.json", arcname="data/meta.json")
    cfg = {"training_id": tid, "engine": eng.id, "preset": tr["preset"]["id"], "params": tr["preset"]["params"],
           "dataset": {"id": ds["id"], "hours": ds["hours"], **info}, "voice_name": ds["meta"]["voice"]["name"],
           "languages": ds["meta"].get("languages", [])}
    return tar_path, cfg


def _remove_pod(tid: str, pod_id: str | None) -> bool:
    """Remove the run's pod and record the outcome; a failure is left for reap() to retry."""
    if not pod_id:
        return True
    try:
        runpod.remove_pod(pod_id)
        _set(tid, pod_state="removed")
        return True
    except Exception as e:
        _set(tid, pod_state="remove_failed", note=f"雲端機器刪除失敗：{str(e)[:200]}。請到 RunPod 確認。")
        return False


def _find_pods(tid: str, loc: dict) -> list[dict]:
    """Pods created for this run (a lost POST response can still have created one, maybe more)."""
    pods = runpod.list_pods(name=f"voice-studio-{tid}", volume=loc.get("volume"))
    return [p for p in pods if (p.get("env") or {}).get("VS_TRAINING_ID", tid) == tid]


@jobs.handler("cloud_train", queue="io")
def cloud_train(ctx: jobs.JobContext) -> dict:
    """Upload → pod → watch → download. Whatever goes wrong, the training row ends in a final state and the pod is
    removed, or marked for removal so reap() keeps trying."""
    tid = ctx.params["training_id"]
    try:
        return _cloud_train(ctx)
    except BaseException as e:
        tr = db.get("trainings", tid)
        if tr and tr["status"] not in ("done", "failed", "canceled"):
            if tr.get("pod_id"):
                _remove_pod(tid, tr["pod_id"])
            elif tr.get("pod_state") == "creating":
                try:
                    for p in _find_pods(tid, _loc(tr)):
                        _remove_pod(tid, p.get("id"))
                except Exception:
                    _set(tid, pod_state="remove_failed")
            _set(tid, status="canceled" if isinstance(e, jobs.Cancelled) else "failed", finished_at=db.now())
            _save_log(tid, tr["remote_prefix"], config.DATA / "jobs" / tid, _loc(tr))
        raise


def _cloud_train(ctx: jobs.JobContext) -> dict:
    tid = ctx.params["training_id"]
    tr = db.get("trainings", tid)
    eng = engines.get(tr["engine"])
    loc = _loc(tr)
    prefix = tr["remote_prefix"]
    work = config.DATA / "jobs" / tid
    work.mkdir(parents=True, exist_ok=True)
    _require_consent(tr["voice_id"])

    resume = bool(ctx.params.get("resume") and tr.get("pod_id"))
    if resume:  # the studio was closed while the pod kept working: pick the run up again
        pod_id = tr["pod_id"]
        deadline = tr.get("deadline") or (tr["created_at"] + float(config.load_settings()["runpod_max_hours"]) * 3600)
        ctx.log(f"resuming watch of pod {pod_id}")
    else:
        # 1. package and upload
        _set(tid, status="uploading")
        ctx.progress(0.01, "整理訓練資料")
        tar_path, cfg = package_dataset(tid, work)
        runpod.put_text(f"{prefix}/config.json", json.dumps(cfg, ensure_ascii=False, indent=2), loc=loc)
        runpod.put_text(f"{prefix}/bootstrap.sh", BOOTSTRAP, loc=loc)
        for fname, text in eng.cloud_files().items():
            runpod.put_text(f"{prefix}/{fname}", text, loc=loc)
        runpod.upload(tar_path, f"{prefix}/dataset.tar", loc=loc,
                      progress=lambda f: ctx.progress(0.02 + 0.16 * f, f"上傳資料 {f * 100:.0f}%"))
        tar_path.unlink(missing_ok=True)
        ctx.check()
        _require_consent(tr["voice_id"])

        # 2. create the pod (intent and deadline are recorded first, so a lost response can be reconciled)
        max_h = float(config.load_settings().get("runpod_max_hours") or 12)
        deadline = time.time() + max_h * 3600 + 900
        _set(tid, status="starting", pod_state="creating", deadline=deadline, started_at=time.time())
        ctx.progress(0.19, "啟動雲端 GPU")
        env = {"VS_TRAINING_ID": tid, "VS_ENGINE": eng.id, "VS_MAX_SECONDS": str(int(max_h * 3600))}
        hf = config.get_secret("hf_token")
        if hf:
            env["HF_TOKEN"] = hf
        preset = eng.preset(tr["preset"]["id"])
        try:
            pod = runpod.create_pod(f"voice-studio-{tid}", eng.image, tr["gpu"], env,
                                    ["bash", "-c", f"bash /workspace/{prefix}/bootstrap.sh"], loc,
                                    container_disk_gb=preset.disk_gb, min_ram_gb=preset.ram_gb,
                                    min_vcpu=preset.vcpu)
        except Exception as e:
            time.sleep(10)
            for p in _find_pods(tid, loc):  # the request may have gone through even though we saw an error
                _remove_pod(tid, p.get("id"))
            _set(tid, pod_state="removed")
            raise RuntimeError(f"沒有租到 GPU：{str(e)[:300]}（這張卡在這個資料中心可能暫時沒貨，換一張試試）")
        pod_id = pod.get("id")
        gpu_actual = (pod.get("machine") or {}).get("gpuTypeId") or tr["gpu"]
        _set(tid, status="running", pod_id=pod_id, pod_state="running", gpu=gpu_actual,
             cost_per_hr=pod.get("costPerHr") or pod.get("adjustedCostPerHr"))
        ctx.log(f"pod {pod_id} created on {gpu_actual} at {pod.get('costPerHr')} /h")

    # 3. watch
    last_poll, s3_errors, partial = 0.0, 0, False
    prog: dict = dict(tr.get("progress") or {})
    try:
        while True:
            ctx.check()
            time.sleep(5)
            if time.time() - last_poll < 30:
                continue
            last_poll = time.time()
            try:
                prog = runpod.get_json(f"{prefix}/progress.json", loc) or prog
                done = runpod.get_json(f"{prefix}/done.json", loc)
                err = runpod.get_json(f"{prefix}/error.json", loc)
                s3_errors = 0
            except Exception as e:  # network or storage hiccup: retry for ~10 minutes before giving up
                s3_errors += 1
                ctx.log(f"storage read failed ({s3_errors}): {e}")
                if s3_errors >= 20:
                    raise RuntimeError("連續 10 分鐘讀不到雲端儲存，已停止並關閉雲端機器。")
                continue
            _set(tid, progress={**prog, "wall_s": int(time.time() - (tr.get("started_at") or tr["created_at"]))})
            ctx.progress(0.2 + 0.65 * _fraction(prog), _phase_label(prog))
            if done:
                partial = done.get("rc", 0) != 0
                break
            if err:
                if runpod.exists(f"{prefix}/model.tar", loc):  # weights were published before the failure
                    partial = True
                    break
                raise RuntimeError(f"雲端訓練失敗（{_stage_label(err)}）。請到「雲端訓練」看紀錄。")
            if time.time() > deadline:
                raise RuntimeError("超過最長時數，已強制停止。")
            try:
                gone = runpod.get_pod(pod_id) is None
            except Exception:
                gone = False
            if gone:
                if runpod.get_json(f"{prefix}/done.json", loc) or runpod.exists(f"{prefix}/model.tar", loc):
                    partial = not runpod.get_json(f"{prefix}/done.json", loc)
                    break
                raise RuntimeError("雲端機器意外消失（可能被平台回收）。可以重試。")
    finally:
        _remove_pod(tid, pod_id)  # normally the pod has already removed itself
    if prog.get("s_per_step"):
        _remember_speed(eng.id, tr["preset"]["id"], db.get("trainings", tid)["gpu"], float(prog["s_per_step"]))

    # 4. download and register
    _set(tid, status="downloading")
    tar_local = work / "model.tar"
    runpod.download(f"{prefix}/model.tar", tar_local, loc=loc,
                    progress=lambda f: ctx.progress(0.86 + 0.1 * f, f"下載模型 {f * 100:.0f}%"))
    samples_local = None
    if runpod.exists(f"{prefix}/samples.tar", loc):
        samples_local = runpod.download(f"{prefix}/samples.tar", work / "samples.tar", loc=loc,
                                        progress=lambda f: ctx.progress(0.96 + 0.03 * f, "下載樣本"))
    _save_log(tid, prefix, work, loc)
    m = install_model(tid, tar_local, samples_local)
    note = "樣本試念沒有完成：模型可以用，但沒有檢查點比較。" if partial or samples_local is None else ""
    _set(tid, status="done", finished_at=db.now(), note=note)
    for name in ("dataset.tar", "model.tar", "samples.tar"):  # keep the volume small; log and config stay
        try:
            runpod.delete(f"{prefix}/{name}", loc)
        except Exception:
            pass
    return {"model_id": m["id"], "message": "訓練完成，模型已下載，正在評分各檢查點"}


def resume_interrupted() -> list[str]:
    """At start-up: runs whose watcher died with the app are picked up again (the pod kept training); a run that
    was creating its pod is reconciled against RunPod's pod list; earlier runs are marked failed."""
    resumed = []
    for tr in db.query("SELECT * FROM trainings WHERE status IN ('queued','uploading','starting','running',"
                       "'downloading')"):
        j = db.get("jobs", tr["job_id"]) if tr.get("job_id") else None
        if j and j["status"] in ("queued", "running"):
            continue
        pod_id = tr.get("pod_id")
        if not pod_id and tr.get("pod_state") == "creating":
            try:
                found = _find_pods(tr["id"], _loc(tr))
            except Exception:
                found = []
            if len(found) == 1:
                pod_id = found[0].get("id")
                _set(tr["id"], pod_id=pod_id, pod_state="running", status="running")
            else:
                for p in found:
                    _remove_pod(tr["id"], p.get("id"))
        if pod_id and tr["status"] in ("starting", "running", "downloading"):
            job = jobs.submit("cloud_train", {"training_id": tr["id"], "resume": True}, "重新連上雲端訓練")
            _set(tr["id"], job_id=job["id"])
            resumed.append(tr["id"])
        else:
            _remove_pod(tr["id"], pod_id)
            _set(tr["id"], status="failed", finished_at=db.now(), note="程式關閉時中斷（還沒開始雲端訓練），請重新開始。")
    return resumed


def reap() -> dict:
    """The safety net outside the pod: retry removals that failed, and find studio pods with no live run."""
    removed, orphans = [], []
    for tr in db.query("SELECT * FROM trainings WHERE pod_state IN ('remove_failed','creating','running') "
                       "AND status IN ('done','failed','canceled')"):
        if tr.get("pod_id") and _remove_pod(tr["id"], tr["pod_id"]):
            removed.append(tr["pod_id"])
    try:
        pods = runpod.studio_pods()
    except Exception as e:
        return {"removed": removed, "orphans": [], "error": str(e)[:200]}
    for p in pods:
        tid = str(p.get("name", ""))[len("voice-studio-"):]
        tr = db.get("trainings", tid)
        if tr and tr["status"] in ("done", "failed", "canceled"):
            try:
                runpod.remove_pod(p["id"])
                removed.append(p["id"])
            except Exception:
                orphans.append({"id": p.get("id"), "name": p.get("name"), "training": tid, "known": True})
        elif not tr:
            orphans.append({"id": p.get("id"), "name": p.get("name"), "training": tid, "known": False,
                            "cost_per_hr": p.get("costPerHr")})
    return {"removed": removed, "orphans": orphans}


CHECKPOINT_NAME = __import__("re").compile(r"^[\w.-]{1,80}$")


def install_model(tid: str, tar_local: Path, samples_tar: Path | None = None) -> dict:
    """Unpack model.tar (and samples.tar) into data/models/<id>, register it once and queue checkpoint scoring."""
    existing = db.query("SELECT * FROM models WHERE training_id=?", (tid,))
    if existing:  # a crash between registering and marking the run done must not register it twice
        return existing[0]
    tr = db.get("trainings", tid)
    ds = db.get("datasets", tr["dataset_id"])
    eng = engines.get(tr["engine"])
    model_id = db.new_id("mdl")
    mdir = config.DATA / "models" / model_id
    tmp = config.DATA / "tmp" / f"unpack-{model_id}"
    for archive in [tar_local] + ([samples_tar] if samples_tar else []):
        with tarfile.open(archive) as t:
            t.extractall(tmp, filter="data")
    emeta = json.loads((tmp / "model" / "engine.json").read_text(encoding="utf-8"))
    bad = [c.get("name") for c in emeta.get("checkpoints", []) if not CHECKPOINT_NAME.match(str(c.get("name", "")))]
    if bad:
        shutil.rmtree(tmp, ignore_errors=True)
        raise ValueError(f"模型檔裡有不合法的檢查點名稱：{bad[:3]}")
    shutil.move(str(tmp / "model"), str(mdir))
    shutil.rmtree(tmp, ignore_errors=True)
    for f in [tar_local] + ([samples_tar] if samples_tar else []):
        f.unlink(missing_ok=True)
    refs = _copy_references(ds, mdir)
    voice = db.get("voices", tr["voice_id"])
    cks = [c for c in emeta.get("checkpoints", []) if c.get("weights")]
    m = db.insert("models", {
        "id": model_id, "voice_id": voice["id"], "engine": eng.id,
        "name": tr["preset"].get("name") or f"{voice['name']} · {eng.name} · {eng.preset(tr['preset']['id']).label}",
        "training_id": tid, "path": str(mdir),
        "meta": {"dataset_id": ds["id"], "preset": tr["preset"], "consent": ds["meta"].get("consent"),
                 "mode": emeta.get("mode"), "checkpoint": cks[-1]["name"] if cks else None, "references": refs,
                 "languages": ds["meta"].get("languages", []), "sampling": emeta.get("sampling")},
        "metrics": {}, "created_at": db.now()})
    if (mdir / "samples").exists():
        jobs.submit("evaluate_model", {"model_id": model_id}, message="評分檢查點")
    return m


def _copy_references(ds: dict, mdir: Path, limit: int = 3) -> list[dict]:
    items = ds["meta"].get("reference_items") or [{"audio": a, "text": "", "lang": ""}
                                                    for a in ds["meta"].get("reference", [])]
    out = []
    (mdir / "references").mkdir(parents=True, exist_ok=True)
    for k, it in enumerate(items[:limit]):
        src = Path(ds["path"]) / it["audio"]
        if not src.exists():
            continue
        dst = mdir / "references" / f"ref{k}.wav"
        shutil.copy2(src, dst)
        out.append({"id": f"ref{k}", "file": f"references/ref{k}.wav", "text": it.get("text", ""),
                    "lang": it.get("lang", ""), "label": "資料集參考 " + str(k + 1), "segment_id": it.get("id")})
    return out


def create_zeroshot(voice_id: str, engine_id: str, segment_ids: list[str], name: str = "") -> dict:
    """A model without training: the base model cloning from reference clips. Free and instant; a good way to hear
    an engine before paying for training, though it copies habits and accent far less than a fine-tuned model."""
    voice = db.get("voices", voice_id)
    if not voice:
        raise KeyError(voice_id)
    if not datasets.consent_ok(voice):
        raise datasets.ConsentMissing("這個聲音的同意紀錄不完整，不能用來合成。")
    eng = engines.get(engine_id)
    if "ref" not in eng.modes({"mode": "zeroshot"}):
        raise ValueError("這個引擎不支援零樣本")
    model_id = db.new_id("mdl")
    mdir = config.DATA / "models" / model_id
    (mdir / "references").mkdir(parents=True, exist_ok=True)
    refs = []
    for k, sid in enumerate(segment_ids[:5]):
        s = db.get("segments", sid)
        if not s or s["voice_id"] != voice_id:
            continue
        shutil.copy2(s["path"], mdir / "references" / f"ref{k}.wav")
        refs.append({"id": f"ref{k}", "file": f"references/ref{k}.wav", "text": s["text"], "lang": s["lang"] or "",
                     "label": (s["text"][:24] + "…") if len(s["text"]) > 24 else s["text"], "segment_id": sid})
    if not refs:
        raise ValueError("請至少選一個這個聲音的片段當參考")
    (mdir / "engine.json").write_text(json.dumps({"engine": eng.id, "mode": "zeroshot", "checkpoints": []}),
                                      encoding="utf-8")
    return db.insert("models", {"id": model_id, "voice_id": voice_id, "engine": eng.id,
                                "name": name or f"{voice['name']} · {eng.name} · 免訓練", "path": str(mdir),
                                "meta": {"mode": "zeroshot", "references": refs, "languages": voice["languages"]},
                                "metrics": {}, "created_at": db.now()})


def add_reference(model_id: str, segment_id: str, label: str = "") -> dict:
    m = db.get("models", model_id)
    s = db.get("segments", segment_id)
    if not m or not s:
        raise KeyError("model or segment")
    if s["voice_id"] != m["voice_id"]:
        raise ValueError("只能用同一個聲音的片段當參考")
    refs = list((m["meta"] or {}).get("references", []))
    k = max([int(r["id"][3:]) for r in refs if r["id"].startswith("ref")] + [-1]) + 1
    mdir = Path(m["path"])
    (mdir / "references").mkdir(parents=True, exist_ok=True)
    shutil.copy2(s["path"], mdir / "references" / f"ref{k}.wav")
    refs.append({"id": f"ref{k}", "file": f"references/ref{k}.wav", "text": s["text"], "lang": s["lang"] or "",
                 "label": label or s["text"][:24], "segment_id": segment_id})
    return db.update("models", model_id, {"meta": {**m["meta"], "references": refs}})


def remove_reference(model_id: str, ref_id: str) -> dict:
    """Only a registered reference can be removed, and only from inside the model's references folder."""
    m = db.get("models", model_id)
    if not m:
        raise KeyError(model_id)
    refs = (m["meta"] or {}).get("references", [])
    ref = next((r for r in refs if r["id"] == ref_id), None)
    if ref is None:
        raise KeyError(ref_id)
    root = (Path(m["path"]) / "references").resolve()
    target = (Path(m["path"]) / ref["file"]).resolve()
    if target.parent != root:
        raise ValueError("不合法的參考片段路徑")
    target.unlink(missing_ok=True)
    return db.update("models", model_id, {"meta": {**m["meta"], "references": [r for r in refs if r is not ref]}})


def _remember_speed(engine_id: str, preset_id: str, gpu: str, s_per_step: float) -> None:
    st = config.load_settings()
    speed = dict(st.get("speed") or {})
    speed[_speed_key(engine_id, preset_id, gpu)] = {"s_per_step": s_per_step, "at": db.now()}
    config.save_settings({"speed": speed})


def _save_log(tid: str, prefix: str, work: Path, loc: dict | None = None) -> None:
    try:
        work.mkdir(parents=True, exist_ok=True)
        (work / "train.log").write_text(runpod.get_text(f"{prefix}/train.log", loc=loc), encoding="utf-8")
    except Exception:
        pass


def _fraction(p: dict) -> float:
    """Overall cloud progress 0–1 across phases (training dominates)."""
    ph = p.get("phase")
    frac = (p.get("step", 0) / p["total"]) if p.get("total") else 0.0
    return {"setup": 0.02, "unpack": 0.04, "download": 0.06, "prepare": 0.08}.get(ph) or \
        {"train": 0.1 + 0.75 * frac, "samples": 0.85 + 0.12 * frac, "package": 0.98}.get(ph, 0.0)


def _phase_label(p: dict) -> str:
    ph = p.get("phase")
    if ph == "setup":
        return "雲端安裝環境（第一次約 10 分鐘，之後會跳過）"
    if ph == "unpack":
        return "解開資料"
    if ph == "download":
        return "下載基礎模型（第一次較久）"
    if ph == "prepare":
        return "預先處理音訊"
    if ph == "samples":
        return f"各檢查點試念樣本 {p.get('step', 0)}/{p.get('total', '?')}"
    if ph == "package":
        return "打包模型"
    if ph == "train" and p.get("total"):
        loss = f"，loss {p['loss']:.3f}" if isinstance(p.get("loss"), (int, float)) else ""
        eta = ""
        if p.get("s_per_step"):
            left = (p["total"] - p.get("step", 0)) * p["s_per_step"] / 60
            eta = f"，約剩 {left:.0f} 分"
        return f"訓練中 {p.get('step', 0)}/{p['total']}{loss}{eta}"
    return "雲端執行中"


def _stage_label(err: dict) -> str:
    return {"setup": "安裝環境", "unpack": "解開資料", "train": "訓練", "package": "打包",
            None: "逾時" if err.get("status") == "timeout" else "未知"}.get(err.get("stage"), err.get("stage") or "?")


def remove_model(model_id: str) -> None:
    m = db.get("models", model_id)
    if m:
        from . import tts
        tts.unload_if(model_id)
        shutil.rmtree(m["path"], ignore_errors=True)
        db.delete("models", model_id)

```

### `vstudio/evaluate.py`

```python
"""Score a trained model's checkpoints on the held-out lines they read aloud in the cloud.

Each sample clip is scored on
- similarity: speaker-embedding cosine to the voice (its enrollment centroid, else the real held-out recordings);
- accuracy: speech recognition of the clip compared with the line it should have said (1 = word for word).

Clips are grouped by generation condition and never mixed: "plain" (the checkpoint alone — what training changed)
and "ref" (with a reference clip — the reference itself carries much of the timbre). The recommendation uses the
"plain" condition, only held-out lines, and only checkpoints whose every clip was scored: the most similar
checkpoint whose accuracy is within 0.05 of the most accurate one. Fine-tuning can raise similarity while the
model starts to skip or invent words, so accuracy gates the choice. Six to twelve lines and one seed are weak
evidence; listening still decides, and the Models page plays every clip next to the real recording.
"""
from __future__ import annotations

import math
from pathlib import Path

import numpy as np

from . import audio, config, db, engines, jobs
from .pipeline import asr, prepare, speaker

CONDITIONS = ("plain", "ref")


def _clip(path: Path) -> np.ndarray:
    y, _ = audio.load(path, 16000)
    return y


def _transcribe(y: np.ndarray, lang: str | None, st: dict) -> str:
    last: Exception | None = None
    for _ in range(2):  # one retry per clip; a single failure never disables scoring for the rest
        try:
            with jobs.GPU_LOCK:
                return asr.transcribe(y, st["asr_secondary"], language=lang or None, device=st["asr_device"])["text"]
        except (ImportError, ModuleNotFoundError):
            raise
        except Exception as e:
            last = e
    raise RuntimeError(str(last))


def _mean(xs: list[float]) -> float | None:
    xs = [x for x in xs if x is not None and math.isfinite(x)]
    return round(float(np.mean(xs)), 4) if xs else None


@jobs.handler("evaluate_model", queue="gpu")
def evaluate_model(ctx: jobs.JobContext) -> dict:
    m = db.get("models", ctx.params["model_id"])
    mdir = Path(m["path"])
    eng = engines.get(m["engine"])
    meta = eng.model_meta(mdir)
    lines = (meta.get("samples") or {}).get("lines", [])
    sdir = mdir / "samples"
    names = [n for n in ["base"] + [c["name"] for c in meta.get("checkpoints", [])] if (sdir / n).exists()]
    if not lines or not names:
        return {"message": "沒有可評分的樣本"}
    st = config.load_settings()
    emb = speaker.Embedder()
    target = prepare.voice_centroids([m["voice_id"]]).get(m["voice_id"])
    ds = db.get("datasets", (m["meta"] or {}).get("dataset_id") or "")
    baseline = []
    gt_embs = []
    if ds:
        gts = [Path(ds["path"]) / ln["audio"] for ln in lines if ln.get("audio")]
        gt_embs = [emb.embed(_clip(g)) for g in gts if g.exists()]
    if target is None and gt_embs:
        c = np.mean(gt_embs, axis=0)
        target = c / (np.linalg.norm(c) + 1e-9)
        if len(gt_embs) > 1:  # each real recording against the others (leave-one-out), so it is not inflated
            baseline = [speaker.cosine(e, np.mean([o for j, o in enumerate(gt_embs) if j != i], axis=0))
                        for i, e in enumerate(gt_embs)]
    elif target is not None:
        baseline = [speaker.cosine(e, target) for e in gt_embs]
    if target is None:
        return {"message": "這個聲音沒有登錄聲紋，也找不到原始資料，無法計算相似度"}

    total = len(names) * len(lines)
    done, asr_available, asr_failures = 0, True, 0
    rows = []
    for name in names:
        clips = []
        for i, ln in enumerate(lines):
            ctx.check()
            for kind in CONDITIONS:
                f = sdir / name / f"{i}_{kind}.wav"
                if not f.exists():
                    continue
                y = _clip(f)
                sim = speaker.cosine(emb.embed(y), target)
                agree = None
                if asr_available:
                    try:
                        heard = _transcribe(y, ln.get("lang"), st)
                        agree = asr.agreement(ln["text"], heard, ln.get("lang") or None)
                    except (ImportError, ModuleNotFoundError):
                        asr_available = False
                    except Exception as e:
                        asr_failures += 1
                        ctx.log(f"ASR failed on {name}/{f.name}: {e}")
                clips.append({"line": i, "kind": kind, "sim": round(sim, 4),
                              "agree": None if agree is None else round(agree, 4), "seen": bool(ln.get("seen"))})
            done += 1
            ctx.progress(done / total, f"評分 {name}")
        summary = {}
        any_held_out = any(not ln.get("seen") for ln in lines)
        for kind in CONDITIONS:
            # held-out lines only; a tiny dataset without any still gets numbers, marked as seen-only
            cs = [c for c in clips if c["kind"] == kind and (not c["seen"] or not any_held_out)]
            if cs:
                summary[kind] = {"sim": _mean([c["sim"] for c in cs]), "agree": _mean([c["agree"] for c in cs]),
                                 "n": len(cs), "complete": all(c["agree"] is not None for c in cs),
                                 "seen_only": not any_held_out}
        rows.append({"name": name, "summary": summary, "clips": clips,
                     # kept for older UI code: the "plain" numbers when there are any, else "ref"
                     "sim": (summary.get("plain") or summary.get("ref") or {}).get("sim"),
                     "agree": (summary.get("plain") or summary.get("ref") or {}).get("agree")})

    held_out = sum(1 for ln in lines if not ln.get("seen"))
    with_weights = {c["name"] for c in meta.get("checkpoints", []) if c.get("weights")}
    eligible = [r for r in rows if r["name"] in with_weights and (s := r["summary"].get("plain"))
                and s["complete"] and s["n"] == held_out and s["sim"] is not None and s["agree"] is not None]
    rec, reason = None, ""
    if not held_out:
        reason = "資料太少，所有試念句子都用在訓練裡，無法客觀比較；請用耳朵選。"
    elif not asr_available:
        reason = "這台電腦沒有語音辨識模型，只算了相似度；請用耳朵選。"
    elif not eligible:
        reason = "有檢查點的樣本或辨識結果不完整，沒有自動推薦；請用耳朵選。"
    else:
        best_agree = max(r["summary"]["plain"]["agree"] for r in eligible)
        ok = [r for r in eligible if r["summary"]["plain"]["agree"] >= best_agree - 0.05]
        rec = max(ok, key=lambda r: r["summary"]["plain"]["sim"])["name"]
    base_plain = next((r["summary"].get("plain") for r in rows if r["name"] == "base"), None)
    rec_plain = next((r["summary"]["plain"] for r in rows if r["name"] == rec), None) if rec else None
    improved = None
    if base_plain and rec_plain and base_plain.get("sim") is not None:
        improved = rec_plain["sim"] > base_plain["sim"]
    metrics = {"checkpoints": rows, "recommended": rec, "reason": reason, "improved_over_base": improved,
               "baseline_sim": _mean(baseline), "asr": asr_available, "asr_failures": asr_failures,
               "held_out_lines": held_out, "conditions": meta.get("sample_conditions") or {},
               "evaluated_at": db.now()}
    new_meta = dict(m["meta"] or {})
    if rec and not new_meta.get("checkpoint_chosen_by_user"):
        new_meta["checkpoint"] = rec
    db.update("models", m["id"], {"metrics": metrics, "meta": new_meta})
    return {"recommended": rec, "message": f"評分完成，建議使用 {rec}" if rec else f"評分完成。{reason}"}

```

### `vstudio/tts.py`

```python
"""Text to speech: single lines, best-of-N takes, and whole scene scripts."""
from __future__ import annotations

import json
import re
import threading
from pathlib import Path

import numpy as np

from . import audio, config, datasets, db, engines, jobs
from .pipeline import asr

_loaded: dict = {"key": None, "handle": None, "engine": None}
_load_lock = threading.Lock()

KANA = re.compile(r"[\u3040-\u30ff\u4e00-\u9fff]")


def detect_language(text: str) -> str:
    """Good enough for ja/en scripts: any kana or kanji means Japanese."""
    return "ja" if KANA.search(text) else "en"


def _handle(model_id: str):
    """Keep one model in GPU memory at a time; switching models (or checkpoints) unloads the previous one."""
    m = db.get("models", model_id)
    if not m:
        raise KeyError(model_id)
    ck = (m["meta"] or {}).get("checkpoint")
    key = (model_id, ck)
    with _load_lock:
        if _loaded["key"] == key:
            return m, _loaded["engine"], _loaded["handle"]
        if _loaded["handle"] is not None:
            _loaded["engine"].unload(_loaded["handle"])
            _loaded.update(key=None, handle=None, engine=None)
        eng = engines.get(m["engine"])
        ok, why = eng.available()
        if not ok:
            raise RuntimeError(f"{eng.name}：{why}")
        h = eng.load(Path(m["path"]), ck)
        _loaded.update(key=key, handle=h, engine=eng)
        return m, eng, h


def unload() -> None:
    with jobs.GPU_LOCK, _load_lock:
        if _loaded["handle"] is not None:
            _loaded["engine"].unload(_loaded["handle"])
        _loaded.update(key=None, handle=None, engine=None)


def unload_if(model_id: str) -> None:
    if _loaded["key"] and _loaded["key"][0] == model_id:
        unload()


def loaded() -> dict | None:
    k = _loaded["key"]
    return {"model_id": k[0], "checkpoint": k[1]} if k else None


def reference(m: dict, ref_id: str | None) -> dict | None:
    refs = (m["meta"] or {}).get("references") or []
    r = next((x for x in refs if x["id"] == ref_id), refs[0] if refs else None)
    if not r:
        return None
    return {"id": r["id"], "path": Path(m["path"]) / r["file"], "text": r.get("text", ""), "lang": r.get("lang", "")}


def apply_lexicon(text: str, lang: str | None) -> str:
    """Replace words with how they should be read (names, readings the engine gets wrong). Longest entries first,
    so 「推しの子」 wins over 「推し」. The original text is kept for display and for the ASR check."""
    entries = [e for e in (config.load_settings().get("lexicon") or [])
               if e.get("from") and e.get("to") and (not e.get("lang") or not lang or e["lang"] == lang)]
    for e in sorted(entries, key=lambda e: -len(e["from"])):
        text = text.replace(e["from"], e["to"])
    return text


def _screen(y: np.ndarray, sr: int, text: str, lang: str | None) -> dict:
    """Transcribe a take and compare it with the requested text (catches skipped, repeated or garbled words)."""
    try:
        x16 = audio.resample(y, sr, 16000)
        st = config.load_settings()
        t = asr.transcribe(x16, st["asr_secondary"], language=lang, device=st["asr_device"])
        return {"heard": t["text"], "match": round(asr.agreement(text, t["text"], lang or t["lang"]), 3)}
    except Exception as e:  # ASR not installed (e.g. test machines)
        return {"heard": "", "match": None, "note": str(e)[:120]}


def generate(model_id: str, text: str, language: str | None = None, style: str = "", takes: int = 1,
             seed: int | None = None, screen: bool = True, batch: str | None = None, mode: str | None = None,
             ref_id: str | None = None, extra: dict | None = None) -> dict:
    """Generate `takes` versions, score them, keep all, and mark the best. The whole request (model load,
    synthesis and the ASR check) holds the GPU, so no other job loads a model under it."""
    with jobs.GPU_LOCK:
        return _generate(model_id, text, language, style, takes, seed, screen, batch, mode, ref_id, extra)


def _generate(model_id, text, language, style, takes, seed, screen, batch, mode, ref_id, extra) -> dict:
    m0 = db.get("models", model_id)
    if not m0:
        raise KeyError(model_id)
    voice = db.get("voices", m0["voice_id"])
    if m0["engine"] != "mock" and (not voice or not datasets.consent_ok(voice)):
        raise datasets.ConsentMissing("這個聲音目前沒有有效的同意紀錄（可能已撤回），不能合成。")
    m, eng, h = _handle(model_id)
    meta = eng.model_meta(Path(m["path"]))
    modes = eng.modes(meta)
    mode = mode if mode in modes else modes[0]
    text_engine, tag_style = eng.render_tags(text)
    if eng.supports_tags:
        text_engine = text
    full_style = ", ".join(s for s in (tag_style, style) if s)
    lang = language if language and language != "auto" else detect_language(text_engine)
    ref = reference(m, ref_id) if mode in ("ref", "hifi") else None
    if mode in ("ref", "hifi") and ref is None:
        raise ValueError("這個模式需要參考片段，請先在模型頁加入參考片段")
    outs = []
    base_seed = seed if seed is not None else int(np.random.default_rng().integers(0, 2 ** 31 - 1))
    for k in range(max(1, min(8, takes))):
        s = base_seed + k
        syn = eng.synthesize(h, apply_lexicon(text_engine, lang), language=lang, style=full_style, mode=mode,
                             reference=ref, seed=s, **(extra or {}))
        oid = db.new_id("out")
        path = audio.save(config.DATA / "outputs" / f"{oid}.wav", syn.audio, syn.sr,
                          synthetic={"engine": eng.id, "model": model_id, "voice": m["voice_id"]})
        dur = len(syn.audio) / syn.sr
        sc = _screen(syn.audio, syn.sr, text_engine, lang) if screen else {}
        outs.append(db.insert("outputs", {"id": oid, "model_id": model_id, "text": text,
                                          "params": {"language": lang, "style": full_style, "seed": s,
                                                     "engine": eng.id, "mode": mode,
                                                     "ref": ref["id"] if ref else None,
                                                     "checkpoint": syn.info.get("checkpoint"), **(extra or {})},
                                          "path": str(path), "duration": round(dur, 3), "score": sc,
                                          "batch": batch, "created_at": db.now()}))
    if len(outs) > 1:
        durs = np.array([o["duration"] for o in outs])
        med = float(np.median(durs))
        for o in outs:
            match = o["score"].get("match")
            ratio = o["duration"] / med if med else 1
            o["score"]["rank_value"] = (match if match is not None else 0.5) - abs(1 - ratio) * 0.5
        best = max(outs, key=lambda o: o["score"]["rank_value"])
        for o in outs:
            o["score"]["best"] = o["id"] == best["id"]
            db.update("outputs", o["id"], {"score": o["score"]})
    elif outs:
        outs[0]["score"]["best"] = True
        db.update("outputs", outs[0]["id"], {"score": outs[0]["score"]})
    return {"outputs": outs, "mode": mode, "language": lang}


# --- scene scripts -------------------------------------------------------------------------------------------------

LINE = re.compile(r"^(?P<speaker>[^:]{1,80}?)\s*::\s*(?P<text>.*)$")
RESERVED = {"STAGE", "SFX", "PAUSE", "ROMAJI", "GLOSS", "NOTE"}


def parse_script(text: str) -> list[dict]:
    """The novel-lab scene format: `Name :: [tags] line`, with STAGE/SFX/PAUSE/ROMAJI/GLOSS metadata lines.
    Returns turns and pauses in order; narration and metadata are kept for the listening sheet but not spoken."""
    events = []
    for n, raw in enumerate(text.splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#") or line.startswith("@@"):
            continue
        m = LINE.match(line)
        if not m:
            continue
        who, body = m.group("speaker").strip(), m.group("text").strip()
        if who in RESERVED:
            if who == "PAUSE":
                try:
                    events.append({"kind": "pause", "seconds": float(body), "line": n})
                except ValueError:
                    pass
            elif who in ("ROMAJI", "GLOSS") and events and events[-1]["kind"] == "turn":
                events[-1][who.lower()] = body
            else:
                events.append({"kind": who.lower(), "text": body, "line": n})
            continue
        events.append({"kind": "turn", "speaker": who, "text": body, "line": n})
    return events


@jobs.handler("render_script", queue="gpu")
def render_script(ctx: jobs.JobContext) -> dict:
    """Render a whole scene: every turn with its cast model, joined with natural gaps and PAUSE lines."""
    p = ctx.params
    events = parse_script(p["script"])
    cast: dict = p["cast"]  # speaker name → {model_id, language, style}
    batch = db.new_id("scene")
    turns = [e for e in events if e["kind"] == "turn" and e["speaker"].lower() != "narrator"]
    missing = sorted({t["speaker"] for t in turns if t["speaker"] not in cast})
    if missing:
        raise ValueError("這些角色還沒有指定聲音：" + "、".join(missing))
    parts, sheet, sr_out = [], [], 48000
    for i, e in enumerate(events):
        ctx.progress(i / max(1, len(events)), f"第 {i + 1}/{len(events)} 行")
        if e["kind"] == "pause" and parts:
            parts[-1] = (parts[-1][0], parts[-1][1] + e["seconds"])
            continue
        if e["kind"] != "turn" or e["speaker"].lower() == "narrator":
            continue
        c = cast[e["speaker"]]
        res = generate(c["model_id"], e["text"], language=c.get("language"), style=c.get("style", ""),
                       takes=int(p.get("takes", 2)), batch=batch, mode=c.get("mode"), ref_id=c.get("ref_id"))
        best = next((o for o in res["outputs"] if o["score"].get("best")), res["outputs"][0])
        y, sr = audio.load(Path(best["path"]), sr_out)
        parts.append((y, float(p.get("gap", 0.35))))
        sheet.append({"line": e["line"], "speaker": e["speaker"], "text": e["text"], "romaji": e.get("romaji"),
                      "output": best["id"], "match": best["score"].get("match")})
    mix = audio.concat(parts, sr_out)
    path = audio.save(config.DATA / "outputs" / f"{batch}.wav", mix, sr_out, synthetic={"scene": batch})
    (config.DATA / "outputs" / f"{batch}.json").write_text(json.dumps(sheet, ensure_ascii=False, indent=2),
                                                           encoding="utf-8")
    db.insert("outputs", {"id": batch, "model_id": None, "text": p["script"][:2000], "params": {"scene": True},
                          "path": str(path), "duration": round(len(mix) / sr_out, 2), "score": {"lines": len(sheet)},
                          "batch": batch, "created_at": db.now()})
    return {"output_id": batch, "lines": len(sheet), "message": f"場景完成：{len(sheet)} 句"}

```

### `vstudio/cloud/runpod.py`

```python
"""RunPod: network volume storage over the S3-compatible API, and GPU pods over the REST API.

Flow for one training run (all from the user's own RunPod account):
1. upload the dataset, the engine's setup and training scripts, and a config to the network volume
   (s3://<volume id>/vs/jobs/<training id>/);
2. create a pod on that volume's datacenter; its start command runs bootstrap.sh, which installs the engine once
   (cached on the volume), trains, writes progress.json while it works and model.tar at the end, then removes itself;
3. the studio polls the pod and progress.json, downloads model.tar when done.json appears, and removes the pod itself
   too if the pod is still there (belt and braces: a forgotten GPU is the main way to lose money).
Keys are read from the OS credential store; they are never written to disk or logs by the studio.
"""
from __future__ import annotations

import json
from pathlib import Path

import httpx

from .. import config

REST = "https://rest.runpod.io/v1"
# S3 endpoints are per datacenter: https://s3api-<dc>.runpod.io (lower-case id; the region is the upper-case id).
# Not every datacenter offers the S3 API; the settings page lists the ones that do.
S3_FMT = "https://s3api-{dc}.runpod.io"

S3_DATACENTERS = ["EU-CZ-1", "EU-RO-1", "EUR-IS-1", "EUR-NO-1", "US-CA-2", "US-GA-2", "US-IL-1", "US-KS-2",
                  "US-MD-1", "US-MO-1", "US-MO-2", "US-NC-1", "US-NC-2", "US-NE-1", "US-WA-1"]

GPUS = {  # Secure Cloud on-demand prices from runpod.io/pricing (updated 2026-09-27); network volumes need Secure Cloud
    "NVIDIA H100 80GB HBM3": {"label": "H100 SXM 80GB", "vram": 80, "usd_h": 3.49},
    "NVIDIA H100 PCIe": {"label": "H100 PCIe 80GB", "vram": 80, "usd_h": 2.89},
    "NVIDIA A100-SXM4-80GB": {"label": "A100 SXM 80GB", "vram": 80, "usd_h": 1.59},
    "NVIDIA A100 80GB PCIe": {"label": "A100 PCIe 80GB", "vram": 80, "usd_h": 1.59},
    "NVIDIA L40S": {"label": "L40S 48GB", "vram": 48, "usd_h": 1.09},
    "NVIDIA RTX 6000 Ada Generation": {"label": "RTX 6000 Ada 48GB", "vram": 48, "usd_h": 0.84},
    "NVIDIA GeForce RTX 5090": {"label": "RTX 5090 32GB", "vram": 32, "usd_h": 0.99},
    "NVIDIA GeForce RTX 4090": {"label": "RTX 4090 24GB", "vram": 24, "usd_h": 0.74},
}


class RunPodError(Exception):
    pass


def _key() -> str:
    k = config.get_secret("runpod_api_key")
    if not k:
        raise RunPodError("尚未設定 RunPod API 金鑰（設定 → 雲端）。")
    return k


def _h() -> dict:
    return {"Authorization": f"Bearer {_key()}", "Content-Type": "application/json"}


def _req(method: str, path: str, **kw):
    with httpx.Client(timeout=60) as c:
        r = c.request(method, REST + path, headers=_h(), **kw)
    if r.status_code >= 400:
        raise RunPodError(f"RunPod {method} {path}: {r.status_code} {r.text[:300]}")
    return r.json() if r.content else {}


def check() -> dict:
    """Verify the API key and the volume; returns the volume's datacenter and size."""
    st = config.load_settings()
    vols = _req("GET", "/networkvolumes")
    vols = vols if isinstance(vols, list) else vols.get("data", vols)
    out = {"ok": True, "volumes": [{"id": v.get("id"), "name": v.get("name"), "dataCenterId": v.get("dataCenterId"),
                                    "size": v.get("size")} for v in vols]}
    vid = st.get("runpod_volume_id")
    if vid:
        match = [v for v in out["volumes"] if v["id"] == vid]
        out["volume"] = match[0] if match else None
    return out


def location() -> dict:
    """The volume and datacenter from settings, frozen into each training run when it starts."""
    st = config.load_settings()
    vol, dc = st.get("runpod_volume_id"), st.get("runpod_datacenter")
    if not vol or not dc:
        raise RunPodError("請先在設定裡填網路磁碟（Network Volume）ID 和它的資料中心。")
    return {"volume": vol, "datacenter": dc, "cloud": st.get("runpod_cloud_type") or "SECURE"}


def create_pod(name: str, image: str, gpu_type: str, env: dict, start_cmd: list[str], loc: dict,
               container_disk_gb: int = 80, min_ram_gb: int = 32, min_vcpu: int = 8) -> dict:
    """Rent exactly the GPU that was quoted (no silent fallback to a pricier card)."""
    body = {"name": name[:180], "imageName": image, "gpuTypeIds": [gpu_type], "gpuTypePriority": "custom",
            "gpuCount": 1, "cloudType": loc.get("cloud") or "SECURE", "networkVolumeId": loc["volume"],
            "dataCenterIds": [loc["datacenter"]], "volumeMountPath": "/workspace",
            "containerDiskInGb": container_disk_gb, "minRAMPerGPU": min_ram_gb, "minVCPUPerGPU": min_vcpu,
            "env": env, "dockerStartCmd": start_cmd, "ports": ["22/tcp"]}
    return _req("POST", "/pods", json=body)


def list_pods(name: str | None = None, volume: str | None = None) -> list[dict]:
    params = {k: v for k, v in (("name", name), ("networkVolumeId", volume)) if v}
    out = _req("GET", "/pods", params=params)
    return out if isinstance(out, list) else out.get("data", [])


def studio_pods() -> list[dict]:
    """Every pod this studio started (named voice-studio-<training id>), for the orphan check."""
    return [p for p in list_pods() if str(p.get("name", "")).startswith("voice-studio-")]


def get_pod(pod_id: str) -> dict | None:
    try:
        return _req("GET", f"/pods/{pod_id}")
    except RunPodError as e:
        if " 404 " in str(e):
            return None
        raise


def remove_pod(pod_id: str) -> None:
    """Delete a pod; a pod that is already gone counts as removed. Other errors propagate."""
    try:
        _req("DELETE", f"/pods/{pod_id}")
    except RunPodError as e:
        if " 404 " not in str(e):
            raise


def gpu_catalog(datacenter: str | None = None) -> list[dict]:
    """Live GPU prices and stock for pods (api.runpod.io/v2/catalog/gpus); falls back to the static table."""
    st = config.load_settings()
    cloud = st.get("runpod_cloud_type") or "SECURE"
    try:
        with httpx.Client(timeout=30) as c:
            r = c.get("https://api.runpod.io/v2/catalog/gpus", headers=_h(),
                      params={"include": "AVAILABILITY", "product": "POD", "cloud": cloud})
        r.raise_for_status()
        out = []
        for g in r.json().get("gpus", []):
            dcs = {d["id"]: d.get("availability") for d in g.get("dataCenters", [])}
            if datacenter and datacenter not in dcs:
                continue
            price = (g.get("price") or {}).get("secure" if cloud == "SECURE" else "community")
            out.append({"id": g["id"], "label": g.get("name") or g["id"], "vram": g.get("memory"), "usd_h": price,
                        "availability": dcs.get(datacenter) if datacenter else g.get("availability")})
        return sorted(out, key=lambda x: (x["usd_h"] is None, x["usd_h"] or 0))
    except Exception:
        return [{"id": k, **v, "availability": None} for k, v in GPUS.items()]


# --- S3 (network volume) ----------------------------------------------------------------------------------------

def s3(loc: dict | None = None):
    import boto3
    from botocore.config import Config
    ak, sk = config.get_secret("runpod_s3_access_key"), config.get_secret("runpod_s3_secret_key")
    if not ak or not sk:
        raise RunPodError("尚未設定 RunPod S3 金鑰（設定 → 雲端）。")
    dc = ((loc or {}).get("datacenter") or config.load_settings().get("runpod_datacenter") or "").strip()
    return boto3.client("s3", aws_access_key_id=ak, aws_secret_access_key=sk, region_name=dc.upper(),
                        endpoint_url=S3_FMT.format(dc=dc.lower()),
                        config=Config(signature_version="s3v4", retries={"max_attempts": 8, "mode": "adaptive"},
                                      s3={"addressing_style": "path"}, connect_timeout=20, read_timeout=120))


def bucket(loc: dict | None = None) -> str:
    return (loc or {}).get("volume") or config.load_settings()["runpod_volume_id"]


def _missing(e: Exception) -> bool:
    from botocore.exceptions import ClientError
    return isinstance(e, ClientError) and e.response.get("Error", {}).get("Code") in ("NoSuchKey", "404", "NotFound")


def upload(local: Path, key: str, progress=None, loc: dict | None = None) -> None:
    from boto3.s3.transfer import TransferConfig
    size = local.stat().st_size
    done = [0]

    def cb(n):
        done[0] += n
        if progress:
            progress(done[0] / max(1, size))
    # parts stay far below the S3 API's 500 MB part limit
    s3(loc).upload_file(str(local), bucket(loc), key, Callback=cb,
                        Config=TransferConfig(multipart_chunksize=64 << 20, max_concurrency=4))


def put_text(key: str, text: str, loc: dict | None = None) -> None:
    s3(loc).put_object(Bucket=bucket(loc), Key=key, Body=text.encode("utf-8"))


def get_json(key: str, loc: dict | None = None) -> dict | None:
    """None only when the object does not exist; network or permission errors propagate to the caller's retry."""
    try:
        obj = s3(loc).get_object(Bucket=bucket(loc), Key=key)
    except Exception as e:
        if _missing(e):
            return None
        raise
    with obj["Body"] as body:
        raw = body.read().decode("utf-8")
    try:
        return json.loads(raw)
    except ValueError:  # caught mid-write; treat as not there yet
        return None


def exists(key: str, loc: dict | None = None) -> bool:
    try:
        s3(loc).head_object(Bucket=bucket(loc), Key=key)
        return True
    except Exception as e:
        if _missing(e):
            return False
        raise


def get_text(key: str, tail: int = 20000, loc: dict | None = None) -> str:
    try:
        obj = s3(loc).get_object(Bucket=bucket(loc), Key=key)
        return obj["Body"].read().decode("utf-8", "replace")[-tail:]
    except Exception:
        return ""


def download(key: str, local: Path, progress=None, loc: dict | None = None) -> Path:
    c = s3(loc)
    size = c.head_object(Bucket=bucket(loc), Key=key)["ContentLength"]
    done = [0]

    def cb(n):
        done[0] += n
        if progress:
            progress(done[0] / max(1, size))
    local.parent.mkdir(parents=True, exist_ok=True)
    c.download_file(bucket(loc), key, str(local), Callback=cb)
    return local


def delete(key: str, loc: dict | None = None) -> None:
    try:
        s3(loc).delete_object(Bucket=bucket(loc), Key=key)
    except Exception as e:
        if not _missing(e):
            raise

```

### `vstudio/server.py`

```python
"""The web app: API under /api, the built web UI everywhere else."""
from __future__ import annotations

import os
import secrets as _secrets
import webbrowser
from contextlib import asynccontextmanager
from urllib.parse import unquote

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse

from . import __version__, config, db, evaluate, jobs, training, tts  # noqa: F401  (modules register job handlers)
from .api import data, docs, speak, system, train, voices
from .engines import install  # noqa: F401  (registers install_engine)
from .pipeline import prepare  # noqa: F401  (registers prepare_source / enroll_voice)

WEB = config.ROOT / "web" / "dist"


def _quiet(fn) -> None:
    try:
        fn()
    except Exception:
        pass


def create_app() -> FastAPI:
    config.ensure_dirs()
    db.connect()

    @asynccontextmanager
    async def lifespan(_app):
        jobs.start()
        try:
            training.resume_interrupted()
        except Exception:  # never block start-up on the cloud
            pass
        import threading  # retry failed pod removals and look for orphaned pods, without delaying start-up
        threading.Thread(target=lambda: _quiet(training.reap), name="reap", daemon=True).start()
        yield
        jobs.stop()

    app = FastAPI(title="Voice Studio", version=__version__, lifespan=lifespan)
    for r in (voices.router, data.router, train.router, speak.router, system.router, docs.router):
        app.include_router(r)

    password = os.environ.get("VSTUDIO_PASSWORD", "")
    local_hosts = {"localhost", "127.0.0.1", "[::1]", "testserver"}
    extra_hosts = {h.strip().lower() for h in os.environ.get("VSTUDIO_ALLOWED_HOSTS", "").split(",") if h.strip()}

    def _hostname(value: str) -> str:
        v = value.strip().lower()
        if v.startswith("["):
            return v.split("]")[0] + "]"
        return v.rsplit(":", 1)[0] if v.count(":") == 1 else v

    @app.middleware("http")
    async def guard(request: Request, call_next):
        """Who may use the API.

        - Default (only this computer): the Host header must name this computer, which blocks DNS-rebinding pages,
          and requests from another website's page (a foreign Origin) are refused, so no site can drive the API.
        - Network mode (VSTUDIO_PASSWORD set): every API request needs the password, whatever its address.
        The web page itself (not /api) is served to anyone who can reach the port, so the login prompt can load."""
        host = _hostname(request.headers.get("host", ""))
        is_api = request.url.path.startswith("/api/")
        if not password and host not in local_hosts | extra_hosts:
            return JSONResponse({"detail": "不允許的主機名稱"}, status_code=403)
        origin = request.headers.get("origin")
        if origin and request.method not in ("GET", "HEAD", "OPTIONS"):
            if _hostname(origin.split("://", 1)[-1]) != host:
                return JSONResponse({"detail": "不允許跨網站的請求"}, status_code=403)
        if password and is_api and request.url.path != "/api/health":
            given = request.headers.get("x-studio-password") or unquote(request.cookies.get("studio_pw") or "")
            if not _secrets.compare_digest(given, password):
                return JSONResponse({"detail": "需要密碼"}, status_code=401)
        return await call_next(request)

    @app.get("/api/health")
    def health():
        return {"ok": True, "version": __version__}

    @app.get("/{full_path:path}")
    def spa(full_path: str):
        if full_path.startswith("api/"):
            return JSONResponse({"detail": "Not Found"}, status_code=404)
        f = (WEB / full_path).resolve()
        if full_path and f.is_file() and WEB.resolve() in f.parents:
            return FileResponse(f)
        index = WEB / "index.html"
        if index.exists():
            return FileResponse(index)
        return JSONResponse({"detail": "web UI not built: run `npm run build` in web/"}, status_code=404)

    return app


app = create_app()


def main() -> None:
    import uvicorn
    st = config.load_settings()
    host, port = os.environ.get("VSTUDIO_HOST", st["host"]), int(os.environ.get("VSTUDIO_PORT", st["port"]))
    if os.environ.get("VSTUDIO_NO_BROWSER") != "1":
        import threading
        threading.Timer(1.5, lambda: webbrowser.open(f"http://127.0.0.1:{port}")).start()
    uvicorn.run(app, host=host, port=port, log_level="warning")


if __name__ == "__main__":
    main()

```

### `vstudio/db.py`

```python
"""SQLite storage. One file (data/studio.db), one connection per thread, JSON columns for flexible fields."""
from __future__ import annotations

import json
import sqlite3
import threading
import time
import uuid
from contextlib import contextmanager

from . import config

SCHEMA = """
CREATE TABLE IF NOT EXISTS voices (
  id TEXT PRIMARY KEY, name TEXT NOT NULL, kind TEXT NOT NULL, languages TEXT NOT NULL DEFAULT '[]',
  notes TEXT NOT NULL DEFAULT '', consent TEXT, consent_doc TEXT, enrollment TEXT NOT NULL DEFAULT '[]',
  created_at REAL NOT NULL
);
CREATE TABLE IF NOT EXISTS sources (
  id TEXT PRIMARY KEY, filename TEXT NOT NULL, path TEXT NOT NULL, duration REAL, status TEXT NOT NULL,
  voice_hint TEXT, language TEXT, meta TEXT NOT NULL DEFAULT '{}', created_at REAL NOT NULL
);
CREATE TABLE IF NOT EXISTS segments (
  id TEXT PRIMARY KEY, source_id TEXT NOT NULL, voice_id TEXT, start REAL NOT NULL, "end" REAL NOT NULL,
  path TEXT NOT NULL, duration REAL NOT NULL, text TEXT NOT NULL DEFAULT '', text_alt TEXT NOT NULL DEFAULT '',
  lang TEXT, asr_agree REAL, spk_sim REAL, snr REAL, clip REAL, cluster INTEGER, score REAL,
  status TEXT NOT NULL DEFAULT 'pending', flags TEXT NOT NULL DEFAULT '[]', edited INTEGER NOT NULL DEFAULT 0
);
CREATE INDEX IF NOT EXISTS seg_voice ON segments(voice_id, status);
CREATE INDEX IF NOT EXISTS seg_source ON segments(source_id);
CREATE TABLE IF NOT EXISTS datasets (
  id TEXT PRIMARY KEY, voice_id TEXT NOT NULL, name TEXT NOT NULL, n_items INTEGER NOT NULL, hours REAL NOT NULL,
  path TEXT NOT NULL, meta TEXT NOT NULL DEFAULT '{}', created_at REAL NOT NULL
);
CREATE TABLE IF NOT EXISTS jobs (
  id TEXT PRIMARY KEY, kind TEXT NOT NULL, queue TEXT NOT NULL, status TEXT NOT NULL, progress REAL NOT NULL DEFAULT 0,
  message TEXT NOT NULL DEFAULT '', params TEXT NOT NULL DEFAULT '{}', result TEXT NOT NULL DEFAULT '{}',
  created_at REAL NOT NULL, started_at REAL, finished_at REAL, cancel INTEGER NOT NULL DEFAULT 0
);
CREATE TABLE IF NOT EXISTS trainings (
  id TEXT PRIMARY KEY, voice_id TEXT NOT NULL, dataset_id TEXT NOT NULL, engine TEXT NOT NULL, preset TEXT NOT NULL,
  target TEXT NOT NULL, status TEXT NOT NULL, pod_id TEXT, gpu TEXT, remote_prefix TEXT, progress TEXT NOT NULL DEFAULT '{}',
  cost_estimate REAL, job_id TEXT, created_at REAL NOT NULL, finished_at REAL
);
CREATE TABLE IF NOT EXISTS models (
  id TEXT PRIMARY KEY, voice_id TEXT NOT NULL, engine TEXT NOT NULL, name TEXT NOT NULL, training_id TEXT,
  path TEXT NOT NULL, meta TEXT NOT NULL DEFAULT '{}', metrics TEXT NOT NULL DEFAULT '{}', created_at REAL NOT NULL
);
CREATE TABLE IF NOT EXISTS outputs (
  id TEXT PRIMARY KEY, model_id TEXT, text TEXT NOT NULL, params TEXT NOT NULL DEFAULT '{}', path TEXT NOT NULL,
  duration REAL, score TEXT NOT NULL DEFAULT '{}', favorite INTEGER NOT NULL DEFAULT 0, batch TEXT, created_at REAL NOT NULL
);
CREATE TABLE IF NOT EXISTS presets (
  id TEXT PRIMARY KEY, name TEXT NOT NULL, source TEXT NOT NULL, model_id TEXT, data TEXT NOT NULL, created_at REAL NOT NULL
);
"""

JSON_COLS = {"languages", "consent", "enrollment", "meta", "flags", "params", "result", "preset", "progress",
             "metrics", "score", "data", "storage"}

_local = threading.local()


def connect() -> sqlite3.Connection:
    c = getattr(_local, "conn", None)
    if c is None:
        f = config.path("studio.db")
        c = sqlite3.connect(f, timeout=30, check_same_thread=False)
        c.row_factory = sqlite3.Row
        c.execute("PRAGMA journal_mode=WAL")
        c.execute("PRAGMA foreign_keys=ON")
        c.executescript(SCHEMA)
        _migrate(c)
        _local.conn = c
    return c


# columns added after the first release: (table, column, declaration)
MIGRATIONS = [
    ("trainings", "storage", "TEXT NOT NULL DEFAULT '{}'"),   # volume + datacenter frozen at start
    ("trainings", "deadline", "REAL"),                        # absolute time the pod must be gone by
    ("trainings", "pod_state", "TEXT"),                       # creating / running / removed / remove_failed
    ("trainings", "started_at", "REAL"),
    ("trainings", "cost_per_hr", "REAL"),
    ("trainings", "note", "TEXT NOT NULL DEFAULT ''"),
]


def _migrate(c: sqlite3.Connection) -> None:
    for table, col, decl in MIGRATIONS:
        cols = {r[1] for r in c.execute(f"PRAGMA table_info({table})")}
        if col not in cols:
            c.execute(f"ALTER TABLE {table} ADD COLUMN {col} {decl}")
    c.execute("CREATE UNIQUE INDEX IF NOT EXISTS models_training ON models(training_id) WHERE training_id IS NOT NULL")
    c.commit()


def reset_connection() -> None:
    c = getattr(_local, "conn", None)
    if c is not None:
        c.close()
        _local.conn = None


@contextmanager
def tx():
    c = connect()
    try:
        yield c
        c.commit()
    except Exception:
        c.rollback()
        raise


def new_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:12]}"


def now() -> float:
    return time.time()


def row(r: sqlite3.Row | None) -> dict | None:
    if r is None:
        return None
    d = dict(r)
    for k in JSON_COLS & d.keys():
        if isinstance(d[k], str):
            try:
                d[k] = json.loads(d[k])
            except json.JSONDecodeError:
                pass
    return d


def rows(rs) -> list[dict]:
    return [row(r) for r in rs]


def dump(v):
    return json.dumps(v, ensure_ascii=False) if not isinstance(v, str) else v


def insert(table: str, data: dict) -> dict:
    cols = list(data)
    vals = [dump(data[k]) if k in JSON_COLS else data[k] for k in cols]
    q = f'INSERT INTO {table} ({", ".join(chr(34) + c + chr(34) for c in cols)}) VALUES ({", ".join("?" * len(cols))})'
    with tx() as c:
        c.execute(q, vals)
    return get(table, data["id"])


def update(table: str, id_: str, data: dict) -> dict | None:
    if not data:
        return get(table, id_)
    cols = list(data)
    vals = [dump(data[k]) if k in JSON_COLS else data[k] for k in cols]
    q = f'UPDATE {table} SET {", ".join(chr(34) + c + chr(34) + "=?" for c in cols)} WHERE id=?'
    with tx() as c:
        c.execute(q, vals + [id_])
    return get(table, id_)


def get(table: str, id_: str) -> dict | None:
    return row(connect().execute(f"SELECT * FROM {table} WHERE id=?", (id_,)).fetchone())


def query(sql: str, args=()) -> list[dict]:
    return rows(connect().execute(sql, args).fetchall())


def delete(table: str, id_: str) -> None:
    with tx() as c:
        c.execute(f"DELETE FROM {table} WHERE id=?", (id_,))

```

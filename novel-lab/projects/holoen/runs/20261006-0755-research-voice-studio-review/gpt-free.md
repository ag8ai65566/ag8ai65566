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
"""Join a project's accepted shots into one playable file.

Why this is not just `ffmpeg -f concat`
---------------------------------------
The concat demuxer copies streams without re-encoding, which is fast and
lossless - and it requires every input to already agree on codec, resolution,
pixel format, frame rate and audio layout. A drama's shots do not agree: the
route for dialogue is a different checkpoint from the route for action, and
different checkpoints produce different frame rates and sizes. Two shots at
16fps and 24fps concatenated without re-encoding produce a file whose second
half plays at the wrong speed.

So each shot is normalised to the project's delivery spec first and then
concatenated. That costs one re-encode. The alternative - silently producing a
file that plays wrong - is not a saving.

Audio is the same problem in miniature: some routes emit sound (S2V, H3) and
some do not, and concatenating a mixture drops the audio track entirely. Every
segment therefore gets an audio track, silent where the shot had none.

This module shells out to ffmpeg. It does not ship one, and it does not pretend
to know whether the user has one - `find_ffmpeg` looks, and the caller reports
what it found rather than failing with "command not found".
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path

# Where ffmpeg tends to be when it is not on PATH. ComfyUI installs frequently
# carry one, and on Windows people unzip it next to the app rather than
# installing it, so a bare `shutil.which` finds nothing and the honest-looking
# conclusion "you do not have ffmpeg" is wrong.
EXTRA_DIRS = (
    "ComfyUI", "ComfyUI/ffmpeg", "ffmpeg", "ffmpeg/bin", "bin",
    "python_embeded", "ComfyUI/venv/Scripts", "venv/Scripts", "venv/bin",
)
NAMES = ("ffmpeg", "ffmpeg.exe", "ffmpeg-linux")


class AssembleError(RuntimeError):
    pass


def find_ffmpeg(root: Path | None = None) -> str:
    """The ffmpeg to use, or "" if there is none to be found.

    Order: an explicit override, then PATH, then the places it tends to be
    unzipped next to this kind of app. The override exists because someone with
    ffmpeg in an unusual place should not have to move it.
    """
    override = (os.environ.get("FFMPEG_BIN") or "").strip()
    if override:
        # An override that does not exist is a mistake worth surfacing, not
        # something to silently fall back from.
        return override if Path(override).is_file() else ""
    found = shutil.which("ffmpeg")
    if found:
        return found
    for base in filter(None, (root, Path.cwd())):
        for folder in EXTRA_DIRS:
            for name in NAMES:
                candidate = Path(base) / folder / name
                if candidate.is_file():
                    return str(candidate)
    return ""


HOW_TO_GET = (
    "找不到 ffmpeg。它是把每顆鏡頭接成一支影片用的，這個 app 沒有內建。\n"
    "Windows：到 https://www.gyan.dev/ffmpeg/builds/ 下載 essentials 版，"
    "解壓縮後把裡面的 ffmpeg.exe 放到 wan-video 資料夾，或加進 PATH。\n"
    "或者在 .env 設 FFMPEG_BIN=完整路徑。"
)


@dataclass
class Segment:
    """One accepted shot, as it will appear in the finished file."""

    path: Path
    seconds: float
    shot_no: int
    # What the file measures, filled in by whoever probed it. `seconds` above is
    # what the *shot list* asked for; these two disagreeing is worth showing.
    media: "Media | None" = None

    def public(self) -> dict:
        out = {"path": self.path.name, "seconds": self.seconds,
               "shot_no": self.shot_no}
        if self.media:
            out["measured"] = self.media.public()
        return out


def _run(args: list[str], timeout: int = 600) -> subprocess.CompletedProcess:
    try:
        return subprocess.run(args, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired as exc:
        raise AssembleError(f"ffmpeg 跑太久了（超過 {timeout} 秒）") from exc
    except OSError as exc:
        raise AssembleError(f"叫不動 ffmpeg：{exc}") from exc


# Encoders in order of preference. Not everything calling itself ffmpeg has
# libx264 - the build bundled with Playwright, for one, has only VP8 - and
# assuming it does produces "Unrecognized option 'preset'", which tells the
# user nothing about what is actually wrong.
VIDEO_ENCODERS = (
    ("libx264", ["-preset", "medium", "-crf", "18"], ".mp4"),
    ("h264_nvenc", ["-preset", "p5", "-cq", "19"], ".mp4"),
    ("mpeg4", ["-q:v", "3"], ".mp4"),
    ("libvpx-vp9", ["-crf", "30", "-b:v", "0"], ".webm"),
    ("libvpx", ["-crf", "30", "-b:v", "1M"], ".webm"),
)
AUDIO_ENCODERS = (("aac", [".mp4"]), ("libopus", [".webm"]), ("libvorbis", [".webm"]))


def encoders(ffmpeg: str) -> set[str]:
    """What this particular ffmpeg can actually encode."""
    result = _run([ffmpeg, "-hide_banner", "-encoders"], timeout=30)
    found = set()
    for line in (result.stdout or "").splitlines():
        parts = line.split()
        if len(parts) >= 2 and parts[0][:1] in ("V", "A", "S"):
            found.add(parts[1])
    return found


@dataclass
class Codecs:
    """The encoders picked for this run, and the container they imply."""

    video: str
    video_args: list[str]
    audio: str
    suffix: str

    def public(self) -> dict:
        return {"video": self.video, "audio": self.audio or "(無音訊)",
                "container": self.suffix}


def filters(ffmpeg: str) -> set[str]:
    result = _run([ffmpeg, "-hide_banner", "-filters"], timeout=30)
    found = set()
    for line in (result.stdout or "").splitlines():
        parts = line.split()
        if len(parts) >= 2 and set(parts[0]) <= set(".TSC"):
            found.add(parts[1])
    return found


def pick_codecs(ffmpeg: str) -> Codecs:
    """Choose the best encoders this build has, rather than assuming."""
    have = encoders(ffmpeg)
    # The silent filler track needs anullsrc. Without it there is no way to give
    # a silent shot an audio stream, so audio is dropped for the whole file
    # rather than kept for some shots and lost at the concat.
    can_silence = "anullsrc" in filters(ffmpeg)
    for name, args, suffix in VIDEO_ENCODERS:
        if name in have:
            audio = next((a for a, boxes in AUDIO_ENCODERS
                          if a in have and suffix in boxes), "")
            if not audio:
                audio = next((a for a, _ in AUDIO_ENCODERS if a in have), "")
            if not can_silence:
                audio = ""
            return Codecs(name, list(args), audio, suffix)
    raise AssembleError(
        "這個 ffmpeg 沒有可以用的影片編碼器。"
        "請換一個完整版的 ffmpeg（gyan.dev 的 essentials 版就可以）。")


def find_ffprobe(ffmpeg: str = "") -> str:
    """The matching ffprobe, or "" if there is none.

    ffprobe is the only thing that answers "how long is this and does it have
    sound" without parsing prose. Nearly every ffmpeg distribution ships it
    beside ffmpeg, so looking next to the ffmpeg already found comes first.
    """
    override = (os.environ.get("FFPROBE_BIN") or "").strip()
    if override:
        return override if Path(override).is_file() else ""
    if ffmpeg:
        beside = Path(ffmpeg).parent
        for name in ("ffprobe", "ffprobe.exe"):
            if (beside / name).is_file():
                return str(beside / name)
    return shutil.which("ffprobe") or ""


def version(binary: str) -> str:
    """The one-line version string, so the panel can name what it found.

    "ffmpeg was found" is not a useful thing to tell someone whose join just
    failed; which build, at which path, is.
    """
    if not binary:
        return ""
    try:
        out = _run([binary, "-version"], timeout=20)
    except AssembleError:
        return ""
    lines = (out.stdout or "").splitlines()
    return lines[0].strip() if lines else ""


@dataclass
class Media:
    """What a file actually is, as opposed to what the project says it is.

    Read from the file rather than from the library record on purpose: a shot
    may have come from H3, from an imported workflow, or from the user's own
    upload, and only some of those ever went through this app's settings.
    """

    seconds: float = 0.0
    width: int = 0
    height: int = 0
    audio: bool = False
    audio_seconds: float = 0.0
    exact: bool = False          # False when this came from the text fallback

    @property
    def ratio(self) -> float:
        return (self.width / self.height) if self.width and self.height else 0.0

    def public(self) -> dict:
        return {"seconds": round(self.seconds, 3), "width": self.width,
                "height": self.height, "audio": self.audio, "exact": self.exact}


def _probe_text(ffmpeg: str, path: Path) -> Media:
    """Last resort: read ffmpeg's own complaint.

    ffprobe is the right tool and this is not it - ffmpeg's -i output is meant
    for humans and its shape is not a promise. It is here so that someone with
    a bare ffmpeg.exe and no ffprobe still gets a joined episode; the one thing
    that needs certainty - whether a shot has to be cropped - refuses to guess
    from it instead.
    """
    out = _run([ffmpeg, "-i", str(path), "-hide_banner"], timeout=60)
    media = Media()
    for line in (out.stderr or "").splitlines():
        if "Duration:" in line and not media.seconds:
            stamp = line.split("Duration:")[1].split(",")[0].strip()
            try:
                hours, minutes, seconds = stamp.split(":")
                media.seconds = int(hours) * 3600 + int(minutes) * 60 + float(seconds)
            except ValueError:
                pass
        if "Audio:" in line:
            media.audio = True
        if "Video:" in line and not media.width:
            found = re.search(r"(\d{2,5})x(\d{2,5})", line)
            if found:
                media.width, media.height = int(found.group(1)), int(found.group(2))
    media.audio_seconds = media.seconds if media.audio else 0.0
    return media


def probe(path: Path, *, ffprobe: str = "", ffmpeg: str = "") -> Media:
    """Duration, size and whether there is sound - measured, not assumed."""
    if not ffprobe:
        return _probe_text(ffmpeg, path) if ffmpeg else Media()
    out = _run([ffprobe, "-v", "error", "-show_streams", "-show_format",
                "-of", "json", str(path)], timeout=60)
    try:
        data = json.loads(out.stdout or "{}")
    except json.JSONDecodeError:
        return _probe_text(ffmpeg, path) if ffmpeg else Media()
    media = Media(exact=True)
    try:
        media.seconds = float((data.get("format") or {}).get("duration") or 0.0)
    except (TypeError, ValueError):
        media.seconds = 0.0
    for stream in data.get("streams") or []:
        kind = stream.get("codec_type")
        if kind == "video" and not media.width:
            media.width = int(stream.get("width") or 0)
            media.height = int(stream.get("height") or 0)
            if not media.seconds:
                try:
                    media.seconds = float(stream.get("duration") or 0.0)
                except (TypeError, ValueError):
                    pass
        elif kind == "audio":
            media.audio = True
            try:
                media.audio_seconds = float(stream.get("duration") or 0.0)
            except (TypeError, ValueError):
                media.audio_seconds = 0.0
    if media.audio and not media.audio_seconds:
        media.audio_seconds = media.seconds
    return media


# Measuring costs a subprocess per file, and the panel that needs the numbers
# re-renders whenever the project is saved. A file's identity here is its path,
# size and modification time: a regenerated take is a new file with a new name,
# and an edited one changes mtime, so a stale entry cannot survive either.
_PROBES: dict[tuple, Media] = {}
PROBE_CACHE_MAX = 512


def probe_cached(path: Path, *, ffprobe: str = "", ffmpeg: str = "") -> Media:
    """`probe`, remembered. Same answer, one subprocess per file per version."""
    try:
        stat = path.stat()
        key = (str(path), stat.st_size, stat.st_mtime_ns, bool(ffprobe))
    except OSError:
        return probe(path, ffprobe=ffprobe, ffmpeg=ffmpeg)
    if key not in _PROBES:
        if len(_PROBES) >= PROBE_CACHE_MAX:
            _PROBES.clear()
        _PROBES[key] = probe(path, ffprobe=ffprobe, ffmpeg=ffmpeg)
    return _PROBES[key]


def probe_duration(ffmpeg: str, path: Path, ffprobe: str = "") -> float:
    """Length in seconds. Its own name because the finished file needs only
    this one number."""
    return probe(path, ffprobe=ffprobe, ffmpeg=ffmpeg).seconds


# How to deal with a shot whose shape is not the delivery shape. Cropping and
# letterboxing are both losses; which one is acceptable is the user's call, not
# a default worth burying, so when it actually matters the join asks.
FITS = {
    "cover": "裁切填滿（不留黑邊，但畫面邊緣會被切掉）",
    "contain": "完整放入（不切畫面，但上下或左右會有黑邊）",
}


def fit_filter(fit: str, width: int, height: int) -> str:
    """The scale/crop/pad chain for one fit policy."""
    if fit == "cover":
        return (f"scale={width}:{height}:force_original_aspect_ratio=increase,"
                f"crop={width}:{height}")
    return (f"scale={width}:{height}:force_original_aspect_ratio=decrease,"
            f"pad={width}:{height}:(ow-iw)/2:(oh-ih)/2:color=black")


# A shot within this much of the delivery ratio needs no crop and no bars: the
# scale/pad chain would add a border a pixel or two wide, which nobody wants to
# be asked about. Wider than this and something visibly goes.
RATIO_TOLERANCE = 0.01


def _measured(segment: Segment) -> bool:
    """Whether this shot's shape is known well enough to act on.

    `exact` is the point: only ffprobe's structured output counts. The text
    fallback often does produce a WxH, but it comes from parsing output meant
    for humans, and cropping someone's picture on the strength of a guess is
    exactly the thing not to do. Without ffprobe nothing is off-ratio, so the
    crop question is never asked and nothing is ever cropped.
    """
    return bool(segment.media and segment.media.exact
                and segment.media.width and segment.media.height)


def off_ratio(segments: list[Segment], width: int, height: int) -> list[int]:
    """Shot numbers whose shape does not match the delivery.

    Only shots that were actually measured count. A shot whose probe failed is
    not reported as fine - `unmeasured` below says so separately - because
    "we could not tell" and "it matches" are different answers.
    """
    want = (width / height) if height else 0.0
    if not want:
        return []
    return [s.shot_no for s in segments
            if _measured(s) and abs(s.media.ratio - want) > RATIO_TOLERANCE]


def unmeasured(segments: list[Segment]) -> list[int]:
    """Shot numbers whose shape is not known for certain."""
    return [s.shot_no for s in segments if not _measured(s)]


def normalise_args(ffmpeg: str, source: Path, target: Path, *,
                   width: int, height: int, fps: int, codecs: Codecs,
                   fit: str = "contain", media: Media | None = None) -> list[str]:
    """The exact ffmpeg command for one shot. Pure, so it can be tested.

    Split out from `normalise` on purpose. This project has no ffmpeg that can
    read or write a real video - the one in its container is a stripped
    Playwright helper with two filters and no demuxers - so the conversion
    itself cannot be exercised here. What *can* be checked is the command, and
    that is where the bugs of this kind live: a missing `-r` leaves the frame
    rate wrong, a wrong map order drops the audio, a bare scale stretches faces.
    """
    media = media or Media()
    # Whether the silent filler is needed is decided per shot, not per run.
    # Mapping both `0:a?` and the silence gives a file with *two* audio tracks
    # when the shot already had sound - which players resolve differently and
    # concat then has to reconcile.
    fill_silence = bool(codecs.audio) and not media.audio
    args = [ffmpeg, "-y", "-i", str(source)]
    if fill_silence:
        # So a shot with no sound still has an audio stream: concatenating a
        # mixture of with-audio and without drops the audio entirely.
        args += ["-f", "lavfi", "-i",
                 "anullsrc=channel_layout=stereo:sample_rate=48000"]
    # `-r` as an output option rather than the `fps` filter, and no `setsar`:
    # both filters are absent from cut-down ffmpeg builds, while `-r` is a core
    # output option that every build has. Same result, fewer ways to fail on a
    # machine whose ffmpeg came bundled with something else.
    args += [
        "-filter_complex", f"[0:v]{fit_filter(fit, width, height)}[v]",
        "-map", "[v]", "-r", str(fps),
    ]
    if codecs.audio:
        args += ["-map", "1:a" if fill_silence else "0:a",
                 "-c:a", codecs.audio, "-ar", "48000", "-ac", "2"]
    else:
        args += ["-an"]
    args += ["-map_metadata", "-1",
             "-c:v", codecs.video, *codecs.video_args, "-pix_fmt", "yuv420p"]
    if fill_silence:
        # anullsrc never ends, so without this the encode never ends either.
        # This is the only case `-shortest` is correct here: with a real audio
        # track it would cut the *picture* short whenever the sound ran out
        # first, which is a silent way to lose the end of a shot.
        args += ["-shortest"]
    elif media.audio and media.seconds and media.audio_seconds > media.seconds + 0.05:
        # Sound that outlasts the picture would otherwise stretch the segment,
        # and every following shot would land late.
        args += ["-t", f"{media.seconds:.3f}"]
    return args + [str(target)]


def normalise(ffmpeg: str, source: Path, target: Path, *,
              width: int, height: int, fps: int, codecs: Codecs,
              fit: str = "contain", media: Media | None = None) -> None:
    """Re-encode one shot to the delivery spec, with an audio track guaranteed."""
    result = _run(normalise_args(
        ffmpeg, source, target, width=width, height=height, fps=fps,
        codecs=codecs, fit=fit, media=media))
    if result.returncode != 0 or not target.is_file():
        tail = (result.stderr or "").strip().splitlines()[-3:]
        raise AssembleError(f"第 {source.name} 段轉檔失敗：" + " / ".join(tail))


def concat_args(ffmpeg: str, listing: Path, target: Path) -> list[str]:
    """The join command. A stream copy - the parts already agree by now.

    `+faststart` only for mp4: it moves the index to the front so the file
    starts playing before it has fully downloaded, and it is meaningless in a
    webm.
    """
    args = [ffmpeg, "-y", "-f", "concat", "-safe", "0", "-i", str(listing), "-c", "copy"]
    if target.suffix.lower() == ".mp4":
        args += ["-movflags", "+faststart"]
    return args + [str(target)]


def concat(ffmpeg: str, parts: list[Path], target: Path, workdir: Path) -> None:
    """Join the normalised parts. They now agree, so this is a stream copy."""
    listing = workdir / "concat.txt"
    # The concat demuxer's own quoting rules: a single quote inside a quoted
    # path has to be closed, escaped and reopened. Our own part files never
    # contain one, but the listing is built the same way regardless - a path
    # containing a quote would otherwise truncate the filename silently.
    listing.write_text(
        "".join("file '%s'\n" % p.as_posix().replace("'", "'\\''")
                for p in parts),
        encoding="utf-8")
    result = _run(concat_args(ffmpeg, listing, target))
    if result.returncode != 0 or not target.is_file():
        tail = (result.stderr or "").strip().splitlines()[-3:]
        raise AssembleError("接起來的時候失敗了：" + " / ".join(tail))


def free_space(path: Path) -> int:
    """Bytes free where the output is going, or -1 if that cannot be read."""
    try:
        target = path if path.exists() else path.parent
        return shutil.disk_usage(target).free
    except OSError:
        return -1


def build(segments: list[Segment], target: Path, *, width: int, height: int,
          fps: int, ffmpeg: str, workdir: Path, ffprobe: str = "",
          fit: str = "contain", on_progress=None) -> dict:
    """Normalise every segment and join them. Returns what was actually made."""
    if not segments:
        raise AssembleError("沒有可以接的鏡頭 —— 每顆鏡頭都要先採用一支影片。")
    if not ffmpeg:
        raise AssembleError(HOW_TO_GET)
    missing = [s for s in segments if not s.path.is_file()]
    if missing:
        raise AssembleError(
            "有鏡頭的影片檔不見了（第 "
            + "、".join(str(s.shot_no) for s in missing[:6]) + " 顆）。"
            "可能是檔案被刪掉或搬走了，那幾顆要重新生成或重新採用。")

    codecs = pick_codecs(ffmpeg)
    if target.suffix.lower() != codecs.suffix:
        target = target.with_suffix(codecs.suffix)
    # Each segment is re-encoded before the join, so the run needs room for the
    # parts *and* the finished file at once. Running out halfway leaves a
    # truncated file that plays until it stops, which looks like a bad join.
    planned = sum(s.seconds for s in segments) or 1.0
    need = int(planned * width * height * fps * 0.09) + (64 << 20)
    have = free_space(target.parent if target.parent.exists() else workdir.parent)
    if 0 <= have < need:
        raise AssembleError(
            f"磁碟空間可能不夠：估計需要約 {need // (1 << 20)} MB，"
            f"這顆硬碟只剩 {have // (1 << 20)} MB。"
            "清一些空間再接，中途空間用完會留下一個播到一半就斷掉的檔案。")

    workdir.mkdir(parents=True, exist_ok=True)
    parts: list[Path] = []
    for index, segment in enumerate(segments):
        if on_progress:
            on_progress(index / (len(segments) + 1),
                        f"處理第 {segment.shot_no} 顆（{index + 1}/{len(segments)}）")
        part = workdir / f"part{index:03d}{codecs.suffix}"
        normalise(ffmpeg, segment.path, part, width=width, height=height,
                  fps=fps, codecs=codecs, fit=fit,
                  media=segment.media or probe(segment.path, ffprobe=ffprobe,
                                               ffmpeg=ffmpeg))
        parts.append(part)

    if on_progress:
        on_progress(len(segments) / (len(segments) + 1), "接起來…")
    target.parent.mkdir(parents=True, exist_ok=True)
    concat(ffmpeg, parts, target, workdir)

    duration = probe_duration(ffmpeg, target, ffprobe)
    for part in parts:
        part.unlink(missing_ok=True)
    (workdir / "concat.txt").unlink(missing_ok=True)
    return {
        "file": target.name,
        "seconds": round(duration, 2),
        "shots": len(segments),
        "width": width, "height": height, "fps": fps,
        "fit": fit,
        "codecs": codecs.public(),
        # What the shot list said it should be, so a mismatch is visible rather
        # than something the user has to notice by watching.
        "planned_seconds": round(planned, 2),
    }

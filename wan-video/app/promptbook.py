"""Import a document full of prompt examples and make it searchable.

People collect prompts long before they have anywhere to put them - a Word
file, a text dump, a spreadsheet, a folder of screenshots' worth of pasted
Automatic1111 blocks. This reads whatever shape that collection is in and turns
it into entries you can search and click.

Everything runs locally on the machine that holds the file. Nothing here
uploads, phones home, or inspects content for any purpose other than splitting
it into entries.

The hard part is not the file formats, it is that nobody writes these the same
way. So rather than one parser there is a small set of splitters, each of which
reports how confident it is, and the best-scoring one wins. The UI then shows
what was extracted *before* anything is saved, because an automatic guess about
someone else's document should always be reviewable.

.docx is read with zipfile + ElementTree - a .docx is a zip whose text lives in
word/document.xml - so it costs no dependency. PDF needs pypdf, which is
optional: without it, PDFs report a clear message instead of failing.
"""

from __future__ import annotations

import csv
import hashlib
import io
import json
import re
import time
import zipfile
from dataclasses import asdict, dataclass, field
from pathlib import Path
from xml.etree import ElementTree

MAX_ENTRIES = 20000
MAX_FIELD = 8000

TEXT_SUFFIXES = {".txt", ".md", ".markdown", ".text", ".prompt", ".prompts"}
DATA_SUFFIXES = {".json", ".jsonl", ".ndjson", ".csv", ".tsv"}
DOC_SUFFIXES = {".docx", ".pdf"}
SUPPORTED = TEXT_SUFFIXES | DATA_SUFFIXES | DOC_SUFFIXES


@dataclass
class Entry:
    positive: str = ""
    negative: str = ""
    title: str = ""
    tags: list[str] = field(default_factory=list)
    note: str = ""
    source: str = ""
    added: float = field(default_factory=time.time)
    starred: bool = False
    uses: int = 0

    @property
    def key(self) -> str:
        """Identity is the prompt text, so re-importing does not duplicate."""
        blob = (self.positive.strip() + " | " + self.negative.strip()).lower()
        return hashlib.sha1(blob.encode("utf-8")).hexdigest()[:16]

    def public(self) -> dict:
        return {**asdict(self), "id": self.key}


def _clean(text: str) -> str:
    text = (text or "").replace("\r\n", "\n").replace("\r", "\n").strip()
    # Collapse the runs of blank lines that survive a copy-paste out of a PDF.
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text[:MAX_FIELD]


def _looks_like_prompt(text: str) -> bool:
    """Cheap test for 'is this a prompt rather than prose or a heading'."""
    text = text.strip()
    if len(text) < 8 or len(text) > MAX_FIELD:
        return False
    if text.startswith(("#", ">", "|", "```")):
        return False
    # Prompts are overwhelmingly comma-separated tag runs or short descriptive
    # sentences. Anything with several full stops is probably prose about them.
    return text.count(",") >= 1 or len(text.split()) >= 3


# -- getting text out of a file ----------------------------------------------


def read_text(data: bytes, name: str) -> tuple[str, str]:
    """(text, error). Never raises for a merely unreadable file."""
    suffix = Path(name).suffix.lower()
    if suffix == ".docx":
        return _from_docx(data)
    if suffix == ".pdf":
        return _from_pdf(data)
    return decode(data), ""


# A byte-order mark is the only *reliable* signal, so it is checked first and
# the matching codec used outright.
BOMS = (
    (b"\xef\xbb\xbf", "utf-8-sig"),
    (b"\xff\xfe\x00\x00", "utf-32"),
    (b"\x00\x00\xfe\xff", "utf-32"),
    (b"\xff\xfe", "utf-16"),
    (b"\xfe\xff", "utf-16"),
)


def decode(data: bytes) -> str:
    """Text out of bytes, guessing the encoding in an order that cannot lie.

    UTF-16 must be tried *after* the legacy Chinese codecs, not before. Without
    a BOM, almost any even-length byte string decodes as UTF-16LE without error
    - it just produces mojibake - so trying it early silently mangles every
    Big5 file that happens to have an even byte count, while the same file one
    byte longer imports fine. Big5 and GB18030 reject far more byte sequences,
    so a successful decode there means much more.
    """
    for bom, codec in BOMS:
        if data.startswith(bom):
            try:
                return data.decode(codec)
            except (UnicodeDecodeError, LookupError):
                break

    # BOM-less UTF-16 has to be spotted from the bytes, not from a successful
    # decode. Mostly-ASCII UTF-16LE is every other byte NUL, and NUL is
    # perfectly valid UTF-8 - so utf-8 "succeeds" and hands back text riddled
    # with NULs. Real text files contain no NUL at all, so their position is
    # the giveaway: odd offsets mean little-endian, even offsets big-endian.
    head = data[:4096]
    nulls = head.count(0)
    if nulls > len(head) * 0.2:
        odd = sum(1 for i in range(1, len(head), 2) if head[i] == 0)
        codec = "utf-16-le" if odd * 2 > nulls else "utf-16-be"
        try:
            return data.decode(codec)
        except (UnicodeDecodeError, LookupError):
            pass

    for codec in ("utf-8", "big5", "gb18030", "cp932", "utf-16", "cp1252"):
        try:
            text = data.decode(codec)
        except (UnicodeDecodeError, LookupError):
            continue
        # A decode that "succeeds" into NULs or unassigned CJK is the mojibake
        # case; treat it as a failure and let the next codec try.
        if "\x00" in text or (codec == "utf-16" and _mojibake(text)):
            continue
        return text
    return data.decode("utf-8", errors="replace").replace("\x00", "")


def _mojibake(text: str) -> bool:
    sample = text[:2000]
    if not sample:
        return False
    odd = sum(1 for ch in sample if ch not in "\n\r\t" and ord(ch) < 32 or ord(ch) >= 0xE000)
    return odd > len(sample) * 0.05


def _from_docx(data: bytes) -> tuple[str, str]:
    ns = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
    try:
        with zipfile.ZipFile(io.BytesIO(data)) as archive:
            xml = archive.read("word/document.xml")
    except (zipfile.BadZipFile, KeyError, OSError):
        return "", "這個 .docx 讀不開（檔案壞了，或其實不是 Word 檔）"
    try:
        root = ElementTree.fromstring(xml)
    except ElementTree.ParseError:
        return "", "這個 .docx 的內容解析失敗"
    lines = []
    for para in root.iter(f"{ns}p"):
        # A <w:br/> is Shift+Enter in Word: a real line break inside one
        # paragraph. Ignoring it glues consecutive prompts into one line, and
        # a document written that way collapses to a single entry.
        parts = []
        for node in para.iter():
            tag = node.tag
            if tag == f"{ns}t":
                parts.append(node.text or "")
            elif tag in (f"{ns}br", f"{ns}cr"):
                parts.append("\n")
            elif tag == f"{ns}tab":
                parts.append("\t")
        lines.append("".join(parts))
    return "\n".join(lines), ""


def _from_pdf(data: bytes) -> tuple[str, str]:
    try:
        import pypdf
    except (KeyboardInterrupt, SystemExit):
        raise
    except BaseException:  # noqa: BLE001 - deliberately wider than Exception
        # pypdf pulls in `cryptography`, which can be installed but broken. A
        # mismatched cffi makes it raise pyo3's PanicException, and that
        # subclasses BaseException, not Exception - so `except Exception` here
        # does not catch it and one bad optional dependency 500s the import
        # endpoint. Everything except a genuine interrupt is a failed import.
        return "", ("這台機器上的 pypdf 沒辦法載入，所以讀不了 PDF。"
                    "把 PDF 另存成 .txt 或 .docx 再匯入就可以了。")
    try:
        reader = pypdf.PdfReader(io.BytesIO(data))
        return "\n".join((page.extract_text() or "") for page in reader.pages), ""
    except Exception as exc:  # noqa: BLE001 - any malformed PDF, not just one kind
        return "", f"這個 PDF 讀不出文字（{type(exc).__name__}）。可能是掃描的圖片檔。"


# -- splitters ---------------------------------------------------------------

# Keys a JSON/CSV collection might use for each field, best first.
POS_KEYS = ("positive", "prompt", "positive_prompt", "pos", "text", "content", "提詞", "正面")
NEG_KEYS = ("negative", "negative_prompt", "neg", "負面", "負面提詞")
TITLE_KEYS = ("title", "name", "label", "id", "標題", "名稱")
TAG_KEYS = ("tags", "tag", "category", "categories", "標籤", "分類")

_A1111_MARK = re.compile(r"^\s*(Negative prompt:|Steps:\s*\d)", re.M)
_HEADING = re.compile(r"^\s{0,3}(#{1,6})\s+(.+?)\s*#*\s*$")
_NUMBERED = re.compile(r"^\s{0,3}(?:\d{1,3}[.)、]|[-*•]\s)\s*")
_RULE = re.compile(r"^\s*(?:-{3,}|={3,}|\*{3,}|_{3,}|—{3,})\s*$")
# Longest alternative first: regex alternation is first-match-wins, so with
# `negative` ahead of `negative prompt` the line "Negative prompt: x" matches
# only "negative", leaves " prompt:" unconsumed, and the whole line gets glued
# onto the positive instead of becoming the negative.
_LABELLED = re.compile(
    r"^\s*("
    r"negative prompt|negative|neg|負面提詞|負面"
    r"|positive prompt|positive|prompt|提詞|正面"
    r"|title|標題|名稱"
    r"|tags|tag|標籤"
    r")\s*[:：]\s*(.*)$",
    re.I,
)
_NEG_LABELS = {"negative prompt", "negative", "neg", "負面提詞", "負面"}
_POS_LABELS = {"positive prompt", "positive", "prompt", "提詞", "正面"}
_TITLE_LABELS = {"title", "標題", "名稱"}
_TAG_LABELS = {"tags", "tag", "標籤"}


@dataclass
class Parsed:
    entries: list[Entry] = field(default_factory=list)
    how: str = ""
    score: float = 0.0
    note: str = ""


def parse(data: bytes, name: str) -> Parsed:
    """Best-effort extraction of prompt entries from one uploaded file."""
    suffix = Path(name).suffix.lower()
    text, error = read_text(data, name)
    if error:
        return Parsed(note=error)
    if not text.strip():
        return Parsed(note="這個檔案裡沒有文字")

    if suffix in (".json", ".jsonl", ".ndjson"):
        if result := _from_json(text, name):
            return result
    if suffix in (".csv", ".tsv"):
        if result := _from_table(text, name, "\t" if suffix == ".tsv" else ","):
            return result

    # For everything else, try each splitter and keep the best.
    candidates = [
        _split_a1111(text, name),
        _split_labelled(text, name),
        _split_headings(text, name),
        _split_rules(text, name),
        _split_blank_lines(text, name),
        _split_lines(text, name),
    ]
    # A JSON or CSV file with the wrong extension still deserves a chance.
    if result := _from_json(text, name):
        candidates.append(result)
    best = max(candidates, key=lambda p: p.score)
    if not best.entries:
        best.note = best.note or "看不出這個檔案的範例是怎麼分段的"
    return best


def _finish(entries: list[Entry], how: str, name: str, bonus: float = 0.0) -> Parsed:
    kept: list[Entry] = []
    seen: set[str] = set()
    for entry in entries:
        entry.positive = _clean(entry.positive)
        entry.negative = _clean(entry.negative)
        entry.title = _clean(entry.title)[:200]
        entry.source = entry.source or name
        if not _looks_like_prompt(entry.positive):
            continue
        if entry.key in seen:
            continue
        seen.add(entry.key)
        kept.append(entry)
        if len(kept) >= MAX_ENTRIES:
            break
    if not kept:
        return Parsed([], how, 0.0)
    # Prefer the splitter that found more entries *and* richer ones. Length is
    # part of it: a splitter that chopped one prompt into ten fragments scores
    # worse than one that kept them whole.
    average = sum(len(e.positive) for e in kept) / len(kept)
    richness = sum(1 for e in kept if e.negative or e.title or e.tags) / len(kept)
    score = len(kept) * (1 + richness) * min(average / 60.0, 3.0) + bonus
    return Parsed(kept, how, score)


def _from_json(text: str, name: str) -> Parsed | None:
    rows: list = []
    stripped = text.strip()
    try:
        loaded = json.loads(stripped)
        rows = loaded if isinstance(loaded, list) else [loaded]
        if isinstance(loaded, dict):
            # {"a": {...}, "b": {...}} or {"prompts": [...]}
            for value in loaded.values():
                if isinstance(value, list) and value:
                    rows = value
                    break
            else:
                if all(isinstance(v, dict) for v in loaded.values()) and loaded:
                    rows = list(loaded.values())
    except ValueError:
        rows = []
        for line in stripped.splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except ValueError:
                return None
        if not rows:
            return None

    entries: list[Entry] = []
    for row in rows:
        if isinstance(row, str):
            entries.append(Entry(positive=row, source=name))
            continue
        if not isinstance(row, dict):
            continue
        lower = {str(k).lower(): v for k, v in row.items()}
        entry = Entry(
            positive=str(_pick(lower, POS_KEYS) or ""),
            negative=str(_pick(lower, NEG_KEYS) or ""),
            title=str(_pick(lower, TITLE_KEYS) or ""),
            source=name,
        )
        raw_tags = _pick(lower, TAG_KEYS)
        if isinstance(raw_tags, list):
            entry.tags = [str(t) for t in raw_tags][:12]
        elif isinstance(raw_tags, str):
            entry.tags = [t.strip() for t in re.split(r"[,;、]", raw_tags) if t.strip()][:12]
        entries.append(entry)
    if not entries:
        return None
    parsed = _finish(entries, "JSON", name, bonus=50)
    # _finish drops rows whose text does not read as a prompt, so valid JSON
    # with unfamiliar key names can come back empty. Returning that as a result
    # short-circuits the text splitters, which might well have found something.
    return parsed if parsed.entries else None


def _pick(row: dict, keys: tuple[str, ...]):
    for key in keys:
        if key in row and row[key] not in (None, ""):
            return row[key]
    return None


def _from_table(text: str, name: str, delimiter: str) -> Parsed | None:
    try:
        sample = text[:8000]
        dialect = csv.Sniffer().sniff(sample, delimiters=delimiter + ",;\t|")
    except csv.Error:
        dialect = None
    reader = csv.reader(io.StringIO(text), dialect) if dialect else \
        csv.reader(io.StringIO(text), delimiter=delimiter)
    rows = [r for r in reader if any(c.strip() for c in r)]
    if not rows:
        return None

    header = [c.strip().lower() for c in rows[0]]
    has_header = any(h in POS_KEYS + NEG_KEYS + TITLE_KEYS + TAG_KEYS for h in header)
    body = rows[1:] if has_header else rows

    def column(keys: tuple[str, ...]) -> int:
        for key in keys:
            if key in header:
                return header.index(key)
        return -1

    pos_at = column(POS_KEYS) if has_header else -1
    neg_at = column(NEG_KEYS) if has_header else -1
    title_at = column(TITLE_KEYS) if has_header else -1
    tags_at = column(TAG_KEYS) if has_header else -1

    entries: list[Entry] = []
    for row in body:
        def cell(index: int) -> str:
            return row[index].strip() if 0 <= index < len(row) else ""
        if pos_at >= 0:
            positive = cell(pos_at)
        else:
            # No header: take the longest cell, which is the prompt in practice.
            positive = max((c.strip() for c in row), key=len, default="")
        entry = Entry(positive=positive, negative=cell(neg_at),
                      title=cell(title_at), source=name)
        if tags := cell(tags_at):
            entry.tags = [t.strip() for t in re.split(r"[,;、]", tags) if t.strip()][:12]
        entries.append(entry)
    if not entries:
        return None
    parsed = _finish(entries, "表格", name, bonus=40)
    # Same reason as _from_json: an empty result must not short-circuit the
    # text splitters, or a .csv that is really a plain list imports as nothing.
    return parsed if parsed.entries else None


def _split_a1111(text: str, name: str) -> Parsed:
    """Blocks pasted straight out of Automatic1111 / CivitAI.

    Reuses the same parser the image inspector uses, so a document of pasted
    parameter blocks yields the negative prompt and settings too.
    """
    import inspect_image

    if not _A1111_MARK.search(text):
        return Parsed([], "A1111", 0.0)
    chunks = re.split(r"\n\s*\n(?=[^\n]*\S)", text)
    entries: list[Entry] = []
    for chunk in chunks:
        if not _A1111_MARK.search(chunk):
            continue
        found = inspect_image._from_a1111(chunk)
        if found is None or not found.prompt.strip():
            continue
        bits = []
        if found.model:
            bits.append(f"底模 {found.model}")
        if found.steps:
            bits.append(f"{found.steps} 步")
        if found.cfg:
            bits.append(f"CFG {found.cfg}")
        if found.sampler:
            bits.append(found.sampler)
        entries.append(
            Entry(positive=found.prompt, negative=found.negative,
                  note=" · ".join(bits), source=name)
        )
    return _finish(entries, "A1111 參數區塊", name, bonus=60)


def _split_labelled(text: str, name: str) -> Parsed:
    """`Prompt: ...` / `Negative: ...` lines, in any of the usual spellings."""
    entries: list[Entry] = []
    current = Entry(source=name)
    field_now = ""
    seen_label = False

    def flush() -> None:
        nonlocal current
        if current.positive:
            entries.append(current)
        current = Entry(source=name)

    for line in text.splitlines():
        match = _LABELLED.match(line)
        if match:
            seen_label = True
            label, value = match.group(1).lower(), match.group(2)
            if label in _NEG_LABELS:
                field_now = "negative"
                current.negative = (current.negative + " " + value).strip()
            elif label in _TAG_LABELS:
                field_now = ""
                current.tags = [t.strip() for t in re.split(r"[,;、]", value) if t.strip()][:12]
            elif label in _TITLE_LABELS:
                # A title belongs to the entry it introduces. If one is already
                # under way, this starts the next - otherwise the new title
                # overwrites the previous entry's and the last one is lost.
                if current.positive:
                    flush()
                field_now = ""
                current.title = value
            else:
                if current.positive:
                    flush()
                field_now = "positive"
                current.positive = value
        elif line.strip() and field_now:
            setattr(current, field_now, (getattr(current, field_now) + " " + line.strip()).strip())
        elif not line.strip():
            field_now = ""
    flush()
    return _finish(entries, "標籤式（Prompt: / Negative:）", name,
                   bonus=55 if seen_label else 0.0)


def _split_headings(text: str, name: str) -> Parsed:
    """Markdown headings, with the prompt in the body under each."""
    lines = text.splitlines()
    if not any(_HEADING.match(l) for l in lines):
        return Parsed([], "標題", 0.0)
    entries: list[Entry] = []
    title, body = "", []

    def flush() -> None:
        joined = "\n".join(body).strip()
        # Fenced code blocks are the usual way people paste a prompt in Markdown.
        fences = re.findall(r"```[\w-]*\n(.*?)```", joined, re.S)
        for fence in fences:
            entries.append(Entry(positive=fence, title=title, source=name))
        if not fences and joined:
            entries.append(Entry(positive=re.sub(r"^>\s?", "", joined, flags=re.M),
                                 title=title, source=name))

    for line in lines:
        if match := _HEADING.match(line):
            flush()
            title, body = match.group(2), []
        else:
            body.append(line)
    flush()
    return _finish(entries, "Markdown 標題", name, bonus=20)


def _split_rules(text: str, name: str) -> Parsed:
    """Entries separated by --- or === lines."""
    if not any(_RULE.match(l) for l in text.splitlines()):
        return Parsed([], "分隔線", 0.0)
    chunks = re.split(r"\n\s*(?:-{3,}|={3,}|\*{3,}|_{3,}|—{3,})\s*\n", text)
    return _finish([Entry(positive=c, source=name) for c in chunks], "分隔線", name, bonus=15)


def _standalone_lines(lines: list[str]) -> bool:
    """Are these N prompts that happen to be adjacent, or one wrapped prompt?

    A tag dump with no blank lines between entries is extremely common, and
    joining it into one giant entry is the worst possible outcome. The tell is
    that every line is a complete comma-separated prompt in its own right, and
    none of them ends in a comma - a trailing comma means the prompt continues
    onto the next line.
    """
    if len(lines) < 2:
        return False
    if any(l.rstrip().endswith((",", "，")) for l in lines):
        return False
    with_commas = sum(1 for l in lines if "," in l or "，" in l)
    return with_commas >= len(lines) * 0.8


def _split_blank_lines(text: str, name: str) -> Parsed:
    chunks = re.split(r"\n\s*\n", text)
    entries = []
    for chunk in chunks:
        lines = [l for l in chunk.splitlines() if l.strip()]
        if not lines:
            continue
        title = ""
        # A short first line above a block is a title - but only if it does not
        # itself read as a prompt. Length alone is not enough: a block of two
        # short prompts would lose the first one to the title, and because that
        # halves the entry count it can even tie on score and win.
        if (len(lines) > 1 and len(lines[0]) < 40
                and not lines[0].rstrip().endswith((",", "，"))
                and not _looks_like_prompt(lines[0])):
            title, lines = lines[0].strip(" #*-"), lines[1:]
        if _standalone_lines(lines):
            entries += [Entry(positive=l, title=title, source=name) for l in lines]
        else:
            entries.append(Entry(positive="\n".join(lines), title=title, source=name))
    return _finish(entries, "空行分段", name)


def _split_lines(text: str, name: str) -> Parsed:
    """One prompt per line - the fallback, and common for tag dumps."""
    entries = []
    for line in text.splitlines():
        stripped = _NUMBERED.sub("", line).strip()
        if stripped:
            entries.append(Entry(positive=stripped, source=name))
    return _finish(entries, "一行一個", name)


# -- storage -----------------------------------------------------------------


class Book:
    """The imported entries, kept as JSONL next to the outputs."""

    def __init__(self, path: Path) -> None:
        self.path = path
        self.entries: dict[str, Entry] = {}
        self._dirty = False
        self._last_save = 0.0

    def load(self) -> None:
        if not self.path.is_file():
            return
        known = set(Entry.__dataclass_fields__)
        for line in self.path.read_text(encoding="utf-8", errors="replace").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                raw = json.loads(line)
            except ValueError:
                continue
            entry = Entry(**{k: v for k, v in raw.items() if k in known})
            if entry.positive:
                self.entries[entry.key] = entry

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        lines = [json.dumps(asdict(e), ensure_ascii=False) for e in self.entries.values()]
        tmp = self.path.with_suffix(".tmp")
        tmp.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")
        tmp.replace(self.path)
        self._dirty = False
        self._last_save = time.time()

    def add_all(self, entries: list[Entry]) -> tuple[int, int]:
        """(added, skipped-as-duplicate)."""
        added = duplicate = 0
        for entry in entries:
            if entry.key in self.entries:
                duplicate += 1
                continue
            self.entries[entry.key] = entry
            added += 1
        if added:
            self.save()
        return added, duplicate

    def search(self, query: str = "", starred: bool = False,
               limit: int = 200, offset: int = 0) -> tuple[list[Entry], int]:
        words = [w for w in re.split(r"\s+", query.strip().lower()) if w]
        found = []
        for entry in self.entries.values():
            if starred and not entry.starred:
                continue
            if words:
                hay = " ".join(
                    [entry.positive, entry.negative, entry.title, " ".join(entry.tags)]
                ).lower()
                if not all(w in hay for w in words):
                    continue
            found.append(entry)
        # Starred first, then most recently added.
        found.sort(key=lambda e: (not e.starred, -e.added))
        return found[offset:offset + limit], len(found)

    def sources(self) -> list[dict]:
        counts: dict[str, int] = {}
        for entry in self.entries.values():
            counts[entry.source or "?"] = counts.get(entry.source or "?", 0) + 1
        return sorted(
            ({"name": k, "count": v} for k, v in counts.items()),
            key=lambda x: -x["count"],
        )

    def delete(self, entry_id: str) -> bool:
        if self.entries.pop(entry_id, None) is None:
            return False
        self.save()
        return True

    def delete_source(self, source: str) -> int:
        gone = [k for k, e in self.entries.items() if e.source == source]
        for key in gone:
            del self.entries[key]
        if gone:
            self.save()
        return len(gone)

    def star(self, entry_id: str, value: bool) -> bool:
        entry = self.entries.get(entry_id)
        if entry is None:
            return False
        entry.starred = value
        self.save()
        return True

    def used(self, entry_id: str) -> None:
        """Bump the use counter, writing at most once every few seconds.

        Rewriting the whole JSONL on every click stalls the server for as long
        as the file takes to serialise, and a use counter is not worth that. A
        star is - it is an explicit action the user expects to persist - so
        that one still writes through.
        """
        entry = self.entries.get(entry_id)
        if entry is None:
            return
        entry.uses += 1
        self._dirty = True
        if time.time() - self._last_save > 5:
            self.save()

    def flush(self) -> None:
        """Write out anything a debounced update left pending."""
        if getattr(self, "_dirty", False):
            self.save()

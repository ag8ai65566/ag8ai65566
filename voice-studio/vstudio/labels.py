"""Emotion and language labels for imported recordings, from a list (Excel or CSV) or from the file name.

- List: any .xlsx or .csv with a column for the file name (檔名 / file) and columns 情緒 / emotion and 語言 / language.
  Values can be the Chinese labels shown in the app (生氣), the English codes (angry) or language names (日文, ja).
- File name: a tag in brackets, 0815直播[生氣].wav, 【開心】雜談.mp4, talk (angry).wav, or a label at the start
  followed by _ or -, 生氣_0815.wav. Words elsewhere in the name are ignored, so "happy birthday.mp4" is not
  labelled happy by accident.
- Folder: files inside a folder named exactly after a label (生氣/, angry/, 日文/) when a whole folder is imported.

Priority for each file: list, then file name, then folder, then what was chosen on the import page.
"""
from __future__ import annotations

import csv
import io
import re
from pathlib import Path

from . import emotions

LANG_WORDS = {
    "ja": ("ja", "jp", "日文", "日語", "日本語", "japanese"),
    "en": ("en", "英文", "英語", "english"),
    "zh": ("zh", "中文", "國語", "华语", "chinese"),
}
AUTO_WORDS = ("auto", "自動", "自動判斷", "mixed", "混合", "")
NO_EMOTION = ("none", "無", "不標記", "不標", "未標記", "n/a", "-", "—")  # an explicit "no label" in a list
FILE_COLS = ("檔名", "檔案", "檔案名稱", "file", "filename", "file name", "名稱", "path")
EMO_COLS = ("情緒", "情緒標籤", "emotion", "風格", "語氣")
LANG_COLS = ("語言", "language", "lang")
BRACKETS = re.compile(r"[\[【(（]([^\]】)）]{1,20})[\]】)）]")
PREFIX = re.compile(r"^([^_\-\s]{1,8})[_\-]")

TEMPLATE_CSV = (
    "檔名,情緒,語言,備註\n"
    "0815直播_開場.wav,開心,日文,情緒可以填：平靜 開心 興奮 生氣 難過 小聲 笑著說 驚訝 害怕 悄悄話 撒嬌 念稿\n"
    "0815直播_輸了.wav,生氣,日文,語言可以填：日文 英文 中文 自動\n"
    "english_chat.mp4,平靜,英文,\n"
    "雜談合集.mp4,,自動,情緒留空＝不標記（之後在檢查資料頁逐句標）\n")


def emotion_of(text: str | None, strict: bool = False) -> str | None:
    """A label code from a cell or tag: the code itself, the Chinese label, or a word that points at one.

    strict: only a whole label or word (for name prefixes and folder names, where "搞笑" must not mean laughing)."""
    s = (text or "").strip()
    if not s:
        return None
    if s.lower() in emotions.EMOTIONS:
        return s.lower()
    for code, label in emotions.EMOTIONS.items():
        if s == label or s in label.split("／"):
            return code
    if strict:
        return next((code for code, words in emotions.WORDS.items()
                     if s.lower() in (w.rstrip("*") for w in words)), None)
    return emotions.from_style(s)


def language_of(text: str | None) -> str | None:
    s = (text or "").strip().lower()
    for code, words in LANG_WORDS.items():
        if s in words:
            return code
    return None


def from_filename(name: str) -> dict:
    """{"emotion": …, "language": …} found in tags of a file name (missing keys = nothing found)."""
    stem = Path(name).stem
    tokens = [(t, False) for t in BRACKETS.findall(stem)]
    m = PREFIX.match(stem)
    if m:
        tokens.append((m.group(1), True))
    out: dict = {}
    for t, strict in tokens:
        if "emotion" not in out and (e := emotion_of(t, strict)):
            out["emotion"] = e
        if "language" not in out and (lang := language_of(t)):
            out["language"] = lang
    return out


def from_folders(names: list[str] | tuple[str, ...]) -> dict:
    """Labels from the folders a file sits in below the imported folder; the innermost folder wins."""
    out: dict = {}
    for n in reversed(names):
        if "emotion" not in out and (e := emotion_of(n, strict=True)):
            out["emotion"] = e
        if "language" not in out and (lang := language_of(n)):
            out["language"] = lang
    return out


def _rows_from_table(rows: list[list[str]]) -> dict:
    """Find the header row (the first with a file-name column) and read the labels below it."""
    def col(header: list[str], names: tuple) -> int | None:
        for i, h in enumerate(header):
            if h.strip().lower() in names:
                return i
        return None

    start = next((i for i, r in enumerate(rows[:20]) if col([str(c or "") for c in r], FILE_COLS) is not None), None)
    if start is None:
        raise ValueError("清單裡找不到「檔名」欄。第一列要有欄位名稱：檔名、情緒、語言。")
    header = [str(c or "") for c in rows[start]]
    fc, ec, lc = col(header, FILE_COLS), col(header, EMO_COLS), col(header, LANG_COLS)
    out, errors = {}, []
    for n, r in enumerate(rows[start + 1:], start + 2):
        cells = [str(c).strip() if c is not None else "" for c in r]
        fname = cells[fc] if fc < len(cells) else ""
        if not fname:
            continue
        entry: dict = {}
        if ec is not None and ec < len(cells) and cells[ec] and cells[ec].lower() not in NO_EMOTION:
            e = emotion_of(cells[ec])
            if e:
                entry["emotion"] = e
            else:
                errors.append(f"第 {n} 列「{cells[ec]}」不是認得的情緒")
        if lc is not None and lc < len(cells) and cells[lc]:
            lang = language_of(cells[lc])
            if lang:
                entry["language"] = lang
            elif cells[lc].strip().lower() not in AUTO_WORDS:
                errors.append(f"第 {n} 列「{cells[lc]}」不是認得的語言")
        out[Path(fname.replace("\\", "/")).name.lower()] = entry
    return {"rows": out, "errors": errors[:20], "count": len(out)}


def parse_list(data: bytes, filename: str) -> dict:
    """Labels from an uploaded or found .xlsx / .csv file."""
    if filename.lower().endswith((".xlsx", ".xlsm")):
        try:
            import openpyxl
        except ImportError:
            raise ValueError("讀 Excel 需要更新程式（執行 update.bat）；也可以在 Excel 另存成 CSV 再上傳。")
        wb = openpyxl.load_workbook(io.BytesIO(data), read_only=True, data_only=True)
        rows = [list(r) for r in wb.worksheets[0].iter_rows(values_only=True)]
        return _rows_from_table(rows)
    for enc in ("utf-8-sig", "cp950", "shift_jis", "gb18030"):  # Excel saves CSV in the system code page unless told UTF-8
        try:
            text = data.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    else:
        raise ValueError("讀不懂這個 CSV 的文字編碼，請在 Excel 另存為「CSV UTF-8」。")
    return _rows_from_table(list(csv.reader(io.StringIO(text))))


def find_list(folder: Path) -> Path | None:
    """A label list placed in an imported folder: prefer names that say so (清單, label, 情緒)."""
    cands = [p for p in folder.iterdir() if p.is_file() and p.suffix.lower() in (".xlsx", ".csv")
             and not p.name.startswith("~$")]
    if not cands:
        return None
    cands.sort(key=lambda p: (not any(k in p.name.lower() for k in ("清單", "label", "情緒", "標籤")), p.name))
    return cands[0]


def resolve(filename: str, rows: dict | None, emotion: str | None, language: str | None,
            folders: list[str] | tuple[str, ...] = ()) -> tuple[str | None, str | None, str]:
    """(emotion, language, where the emotion came from: list / filename / folder / form / "") for one file."""
    key = Path(filename).name.lower()
    row = (rows or {}).get(key) or (rows or {}).get(Path(key).stem) or {}
    found = [("list", row), ("filename", from_filename(filename)), ("folder", from_folders(folders)),
             ("form", {"emotion": emotion or None, "language": language or None})]
    e = next(((w, d["emotion"]) for w, d in found if d.get("emotion")), ("", None))
    lang = next((d["language"] for _, d in found if d.get("language")), None)
    return e[1], lang, e[0]

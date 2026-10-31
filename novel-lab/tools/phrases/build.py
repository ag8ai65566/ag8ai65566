"""hololive 常用語 workbook: curated rows (rows/*.txt: type, original, reading, 中文, when, frequency, verification,
sources) plus the research notes, tone tables, sample lines, ASR checks and sources pulled from the character files.

    python novel-lab/tools/phrases/build.py [out.xlsx]

Formulas (counts) are computed when the file is opened in Excel or LibreOffice."""
import json, re, sys
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.table import Table, TableStyleInfo

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
from rows import load_rows  # noqa: E402

from extract import extract  # noqa: E402

ROOT = HERE.parents[1] / "projects" / "holoen"
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "export" / "hololive-常用語.xlsx"
M = {m["file"]: m for m in extract()}

INFO = {  # file → (中文名, 分部・期別, 狀態, 主要直播語言)
    "Mori-Calliope": ("森美聲", "hololive English -Myth-", "在籍", "英文"),
    "Takanashi-Kiara": ("小鳥遊琪亞拉", "hololive English -Myth-", "在籍", "英文（夾德文、日文）"),
    "Ninomae-Inanis": ("一伊那爾栖", "hololive English -Myth-", "在籍", "英文"),
    "Gawr-Gura": ("噶嗚・古拉", "hololive English -Myth-", "已畢業（2025-05-01）", "英文"),
    "Watson-Amelia": ("華生・艾米莉亞", "hololive English -Myth-", "準成員（2024-09-30 結束常規活動）", "英文"),
    "IRyS": ("IRyS", "hololive English -Promise-（原 Project: HOPE）", "在籍", "英文（夾日文）"),
    "Ouro-Kronii": ("歐羅・克洛尼", "hololive English -Promise-", "在籍", "英文"),
    "Ceres-Fauna": ("塞蕾斯・法娜", "hololive English -Promise-", "已畢業（2025-01-03）", "英文"),
    "Nanashi-Mumei": ("七詩無銘", "hololive English -Promise-", "已畢業（2025-04）", "英文"),
    "Hakos-Baelz": ("哈科斯・貝爾絲", "hololive English -Promise-", "在籍", "英文"),
    "Shiori-Novella": ("詩織・諾薇拉", "hololive English -Advent-", "在籍", "英文"),
    "Koseki-Bijou": ("古石碧珠", "hololive English -Advent-", "在籍", "英文"),
    "Nerissa-Ravencroft": ("妮莉莎・瑞文克羅夫特", "hololive English -Advent-", "在籍", "英文"),
    "Fuwawa-Abyssgard": ("弗瓦瓦・阿比斯加德（FUWAMOCO）", "hololive English -Advent-", "在籍", "英文"),
    "Mococo-Abyssgard": ("茉可可・阿比斯加德（FUWAMOCO）", "hololive English -Advent-", "在籍", "英文"),
    "Elizabeth-Rose-Bloodflame": ("伊莉莎白・蘿絲・布拉德法蘭", "hololive English -Justice-", "在籍", "英文（英式）"),
    "Gigi-Murin": ("吉吉・穆林", "hololive English -Justice-", "在籍", "英文"),
    "Cecilia-Immergreen": ("賽西莉亞・伊默格林", "hololive English -Justice-", "在籍", "英文"),
    "Raora-Panthera": ("拉奧拉・潘瑟拉", "hololive English -Justice-", "在籍", "英文（夾義大利文）"),
    "AZKi": ("AZKi", "hololive 0 期生", "在籍", "日文"),
    "Hoshimachi-Suisei": ("星街彗星", "hololive 0 期生", "在籍", "日文"),
    "Houshou-Marine": ("寶鐘瑪琳", "hololive 3 期生", "在籍", "日文"),
    "Shirogane-Noel": ("白銀諾艾爾", "hololive 3 期生", "在籍", "日文"),
    "Nakiri-Ayame": ("百鬼綾目", "hololive 2 期生", "在籍", "日文"),
    "Nekomata-Okayu": ("貓又小粥", "hololive GAMERS", "在籍", "日文"),
    "Shishiro-Botan": ("獅白牡丹", "hololive 5 期生", "在籍", "日文"),
    "Yukihana-Lamy": ("雪花菈米", "hololive 5 期生", "在籍", "日文"),
    "Laplus-Darknesss": ("拉普拉斯・達克尼斯", "秘密結社 holoX（6 期生）", "在籍", "日文"),
    "Takane-Lui": ("鷹嶺琉依", "秘密結社 holoX（6 期生）", "在籍", "日文"),
    "Hakui-Koyori": ("博衣小夜璃", "秘密結社 holoX（6 期生）", "在籍", "日文"),
    "Sakamata-Chloe": ("沙花叉克蘿耶", "秘密結社 holoX（6 期生）", "已畢業（2025-01-26）", "日文"),
    "Kazama-Iroha": ("風真伊呂波", "秘密結社 holoX（6 期生）", "在籍", "日文"),
    "Kikirara-Vivi": ("綺綺羅羅薇薇", "hololive DEV_IS FLOW GLOW", "在籍", "日文（關西腔）"),
}
ORDER = list(INFO)
VER = {"O": "官方資料", "S": "本人社群貼文", "A": "語音辨識（兩個模型一致）", "A1": "語音辨識（只有一個模型）", "C": "直播字幕觀察",
       "W": "Wiki 等次要來源", "T": "只有影片標題"}
TYPE_FIX = {"開場・節目": "開場招呼", "開場・閒聊": "開場閒聊", "其他（未放進卡片）": "其他（未放進角色卡）",
            "粉絲台詞": "粉絲互動", "粉絲回應": "粉絲互動", "組合名": "稱呼・暱稱", "英式用語": "用語特色"}
GREET = ("開場招呼", "自我介紹", "開場閒聊", "結尾道別")

AUDIO = {"ame": "Watson-Amelia", "ayame": "Nakiri-Ayame", "azki": "AZKi", "bae": "Hakos-Baelz",
         "bijou": "Koseki-Bijou", "botan": "Shishiro-Botan", "calli": "Mori-Calliope", "cecilia": "Cecilia-Immergreen",
         "chloe": "Sakamata-Chloe", "elizabeth": "Elizabeth-Rose-Bloodflame", "fauna": "Ceres-Fauna",
         "gigi": "Gigi-Murin", "gura": "Gawr-Gura", "ina": "Ninomae-Inanis", "iroha": "Kazama-Iroha", "irys": "IRyS",
         "kiara": "Takanashi-Kiara", "koyori": "Hakui-Koyori", "kronii": "Ouro-Kronii", "lamy": "Yukihana-Lamy",
         "laplus": "Laplus-Darknesss", "lui": "Takane-Lui", "marine": "Houshou-Marine", "mumei": "Nanashi-Mumei",
         "nerissa": "Nerissa-Ravencroft", "noel": "Shirogane-Noel", "okayu": "Nekomata-Okayu",
         "raora": "Raora-Panthera", "shiori": "Shiori-Novella", "suisei": "Hoshimachi-Suisei", "vivi": "Kikirara-Vivi"}
TRAIT = {"Vocabulary / fillers": "常用詞・語助詞", "Laughs, noises": "笑聲・聲音", "Rhythm & rhetoric": "節奏・修辭",
         "Profanity": "髒話程度", "Code-switching": "語言切換", "Language": "使用語言", "Sounds off": "不像她的說法",
         "Timbre / pitch / pace": "音色・音高・語速"}

FONT = "Arial"
HEAD_FILL = PatternFill("solid", fgColor="1F3A5F")
BAND = PatternFill("solid", fgColor="F3F6FA")
THIN = Side(style="thin", color="D0D7E2")
def name_of(f): return M[f]["name"]

wb = Workbook()

def sheet(title, headers, widths, rows, links=None, table=True, wrap_cols=None):
    ws = wb.create_sheet(title)
    ws.append(headers)
    for r in rows:
        ws.append(r)
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w
    for c in ws[1]:
        c.font = Font(name=FONT, bold=True, color="FFFFFF", size=10)
        c.fill = HEAD_FILL
        c.alignment = Alignment(vertical="center", wrap_text=True)
    ws.row_dimensions[1].height = 30
    for row in ws.iter_rows(min_row=2):
        for c in row:
            c.font = Font(name=FONT, size=10)
            c.alignment = Alignment(vertical="top", wrap_text=True)
            c.border = Border(bottom=THIN)
    for (r, col), url in (links or {}).items():
        cell = ws.cell(row=r, column=col)
        cell.hyperlink = url
        cell.font = Font(name=FONT, size=10, color="1155CC", underline="single")
    ws.freeze_panes = "C2" if len(headers) > 4 else "B2"
    if table and rows:
        ref = f"A1:{get_column_letter(len(headers))}{len(rows) + 1}"
        t = Table(displayName=re.sub(r"\W", "", title.encode("ascii", "ignore").decode()) or f"T{len(wb.sheetnames)}", ref=ref)
        t.displayName = f"T{len(wb.sheetnames)}"
        t.tableStyleInfo = TableStyleInfo(name="TableStyleLight9", showRowStripes=True)
        ws.add_table(t)
    return ws

def first_url(member, srcs):
    for s in srcs:
        info = M[member]["sources"].get(s)
        if info and info["urls"]:
            return info["urls"][0]
    return None

# --- 常用語總表 ---------------------------------------------------------------------------------------------------
rows = load_rows()
rows.sort(key=lambda r: ORDER.index(r["member"]))
main, links = [], {}
for i, r in enumerate(rows, 1):
    t = TYPE_FIX.get(r["type"], r["type"])
    r["type"] = t
    url = first_url(r["member"], r["src"])
    main.append([i, name_of(r["member"]), INFO[r["member"]][0], INFO[r["member"]][1], t, r["orig"], r["reading"], r["zh"],
                 r["when"], r["freq"], VER[r["ver"]], ", ".join(r["src"]), url or ""])
    if url:
        links[(i + 1, 13)] = url
H_MAIN = ["編號", "成員", "中文名", "分部・期別", "類型", "原文", "讀音・官方英譯", "中文意思", "使用時機・說明", "頻率",
          "查證等級", "來源編號", "來源連結"]
W_MAIN = [6, 22, 18, 22, 12, 46, 30, 40, 44, 12, 18, 12, 36]

# --- 開場與結尾 ----------------------------------------------------------------------------------------------------
greet = [m for m in main if m[4] in GREET]
greet_rows, glinks = [], {}
for i, m in enumerate(greet, 1):
    greet_rows.append([i, m[1], m[2], m[4], m[5], m[6], m[7], m[8], m[10], m[11], m[12]])
    if m[12]:
        glinks[(i + 1, 11)] = m[12]
H_GREET = ["編號", "成員", "中文名", "類型", "原文", "讀音・官方英譯", "中文意思", "使用時機・說明", "查證等級", "來源編號", "來源連結"]
W_GREET = [6, 22, 18, 11, 48, 30, 42, 44, 18, 12, 36]

# --- 說話特徵（原文）、情境語氣、範例台詞 -----------------------------------------------------------------------------
traits, tones, samples = [], [], []
for f in ORDER:
    m = M[f]
    for label, subs, own in m["bullets"]:
        base = re.sub(r"\s*\(.*$", "", label).rstrip(":")
        if base.lower().startswith("greetings") or "catchphrase" in base.lower():
            continue
        text = " ".join([own] + [f"• {s}" for s in subs]).strip()
        traits.append([name_of(f), INFO[f][0], TRAIT.get(base, "其他"), label, text])
    for sit, tone, phr in m["tone"]:
        tones.append([name_of(f), INFO[f][0], sit, tone, phr])
    for k, s in enumerate(m["samples"], 1):
        samples.append([name_of(f), INFO[f][0], k, s])

# --- 語音辨識實測 ------------------------------------------------------------------------------------------------
asr, alinks = [], {}
for p in sorted((ROOT / "research" / "audio-check").glob("*.md")):
    if p.stem not in AUDIO and p.stem != "fuwamoco":
        continue
    t = p.read_text(encoding="utf-8")
    for sec in re.split(r"^## ", t, flags=re.M):
        if not sec.startswith("Second"):
            continue
        for ln in sec.split("\n"):
            cells = [c.strip() for c in ln.strip().strip("|").split("|")] if ln.startswith("|") else []
            if len(cells) < 4 or cells[0].startswith(("First", "---")) or set(cells[0]) <= set("-: "):
                continue
            lm = re.search(r"\[([^\]]+)\]\((https?://[^)]+)\)", cells[1])
            if p.stem == "fuwamoco":
                vid = lm.group(2) if lm else ""
                who = "Fuwawa Abyssgard" if "L93K3U4Hrjg" in vid else "Mococo Abyssgard" if "Sxx4UW3XKnc" in vid else "FUWAMOCO（雙人）"
            else:
                who = name_of(AUDIO[p.stem])
            verdict = re.sub(r"\*\*", "", cells[3])
            used = "是" if re.search(r"Shared span|^Agrees|Partial", verdict) else "否"
            asr.append([who, cells[0].strip('"'), lm.group(1) if lm else cells[1], cells[2].strip('"'), verdict, used])
            if lm:
                alinks[(len(asr) + 1, 3)] = lm.group(2)
H_ASR = ["成員", "第一個模型聽到的", "時間點（點開跳到影片）", "第二個模型聽到的（節錄）", "判定（原文）", "可以引用"]

# --- 角色卡原文 --------------------------------------------------------------------------------------------------
cards = [[name_of(f), INFO[f][0], m["other_names"], m["catchphrases_sw"], m["dialogue_style"]] for f in ORDER for m in [M[f]]]

# --- 來源 -----------------------------------------------------------------------------------------------------
srcs, slinks = [], {}
for f in ORDER:
    for sid, info in M[f]["sources"].items():
        srcs.append([name_of(f), sid, info["desc"], info["urls"][0] if info["urls"] else "", M[f]["checked"]])
        if info["urls"]:
            slinks[(len(srcs) + 1, 4)] = info["urls"][0]

# --- 成員總覽（公式） -------------------------------------------------------------------------------------------
def pick(f, types, field=5):
    for m in main:
        if m[1] == name_of(f) and m[4] in types:
            return m[field]
    return ""
def fans(f):
    v = [m[5] for m in main if m[1] == name_of(f) and m[4] == "粉絲稱呼"]
    return " ／ ".join(v)
def selfref(f):
    return " ／ ".join(m[5] for m in main if m[1] == name_of(f) and m[4] == "自稱")
over = []
for i, f in enumerate(ORDER, 2):
    over.append([name_of(f), INFO[f][0], INFO[f][1], INFO[f][2], INFO[f][3], fans(f), selfref(f),
                 pick(f, ("開場招呼", "自我介紹")), pick(f, ("結尾道別",)),
                 f"=COUNTIF('常用語總表'!$B:$B,$A{i})",
                 f"=COUNTIFS('常用語總表'!$B:$B,$A{i},'常用語總表'!$E:$E,\"開場招呼\")+COUNTIFS('常用語總表'!$B:$B,$A{i},'常用語總表'!$E:$E,\"自我介紹\")",
                 f"=COUNTIFS('常用語總表'!$B:$B,$A{i},'常用語總表'!$E:$E,\"結尾道別\")",
                 f"=COUNTIFS('常用語總表'!$B:$B,$A{i},'常用語總表'!$K:$K,\"官方資料\")",
                 f"=COUNTIFS('常用語總表'!$B:$B,$A{i},'常用語總表'!$K:$K,\"語音辨識（兩個模型一致）\")",
                 M[f]["checked"]])
n = len(ORDER) + 1
over.append(["合計", "", "", "", "", "", "", "", ""] + [f"=SUM({c}2:{c}{n})" for c in "JKLMN"] + [""])
H_OVER = ["成員", "中文名", "分部・期別", "狀態（依 2026-10 資料）", "主要直播語言", "粉絲稱呼", "自稱",
          "招牌開場／自我介紹", "招牌結尾", "收錄句數", "開場・介紹句數", "結尾句數", "官方資料句數", "語音辨識確認句數", "資料查核日期"]
W_OVER = [24, 22, 26, 22, 16, 24, 18, 46, 40, 10, 10, 10, 10, 12, 12]

# --- build ---------------------------------------------------------------------------------------------------------
readme = wb.active
readme.title = "說明"
ws_over = sheet("成員總覽", H_OVER, W_OVER, over, table=False)
for c in ws_over[n + 1]:
    c.font = Font(name=FONT, size=10, bold=True)
ws_over.auto_filter.ref = f"A1:O{n}"
sheet("常用語總表", H_MAIN, W_MAIN, main, links)
sheet("開場與結尾", H_GREET, W_GREET, greet_rows, glinks)
sheet("說話特徵（英文原文）", ["成員", "中文名", "項目", "原始標題", "內容（英文研究筆記原文）"], [22, 18, 14, 26, 110], traits)
sheet("各情境語氣（英文原文）", ["成員", "中文名", "情境", "語氣・音高・速度", "代表說法"], [22, 18, 26, 44, 60], tones)
sheet("範例台詞（英文原文）", ["成員", "中文名", "序號", "台詞（含來源註記）"], [22, 18, 6, 110], samples)
sheet("語音辨識實測", H_ASR, [22, 46, 14, 50, 50, 10], asr, alinks)
sheet("角色卡原文", ["成員", "中文名", "其他稱呼（Other Names）", "口頭禪欄（Catchphrases）", "說話風格（Dialogue Style）"],
      [22, 18, 40, 90, 90], cards)
sheet("來源", ["成員", "來源編號", "說明", "連結", "查核日期"], [22, 10, 90, 50, 12], srcs, slinks)

# --- 說明 ---------------------------------------------------------------------------------------------------------
types = sorted({m[4] for m in main}, key=lambda t: (t not in GREET, GREET.index(t) if t in GREET else 0, t))
lines = [
    ("hololive 成員常用語（開場、結尾、口頭禪）", "title"),
    ("整理自 novel-lab 專案 holoen 的角色檔（bible/characters，2026-09-30～10-02 查核）與語音辨識報告（research/audio-check）。", ""),
    ("收錄 33 位成員（Myth、Promise、Advent、Justice 與 14 位日本成員）。", ""),
    ("", ""),
    ("工作表", "h"),
    ("成員總覽：每位成員的分部、狀態、粉絲稱呼、自稱、招牌開場與結尾，以及各類句數（公式自動計算）。", ""),
    ("常用語總表：全部句子，一句一列，附中文意思、使用時機、頻率、查證等級和來源連結。可以用篩選找成員或類型。", ""),
    ("開場與結尾：只列開場招呼、自我介紹、開場閒聊、結尾道別。", ""),
    ("說話特徵／各情境語氣／範例台詞（英文原文）：角色檔裡的研究筆記原文（語助詞、笑聲、節奏、髒話程度、語言切換、音色測量等）。", ""),
    ("語音辨識實測：每一句用兩個語音辨識模型轉寫比對的結果，時間點可以直接點開影片。", ""),
    ("角色卡原文：給 Sudowrite 的口頭禪欄和說話風格欄原文。", ""),
    ("來源：每位成員的來源編號、說明和連結。", ""),
    ("", ""),
    ("查證等級（由強到弱）", "h"),
    ("官方資料：官方簡介、官方訪談、官方商品或成員自己上傳的影片。", ""),
    ("本人社群貼文：成員自己在 X 等社群發的文字。", ""),
    ("語音辨識（兩個模型一致）：直播存檔用兩個不同的語音辨識模型轉寫，兩邊寫出一樣的字才採用。這是機器轉寫，不是人耳聽寫。", ""),
    ("語音辨識（只有一個模型）：只有一個模型聽到，當作研究線索，不當原文引用。", ""),
    ("直播字幕觀察：從直播自動字幕或字幕檔看到的說法。", ""),
    ("Wiki 等次要來源：粉絲 Wiki、剪輯影片說明等二手紀錄，沒有逐句對照原影片。", ""),
    ("只有影片標題：只在剪輯或直播標題看到，用法和確切台詞未證實。", ""),
    ("", ""),
    ("注意", "h"),
    ("中文意思是我們的翻譯；官方有英譯的放在「讀音・官方英譯」欄。頻率是估計，不是統計。", ""),
    ("日本成員的資料比英文成員少（研究時以官方簡介和兩段 2026 年直播抽樣為主）。", ""),
    ("類型「口頭禪（較色）」是粉絲 Wiki 收錄、非露骨的玩笑話；「口頭禪（風格示範）」不是逐字台詞。", ""),
]
r = 1
for text, kind in lines:
    c = readme.cell(row=r, column=1, value=text)
    c.font = Font(name=FONT, size=16 if kind == "title" else 11, bold=kind in ("title", "h"),
                  color="1F3A5F" if kind in ("title", "h") else "000000")
    c.alignment = Alignment(wrap_text=True, vertical="top")
    r += 1
# counts beside the text (columns C–D), computed from the main sheet
def count_table(row, title, labels, col_letter):
    readme.cell(row=row, column=3, value=title).font = Font(name=FONT, size=11, bold=True, color="1F3A5F")
    readme.cell(row=row, column=4, value="句數").font = Font(name=FONT, size=11, bold=True, color="1F3A5F")
    row += 1
    first = row
    for t in labels:
        readme.cell(row=row, column=3, value=t).font = Font(name=FONT, size=10)
        readme.cell(row=row, column=4, value=f"=COUNTIF('常用語總表'!${col_letter}:${col_letter},C{row})").font = Font(name=FONT, size=10)
        row += 1
    readme.cell(row=row, column=3, value="合計").font = Font(name=FONT, size=10, bold=True)
    readme.cell(row=row, column=4, value=f"=SUM(D{first}:D{row - 1})").font = Font(name=FONT, size=10, bold=True)
    return row + 2
nxt = count_table(5, "各查證等級", list(VER.values()), "K")
count_table(nxt, "各類型", types, "E")
readme.column_dimensions["A"].width = 92
readme.column_dimensions["B"].width = 3
readme.column_dimensions["C"].width = 26
readme.column_dimensions["D"].width = 8
wb.save(OUT)
print("rows", len(main), "greet", len(greet_rows), "traits", len(traits), "tones", len(tones), "samples", len(samples),
      "asr", len(asr), "cards", len(cards), "sources", len(srcs))

#!/usr/bin/env python3
"""novel-lab: Claude x GPT 協作的 Sudowrite 設定工作台。

只用 Python 標準庫。子指令：

  new-project <slug> [--title T] [--lang zh-TW]   建立一個小說專案
  brief <slug> <kind> <text...> [--name N]         把一句話的需求變成一次「調查」(run)
  gpt <run-dir> [<run-dir> ...] <stage>            讓 GPT 做某一階段（draft / review / verify / free）；
                                                   多個 run 會打包成一次呼叫（批次）
  split <stage> <reply.md>                         把人工轉貼回來的批次回覆拆回各 run
  promote <run-dir>                                把 final.md 收進專案的 bible/
  export <slug>                                    檢查字數上限並產生 Sudowrite 貼上單
  status [slug]                                    列出專案與每次 run 的進度
  doctor                                           檢查 GPT 連線方式與模型限制
  framework-review                                 請 GPT 審查這個框架本身

GPT 只允許 GPT-6 家族的 Astra / Sol，推理強度只允許 high 以上（見 ALLOWED_*）。
"""

import argparse
import datetime as dt
import json
import os
import re
import shutil
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent          # novel-lab/
FRAMEWORK = ROOT / "framework"
PROJECTS = ROOT / "projects"
FIELDS_FILE = FRAMEWORK / "sudowrite-fields.json"

# 使用者的大前提：只能用 GPT-6、推理強度 high 或以上。這裡是硬性檢查，不是預設值。
ALLOWED_MODEL = re.compile(r"^gpt-6(\.\d+)?-(astra|sol)$")
ALLOWED_EFFORTS = ("high", "xhigh", "max", "ultra")
DEFAULT_MODEL = os.environ.get("NOVEL_LAB_GPT_MODEL", "gpt-6-astra")
FALLBACK_MODEL = "gpt-6.1-sol"
DEFAULT_EFFORT = os.environ.get("NOVEL_LAB_GPT_EFFORT", "xhigh")

KINDS = {
    "character": "角色調查",
    "world": "世界觀元素",
    "idea": "創意／故事核心",
    "research": "現實考據",
    "check": "一致性檢查",
}

STAGES = {
    "draft": "gpt-draft.md",       # 盲寫：GPT 只看 brief 與既有 bible，不看 Claude 的稿
    "review": "gpt-review.md",     # GPT 審 Claude 的初稿
    "verify": "gpt-verify.md",     # GPT 審合併後的 final.md，給 APPROVE / CHANGES
    "free": "gpt-free.md",         # 自由提問（prompt 放在 run 目錄的 to-gpt.free.md）
}


def die(msg, code=1):
    print(f"✗ {msg}", file=sys.stderr)
    sys.exit(code)


def slugify(text):
    text = re.sub(r"[\s/\\:*?\"<>|]+", "-", text.strip())
    return text.strip("-")[:40] or "untitled"


def read(path):
    return Path(path).read_text(encoding="utf-8")


def write(path, text):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def project_dir(slug):
    d = PROJECTS / slug
    if not d.is_dir():
        die(f"找不到專案 {slug}（先跑 new-project）")
    return d


# ---------------------------------------------------------------- 專案與 run

def cmd_new_project(args):
    d = PROJECTS / args.slug
    if d.exists():
        die(f"{d} 已存在")
    tpl = read(FRAMEWORK / "templates" / "project.md")
    write(d / "project.md", tpl.replace("{{title}}", args.title or args.slug)
          .replace("{{lang}}", args.lang))
    for sub in ("bible/characters", "bible/world", "bible/story", "runs", "export"):
        (d / sub).mkdir(parents=True, exist_ok=True)
    print(f"✓ 建立 {d.relative_to(ROOT.parent)}，請先填 project.md")


def cmd_brief(args):
    if args.kind not in KINDS:
        die(f"kind 必須是 {', '.join(KINDS)}")
    d = project_dir(args.slug)
    text = " ".join(args.text).strip()
    name = args.name or text.split("，")[0].split(",")[0][:20]
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M")
    run = d / "runs" / f"{stamp}-{args.kind}-{slugify(name)}"
    if run.exists():
        die(f"{run} 已存在")
    tpl = read(FRAMEWORK / "templates" / f"brief-{args.kind}.md")
    write(run / "brief.md", tpl.replace("{{name}}", name).replace("{{input}}", text))
    print(run.relative_to(ROOT.parent))


def bible_context(proj, limit_chars=24000):
    """把 project.md 和既有 bible 串成上下文，讓兩個模型對同一份設定工作。"""
    parts = [f"# project.md\n\n{read(proj / 'project.md')}"]
    for f in sorted((proj / "bible").rglob("*.md")):
        parts.append(f"# bible/{f.relative_to(proj / 'bible')}\n\n{read(f)}")
    ctx = "\n\n---\n\n".join(parts)
    if len(ctx) > limit_chars:
        ctx = ctx[:limit_chars] + "\n\n…（bible 過長已截斷；需要時請到檔案裡查）"
    return ctx


def build_prompt(run, stage):
    proj = run.parent.parent
    kind = run.name.split("-")[2]
    fill = {
        "{{context}}": bible_context(proj),
        "{{brief}}": read(run / "brief.md"),
        "{{schema}}": read(FRAMEWORK / "templates" / f"dossier-{kind}.md"),
        "{{rubric}}": read(FRAMEWORK / "prompts" / "rubric.md"),
        "{{rules}}": read(FRAMEWORK / "prompts" / "shared-rules.md"),
    }
    if stage == "review":
        fill["{{target}}"] = read(run / "claude-draft.md")
        own = run / "gpt-draft.md"
        fill["{{own}}"] = read(own) if own.exists() else "（你這次沒有寫初稿）"
    if stage == "verify":
        fill["{{target}}"] = read(run / "final.md")
        reviews = [f"## {n}\n\n{read(run / n)}" for n in ("claude-review.md", "gpt-review.md")
                   if (run / n).exists()]
        fill["{{reviews}}"] = "\n\n".join(reviews) or "（無）"
    if stage == "free":
        return read(run / "to-gpt.free.md")
    prompt = read(FRAMEWORK / "prompts" / f"gpt-{stage}.md")
    for k, v in fill.items():
        prompt = prompt.replace(k, v)
    return prompt


# ---------------------------------------------------------------- GPT 橋接

def check_model(model, effort):
    if not ALLOWED_MODEL.match(model):
        die(f"模型 {model} 不在允許範圍（只允許 GPT-6 Astra / Sol）")
    if effort not in ALLOWED_EFFORTS:
        die(f"推理強度 {effort} 不允許（只允許 {'/'.join(ALLOWED_EFFORTS)}）")


def codex_ready():
    if not shutil.which("codex"):
        return False
    st = subprocess.run(["codex", "login", "status"], capture_output=True, text=True)
    if st.returncode == 0 and "not logged in" not in (st.stdout + st.stderr).lower():
        return True
    for env, flag in (("OPENAI_API_KEY", "--with-api-key"), ("CODEX_ACCESS_TOKEN", "--with-access-token")):
        if os.environ.get(env):
            r = subprocess.run(["codex", "login", flag], input=os.environ[env],
                               capture_output=True, text=True)
            if r.returncode == 0:
                return True
    return False


def via_codex(prompt, out, model, effort, live_search=False):
    cmd = ["codex", "exec", "-m", model, "-c", f'model_reasoning_effort="{effort}"',
           "-c", f'web_search="{"live" if live_search else "cached"}"',
           "-s", "read-only", "--skip-git-repo-check", "--ephemeral",
           "-C", str(ROOT), "-o", str(out), "-"]
    r = subprocess.run(cmd, input=prompt, capture_output=True, text=True)
    if r.returncode != 0 or not out.exists() or not out.read_text(encoding="utf-8").strip():
        tail = (r.stderr or r.stdout)[-1500:]
        raise RuntimeError(f"codex exec 失敗（{model}/{effort}）：\n{tail}")


def via_api(prompt, out, model, effort, live_search=False):
    payload = {"model": model, "reasoning": {"effort": effort}, "input": prompt}
    if live_search:
        payload["tools"] = [{"type": "web_search"}]
    body = json.dumps(payload).encode()
    req = urllib.request.Request(
        "https://api.openai.com/v1/responses", data=body,
        headers={"Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}",
                 "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=900) as resp:
            data = json.load(resp)
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"OpenAI API {e.code}（{model}/{effort}）：{e.read()[:800]!r}")
    texts = [c["text"] for item in data.get("output", []) if item.get("type") == "message"
             for c in item.get("content", []) if c.get("type") == "output_text"]
    if not texts:
        raise RuntimeError(f"OpenAI API 沒有回傳文字：{json.dumps(data)[:800]}")
    served = data.get("model", model)
    if not served.startswith("gpt-6"):
        raise RuntimeError(f"OpenAI 實際回應的模型是 {served}，不是 GPT-6，結果不採用")
    write(out, "\n".join(texts))
    return served


def ask_gpt(prompt, out, model, effort, live_search=False):
    """回傳實際用的 (via, model)。沒有任何連線方式時改成人工轉貼模式（exit 3）。"""
    check_model(model, effort)
    tries = [model] + ([FALLBACK_MODEL] if model != FALLBACK_MODEL else [])
    errors = []
    use_codex = codex_ready()
    for m in tries:
        try:
            if use_codex:
                via_codex(prompt, out, m, effort, live_search)
                return "codex", m
            if os.environ.get("OPENAI_API_KEY"):
                return "api", via_api(prompt, out, m, effort, live_search)
        except RuntimeError as e:
            errors.append(str(e))
            continue
        break
    if errors:
        die("GPT 呼叫全部失敗，沒有降級到 GPT-6 以外的模型：\n\n" + "\n\n".join(errors))
    manual = out.with_suffix(".to-gpt.md")
    write(manual, prompt)
    print(f"⚠ 這個環境沒有 GPT 連線。已把完整提示寫到 {manual.relative_to(ROOT.parent)}\n"
          f"  請貼到 ChatGPT / Codex（模型 {model}，推理 {effort}），把回覆存成 "
          f"{out.relative_to(ROOT.parent)} 或直接貼回給 Claude。", file=sys.stderr)
    sys.exit(3)


def prepare_run(run, stage):
    """檢查 run 目錄並把上一輪的輸出改名保留，回傳 (輸出路徑, 提示)。"""
    if not (run / "brief.md").exists():
        die(f"{run} 不是 run 目錄（缺 brief.md）")
    if stage == "review" and not (run / "claude-draft.md").exists():
        die(f"{run.name}：review 需要先有 claude-draft.md")
    if stage == "verify" and not (run / "final.md").exists():
        die(f"{run.name}：verify 需要先有 final.md")
    out = run / STAGES[stage]
    prompt = build_prompt(run, stage)
    if out.exists():  # 例如 CHANGES 之後重新驗收：保留上一輪，不覆蓋
        n = 1
        while (old := out.with_name(f"{out.stem}.{n}.md")).exists():
            n += 1
        out.rename(old)
    return out, prompt


def log_gpt(run, stage, via, model, effort):
    with (run / "gpt-log.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps({"stage": stage, "via": via, "model": model, "effort": effort,
                            "at": dt.datetime.now().isoformat(timespec="seconds")},
                           ensure_ascii=False) + "\n")


BATCH_OPEN = "<<<RUN: {name}>>>"
BATCH_CLOSE = "<<<END RUN>>>"


def batch_prompt(items):
    head = (f"# 批次任務：以下有 {len(items)} 個互相獨立的任務\n\n"
            "請依序完成每一個。每個任務的完整輸出前後要加上標記，標記要單獨一行、逐字照抄：\n\n"
            + "\n".join(f"- 任務 {i + 1}：開頭 `{BATCH_OPEN.format(name=run.name)}`，結尾 `{BATCH_CLOSE}`"
                        for i, (run, _, _) in enumerate(items))
            + "\n\n標記之外不要寫任何東西。每個任務都要完整輸出，不要因為篇幅而省略或合併。\n")
    body = "\n\n".join(f"{'=' * 20} 任務 {i + 1}：{run.name} {'=' * 20}\n\n{prompt}"
                       for i, (run, _, prompt) in enumerate(items))
    return head + "\n\n" + body


def split_batch(text, items):
    """把批次回覆依標記拆回各 run；缺任何一段就整批不寫入。"""
    parts = {}
    for run, out, _ in items:
        m = re.search(re.escape(BATCH_OPEN.format(name=run.name)) + r"\s*\n(.*?)\n\s*" + re.escape(BATCH_CLOSE),
                      text, re.S)
        if not m or not m.group(1).strip():
            die(f"批次回覆裡找不到 {run.name} 的段落（標記 {BATCH_OPEN.format(name=run.name)}）")
        parts[out] = m.group(1).strip() + "\n"
    for out, body in parts.items():
        write(out, body)


def cmd_gpt(args):
    *names, stage = args.items
    if stage not in STAGES:
        die(f"用法：gpt <run> [<run> ...] <stage>；stage 必須是 {', '.join(STAGES)}")
    if not names:
        die("至少要一個 run 目錄")
    check_model(args.model, args.effort)
    runs = [Path(n).resolve() for n in names]
    live = any(r.name.split("-")[2] == "research" for r in runs)
    if len(runs) == 1:
        out, prompt = prepare_run(runs[0], stage)
        via, model = ask_gpt(prompt, out, args.model, args.effort, live_search=live)
        log_gpt(runs[0], stage, via, model, args.effort)
        print(f"✓ {out.relative_to(ROOT.parent)}（{via} · {model} · {args.effort}）")
        return
    if len({r.parent for r in runs}) != 1:
        die("批次的 run 必須屬於同一個專案")
    items = [(r, *prepare_run(r, stage)) for r in runs]
    raw = runs[0].parent / f"_batch-{dt.datetime.now():%Y%m%d-%H%M}-{stage}.md"
    via, model = ask_gpt(batch_prompt(items), raw, args.model, args.effort, live_search=live)
    split_batch(read(raw), items)
    for run, out, _ in items:
        log_gpt(run, stage, via, model, args.effort)
        print(f"✓ {out.relative_to(ROOT.parent)}（{via} · {model} · {args.effort}）")


def cmd_split(args):
    """人工轉貼的批次回覆：把貼回來的整份回覆拆回各 run。"""
    reply = Path(args.reply).resolve()
    text = read(reply)
    names = re.findall(r"<<<RUN: (.+?)>>>", text)
    if not names:
        die("回覆裡沒有任何 <<<RUN: …>>> 標記")
    runs_dir = reply.parent if reply.parent.name == "runs" else None
    items = []
    for name in dict.fromkeys(names):
        run = (runs_dir / name) if runs_dir else next(PROJECTS.glob(f"*/runs/{name}"), None)
        if not run or not run.is_dir():
            die(f"找不到 run 目錄 {name}")
        items.append((run, run / STAGES[args.stage], ""))
    split_batch(text, items)
    for run, out, _ in items:
        log_gpt(run, args.stage, "manual", "（使用者轉貼）", "（使用者轉貼）")
        print(f"✓ {out.relative_to(ROOT.parent)}")


REVIEW_FILES = ["README.md", "framework/prompts/shared-rules.md", "framework/prompts/rubric.md",
                "framework/templates/dossier-character.md", "framework/templates/dossier-world.md",
                "framework/templates/dossier-idea.md", "framework/sudowrite-fields.json",
                "docs/sudowrite-2026-09.md"]


def cmd_framework_review(args):
    """框架本身也要和 GPT 商擬：把關鍵檔案打包成一份自足的提示送給 GPT。"""
    check_model(args.model, args.effort)
    files = "\n\n".join(f"## `{name}`\n\n````\n{read(ROOT / name)}\n````" for name in REVIEW_FILES)
    prompt = read(FRAMEWORK / "prompts" / "gpt-framework-review.md").replace("{{files}}", files)
    out = ROOT / "docs" / "reviews" / f"gpt-framework-review-{dt.datetime.now():%Y%m%d-%H%M}.md"
    via, model = ask_gpt(prompt, out, args.model, args.effort)
    print(f"✓ {out.relative_to(ROOT.parent)}（{via} · {model} · {args.effort}）")


def cmd_doctor(_args):
    print(f"預設模型 {DEFAULT_MODEL} · 推理 {DEFAULT_EFFORT} · 備援 {FALLBACK_MODEL}")
    check_model(DEFAULT_MODEL, DEFAULT_EFFORT)
    print(f"codex CLI：{shutil.which('codex') or '未安裝（npm i -g @openai/codex）'}")
    for env in ("OPENAI_API_KEY", "CODEX_ACCESS_TOKEN"):
        print(f"{env}：{'有' if os.environ.get(env) else '沒有'}")
    if codex_ready():
        print("→ 會透過 Codex CLI 呼叫 GPT")
    elif os.environ.get("OPENAI_API_KEY"):
        print("→ 會直接呼叫 OpenAI Responses API")
    else:
        print("→ 沒有連線方式：gpt 指令會改成產生 to-gpt.md 讓你手動轉貼")


# ---------------------------------------------------------------- 收錄與匯出

SW_SECTION = re.compile(r"^## \[SW\] (.+?)\s*$", re.M)
EMPTY = {"（無）", "(無)", "（none）", "(none)", "無", "none", "N/A", "（交給 Sudowrite 生成）"}
CJK = re.compile(r"[぀-ヿ㐀-鿿가-힯豈-﫿]")
SECTION_DIR = {"Characters": "characters", "Worldbuilding": "world", "Story": "story"}


def sw_fields(text):
    """抓出 `## [SW] 欄位名` 的段落 → {欄位名: 內容}；「（無）」視為空白。"""
    marks = list(SW_SECTION.finditer(text))
    out = {}
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        body = re.split(r"^## (?!\[SW\])", text[m.end():end], maxsplit=1, flags=re.M)[0]
        body = re.sub(r"(\n\s*-{3,}\s*)+$", "", body.rstrip()).strip()
        out[m.group(1)] = "" if body in EMPTY else body
    return out


def count_words(text):
    """Sudowrite 以 word 計上限。中日韓字元每字算 1，其餘按英文單字算。"""
    latin = re.findall(r"[A-Za-z0-9]+(?:['’-][A-Za-z0-9]+)*", CJK.sub(" ", text))
    return len(CJK.findall(text)) + len(latin)


def front_matter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    meta = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip().strip('"')
    return meta


def verdict(run):
    """gpt-verify.md 第一個非空行：APPROVE / CHANGES / None。"""
    f = run / "gpt-verify.md"
    if not f.exists():
        return None
    first = next((l.strip().strip("*#` ") for l in read(f).splitlines() if l.strip()), "")
    return "APPROVE" if first.upper().startswith("APPROVE") else "CHANGES"


def cmd_promote(args):
    run = Path(args.run).resolve()
    final = run / "final.md"
    if not final.exists():
        die("沒有 final.md")
    if verdict(run) != "APPROVE" and not args.force:
        die("GPT 還沒 APPROVE（gpt-verify.md 第一行）。確定要收錄請加 --force")
    text = read(final)
    meta = front_matter(text)
    sub = SECTION_DIR.get(meta.get("sw_section", ""))
    if not sub:
        die("final.md 的 front matter 沒有 sw_section（Characters / Worldbuilding / Story）；check 類不用收錄")
    dest = run.parent.parent / "bible" / sub / f"{slugify(meta.get('name') or run.name)}.md"
    write(dest, text)
    print(f"✓ 收錄到 {dest.relative_to(ROOT.parent)}")


def write_csv(path, base_cols, rows):
    """照 Sudowrite 匯入模板的欄位順序寫 CSV；自訂特質接在後面。"""
    import csv
    cols = list(base_cols)
    for r in rows:
        cols += [k for k in r if k not in cols]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for r in rows:
            w.writerow([r.get(c, "") for c in cols])


def cmd_export(args):
    proj = project_dir(args.slug)
    spec = json.loads(read(FIELDS_FILE))
    hard_w, hard_c, soft_w = spec["hard_limits_words"], spec["hard_limits_chars"], spec["soft_limits_words"]
    hidden = set(spec["hide_in_sudowrite"])
    cards = {"Story": [], "Characters": [], "Worldbuilding": []}
    for f in sorted((proj / "bible").rglob("*.md")):
        text = read(f)
        fields = sw_fields(text)
        if fields:
            meta = front_matter(text)
            section = meta.get("sw_section") or {v: k for k, v in SECTION_DIR.items()}.get(f.parent.name, "Story")
            cards.setdefault(section, []).append((f, meta, fields))

    errors, warnings = [], []
    lines = [f"# Sudowrite 貼上單 — {args.slug}",
             f"_產生時間 {dt.datetime.now():%Y-%m-%d %H:%M}。字數：中日韓字元每字算 1、英文每字算 1。"
             f"⛔ = 超過 Sudowrite 官方上限；⚠ = 超過本框架建議長度。_", ""]
    guide = {
        "Story": "貼到 Story Bible 對應的欄位（Braindump、Genre、Style、Synopsis）。",
        "Characters": ("用 CSV 匯入：Story Bible 的 Characters 標題旁 ••• → Import → CSV。"
                       "`characters.csv` 是全部角色；只想加一個新角色就用 `cards/` 裡那一個的 CSV。"
                       "Sudowrite 沒說重複匯入會不會合併，**更新既有角色時請逐欄貼上**，不要再匯入一次。"),
        "Worldbuilding": ("用 CSV 匯入：Story Bible 的 Worldbuilding 標題旁 ••• → Import → CSV。"
                          "`worldbuilding.csv` 是全部元素；單一元素在 `cards/`。更新既有元素請逐欄貼上。"),
    }
    for section in ("Story", "Characters", "Worldbuilding"):
        if not cards.get(section):
            continue
        lines += [f"# {section}", guide[section], ""]
        for f, meta, fields in cards[section]:
            label = f"{f.relative_to(proj / 'bible')}"
            lines.append(f"## {meta.get('name', f.stem)}")
            lines.append(f"_來源：bible/{label}_\n")
            for name, body in fields.items():
                if not body:
                    continue
                n = count_words(body)
                flag = ""
                if name in hard_w and n > hard_w[name]:
                    flag = f" ⛔ 超過官方上限 {hard_w[name]}"
                    errors.append(f"{label} · {name}：{n}/{hard_w[name]}")
                elif name in hard_c and len(body) > hard_c[name]:
                    flag = f" ⛔ 超過官方上限 {hard_c[name]} 字元"
                    errors.append(f"{label} · {name}：{len(body)}/{hard_c[name]} 字元")
                elif name in soft_w and n > soft_w[name]:
                    flag = f" ⚠ 超過建議 {soft_w[name]}"
                    warnings.append(f"{label} · {name}：{n}/{soft_w[name]}")
                cap = hard_w.get(name) or soft_w.get(name)
                hide = "（匯入後請按眼睛圖示隱藏）" if name in hidden else ""
                lines.append(f"### {name}（{n}{'/' + str(cap) if cap else ''}）{flag}{hide}")
                lines.append("```text\n" + body + "\n```\n")

    exp = proj / "export"
    write(exp / "sudowrite-paste.md", "\n".join(lines))
    made = ["sudowrite-paste.md"]
    for section, fname, key in (("Characters", "characters.csv", "character_columns"),
                                ("Worldbuilding", "worldbuilding.csv", "worldbuilding_columns")):
        entries = cards.get(section, [])
        if entries:
            write_csv(exp / fname, spec[key], [fields for _, _, fields in entries])
            for f, _, fields in entries:
                write_csv(exp / "cards" / f"{section.lower()}-{f.stem}.csv", spec[key], [fields])
            made.append(f"{fname}（{len(entries)} 張，另有單張 CSV 在 cards/）")
    print(f"✓ {exp.relative_to(ROOT.parent)}/ → {', '.join(made)}")
    if warnings:
        print("⚠ 超過建議長度（可以匯入，但 Sudowrite 上下文不夠時會先被擠掉）：\n  " + "\n  ".join(warnings))
    if errors:
        print("⛔ 超過 Sudowrite 官方上限，必須縮短：\n  " + "\n  ".join(errors))
        sys.exit(2)


def run_state(run):
    steps = [("brief.md", "brief"), ("claude-draft.md", "C稿"), ("gpt-draft.md", "G稿"),
             ("claude-review.md", "C審"), ("gpt-review.md", "G審"), ("final.md", "合併"),
             ("gpt-verify.md", "G驗")]
    marks = " ".join(("●" if (run / f).exists() else "○") + label for f, label in steps)
    v = verdict(run)
    return marks + {"APPROVE": " ✅APPROVE", "CHANGES": " ↺CHANGES", None: ""}[v]


def cmd_status(args):
    projects = [project_dir(args.slug)] if args.slug else sorted(p for p in PROJECTS.iterdir() if p.is_dir())
    if not projects:
        print("還沒有專案。python3 novel-lab/tools/lab.py new-project <slug>")
    for proj in projects:
        n = len(list((proj / "bible").rglob("*.md")))
        print(f"\n■ {proj.name}（bible {n} 份）")
        for run in sorted(r for r in (proj / "runs").iterdir() if r.is_dir()):
            print(f"  {run.name}\n    {run_state(run)}")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("new-project"); s.add_argument("slug")
    s.add_argument("--title"); s.add_argument("--lang", default="zh-TW")
    s.set_defaults(fn=cmd_new_project)

    s = sub.add_parser("brief"); s.add_argument("slug"); s.add_argument("kind")
    s.add_argument("text", nargs="+"); s.add_argument("--name")
    s.set_defaults(fn=cmd_brief)

    s = sub.add_parser("gpt"); s.add_argument("items", nargs="+", metavar="<run> [<run> ...] <stage>")
    s.add_argument("--model", default=DEFAULT_MODEL); s.add_argument("--effort", default=DEFAULT_EFFORT)
    s.set_defaults(fn=cmd_gpt)

    s = sub.add_parser("split"); s.add_argument("stage"); s.add_argument("reply")
    s.set_defaults(fn=cmd_split)

    s = sub.add_parser("promote"); s.add_argument("run"); s.add_argument("--force", action="store_true")
    s.set_defaults(fn=cmd_promote)

    s = sub.add_parser("export"); s.add_argument("slug"); s.set_defaults(fn=cmd_export)
    s = sub.add_parser("status"); s.add_argument("slug", nargs="?"); s.set_defaults(fn=cmd_status)
    s = sub.add_parser("doctor"); s.set_defaults(fn=cmd_doctor)
    s = sub.add_parser("framework-review")
    s.add_argument("--model", default=DEFAULT_MODEL); s.add_argument("--effort", default=DEFAULT_EFFORT)
    s.set_defaults(fn=cmd_framework_review)

    args = p.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()

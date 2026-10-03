#!/usr/bin/env python3
"""novel-lab: Claude x GPT 協作的 Sudowrite 設定工作台。

只用 Python 標準庫。子指令：

  new-project <slug> [--title T] [--lang zh-TW]   建立一個小說專案
  brief <slug> <kind> <text...> [--name N]         把一句話的需求變成一次「調查」(run)
  gpt <run-dir> [<run-dir> ...] <stage>            讓 GPT 做某一階段（draft / review / verify / free）；
                                                   多個 run 會打包成一次呼叫（批次）
  split <stage> <reply.md>                         把人工轉貼回來的批次回覆拆回各 run
  pack <run-dir> [...]                             產生本次任務的固定資料包 context.md（兩邊盲稿共用）
  promote <run-dir>                                把 final.md 收進專案的 bible/
  export <slug>                                    檢查字數上限並產生 Sudowrite 貼上單
  status [slug]                                    列出專案與每次 run 的進度
  doctor                                           檢查 GPT 連線方式與模型限制
  framework-review                                 請 GPT 審查這個框架本身

GPT 只允許 GPT-6 家族的 Astra / Sol，推理強度只允許 high 以上（見 ALLOWED_*）。
"""

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import shlex
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
# 作者定案（2026-10-01，取代 2026-09-30 的「審稿 high」）：提高 GPT 審查力度與準確性，所有階段一律 xhigh
STAGE_EFFORT = {"draft": "xhigh", "free": "xhigh", "review": "xhigh", "verify": "xhigh", "framework": "xhigh"}
# GPT 額度用完時寫這個檔（不進 git）：重置時間＋待重跑的指令，讓 Claude 排程在重置後回來
QUOTA_FILE = ROOT / ".gpt-quota.json"
QUOTA_EXIT = 75  # EX_TEMPFAIL：額度用完，稍後重跑即可
EFFORT_OVERRIDE = os.environ.get("NOVEL_LAB_GPT_EFFORT")  # 設了就全部階段都用它
DEFAULT_EFFORT = EFFORT_OVERRIDE or STAGE_EFFORT["draft"]


def effort_for(stage, explicit=None):
    return explicit or EFFORT_OVERRIDE or STAGE_EFFORT[stage]

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
    text = re.sub(r"['’`]", "", text.strip())  # 撇號在 shell 裡很麻煩（Ina'nis → Inanis）
    text = re.sub(r"(?<=\w)\+", "plus", text)  # La+ Darknesss → Laplus-Darknesss（檔名不放「+」）
    text = re.sub(r"[\s/\\:*?\"<>|]+", "-", text)
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


CONTEXT_BUDGET = 60000  # 字元；超過時整份檔案不附上並列出，不會切掉半張卡


def sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


def context_pack(run):
    """本次任務的固定資料包。第一次使用時產生並存成 <run>/context.md，之後每個階段、
    GPT 和 Claude 都讀同一份，確保兩份盲稿根據相同的設定。"""
    f = run / "context.md"
    if f.exists():
        return read(f)
    proj = run.parent.parent
    brief = read(run / "brief.md")
    bible = sorted((proj / "bible").rglob("*.md"))

    def related(p):
        name = front_matter(read(p)).get("name") or p.stem
        return bool(name) and name in brief

    files = [proj / "project.md"] + [p for p in bible if related(p)] + [p for p in bible if not related(p)]
    parts, listed, omitted, used = [], [], [], 0
    for i, p in enumerate(files):
        text, rel = read(p), p.relative_to(proj)
        block = f"# {rel}（sha256 {sha(text)}）\n\n{text}"
        if i and used + len(block) > CONTEXT_BUDGET:
            omitted.append(f"- {rel}")
            continue
        parts.append(block)
        listed.append(f"- {rel}（sha256 {sha(text)}）")
        used += len(block)
    head = "## 本資料包包含的檔案\n" + "\n".join(listed)
    if omitted:
        head += "\n\n## 因篇幅沒有附上的檔案（需要時在「待確認」提出）\n" + "\n".join(omitted)
    pack = head + "\n\n---\n\n" + "\n\n---\n\n".join(parts)
    write(f, pack)
    return pack


def frozen(run, name, source):
    """本次任務的輸入在第一次使用時複製到 <run>/frozen/，之後各階段都讀這份，
    模板或規則中途改版也不會讓同一個任務前後收到不同的依據。"""
    f = run / "frozen" / name
    if not f.exists():
        if source is None:  # free-stage runs built by a tool (QA, voice, research) freeze the shared prompt on first use
            source = FRAMEWORK / "prompts" / name
        write(f, source() if callable(source) else read(source))
    return read(f)


def freeze_all(run):
    """一次凍結本任務的全部輸入（資料包、brief、模板、欄位上限、規則、評分表、各階段提示、
    給 GPT 的專案說明），確保兩份盲稿與之後每個階段都根據同一個版本。"""
    kind = run.name.split("-")[2]
    context_pack(run)
    frozen(run, "brief.md", run / "brief.md")
    frozen(run, f"dossier-{kind}.md", FRAMEWORK / "templates" / f"dossier-{kind}.md")
    frozen(run, "sudowrite-fields.md", lambda: ("## Sudowrite 欄位上限與必填（sudowrite-fields.json）\n\n```json\n"
                                                + read(FIELDS_FILE) + "\n```\n"))
    for name in ("rubric.md", "shared-rules.md", "gpt-brief.md", "gpt-draft.md", "gpt-review.md", "gpt-verify.md"):
        frozen(run, name, FRAMEWORK / "prompts" / name)


def build_prompt(run, stage):
    kind = run.name.split("-")[2]
    freeze_all(run)
    fill = {
        "{{context}}": context_pack(run),
        "{{brief}}": frozen(run, "brief.md", None),
        "{{schema}}": frozen(run, f"dossier-{kind}.md", None),
        "{{limits}}": frozen(run, "sudowrite-fields.md", None),
        "{{rubric}}": frozen(run, "rubric.md", None),
        "{{rules}}": frozen(run, "shared-rules.md", None),
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
    prompt = frozen(run, f"gpt-{stage}.md", None)
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


def snapshot_copy():
    """GPT 讀的是開跑當下工作目錄的副本（不含 runs/、不含 git）：Claude 之後再改檔不會影響這一輪，
    內嵌在提示裡的 packet 也和 GPT 能打開的檔案一致。"""
    if os.environ.get("NOVEL_LAB_SNAPSHOT") == "0":
        return None, ROOT
    import tempfile
    tmp = Path(tempfile.mkdtemp(prefix="novel-lab-snap-"))
    skip = {".git", "runs", "models", "__pycache__", ".gpt-quota.json"}
    shutil.copytree(ROOT, tmp / ROOT.name, ignore=lambda d, names: [n for n in names if n in skip])
    return tmp, tmp / ROOT.name


def via_codex(prompt, out, model, effort, live_search=False):
    snap, cwd = snapshot_copy()
    cmd = ["codex", "exec", "--json", "-m", model, "-c", f'model_reasoning_effort="{effort}"',
           "-c", f'web_search="{"live" if live_search else "cached"}"',
           "-s", "read-only", "--skip-git-repo-check", "--ephemeral",
           "-C", str(cwd), "-o", str(out), "-"]
    try:
        r = subprocess.run(cmd, input=prompt, capture_output=True, text=True)
    finally:
        if snap:
            shutil.rmtree(snap, ignore_errors=True)
    # 事件記錄（工具呼叫、token 用量），失敗時也留下，方便調整每次任務的大小
    out.with_name(out.stem + ".events.jsonl").write_text(r.stdout, encoding="utf-8")
    if r.returncode != 0 or not out.exists() or not out.read_text(encoding="utf-8").strip():
        errors = []
        for line in r.stdout.splitlines():
            try:
                ev = json.loads(line)
            except ValueError:
                continue
            if not isinstance(ev, dict):
                continue
            err = ev.get("error")
            msg = ev.get("message") or (err.get("message") if isinstance(err, dict) else err)
            if msg and ("error" in str(ev.get("type", "")) or "failed" in str(ev.get("type", ""))):
                errors.append(str(msg))
        tail = ((r.stderr or "")[-1200:] + ("\n" + "\n".join(errors[-2:]) if errors else "")).strip()
        raise RuntimeError(f"codex exec 失敗（{model}/{effort}）：\n{tail[-1500:]}")


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


def quota_reset_time(err):
    """從 codex 的「try again at 4:13 PM.」或「try again at Oct 1st, 2026 2:22 AM.」算出重置時間（UTC）。"""
    m = re.search(r"try again at (.+?)\.?\s*$", err.strip().splitlines()[-1] if err.strip() else "")
    if not m:
        m = re.search(r"try again at ([^\n]+?)\.(?:\s|$)", err)
    if not m:
        return None
    raw = re.sub(r"(\d)(st|nd|rd|th),", r"\1,", m.group(1).strip())
    now = dt.datetime.now().astimezone()
    for fmt in ("%b %d, %Y %I:%M %p", "%I:%M %p"):
        try:
            t = dt.datetime.strptime(raw, fmt)
        except ValueError:
            continue
        if fmt == "%I:%M %p":
            t = now.replace(hour=t.hour, minute=t.minute, second=0, microsecond=0)
            if t < now:
                t += dt.timedelta(days=1)
        else:
            t = t.replace(tzinfo=now.tzinfo)
        return t.astimezone(dt.timezone.utc)
    return None


def record_quota(err):
    """額度用完：記下重置時間與這次的指令（累加，不重複），然後以 QUOTA_EXIT 結束。"""
    reset = quota_reset_time(err)
    data = json.loads(read(QUOTA_FILE)) if QUOTA_FILE.exists() else {"pending": []}
    cmd = "python3 novel-lab/tools/lab.py " + " ".join(shlex.quote(a) for a in sys.argv[1:])
    if cmd not in data["pending"]:
        data["pending"].append(cmd)
    data["reset_utc"] = reset.isoformat(timespec="minutes") if reset else None
    data["noted_at"] = dt.datetime.now(dt.timezone.utc).isoformat(timespec="minutes")
    write(QUOTA_FILE, json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print(f"⏸ GPT 額度用完；重置時間 {data['reset_utc'] or '未知（看下面的訊息）'}。"
          f"待重跑的指令記在 {QUOTA_FILE.relative_to(ROOT.parent)}。\n"
          f"GPT_QUOTA_RESET_UTC={data['reset_utc'] or ''}\n\n{err[-600:]}", file=sys.stderr)
    sys.exit(QUOTA_EXIT)


def clear_pending():
    """這次指令成功了：從待重跑清單移除；清單空了就刪檔。"""
    if not QUOTA_FILE.exists():
        return
    data = json.loads(read(QUOTA_FILE))
    cmd = "python3 novel-lab/tools/lab.py " + " ".join(shlex.quote(a) for a in sys.argv[1:])
    data["pending"] = [c for c in data["pending"] if c != cmd]
    if data["pending"]:
        write(QUOTA_FILE, json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    else:
        QUOTA_FILE.unlink()


def ask_gpt(prompt, out, model, effort, live_search=False, brief=None):
    """回傳實際用的 (via, model)。沒有任何連線方式時改成人工轉貼模式（exit 3）。"""
    check_model(model, effort)
    # 每次呼叫都先附上專案說明（任務裡用凍結的版本），讓 GPT 知道專案在做什麼、自己的角色是什麼
    prompt = (brief or read(FRAMEWORK / "prompts" / "gpt-brief.md")) + "\n\n---\n\n" + prompt
    tries = [model] + ([FALLBACK_MODEL] if model != FALLBACK_MODEL else [])
    errors = []
    use_codex = codex_ready()
    for m in tries:
        try:
            if use_codex:
                via_codex(prompt, out, m, effort, live_search)
                clear_pending()
                return "codex", m
            if os.environ.get("OPENAI_API_KEY"):
                served = via_api(prompt, out, m, effort, live_search)
                clear_pending()
                return "api", served
        except RuntimeError as e:
            if "usage limit" in str(e).lower() or "insufficient_quota" in str(e):  # 同一個帳號的額度，換模型也沒用
                record_quota(str(e))
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
    if stage == "verify":  # 驗收綁定這一版 final.md；之後改過就要重新驗收
        write(run / "verify-target.sha256", sha(read(run / "final.md")) + "\n")
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
    args.effort = effort_for(stage, args.effort)
    check_model(args.model, args.effort)
    runs = [Path(n).resolve() for n in names]
    # 考據類，或 project.md 寫了 web_search: live 的專案（例如以真人為基礎、資訊常變的角色），用即時搜尋
    proj_live = front_matter(read(runs[0].parent.parent / "project.md")).get("web_search") == "live"
    live = proj_live or any(r.name.split("-")[2] == "research" for r in runs)
    if len(runs) == 1:
        if stage == "free" and (runs[0] / "qa.json").exists():
            # QA 審計：開跑前重建 packets 並重寫內嵌提示，讓內容和這一輪的快照一致
            subprocess.run([sys.executable, str(ROOT / "tools" / "qa_runs.py"), "prepare", str(runs[0])], check=True)
        out, prompt = prepare_run(runs[0], stage)
        via, model = ask_gpt(prompt, out, args.model, args.effort, live_search=live,
                             brief=frozen(runs[0], "gpt-brief.md", None))
        log_gpt(runs[0], stage, via, model, args.effort)
        print(f"✓ {out.relative_to(ROOT.parent)}（{via} · {model} · {args.effort}）")
        return
    if len({r.parent for r in runs}) != 1:
        die("批次的 run 必須屬於同一個專案")
    for r in runs:
        freeze_all(r)
    if len({frozen(r, "gpt-brief.md", None) for r in runs}) > 1:
        # 每個任務凍結的專案說明不同時不能合批，否則有任務會收到別的版本（在動到任何輸出檔之前檢查）
        die("這些 run 凍結的 gpt-brief.md 版本不同，請分開呼叫（不要合批）")
    items = [(r, *prepare_run(r, stage)) for r in runs]
    raw = runs[0].parent / f"_batch-{dt.datetime.now():%Y%m%d-%H%M}-{stage}.md"
    via, model = ask_gpt(batch_prompt(items), raw, args.model, args.effort, live_search=live,
                         brief=frozen(runs[0], "gpt-brief.md", None))
    split_batch(read(raw), items)
    for run, out, _ in items:
        log_gpt(run, stage, via, model, args.effort)
        print(f"✓ {out.relative_to(ROOT.parent)}（{via} · {model} · {args.effort}）")


def cmd_gpt_resume(args):
    """額度重置後：依清單順序一次跑一個待重跑的 GPT 指令（不並行，避免一起中斷），遇到額度用完就停。"""
    if not QUOTA_FILE.exists():
        print("沒有待重跑的 GPT 指令")
        return
    data = json.loads(read(QUOTA_FILE))
    reset = data.get("reset_utc")
    if reset and not args.now and dt.datetime.fromisoformat(reset) > dt.datetime.now(dt.timezone.utc):
        print(f"⏸ 額度還沒重置（{reset}）；GPT_QUOTA_RESET_UTC={reset}", file=sys.stderr)
        sys.exit(QUOTA_EXIT)
    for cmd in list(data["pending"]):
        print(f"▶ {cmd}", flush=True)
        r = subprocess.run(shlex.split(cmd), cwd=ROOT.parent)
        if r.returncode == QUOTA_EXIT:
            sys.exit(QUOTA_EXIT)  # record_quota 已寫好新的重置時間
        if r.returncode != 0:
            print(f"✗ 失敗（exit {r.returncode}），保留在清單裡：{cmd}", file=sys.stderr)
    print("✓ 待重跑清單處理完")


def cmd_pack(args):
    for name in args.runs:
        run = Path(name).resolve()
        if not (run / "brief.md").exists():
            die(f"{run} 不是 run 目錄（缺 brief.md）")
        existed = (run / "context.md").exists()
        freeze_all(run)
        print(f"{'已存在' if existed else '✓ 產生'} {(run / 'context.md').relative_to(ROOT.parent)}")


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
                "framework/prompts/gpt-brief.md", "tools/lab.py",
                "framework/templates/dossier-character.md", "framework/templates/dossier-world.md",
                "framework/templates/dossier-idea.md", "framework/sudowrite-fields.json",
                "docs/sudowrite-2026-09.md"]


def cmd_framework_review(args):
    """框架本身也要和 GPT 商擬：把關鍵檔案打包成一份自足的提示送給 GPT。"""
    args.effort = effort_for("framework", args.effort)
    check_model(args.model, args.effort)
    files = "\n\n".join(f"## `{name}`\n\n````\n{read(ROOT / name)}\n````" for name in REVIEW_FILES)
    if args.followup:
        # 追蹤審查：只確認上一輪的必改有沒有處理好，不重新全面審查
        prompt = (read(FRAMEWORK / "prompts" / "gpt-framework-followup.md")
                  .replace("{{previous}}", read(Path(args.followup)))
                  .replace("{{changes}}", args.changes or "（見檔案）")
                  .replace("{{files}}", files))
    else:
        prompt = read(FRAMEWORK / "prompts" / "gpt-framework-review.md").replace("{{files}}", files)
    out = ROOT / "docs" / "reviews" / f"gpt-framework-review-{dt.datetime.now():%Y%m%d-%H%M}.md"
    via, model = ask_gpt(prompt, out, args.model, args.effort)
    print(f"✓ {out.relative_to(ROOT.parent)}（{via} · {model} · {args.effort}）")


def cmd_doctor(_args):
    print(f"預設模型 {DEFAULT_MODEL} · 推理 " + ", ".join(f"{k}={effort_for(k)}" for k in STAGE_EFFORT)
          + f" · 備援 {FALLBACK_MODEL}")
    check_model(DEFAULT_MODEL, DEFAULT_EFFORT)
    print(f"codex CLI：{shutil.which('codex') or '未安裝（npm i -g @openai/codex）'}")
    for env in ("OPENAI_API_KEY", "CODEX_ACCESS_TOKEN"):
        print(f"{env}：{'有' if os.environ.get(env) else '沒有'}")
    if codex_ready():
        print("→ 會透過 Codex CLI 呼叫 GPT")
    elif os.environ.get("OPENAI_API_KEY"):
        print("→ 會直接呼叫 OpenAI Responses API")
    else:
        print("→ 沒有連線方式。用 ChatGPT 帳號登入：codex login --device-auth（不需要 API 金鑰）")


# ---------------------------------------------------------------- 收錄與匯出

SW_SECTION = re.compile(r"^## \[SW\] (.+?)\s*$", re.M)
EMPTY = {"（無）", "(無)", "（none）", "(none)", "無", "none", "None", "NONE", "N/A", "n/a", "NA",
         "不適用", "（不適用）", "無此設定", "沒有找到證據", "Not applicable", "(not applicable)",
         "（交給 Sudowrite 生成）"}
CJK = re.compile(r"[぀-ヿ㐀-鿿가-힯豈-﫿]")
SECTION_DIR = {"Characters": "characters", "Worldbuilding": "world", "Story": "story"}


def sw_duplicates(text):
    names = [m.group(1) for m in SW_SECTION.finditer(text)]
    return sorted({n for n in names if names.count(n) > 1})


def sw_fields(text):
    """抓出 `## [SW] 欄位名` 的段落 → {欄位名: 內容}；「（無）」「None」等視為空白。"""
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
    """gpt-verify.md 第一個非空行（去掉 Markdown 符號）必須剛好是 APPROVE 或 CHANGES。"""
    f = run / "gpt-verify.md"
    if not f.exists():
        return None
    lines = read(f).splitlines()
    first = lines[0] if lines else ""  # 第一行必須剛好是這兩個字，不接受 **粗體** 或前置空行
    return first if first in ("APPROVE", "CHANGES") else "INVALID"


MERGE_RECORD = re.compile(r"^## (合併紀錄|Merge (Record|Log|Notes))\b", re.M)
REQUIRED_FOR_PROMOTE = ["brief.md", "claude-draft.md", "gpt-draft.md", "claude-review.md",
                        "gpt-review.md", "final.md", "gpt-verify.md"]


def cmd_promote(args):
    run = Path(args.run).resolve()
    final = run / "final.md"
    if not final.exists():
        die("沒有 final.md")
    text = read(final)
    if args.force:
        if not args.reason:
            die("--force 要附 --reason \"作者裁決的理由\"；這會記成作者裁決，不算 GPT 核准")
        with (run / "author-decision.md").open("a", encoding="utf-8") as f:
            f.write(f"- {dt.datetime.now():%Y-%m-%d %H:%M} 作者裁決收錄 final.md（sha256 {sha(text)}）：{args.reason}\n")
    else:
        missing = [n for n in REQUIRED_FOR_PROMOTE if not (run / n).exists()]
        if missing:
            die(f"流程還沒走完，缺：{', '.join(missing)}")
        if not MERGE_RECORD.search(text):
            die("final.md 沒有合併紀錄段落（## 合併紀錄 / ## Merge Record）")
        v = verdict(run)
        if v != "APPROVE":
            die(f"GPT 驗收結果是 {v}（gpt-verify.md 第一行必須剛好是 APPROVE）")
        target = run / "verify-target.sha256"
        if not target.exists() or read(target).strip() != sha(text):
            die("final.md 在 GPT 驗收之後被改過，請重新跑 verify")
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


def template_placeholders():
    """模板裡的 <…> 佔位文字；出現在成品裡代表沒填。"""
    out = set()
    for t in (FRAMEWORK / "templates").glob("dossier-*.md"):
        out |= set(re.findall(r"<[^<>\n]{2,}>", read(t)))
    return out


def cmd_export(args):
    proj = project_dir(args.slug)
    spec = json.loads(read(FIELDS_FILE))
    hard_w, hard_c, soft_w = spec["hard_limits_words"], spec["hard_limits_chars"], spec["soft_limits_words"]
    hidden = set(spec["hide_in_sudowrite"])
    known = (set(spec["character_columns"]) | set(spec["worldbuilding_columns"]) | set(spec["story_fields"])
             | set(hard_w) | set(hard_c) | set(soft_w) | hidden)
    placeholders = template_placeholders()
    errors, warnings = [], []
    cards = {"Story": [], "Characters": [], "Worldbuilding": []}

    # ---- 先驗證，全部通過才寫檔
    for f in sorted((proj / "bible").rglob("*.md")):
        text = read(f)
        fields = sw_fields(text)
        label = str(f.relative_to(proj / "bible"))
        meta = front_matter(text)
        if not fields:
            if meta.get("sw_section"):
                errors.append(f"{label}：宣告了 sw_section「{meta['sw_section']}」卻沒有任何 [SW] 段落")
            continue
        section = meta.get("sw_section") or {v: k for k, v in SECTION_DIR.items()}.get(f.parent.name)
        if section not in SECTION_DIR:
            errors.append(f"{label}：sw_section「{section}」不是 Characters / Worldbuilding / Story")
            continue
        present = {m.group(1) for m in SW_SECTION.finditer(text)}
        kind = meta.get("kind")
        allowed = {"Characters": {"character"}, "Worldbuilding": {"world", "research"}, "Story": {"idea"}}[section]
        if kind not in allowed:
            errors.append(f"{label}：kind「{kind}」和 sw_section「{section}」對不上（應為 {' / '.join(sorted(allowed))}）")
            continue
        for fld in spec["required"].get(kind, []):
            if fld not in present:
                errors.append(f"{label}：缺 [SW] {fld} 段落")
            elif not fields.get(fld):
                errors.append(f"{label}：[SW] {fld} 是必填，不能留白")
        for fld in spec["optional"].get(kind, []):
            if fld not in present:
                errors.append(f"{label}：缺 [SW] {fld} 段落（可以留白，但段落要在）")
        for d in sw_duplicates(text):
            errors.append(f"{label}：[SW] {d} 出現不只一次（後面的會蓋掉前面的）")
        for name, body in fields.items():
            if body and (any(ph in body for ph in placeholders) or (body.startswith("<") and body.endswith(">"))):
                errors.append(f"{label} · {name}：還是模板的佔位文字")
            if name not in known:
                warnings.append(f"{label} · {name}：不是已知欄位（自訂特質就沒問題；拼錯請修正）")
        if section in ("Characters", "Worldbuilding") and fields.get("Name") and fields["Name"] != meta.get("name"):
            # front matter 的 name 是正式名稱；bible 檔名、Other Names 都以它為準
            errors.append(f"{label}：[SW] Name「{fields['Name']}」和 front matter 的 name「{meta.get('name')}」不一致")
        cards.setdefault(section, []).append((f, meta, fields, label))

    # Story 只能有一份有效設定：多份時由 front matter「active: true」指定採用哪一份
    if len(cards["Story"]) > 1:
        active = [c for c in cards["Story"] if c[1].get("active", "").lower() == "true"]
        if len(active) != 1:
            names = ", ".join(lab for *_, lab in cards["Story"])
            errors.append(f"Story 有 {len(cards['Story'])} 份（{names}），請在採用的那份 front matter 寫 active: true（只能一份）")
        else:
            cards["Story"] = active

    lines = [f"# Sudowrite 貼上單 — {args.slug}",
             f"_產生時間 {dt.datetime.now():%Y-%m-%d %H:%M}。字數是本地估算：英文按單字、中日韓字元每字算 1"
             f"（中文的算法是本框架的保守估計，Sudowrite 實際怎麼算未公布）。"
             f"⛔ = 超過 Sudowrite 官方上限；⚠ = 超過建議長度或本地估算可能超限。_", ""]
    # 聲音用的 Style 區塊放最前面：照這份貼上單走的人第一步就會貼到（GPT 專案諮詢 2026-10-01，P0）
    style_md = proj / "export" / "elevenlabs" / "sudowrite-style.md"
    style_block = re.search(r"```text\n(.*?)\n```", read(style_md), re.S) if style_md.exists() else None
    if style_block:
        body = style_block.group(1).strip()
        lines += ["# Style — paste this block first",
                  f"貼到 Story Bible → **Style**（{count_words(body)} 字；故事本身的文風說明可以接在後面，合計超過約 120 字時請檢查）。"
                  "它教 Sudowrite 用每個角色的 **Audio Tags** 特質在對白裡寫 ElevenLabs v4 標籤。"
                  "說明與注意事項見 `elevenlabs/sudowrite-style.md`。", "",
                  "```text\n" + body + "\n```", ""]
    guide = {
        "Story": "貼到 Story Bible 對應的欄位（Braindump、Genre、Style、Synopsis）。還沒定稿的欄位保持空白。",
        "Characters": ("用 CSV 匯入：Story Bible 的 Characters 標題旁 ••• → Import → CSV。"
                       "`characters.csv` 是全部角色；只想加一個新角色就用 `cards/` 裡那一個的 CSV。"
                       "Sudowrite 沒說重複匯入會不會合併，**更新既有角色時請逐欄貼上**，不要再匯入一次。"
                       "**Secrets 不會自動隱藏**：匯入後、第一次用 AI 功能前，請手動按眼睛圖示隱藏。"),
        "Worldbuilding": ("用 CSV 匯入：Story Bible 的 Worldbuilding 標題旁 ••• → Import → CSV。"
                          "`worldbuilding.csv` 是全部元素；單一元素在 `cards/`。更新既有元素請逐欄貼上。"
                          "Secrets 匯入後請手動隱藏。"),
    }
    for section in ("Story", "Characters", "Worldbuilding"):
        if not cards.get(section):
            continue
        lines += [f"# {section}", guide[section], ""]
        for f, meta, fields, label in cards[section]:
            lines.append(f"## {meta.get('name', f.stem)}")
            lines.append(f"_來源：bible/{label}_\n")
            for name, body in fields.items():
                if not body:
                    continue
                n = count_words(body)
                flag = ""
                if name in hard_w and n > hard_w[name]:
                    if CJK.search(body):
                        flag = f" ⚠ 本地保守估算 {n} 超過 {hard_w[name]}（平台實際計數待確認）"
                        warnings.append(f"{label} · {name}：本地估算 {n}/{hard_w[name]}，平台計數待確認")
                    else:
                        flag = f" ⛔ 超過官方上限 {hard_w[name]}"
                        errors.append(f"{label} · {name}：{n}/{hard_w[name]}")
                elif name in hard_c and len(body) > hard_c[name]:
                    flag = f" ⛔ 超過官方上限 {hard_c[name]} 字元"
                    errors.append(f"{label} · {name}：{len(body)}/{hard_c[name]} 字元")
                elif name in soft_w and n > soft_w[name]:
                    flag = f" ⚠ 超過建議 {soft_w[name]}"
                    warnings.append(f"{label} · {name}：{n}/{soft_w[name]}")
                cap = hard_w.get(name) or soft_w.get(name)
                hide = "（CSV 不帶隱藏設定：匯入後請手動按眼睛圖示隱藏）" if name in hidden else ""
                lines.append(f"### {name}（{n}{'/' + str(cap) if cap else ''}）{flag}{hide}")
                lines.append("```text\n" + body + "\n```\n")

    if warnings:
        print("⚠ 提醒：\n  " + "\n  ".join(warnings))
    if errors:
        print("⛔ 有錯誤，這次沒有寫出任何匯出檔：\n  " + "\n  ".join(errors))
        sys.exit(2)

    # ---- 通過驗證：清掉舊成品再寫，避免殘留已刪除的卡片
    exp = proj / "export"
    if exp.exists():
        for p in exp.iterdir():
            if p.name == "elevenlabs":  # 手寫的 ElevenLabs 表演表，不是匯出產物，保留
                continue
            shutil.rmtree(p) if p.is_dir() else p.unlink()
    write(exp / "sudowrite-paste.md", "\n".join(lines))
    made = ["sudowrite-paste.md"]
    for section, fname, key in (("Characters", "characters.csv", "character_columns"),
                                ("Worldbuilding", "worldbuilding.csv", "worldbuilding_columns")):
        entries = cards.get(section, [])
        if entries:
            write_csv(exp / fname, spec[key], [fields for _, _, fields, _ in entries])
            for f, _, fields, _ in entries:
                write_csv(exp / "cards" / f"{section.lower()}-{f.stem}.csv", spec[key], [fields])
            made.append(f"{fname}（{len(entries)} 張，另有單張 CSV 在 cards/）")
    print(f"✓ {exp.relative_to(ROOT.parent)}/ → {', '.join(made)}")


def run_state(run):
    steps = [("brief.md", "brief"), ("claude-draft.md", "C稿"), ("gpt-draft.md", "G稿"),
             ("claude-review.md", "C審"), ("gpt-review.md", "G審"), ("final.md", "合併"),
             ("gpt-verify.md", "G驗")]
    marks = " ".join(("●" if (run / f).exists() else "○") + label for f, label in steps)
    v = verdict(run)
    return marks + {"APPROVE": " ✅APPROVE", "CHANGES": " ↺CHANGES", "INVALID": " ⚠驗收格式不合", None: ""}[v]


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
    s.add_argument("--model", default=DEFAULT_MODEL)
    s.add_argument("--effort", default=None, help="預設全部 xhigh（作者 2026-10-01）")
    s.set_defaults(fn=cmd_gpt)

    s = sub.add_parser("gpt-resume", help="額度重置後依序重跑 .gpt-quota.json 裡的指令")
    s.add_argument("--now", action="store_true", help="不檢查重置時間")
    s.set_defaults(fn=cmd_gpt_resume)

    s = sub.add_parser("pack"); s.add_argument("runs", nargs="+"); s.set_defaults(fn=cmd_pack)

    s = sub.add_parser("split"); s.add_argument("stage"); s.add_argument("reply")
    s.set_defaults(fn=cmd_split)

    s = sub.add_parser("promote"); s.add_argument("run"); s.add_argument("--force", action="store_true")
    s.add_argument("--reason", help="--force 時必填：作者裁決的理由")
    s.set_defaults(fn=cmd_promote)

    s = sub.add_parser("export"); s.add_argument("slug"); s.set_defaults(fn=cmd_export)
    s = sub.add_parser("status"); s.add_argument("slug", nargs="?"); s.set_defaults(fn=cmd_status)
    s = sub.add_parser("doctor"); s.set_defaults(fn=cmd_doctor)
    s = sub.add_parser("framework-review")
    s.add_argument("--followup", help="上一輪審查的檔案；只確認必改是否處理")
    s.add_argument("--changes", help="這一輪改了什麼（簡述）")
    s.add_argument("--model", default=DEFAULT_MODEL)
    s.add_argument("--effort", default=None, help="預設 xhigh")
    s.set_defaults(fn=cmd_framework_review)

    args = p.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()

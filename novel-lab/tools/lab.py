#!/usr/bin/env python3
"""novel-lab: Claude x GPT 協作的 Sudowrite 設定工作台。

只用 Python 標準庫。子指令：

  new-project <slug> [--title T] [--lang zh-TW]   建立一個小說專案
  brief <slug> <kind> <text...> [--name N]         把一句話的需求變成一次「調查」(run)
  gpt <run-dir> <stage>                            讓 GPT 做某一階段（draft / review / verify / free）
  promote <run-dir>                                把 final.md 收進專案的 bible/
  export <slug>                                    檢查字數上限並產生 Sudowrite 貼上單
  status [slug]                                    列出專案與每次 run 的進度
  doctor                                           檢查 GPT 連線方式與模型限制

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
    write(out, "\n".join(texts))
    return data.get("model", model)


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


def cmd_gpt(args):
    run = Path(args.run).resolve()
    if not (run / "brief.md").exists():
        die(f"{run} 不是 run 目錄（缺 brief.md）")
    if args.stage not in STAGES:
        die(f"stage 必須是 {', '.join(STAGES)}")
    check_model(args.model, args.effort)
    if args.stage == "review" and not (run / "claude-draft.md").exists():
        die("review 需要先有 claude-draft.md")
    if args.stage == "verify" and not (run / "final.md").exists():
        die("verify 需要先有 final.md")
    out = run / STAGES[args.stage]
    prompt = build_prompt(run, args.stage)
    live = run.name.split("-")[2] == "research"
    via, model = ask_gpt(prompt, out, args.model, args.effort, live_search=live)
    log = run / "gpt-log.jsonl"
    with log.open("a", encoding="utf-8") as f:
        f.write(json.dumps({"stage": args.stage, "via": via, "model": model, "effort": args.effort,
                            "at": dt.datetime.now().isoformat(timespec="seconds")},
                           ensure_ascii=False) + "\n")
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


def sw_fields(text):
    """抓出 `## [SW] 欄位名` 的段落 → {欄位名: 內容}。"""
    marks = list(SW_SECTION.finditer(text))
    out = {}
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        body = text[m.end():end]
        body = re.split(r"^## (?!\[SW\])", body, maxsplit=1, flags=re.M)[0]
        out[m.group(1)] = body.strip()
    return out


def front_matter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    meta = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip().strip('"')
    return meta


def cmd_promote(args):
    run = Path(args.run).resolve()
    final = run / "final.md"
    if not final.exists():
        die("沒有 final.md")
    verify = run / "gpt-verify.md"
    if not args.force and (not verify.exists() or "APPROVE" not in read(verify)[:400]):
        die("GPT 還沒 APPROVE（gpt-verify.md）。確定要收錄請加 --force")
    text = read(final)
    meta = front_matter(text)
    kind = meta.get("kind") or run.name.split("-")[2]
    sub = {"character": "characters", "world": "world"}.get(kind, "story")
    dest = run.parent.parent / "bible" / sub / f"{slugify(meta.get('name') or run.name)}.md"
    write(dest, text)
    print(f"✓ 收錄到 {dest.relative_to(ROOT.parent)}")


def cmd_export(args):
    proj = project_dir(args.slug)
    spec = json.loads(read(FIELDS_FILE))
    limits = spec["limits"]
    lines = [f"# Sudowrite 貼上單 — {args.slug}",
             f"_產生時間 {dt.datetime.now():%Y-%m-%d %H:%M}；字數以字元計，上限見 framework/sudowrite-fields.json_", ""]
    problems = []
    order = spec["export_order"]
    files = sorted((proj / "bible").rglob("*.md"),
                   key=lambda f: (order.index(f.parent.name) if f.parent.name in order else 99, f.name))
    for f in files:
        text = read(f)
        fields = sw_fields(text)
        if not fields:
            continue
        meta = front_matter(text)
        lines.append(f"## {meta.get('sw_section', f.parent.name)} → {meta.get('name', f.stem)}")
        lines.append(f"_來源：bible/{f.relative_to(proj / 'bible')}_\n")
        for name, body in fields.items():
            n = len(body)
            cap = limits.get(name)
            flag = ""
            if cap and n > cap:
                flag = f" ⚠ 超過上限 {cap}"
                problems.append(f"{f.name} · {name}：{n}/{cap}")
            lines.append(f"### {name}（{n}{'/' + str(cap) if cap else ''} 字元）{flag}")
            lines.append("```text\n" + body + "\n```\n")
    out = proj / "export" / "sudowrite-paste.md"
    write(out, "\n".join(lines))
    print(f"✓ {out.relative_to(ROOT.parent)}")
    if problems:
        print("⚠ 超過上限：\n  " + "\n  ".join(problems))
        sys.exit(2)


def run_state(run):
    steps = [("brief.md", "brief"), ("claude-draft.md", "C稿"), ("gpt-draft.md", "G稿"),
             ("claude-review.md", "C審"), ("gpt-review.md", "G審"), ("final.md", "合併"),
             ("gpt-verify.md", "G驗")]
    marks = " ".join(("●" if (run / f).exists() else "○") + label for f, label in steps)
    verdict = ""
    if (run / "gpt-verify.md").exists():
        head = read(run / "gpt-verify.md")[:400]
        verdict = " ✅APPROVE" if "APPROVE" in head else " ↺CHANGES"
    return marks + verdict


def cmd_status(args):
    projects = [project_dir(args.slug)] if args.slug else sorted(p for p in PROJECTS.iterdir() if p.is_dir())
    if not projects:
        print("還沒有專案。python3 novel-lab/tools/lab.py new-project <slug>")
    for proj in projects:
        n = len(list((proj / "bible").rglob("*.md")))
        print(f"\n■ {proj.name}（bible {n} 份）")
        for run in sorted((proj / "runs").iterdir()):
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

    s = sub.add_parser("gpt"); s.add_argument("run"); s.add_argument("stage")
    s.add_argument("--model", default=DEFAULT_MODEL); s.add_argument("--effort", default=DEFAULT_EFFORT)
    s.set_defaults(fn=cmd_gpt)

    s = sub.add_parser("promote"); s.add_argument("run"); s.add_argument("--force", action="store_true")
    s.set_defaults(fn=cmd_promote)

    s = sub.add_parser("export"); s.add_argument("slug"); s.set_defaults(fn=cmd_export)
    s = sub.add_parser("status"); s.add_argument("slug", nargs="?"); s.set_defaults(fn=cmd_status)
    s = sub.add_parser("doctor"); s.set_defaults(fn=cmd_doctor)

    args = p.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()

import { useEffect, useMemo, useRef, useState } from "react";
import { useQuery } from "@tanstack/react-query";
import clsx from "clsx";
import { Search, Tags, X } from "lucide-react";
import { api, type Phrase, type TagCatalogue, type TagInfo } from "./api";

/** Put a [tag] into a text at the cursor of its box (or at the end), with a space on either side where needed.
 *  Returns the new text and where the cursor goes. */
export function insertAt(el: HTMLTextAreaElement | HTMLInputElement | null, text: string, tag: string): [string, number] {
  const a = el?.selectionStart ?? text.length, b = el?.selectionEnd ?? text.length;
  const before = text.slice(0, a), after = text.slice(b);
  const t = (before && !/\s$/.test(before) ? " " : "") + tag + (after && !/^\s/.test(after) ? " " : "");
  return [before + t + after, a + t.length];
}

const namesOf = (t: TagInfo) => [t.zh, t.key, ...t.names];
const readLang = () => { try { return localStorage.getItem("tagLang") === "en" ? "en" : "zh"; } catch { return "zh"; } };

/** Every tag (tags.py), by group, searchable in any language; sounds the voice has recordings of are green. */
export function TagPicker({ onPick, sounds = [], label = "標籤", align = "left" }: {
  onPick: (tag: string) => void; sounds?: Phrase[]; label?: string; align?: "left" | "right";
}) {
  const [open, setOpen] = useState(false);
  const [q, setQ] = useState("");
  const [lang, setLang] = useState<"zh" | "en">(readLang);
  const cat = useQuery({ queryKey: ["tags"], queryFn: () => api.get<TagCatalogue>("/api/tags"), staleTime: Infinity, enabled: open });
  const box = useRef<HTMLDivElement>(null);
  useEffect(() => {
    if (!open) return;
    const close = (e: MouseEvent) => { if (box.current && !box.current.contains(e.target as Node)) setOpen(false); };
    document.addEventListener("mousedown", close);
    return () => document.removeEventListener("mousedown", close);
  }, [open]);
  const recorded = useMemo(() => new Set(sounds.filter((s) => s.clips.length)
    .flatMap((s) => [s.text, ...s.variants]).map((x) => x.replace(/^\[|\]$/g, "").trim().toLowerCase())), [sounds]);
  const hasRecording = (t: TagInfo) => namesOf(t).some((n) => recorded.has(n.toLowerCase()));
  const groups = useMemo(() => {
    const s = q.trim().toLowerCase();
    return (cat.data?.groups ?? []).map((g) => ({
      ...g, tags: s ? g.tags.filter((t) => [...namesOf(t), t.style].some((n) => n.toLowerCase().includes(s))) : g.tags,
    })).filter((g) => g.tags.length);
  }, [cat.data, q]);
  const own = sounds.filter((x) => x.clips.length && (!q.trim() || x.text.toLowerCase().includes(q.trim().toLowerCase())));
  const pick = (name: string) => { onPick(`[${name}]`); setOpen(false); };
  const setL = (l: "zh" | "en") => { setLang(l); try { localStorage.setItem("tagLang", l); } catch { /* private mode */ } };
  return (
    <div className="relative inline-block" ref={box}>
      <button type="button" onClick={() => setOpen(!open)}
        className={clsx("inline-flex items-center gap-1 rounded-full px-2.5 py-1 text-xs", open ? "bg-brand-600 text-white" : "bg-zinc-100 hover:bg-brand-100 dark:bg-zinc-800")}>
        <Tags className="size-3.5" />{label}
      </button>
      {open && (
        <div className={clsx("absolute z-30 mt-1 w-[min(38rem,calc(100vw-2rem))]", align === "right" ? "right-0" : "left-0", "rounded-xl border border-zinc-200 bg-white p-3 shadow-xl dark:border-zinc-700 dark:bg-zinc-900")}>
          <div className="mb-2 flex items-center gap-2">
            <div className="relative flex-1">
              <Search className="absolute top-2 left-2 size-3.5 text-zinc-400" />
              <input autoFocus className="input py-1 pl-7 text-sm" value={q} onChange={(e) => setQ(e.target.value)} placeholder="搜尋：害羞、照れ、nervous、喘…" />
            </div>
            <div className="flex rounded-lg border border-zinc-300 p-0.5 text-xs dark:border-zinc-700" title="插入的標籤用中文名還是英文名（效果一樣）">
              {(["zh", "en"] as const).map((l) => (
                <button key={l} onClick={() => setL(l)} className={clsx("rounded-md px-2 py-0.5", lang === l ? "bg-brand-600 text-white" : "")}>{l === "zh" ? "中" : "EN"}</button>
              ))}
            </div>
            <button onClick={() => setOpen(false)} className="text-zinc-400 hover:text-zinc-600" aria-label="關閉"><X className="size-4" /></button>
          </div>
          <div className="max-h-[55vh] space-y-3 overflow-y-auto pr-1">
            {own.length > 0 && (
              <div>
                <div className="mb-1 text-[11px] font-medium text-emerald-700 dark:text-emerald-300">你的原音（播你自己錄的聲音）</div>
                <div className="flex flex-wrap gap-1">{own.map((x) => (
                  <button key={x.id} onClick={() => pick(x.text.slice(1, -1))} className="rounded-full bg-emerald-100 px-2 py-0.5 text-xs text-emerald-900 hover:bg-emerald-200 dark:bg-emerald-900/40 dark:text-emerald-100">{x.text}</button>
                ))}</div>
              </div>
            )}
            {cat.isLoading && <p className="text-xs text-zinc-500">載入中…</p>}
            {groups.map((g) => (
              <div key={g.id}>
                <div className="mb-1 text-[11px] font-medium text-zinc-500">{g.name}{g.event ? "　只在寫的位置出現一次" : ""}</div>
                <div className="flex flex-wrap gap-1">{g.tags.map((t) => (
                  <button key={t.key} onClick={() => pick(lang === "zh" ? t.zh : t.key)}
                    title={`${t.style || (t.pause ? `停 ${t.pause} 秒` : "")}\n也可以寫：${t.names.slice(0, 12).join("、")}`}
                    className={clsx("rounded-full px-2 py-0.5 text-xs", hasRecording(t)
                      ? "bg-emerald-100 text-emerald-900 hover:bg-emerald-200 dark:bg-emerald-900/40 dark:text-emerald-100"
                      : "bg-zinc-100 hover:bg-brand-100 dark:bg-zinc-800")}>
                    {t.zh} <span className="text-zinc-400">{t.key}</span>
                  </button>
                ))}</div>
              </div>
            ))}
            {cat.data && !groups.length && !own.length && <p className="text-xs text-zinc-500">找不到。沒有的標籤也可以直接寫英文描述，例如 [like a pirate]。</p>}
          </div>
          <p className="mt-2 border-t border-zinc-100 pt-2 text-[11px] leading-5 text-zinc-500 dark:border-zinc-800">
            標籤管它後面的字，到下一個標籤為止；說話方式會延續到句尾，聲音和停頓只出現一次。停頓可以寫秒數：<code className="kbd">[停頓 1.5秒]</code>。綠色＝你已經放了原音。
          </p>
        </div>
      )}
    </div>
  );
}

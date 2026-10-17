import { useEffect, useMemo, useRef, useState } from "react";
import { Link, useLocation, useNavigate } from "react-router";
import { useQuery } from "@tanstack/react-query";
import clsx from "clsx";
import DOMPurify from "dompurify";
import { marked } from "marked";
import { BookOpenText, ExternalLink, LocateFixed, X } from "lucide-react";
import { api } from "./api";

// the manual's section for each page (anchors are <a id="…"></a> lines in docs/00-manual.md)
const ROUTE_SECTION: [string, string][] = [
  ["/voices", "step-voices"], ["/import", "step-import"], ["/review", "step-review"], ["/train", "step-train"],
  ["/models", "step-models"], ["/speak", "step-speak"], ["/perform", "step-perform"], ["/script", "step-script"],
  ["/characters", "step-script"], ["/settings", "step-settings"], ["/jobs", "step-trouble"], ["/", "start"],
];

export function sectionFor(path: string) {
  return ROUTE_SECTION.find(([r]) => (r === "/" ? path === "/" : path.startsWith(r)))?.[1] ?? "start";
}

export default function ManualPanel({ onClose }: { onClose: () => void }) {
  const doc = useQuery({ queryKey: ["doc", "00-manual"], queryFn: () => api.get<{ markdown: string }>("/api/docs/00-manual") });
  const loc = useLocation();
  const navigate = useNavigate();
  const body = useRef<HTMLDivElement>(null);
  const [toc, setToc] = useState<{ id: string; text: string }[]>([]);
  const [follow, setFollow] = useState(() => { try { return localStorage.getItem("manual-follow") !== "0"; } catch { return true; } });
  const html = useMemo(() => {
    if (!doc.data?.markdown) return "";
    const md = doc.data.markdown.replace(/\]\((\d\d-[\w-]+)(?:\.md)?\)/g, "](/guide/$1)");
    return DOMPurify.sanitize(marked.parse(md, { async: false }) as string);
  }, [doc.data]);

  const jump = (id: string, smooth = true) => {
    const el = body.current?.querySelector(`[id="${id}"]`);
    if (el && body.current) body.current.scrollTo({ top: (el as HTMLElement).offsetTop - 8, behavior: smooth ? "smooth" : "auto" });
  };
  useEffect(() => {  // headings get ids so the table of contents can jump to them
    const hs = Array.from(body.current?.querySelectorAll("h2") ?? []) as HTMLElement[];
    hs.forEach((h, i) => { if (!h.id) h.id = `m-${i}`; });
    setToc(hs.map((h) => ({ id: h.id, text: h.textContent ?? "" })));
  }, [html]);
  useEffect(() => { if (follow && html) jump(sectionFor(loc.pathname), false); }, [loc.pathname, html, follow]);
  useEffect(() => { try { localStorage.setItem("manual-follow", follow ? "1" : "0"); } catch { /* private mode */ } }, [follow]);

  // links: pages of the app open in place (the manual stays open), #anchors scroll, other sites open a new tab
  const onClick = (e: React.MouseEvent) => {
    const a = (e.target as HTMLElement).closest("a");
    const href = a?.getAttribute("href");
    if (!a || !href) return;
    if (href.startsWith("#")) { e.preventDefault(); jump(href.slice(1)); return; }
    if (href.startsWith("/api/")) return;  // downloads (e.g. the emotion list template)
    if (href.startsWith("/")) {
      e.preventDefault();
      const [path, hash] = href.split("#");
      navigate(path + (hash ? `#${hash}` : ""));
      if (hash) setTimeout(() => document.getElementById(hash)?.scrollIntoView({ behavior: "smooth", block: "start" }), 300);
      return;
    }
    if (/^https?:/.test(href)) { e.preventDefault(); window.open(href, "_blank", "noopener"); }
  };

  return (
    <div className="flex h-full flex-col">
      <div className="flex shrink-0 items-center gap-2 border-b border-zinc-200 px-4 py-2.5 dark:border-zinc-800">
        <BookOpenText className="size-4 text-brand-600" />
        <div className="font-semibold">使用手冊</div>
        <div className="ml-auto flex items-center gap-1">
          <button title={follow ? "跟著目前的頁面捲動（開）" : "跟著目前的頁面捲動（關）"} onClick={() => { setFollow(!follow); if (!follow) jump(sectionFor(loc.pathname)); }}
            className={clsx("rounded-lg p-1.5", follow ? "bg-brand-50 text-brand-700 dark:bg-brand-900/30 dark:text-brand-200" : "text-zinc-500 hover:bg-zinc-100 dark:hover:bg-zinc-800")}>
            <LocateFixed className="size-4" />
          </button>
          <Link to="/guide/00-manual" title="在教學頁開啟（比較寬）" className="rounded-lg p-1.5 text-zinc-500 hover:bg-zinc-100 dark:hover:bg-zinc-800"><ExternalLink className="size-4" /></Link>
          <button onClick={onClose} title="關閉手冊" className="rounded-lg p-1.5 text-zinc-500 hover:bg-zinc-100 dark:hover:bg-zinc-800"><X className="size-4" /></button>
        </div>
      </div>
      {toc.length > 0 && (
        <div className="shrink-0 border-b border-zinc-200 px-4 py-2 dark:border-zinc-800">
          <select className="input py-1 text-xs" value="" onChange={(e) => e.target.value && jump(e.target.value)}>
            <option value="">跳到…</option>
            {toc.map((t) => <option key={t.id} value={t.id}>{t.text}</option>)}
          </select>
        </div>
      )}
      <div ref={body} className="relative flex-1 overflow-y-auto px-5 py-4" onClick={onClick}>
        {doc.isError ? <p className="text-sm text-red-500">讀不到手冊（docs/00-manual.md）。</p>
          : <article className="prose-guide prose-manual" dangerouslySetInnerHTML={{ __html: html }} />}
      </div>
    </div>
  );
}

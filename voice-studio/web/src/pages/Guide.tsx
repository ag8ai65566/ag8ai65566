import { useMemo } from "react";
import { Link, useParams } from "react-router";
import { useQuery } from "@tanstack/react-query";
import clsx from "clsx";
import DOMPurify from "dompurify";
import { marked } from "marked";
import { api } from "../api";
import { Card, PageHeader } from "../ui";

type Doc = { id: string; title: string; markdown?: string };

export default function Guide() {
  const { doc } = useParams();
  const list = useQuery({ queryKey: ["docs"], queryFn: () => api.get<Doc[]>("/api/docs") });
  const id = doc ?? list.data?.[0]?.id;
  const cur = useQuery({ queryKey: ["doc", id], enabled: !!id, queryFn: () => api.get<Doc>(`/api/docs/${id}`) });
  const html = useMemo(() => {
    if (!cur.data?.markdown) return "";
    // internal links like (05-models.md) or (05-models) open inside the guide
    const md = cur.data.markdown.replace(/\]\((\d\d-[\w-]+)(?:\.md)?\)/g, "](/guide/$1)");
    return DOMPurify.sanitize(marked.parse(md, { async: false }) as string);
  }, [cur.data]);
  const idx = list.data?.findIndex((d) => d.id === id) ?? -1;
  const prev = idx > 0 ? list.data![idx - 1] : null;
  const next = list.data && idx >= 0 && idx < list.data.length - 1 ? list.data[idx + 1] : null;
  return (
    <div>
      <PageHeader title="教學" subtitle="從第一次安裝到合成整場對話。每一章都可以單獨看。" />
      <div className="grid gap-6 lg:grid-cols-[240px_1fr]">
        <nav className="space-y-0.5">
          {list.data?.map((d) => (
            <Link key={d.id} to={`/guide/${d.id}`}
              className={clsx("block rounded-lg px-3 py-2 text-sm", d.id === id ? "bg-brand-50 font-medium text-brand-700 dark:bg-brand-900/30 dark:text-brand-200" : "text-zinc-600 hover:bg-zinc-100 dark:text-zinc-400 dark:hover:bg-zinc-800")}>
              {d.title}
            </Link>
          ))}
        </nav>
        <Card>
          <article className="prose-guide max-w-3xl" dangerouslySetInnerHTML={{ __html: html }} />
          <div className="mt-10 flex justify-between border-t border-zinc-100 pt-4 text-sm dark:border-zinc-800">
            {prev ? <Link to={`/guide/${prev.id}`} className="text-brand-600">← {prev.title}</Link> : <span />}
            {next ? <Link to={`/guide/${next.id}`} className="text-brand-600">{next.title} →</Link> : <span />}
          </div>
        </Card>
      </div>
    </div>
  );
}

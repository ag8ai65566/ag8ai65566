import { useState } from "react";
import { Link } from "react-router";
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import clsx from "clsx";
import { Download, Search, Wand2 } from "lucide-react";
import { api, LANGS, MODES, type CharacterPreset, type Model } from "../api";
import { Badge, Button, Card, Empty, ErrorText, Field, PageHeader } from "../ui";

export default function Characters() {
  const qc = useQueryClient();
  const presets = useQuery({ queryKey: ["presets"], queryFn: () => api.get<CharacterPreset[]>("/api/presets") });
  const models = useQuery({ queryKey: ["models"], queryFn: () => api.get<Model[]>("/api/models") });
  const imp = useMutation({ mutationFn: () => api.post<{ created: number; updated: number }>("/api/presets/import-holoen"), onSuccess: () => qc.invalidateQueries({ queryKey: ["presets"] }) });
  const [q, setQ] = useState("");
  const [lang, setLang] = useState("");
  const [open, setOpen] = useState<string | null>(null);
  const list = (presets.data ?? []).filter((p) => (!lang || p.data.language === lang) && (!q || p.name.toLowerCase().includes(q.toLowerCase())));
  const cur = presets.data?.find((p) => p.id === open) ?? list[0];
  return (
    <div>
      <PageHeader title="角色預設"
        subtitle="從 novel-lab 的表演單（performance sheet）匯入每個角色的語言、語氣標籤、情境和念法注意事項。劇本配音時會自動套用。預設只有「怎麼演」，不含任何人的聲音；聲音一律來自你有同意紀錄的模型。"
        actions={<Button variant="secondary" onClick={() => imp.mutate()} loading={imp.isPending}><Download className="size-4" />從 novel-lab 匯入／更新</Button>} />
      {imp.data && <p className="mb-4 text-sm text-emerald-600">匯入完成：新增 {imp.data.created}、更新 {imp.data.updated}。</p>}
      <ErrorText error={imp.error} />
      {!presets.data?.length ? (
        <Empty icon={<Wand2 className="size-8" />} title="還沒有角色預設">按右上角「從 novel-lab 匯入」，會讀取 novel-lab/projects/holoen/export/elevenlabs 裡的表演單。</Empty>
      ) : (
        <div className="grid gap-6 lg:grid-cols-[300px_1fr]">
          <div>
            <div className="mb-3 flex gap-2">
              <div className="relative flex-1"><Search className="absolute top-2.5 left-2.5 size-4 text-zinc-400" />
                <input className="input pl-8" placeholder="搜尋角色" value={q} onChange={(e) => setQ(e.target.value)} /></div>
              <select className="input w-24" value={lang} onChange={(e) => setLang(e.target.value)}><option value="">全部</option><option value="ja">日文</option><option value="en">英文</option></select>
            </div>
            <ul className="max-h-[70vh] space-y-1 overflow-y-auto">
              {list.map((p) => {
                const m = models.data?.find((x) => x.id === p.model_id);
                return (
                  <li key={p.id}><button onClick={() => setOpen(p.id)}
                    className={clsx("w-full rounded-lg px-3 py-2 text-left text-sm", cur?.id === p.id ? "bg-brand-50 dark:bg-brand-900/20" : "hover:bg-zinc-50 dark:hover:bg-zinc-800/50")}>
                    <div className="flex items-center gap-2"><span className="flex-1 truncate font-medium">{p.name}</span><Badge>{LANGS[p.data.language]}</Badge></div>
                    <div className="truncate text-xs text-zinc-500">{m ? `聲音：${m.name}` : "尚未指定聲音"}</div>
                  </button></li>
                );
              })}
            </ul>
          </div>
          {cur && <PresetDetail key={cur.id} p={cur} models={models.data ?? []} />}
        </div>
      )}
    </div>
  );
}

function PresetDetail({ p, models }: { p: CharacterPreset; models: Model[] }) {
  const qc = useQueryClient();
  const save = useMutation({ mutationFn: (b: Record<string, unknown>) => api.patch(`/api/presets/${p.id}`, b), onSuccess: () => qc.invalidateQueries({ queryKey: ["presets"] }) });
  const m = models.find((x) => x.id === p.model_id);
  const d = p.data;
  return (
    <div className="min-w-0 space-y-6">
      <Card title={p.name}>
        <div className="grid gap-3 sm:grid-cols-2">
          <Field label="用哪個聲音模型演這個角色" hint="只能選你自己的模型（有同意紀錄的聲音）。">
            <select className="input" value={p.model_id ?? ""} onChange={(e) => save.mutate({ model_id: e.target.value })}>
              <option value="">尚未指定</option>
              {models.map((x) => <option key={x.id} value={x.id}>{x.name}</option>)}
            </select>
          </Field>
          {m && <Field label="預設合成方式"><select className="input" value={d.cast_mode ?? ""} onChange={(e) => save.mutate({ mode: e.target.value })}>
            <option value="">跟著模型</option>{m.modes.map((k) => <option key={k} value={k}>{MODES[k]?.label}</option>)}</select></Field>}
        </div>
        <div className="mt-4 text-sm">
          <div className="label">台詞語言</div><div>{LANGS[d.language]}</div>
          <div className="label mt-3">常用語氣</div>
          <div className="flex flex-wrap gap-1">{d.default_tags.map((t) => <span key={t} className="kbd">[{t}]</span>)}</div>
          {d.extra_tags.length > 0 && <><div className="label mt-3">其他可用標籤</div><div className="flex flex-wrap gap-1">{d.extra_tags.map((t) => <span key={t} className="kbd">[{t}]</span>)}</div></>}
        </div>
        {m && <Link to={`/speak?model=${m.id}`} className="mt-4 inline-block"><Button size="sm">用這個角色試念</Button></Link>}
      </Card>
      {d.situations.length > 0 && (
        <Card title="情境">
          <table className="w-full text-sm"><tbody>
            {d.situations.map((s) => (
              <tr key={s.situation} className="border-t border-zinc-100 align-top first:border-0 dark:border-zinc-800">
                <td className="py-2 pr-3 font-medium whitespace-nowrap">{s.situation}</td>
                <td className="py-2 pr-3">{s.tags.map((t) => <span key={t} className="kbd mr-1">[{t}]</span>)}</td>
                <td className="py-2 text-zinc-600 dark:text-zinc-400">{s.example}</td>
              </tr>))}
          </tbody></table>
        </Card>
      )}
      {(d.reading_guide || d.avoid) && (
        <Card title="念法注意">
          {d.reading_guide && <p className="text-sm whitespace-pre-wrap">{d.reading_guide}</p>}
          {d.avoid && <><div className="label mt-3">避免</div><p className="text-sm whitespace-pre-wrap">{d.avoid}</p></>}
        </Card>
      )}
      {d.examples.length > 0 && (
        <Card title="示範台詞">
          <ul className="space-y-2 text-sm">{d.examples.map((e, i) => <li key={i}>{e.text}{e.romaji && <div className="text-xs text-zinc-500">{e.romaji}</div>}</li>)}</ul>
        </Card>
      )}
    </div>
  );
}

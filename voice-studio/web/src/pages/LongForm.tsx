import { useEffect, useState } from "react";
import { Link, useSearchParams } from "react-router";
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import clsx from "clsx";
import { Download, FileText, Mic2, RefreshCw, Scissors, Trash2 } from "lucide-react";
import { api, EMOTIONS, LANGS, MODES, type Model } from "../api";
import { Badge, Button, Card, Empty, ErrorText, Field, PlayButton, Progress, usePlayer, Wave } from "../ui";

const MAX = 20000;
type LineIn = { i: number; text: string; emotion: string; style: string; pause: number; skip: boolean };
type LineOut = { i: number; match: number | null; heard: string; emotion: string | null; spoken: number; model_id: string };
type Opts = { mode: string; takes: number; emotion: string; style: string; phrases: boolean };
type Doc = {
  id: string; name: string; status: string; lang: string | null; phrases: LineIn[]; meta: { text?: string };
  params: Partial<Opts> & { model_id?: string };
  result: { output_id?: string; model_id?: string; phrases?: LineOut[]; error?: string };
  job: { status: string; progress: number; message: string } | null;
};
export const STYLE_CHIPS: [string, string][] = [
  ["開心", "cheerful, bright"], ["興奮", "excited, energetic"], ["平靜", "calm, steady"], ["溫柔", "gentle, warm"],
  ["小聲", "soft, quiet"], ["悄悄話", "whispering"], ["慢慢說", "slow, unhurried"], ["快一點", "slightly faster"],
  ["生氣", "annoyed, sharp"], ["難過", "sad, subdued"], ["無奈", "deadpan, dry"], ["撒嬌", "playful, teasing"],
];
const busy = (d?: Doc) => !!d && d.status === "rendering" && d.job?.status !== "failed";
const tagsOf = (t: string) => Array.from(t.matchAll(/\[([^\]]{1,40})\]/g)).map((m) => m[1]);

/** Long text: split into lines, give any line its own emotion, style hint and pause, render all, redo any one. */
export default function LongForm({ models, initialText }: { models: Model[]; initialText?: string }) {
  const qc = useQueryClient();
  const [sp, setSp] = useSearchParams();
  const id = sp.get("doc") ?? "";
  const list = useQuery({ queryKey: ["longform"], queryFn: () => api.get<Doc[]>("/api/perform?kind=text") });
  const doc = useQuery({
    queryKey: ["longform", id], enabled: !!id, queryFn: () => api.get<Doc>(`/api/perform/${id}`),
    refetchInterval: (q) => (busy(q.state.data) ? 1500 : false),
  });
  const d = doc.data;
  const [text, setText] = useState(initialText ?? "");
  const [name, setName] = useState("");
  const [language, setLanguage] = useState("");
  useEffect(() => { if (d) { setText(d.meta.text ?? ""); setName(d.name); setLanguage(d.lang ?? ""); } }, [d?.id]); // eslint-disable-line react-hooks/exhaustive-deps
  const select = (v: string) => setSp((cur) => { const n = new URLSearchParams(cur); if (v) n.set("doc", v); else n.delete("doc"); return n; });
  const create = useMutation({
    mutationFn: () => api.post<Doc>("/api/perform/text", { text, name, language: language || null }),
    onSuccess: (r) => { select(r.id); qc.invalidateQueries({ queryKey: ["longform"] }); },
  });
  const resplit = useMutation({
    mutationFn: () => api.put<Doc>(`/api/perform/${id}/text`, { text, name, language: language || null }),
    onSuccess: () => qc.invalidateQueries({ queryKey: ["longform"] }),
  });
  const remove = useMutation({
    mutationFn: (x: string) => api.del(`/api/perform/${x}`),
    onSuccess: (_r, x) => { if (x === id) select(""); qc.invalidateQueries({ queryKey: ["longform"] }); },
  });
  const changed = !!d && text.trim() !== (d.meta.text ?? "").trim();

  return (
    <div className="space-y-6">
      <Card title="1. 貼上文字">
        <div className="grid gap-4 lg:grid-cols-[1fr_260px]">
          <div className="space-y-3">
            <Field label={`文字（${text.length.toLocaleString()}/${MAX.toLocaleString()}）`}
              hint={<>空一行＝換段落（停比較久）。句子開頭可以加 <code className="kbd">[excited]</code>、<code className="kbd">[whispers]</code> 這類標籤；寫在段落開頭的標籤會套用到整段。</>}>
              <textarea className="input min-h-56 text-base leading-7" value={text} maxLength={MAX} onChange={(e) => setText(e.target.value)}
                placeholder={"[excited] やっほー！今日はね、すごいニュースがあるの。\n\n[whispers] これはまだ秘密なんだけど…"} />
            </Field>
            <div className="grid gap-3 sm:grid-cols-2">
              <Field label="名稱（選填）"><input className="input" value={name} onChange={(e) => setName(e.target.value)} placeholder="第一行會當名稱" /></Field>
              <Field label="語言">
                <select className="input" value={language} onChange={(e) => setLanguage(e.target.value)}>
                  <option value="">自動（每句自己判斷）</option>
                  {Object.entries(LANGS).map(([k, l]) => <option key={k} value={k}>{l}</option>)}
                </select>
              </Field>
            </div>
            <div className="flex flex-wrap gap-2">
              {!d ? (
                <Button onClick={() => create.mutate()} loading={create.isPending} disabled={!text.trim()}><Scissors className="size-4" />分句</Button>
              ) : (
                <>
                  <Button variant="secondary" onClick={() => confirm("用改過的全文重新分句？每一句的設定和已經念好的結果會重來。") && resplit.mutate()}
                    loading={resplit.isPending} disabled={!changed || busy(d)}><Scissors className="size-4" />用改過的全文重新分句</Button>
                  <Button variant="ghost" onClick={() => { select(""); setText(""); setName(""); }}>新的一篇</Button>
                </>
              )}
            </div>
            <ErrorText error={create.error ?? resplit.error} />
          </div>
          <div>
            <div className="label">之前的長文</div>
            {!list.data?.length ? <p className="text-xs text-zinc-500">還沒有。</p> : (
              <ul className="max-h-72 space-y-0.5 overflow-y-auto text-sm">
                {list.data.map((x) => (
                  <li key={x.id} className="flex items-center gap-1">
                    <button onClick={() => select(x.id)}
                      className={clsx("min-w-0 flex-1 truncate rounded-lg px-2 py-1 text-left",
                        x.id === id ? "bg-brand-50 font-medium text-brand-700 dark:bg-brand-900/30 dark:text-brand-200" : "hover:bg-zinc-100 dark:hover:bg-zinc-800")}>
                      {x.name} <span className="text-xs text-zinc-500">{x.phrases.length} 句{x.result.output_id ? " · 已念" : ""}</span>
                    </button>
                    <button title="刪除" className="p-1 text-zinc-400 hover:text-red-500" onClick={() => confirm(`刪除「${x.name}」？`) && remove.mutate(x.id)}><Trash2 className="size-3.5" /></button>
                  </li>
                ))}
              </ul>
            )}
          </div>
        </div>
      </Card>
      {!d ? (
        <Card><Empty icon={<FileText className="size-8" />} title="貼上文字後按「分句」">每一句都可以單獨調整情緒、風格、停頓，不滿意的那句可以單獨重念。</Empty></Card>
      ) : (
        <>
          <Lines d={d} />
          <RenderCard d={d} models={models} />
        </>
      )}
    </div>
  );
}

function Lines({ d }: { d: Doc }) {
  const player = usePlayer();
  const out = Object.fromEntries((d.result.phrases ?? []).map((l) => [l.i, l]));
  return (
    <Card title={`2. 每一句（${d.phrases.length} 句）`}>
      <p className="mb-3 text-xs text-zinc-500">
        情緒會挑你自己那種情緒的參考片段來念，最能帶出語氣；「跟標籤或預設」＝用句子裡的 [標籤]，沒有就用下面「3. 產生」選的預設。
        風格提示用英文描述最穩定，例如 <code className="kbd">slow, gentle</code>。取消勾選的句子不念。
      </p>
      <div className="space-y-2">{d.phrases.map((x) => <LineRow key={x.i} d={d} x={x} out={out[x.i]} player={player} />)}</div>
    </Card>
  );
}

function LineRow({ d, x, out, player }: { d: Doc; x: LineIn; out?: LineOut; player: ReturnType<typeof usePlayer> }) {
  const qc = useQueryClient();
  const [text, setText] = useState(x.text);
  const [style, setStyle] = useState(x.style);
  const [pause, setPause] = useState(String(x.pause));
  useEffect(() => { setText(x.text); setStyle(x.style); setPause(String(x.pause)); }, [x.text, x.style, x.pause]);
  const edit = useMutation({
    mutationFn: (f: Partial<LineIn>) => api.patch(`/api/perform/${d.id}`, { phrases: [{ i: x.i, ...f }] }),
    onSuccess: () => qc.invalidateQueries({ queryKey: ["longform", d.id] }),
  });
  const redo = useMutation({
    mutationFn: () => api.post(`/api/perform/${d.id}/render`, { ...d.params, model_id: d.result.model_id, only: [x.i] }),
    onSuccess: () => qc.invalidateQueries({ queryKey: ["longform", d.id] }),
  });
  const tags = tagsOf(x.text);
  return (
    <div className={clsx("rounded-xl border border-zinc-200 p-2.5 dark:border-zinc-800", x.skip && "opacity-50")}>
      <div className="flex items-start gap-2">
        <input type="checkbox" className="mt-2.5" title="取消勾選＝這句不念" checked={!x.skip} onChange={(e) => edit.mutate({ skip: !e.target.checked })} />
        <span className="mt-1.5 w-6 text-right text-xs text-zinc-400 tabular-nums">{x.i + 1}</span>
        <textarea className="input min-h-9 flex-1 resize-y py-1 text-sm leading-6" rows={1} value={text} onChange={(e) => setText(e.target.value)}
          onBlur={() => text !== x.text && edit.mutate({ text })} />
      </div>
      <div className="mt-2 flex flex-wrap items-center gap-x-3 gap-y-2 pl-14 text-xs">
        <label className="flex items-center gap-1"><span className="text-zinc-500">情緒</span>
          <select className="input w-32 py-1 text-xs" value={x.emotion} onChange={(e) => edit.mutate({ emotion: e.target.value })}>
            <option value="">跟標籤或預設</option>
            {EMOTIONS.map(([k, l]) => <option key={k} value={k}>{l}</option>)}
          </select>
        </label>
        {tags.length > 0 && <span className="text-zinc-500">標籤：{tags.map((t) => <Badge key={t}>{t}</Badge>)}</span>}
        <label className="flex min-w-48 flex-1 items-center gap-1"><span className="whitespace-nowrap text-zinc-500">風格提示</span>
          <input className="input py-1 text-xs" value={style} placeholder="空白＝用預設" onChange={(e) => setStyle(e.target.value)}
            onBlur={() => style !== x.style && edit.mutate({ style })} />
        </label>
        <label className="flex items-center gap-1"><span className="text-zinc-500">之後停</span>
          <input className="input w-20 py-1 text-xs tabular-nums" type="number" step="0.05" min="0" max="5" value={pause}
            onChange={(e) => setPause(e.target.value)} onBlur={() => Number(pause) !== x.pause && edit.mutate({ pause: Number(pause) || 0 })} />
          <span className="text-zinc-500">秒</span>
        </label>
        {out && (
          <span className="ml-auto flex items-center gap-1">
            <PlayButton small url={`/api/perform/${d.id}/phrase/${x.i}/output?v=${d.result.output_id}`} player={player} label="聽" />
            <Button size="sm" variant="ghost" title="只重念這一句（用改過的情緒、風格）" onClick={() => redo.mutate()} disabled={busy(d)} loading={redo.isPending}>
              <RefreshCw className="size-3" />重念
            </Button>
            {out.match != null && out.match < 0.8 && <span title={`聽到：${out.heard}`}><Badge tone="amber">可能念錯</Badge></span>}
          </span>
        )}
      </div>
    </div>
  );
}

function RenderCard({ d, models }: { d: Doc; models: Model[] }) {
  const qc = useQueryClient();
  const [modelId, setModelId] = useState(d.params.model_id ?? models[0]?.id ?? "");
  const model = models.find((m) => m.id === modelId);
  const [opts, setOpts] = useState<Opts>({
    mode: d.params.mode ?? "", takes: d.params.takes ?? 2, emotion: d.params.emotion ?? "", style: d.params.style ?? "",
    phrases: d.params.phrases ?? true,
  });
  useEffect(() => {
    if (!model) return;
    const preferred = model.modes.includes("ref") && model.meta.references?.length ? "ref" : model.modes[0];
    setOpts((o) => ({ ...o, mode: model.modes.includes(o.mode) ? o.mode : preferred }));
  }, [model?.id]); // eslint-disable-line react-hooks/exhaustive-deps
  const render = useMutation({
    mutationFn: () => api.post(`/api/perform/${d.id}/render`,
      { model_id: modelId, ...opts, emotion: opts.emotion || null, keep_pauses: true, match_timing: false, follow_level: false }),
    onSuccess: () => qc.invalidateQueries({ queryKey: ["longform", d.id] }),
  });
  const rendering = busy(d);
  const oid = d.result.output_id;
  const n = d.phrases.filter((x) => !x.skip).length;
  if (!models.length)
    return <Card title="3. 產生"><Empty title="還沒有模型">先 <Link to="/train" className="underline">訓練一個</Link>。</Empty></Card>;
  return (
    <Card title="3. 產生">
      <div className="grid gap-4 md:grid-cols-2">
        <div className="space-y-3">
          <Field label="模型">
            <select className="input" value={modelId} onChange={(e) => setModelId(e.target.value)}>
              {models.map((m) => <option key={m.id} value={m.id}>{m.name}</option>)}
            </select>
          </Field>
          {model && !model.available[0] && <p className="rounded-lg bg-amber-50 px-3 py-2 text-xs text-amber-800 dark:bg-amber-950/40 dark:text-amber-200">本機還不能用 {model.engine_name}：{model.available[1]}。<Link to="/settings#engines" className="underline">安裝引擎</Link></p>}
          <div>
            <span className="label">合成方式</span>
            <div className="grid gap-2">
              {(model?.modes ?? []).map((k) => (
                <button key={k} onClick={() => setOpts({ ...opts, mode: k })}
                  className={clsx("rounded-xl border p-2.5 text-left", opts.mode === k ? "border-brand-500 ring-2 ring-brand-500/20" : "border-zinc-200 dark:border-zinc-800")}>
                  <div className="text-sm font-medium">{MODES[k]?.label ?? k}{k === "ref" && " （建議）"}</div>
                  <div className="mt-0.5 text-[11px] leading-4 text-zinc-500">
                    {k === "ref" ? "每句挑你自己同情緒的參考片段，最能帶出語氣。要先在模型頁有參考片段。" : MODES[k]?.hint}
                  </div>
                </button>
              ))}
            </div>
          </div>
        </div>
        <div className="space-y-3">
          <Field label="預設情緒" hint="給沒有自己情緒、也沒有 [標籤] 的句子。">
            <select className="input" value={opts.emotion} onChange={(e) => setOpts({ ...opts, emotion: e.target.value })}>
              <option value="">不指定（模型平常的說法）</option>
              {EMOTIONS.map(([k, l]) => <option key={k} value={k}>{l}</option>)}
            </select>
          </Field>
          <Field label="預設風格提示" hint="給沒有自己風格提示的句子。「完整複製」模式會忽略風格提示。">
            <input className="input" value={opts.style} onChange={(e) => setOpts({ ...opts, style: e.target.value })} placeholder="natural, conversational" />
            <div className="mt-2 flex flex-wrap gap-1">{STYLE_CHIPS.map(([zh, en]) => (
              <button key={zh} onClick={() => setOpts({ ...opts, style: opts.style ? `${opts.style}, ${en}` : en })} className="rounded-full bg-zinc-100 px-2 py-0.5 text-xs hover:bg-brand-100 dark:bg-zinc-800">{zh}</button>))}</div>
          </Field>
          <div className="grid grid-cols-2 gap-3">
            <Field label={`每句念幾次（${opts.takes}）`}>
              <input type="range" min={1} max={5} value={opts.takes} className="w-full" onChange={(e) => setOpts({ ...opts, takes: Number(e.target.value) })} />
            </Field>
            <label className="mt-6 flex items-center gap-2 text-sm"><input type="checkbox" checked={opts.phrases} onChange={(e) => setOpts({ ...opts, phrases: e.target.checked })} />口頭禪、聲音標籤用原音</label>
          </div>
          <Button className="w-full" onClick={() => render.mutate()} loading={render.isPending} disabled={!modelId || rendering || !opts.mode || !n}>
            <Mic2 className="size-4" />全部產生（{n} 句）
          </Button>
          <ErrorText error={render.error} />
          {rendering && <div><div className="mb-1 text-xs text-zinc-500">{d.job?.message}</div><Progress value={d.job?.progress ?? 0} /></div>}
          {d.result.error && !rendering && <ErrorText error={`上次產生失敗：${d.result.error}`} />}
        </div>
      </div>
      {oid && (
        <div className="mt-5 border-t border-zinc-100 pt-4 dark:border-zinc-800">
          <div className="label flex items-center justify-between">整篇
            <span className="flex gap-2 text-xs font-normal">
              <a className="inline-flex items-center gap-1 text-brand-600 hover:underline" href={`/api/outputs/${oid}/audio`} download><Download className="size-3" />WAV</a>
              <a className="inline-flex items-center gap-1 text-brand-600 hover:underline" href={`/api/outputs/${oid}/audio?format=mp3`} download><Download className="size-3" />MP3</a>
            </span>
          </div>
          <Wave key={oid} src={`/api/outputs/${oid}/audio`} />
          <p className="mt-2 text-xs text-zinc-500">哪一句不像：在那一句改情緒或風格提示，按那一句的「重念」，其他句不變，整篇會重新接好。</p>
        </div>
      )}
    </Card>
  );
}

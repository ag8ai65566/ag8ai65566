import { useEffect, useRef, useState } from "react";
import { Link, useSearchParams } from "react-router";
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import clsx from "clsx";
import { Download, Drama, RefreshCw, RotateCcw, Trash2, Upload } from "lucide-react";
import { api, EMOTION_LABEL, EMOTIONS, LANGS, MODES, type Model } from "../api";
import { Badge, Button, Card, Empty, ErrorText, Field, PageHeader, PlayButton, Progress, usePlayer, Wave } from "../ui";

type Phrase = {
  i: number; start: number; end: number; text: string; emotion: string; style: string; pause: number; skip: boolean;
  tags: string[]; labels: string[]; guess: { emotion: string; style: string };
  rel: { level: number; pitch: number; range: number; rate: number; end: number };
};
type Line = { i: number; match: number | null; heard: string; emotion: string | null; stretch: number; original: number;
  spoken: number; gain_db?: number };
type Perf = {
  id: string; name: string; status: string; lang: string | null; duration: number | null; phrases: Phrase[];
  params: Partial<RenderOpts> & { model_id?: string };
  result: { output_id?: string; model_id?: string; phrases?: Line[]; error?: string };
  job: { id: string; kind: string; status: string; progress: number; message: string } | null;
};
type RenderOpts = { mode: string; takes: number; keep_pauses: boolean; match_timing: boolean; follow_level: boolean; phrases: boolean };

function upload(file: File, fields: Record<string, string>, onProgress: (f: number) => void) {
  return new Promise<Perf>((resolve, reject) => {
    const fd = new FormData();
    fd.append("file", file);
    Object.entries(fields).forEach(([k, v]) => fd.append(k, v));
    const x = new XMLHttpRequest();
    x.open("POST", "/api/perform");
    x.upload.onprogress = (e) => e.lengthComputable && onProgress(e.loaded / e.total);
    x.onload = () => (x.status < 300 ? resolve(JSON.parse(x.responseText)) : reject(new Error(x.responseText || x.statusText)));
    x.onerror = () => reject(new Error("上傳失敗（連線中斷）"));
    x.send(fd);
  });
}

const busy = (p?: Perf) => !!p && (p.status === "analyzing" || p.status === "rendering") && p.job?.status !== "failed";

export default function Perform() {
  const qc = useQueryClient();
  const [sp, setSp] = useSearchParams();
  const pid = sp.get("id") ?? "";
  const list = useQuery({ queryKey: ["perform"], queryFn: () => api.get<Perf[]>("/api/perform") });
  const rec = useQuery({
    queryKey: ["perform", pid], enabled: !!pid, queryFn: () => api.get<Perf>(`/api/perform/${pid}`),
    refetchInterval: (q) => (busy(q.state.data) ? 1500 : false),
  });
  const models = useQuery({ queryKey: ["models"], queryFn: () => api.get<Model[]>("/api/models") });
  const [language, setLanguage] = useState("");
  const [separate, setSeparate] = useState(false);
  const [drag, setDrag] = useState(false);
  const [up, setUp] = useState<{ name: string; progress: number } | null>(null);
  const [upError, setUpError] = useState<unknown>(null);
  const fileInput = useRef<HTMLInputElement>(null);
  const p = rec.data;

  async function send(f: File) {
    setUpError(null);
    setUp({ name: f.name, progress: 0 });
    try {
      const r = await upload(f, { language, separate: String(separate) }, (x) => setUp({ name: f.name, progress: x }));
      setSp({ id: r.id });
      qc.invalidateQueries({ queryKey: ["perform"] });
    } catch (e) {
      setUpError(e);
    }
    setUp(null);
  }
  const reanalyze = useMutation({
    mutationFn: () => api.post(`/api/perform/${pid}/analyze`, { language: language || p?.lang, separate }),
    onSuccess: () => qc.invalidateQueries({ queryKey: ["perform"] }),
  });
  const remove = useMutation({
    mutationFn: (id: string) => api.del(`/api/perform/${id}`),
    onSuccess: () => { setSp({}); qc.invalidateQueries({ queryKey: ["perform"] }); },
  });

  return (
    <div>
      <PageHeader title="照著念"
        subtitle="丟一段錄音進來，用你訓練好的聲音照它的台詞、停頓和口氣再念一次。聲音、音高和說話習慣還是你自己的。" />
      <div className="mb-6 rounded-xl border border-zinc-200 bg-zinc-50 px-4 py-3 text-sm leading-6 text-zinc-600 dark:border-zinc-800 dark:bg-zinc-900 dark:text-zinc-300">
        原音只用來<b>分析</b>：聽出每句台詞、句子之間停多久，以及每句比起整段是大聲還是小聲、高還是低、快還是慢、句尾上揚還是下降。
        合成時用的是<b>你的模型和你自己的參考片段</b>，不會把原音的聲音複製過來。分析結果是猜的，每一句都可以改。
      </div>
      <div className="space-y-6">
        <Card title="1. 上傳錄音">
          <div className="grid gap-5 md:grid-cols-2">
            <div className="space-y-3">
              <div
                onDragOver={(e) => { e.preventDefault(); setDrag(true); }} onDragLeave={() => setDrag(false)}
                onDrop={(e) => { e.preventDefault(); setDrag(false); if (e.dataTransfer.files[0]) send(e.dataTransfer.files[0]); }}
                onClick={() => fileInput.current?.click()}
                className={clsx("flex cursor-pointer flex-col items-center justify-center rounded-2xl border-2 border-dashed px-4 py-7 text-center transition",
                  drag ? "border-brand-500 bg-brand-50 dark:bg-brand-900/20" : "border-zinc-300 hover:border-brand-400 dark:border-zinc-700")}>
                <Upload className="mb-2 size-7 text-brand-500" />
                <p className="text-sm font-medium">把錄音或影片拖到這裡，或點一下選檔</p>
                <p className="mt-1 text-xs text-zinc-500">最多前 5 分鐘。一段 10–60 秒、人聲清楚的最好。</p>
                <input ref={fileInput} type="file" className="hidden" accept="audio/*,video/*,.mkv,.flv,.ts"
                  onChange={(e) => { if (e.target.files?.[0]) send(e.target.files[0]); e.target.value = ""; }} />
              </div>
              {up && <div className="text-xs"><div className="truncate">{up.name}</div><Progress value={up.progress} className="mt-1" /></div>}
              <ErrorText error={upError} />
            </div>
            <div className="space-y-3">
              <div className="grid gap-3 sm:grid-cols-2">
                <Field label="錄音的語言">
                  <select className="input" value={language} onChange={(e) => setLanguage(e.target.value)}>
                    <option value="">自動判斷</option>
                    {Object.entries(LANGS).map(([k, l]) => <option key={k} value={k}>{l}</option>)}
                  </select>
                </Field>
                <label className="flex items-start gap-2 pt-6 text-sm">
                  <input type="checkbox" className="mt-1" checked={separate} onChange={(e) => setSeparate(e.target.checked)} />
                  <span>去除背景音樂<span className="block text-xs text-zinc-500">有配樂或遊戲音效時勾選</span></span>
                </label>
              </div>
              {!!list.data?.length && (
                <div>
                  <div className="label">之前的錄音</div>
                  <ul className="max-h-40 space-y-0.5 overflow-y-auto text-sm">
                    {list.data.map((x) => (
                      <li key={x.id} className="flex items-center gap-1">
                        <button onClick={() => setSp({ id: x.id })}
                          className={clsx("min-w-0 flex-1 truncate rounded-lg px-2 py-1 text-left",
                            x.id === pid ? "bg-brand-50 font-medium text-brand-700 dark:bg-brand-900/30 dark:text-brand-200" : "hover:bg-zinc-100 dark:hover:bg-zinc-800")}>
                          {x.name} <span className="text-xs text-zinc-500">{x.phrases.length ? `${x.phrases.length} 句` : ""}{x.result.output_id ? " · 已念" : ""}</span>
                        </button>
                        <button title="刪除" className="p-1 text-zinc-400 hover:text-red-500"
                          onClick={() => confirm(`刪除「${x.name}」和它的結果？`) && remove.mutate(x.id)}><Trash2 className="size-3.5" /></button>
                      </li>
                    ))}
                  </ul>
                </div>
              )}
            </div>
          </div>
        </Card>
        <div className="space-y-6">
          {!p ? (
            <Card><Empty icon={<Drama className="size-8" />} title={pid ? "載入中…" : "先上傳一段錄音"}>
              例如一段你想重新配音的台詞、別人念得很有感覺的一句話，或你自己之前錄的一段。
            </Empty></Card>
          ) : (
            <>
              <Card title={`2. 確認台詞和口氣 — ${p.name}`}
                actions={p.status !== "analyzing" && <Button size="sm" variant="ghost" onClick={() => reanalyze.mutate()} loading={reanalyze.isPending}
                  title="用上面選的語言和去背景音樂設定重新分析（會清掉修改）"><RefreshCw className="size-3.5" />重新分析</Button>}>
                {p.status === "analyzing" && p.job?.status !== "failed" ? (
                  <div><div className="mb-1 text-sm text-zinc-500">{p.job?.message ?? "排隊中"}</div><Progress value={p.job?.progress ?? 0} /></div>
                ) : p.status === "failed" || (p.status === "analyzing" && p.job?.status === "failed") ? (
                  <div className="text-sm"><ErrorText error={p.result.error ?? p.job?.message ?? "分析失敗"} />
                    <p className="mt-2 text-zinc-500">可以換語言或勾選去除背景音樂後按「重新分析」，或到 <Link to="/jobs" className="underline">工作佇列</Link> 看詳細原因。</p></div>
                ) : (
                  <Phrases p={p} />
                )}
              </Card>
              {(p.status === "ready" || p.status === "done" || p.status === "rendering") && <RenderCard p={p} models={models.data ?? []} />}
            </>
          )}
        </div>
      </div>
    </div>
  );
}

function Phrases({ p }: { p: Perf }) {
  const player = usePlayer();
  const lines = Object.fromEntries((p.result.phrases ?? []).map((l) => [l.i, l]));
  return (
    <div>
      <div className="mb-3"><Wave src={`/api/perform/${p.id}/source`} compact /></div>
      <p className="mb-3 text-xs text-zinc-500">
        「聽起來」是和整段錄音比較的結果。情緒會挑你自己那種情緒的參考片段，最能帶出口氣；風格提示是給引擎的英文說明，可以改或清空。
        取消勾選的句子不念。{LANGS[p.lang ?? ""] && <>語言：{LANGS[p.lang ?? ""]}。</>}
      </p>
      <div className="space-y-2">{p.phrases.map((x) => <Row key={x.i} p={p} x={x} line={lines[x.i]} player={player} />)}</div>
    </div>
  );
}

function Row({ p, x, line, player }: { p: Perf; x: Phrase; line?: Line; player: ReturnType<typeof usePlayer> }) {
  const qc = useQueryClient();
  const [text, setText] = useState(x.text);
  const [style, setStyle] = useState(x.style);
  const [pause, setPause] = useState(String(x.pause));
  useEffect(() => { setText(x.text); setStyle(x.style); setPause(String(x.pause)); }, [x.text, x.style, x.pause]);
  const edit = useMutation({
    mutationFn: (f: Partial<Phrase>) => api.patch(`/api/perform/${p.id}`, { phrases: [{ i: x.i, ...f }] }),
    onSuccess: () => qc.invalidateQueries({ queryKey: ["perform", p.id] }),
  });
  const redo = useMutation({
    mutationFn: () => api.post(`/api/perform/${p.id}/render`, { ...p.params, model_id: p.result.model_id, only: [x.i] }),
    onSuccess: () => qc.invalidateQueries({ queryKey: ["perform", p.id] }),
  });
  const changed = x.emotion !== x.guess.emotion || x.style !== x.guess.style;
  return (
    <div className={clsx("rounded-xl border border-zinc-200 p-2.5 dark:border-zinc-800", x.skip && "opacity-50")}>
      <div className="flex items-start gap-2">
        <input type="checkbox" className="mt-2.5" title="取消勾選＝這句不念" checked={!x.skip} onChange={(e) => edit.mutate({ skip: !e.target.checked })} />
        <span className="mt-1.5 w-5 text-right text-xs text-zinc-400 tabular-nums">{x.i + 1}</span>
        <div className="mt-0.5"><PlayButton small url={`/api/perform/${p.id}/phrase/${x.i}/source`} player={player} label={`原音 ${(x.end - x.start).toFixed(1)}s`} /></div>
        <textarea className="input min-h-9 flex-1 resize-y py-1 text-sm leading-6" rows={1} value={text} onChange={(e) => setText(e.target.value)}
          onBlur={() => text !== x.text && edit.mutate({ text })} />
      </div>
      <div className="mt-2 flex flex-wrap items-center gap-x-3 gap-y-2 pl-12 text-xs">
        <span className="flex flex-wrap items-center gap-1" title="和整段錄音比較">
          <span className="text-zinc-500">聽起來</span>
          {x.labels.length ? x.labels.map((l) => <Badge key={l}>{l}</Badge>) : <span className="text-zinc-400">跟平常一樣</span>}
        </span>
        <label className="flex items-center gap-1"><span className="text-zinc-500">情緒</span>
          <select className="input w-24 py-1 text-xs" value={x.emotion} onChange={(e) => edit.mutate({ emotion: e.target.value })}>
            <option value="">不指定</option>
            {EMOTIONS.map(([k, l]) => <option key={k} value={k}>{l}</option>)}
          </select>
        </label>
        <label className="flex min-w-48 flex-1 items-center gap-1"><span className="whitespace-nowrap text-zinc-500">風格提示</span>
          <input className="input py-1 text-xs" value={style} placeholder="例如 slow, gentle" onChange={(e) => setStyle(e.target.value)}
            onBlur={() => style !== x.style && edit.mutate({ style })} />
        </label>
        {changed && <button className="inline-flex items-center gap-0.5 text-zinc-400 hover:text-brand-600" title={`猜的是：${EMOTION_LABEL[x.guess.emotion] ?? "不指定"}／${x.guess.style || "無"}`}
          onClick={() => edit.mutate({ emotion: x.guess.emotion, style: x.guess.style })}><RotateCcw className="size-3" />用猜的</button>}
        <label className="flex items-center gap-1"><span className="text-zinc-500">之後停</span>
          <input className="input w-16 py-1 text-xs tabular-nums" type="number" step="0.1" min="0" max="5" value={pause}
            onChange={(e) => setPause(e.target.value)} onBlur={() => Number(pause) !== x.pause && edit.mutate({ pause: Number(pause) || 0 })} />
          <span className="text-zinc-500">秒</span>
        </label>
        {line && (
          <span className="ml-auto flex items-center gap-1">
            <PlayButton small url={`/api/perform/${p.id}/phrase/${x.i}/output?v=${p.result.output_id}`} player={player} label="我的聲音" />
            <Button size="sm" variant="ghost" title="只重念這一句" onClick={() => redo.mutate()} disabled={busy(p)} loading={redo.isPending}>
              <RefreshCw className="size-3" />
            </Button>
            {line.match != null && line.match < 0.8 && <span title={`聽到：${line.heard}`}><Badge tone="amber">可能念錯</Badge></span>}
          </span>
        )}
      </div>
    </div>
  );
}

function RenderCard({ p, models }: { p: Perf; models: Model[] }) {
  const qc = useQueryClient();
  const [modelId, setModelId] = useState(p.params.model_id ?? models[0]?.id ?? "");
  const model = models.find((m) => m.id === modelId);
  const [opts, setOpts] = useState<RenderOpts>({
    mode: p.params.mode ?? "", takes: p.params.takes ?? 3, keep_pauses: p.params.keep_pauses ?? true,
    match_timing: p.params.match_timing ?? true, follow_level: p.params.follow_level ?? true, phrases: p.params.phrases ?? true,
  });
  useEffect(() => { if (!modelId && models[0]) setModelId(models[0].id); }, [models, modelId]);
  useEffect(() => {
    if (!model) return;
    const preferred = model.modes.includes("ref") && model.meta.references?.length ? "ref" : model.modes[0];
    setOpts((o) => ({ ...o, mode: model.modes.includes(o.mode) ? o.mode : preferred }));
  }, [model?.id]); // eslint-disable-line react-hooks/exhaustive-deps
  const render = useMutation({
    mutationFn: () => api.post(`/api/perform/${p.id}/render`, { model_id: modelId, ...opts }),
    onSuccess: () => qc.invalidateQueries({ queryKey: ["perform", p.id] }),
  });
  const rendering = p.status === "rendering" && p.job?.status !== "failed";
  const oid = p.result.output_id;
  const check = (k: keyof RenderOpts, label: string, hint: string) => (
    <label className="flex items-start gap-2 text-sm">
      <input type="checkbox" className="mt-1" checked={!!opts[k]} onChange={(e) => setOpts({ ...opts, [k]: e.target.checked })} />
      <span>{label}<span className="block text-xs text-zinc-500">{hint}</span></span>
    </label>
  );
  if (!models.length)
    return <Card title="3. 用我的聲音念"><Empty title="還沒有模型">先 <Link to="/train" className="underline">訓練一個</Link>，或到 <Link to="/models" className="underline">模型</Link> 建立免訓練模型。</Empty></Card>;
  return (
    <Card title="3. 用我的聲音念">
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
                    {k === "ref" ? "每句挑你自己同情緒的參考片段，最能帶出口氣。要先在模型頁有參考片段。" : MODES[k]?.hint}
                  </div>
                </button>
              ))}
            </div>
          </div>
          <Field label={`每句念幾次（${opts.takes}）`} hint="多念幾次，挑長度最接近原音、而且沒念錯的那次。越多越慢。">
            <input type="range" min={1} max={5} value={opts.takes} className="w-full" onChange={(e) => setOpts({ ...opts, takes: Number(e.target.value) })} />
          </Field>
        </div>
        <div className="space-y-3">
          {check("keep_pauses", "保留原本的停頓", "句子之間停的時間照原音（每句的「之後停」可以改）。")}
          {check("match_timing", "對齊每句的長度", "把每句稍微加快或放慢（最多 ±20–25%），讓節奏接近原音。音高不變。")}
          {check("follow_level", "跟著原音的大小聲", "原音大聲的句子也大聲一點、小聲的小聲一點（最多 ±6 dB）。")}
          {check("phrases", "口頭禪用原音", "台詞裡有你的口頭禪時，接上你自己的原音片段。")}
          <Button className="w-full" onClick={() => render.mutate()} loading={render.isPending} disabled={!modelId || rendering || !opts.mode}>
            <Drama className="size-4" />用我的聲音念
          </Button>
          <ErrorText error={render.error} />
          {rendering && <div><div className="mb-1 text-xs text-zinc-500">{p.job?.message}</div><Progress value={p.job?.progress ?? 0} /></div>}
          {p.result.error && !rendering && <ErrorText error={`上次合成失敗：${p.result.error}`} />}
        </div>
      </div>
      {oid && (
        <div className="mt-5 grid gap-4 border-t border-zinc-100 pt-4 md:grid-cols-2 dark:border-zinc-800">
          <div><div className="label">原音</div><Wave src={`/api/perform/${p.id}/source`} /></div>
          <div>
            <div className="label flex items-center justify-between">我的聲音
              <span className="flex gap-2 text-xs font-normal">
                <a className="inline-flex items-center gap-1 text-brand-600 hover:underline" href={`/api/outputs/${oid}/audio`} download><Download className="size-3" />WAV</a>
                <a className="inline-flex items-center gap-1 text-brand-600 hover:underline" href={`/api/outputs/${oid}/audio?format=mp3`} download><Download className="size-3" />MP3</a>
              </span>
            </div>
            <Wave key={oid} src={`/api/outputs/${oid}/audio`} />
          </div>
          <p className="text-xs text-zinc-500 md:col-span-2">
            哪一句不像：改它的情緒或風格提示，按那一句的 <RefreshCw className="inline size-3" /> 只重念那一句。標「可能念錯」的是語音辨識聽到的和台詞不一樣。
          </p>
        </div>
      )}
    </Card>
  );
}

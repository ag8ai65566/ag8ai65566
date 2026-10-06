import { useEffect, useState } from "react";
import { Link, useSearchParams } from "react-router";
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import clsx from "clsx";
import { Boxes, Crown, Mic2, Pencil, Plus, RefreshCw, Trash2, Wand2 } from "lucide-react";
import { api, fmtDur, fmtTime, LANGS, type EngineInfo, type Model, type Segment, type Voice } from "../api";
import { Badge, Button, Card, Empty, ErrorText, Field, Modal, PageHeader, PlayButton, usePlayer } from "../ui";

const MODE_LABEL: Record<string, string> = { lora: "LoRA 微調", full: "完整微調", sft: "官方微調", zeroshot: "免訓練（零樣本）", mock: "測試" };
const pct = (x: number | null | undefined) => (x == null ? "—" : `${(x * 100).toFixed(1)}`);

export default function Models() {
  const [sp, setSp] = useSearchParams();
  const models = useQuery({ queryKey: ["models"], queryFn: () => api.get<Model[]>("/api/models"), refetchInterval: 15000 });
  const [zs, setZs] = useState(false);
  const id = sp.get("id") ?? models.data?.[0]?.id;
  return (
    <div>
      <PageHeader title="模型"
        subtitle="訓練完成的模型會出現在這裡。每個檢查點都念了同一批沒看過的句子：平台會自動評分並推薦一個，但最後請用耳朵決定。"
        actions={<Button variant="secondary" onClick={() => setZs(true)}><Wand2 className="size-4" />建立免訓練模型</Button>} />
      {!models.data?.length ? (
        <Empty icon={<Boxes className="size-8" />} title="還沒有模型">
          到 <Link to="/train" className="underline">雲端訓練</Link> 訓練一個；或先按「建立免訓練模型」用幾段錄音直接試聽引擎（不用花錢，但像的程度有限）。
        </Empty>
      ) : (
        <div className="grid gap-6 lg:grid-cols-[280px_1fr]">
          <div className="space-y-2">
            {models.data.map((m) => (
              <button key={m.id} onClick={() => setSp({ id: m.id })}
                className={clsx("card w-full p-3 text-left transition hover:border-brand-300", m.id === id && "border-brand-500 ring-2 ring-brand-500/20")}>
                <div className="truncate font-medium">{m.name}</div>
                <div className="mt-0.5 flex flex-wrap items-center gap-1.5 text-xs text-zinc-500">
                  <span>{m.voice_name}</span>·<span>{m.engine_name}</span>
                  <Badge tone={m.meta.mode === "zeroshot" ? "zinc" : "brand"}>{MODE_LABEL[m.meta.mode ?? ""] ?? m.meta.mode}</Badge>
                </div>
              </button>
            ))}
          </div>
          {id && <ModelDetail key={id} id={id} />}
        </div>
      )}
      {zs && <ZeroShotModal onClose={() => setZs(false)} onCreated={(m) => { setZs(false); setSp({ id: m.id }); }} />}
    </div>
  );
}

function ModelDetail({ id }: { id: string }) {
  const qc = useQueryClient();
  const q = useQuery({ queryKey: ["model", id], queryFn: () => api.get<Model>(`/api/models/${id}`), refetchInterval: 10000 });
  const player = usePlayer();
  const [renaming, setRenaming] = useState(false);
  const [name, setName] = useState("");
  const [picking, setPicking] = useState(false);
  const inv = () => { qc.invalidateQueries({ queryKey: ["model", id] }); qc.invalidateQueries({ queryKey: ["models"] }); };
  const patch = useMutation({ mutationFn: (b: Record<string, unknown>) => api.patch(`/api/models/${id}`, b), onSuccess: inv });
  const evaluate = useMutation({ mutationFn: () => api.post(`/api/models/${id}/evaluate`), onSuccess: inv });
  const del = useMutation({ mutationFn: () => api.del(`/api/models/${id}`), onSuccess: () => { qc.invalidateQueries({ queryKey: ["models"] }); location.assign("/models"); } });
  const addRef = useMutation({ mutationFn: (sid: string) => api.post(`/api/models/${id}/references`, { segment_id: sid }), onSuccess: inv });
  const delRef = useMutation({ mutationFn: (rid: string) => api.del(`/api/models/${id}/references/${rid}`), onSuccess: inv });
  const m = q.data;
  if (!m) return null;
  const scores = new Map((m.metrics.checkpoints ?? []).map((c) => [c.name, c]));
  const rows = [{ name: "base", step: 0, epoch: 0, weights: false }, ...m.checkpoints];
  const lines = m.samples.lines ?? [];
  const shown = rows.filter((r) => r.name === "base" || r.weights || scores.has(r.name));
  // which clips each row has: from the scores when available, else what each engine's cloud script writes
  const kindsFor = (name: string) => {
    const sm = scores.get(name)?.summary;
    if (sm && Object.keys(sm).length) return Object.keys(sm);
    if (m.engine === "voxcpm2") return ["plain", "ref"];
    if (m.engine === "qwen3" && name === "base") return ["ref"];
    return ["plain"];
  };
  return (
    <div className="min-w-0 space-y-6">
      <Card>
        <div className="flex flex-wrap items-start gap-4">
          <div className="min-w-0 flex-1">
            {renaming ? (
              <div className="flex gap-2"><input className="input" value={name} onChange={(e) => setName(e.target.value)} autoFocus />
                <Button size="sm" onClick={() => { patch.mutate({ name }); setRenaming(false); }}>儲存</Button></div>
            ) : (
              <h2 className="flex items-center gap-2 text-xl font-semibold">{m.name}
                <button className="text-zinc-400 hover:text-zinc-600" onClick={() => { setName(m.name); setRenaming(true); }}><Pencil className="size-4" /></button></h2>
            )}
            <div className="mt-1 flex flex-wrap gap-x-3 gap-y-1 text-sm text-zinc-500">
              <span>{m.voice_name}</span><span>{m.engine_name}</span><span>{MODE_LABEL[m.meta.mode ?? ""] ?? m.meta.mode}</span>
              {m.meta.languages?.length ? <span>{m.meta.languages.map((l) => LANGS[l] ?? l).join("、")}</span> : null}
              {m.train_seconds ? <span>雲端 {fmtDur(m.train_seconds)}</span> : null}
              <span>{fmtTime(m.created_at)}</span>
            </div>
            {!m.available[0] && <p className="mt-2 text-sm text-amber-700 dark:text-amber-300">本機還不能用這個模型合成：{m.available[1]}。<Link to="/settings#engines" className="underline">去安裝</Link></p>}
          </div>
          <div className="flex gap-2">
            <Link to={`/speak?model=${m.id}`}><Button><Mic2 className="size-4" />用這個模型合成</Button></Link>
            <Button variant="ghost" onClick={() => confirm(`刪除模型「${m.name}」？檔案會一起刪除。`) && del.mutate()}><Trash2 className="size-4" /></Button>
          </div>
        </div>
      </Card>

      {m.checkpoints.length > 0 && (
        <Card title="檢查點比較" actions={<Button size="sm" variant="ghost" loading={evaluate.isPending} onClick={() => evaluate.mutate()}><RefreshCw className="size-3.5" />重新評分</Button>}>
          <p className="mb-3 text-sm text-zinc-500">
            <b>相似度</b>是聲紋模型算出的接近程度（不是百分比的「像幾成」）{m.metrics.baseline_sim != null && <>；本人不同錄音彼此約 {pct(m.metrics.baseline_sim)}，可以當參考基準</>}。
            <b>念對程度</b>是語音辨識聽到的和應該念的一致程度。「只用模型」才看得出訓練學到多少；「＋參考」的音色有一部分來自參考錄音，分開比較。
            推薦的是「只用模型」時，念對程度和最好的差不到 5 分的檢查點裡最像的。
          </p>
          {m.metrics.reason && <p className="mb-3 rounded-lg bg-amber-50 px-3 py-2 text-sm text-amber-800 dark:bg-amber-950/40 dark:text-amber-200">{m.metrics.reason}</p>}
          {m.metrics.improved_over_base === false && <p className="mb-3 rounded-lg bg-amber-50 px-3 py-2 text-sm text-amber-800 dark:bg-amber-950/40 dark:text-amber-200">推薦的檢查點沒有比訓練前更像。可能是資料太少或品質不夠，請先聽聽看，再考慮補資料重訓。</p>}
          {m.meta.sampling && m.meta.sampling !== "complete" && <p className="mb-3 text-sm text-amber-700">雲端試念沒有完成，部分檢查點沒有樣本。</p>}
          <div className="overflow-x-auto">
            <table className="w-full text-sm">
              <thead className="text-left text-xs text-zinc-500">
                <tr><th className="py-2">檢查點</th><th>epoch</th><th colSpan={2}>只用模型：相似度／念對</th><th colSpan={2}>＋參考：相似度／念對</th><th /></tr>
              </thead>
              <tbody>
                {shown.map((r) => {
                  const sc = scores.get(r.name)?.summary ?? {};
                  const using = m.meta.checkpoint === r.name;
                  return (
                    <tr key={r.name} className={clsx("border-t border-zinc-100 dark:border-zinc-800", using && "bg-brand-50/60 dark:bg-brand-900/10")}>
                      <td className="py-2 font-mono text-xs">{r.name === "base" ? "訓練前（基礎模型）" : r.name}
                        {m.metrics.recommended === r.name && <Badge tone="green"><Crown className="size-3" />推薦</Badge>}</td>
                      <td className="tabular-nums">{r.name === "base" ? "—" : r.epoch}</td>
                      <td className="tabular-nums">{pct(sc.plain?.sim)}</td>
                      <td className="tabular-nums">{pct(sc.plain?.agree)}</td>
                      <td className="tabular-nums text-zinc-500">{pct(sc.ref?.sim)}</td>
                      <td className="tabular-nums text-zinc-500">{pct(sc.ref?.agree)}</td>
                      <td className="text-right">
                        {r.weights ? (using ? <Badge tone="brand">使用中</Badge> : <Button size="sm" variant="secondary" onClick={() => patch.mutate({ checkpoint: r.name })}>使用這個</Button>)
                          : <span className="text-xs text-zinc-400">{r.name === "base" ? "對照用" : "只有樣本"}</span>}
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
          {!m.metrics.checkpoints && <p className="mt-2 text-xs text-zinc-500">評分中…（在工作佇列裡）</p>}
        </Card>
      )}

      {lines.length > 0 && (
        <Card title="試聽比較">
          <p className="mb-3 text-sm text-zinc-500">每一行是一句沒拿來訓練的真實錄音{lines.some((l) => l.seen) && "（資料太少，這幾句有用在訓練裡）"}。先聽「本人」，再聽各檢查點。「＋參考」是同時給模型一段參考錄音。</p>
          <div className="space-y-4">
            {lines.map((ln, i) => (
              <div key={ln.id} className="rounded-xl border border-zinc-200 p-3 dark:border-zinc-800">
                <div className="mb-2 text-sm">{ln.text} <span className="text-xs text-zinc-400">{LANGS[ln.lang] ?? ln.lang}</span></div>
                <div className="flex flex-wrap gap-1.5">
                  <PlayButton player={player} url={`/api/segments/${ln.id}/audio`} label="本人" />
                  {shown.map((r) => kindsFor(r.name).map((k) => (
                    <PlayButton key={r.name + k} small player={player} url={`/api/models/${m.id}/samples/${r.name}/${i}_${k}.wav`}
                      label={`${r.name === "base" ? "訓練前" : `ep ${r.epoch}`}${k === "ref" ? "＋參考" : ""}`} />
                  )))}
                </div>
              </div>
            ))}
          </div>
        </Card>
      )}

      <Card title="參考片段" actions={<Button size="sm" variant="secondary" onClick={() => setPicking(true)}><Plus className="size-3.5" />加入</Button>}>
        <p className="mb-3 text-sm text-zinc-500">「參考音色」和「完整複製」模式會用到。準備幾種情緒（平靜、開心、小聲…）各一段，合成時挑最接近想要語氣的那段，效果最好。5–12 秒、乾淨、文字正確的片段最好。</p>
        {!m.meta.references?.length ? <Empty title="還沒有參考片段" /> : (
          <ul className="space-y-2">
            {m.meta.references.map((r) => (
              <li key={r.id} className="flex items-center gap-3 rounded-lg bg-zinc-50 px-3 py-2 text-sm dark:bg-zinc-800/50">
                <PlayButton player={player} url={`/api/models/${m.id}/references/${r.id}/audio`} />
                <div className="min-w-0 flex-1"><div className="truncate">{r.text || "（沒有逐字稿：不能用完整複製）"}</div><div className="text-xs text-zinc-500">{r.label}</div></div>
                <button className="text-zinc-400 hover:text-red-500" onClick={() => delRef.mutate(r.id)}><Trash2 className="size-4" /></button>
              </li>
            ))}
          </ul>
        )}
        <ErrorText error={addRef.error} />
      </Card>
      {picking && <SegmentPicker voiceId={m.voice_id} title="選一段當參考" onClose={() => setPicking(false)} onPick={(ids) => { ids.forEach((s) => addRef.mutate(s)); setPicking(false); }} />}
    </div>
  );
}

export function SegmentPicker({ voiceId, title, onClose, onPick, multi }: {
  voiceId: string; title: string; onClose: () => void; onPick: (ids: string[]) => void; multi?: boolean;
}) {
  const [q, setQ] = useState("");
  const [sel, setSel] = useState<string[]>([]);
  const player = usePlayer();
  const segs = useQuery({
    queryKey: ["picker", voiceId, q],
    queryFn: () => api.get<{ items: Segment[] }>(`/api/segments?voice_id=${voiceId}&status=approved&limit=60&q=${encodeURIComponent(q)}`),
  });
  const items = (segs.data?.items ?? []).slice().sort((a, b) => Number(b.duration >= 5 && b.duration <= 12) - Number(a.duration >= 5 && a.duration <= 12));
  return (
    <Modal open onClose={onClose} title={title} wide>
      <input className="input mb-3" placeholder="搜尋文字（例如想要的語氣會出現的字）" value={q} onChange={(e) => setQ(e.target.value)} />
      <div className="max-h-[50vh] space-y-1.5 overflow-y-auto">
        {items.map((s) => (
          <label key={s.id} className={clsx("flex cursor-pointer items-center gap-3 rounded-lg px-3 py-2 text-sm", sel.includes(s.id) ? "bg-brand-50 dark:bg-brand-900/20" : "hover:bg-zinc-50 dark:hover:bg-zinc-800/50")}>
            <input type={multi ? "checkbox" : "radio"} checked={sel.includes(s.id)}
              onChange={() => setSel(multi ? (sel.includes(s.id) ? sel.filter((x) => x !== s.id) : [...sel, s.id]) : [s.id])} />
            <PlayButton player={player} url={`/api/segments/${s.id}/audio`} small />
            <span className="min-w-0 flex-1 truncate">{s.text}</span>
            <span className="shrink-0 text-xs text-zinc-500">{s.duration.toFixed(1)} 秒</span>
          </label>
        ))}
        {!items.length && <Empty title="沒有已核可的片段" />}
      </div>
      <div className="mt-4 flex justify-end gap-2">
        <Button variant="ghost" onClick={onClose}>取消</Button>
        <Button disabled={!sel.length} onClick={() => onPick(sel)}>確定（{sel.length}）</Button>
      </div>
    </Modal>
  );
}

function ZeroShotModal({ onClose, onCreated }: { onClose: () => void; onCreated: (m: Model) => void }) {
  const qc = useQueryClient();
  const voices = useQuery({ queryKey: ["voices"], queryFn: () => api.get<Voice[]>("/api/voices") });
  const engines = useQuery({ queryKey: ["engines"], queryFn: () => api.get<EngineInfo[]>("/api/engines") });
  const ok = (voices.data ?? []).filter((v) => v.consent_ok);
  const [voiceId, setVoiceId] = useState("");
  const [engine, setEngine] = useState("voxcpm2");
  const [segs, setSegs] = useState<string[]>([]);
  const [picking, setPicking] = useState(false);
  useEffect(() => { if (!voiceId && ok.length) setVoiceId(ok[0].id); }, [ok, voiceId]);
  const create = useMutation({
    mutationFn: () => api.post<Model>("/api/models/zeroshot", { voice_id: voiceId, engine, segment_ids: segs }),
    onSuccess: (m) => { qc.invalidateQueries({ queryKey: ["models"] }); onCreated(m); },
  });
  return (
    <Modal open onClose={onClose} title="建立免訓練模型">
      <p className="mb-4 text-sm text-zinc-500">用基礎模型＋幾段參考錄音直接合成。不用租 GPU，適合先試聽引擎、或資料還不夠時先用；但口音和說話習慣只能抓到一部分，要「完美複製」還是需要訓練。</p>
      {!ok.length ? <Empty title="沒有已同意的聲音" /> : (
        <div className="space-y-4">
          <Field label="聲音"><select className="input" value={voiceId} onChange={(e) => { setVoiceId(e.target.value); setSegs([]); }}>{ok.map((v) => <option key={v.id} value={v.id}>{v.name}</option>)}</select></Field>
          <Field label="引擎"><select className="input" value={engine} onChange={(e) => setEngine(e.target.value)}>
            {engines.data?.map((e) => <option key={e.id} value={e.id}>{e.name}{e.available ? "" : "（本機尚未安裝）"}</option>)}</select></Field>
          <Field label="參考片段（1–5 段）"><Button variant="secondary" onClick={() => setPicking(true)}>選片段（已選 {segs.length}）</Button></Field>
          <ErrorText error={create.error} />
          <Button className="w-full" disabled={!segs.length} loading={create.isPending} onClick={() => create.mutate()}>建立</Button>
        </div>
      )}
      {picking && <SegmentPicker voiceId={voiceId} title="選參考片段" multi onClose={() => setPicking(false)} onPick={(ids) => { setSegs(ids.slice(0, 5)); setPicking(false); }} />}
    </Modal>
  );
}

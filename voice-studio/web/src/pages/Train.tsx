import { useEffect, useMemo, useState } from "react";
import { Link, useSearchParams } from "react-router";
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import clsx from "clsx";
import { AlertTriangle, Cloud, Cpu, FileText, Sparkles, Square } from "lucide-react";
import {
  api, fmtDur, fmtMin, fmtTime, fmtUsd, type Dataset, type EngineInfo, type GpuOffer, type Orphan, type Plan, type Training, type Voice,
} from "../api";
import { Badge, Button, Card, Empty, ErrorText, Field, Modal, PageHeader, Progress } from "../ui";

const STATUS: Record<string, [string, "zinc" | "green" | "amber" | "red" | "brand" | "blue"]> = {
  queued: ["排隊中", "zinc"], uploading: ["上傳資料", "blue"], starting: ["啟動 GPU", "blue"], running: ["雲端訓練中", "brand"],
  downloading: ["下載模型", "blue"], done: ["完成", "green"], failed: ["失敗", "red"], canceled: ["已取消", "zinc"],
};

export default function Train() {
  const [sp] = useSearchParams();
  const settings = useQuery({ queryKey: ["settings"], queryFn: () => api.get<{ secrets: Record<string, boolean>; settings: Record<string, unknown> }>("/api/settings") });
  const trainings = useQuery({ queryKey: ["trainings"], queryFn: () => api.get<Training[]>("/api/training"), refetchInterval: 5000 });
  const s = settings.data;
  const cloudReady = !!s && s.secrets.runpod_api_key && s.secrets.runpod_s3_access_key && s.secrets.runpod_s3_secret_key && !!s.settings.runpod_volume_id && !!s.settings.runpod_datacenter;
  const [logFor, setLogFor] = useState<Training | null>(null);
  return (
    <div>
      <PageHeader title="雲端訓練"
        subtitle="在 RunPod 租一張 GPU 幫你微調模型。平台會自動上傳資料、開機、安裝、訓練、讓每個檢查點試念、打包下載，最後自動關機，不會忘記關而一直計費。" />
      {s && !cloudReady && (
        <div className="mb-6 flex items-start gap-3 rounded-xl border border-amber-300 bg-amber-50 px-4 py-3 text-sm text-amber-800 dark:border-amber-800 dark:bg-amber-950/40 dark:text-amber-200">
          <AlertTriangle className="mt-0.5 size-4 shrink-0" />
          <div>還沒設定 RunPod。到 <Link to="/settings" className="font-medium underline">設定 → 雲端 GPU</Link> 填入 API 金鑰、S3 金鑰和網路磁碟（Network Volume），大約 10 分鐘。<Link to="/guide/04-cloud" className="underline">看圖文教學</Link></div>
        </div>
      )}
      {cloudReady && <Orphans />}
      <NewTraining initialDataset={sp.get("dataset") ?? ""} cloudReady={!!cloudReady} />
      <Card title="訓練紀錄" className="mt-6">
        {!trainings.data?.length ? <Empty icon={<Cloud className="size-8" />} title="還沒有訓練" /> : (
          <div className="space-y-3">
            {trainings.data.map((t) => <TrainingRow key={t.id} t={t} onLog={() => setLogFor(t)} />)}
          </div>
        )}
      </Card>
      {logFor && <LogModal t={logFor} onClose={() => setLogFor(null)} />}
    </div>
  );
}

function NewTraining({ initialDataset, cloudReady }: { initialDataset: string; cloudReady: boolean }) {
  const qc = useQueryClient();
  const voices = useQuery({ queryKey: ["voices"], queryFn: () => api.get<Voice[]>("/api/voices") });
  const datasets = useQuery({ queryKey: ["datasets"], queryFn: () => api.get<Dataset[]>("/api/datasets") });
  const engines = useQuery({ queryKey: ["engines"], queryFn: () => api.get<EngineInfo[]>("/api/engines") });
  const gpus = useQuery({ queryKey: ["gpus", cloudReady], queryFn: () => api.get<GpuOffer[]>("/api/cloud/gpus"), staleTime: 120000 });
  const [dsId, setDsId] = useState(initialDataset);
  const [engineId, setEngineId] = useState("voxcpm2");
  const [presetId, setPresetId] = useState("");
  const [gpu, setGpu] = useState("");
  const [name, setName] = useState("");
  const [epochs, setEpochs] = useState<string>("");
  const [ack, setAck] = useState(false);
  const engine = engines.data?.find((e) => e.id === engineId);
  const preset = engine?.presets.find((p) => p.id === presetId) ?? engine?.presets[0];
  useEffect(() => { if (!dsId && datasets.data?.length) setDsId(datasets.data[0].id); }, [datasets.data, dsId]);
  useEffect(() => { setPresetId(engine?.presets.find((p) => p.recommended)?.id ?? engine?.presets[0]?.id ?? ""); }, [engineId, engine]);
  useEffect(() => { setGpu(preset?.gpu[0] ?? ""); setAck(false); setEpochs(""); }, [preset?.id, engineId]);
  const overrides = epochs && Number(epochs) > 0 ? { epochs: Number(epochs) } : null;
  const offers = useMemo(() => {
    const live = new Map((gpus.data ?? []).map((g) => [g.id, g]));
    return (preset?.gpu ?? []).map((id) => live.get(id) ?? { id, label: id.replace("NVIDIA ", ""), vram: 0, usd_h: null, availability: null });
  }, [gpus.data, preset]);
  const offer = offers.find((o) => o.id === gpu);
  const plan = useQuery({
    queryKey: ["plan", dsId, engineId, preset?.id, gpu, offer?.usd_h, epochs],
    queryFn: () => api.post<Plan>("/api/training/plan", { dataset_id: dsId, engine: engineId, preset: preset!.id, gpu, usd_h: offer?.usd_h ?? null, params: overrides }),
    enabled: !!dsId && !!preset && !!gpu,
  });
  const start = useMutation({
    mutationFn: () => api.post<Training>("/api/training", { dataset_id: dsId, engine: engineId, preset: preset!.id, gpu, name, usd_h: offer?.usd_h ?? null, params: overrides }),
    onSuccess: () => { qc.invalidateQueries({ queryKey: ["trainings"] }); setAck(false); },
  });
  const vname = (id: string) => voices.data?.find((v) => v.id === id)?.name ?? "?";
  if (datasets.data && !datasets.data.length)
    return <Card title="開始新的訓練"><Empty icon={<Sparkles className="size-8" />} title="還沒有訓練資料集">到 <Link to="/review" className="underline">檢查資料</Link> 核可片段後，按「建立新的資料集」。</Empty></Card>;
  return (
    <Card title="開始新的訓練">
      <div className="grid gap-6 lg:grid-cols-2">
        <div className="space-y-5">
          <Field label="1. 訓練資料集">
            <select className="input" value={dsId} onChange={(e) => setDsId(e.target.value)}>
              {datasets.data?.map((d) => <option key={d.id} value={d.id}>{vname(d.voice_id)} · {d.name}（{fmtMin(d.hours * 60)}，{d.n_items} 段）</option>)}
            </select>
          </Field>
          <div>
            <span className="label">2. 引擎</span>
            <div className="grid gap-2">
              {engines.data?.map((e) => (
                <button key={e.id} onClick={() => setEngineId(e.id)}
                  className={clsx("rounded-xl border p-3 text-left transition", engineId === e.id ? "border-brand-500 ring-2 ring-brand-500/20" : "border-zinc-200 hover:border-brand-300 dark:border-zinc-800")}>
                  <div className="flex items-center gap-2 font-medium">{e.name}
                    {e.id === "voxcpm2" && <Badge tone="brand">推薦</Badge>}{e.id === "mock" && <Badge>測試流程用</Badge>}
                    <span className="ml-auto text-xs font-normal text-zinc-500">{e.license}</span></div>
                  <p className="mt-1 text-xs leading-5 text-zinc-500">{e.summary}</p>
                </button>
              ))}
            </div>
          </div>
          {engine && (
            <div>
              <span className="label">3. 訓練方式</span>
              <div className="grid gap-2">
                {engine.presets.map((p) => (
                  <label key={p.id} className={clsx("flex cursor-pointer gap-3 rounded-xl border p-3", preset?.id === p.id ? "border-brand-500 bg-brand-50/50 dark:bg-brand-900/10" : "border-zinc-200 dark:border-zinc-800")}>
                    <input type="radio" className="mt-1" checked={preset?.id === p.id} onChange={() => setPresetId(p.id)} />
                    <div><div className="text-sm font-medium">{p.label}</div><p className="mt-0.5 text-xs leading-5 text-zinc-500">{p.description}</p></div>
                  </label>
                ))}
              </div>
            </div>
          )}
        </div>
        <div className="space-y-5">
          <Field label="4. 雲端 GPU" hint="價格是 RunPod Secure Cloud 每小時價格（網路磁碟只能用 Secure Cloud）。平台只會租你選的這一張，不會偷偷換成更貴的卡；沒貨時會告訴你，換一張再按一次就好。">
            <div className="grid gap-2">
              {offers.map((o) => (
                <label key={o.id} className={clsx("flex cursor-pointer items-center gap-3 rounded-lg border px-3 py-2 text-sm", gpu === o.id ? "border-brand-500" : "border-zinc-200 dark:border-zinc-800")}>
                  <input type="radio" checked={gpu === o.id} onChange={() => setGpu(o.id)} />
                  <Cpu className="size-4 text-zinc-400" />
                  <span className="flex-1">{o.label}{o.vram ? ` · ${o.vram} GB` : ""}</span>
                  {o.availability && <Badge tone={o.availability === "High" ? "green" : o.availability === "Low" ? "amber" : "zinc"}>{o.availability === "High" ? "充足" : o.availability === "Medium" ? "普通" : o.availability === "Low" ? "很少" : o.availability}</Badge>}
                  <span className="tabular-nums text-zinc-600 dark:text-zinc-300">{o.usd_h != null ? `$${o.usd_h.toFixed(2)}/時` : ""}</span>
                </label>
              ))}
            </div>
          </Field>
          <Field label="模型名稱（選填）"><input className="input" value={name} onChange={(e) => setName(e.target.value)} placeholder="例如：我的聲音 v1" /></Field>
          {preset?.params.epochs != null && (
            <details className="rounded-lg border border-zinc-200 px-3 py-2 text-sm dark:border-zinc-800">
              <summary className="cursor-pointer text-zinc-600 dark:text-zinc-300">進階設定</summary>
              <div className="mt-3">
                <Field label={`epoch 數（預設 ${String(preset.params.epochs)}）`}
                  hint="整份資料要看幾遍。官方建議單一說話者 1–3 遍就夠，太多容易「背答案」。途中會存好幾個檢查點，之後在模型頁比較。">
                  <input className="input w-32" type="number" min={0.25} max={10} step={0.25} value={epochs}
                    placeholder={String(preset.params.epochs)} onChange={(e) => setEpochs(e.target.value)} />
                </Field>
              </div>
            </details>
          )}
          {plan.data && (
            <div className="rounded-xl bg-zinc-50 p-4 text-sm dark:bg-zinc-800/50">
              <div className="grid grid-cols-2 gap-3">
                <div><div className="text-xs text-zinc-500">預估時間</div><div className="text-lg font-semibold">{plan.data.estimate_hours.toFixed(1)} 小時</div></div>
                <div><div className="text-xs text-zinc-500">預估費用</div><div className="text-lg font-semibold">{fmtUsd(plan.data.estimate_usd)}</div></div>
                <div><div className="text-xs text-zinc-500">訓練步數</div><div>{plan.data.steps || "—"}（{plan.data.n_train} 段{plan.data.epochs_effective ? `，約 ${plan.data.epochs_effective} epoch` : ""}）</div></div>
                <div><div className="text-xs text-zinc-500">最多（時數上限）</div><div>{plan.data.max_hours} 小時 · {fmtUsd(plan.data.max_usd)}</div></div>
              </div>
              <p className="mt-3 text-xs text-zinc-500">
                {plan.data.estimate_basis === "measured" ? "這個估計用的是你上次在同一張 GPU 上實際量到的速度。" : "第一次是粗估；跑完一次後平台會用實際速度校正。"}
                網路磁碟另計（約 $0.07/GB/月）。
              </p>
              {plan.data.blocked && <p className="mt-2 flex gap-1.5 text-xs font-medium text-red-600"><AlertTriangle className="mt-0.5 size-3.5 shrink-0" />{plan.data.blocked}</p>}
              {plan.data.warnings.map((w) => <p key={w} className="mt-2 flex gap-1.5 text-xs text-amber-700 dark:text-amber-300"><AlertTriangle className="mt-0.5 size-3.5 shrink-0" />{w}</p>)}
            </div>
          )}
          <ErrorText error={plan.error} />
          <label className="flex items-start gap-2 text-sm">
            <input type="checkbox" className="mt-1" checked={ack} onChange={(e) => setAck(e.target.checked)} />
            <span>我了解這會用我的 RunPod 帳號租 GPU 並計費；訓練完成、失敗、取消或達到時數上限時，平台會自動關機。</span>
          </label>
          <Button className="w-full" onClick={() => start.mutate()} loading={start.isPending} disabled={!ack || !cloudReady || !plan.data || !!plan.data.blocked}>
            <Cloud className="size-4" />開始雲端訓練
          </Button>
          <ErrorText error={start.error} />
        </div>
      </div>
    </Card>
  );
}

function TrainingRow({ t, onLog }: { t: Training; onLog: () => void }) {
  const qc = useQueryClient();
  const cancel = useMutation({ mutationFn: () => api.post(`/api/training/${t.id}/cancel`), onSuccess: () => qc.invalidateQueries({ queryKey: ["trainings"] }) });
  const [label, tone] = STATUS[t.status] ?? [t.status, "zinc"];
  const active = !["done", "failed", "canceled"].includes(t.status);
  const p = t.progress ?? {};
  const voice = useQuery({ queryKey: ["voices"], queryFn: () => api.get<Voice[]>("/api/voices") }).data?.find((v) => v.id === t.voice_id);
  const model = useQuery({ queryKey: ["models"], queryFn: () => api.get<{ id: string; training_id: string | null }[]>("/api/models"), enabled: t.status === "done" })
    .data?.find((m) => m.training_id === t.id);
  return (
    <div className="rounded-xl border border-zinc-200 p-4 dark:border-zinc-800">
      <div className="flex flex-wrap items-center gap-2">
        <span className="font-medium">{t.preset.name || `${voice?.name ?? ""} · ${t.engine}`}</span>
        <Badge tone={tone}>{label}</Badge>
        <span className="text-xs text-zinc-500">{t.engine} / {t.preset.id} · {p.gpu_name ?? t.gpu.replace("NVIDIA ", "")} · {fmtTime(t.created_at)}</span>
        <div className="ml-auto flex gap-2">
          <Button size="sm" variant="ghost" onClick={onLog}><FileText className="size-3.5" />紀錄</Button>
          {active && <Button size="sm" variant="danger" loading={cancel.isPending} onClick={() => confirm("停止這次訓練並關閉雲端機器？已經花的費用不會退回。") && cancel.mutate()}><Square className="size-3.5" />停止</Button>}
          {model && <Link to={`/models?id=${model.id}`}><Button size="sm">試聽模型</Button></Link>}
        </div>
      </div>
      {active && t.job && (
        <div className="mt-3">
          <div className="mb-1 flex justify-between text-xs text-zinc-500"><span>{t.job.message}</span><span>{Math.round(t.job.progress * 100)}%</span></div>
          <Progress value={t.job.progress} />
        </div>
      )}
      <div className="mt-2 flex flex-wrap gap-x-4 gap-y-1 text-xs text-zinc-500">
        {p.wall_s != null && <span>已執行 {fmtDur(p.wall_s)}</span>}
        {p.epoch != null && <span>epoch {p.epoch}</span>}
        {p.loss != null && <span>訓練 loss {p.loss.toFixed(3)}</span>}
        {p.val_loss != null && <span>驗證 loss {p.val_loss.toFixed(3)}</span>}
        {p.s_per_step != null && <span>{p.s_per_step.toFixed(1)} 秒/步</span>}
        <span>預估 {fmtUsd(t.cost_estimate)}</span>
        {t.cost_per_hr != null && <span>實際 ${t.cost_per_hr.toFixed(2)}/時</span>}
        {t.status === "failed" && t.job?.message && <span className="text-red-600">{t.job.message}</span>}
      </div>
      {t.note && <p className="mt-2 text-xs text-amber-700 dark:text-amber-300">{t.note}</p>}
      {t.pod_state === "remove_failed" && (
        <p className="mt-2 flex items-center gap-2 text-xs font-medium text-red-600"><AlertTriangle className="size-3.5" />
          雲端機器可能還在計費。平台會在下次開啟時自動再刪一次；也可以馬上到 runpod.io → Pods 手動刪除。</p>
      )}
    </div>
  );
}

function LogModal({ t, onClose }: { t: Training; onClose: () => void }) {
  const q = useQuery({ queryKey: ["training", t.id], queryFn: () => api.get<Training>(`/api/training/${t.id}`), refetchInterval: 10000 });
  return (
    <Modal open onClose={onClose} title="訓練紀錄" wide>
      <p className="mb-2 text-xs text-zinc-500">雲端機器上的完整輸出（每 10 秒更新）。遇到問題時，把最後幾十行貼給 Claude 或 GPT 問就好，裡面不含任何金鑰。</p>
      <pre className="max-h-[60vh] overflow-auto rounded-xl bg-zinc-950 p-4 text-[11px] leading-5 whitespace-pre-wrap text-zinc-200">{q.data?.log || "（還沒有輸出）"}</pre>
    </Modal>
  );
}

function Orphans() {
  const qc = useQueryClient();
  const reap = useQuery({ queryKey: ["reap"], queryFn: () => api.post<{ removed: string[]; orphans: Orphan[]; error?: string }>("/api/cloud/reap"),
    refetchInterval: 300000, staleTime: 60000 });
  const remove = useMutation({ mutationFn: (id: string) => api.post(`/api/cloud/pods/${id}/remove`), onSuccess: () => qc.invalidateQueries({ queryKey: ["reap"] }) });
  const orphans = reap.data?.orphans ?? [];
  if (!orphans.length && !reap.data?.removed.length) return null;
  return (
    <div className="mb-6 rounded-xl border border-red-300 bg-red-50 px-4 py-3 text-sm text-red-800 dark:border-red-900 dark:bg-red-950/40 dark:text-red-200">
      {reap.data?.removed.length ? <p>已自動關掉 {reap.data.removed.length} 台沒有在用的雲端機器。</p> : null}
      {orphans.length > 0 && (
        <>
          <p className="font-medium">你的 RunPod 帳號上有 {orphans.length} 台 Voice Studio 開的機器，不屬於任何進行中的訓練（可能還在計費）：</p>
          <ul className="mt-2 space-y-1">{orphans.map((o) => (
            <li key={o.id} className="flex items-center gap-2"><code className="kbd">{o.name}</code>{o.cost_per_hr ? <span>${o.cost_per_hr}/時</span> : null}
              <Button size="sm" variant="danger" loading={remove.isPending && remove.variables === o.id}
                onClick={() => confirm(`刪除雲端機器 ${o.name}？`) && remove.mutate(o.id)}>刪除</Button></li>))}</ul>
          <ErrorText error={remove.error} />
        </>
      )}
    </div>
  );
}

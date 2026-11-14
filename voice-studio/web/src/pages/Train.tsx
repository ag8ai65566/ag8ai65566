import { useEffect, useMemo, useState } from "react";
import { Link, useSearchParams } from "react-router";
import { useMutation, useQuery, useQueryClient, type UseQueryResult } from "@tanstack/react-query";
import clsx from "clsx";
import { AlertTriangle, Cloud, Cpu, FileText, FolderSync, RefreshCw, Sparkles, Square, Trash2 } from "lucide-react";
import {
  api, fmtDur, fmtMin, fmtTime, fmtUsd, inStock, type CloudCheck, type ColabStatus, type Dataset, type EngineInfo, type GpuOffer, type GpuOffers,
  type Orphan, type Plan, type Training, type Voice,
} from "../api";
import { Badge, Button, Card, Empty, ErrorText, Field, Modal, PageHeader, Progress } from "../ui";

const STATUS: Record<string, [string, "zinc" | "green" | "amber" | "red" | "brand" | "blue"]> = {
  queued: ["排隊中", "zinc"], starting: ["準備、租用 GPU", "blue"], uploading: ["已租到 GPU，上傳資料", "blue"], running: ["雲端訓練中", "brand"],
  waiting: ["等你在 Colab 執行", "amber"], waiting_gpu: ["等 GPU 有貨", "amber"],
  downloading: ["下載模型", "blue"], splitting: ["雲端切檔中", "blue"], done: ["完成", "green"], failed: ["失敗", "red"], canceled: ["已取消", "zinc"],
};

const STOCK: Record<string, [string, "green" | "blue" | "amber" | "red"]> = {
  HIGH: ["充足", "green"], MEDIUM: ["普通", "blue"], LOW: ["很少", "amber"], NONE: ["沒貨", "red"],
};

function useGpuOffers(engine: string | undefined, preset: string | undefined, enabled: boolean) {
  return useQuery({
    queryKey: ["gpus", engine, preset],
    queryFn: () => api.get<GpuOffers>(`/api/cloud/gpus?engine=${encodeURIComponent(engine!)}&preset=${encodeURIComponent(preset!)}`),
    enabled: enabled && !!engine && !!preset, staleTime: 60000,
  });
}

/** Keeps the selection on a card that can be rented: the server's default when nothing (or a sold-out card) is chosen. */
function useRentableChoice(gpus: UseQueryResult<GpuOffers>, gpu: string, setGpu: (id: string) => void) {
  useEffect(() => {
    const d = gpus.data;
    if (!d) return;
    const cur = d.offers.find((o) => o.id === gpu);
    if (!cur || (d.live && !inStock(cur))) setGpu(d.default ?? d.offers[0]?.id ?? "");
  }, [gpus.data, gpu]);
}

/** One card (value/onChange), or for auto-grab several (picked/onToggle): then sold-out cards can be ticked too. */
function GpuPicker({ q, value, onChange, picked, onToggle }: {
  q: UseQueryResult<GpuOffers>; value: string; onChange: (id: string) => void;
  picked?: string[]; onToggle?: (id: string) => void;
}) {
  const multi = !!picked && !!onToggle;
  const d = q.data;
  const checked = d?.live ? `${d.datacenter ?? "所有資料中心"} 的即時庫存，${new Date(q.dataUpdatedAt).toLocaleTimeString("zh-TW", { hour: "2-digit", minute: "2-digit" })} 查詢` : "";
  return (
    <div className="grid gap-2">
      <div className="flex items-center gap-2 text-xs text-zinc-500">
        <span>{q.isLoading ? "正在查詢 RunPod 的庫存…" : checked}</span>
        <Button size="sm" variant="ghost" className="ml-auto" loading={q.isFetching} onClick={() => q.refetch()}><RefreshCw className="size-3.5" />重新查詢</Button>
      </div>
      {d && !d.live && (
        <p className="flex gap-1.5 text-xs text-amber-700 dark:text-amber-300"><AlertTriangle className="mt-0.5 size-3.5 shrink-0" />
          讀不到 RunPod 的即時庫存（{d.error}）。下面是內建清單，沒辦法確定有沒有貨。</p>
      )}
      {d?.live && !d.offers.some(inStock) && !multi && (
        <p className="flex gap-1.5 text-xs font-medium text-red-600"><AlertTriangle className="mt-0.5 size-3.5 shrink-0" />
          這個訓練方式能用的卡，在 {d.datacenter} 現在都沒貨。可以勾下面的「沒貨時自動搶卡」，有貨時自動開始；或在 RunPod 其他資料中心建立網路磁碟，再到設定改用它。</p>
      )}
      {multi && <p className="text-xs text-zinc-500">勾選可以接受的卡。有貨時會租勾選的卡裡最便宜、有貨的那張。</p>}
      {(d?.offers ?? []).map((o) => {
        const soldOut = d!.live && !inStock(o);
        const on = multi ? picked!.includes(o.id) : value === o.id;
        const stock = o.availability ? STOCK[o.availability] : undefined;
        return (
          <label key={o.id} className={clsx("flex items-center gap-3 rounded-lg border px-3 py-2 text-sm",
            soldOut && !multi ? "cursor-not-allowed opacity-50" : "cursor-pointer", soldOut && multi && !on && "opacity-70",
            on ? "border-brand-500" : "border-zinc-200 dark:border-zinc-800")}>
            {multi ? <input type="checkbox" checked={on} onChange={() => onToggle!(o.id)} />
              : <input type="radio" disabled={soldOut} checked={on} onChange={() => onChange(o.id)} />}
            <Cpu className="size-4 text-zinc-400" />
            <span className="flex-1">{o.label}{o.vram ? ` · ${o.vram} GB` : ""}
              {!o.recommended && <span className="ml-2 text-xs text-zinc-500">記憶體夠，也能用</span>}</span>
            {stock && <Badge tone={stock[1]}>{stock[0]}</Badge>}
            <span className="tabular-nums text-zinc-600 dark:text-zinc-300">{o.usd_h != null ? `$${o.usd_h.toFixed(2)}/時` : ""}</span>
          </label>
        );
      })}
    </div>
  );
}

export default function Train() {
  const [sp] = useSearchParams();
  const settings = useQuery({ queryKey: ["settings"], queryFn: () => api.get<{ secrets: Record<string, boolean>; settings: Record<string, unknown> }>("/api/settings") });
  const trainings = useQuery({ queryKey: ["trainings"], queryFn: () => api.get<Training[]>("/api/training"), refetchInterval: 5000 });
  const s = settings.data;
  const cloudReady = !!s && s.secrets.runpod_api_key && s.secrets.runpod_s3_access_key && s.secrets.runpod_s3_secret_key && !!s.settings.runpod_volume_id && !!s.settings.runpod_datacenter;
  const colab = useQuery({ queryKey: ["colab"], queryFn: () => api.get<ColabStatus>("/api/colab/status") });
  const colabReady = !!colab.data?.ok;
  const check = useQuery({ queryKey: ["cloudcheck"], queryFn: () => api.get<CloudCheck>("/api/cloud/check"),
    enabled: !!cloudReady, staleTime: 60000, retry: false });
  const volumeProblem = (check.data?.ok && check.data.problem) || "";
  const [logFor, setLogFor] = useState<Training | null>(null);
  return (
    <div>
      <PageHeader title="雲端訓練"
        subtitle="用雲端 GPU 微調模型：在 RunPod 租一張（全自動，付費），或用 Google AI 方案附的 Colab 運算單位（要自己在 Colab 按執行）。訓練完會自動下載、讓每個檢查點試念並評分。" />
      {s && !cloudReady && !colabReady && (
        <div className="mb-6 flex items-start gap-3 rounded-xl border border-amber-300 bg-amber-50 px-4 py-3 text-sm text-amber-800 dark:border-amber-800 dark:bg-amber-950/40 dark:text-amber-200">
          <AlertTriangle className="mt-0.5 size-4 shrink-0" />
          <div>還沒設定雲端訓練。二選一：到 <Link to="/settings" className="font-medium underline">設定 → 雲端 GPU</Link> 填入 RunPod 的金鑰和網路磁碟（<Link to="/guide/04-cloud" className="underline">教學</Link>），或到 <Link to="/settings#colab" className="font-medium underline">設定 → Google Colab</Link> 選雲端硬碟資料夾（<Link to="/guide/11-colab" className="underline">教學</Link>）。</div>
        </div>
      )}
      {volumeProblem && (
        <div className="mb-6 flex items-start gap-3 rounded-xl border border-red-300 bg-red-50 px-4 py-3 text-sm text-red-800 dark:border-red-900 dark:bg-red-950/40 dark:text-red-200">
          <AlertTriangle className="mt-0.5 size-4 shrink-0" />
          <div>RunPod 現在不能訓練：{volumeProblem} <Link to="/settings" className="font-medium underline">設定 → 雲端 GPU</Link></div>
        </div>
      )}
      {cloudReady && <Orphans />}
      <NewTraining initialDataset={sp.get("dataset") ?? ""} cloudReady={!!cloudReady} colabReady={colabReady} volumeProblem={volumeProblem} />
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

function NewTraining({ initialDataset, cloudReady, colabReady, volumeProblem }: { initialDataset: string; cloudReady: boolean; colabReady: boolean; volumeProblem: string }) {
  const qc = useQueryClient();
  const voices = useQuery({ queryKey: ["voices"], queryFn: () => api.get<Voice[]>("/api/voices") });
  const datasets = useQuery({ queryKey: ["datasets"], queryFn: () => api.get<Dataset[]>("/api/datasets") });
  const engines = useQuery({ queryKey: ["engines"], queryFn: () => api.get<EngineInfo[]>("/api/engines") });
  const [dsId, setDsId] = useState(initialDataset);
  const [engineId, setEngineId] = useState("voxcpm2");
  const [presetId, setPresetId] = useState("");
  const [gpu, setGpu] = useState("");
  const [name, setName] = useState("");
  const [epochs, setEpochs] = useState<string>("");
  const [ack, setAck] = useState(false);
  const [target, setTarget] = useState<"runpod" | "colab">("runpod");
  useEffect(() => { if (colabReady && !cloudReady) setTarget("colab"); }, [colabReady, cloudReady]);
  const engine = engines.data?.find((e) => e.id === engineId);
  const preset = engine?.presets.find((p) => p.id === presetId) ?? engine?.presets[0];
  useEffect(() => { if (!dsId && datasets.data?.length) setDsId(datasets.data[0].id); }, [datasets.data, dsId]);
  useEffect(() => { setPresetId(engine?.presets.find((p) => p.recommended)?.id ?? engine?.presets[0]?.id ?? ""); }, [engineId, engine]);
  useEffect(() => { setGpu(preset?.gpu[0] ?? ""); setAck(false); setEpochs(""); }, [preset?.id, engineId]);
  const overrides = epochs && Number(epochs) > 0 ? { epochs: Number(epochs) } : null;
  const gpus = useGpuOffers(engineId, preset?.id, cloudReady && target === "runpod");
  useRentableChoice(gpus, gpu, setGpu);
  const offers = useMemo<GpuOffer[]>(() => gpus.data?.offers
    ?? (preset?.gpu ?? []).map((id) => ({ id, label: id.replace("NVIDIA ", ""), vram: 0, usd_h: null, recommended: true, availability: null })),
  [gpus.data, preset]);
  // auto-grab: wait (renting nothing) until one of the ticked cards is in stock; tried cheapest first
  const [grab, setGrab] = useState(false);
  const [picked, setPicked] = useState<string[]>([]);
  const [waitHours, setWaitHours] = useState(12);
  // the training method's recommended cards are ticked once its list is known (also when it loads after the tick)
  const recommendedIds = useMemo(() => (gpus.data?.offers ?? []).filter((o) => o.recommended).map((o) => o.id).join("|"), [gpus.data]);
  useEffect(() => { setPicked(grab && recommendedIds ? recommendedIds.split("|") : []); }, [preset?.id, engineId, recommendedIds]);
  const grabbing = grab && target === "runpod";
  const grabList = useMemo(() => offers.filter((o) => picked.includes(o.id))
    .sort((a, b) => (a.usd_h ?? 99) - (b.usd_h ?? 99)).map((o) => o.id), [offers, picked]);
  const toggleGrab = (on: boolean) => {
    setGrab(on);
    if (on && !picked.length) setPicked(offers.filter((o) => o.recommended).map((o) => o.id));
  };
  const togglePick = (id: string) => setPicked((p) => (p.includes(id) ? p.filter((x) => x !== id) : [...p, id]));
  const prices = grabList.map((id) => offers.find((o) => o.id === id)?.usd_h).filter((x): x is number => x != null);
  const planGpu = grabbing ? (grabList[0] ?? "") : gpu;
  const offer = offers.find((o) => o.id === planGpu);
  const soldOut = target === "runpod" && !grabbing && !!gpus.data?.live && !inStock(offer);
  const plan = useQuery({
    queryKey: ["plan", dsId, engineId, preset?.id, planGpu, offer?.usd_h, epochs, target],
    queryFn: () => api.post<Plan>("/api/training/plan", { dataset_id: dsId, engine: engineId, preset: preset!.id, gpu: planGpu, usd_h: offer?.usd_h ?? null, params: overrides, target }),
    enabled: !!dsId && !!preset && (!!planGpu || target === "colab"),
  });
  const start = useMutation({
    mutationFn: () => api.post<Training>("/api/training", {
      dataset_id: dsId, engine: engineId, preset: preset!.id, gpu: planGpu, name, usd_h: offer?.usd_h ?? null, params: overrides, target,
      ...(grabbing ? { gpus: grabList, wait_hours: waitHours } : {}),
    }),
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
          <div>
            <span className="label">4. 在哪裡訓練</span>
            <div className="grid gap-2 sm:grid-cols-2">
              {([["runpod", "RunPod", "全自動開機、訓練、關機。按小時付費。", cloudReady],
                ["colab", "Google Colab", "用 Google AI 方案的運算單位。要自己在 Colab 按執行，分頁要開著。", colabReady]] as const).map(([k, l, d, ready]) => (
                <button key={k} onClick={() => setTarget(k)}
                  className={clsx("rounded-xl border p-3 text-left transition", target === k ? "border-brand-500 ring-2 ring-brand-500/20" : "border-zinc-200 hover:border-brand-300 dark:border-zinc-800")}>
                  <div className="flex items-center gap-2 text-sm font-medium">{k === "colab" ? <FolderSync className="size-4" /> : <Cloud className="size-4" />}{l}
                    {!ready && <Badge tone="amber">未設定</Badge>}</div>
                  <p className="mt-1 text-xs leading-5 text-zinc-500">{d}</p>
                </button>
              ))}
            </div>
          </div>
          {target === "colab" ? (
            <div className="rounded-xl border border-zinc-200 p-3 text-sm dark:border-zinc-800">
              {colabReady ? (
                <ul className="list-disc space-y-1 pl-4 text-xs leading-5 text-zinc-600 dark:text-zinc-300">
                  <li>按開始後，平台把資料放進雲端硬碟的 Voice Studio 資料夾（Google 雲端硬碟電腦版會自動上傳）。</li>
                  <li>到 Colab 打開 <b>VoiceStudio-Colab.ipynb</b>，執行階段選 <b>A100</b>（沒有就選 L4），按 ▶。</li>
                  <li>完成後 Colab 自動斷線；模型同步回來後，平台會自動安裝和評分。</li>
                  <li>建議只用 <b>LoRA</b>：完整微調的檔案太大，同步很慢。</li>
                </ul>
              ) : <p className="text-xs text-amber-700 dark:text-amber-300">還沒設定。到 <Link to="/settings#colab" className="underline">設定 → Google Colab</Link> 選雲端硬碟資料夾。</p>}
            </div>
          ) : (
          <div>{/* not a <Field>: that is a <label>, and the card rows are labels of their own */}
            <span className="label">雲端 GPU</span>
            {cloudReady ? <GpuPicker q={gpus} value={gpu} onChange={setGpu} {...(grabbing ? { picked, onToggle: togglePick } : {})} /> : (
              <div className="grid gap-2">
                {offers.map((o) => (
                  <div key={o.id} className="flex items-center gap-3 rounded-lg border border-zinc-200 px-3 py-2 text-sm text-zinc-500 dark:border-zinc-800">
                    <Cpu className="size-4 text-zinc-400" /><span className="flex-1">{o.label}</span></div>
                ))}
              </div>
            )}
            {cloudReady && (
              <div className={clsx("mt-3 rounded-xl border px-3 py-2 text-sm",
                gpus.data?.live && !gpus.data.offers.some(inStock) && !grab
                  ? "border-amber-400 bg-amber-50 dark:border-amber-700 dark:bg-amber-950/40" : "border-zinc-200 dark:border-zinc-800")}>
                <label className="flex cursor-pointer items-start gap-2">
                  <input type="checkbox" className="mt-1" checked={grab} onChange={(e) => toggleGrab(e.target.checked)} />
                  <span><b>沒貨時自動搶卡</b>：每 30 秒查一次 {gpus.data?.datacenter ?? "資料中心"} 的庫存，勾選的卡一有貨，就自動租下最便宜的那張、開始訓練。
                    等的時候不租任何機器、不計費。Voice Studio 要開著；關掉的話，下次打開會接著等。</span>
                </label>
                {grab && (
                  <div className="mt-2 flex flex-wrap items-center gap-2 pl-6 text-xs text-zinc-600 dark:text-zinc-300">
                    最多等
                    <select className="input w-auto py-1" value={waitHours} onChange={(e) => setWaitHours(+e.target.value)}>
                      {[1, 3, 6, 12, 24, 48].map((h) => <option key={h} value={h}>{h} 小時</option>)}
                    </select>
                    {grabList.length
                      ? <span>勾了 {grabList.length} 張{prices.length ? `，每小時 $${Math.min(...prices).toFixed(2)}–$${Math.max(...prices).toFixed(2)}（下面的預估用最便宜的那張算）` : ""}</span>
                      : <span className="text-red-600">至少勾一張卡</span>}
                  </div>
                )}
              </div>
            )}
            <span className="mt-1 block text-xs text-zinc-500">只列出你網路磁碟所在資料中心的卡，沒貨的不能選。價格是 RunPod Secure Cloud 每小時價格（網路磁碟只能用 Secure Cloud）。平台只會租你選的這一張（自動搶卡時，是你勾的卡裡最便宜、有貨的那張），不會偷偷換成更貴的卡。按開始後會先租下這張卡（佔住），再上傳訓練資料：上傳期間就開始計費，但雲端機器同時在準備環境，不會上傳完才發現卡被租走。</span>
          </div>
          )}
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
                {target === "colab" ? (
                  <div><div className="text-xs text-zinc-500">預估運算單位</div><div className="text-lg font-semibold">{plan.data.compute_units ? `約 ${plan.data.compute_units[0]}–${plan.data.compute_units[1]}` : "—"}</div></div>
                ) : <div><div className="text-xs text-zinc-500">預估費用</div><div className="text-lg font-semibold">{fmtUsd(plan.data.estimate_usd)}</div></div>}
                <div><div className="text-xs text-zinc-500">訓練步數</div><div>{plan.data.steps || "—"}（{plan.data.n_train} 段{plan.data.epochs_effective ? `，約 ${plan.data.epochs_effective} epoch` : ""}）</div></div>
                <div><div className="text-xs text-zinc-500">最多（時數上限）</div><div>{plan.data.max_hours} 小時{target === "colab" ? "" : ` · ${fmtUsd(plan.data.max_usd)}`}</div></div>
              </div>
              <p className="mt-3 text-xs text-zinc-500">
                {plan.data.estimate_basis === "measured" ? "這個估計用的是你上次在這張卡實際量到的速度。"
                  : plan.data.estimate_basis === "scaled" ? `這張卡還沒跑過：用你在 ${plan.data.estimate_from} 量到的速度，依兩張卡的效能比例換算（粗估），跑完一次後會改用這張卡的實測速度。`
                  : "第一次是粗估；跑完一次後平台會用實際速度校正。"}
                {plan.data.s_per_step ? `（每步約 ${plan.data.s_per_step} 秒）` : ""}
                {target === "runpod" && plan.data.upload && (plan.data.upload.minutes != null
                  ? `上傳約 ${plan.data.upload.gb} GB、約 ${plan.data.upload.minutes} 分鐘（照你上次的上傳速度），已算進預估：GPU 先租下才上傳，這段時間也在計費。`
                  : `上傳約 ${plan.data.upload.gb} GB。GPU 先租下才上傳，這段時間也在計費；第一次上傳完會記下你的上傳速度，之後算進預估。`)}
                {target === "colab" ? "運算單位是粗估（A100 每小時約 5–15，Google 沒有公布），實際用量看 Colab 的資源面板。每次新的 Colab 執行階段都要重新安裝環境（約 5–10 分鐘）。" : "網路磁碟另計（約 $0.07/GB/月）。"}
              </p>
              {plan.data.blocked && <p className="mt-2 flex gap-1.5 text-xs font-medium text-red-600"><AlertTriangle className="mt-0.5 size-3.5 shrink-0" />{plan.data.blocked}</p>}
              {plan.data.warnings.map((w) => <p key={w} className="mt-2 flex gap-1.5 text-xs text-amber-700 dark:text-amber-300"><AlertTriangle className="mt-0.5 size-3.5 shrink-0" />{w}</p>)}
            </div>
          )}
          <ErrorText error={plan.error} />
          <label className="flex items-start gap-2 text-sm">
            <input type="checkbox" className="mt-1" checked={ack} onChange={(e) => setAck(e.target.checked)} />
            <span>{target === "colab"
              ? "我了解：要自己在 Colab 執行筆記本，訓練時分頁要開著；A100 不保證有；Colab 規則禁止製作深偽內容，我只訓練有同意的聲音。"
              : grabbing
                ? "我了解：等卡時不租任何機器、不計費；搶到卡後會用我的 RunPod 帳號租那張卡並計費，訓練完成、失敗、取消或達到時數上限時，平台會自動關機。"
                : "我了解這會用我的 RunPod 帳號租 GPU 並計費；訓練完成、失敗、取消或達到時數上限時，平台會自動關機。"}</span>
          </label>
          <Button className="w-full" onClick={() => start.mutate()} loading={start.isPending}
            disabled={!ack || !(target === "colab" ? colabReady : cloudReady) || !plan.data || !!plan.data.blocked || soldOut
              || (grabbing && !grabList.length)
              || (target === "runpod" && !!volumeProblem)}>
            {target === "colab" ? <><FolderSync className="size-4" />放進雲端硬碟，準備在 Colab 訓練</>
              : grabbing ? <><Cloud className="size-4" />開始等卡（有貨自動開始）</> : <><Cloud className="size-4" />開始雲端訓練</>}
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
  const recover = useMutation({ mutationFn: () => api.post(`/api/training/${t.id}/recover`), onSuccess: () => qc.invalidateQueries({ queryKey: ["trainings"] }) });
  const split = useMutation({ mutationFn: () => api.post(`/api/training/${t.id}/split`), onSuccess: () => qc.invalidateQueries({ queryKey: ["trainings"] }) });
  const remove = useMutation({ mutationFn: () => api.del(`/api/training/${t.id}`), onSuccess: () => qc.invalidateQueries({ queryKey: ["trainings"] }) });
  const [retryOpen, setRetryOpen] = useState(false);
  const [label, tone] = STATUS[t.status] ?? [t.status, "zinc"];
  const active = !["done", "failed", "canceled"].includes(t.status);
  const isColab = t.target === "colab";
  const p = t.progress ?? {};
  const voice = useQuery({ queryKey: ["voices"], queryFn: () => api.get<Voice[]>("/api/voices") }).data?.find((v) => v.id === t.voice_id);
  const model = useQuery({ queryKey: ["models"], queryFn: () => api.get<{ id: string; training_id: string | null }[]>("/api/models"), enabled: t.status === "done" })
    .data?.find((m) => m.training_id === t.id);
  return (
    <div className="rounded-xl border border-zinc-200 p-4 dark:border-zinc-800">
      <div className="flex flex-wrap items-center gap-2">
        <span className="font-medium">{t.preset.name || `${voice?.name ?? ""} · ${t.engine}`}</span>
        <Badge tone={tone}>{label}</Badge>
        <span className="text-xs text-zinc-500">{t.engine} / {t.preset.id} · {isColab ? `Colab${p.gpu_name ? ` ${p.gpu_name.replace("NVIDIA ", "")}` : ""}` : p.gpu_name ?? t.gpu.replace("NVIDIA ", "")} · {fmtTime(t.created_at)}</span>
        <div className="ml-auto flex gap-2">
          <Button size="sm" variant="ghost" onClick={onLog}><FileText className="size-3.5" />紀錄</Button>
          {active && <Button size="sm" variant="danger" loading={cancel.isPending} onClick={() => confirm(isColab ? "停止這次 Colab 訓練？（Colab 上的程式會在 30 秒內停下）"
                : t.status === "waiting_gpu" ? "停止等卡？（還沒租用或上傳任何東西，沒有費用）"
                : "停止這次訓練並關閉雲端機器？已經花的費用不會退回。") && cancel.mutate()}><Square className="size-3.5" />停止</Button>}
          {model && <Link to={`/models?id=${model.id}`}><Button size="sm">試聽模型</Button></Link>}
          {t.can_retry_gpu && <Button size="sm" onClick={() => setRetryOpen(true)} title="資料已經在雲端，不會重新上傳"><RefreshCw className="size-3.5" />換一張 GPU 重試</Button>}
          {(t.status === "failed" || t.status === "canceled") && !model && !t.can_retry_gpu && (
            <Button size="sm" variant="secondary" loading={recover.isPending} title="訓練如果已經進行到存檔，可以把權重下載回來"
              onClick={() => recover.mutate()}>救回模型</Button>)}
          {(t.status === "failed" || t.status === "canceled") && !model && !t.can_retry_gpu && !isColab && (
            <Button size="sm" variant="secondary" loading={split.isPending}
              title="模型檔太大、RunPod 一直傳不過來（524）時用：在雲端切成小檔再下載"
              onClick={() => confirm("在 RunPod 上把模型檔切小再下載？\n\n"
                + "RunPod 沒辦法直接傳一整個幾十 GB 的模型檔（每次都 524），所以會租一台目前有貨、最便宜的 GPU，"
                + "在你的網路磁碟上把它切成 64 MB 的小檔，切完立刻關機，接著自動下載。\n\n"
                + "通常 10–20 分鐘，費用大約 US$0.5–1.5（看租到哪張卡）。中途關掉 Voice Studio 也沒關係，機器會被關掉，再按一次會接著切。")
                && split.mutate()}>切小再救回</Button>)}
          {!active && (
            <Button size="sm" variant="ghost" loading={remove.isPending} title="刪掉這筆紀錄和它在雲端、電腦上的檔案"
              onClick={() => confirm("刪除這筆訓練紀錄？\n\n"
                + (isColab ? "會刪掉它在 Google 雲端硬碟裡的訓練資料夾" : "會刪掉它在 RunPod 網路磁碟上的檔案（模型檔、試念樣本、上傳的訓練資料）")
                + "，以及電腦上沒下載完的模型檔，空出空間。"
                + (model ? "已經救回的模型會留在「模型」頁，不受影響。" : "這次訓練的模型就不能再救回了。")
                + "\n\n你的錄音和資料集不會動。")
                && remove.mutate()}><Trash2 className="size-3.5" />刪除紀錄</Button>)}
        </div>
      </div>
      {retryOpen && <RetryGpuModal t={t} onClose={() => setRetryOpen(false)} />}
      {isColab && t.phase && (t.status === "waiting" || t.status === "running") && (
        <div className="mt-3">
          <div className="mb-1 flex justify-between text-xs text-zinc-500"><span>{t.phase.label}</span><span>{Math.round(t.phase.fraction * 100)}%</span></div>
          <Progress value={t.phase.fraction} />
        </div>
      )}
      {isColab && t.status === "waiting" && (
        <div className="mt-3 rounded-lg bg-amber-50 px-3 py-2 text-xs leading-5 text-amber-900 dark:bg-amber-950/40 dark:text-amber-100">
          <div className="font-medium">接下來在 Colab：</div>
          <ol className="mt-1 list-decimal pl-4">
            <li>等雲端硬碟電腦版把資料上傳完（工作列的雲端硬碟圖示不再轉圈）。</li>
            <li>在瀏覽器打開 Google 雲端硬碟，找到「我的雲端硬碟」裡的 <code className="kbd">{t.colab_path ?? "VoiceStudio/VoiceStudio-Colab.ipynb"}</code>，右鍵 → 開啟工具 → Google Colaboratory。</li>
            <li>「執行階段 → 變更執行階段類型」選 A100（沒有就選 L4），按那一格左邊的 ▶，分頁保持開著。</li>
          </ol>
        </div>
      )}
      {t.status === "waiting_gpu" && t.wait && (
        <div className="mt-3 rounded-lg bg-amber-50 px-3 py-2 text-xs leading-5 text-amber-900 dark:bg-amber-950/40 dark:text-amber-100">
          <div className="font-medium">正在等卡：還沒租用任何機器，不計費。勾選的卡一有貨就自動開始。</div>
          <div>可以接受：{(t.wait.gpus ?? []).map((g) => {
            const s = t.wait?.seen?.[g];
            return `${g.replace("NVIDIA ", "").replace("GeForce ", "")}${s ? `（${STOCK[s]?.[0] ?? s}）` : ""}`;
          }).join("、")}</div>
          <div>每 30 秒查一次 {t.storage?.datacenter ?? ""} 的庫存，已查 {t.wait.checks ?? 0} 次
            {t.wait.last ? `，最近一次 ${fmtTime(t.wait.last)}` : ""}；最多等到 {t.wait.until ? fmtTime(t.wait.until) : "—"}。</div>
          {!!t.wait.misses && <div>差一點搶到 {t.wait.misses} 次（被別人先租走），繼續等。</div>}
          {t.wait.error && <div className="text-red-700 dark:text-red-300">讀不到庫存：{t.wait.error}</div>}
        </div>
      )}
      {active && t.job && t.status !== "waiting_gpu" && !(isColab && (t.status === "waiting" || t.status === "running")) && (
        <div className="mt-3">
          <div className="mb-1 flex justify-between text-xs text-zinc-500"><span>{t.job.message}</span><span>{Math.round(t.job.progress * 100)}%</span></div>
          <Progress value={t.job.progress} />
          {!isColab && <p className="mt-1 text-xs text-zinc-500">訓練時請讓 Voice Studio 開著：結束時由它確認雲端機器已經關機，再把模型下載回來。
            關掉的話，下次打開會接著處理，但在那之前雲端機器可能還在計費。</p>}
        </div>
      )}
      <div className="mt-2 flex flex-wrap gap-x-4 gap-y-1 text-xs text-zinc-500">
        {p.wall_s != null && <span>已執行 {fmtDur(p.wall_s)}</span>}
        {p.epoch != null && <span>epoch {p.epoch}</span>}
        {p.loss != null && <span>訓練 loss {p.loss.toFixed(3)}</span>}
        {p.val_loss != null && <span>驗證 loss {p.val_loss.toFixed(3)}</span>}
        {p.s_per_step != null && <span>{p.s_per_step.toFixed(1)} 秒/步</span>}
        <span>{isColab ? "用 Colab 運算單位" : `預估 ${fmtUsd(t.cost_estimate)}`}</span>
        {t.cost_per_hr != null && <span>實際 ${t.cost_per_hr.toFixed(2)}/時</span>}
        {t.status === "failed" && t.job?.status === "failed" && t.job.message && <span className="text-red-600">{t.job.message}</span>}
      </div>
      {t.note && <p className="mt-2 text-xs text-amber-700 dark:text-amber-300">{t.note}</p>}
      {recover.error && <ErrorText error={recover.error} />}
      {split.error && <ErrorText error={split.error} />}
      {remove.error && <ErrorText error={remove.error} />}
      {t.pod_state === "remove_failed" && (
        <p className="mt-2 flex items-center gap-2 text-xs font-medium text-red-600"><AlertTriangle className="size-3.5" />
          雲端機器可能還在計費。平台會在下次開啟時自動再刪一次；也可以馬上到 runpod.io → Pods 手動刪除。</p>
      )}
    </div>
  );
}

function RetryGpuModal({ t, onClose }: { t: Training; onClose: () => void }) {
  const qc = useQueryClient();
  const gpus = useGpuOffers(t.engine, t.preset.id, true);
  const [gpu, setGpu] = useState("");
  useRentableChoice(gpus, gpu, setGpu);
  const offer = gpus.data?.offers.find((o) => o.id === gpu);
  const retry = useMutation({
    mutationFn: () => api.post(`/api/training/${t.id}/retry-gpu`, { gpu, usd_h: offer?.usd_h ?? null }),
    onSuccess: () => { qc.invalidateQueries({ queryKey: ["trainings"] }); onClose(); },
  });
  return (
    <Modal open onClose={onClose} title="換一張 GPU 重試">
      <p className="mb-3 text-xs leading-5 text-zinc-500">這次訓練的資料已經在雲端，不會重新上傳。選一張現在有貨的卡，平台會直接租這張開始訓練（租之前會再確認一次有貨）。</p>
      <GpuPicker q={gpus} value={gpu} onChange={setGpu} />
      <Button className="mt-4 w-full" loading={retry.isPending} onClick={() => retry.mutate()}
        disabled={!gpu || (!!gpus.data?.live && !inStock(offer))}><Cloud className="size-4" />用這張開始訓練</Button>
      <ErrorText error={retry.error} />
    </Modal>
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

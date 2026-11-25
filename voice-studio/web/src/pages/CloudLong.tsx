// Long-form speech on a rented RunPod GPU: a whole chapter or script in one go, for about a dollar of GPU time.
import { useEffect, useState } from "react";
import { Link } from "react-router";
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import clsx from "clsx";
import { CloudUpload, Download, FileText, Play, RotateCcw, Square, Trash2 } from "lucide-react";
import { api, fmtTime, MODES, type CloudTtsPlan, type CloudTtsRun, type Model } from "../api";
import { Badge, Button, Card, ErrorText, Field, Modal, Progress, Wave } from "../ui";

const MAX_CHARS = 400_000;
const CLOUD_ENGINES = ["voxcpm2", "mock"];
const STATUS: Record<string, [string, "zinc" | "green" | "amber" | "red" | "brand" | "blue"]> = {
  queued: ["排隊中", "zinc"], uploading_model: ["上傳模型（只有第一次）", "blue"], uploading: ["上傳文字", "blue"],
  starting: ["租用 GPU", "blue"], running: ["雲端合成中", "brand"], downloading: ["下載、接成音檔", "blue"],
  done: ["完成", "green"], failed: ["停下來了", "red"], canceled: ["已停止", "amber"],
};

const usd = (x: number | null | undefined) => (x == null ? "—" : `US$${x < 0.1 ? x.toFixed(3) : x.toFixed(2)}`);
const size = (b: number) => (b >= 1e9 ? `${(b / 1e9).toFixed(1)} GB` : `${Math.max(1, Math.round(b / 1e6))} MB`);
const minutes = (s: number) => (s >= 3600 ? `${Math.floor(s / 3600)} 小時 ${Math.round((s % 3600) / 60)} 分` : `${Math.max(1, Math.round(s / 60))} 分鐘`);

export default function CloudLong({ models }: { models: Model[] }) {
  const qc = useQueryClient();
  const usable = models.filter((m) => CLOUD_ENGINES.includes(m.engine));
  const [picked, setModelId] = useState("");  // the list may still be loading on the first render
  const model = usable.find((m) => m.id === picked) ?? usable[0];
  const modelId = model?.id ?? "";
  const [text, setText] = useState("");
  const [name, setName] = useState("");
  const [mode, setMode] = useState("plain");
  const [refId, setRefId] = useState("");
  const [language, setLanguage] = useState("auto");
  const [gpu, setGpu] = useState<string | null>(null);
  const [agree, setAgree] = useState(false);
  const [debounced, setDebounced] = useState("");
  useEffect(() => { const t = setTimeout(() => setDebounced(text), 700); return () => clearTimeout(t); }, [text]);
  useEffect(() => {
    if (!model) return;
    setMode(model.modes.includes(mode) ? mode : model.modes[0]);
    setRefId(model.meta.references?.[0]?.id ?? "");
  }, [model?.id]); // eslint-disable-line react-hooks/exhaustive-deps
  useEffect(() => setAgree(false), [debounced, gpu, modelId, mode]);
  const refs = model?.meta.references ?? [];
  const needsRef = mode === "ref" || mode === "hifi";
  const body = { model_id: modelId, text: debounced, gpu, tts_mode: mode, ref_id: needsRef ? refId || null : null, language, name };

  const plan = useQuery({
    queryKey: ["cloud-tts-plan", modelId, debounced, gpu, mode, refId, language],
    queryFn: () => api.post<CloudTtsPlan>("/api/cloud-tts/plan", body),
    enabled: !!model && debounced.trim().length > 0 && (!needsRef || refs.length > 0), retry: false,
  });
  const p = plan.data;
  const chosen = p?.gpus.find((g) => g.id === p.gpu);
  const runs = useQuery({
    queryKey: ["cloud-tts"], queryFn: () => api.get<CloudTtsRun[]>("/api/cloud-tts"),
    refetchInterval: (q) => ((q.state.data ?? []).some((r) => r.active) ? 3000 : 20000),
  });
  const start = useMutation({
    mutationFn: () => api.post<CloudTtsRun>("/api/cloud-tts", { ...body, text, gpu: p?.gpu ?? gpu }),
    onSuccess: () => { setAgree(false); qc.invalidateQueries({ queryKey: ["cloud-tts"] }); },
  });

  if (!usable.length)
    return (
      <Card>
        <p className="text-sm text-zinc-600 dark:text-zinc-300">雲端長篇合成目前只支援 VoxCPM2 的模型。先到 <Link to="/train" className="underline">雲端訓練</Link> 訓練一個 VoxCPM2 模型，或到 <Link to="/models" className="underline">模型</Link> 建立免訓練模型。</p>
      </Card>
    );

  const words = (text.match(/[\w']+/g) ?? []).length;
  return (
    <div className="grid gap-6 lg:grid-cols-[1fr_380px]">
      <div className="space-y-6">
        <Card>
          <div className="space-y-4">
            <p className="rounded-lg bg-brand-50 px-3 py-2 text-sm leading-6 text-brand-900 dark:bg-brand-900/20 dark:text-brand-100">
              整篇文字交給 RunPod 上租來的 GPU 念：大約 1–2 萬個英文字（1–2 小時的語音）通常只要 US$1 左右，跑完機器會自動關掉。
              你的電腦不用一直開著顯示卡，但這個程式要開著，才能下載結果、關掉機器。
            </p>
            <div className="grid gap-3 sm:grid-cols-2">
              <Field label="模型">
                <select className="input" value={modelId} onChange={(e) => setModelId(e.target.value)}>
                  {usable.map((m) => <option key={m.id} value={m.id}>{m.name}{m.meta.checkpoint ? `（${m.meta.checkpoint}）` : ""}</option>)}
                </select>
              </Field>
              <Field label="名稱（選填）">
                <input className="input" value={name} onChange={(e) => setName(e.target.value)} placeholder="第 3 章" />
              </Field>
            </div>
            <Field label={`文字（${text.length.toLocaleString()} 字元，約 ${words.toLocaleString()} 個英文字）`}
              hint={<>一句一句念，句子之間自動停頓、段落之間停久一點。可以用 <code className="kbd">[whispers]</code> <code className="kbd">[停頓 1秒]</code> 這類標籤；發音字典也會套用。</>}>
              <textarea className="input min-h-64 text-base leading-7" value={text} maxLength={MAX_CHARS}
                onChange={(e) => setText(e.target.value)} placeholder="Paste the whole chapter here…" />
            </Field>
            <div>
              <span className="label">合成方式</span>
              <div className="grid gap-2 sm:grid-cols-3">
                {(model?.modes ?? ["plain"]).map((k) => (
                  <button key={k} onClick={() => setMode(k)}
                    className={clsx("rounded-xl border p-3 text-left", mode === k ? "border-brand-500 ring-2 ring-brand-500/20" : "border-zinc-200 dark:border-zinc-800")}>
                    <div className="text-sm font-medium">{MODES[k]?.label ?? k}</div>
                    <div className="mt-0.5 text-[11px] leading-4 text-zinc-500">{MODES[k]?.hint}</div>
                  </button>
                ))}
              </div>
            </div>
            <div className="grid gap-3 sm:grid-cols-2">
              {needsRef && (
                <Field label="參考片段">
                  {refs.length ? (
                    <select className="input" value={refId} onChange={(e) => setRefId(e.target.value)}>
                      {refs.map((r) => <option key={r.id} value={r.id}>{r.text || r.label}</option>)}
                    </select>
                  ) : <p className="text-sm text-amber-700">這個模型還沒有參考片段，到 <Link to={`/models?id=${modelId}`} className="underline">模型頁</Link> 加入，或改用「只用模型」。</p>}
                </Field>
              )}
              <Field label="語言">
                <select className="input" value={language} onChange={(e) => setLanguage(e.target.value)}>
                  <option value="auto">自動</option><option value="en">英文</option><option value="ja">日文</option><option value="zh">中文</option>
                </select>
              </Field>
            </div>
          </div>
        </Card>
        <Runs runs={runs.data ?? []} />
      </div>

      <div className="space-y-4">
        <Card title="費用估算">
          {!text.trim() ? <p className="text-sm text-zinc-500">貼上文字後會估算時間和費用。</p> : plan.isFetching && !p ? <p className="text-sm text-zinc-500">估算中…</p> : (
            <div className="space-y-4 text-sm">
              <ErrorText error={plan.error} />
              {p && (<>
                <div className="grid grid-cols-3 gap-2 text-center">
                  <div><div className="text-lg font-semibold">{p.lines.toLocaleString()}</div><div className="text-xs text-zinc-500">句</div></div>
                  <div><div className="text-lg font-semibold">{minutes(p.speech_min * 60)}</div><div className="text-xs text-zinc-500">語音（約）</div></div>
                  <div><div className="text-lg font-semibold">{usd(p.estimate_usd)}</div><div className="text-xs text-zinc-500">GPU 費用（約）</div></div>
                </div>
                {p.model_upload_bytes > 0 && (
                  <p className="rounded-lg bg-zinc-50 px-3 py-2 text-xs leading-5 text-zinc-600 dark:bg-zinc-800/50 dark:text-zinc-300">
                    第一次要先把模型（{size(p.model_upload_bytes)}）傳到你的 RunPod 網路磁碟{p.model_upload_min ? `，約 ${p.model_upload_min} 分鐘` : ""}。
                    這段在租 GPU 之前做，不收 GPU 費用；之後同一個模型就不用再傳（網路磁碟每 GB 每月約 US$0.07）。
                  </p>
                )}
                <div>
                  <span className="label">顯示卡</span>
                  <div className="space-y-1">
                    {p.gpus.map((g) => (
                      <label key={g.id} className={clsx("flex cursor-pointer items-center gap-2 rounded-lg border px-2.5 py-2",
                        p.gpu === g.id ? "border-brand-500 bg-brand-50/50 dark:bg-brand-900/20" : "border-zinc-200 dark:border-zinc-800",
                        !g.in_stock && "opacity-50")}>
                        <input type="radio" checked={p.gpu === g.id} disabled={!g.in_stock} onChange={() => setGpu(g.id)} />
                        <span className="flex-1">
                          <span className="font-medium">{g.label}</span>
                          <span className="block text-[11px] text-zinc-500">{usd(g.usd_h)}/小時 · 約 {g.minutes} 分鐘{g.measured ? "（實測）" : ""}</span>
                        </span>
                        <span className="text-right">
                          <span className="block font-medium">{usd(g.usd)}</span>
                          {g.in_stock ? null : <Badge tone="red">沒貨</Badge>}
                        </span>
                      </label>
                    ))}
                  </div>
                </div>
                {p.warnings.map((w) => <p key={w} className="rounded-lg bg-amber-50 px-3 py-2 text-xs leading-5 text-amber-800 dark:bg-amber-950/40 dark:text-amber-200">{w}</p>)}
                <label className="flex items-start gap-2 text-xs leading-5">
                  <input type="checkbox" className="mt-0.5" checked={agree} onChange={(e) => setAgree(e.target.checked)} />
                  <span>我知道會租用 RunPod 的 {chosen?.label ?? "GPU"}，費用從我的 RunPod 帳戶扣：預估 {usd(p.estimate_usd)}；
                    最多跑 {p.max_hours} 小時（約 {usd(p.max_hours * p.usd_per_hour)}）就會強制關機，沒念完的可以按「繼續」。</span>
                </label>
                <Button className="w-full" disabled={!agree || !p.gpu || !chosen?.in_stock || start.isPending} loading={start.isPending}
                  onClick={() => start.mutate()}>
                  <CloudUpload className="size-4" />開始雲端合成
                </Button>
                <ErrorText error={start.error} />
                <p className="text-[11px] leading-4 text-zinc-500">建議第一次先貼一小段（幾百字）試跑，確認聲音和流程都正常，再跑整篇。</p>
              </>)}
            </div>
          )}
        </Card>
      </div>
    </div>
  );
}

function Runs({ runs }: { runs: CloudTtsRun[] }) {
  const qc = useQueryClient();
  const refresh = () => qc.invalidateQueries({ queryKey: ["cloud-tts"] });
  const cancel = useMutation({ mutationFn: (id: string) => api.post(`/api/cloud-tts/${id}/cancel`), onSuccess: refresh });
  const resume = useMutation({ mutationFn: (id: string) => api.post(`/api/cloud-tts/${id}/resume`), onSuccess: refresh });
  const del = useMutation({ mutationFn: (id: string) => api.del(`/api/cloud-tts/${id}`), onSuccess: refresh });
  const [playing, setPlaying] = useState<string | null>(null);
  const [logOf, setLogOf] = useState<string | null>(null);
  const log = useQuery({ queryKey: ["cloud-tts-log", logOf], enabled: !!logOf, retry: false,
    queryFn: () => api.get<{ log: string }>(`/api/cloud-tts/${logOf}/log`) });
  if (!runs.length) return null;
  return (
    <Card title="雲端合成紀錄">
      <div className="divide-y divide-zinc-100 dark:divide-zinc-800">
        {runs.map((r) => {
          const [label, tone] = STATUS[r.status] ?? [r.status, "zinc"];
          const total = r.params.lines ?? r.progress.total ?? 0;
          const spent = r.cost_per_hr && r.started_at ? r.cost_per_hr * (((r.finished_at ?? Date.now() / 1000) - r.started_at) / 3600) : null;
          return (
            <div key={r.id} className="space-y-2 py-3 first:pt-0 last:pb-0">
              <div className="flex flex-wrap items-center gap-2">
                <span className="font-medium">{r.params.name || r.params.preview.slice(0, 40) || r.id}</span>
                <Badge tone={tone}>{label}</Badge>
                <span className="text-xs text-zinc-500">{fmtTime(r.created_at)} · {total.toLocaleString()} 句 · {r.gpu?.replace("NVIDIA ", "")}
                  {spent != null ? ` · 已用約 ${usd(spent)}` : r.cost_estimate != null ? ` · 預估 ${usd(r.cost_estimate)}` : ""}</span>
                <span className="ml-auto flex gap-1">
                  {r.active && <Button size="sm" variant="secondary" onClick={() => cancel.mutate(r.id)} loading={cancel.isPending && cancel.variables === r.id}><Square className="size-3.5" />停止</Button>}
                  {(r.status === "failed" || r.status === "canceled") && <Button size="sm" variant="secondary" onClick={() => resume.mutate(r.id)} loading={resume.isPending && resume.variables === r.id}><RotateCcw className="size-3.5" />繼續</Button>}
                  {r.started_at && <Button size="sm" variant="ghost" title="雲端機器的紀錄" onClick={() => setLogOf(r.id)}><FileText className="size-3.5" />紀錄</Button>}
                  {!r.active && <Button size="sm" variant="ghost" title="刪除這筆紀錄和雲端上的暫存檔（做好的音檔會留在文字轉語音的紀錄裡）"
                    onClick={() => { if (window.confirm("刪除這筆紀錄和雲端上的暫存檔？做好的音檔會保留。")) del.mutate(r.id); }}><Trash2 className="size-3.5" /></Button>}
                </span>
              </div>
              {r.active && r.job && (
                <div className="space-y-1">
                  <Progress value={r.job.progress} />
                  <p className="text-xs text-zinc-500">{r.job.message}</p>
                </div>
              )}
              {r.note && <p className={clsx("text-xs", r.status === "done" ? "text-zinc-500" : "text-amber-700 dark:text-amber-300")}>{r.note}</p>}
              {r.output && (
                <div className="flex flex-wrap items-center gap-2 text-sm">
                  <span className="text-zinc-500">{minutes(r.output.duration)}</span>
                  <Button size="sm" variant="secondary" onClick={() => setPlaying(playing === r.id ? null : r.id)}><Play className="size-3.5" />{playing === r.id ? "收起" : "試聽"}</Button>
                  <a className="inline-flex items-center gap-1 text-xs text-brand-600 hover:underline" href={`/api/outputs/${r.output.id}/audio`} download><Download className="size-3.5" />WAV</a>
                  <a className="inline-flex items-center gap-1 text-xs text-brand-600 hover:underline" href={`/api/outputs/${r.output.id}/audio?format=mp3`} download><Download className="size-3.5" />MP3</a>
                  <a className="inline-flex items-center gap-1 text-xs text-brand-600 hover:underline" href={`/api/outputs/${r.output.id}/sheet`} target="_blank" rel="noreferrer">每句的時間點</a>
                </div>
              )}
              {r.output && playing === r.id && <Wave src={`/api/outputs/${r.output.id}/audio?format=mp3`} />}
              <ErrorText error={(cancel.variables === r.id && cancel.error) || (resume.variables === r.id && resume.error) || (del.variables === r.id && del.error) || null} />
            </div>
          );
        })}
      </div>
      <Modal open={!!logOf} onClose={() => setLogOf(null)} title="雲端機器的紀錄" wide>
        {log.isFetching ? <p className="text-sm text-zinc-500">讀取中…</p> : <ErrorText error={log.error} />}
        {log.data && <pre className="max-h-[60vh] overflow-auto whitespace-pre-wrap rounded-lg bg-zinc-950 p-3 text-[11px] leading-4 text-zinc-100">{log.data.log}</pre>}
      </Modal>
    </Card>
  );
}

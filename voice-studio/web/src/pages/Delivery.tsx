import { useEffect, useState } from "react";
import { Link } from "react-router";
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { CheckCircle2, Cpu, FolderInput, FolderSearch, ShieldAlert } from "lucide-react";
import { api, EMOTION_LABEL, fmtMin, LANGS, type Job, type Voice } from "../api";
import { Badge, Button, Card, Empty, ErrorText, Field, PageHeader, Progress } from "../ui";

type Count = { count: number; minutes: number };
type Person = {
  name: string; path: string; group: string; parts: Record<string, boolean>;
  delivery: { clean: Count; bgm: Count; sep: Count };
  training: Count & { skipped: Record<string, number>; from_common: number; from_library: number };
  languages: Record<string, number>; emotions: Record<string, number>;
  phrases: { count: number; clips: number; types: string[] };
  sounds: { count: number; clips: number; names: string[] };
  voice: { id: string; name: string; consent_ok: boolean } | null;
};
type Scan = { path: string; people: Person[] };
type Options = { bgm: "sep" | "original" | "skip"; common: boolean; phrase_clips: number; approve: boolean; build: boolean };
type ImportResult = {
  message: string; added: number; approved: number; approved_hours: number; pending: number; phrases: number;
  phrase_clips: number; sounds: number; sound_clips: number; dataset_id: string | null; dataset_error: string;
  too_long: string[]; problems: string[]; n_problems: number; skipped: Record<string, number>;
};

const BGM: Record<Options["bgm"], string> = {
  sep: "用去背景音樂的版本（有的話）", original: "用原音（保留小聲的音樂）", skip: "不要用",
};
const SKIPPED: Record<string, string> = {
  no_text: "沒有逐字稿", duplicate: "和別的片段重複", incomplete: "句子不完整", bgm: "有背景音樂（設定為不用）",
};

function readSaved<T>(key: string, fallback: T): T {
  try { const v = localStorage.getItem(key); return v ? (JSON.parse(v) as T) : fallback; } catch { return fallback; }
}

export default function Delivery() {
  const [path, setPath] = useState(() => readSaved("delivery-path", ""));
  const [opts, setOpts] = useState<Options>(() => readSaved("delivery-opts",
    { bgm: "sep", common: true, phrase_clips: 8, approve: true, build: true }));
  useEffect(() => { try { localStorage.setItem("delivery-path", JSON.stringify(path)); } catch { /* private mode */ } }, [path]);
  useEffect(() => { try { localStorage.setItem("delivery-opts", JSON.stringify(opts)); } catch { /* private mode */ } }, [opts]);
  const voices = useQuery({ queryKey: ["voices"], queryFn: () => api.get<Voice[]>("/api/voices") });
  const scan = useMutation({ mutationFn: () => api.post<Scan>("/api/delivery/scan", { path, bgm: opts.bgm }) });

  return (
    <div>
      <PageHeader title="交付資料夾"
        subtitle={<>選一個交付資料夾（一個人，或放了很多人的上層資料夾），平台會照資料夾名稱把每段錄音放到對的位置：
          訓練片段（語言、情緒、有沒有背景音樂）、口頭禪和常用語的原音、聲音標籤。只有<b>同意紀錄完整</b>的聲音可以匯入。
          結構說明見 <Link className="text-brand-600 underline" to="/guide/16-delivery">〈交付資料夾〉</Link>。</>} />
      <Card className="mb-6">
        <div className="grid gap-4 md:grid-cols-[1fr_auto]">
          <Field label="資料夾路徑" hint="例如 E:\交付總覽（掃描全部的人）或 E:\交付總覽\EN\某某（只看一個人）。可以從檔案總管的網址列複製。">
            <input className="input font-mono" value={path} onChange={(e) => setPath(e.target.value)}
              placeholder="E:\交付總覽" onKeyDown={(e) => e.key === "Enter" && path.trim() && scan.mutate()} />
          </Field>
          <div className="flex items-end">
            <Button onClick={() => scan.mutate()} loading={scan.isPending} disabled={!path.trim()}>
              <FolderSearch className="size-4" />掃描
            </Button>
          </div>
        </div>
        <details className="mt-4 text-sm">
          <summary className="cursor-pointer text-zinc-600 dark:text-zinc-300">匯入設定</summary>
          <div className="mt-3 grid gap-4 md:grid-cols-2">
            <Field label="有背景音樂的片段（bgm）">
              <select className="input" value={opts.bgm} onChange={(e) => setOpts({ ...opts, bgm: e.target.value as Options["bgm"] })}>
                {Object.entries(BGM).map(([k, l]) => <option key={k} value={k}>{l}</option>)}
              </select>
            </Field>
            <Field label="每句口頭禪／聲音標籤最多放幾段原音" hint="挑不同情緒、聲紋最像、句子完整的">
              <input className="input" type="number" min={1} max={30} value={opts.phrase_clips}
                onChange={(e) => setOpts({ ...opts, phrase_clips: Math.max(1, Math.min(30, Number(e.target.value) || 1)) })} />
            </Field>
            <label className="flex items-start gap-2"><input type="checkbox" className="mt-1" checked={opts.common} onChange={(e) => setOpts({ ...opts, common: e.target.checked })} />
              <span>常用語的錄音也當訓練資料<span className="block text-xs text-zinc-500">句子不完整的不會放進去</span></span></label>
            <label className="flex items-start gap-2"><input type="checkbox" className="mt-1" checked={opts.approve} onChange={(e) => setOpts({ ...opts, approve: e.target.checked })} />
              <span>通過檢查的片段直接核可<span className="block text-xs text-zinc-500">爆音、分數太低的會留在「檢查資料」等你聽</span></span></label>
            <label className="flex items-start gap-2"><input type="checkbox" className="mt-1" checked={opts.build} onChange={(e) => setOpts({ ...opts, build: e.target.checked })} />
              <span>匯入後建立資料集（訓練要用）</span></label>
          </div>
        </details>
        <ErrorText error={scan.error} />
      </Card>
      {scan.data && (scan.data.people.length === 0
        ? <Empty icon={<FolderInput className="size-8" />} title="這個資料夾裡沒有交付資料夾">要有「交付」「常用語」或「素材庫」其中一個子資料夾。</Empty>
        : <div className="space-y-4">
            <p className="text-sm text-zinc-500">找到 {scan.data.people.length} 個人。</p>
            {scan.data.people.map((p) => <PersonCard key={p.path} p={p} voices={voices.data ?? []} opts={opts} />)}
          </div>)}
    </div>
  );
}

function PersonCard({ p, voices, opts }: { p: Person; voices: Voice[]; opts: Options }) {
  const qc = useQueryClient();
  const [voiceId, setVoiceId] = useState(p.voice?.id ?? "");
  const [jobId, setJobId] = useState("");
  const voice = voices.find((v) => v.id === voiceId);
  const start = useMutation({
    mutationFn: () => api.post<Job>("/api/delivery/import", { path: p.path, voice_id: voiceId, ...opts }),
    onSuccess: (j) => setJobId(j.id),
  });
  const job = useQuery({
    queryKey: ["job", jobId], queryFn: () => api.get<Job>(`/api/jobs/${jobId}`), enabled: !!jobId,
    refetchInterval: (q) => (q.state.data && ["done", "failed", "canceled"].includes(q.state.data.status) ? false : 1500),
  });
  const done = job.data?.status === "done";
  useEffect(() => { if (done) { qc.invalidateQueries({ queryKey: ["voices"] }); qc.invalidateQueries({ queryKey: ["datasets"] }); } }, [done, qc]);
  const res = done ? (job.data!.result as unknown as ImportResult) : null;
  const running = !!jobId && !!job.data && ["queued", "running"].includes(job.data.status);
  const skipped = Object.entries(p.training.skipped).filter(([, n]) => n > 0);

  return (
    <Card title={<span>{p.name}{p.group && <span className="ml-2 text-xs font-normal text-zinc-500">{p.group}</span>}</span>}
      actions={<span className="max-w-md truncate font-mono text-[11px] text-zinc-400" title={p.path}>{p.path}</span>}>
      <div className="grid gap-4 text-sm md:grid-cols-4">
        <div>
          <div className="text-xs text-zinc-500">訓練片段</div>
          <div className="text-lg font-semibold">{p.training.count} 段</div>
          <div className="text-xs text-zinc-500">{fmtMin(p.training.minutes)}
            {(p.training.from_common > 0 || p.training.from_library > 0) && `，含常用語 ${p.training.from_common}、素材庫 ${p.training.from_library}`}</div>
        </div>
        <div>
          <div className="text-xs text-zinc-500">背景</div>
          <div>安靜 {p.delivery.clean.count}　有音樂 {p.delivery.bgm.count}</div>
          <div className="text-xs text-zinc-500">去背景音樂版 {p.delivery.sep.count} 段</div>
        </div>
        <div>
          <div className="text-xs text-zinc-500">口頭禪・常用語</div>
          <div>{p.phrases.count} 句（{p.phrases.clips} 段錄音）</div>
          <div className="truncate text-xs text-zinc-500" title={p.phrases.types.join("、")}>{p.phrases.types.join("、")}</div>
        </div>
        <div>
          <div className="text-xs text-zinc-500">聲音標籤</div>
          <div>{p.sounds.count} 種（{p.sounds.clips} 段）</div>
          <div className="truncate text-xs text-zinc-500" title={p.sounds.names.join(" ")}>{p.sounds.names.join(" ")}</div>
        </div>
      </div>
      <div className="mt-3 flex flex-wrap gap-1">
        {Object.entries(p.languages).map(([k, m]) => <Badge key={k} tone="blue">{LANGS[k] ?? "日英混合／未標"} {fmtMin(m)}</Badge>)}
        {Object.entries(p.emotions).map(([k, m]) => <Badge key={k}>{k ? EMOTION_LABEL[k] ?? k : "未標情緒"} {fmtMin(m)}</Badge>)}
      </div>
      {skipped.length > 0 && (
        <p className="mt-2 text-xs text-zinc-500">不會放進訓練：{skipped.map(([k, n]) => `${SKIPPED[k] ?? k} ${n} 段`).join("、")}</p>
      )}

      <div className="mt-4 flex flex-wrap items-end gap-3 border-t border-zinc-100 pt-4 dark:border-zinc-800">
        <Field label="匯入到哪個聲音">
          <select className="input min-w-56" value={voiceId} onChange={(e) => setVoiceId(e.target.value)}>
            <option value="">選擇聲音…</option>
            {voices.map((v) => <option key={v.id} value={v.id}>{v.name}{v.consent_ok ? "" : "（同意紀錄不完整）"}</option>)}
          </select>
        </Field>
        <Button onClick={() => start.mutate()} loading={start.isPending || running} disabled={!voice?.consent_ok || running}>
          <FolderInput className="size-4" />一鍵匯入
        </Button>
        {!voiceId && <span className="text-xs text-zinc-500">沒有這個人的聲音？先到 <Link className="text-brand-600 underline" to="/voices">聲音與同意</Link> 新增並填同意紀錄。</span>}
      </div>
      {voice && !voice.consent_ok && (
        <p className="mt-3 flex items-start gap-2 rounded-lg bg-amber-50 p-3 text-sm text-amber-900 dark:bg-amber-900/20 dark:text-amber-200">
          <ShieldAlert className="mt-0.5 size-4 shrink-0" />
          <span>「{voice.name}」還沒有完整的同意紀錄，不能匯入。請到 <Link className="underline" to={`/voices/${voice.id}`}>聲音與同意</Link> 填好本人的簽名、日期、同意範圍和同意書。</span>
        </p>
      )}
      <ErrorText error={start.error} />
      {running && <div className="mt-3"><div className="text-xs text-zinc-500">{job.data!.message}</div><Progress value={job.data!.progress} className="mt-1" /></div>}
      {job.data?.status === "failed" && <p className="mt-3 text-sm text-red-600">匯入失敗：{job.data.message}（<Link className="underline" to="/jobs">看詳細</Link>）</p>}
      {res && (
        <div className="mt-3 rounded-lg bg-emerald-50 p-3 text-sm dark:bg-emerald-900/20">
          <p className="flex items-start gap-2"><CheckCircle2 className="mt-0.5 size-4 shrink-0 text-emerald-600" />{res.message}</p>
          {res.pending > 0 && <p className="mt-1 text-xs text-zinc-600 dark:text-zinc-300">{res.pending} 段沒有自動核可，在「檢查資料」等你聽。</p>}
          {res.dataset_error && <p className="mt-1 text-xs text-amber-700">沒有建立資料集：{res.dataset_error}</p>}
          {res.too_long.length > 0 && <p className="mt-1 text-xs text-zinc-600 dark:text-zinc-300">超過 60 字、只當訓練資料的常用語：{res.too_long.join("、")}</p>}
          {res.n_problems > 0 && (
            <details className="mt-1 text-xs"><summary className="cursor-pointer">{res.n_problems} 段原音沒有加入（長度不合）</summary>
              <ul className="mt-1 list-disc pl-5">{res.problems.map((x) => <li key={x}>{x}</li>)}</ul></details>
          )}
          <div className="mt-3 flex flex-wrap gap-2">
            {res.dataset_id && <Link to={`/train?dataset=${res.dataset_id}`}><Button size="sm"><Cpu className="size-3.5" />用這份資料集訓練</Button></Link>}
            <Link to="/review"><Button size="sm" variant="secondary">檢查資料</Button></Link>
            {voice && <Link to={`/voices/${voice.id}`}><Button size="sm" variant="secondary">看口頭禪和聲音標籤</Button></Link>}
          </div>
        </div>
      )}
    </Card>
  );
}

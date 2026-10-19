import { useRef, useState } from "react";
import { Link } from "react-router";
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import clsx from "clsx";
import { ChevronDown, ChevronRight, CircleCheck, CircleHelp, CircleX, FolderSearch, RefreshCw, Stethoscope, Trash2, TriangleAlert, Upload } from "lucide-react";
import { api, fmtMin, LANGS, type Voice } from "../api";
import { Badge, Button, Card, Empty, ErrorText, Field, Modal, PageHeader, PlayButton, Progress, usePlayer } from "../ui";

type Level = "pass" | "warn" | "fail" | "unknown" | "info";
type CheckRow = { key: string; label: string; level: Level; value: string; detail: string; ranges: [number, number][] };
type Item = {
  id: string; batch: string; filename: string; path: string; status: string; verdict: "pass" | "warn" | "fail" | null;
  duration: number | null; copied: number; meta: { imported?: string };
  result: {
    checks?: CheckRow[]; error?: string;
    info?: { codec?: string; sr?: number; channels?: number; kbps?: number; duration: number; analysed: number; sampled: boolean; speech_seconds: number };
    timeline?: { windows: [number, number][]; speech: [number, number][]; background: [number, number][]; clipping: [number, number][] };
  };
};
type Batch = { id: string; created_at: number; root: string | null; items: Item[]; job: { status: string; progress: number; message: string } | null };
type Criterion = { label: string; pass: string; warn: string; fail: string };

const VERDICT: Record<string, [string, "green" | "amber" | "red"]> = { pass: ["通過", "green"], warn: ["勉強可用", "amber"], fail: ["不通過", "red"] };
const SHORT: Record<string, string> = {
  background: "背景音", noise: "雜音", echo: "回音", clipping: "破音", level: "音量", band: "音質", processed: "後製", dropouts: "斷訊",
  under: "說話底下", speech: "說話",
};
const tone = (l: Level) => (l === "fail" ? "red" : l === "warn" ? "amber" : l === "pass" ? "green" : "zinc");
const fmtT = (s: number) => `${Math.floor(s / 60)}:${String(Math.floor(s % 60)).padStart(2, "0")}`;

function LevelIcon({ level }: { level: Level }) {
  if (level === "pass" || level === "info") return <CircleCheck className="size-4 shrink-0 text-emerald-600" />;
  if (level === "warn") return <TriangleAlert className="size-4 shrink-0 text-amber-500" />;
  if (level === "fail") return <CircleX className="size-4 shrink-0 text-red-600" />;
  return <CircleHelp className="size-4 shrink-0 text-zinc-400" />;
}

function upload(file: File, batch: string, deep: boolean, onProgress: (f: number) => void) {
  return new Promise<void>((resolve, reject) => {
    const fd = new FormData();
    fd.append("file", file);
    fd.append("batch", batch);
    fd.append("deep", String(deep));
    const x = new XMLHttpRequest();
    x.open("POST", "/api/checks/upload");
    x.upload.onprogress = (e) => e.lengthComputable && onProgress(e.loaded / e.total);
    x.onload = () => (x.status < 300 ? resolve() : reject(new Error(x.responseText || x.statusText)));
    x.onerror = () => reject(new Error("上傳失敗（連線中斷）"));
    x.send(fd);
  });
}

const MEDIA = /\.(mp4|mkv|mov|webm|flv|ts|avi|wav|mp3|m4a|aac|flac|ogg|opus|wma)$/i;

export default function CheckPage() {
  const qc = useQueryClient();
  const batches = useQuery({
    queryKey: ["checks"], queryFn: () => api.get<Batch[]>("/api/checks"),
    refetchInterval: (q) => (q.state.data?.some((b) => b.job || b.items.some((i) => i.status === "queued" || i.status === "running")) ? 1500 : false),
  });
  const criteria = useQuery({ queryKey: ["check-criteria"], queryFn: () => api.get<Criterion[]>("/api/checks/criteria") });
  const [deep, setDeep] = useState(false);
  const [drag, setDrag] = useState(false);
  const [folder, setFolder] = useState("");
  const [up, setUp] = useState<{ name: string; progress: number; n: number; of: number } | null>(null);
  const [upError, setUpError] = useState<unknown>(null);
  const [showCriteria, setShowCriteria] = useState(false);
  const fileInput = useRef<HTMLInputElement>(null);

  async function send(files: FileList | File[]) {
    const list = Array.from(files).filter((f) => MEDIA.test(f.name) || /^(audio|video)\//.test(f.type));
    if (!list.length) return;
    setUpError(null);
    try {
      const { id } = await api.post<{ id: string }>("/api/checks/batches");
      for (const [i, f] of list.entries()) {
        setUp({ name: f.name, progress: 0, n: i + 1, of: list.length });
        await upload(f, id, deep, (p) => setUp({ name: f.name, progress: p, n: i + 1, of: list.length }));
        qc.invalidateQueries({ queryKey: ["checks"] });
      }
    } catch (e) {
      setUpError(e);
    }
    setUp(null);
  }
  const byPath = useMutation({
    mutationFn: () => api.post<{ batch: string; count: number }>("/api/checks/path", { path: folder.trim(), deep }),
    onSuccess: () => qc.invalidateQueries({ queryKey: ["checks"] }),
  });

  return (
    <div>
      <PageHeader title="檢查音檔"
        subtitle="匯入前先檢查聲音本身：背景音、雜音、回音、破音、音量和音質。每一項都通過才算「通過」；有問題的地方會列出時間，點一下就能聽。" />
      <div className="grid gap-6 lg:grid-cols-2">
        <Card title="1. 丟音檔進來">
          <div
            onDragOver={(e) => { e.preventDefault(); setDrag(true); }} onDragLeave={() => setDrag(false)}
            onDrop={(e) => { e.preventDefault(); setDrag(false); send(e.dataTransfer.files); }}
            onClick={() => fileInput.current?.click()}
            className={clsx("flex cursor-pointer flex-col items-center justify-center rounded-2xl border-2 border-dashed px-6 py-8 text-center transition",
              drag ? "border-brand-500 bg-brand-50 dark:bg-brand-900/20" : "border-zinc-300 hover:border-brand-400 dark:border-zinc-700")}>
            <Upload className="mb-2 size-7 text-brand-500" />
            <p className="font-medium">把錄音或影片拖到這裡，或點一下選檔</p>
            <p className="mt-1 text-xs text-zinc-500">一次可以很多個。超過 20 分鐘的檔案會平均抽 20 段、每段 1 分鐘來檢查。</p>
            <input ref={fileInput} type="file" multiple className="hidden" accept="audio/*,video/*,.mkv,.flv,.ts"
              onChange={(e) => { if (e.target.files) send(e.target.files); e.target.value = ""; }} />
          </div>
          {up && <div className="mt-3 text-xs"><div className="flex justify-between"><span className="truncate">{up.name}</span><span className="text-zinc-500">{up.n}/{up.of}</span></div><Progress value={up.progress} className="mt-1" /></div>}
          <ErrorText error={upError} />
          <div className="mt-4 border-t border-zinc-100 pt-3 dark:border-zinc-800">
            <Field label="或：檢查電腦上的資料夾（檔案很多時用這個，不會複製檔案）" hint={<>例如 <code className="kbd">D:\交付\clean</code>，子資料夾也會一起檢查。</>}>
              <div className="flex gap-2">
                <input className="input" value={folder} onChange={(e) => setFolder(e.target.value)} placeholder="D:\recordings" />
                <Button variant="secondary" className="shrink-0 whitespace-nowrap" onClick={() => byPath.mutate()} loading={byPath.isPending} disabled={!folder.trim()}>
                  <FolderSearch className="size-4" />檢查
                </Button>
              </div>
            </Field>
            <ErrorText error={byPath.error} />
          </div>
          <label className="mt-3 flex items-start gap-2 text-sm">
            <input type="checkbox" className="mt-1" checked={deep} onChange={(e) => setDeep(e.target.checked)} />
            <span>深入檢查：也用人聲分離檢查「說話時底下」的背景音
              <span className="block text-xs text-zinc-500">一般檢查只聽得到停頓時的背景。勾這個會慢很多（要用顯示卡），適合幾乎沒有停頓、或想再確認的檔案。</span></span>
          </label>
        </Card>
        <Card title="通過標準" actions={<Button size="sm" variant="ghost" onClick={() => setShowCriteria(!showCriteria)}>{showCriteria ? "收起" : "展開"}</Button>}>
          <p className="text-sm text-zinc-600 dark:text-zinc-300">
            只看聲音本身，不看是誰在說、說了什麼（那些匯入後會檢查）。結果分三種：
            <Badge tone="green">通過</Badge> 每一項都符合；<Badge tone="amber">勉強可用</Badge> 能用但不理想；<Badge tone="red">不通過</Badge> 有一項不符合，建議換一段。
            每一條的理由見 <Link to="/guide/13-ideal-audio" className="text-brand-600 underline">理想的訓練音檔</Link>。
          </p>
          {showCriteria && criteria.data && (
            <div className="mt-3 overflow-x-auto">
              <table className="w-full text-xs">
                <thead className="text-left text-zinc-500"><tr><th className="py-1 pr-2">項目</th><th className="pr-2">通過</th><th className="pr-2">勉強可用</th><th>不通過</th></tr></thead>
                <tbody>{criteria.data.map((c) => (
                  <tr key={c.label} className="border-t border-zinc-100 align-top dark:border-zinc-800">
                    <td className="py-1.5 pr-2 font-medium">{c.label}</td><td className="pr-2 text-emerald-700 dark:text-emerald-300">{c.pass}</td>
                    <td className="pr-2 text-amber-700 dark:text-amber-300">{c.warn}</td><td className="text-red-700 dark:text-red-300">{c.fail}</td>
                  </tr>))}</tbody>
              </table>
            </div>
          )}
        </Card>
      </div>

      <div className="mt-6 space-y-6">
        {batches.data?.length === 0 && <Card><Empty icon={<Stethoscope className="size-8" />} title="還沒有檢查過任何音檔" /></Card>}
        {batches.data?.map((b) => <BatchCard key={b.id} b={b} />)}
      </div>
    </div>
  );
}

function BatchCard({ b }: { b: Batch }) {
  const qc = useQueryClient();
  const [filter, setFilter] = useState<"all" | "fail" | "warn" | "pass">("all");
  const [importing, setImporting] = useState(false);
  const count = (v: string) => b.items.filter((i) => i.verdict === v).length;
  const pending = b.items.filter((i) => i.status === "queued" || i.status === "running").length;
  const shown = b.items.filter((i) => filter === "all" || i.verdict === filter);
  const recheck = useMutation({
    mutationFn: () => api.post(`/api/checks/${b.id}/recheck`, { deep: true }),
    onSuccess: () => qc.invalidateQueries({ queryKey: ["checks"] }),
  });
  const remove = useMutation({
    mutationFn: () => api.del(`/api/checks/batch/${b.id}`),
    onSuccess: () => qc.invalidateQueries({ queryKey: ["checks"] }),
  });
  return (
    <Card title={<span className="flex flex-wrap items-center gap-2">
      {new Date(b.created_at * 1000).toLocaleString("zh-TW", { hour12: false })}
      <span className="text-sm font-normal text-zinc-500">{b.items.length} 個檔案{b.root ? ` · ${b.root}` : ""}</span></span>}
      actions={<div className="flex flex-wrap gap-1">
        <Button size="sm" onClick={() => setImporting(true)} disabled={!count("pass") && !count("warn")}>匯入通過的</Button>
        <Button size="sm" variant="ghost" title="用人聲分離再檢查一次整批" onClick={() => recheck.mutate()} disabled={pending > 0}><RefreshCw className="size-3.5" />深入檢查</Button>
        <Button size="sm" variant="ghost" title="刪除這批檢查結果（資料夾裡的原始檔案不會被刪）" onClick={() => confirm("刪除這批檢查結果？上傳的複本會刪除；資料夾裡的原始檔案不會被刪。") && remove.mutate()}><Trash2 className="size-3.5" /></Button>
      </div>}>
      <div className="mb-3 flex flex-wrap items-center gap-2 text-sm">
        {([["all", `全部 ${b.items.length}`], ["fail", `不通過 ${count("fail")}`], ["warn", `勉強可用 ${count("warn")}`], ["pass", `通過 ${count("pass")}`]] as const).map(([k, l]) => (
          <button key={k} onClick={() => setFilter(k)}
            className={clsx("rounded-full px-3 py-1 text-xs", filter === k ? "bg-brand-600 text-white" : "bg-zinc-100 text-zinc-600 hover:bg-zinc-200 dark:bg-zinc-800 dark:text-zinc-300")}>{l}</button>
        ))}
        {pending > 0 && <span className="ml-auto flex min-w-48 items-center gap-2 text-xs text-zinc-500">
          <span className="truncate">{b.job?.message ?? "排隊中"}</span><Progress value={b.job?.progress ?? 0} className="w-24" /></span>}
      </div>
      <div className="divide-y divide-zinc-100 dark:divide-zinc-800">{shown.map((i) => <ItemRow key={i.id} item={i} />)}</div>
      {importing && <ImportModal batch={b} onClose={() => setImporting(false)} />}
    </Card>
  );
}

function ItemRow({ item }: { item: Item }) {
  const [open, setOpen] = useState(false);
  const player = usePlayer();
  const checks = item.result.checks ?? [];
  const bad = checks.filter((c) => c.level === "fail" || c.level === "warn");
  const v = item.verdict ? VERDICT[item.verdict] : null;
  return (
    <div className="py-2">
      <button className="flex w-full items-center gap-2 text-left" onClick={() => setOpen(!open)} disabled={!checks.length}>
        {checks.length ? (open ? <ChevronDown className="size-4 text-zinc-400" /> : <ChevronRight className="size-4 text-zinc-400" />) : <span className="w-4" />}
        <span className="w-20 shrink-0">
          {v ? <Badge tone={v[1]}>{v[0]}</Badge>
            : item.status === "failed" ? <Badge tone="red">讀不到</Badge>
              : item.status === "running" ? <Badge tone="brand">檢查中</Badge> : <Badge>等待中</Badge>}
        </span>
        <span className="min-w-0 flex-1 truncate text-sm" title={item.path}>{item.filename}</span>
        {item.meta?.imported && <Badge tone="blue">已匯入</Badge>}
        <span className="hidden flex-wrap justify-end gap-1 sm:flex">
          {bad.map((c) => <Badge key={c.key} tone={tone(c.level)}>{SHORT[c.key] ?? c.label}</Badge>)}
        </span>
        <span className="w-16 shrink-0 text-right text-xs tabular-nums text-zinc-500">{item.duration ? fmtMin(item.duration / 60) : ""}</span>
      </button>
      {item.status === "failed" && <p className="ml-6 mt-1 text-xs text-red-600">{item.result.error}</p>}
      {open && checks.length > 0 && (
        <div className="ml-6 mt-3 space-y-3">
          {item.result.timeline && item.duration ? <Timeline t={item.result.timeline} duration={item.duration} /> : null}
          <ul className="space-y-2">
            {checks.map((c) => (
              <li key={c.key} className="flex gap-2 text-sm">
                <LevelIcon level={c.level} />
                <div className="min-w-0">
                  <div><span className="font-medium">{c.label}</span>：{c.value}</div>
                  {c.detail && <div className="text-xs text-zinc-500">{c.detail}</div>}
                  {c.ranges.length > 0 && (
                    <div className="mt-1 flex flex-wrap gap-1">
                      {c.ranges.map(([a, b]) => (
                        <PlayButton key={`${a}-${b}`} small player={player} label={`${fmtT(a)}${b - a >= 1 ? `–${fmtT(b)}` : ""}`}
                          url={`/api/checks/${item.id}/audio?start=${a}&end=${b}`} />
                      ))}
                    </div>
                  )}
                </div>
              </li>
            ))}
          </ul>
          {item.result.info && (
            <p className="text-xs text-zinc-500">
              {[item.result.info.codec, item.result.info.sr && `${item.result.info.sr / 1000} kHz`, item.result.info.channels === 1 ? "單聲道" : item.result.info.channels === 2 ? "立體聲" : null,
                item.result.info.kbps && `${item.result.info.kbps} kb/s`].filter(Boolean).join(" · ")}
              {" · "}說話 {fmtMin(item.result.info.speech_seconds / 60)}
              {item.result.info.sampled && `（很長，只抽 ${fmtMin(item.result.info.analysed / 60)} 檢查）`}
            </p>
          )}
        </div>
      )}
    </div>
  );
}

function Timeline({ t, duration }: { t: NonNullable<Item["result"]["timeline"]>; duration: number }) {
  const pos = (a: number, b: number) => ({ left: `${(a / duration) * 100}%`, width: `${Math.max(0.15, ((b - a) / duration) * 100)}%` });
  return (
    <div>
      <div className="relative h-6 overflow-hidden rounded-md bg-zinc-100 dark:bg-zinc-800" title="灰：說話；紅：背景音；橘：破音">
        {t.windows.length > 1 && t.windows.map(([a, b]) => <div key={`w${a}`} className="absolute inset-y-0 bg-zinc-200 dark:bg-zinc-700" style={pos(a, b)} />)}
        {t.speech.map(([a, b]) => <div key={`s${a}`} className="absolute inset-y-1.5 bg-zinc-400/70 dark:bg-zinc-500" style={pos(a, b)} />)}
        {t.background.map(([a, b]) => <div key={`b${a}`} className="absolute inset-y-0 bg-red-500/70" style={pos(a, b)} />)}
        {t.clipping.map(([a, b]) => <div key={`c${a}`} className="absolute inset-y-0 bg-orange-500" style={pos(a, b)} />)}
      </div>
      <div className="mt-1 flex gap-3 text-[11px] text-zinc-500">
        <span><i className="mr-1 inline-block size-2 rounded-sm bg-zinc-400" />說話</span>
        <span><i className="mr-1 inline-block size-2 rounded-sm bg-red-500" />背景音</span>
        <span><i className="mr-1 inline-block size-2 rounded-sm bg-orange-500" />破音</span>
        {t.windows.length > 1 && <span>淺色區塊是抽查的段落</span>}
      </div>
    </div>
  );
}

function ImportModal({ batch, onClose }: { batch: Batch; onClose: () => void }) {
  const qc = useQueryClient();
  const voices = useQuery({ queryKey: ["voices"], queryFn: () => api.get<Voice[]>("/api/voices") });
  const [voice, setVoice] = useState("");
  const [language, setLanguage] = useState("");
  const [withWarn, setWithWarn] = useState(false);
  const ids = batch.items.filter((i) => !i.meta?.imported && (i.verdict === "pass" || (withWarn && i.verdict === "warn"))).map((i) => i.id);
  const run = useMutation({
    mutationFn: () => api.post<{ created: number }>("/api/checks/import", { ids, voice_hint: voice || null, language: language || null }),
    onSuccess: () => { qc.invalidateQueries({ queryKey: ["checks"] }); qc.invalidateQueries({ queryKey: ["sources"] }); },
  });
  return (
    <Modal open onClose={onClose} title="匯入通過的檔案">
      {run.data ? (
        <div className="space-y-3 text-sm">
          <p>已匯入 {run.data.created} 個檔案，正在處理。</p>
          <Link to="/import"><Button>前往匯入錄音看進度</Button></Link>
        </div>
      ) : (
        <div className="space-y-4">
          <Field label="這些錄音裡主要是誰？">
            <select className="input" value={voice} onChange={(e) => setVoice(e.target.value)}>
              <option value="">自動分辨（多人或不確定）</option>
              {voices.data?.map((v) => <option key={v.id} value={v.id}>{v.name}{v.consent_ok ? "" : "（尚未同意）"}</option>)}
            </select>
          </Field>
          <Field label="語言" hint="檔名或資料夾名稱裡的語言、情緒標籤會照常套用。">
            <select className="input" value={language} onChange={(e) => setLanguage(e.target.value)}>
              <option value="">自動判斷</option>
              {Object.entries(LANGS).map(([k, l]) => <option key={k} value={k}>{l}</option>)}
            </select>
          </Field>
          <label className="flex items-center gap-2 text-sm"><input type="checkbox" checked={withWarn} onChange={(e) => setWithWarn(e.target.checked)} />也匯入「勉強可用」的</label>
          <ErrorText error={run.error} />
          <Button className="w-full" onClick={() => run.mutate()} loading={run.isPending} disabled={!ids.length}>匯入 {ids.length} 個檔案</Button>
        </div>
      )}
    </Modal>
  );
}

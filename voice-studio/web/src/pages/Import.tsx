import { useRef, useState } from "react";
import { Link } from "react-router";
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import clsx from "clsx";
import { Download, FileSpreadsheet, FolderOpen, FolderUp, RefreshCw, Trash2, Upload, Users, X } from "lucide-react";
import { api, EMOTION_LABEL, EMOTIONS, fmtMin, type Source, type Voice } from "../api";
import { Badge, Button, Card, Empty, ErrorText, Field, Modal, PageHeader, Progress, Wave } from "../ui";

type SourceRow = Source & {
  approved: number; unassigned: number;
  job: { id: string; status: string; progress: number; message: string } | null;
};
type Cluster = { cluster: number; n: number; secs: number; samples: string[]; voice_id: string | null; rejected: number };
type LabelList = { id: string; filename: string; count: number; errors: string[]; emotions: Record<string, number> };
type FolderResult = {
  found: number; created: number; labelled: Record<string, number>; list: string | null; list_errors: string[];
};

const MEDIA = /\.(mp4|mkv|mov|webm|flv|ts|avi|wav|mp3|m4a|aac|flac|ogg|opus|wma)$/i;
const LIST = /\.(xlsx|xlsm|csv)$/i;
const FROM: Record<string, string> = { list: "清單", filename: "檔名", folder: "資料夾名稱", form: "上面選的情緒" };

function uploadWithProgress(file: File, fields: Record<string, string>, onProgress: (f: number) => void) {
  return new Promise<{ source: Source; label_from: string }>((resolve, reject) => {
    const fd = new FormData();
    fd.append("file", file);
    Object.entries(fields).forEach(([k, v]) => fd.append(k, v));
    const x = new XMLHttpRequest();
    x.open("POST", "/api/sources/upload");
    x.upload.onprogress = (e) => e.lengthComputable && onProgress(e.loaded / e.total);
    x.onload = () => (x.status < 300 ? resolve(JSON.parse(x.responseText)) : reject(new Error(x.responseText || x.statusText)));
    x.onerror = () => reject(new Error("上傳失敗（連線中斷）"));
    x.send(fd);
  });
}

export default function ImportPage() {
  const qc = useQueryClient();
  const voices = useQuery({ queryKey: ["voices"], queryFn: () => api.get<Voice[]>("/api/voices") });
  const sources = useQuery({ queryKey: ["sources"], queryFn: () => api.get<SourceRow[]>("/api/sources"), refetchInterval: 3000 });
  const [opts, setOpts] = useState({ voice_hint: "", language: "", separate: false, emotion: "" });
  const [drag, setDrag] = useState(false);
  const [queue, setQueue] = useState<{ name: string; progress: number; error?: string }[]>([]);
  const [folder, setFolder] = useState("");
  const [clusterFor, setClusterFor] = useState<SourceRow | null>(null);
  const [labelList, setLabelList] = useState<LabelList | null>(null);
  const [listError, setListError] = useState<unknown>(null);
  const [labelled, setLabelled] = useState<Record<string, number>>({});
  const fileInput = useRef<HTMLInputElement>(null);
  const folderInput = useRef<HTMLInputElement>(null);
  const listInput = useRef<HTMLInputElement>(null);
  const consented = (voices.data ?? []).filter((v) => v.consent_ok);

  async function uploadList(f: File): Promise<LabelList | null> {
    const fd = new FormData();
    fd.append("file", f);
    setListError(null);
    try {
      const l = await api.post<LabelList>("/api/import-labels", fd);
      setLabelList(l);
      return l;
    } catch (e) {
      setListError(e);
      return null;
    }
  }

  // a dropped or picked .xlsx / .csv is the emotion list; it is read first so the recordings next to it use it
  async function uploadFiles(files: FileList | File[]) {
    const all = Array.from(files);
    const lists = all.filter((f) => LIST.test(f.name));
    const media = all.filter((f) => MEDIA.test(f.name) || (!LIST.test(f.name) && /^(audio|video)\//.test(f.type)));
    let list = labelList;
    if (lists.length) list = (await uploadList(lists.find((f) => /清單|label|情緒|標籤/i.test(f.name)) ?? lists[0])) ?? list;
    if (!media.length) return;
    const fields = { voice_hint: opts.voice_hint, language: opts.language, separate: String(opts.separate), emotion: opts.emotion,
      labels_id: list?.id ?? "" };
    const key = (f: File) => f.webkitRelativePath || f.name;
    setQueue((q) => [...q, ...media.map((f) => ({ name: key(f), progress: 0 }))]);
    setLabelled({});
    for (const f of media) {
      try {
        const r = await uploadWithProgress(f, { ...fields, relpath: f.webkitRelativePath },
          (p) => setQueue((q) => q.map((x) => (x.name === key(f) ? { ...x, progress: p } : x))));
        if (r.source.emotion) setLabelled((c) => ({ ...c, [r.label_from]: (c[r.label_from] ?? 0) + 1 }));
        setQueue((q) => q.filter((x) => x.name !== key(f)));
      } catch (e) {
        setQueue((q) => q.map((x) => (x.name === key(f) ? { ...x, error: String((e as Error).message) } : x)));
      }
      qc.invalidateQueries({ queryKey: ["sources"] });
    }
  }
  const importFolder = useMutation({
    mutationFn: () => api.post<FolderResult>("/api/sources/import-path",
      { path: folder.trim(), voice_hint: opts.voice_hint || null, language: opts.language || null, separate: opts.separate,
        emotion: opts.emotion || null, labels_id: labelList?.id ?? null }),
    onSuccess: () => qc.invalidateQueries({ queryKey: ["sources"] }),
  });
  const reprocess = useMutation({
    mutationFn: (s: SourceRow) => api.post(`/api/sources/${s.id}/process`, { separate: opts.separate }),
    onSuccess: () => qc.invalidateQueries({ queryKey: ["sources"] }),
  });
  const setEmotion = useMutation({
    mutationFn: ({ s, emotion }: { s: SourceRow; emotion: string }) => api.patch(`/api/sources/${s.id}`, { emotion }),
    onSuccess: () => { qc.invalidateQueries({ queryKey: ["sources"] }); qc.invalidateQueries({ queryKey: ["voices"] }); },
  });
  const remove = useMutation({
    mutationFn: (s: SourceRow) => api.del(`/api/sources/${s.id}`),
    onSuccess: () => { qc.invalidateQueries({ queryKey: ["sources"] }); qc.invalidateQueries({ queryKey: ["voices"] }); },
  });

  return (
    <div>
      <PageHeader title="匯入錄音"
        subtitle="丟進長影片或錄音就好：平台會自動抽出聲音、切成 2–15 秒的句子、辨認是誰在說話、用兩個語音辨識模型轉成文字並互相比對。原始檔案不會被修改。" />
      {voices.data && consented.length === 0 && (
        <div className="mb-6 rounded-xl border border-amber-300 bg-amber-50 px-4 py-3 text-sm text-amber-800 dark:border-amber-800 dark:bg-amber-950/40 dark:text-amber-200">
          還沒有任何一個聲音有完整的同意紀錄。可以先匯入，但要到 <Link to="/voices" className="underline">聲音與同意</Link> 填好同意紀錄才能訓練。
        </div>
      )}
      <div className="grid gap-6 lg:grid-cols-3">
        <Card title="1. 匯入設定" className="lg:col-span-1">
          <div className="space-y-4">
            <Field label="這些錄音裡主要是誰？"
              hint="選定一個聲音時，跟他不像的片段會標記出來。錄音裡有好幾個人時選「自動分辨」，之後再把每一群指定給對的人。">
              <select className="input" value={opts.voice_hint} onChange={(e) => setOpts({ ...opts, voice_hint: e.target.value })}>
                <option value="">自動分辨（多人或不確定）</option>
                {voices.data?.map((v) => <option key={v.id} value={v.id}>{v.name}{v.consent_ok ? "" : "（尚未同意）"}</option>)}
              </select>
            </Field>
            <Field label="語言" hint="不確定就選自動；日英混雜也可以。">
              <select className="input" value={opts.language} onChange={(e) => setOpts({ ...opts, language: e.target.value })}>
                <option value="">自動判斷</option>
                <option value="ja">日文</option>
                <option value="en">英文</option>
                <option value="zh">中文</option>
              </select>
            </Field>
            <Field label="情緒／風格（選填）"
              hint="這一批全部都是同一種情緒時才選，例如一個資料夾的生氣台詞。混在一起的請留空，改用下面的清單或檔名標記。">
              <select className="input" value={opts.emotion} onChange={(e) => setOpts({ ...opts, emotion: e.target.value })}>
                <option value="">不標記</option>
                {EMOTIONS.map(([k, l]) => <option key={k} value={k}>{l}</option>)}
              </select>
            </Field>
            <div id="labels" className="rounded-xl border border-zinc-200 p-3 text-sm dark:border-zinc-800">
              <div className="mb-1 font-medium">每個檔案不同情緒？這樣標</div>
              <ul className="mb-3 list-disc space-y-1 pl-5 text-xs text-zinc-600 dark:text-zinc-400">
                <li><b>檔名</b>：加上括號標籤，例如 <code className="kbd">0815直播[生氣].mp4</code>、<code className="kbd">【開心】雜談.wav</code>，或開頭 <code className="kbd">生氣_0815.wav</code>。</li>
                <li><b>Excel／CSV 清單</b>：一欄檔名、一欄情緒（可再加一欄語言）。檔案很多或不想改檔名時用這個。</li>
                <li>放在名叫 <code className="kbd">生氣</code>、<code className="kbd">開心</code> 的資料夾裡也可以（匯入整個資料夾時）。</li>
              </ul>
              {labelList ? (
                <div className="rounded-lg bg-emerald-50 px-3 py-2 text-xs text-emerald-800 dark:bg-emerald-950/40 dark:text-emerald-200">
                  <div className="flex items-start justify-between gap-2">
                    <span><FileSpreadsheet className="mr-1 inline size-3.5" />已讀取「{labelList.filename}」：{labelList.count} 個檔案
                      {Object.keys(labelList.emotions).length > 0 && <>（{Object.entries(labelList.emotions).map(([k, n]) => `${EMOTION_LABEL[k]} ${n}`).join("、")}）</>}
                    </span>
                    <button title="不用這份清單" onClick={() => setLabelList(null)}><X className="size-3.5" /></button>
                  </div>
                  {labelList.errors.length > 0 && (
                    <ul className="mt-1 list-disc pl-4 text-amber-700 dark:text-amber-300">{labelList.errors.map((e) => <li key={e}>{e}</li>)}</ul>
                  )}
                  <div className="mt-1 text-zinc-500">接下來加入的檔案會照這份清單標情緒。</div>
                </div>
              ) : (
                <div className="flex flex-wrap gap-2">
                  <Button size="sm" variant="secondary" onClick={() => listInput.current?.click()}>
                    <FileSpreadsheet className="size-3.5" />上傳情緒清單
                  </Button>
                  <a className="inline-flex items-center gap-1 px-2 text-xs text-brand-600 hover:underline"
                    href="/api/import-labels/template.csv" download>
                    <Download className="size-3.5" />下載範本
                  </a>
                </div>
              )}
              <input ref={listInput} type="file" className="hidden" accept=".xlsx,.xlsm,.csv"
                onChange={(e) => { if (e.target.files?.[0]) uploadList(e.target.files[0]); e.target.value = ""; }} />
              <ErrorText error={listError} />
            </div>
            <label className="flex items-start gap-2 text-sm">
              <input type="checkbox" className="mt-1" checked={opts.separate} onChange={(e) => setOpts({ ...opts, separate: e.target.checked })} />
              <span>去除背景音樂（BS-RoFormer 人聲分離）<span className="block text-xs text-zinc-500">只在有背景音樂或遊戲音效時勾選。乾淨的錄音不要勾，處理會改變一點音色，而且比較慢。</span></span>
            </label>
          </div>
        </Card>
        <Card title="2. 加入檔案" className="lg:col-span-2">
          <div
            onDragOver={(e) => { e.preventDefault(); setDrag(true); }} onDragLeave={() => setDrag(false)}
            onDrop={(e) => { e.preventDefault(); setDrag(false); uploadFiles(e.dataTransfer.files); }}
            onClick={() => fileInput.current?.click()}
            className={clsx("flex cursor-pointer flex-col items-center justify-center rounded-2xl border-2 border-dashed px-6 py-10 text-center transition",
              drag ? "border-brand-500 bg-brand-50 dark:bg-brand-900/20" : "border-zinc-300 hover:border-brand-400 dark:border-zinc-700")}>
            <Upload className="mb-2 size-8 text-brand-500" />
            <p className="font-medium">把影片或錄音拖到這裡，或點一下選檔</p>
            <p className="mt-1 text-xs text-zinc-500">mp4、mkv、mov、wav、mp3、m4a、flac… 一次可以選很多個。情緒清單（.xlsx、.csv）也可以一起拖進來。</p>
            <input ref={fileInput} type="file" multiple className="hidden" accept="audio/*,video/*,.mkv,.flv,.ts,.xlsx,.xlsm,.csv"
              onChange={(e) => { if (e.target.files) uploadFiles(e.target.files); e.target.value = ""; }} />
          </div>
          <div className="mt-2 flex flex-wrap items-center gap-2 text-xs text-zinc-500">
            <Button size="sm" variant="ghost" onClick={() => folderInput.current?.click()}><FolderUp className="size-3.5" />選整個資料夾上傳</Button>
            <span>資料夾裡的子資料夾名稱（例如「生氣」）和情緒清單會一起套用。</span>
            <input ref={folderInput} type="file" multiple className="hidden"
              {...({ webkitdirectory: "", directory: "" } as Record<string, string>)}
              onChange={(e) => { if (e.target.files) uploadFiles(e.target.files); e.target.value = ""; }} />
          </div>
          {Object.keys(labelled).length > 0 && (
            <p className="mt-2 text-sm text-emerald-600">
              已標上情緒：{Object.entries(labelled).map(([k, n]) => `${n} 個來自${FROM[k] ?? k}`).join("、")}。可以在下方表格的「情緒」欄修改。
            </p>
          )}
          {queue.length > 0 && (
            <ul className="mt-4 space-y-2 text-sm">
              {queue.map((q) => (
                <li key={q.name}>
                  <div className="flex justify-between"><span className="truncate">{q.name}</span><span className="text-zinc-500">{q.error ? "失敗" : `${Math.round(q.progress * 100)}%`}</span></div>
                  {q.error ? <ErrorText error={q.error} /> : <Progress value={q.progress} className="mt-1" />}
                </li>
              ))}
            </ul>
          )}
          <div className="mt-5 border-t border-zinc-100 pt-4 dark:border-zinc-800">
            <Field label="或：直接匯入電腦上的資料夾（大量檔案建議用這個，不會複製檔案）"
              hint={<>例如 <code className="kbd">D:\錄音\2026</code>。子資料夾裡的影音檔也會一起匯入；已匯入過的會自動跳過。資料夾裡放一份情緒清單（.xlsx 或 .csv）會自動讀取。</>}>
              <div className="flex gap-2">
                <input className="input" value={folder} onChange={(e) => setFolder(e.target.value)} placeholder="D:\recordings" />
                <Button variant="secondary" className="shrink-0 whitespace-nowrap" onClick={() => importFolder.mutate()} loading={importFolder.isPending} disabled={!folder.trim()}>
                  <FolderOpen className="size-4" />匯入
                </Button>
              </div>
            </Field>
            {importFolder.data && (
              <div className="mt-2 text-sm text-emerald-600">
                <p>找到 {importFolder.data.found} 個檔案，新增 {importFolder.data.created} 個。
                  {importFolder.data.list && <>讀取了資料夾裡的情緒清單「{importFolder.data.list}」。</>}
                  {Object.keys(importFolder.data.labelled).length > 0 &&
                    <>已標上情緒：{Object.entries(importFolder.data.labelled).map(([k, n]) => `${n} 個來自${FROM[k] ?? k}`).join("、")}。</>}
                </p>
                {importFolder.data.list_errors.length > 0 && (
                  <ul className="mt-1 list-disc pl-5 text-xs text-amber-600">{importFolder.data.list_errors.map((e) => <li key={e}>{e}</li>)}</ul>
                )}
              </div>
            )}
            <ErrorText error={importFolder.error} />
          </div>
        </Card>
      </div>

      <Card title="3. 處理狀態" className="mt-6"
        actions={<Link to="/review"><Button size="sm">前往檢查資料</Button></Link>}>
        {!sources.data?.length ? (
          <Empty icon={<Upload className="size-8" />} title="還沒有匯入任何錄音" />
        ) : (
          <div className="overflow-x-auto">
            <table className="w-full text-sm">
              <thead className="text-left text-xs text-zinc-500">
                <tr><th className="py-2 pr-3">檔案</th><th className="pr-3">長度</th><th className="pr-3">狀態</th><th className="pr-3">片段</th><th className="pr-3">誰</th><th className="pr-3">情緒</th><th /></tr>
              </thead>
              <tbody>
                {sources.data.map((s) => {
                  const running = s.job && (s.job.status === "running" || s.job.status === "queued");
                  const failed = s.job?.status === "failed";
                  const hint = voices.data?.find((v) => v.id === s.voice_hint)?.name;
                  return (
                    <tr key={s.id} className="border-t border-zinc-100 align-middle dark:border-zinc-800">
                      <td className="max-w-xs truncate py-2 pr-3" title={s.path}>{s.filename}</td>
                      <td className="pr-3 tabular-nums text-zinc-500">{s.duration ? fmtMin(s.duration / 60) : "—"}</td>
                      <td className="min-w-40 pr-3">
                        {running ? (<div><div className="text-xs text-zinc-500">{s.job!.message}</div><Progress value={s.job!.progress} className="mt-1" /></div>)
                          : failed ? <Link to="/jobs"><Badge tone="red">失敗 · 看原因</Badge></Link>
                            : s.status === "ready" ? <Badge tone="green">完成</Badge> : <Badge>{s.status}</Badge>}
                      </td>
                      <td className="pr-3 tabular-nums">{s.segments}<span className="text-xs text-zinc-500">（已核可 {s.approved}）</span></td>
                      <td className="pr-3">
                        {s.unassigned > 0 && s.status === "ready"
                          ? <Button size="sm" variant="secondary" onClick={() => setClusterFor(s)}><Users className="size-3.5" />{s.unassigned} 段待指定</Button>
                          : <span className="text-xs text-zinc-500">{hint ?? "自動"}</span>}
                      </td>
                      <td className="pr-3">
                        <select className="input w-28 py-1 text-xs" value={s.emotion ?? ""} title="整個檔案的情緒；你逐句改過的不會被覆蓋"
                          onChange={(e) => setEmotion.mutate({ s, emotion: e.target.value })}>
                          <option value="">{s.emotion ? "清除" : "—"}</option>
                          {EMOTIONS.map(([k, l]) => <option key={k} value={k}>{l}</option>)}
                        </select>
                      </td>
                      <td className="whitespace-nowrap text-right">
                        <Button size="sm" variant="ghost" title="重新處理" onClick={() => reprocess.mutate(s)} disabled={!!running}><RefreshCw className="size-3.5" /></Button>
                        <Button size="sm" variant="ghost" title="移除（含片段）" onClick={() => confirm(`移除「${s.filename}」和它的所有片段？${s.path.includes("_uploads") ? "上傳的複本也會刪除。" : "原始檔案不會被刪除。"}`) && remove.mutate(s)}><Trash2 className="size-3.5" /></Button>
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        )}
      </Card>
      {clusterFor && <ClusterModal source={clusterFor} voices={voices.data ?? []} onClose={() => setClusterFor(null)} />}
    </div>
  );
}

function ClusterModal({ source, voices, onClose }: { source: SourceRow; voices: Voice[]; onClose: () => void }) {
  const qc = useQueryClient();
  const clusters = useQuery({ queryKey: ["clusters", source.id], queryFn: () => api.get<Cluster[]>(`/api/sources/${source.id}/clusters`) });
  const assign = useMutation({
    mutationFn: ({ cluster, voice_id }: { cluster: number; voice_id: string }) =>
      api.post(`/api/sources/${source.id}/clusters/${cluster}/assign`, voice_id === "__none" ? { reject: true } : { voice_id }),
    onSuccess: () => { qc.invalidateQueries({ queryKey: ["clusters", source.id] }); qc.invalidateQueries({ queryKey: ["sources"] }); },
  });
  return (
    <Modal open onClose={onClose} title={`誰在說話？— ${source.filename}`} wide>
      <p className="mb-4 text-sm text-zinc-500">平台把聲音相似的片段分成幾群。聽一下每群的樣本，把它指定給對的聲音；不要的人（例如來賓、遊戲角色）選「不是任何人」，那些片段就不會進入訓練。</p>
      <div className="space-y-4">
        {clusters.data?.map((c) => (
          <div key={c.cluster} className="rounded-xl border border-zinc-200 p-3 dark:border-zinc-800">
            <div className="mb-2 flex items-center justify-between gap-3">
              <div className="font-medium">第 {c.cluster + 1} 群 <span className="text-sm text-zinc-500">{c.n} 段 · {fmtMin(c.secs / 60)}</span></div>
              <select className="input w-56" value={c.rejected === c.n ? "__none" : c.voice_id ?? ""}
                onChange={(e) => assign.mutate({ cluster: c.cluster, voice_id: e.target.value })}>
                <option value="" disabled>指定給…</option>
                {voices.map((v) => <option key={v.id} value={v.id}>{v.name}</option>)}
                <option value="__none">不是任何人（不用）</option>
              </select>
            </div>
            <div className="space-y-2">{c.samples.map((id) => <Wave key={id} src={`/api/segments/${id}/audio`} compact />)}</div>
          </div>
        ))}
        {clusters.data?.length === 0 && <Empty title="沒有需要指定的群組" />}
      </div>
    </Modal>
  );
}

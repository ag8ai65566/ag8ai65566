import { useEffect, useRef, useState } from "react";
import { Link } from "react-router";
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import clsx from "clsx";
import { MessageSquareQuote, Pause, Play, Plus, Scissors, Trash2, Upload, Wand2 } from "lucide-react";
import { api, EMOTIONS, LANGS, type Job, type Model, type Phrase, type Segment, type Voice } from "../api";
import { Badge, Button, Card, ErrorText, Field, Modal, PlayButton, Progress, usePlayer } from "../ui";

const splitList = (s: string) => s.split(/[,，、\n]/).map((x) => x.trim()).filter(Boolean);
const pct = (x: number | null | undefined) => (x == null ? "—" : `${Math.round(x * 100)}%`);

/** Catchphrases of one voice: spelling, how often they are in the data, original recordings, model check. */
export function PhrasesCard({ voice }: { voice: Voice }) {
  const qc = useQueryClient();
  const key = ["phrases", voice.id];
  const list = useQuery({ queryKey: key, queryFn: () => api.get<Phrase[]>(`/api/voices/${voice.id}/phrases`) });
  const models = useQuery({ queryKey: ["models", voice.id], queryFn: () => api.get<Model[]>(`/api/models?voice_id=${voice.id}`) });
  const inv = () => { qc.invalidateQueries({ queryKey: key }); qc.invalidateQueries({ queryKey: ["phrases", voice.id, "light"] }); };
  const [form, setForm] = useState({ text: "", variants: "", lang: "" });
  const add = useMutation({
    mutationFn: () => api.post(`/api/voices/${voice.id}/phrases`, { text: form.text, variants: splitList(form.variants), lang: form.lang || null }),
    onSuccess: () => { setForm({ text: "", variants: "", lang: "" }); inv(); },
  });
  const unifyAll = useMutation({ mutationFn: () => api.post<{ changed: number }>(`/api/voices/${voice.id}/phrases/unify`), onSuccess: inv });
  const [modelId, setModelId] = useState("");
  useEffect(() => { if (!modelId && models.data?.length) setModelId(models.data[0].id); }, [models.data, modelId]);
  const [jobId, setJobId] = useState<string | null>(null);
  const check = useMutation({
    mutationFn: () => api.post<Job>(`/api/voices/${voice.id}/phrases/check`, { model_id: modelId }),
    onSuccess: (j) => setJobId(j.id),
  });
  const job = useQuery({
    queryKey: ["job", jobId], enabled: !!jobId, queryFn: () => api.get<Job>(`/api/jobs/${jobId}`),
    refetchInterval: (q) => (q.state.data && ["done", "failed", "canceled"].includes(q.state.data.status) ? false : 1500),
  });
  useEffect(() => { if (job.data?.status === "done") inv(); }, [job.data?.status]); // eslint-disable-line react-hooks/exhaustive-deps
  const phrases = list.data ?? [];
  const otherSpellings = phrases.reduce((n, p) => n + (p.counts.other_spellings ?? 0), 0);
  const running = !!job.data && ["queued", "running"].includes(job.data.status);

  return (
    <Card title={<span className="flex items-center gap-2"><MessageSquareQuote className="size-4" />口頭禪（{phrases.length}）</span>}
      actions={otherSpellings > 0 ? <Button size="sm" variant="secondary" loading={unifyAll.isPending}
        onClick={() => confirm(`把 ${otherSpellings} 段裡的其他寫法都改成登記的寫法？`) && unifyAll.mutate()}>統一全部寫法</Button> : undefined}>
      <p className="mb-3 text-sm text-zinc-500">
        登記這個人最有特色的口頭禪。平台會：匯入時提示語音辨識用同一種寫法；顯示訓練資料裡出現幾次；合成時把口頭禪換成本人的原音（每個口頭禪收 2–5 段不同語氣的原音最好）；檢查模型自己念得像不像。
      </p>
      <div className="grid gap-2 rounded-xl bg-zinc-50 p-3 sm:grid-cols-[1fr_1fr_110px_auto] dark:bg-zinc-800/50">
        <input className="input" placeholder="寫法，例如 えっとね" value={form.text} onChange={(e) => setForm({ ...form, text: e.target.value })} />
        <input className="input" placeholder="其他寫法（用逗號分隔，選填）" value={form.variants} onChange={(e) => setForm({ ...form, variants: e.target.value })} />
        <select className="input" value={form.lang} onChange={(e) => setForm({ ...form, lang: e.target.value })}>
          <option value="">任何語言</option><option value="ja">日文</option><option value="en">英文</option><option value="zh">中文</option>
        </select>
        <Button onClick={() => add.mutate()} disabled={!form.text.trim()} loading={add.isPending}><Plus className="size-4" />登記</Button>
      </div>
      <ErrorText error={add.error} />
      {unifyAll.data && <p className="mt-2 text-sm text-emerald-600">改了 {unifyAll.data.changed} 段。</p>}

      <div className="mt-4 space-y-3">
        {phrases.map((p) => <PhraseRow key={p.id} p={p} voice={voice} modelId={modelId} onChange={inv} />)}
      </div>

      {phrases.length > 0 && (
        <div className="mt-5 border-t border-zinc-100 pt-4 dark:border-zinc-800">
          <div className="mb-2 text-sm font-medium">模型自己念得像不像？</div>
          <p className="mb-2 text-xs text-zinc-500">用模型單獨念每個口頭禪（不換原音），和原音比：辨識出來對不對、聲紋像不像、長度和本人差多少（念太快或太慢就是沒學到那個節奏）。</p>
          {!models.data?.length ? <p className="text-sm text-zinc-500">這個聲音還沒有模型。</p> : (
            <div className="flex flex-wrap items-center gap-2">
              <select className="input max-w-xs" value={modelId} onChange={(e) => setModelId(e.target.value)}>
                {models.data.map((m) => <option key={m.id} value={m.id}>{m.name}</option>)}
              </select>
              <Button variant="secondary" onClick={() => check.mutate()} loading={check.isPending} disabled={running || !modelId}><Wand2 className="size-4" />檢查念法</Button>
              {running && <div className="min-w-40 flex-1"><div className="text-xs text-zinc-500">{job.data!.message}</div><Progress value={job.data!.progress} /></div>}
              {job.data?.status === "failed" && <ErrorText error={job.data.message} />}
            </div>
          )}
          <ErrorText error={check.error} />
        </div>
      )}
    </Card>
  );
}

function PhraseRow({ p, voice, modelId, onChange }: { p: Phrase; voice: Voice; modelId: string; onChange: () => void }) {
  const player = usePlayer();
  const [editing, setEditing] = useState(false);
  const [f, setF] = useState({ text: p.text, variants: p.variants.join("、") });
  const [adding, setAdding] = useState(false);
  const save = useMutation({ mutationFn: () => api.patch(`/api/phrases/${p.id}`, { text: f.text, variants: splitList(f.variants) }), onSuccess: () => { setEditing(false); onChange(); } });
  const del = useMutation({ mutationFn: () => api.del(`/api/phrases/${p.id}`), onSuccess: onChange });
  const unify = useMutation({ mutationFn: () => api.post(`/api/phrases/${p.id}/unify`), onSuccess: onChange });
  const delClip = useMutation({ mutationFn: (cid: string) => api.del(`/api/phrases/${p.id}/clips/${cid}`), onSuccess: onChange });
  const clipEmotion = useMutation({ mutationFn: ({ cid, emotion }: { cid: string; emotion: string }) => api.patch(`/api/phrases/${p.id}/clips/${cid}`, { emotion }), onSuccess: onChange });
  const c = p.counts;
  const chk = modelId ? p.checks?.[modelId] : undefined;
  const speed = chk?.dur_ratio == null ? null : chk.dur_ratio < 0.9 ? `比本人快 ${Math.round((1 - chk.dur_ratio) * 100)}%`
    : chk.dur_ratio > 1.1 ? `比本人慢 ${Math.round((chk.dur_ratio - 1) * 100)}%` : "長度和本人差不多";
  return (
    <div className="rounded-xl border border-zinc-200 p-3 dark:border-zinc-800">
      <div className="flex flex-wrap items-start gap-2">
        {editing ? (
          <div className="grid flex-1 gap-2 sm:grid-cols-2">
            <input className="input" value={f.text} onChange={(e) => setF({ ...f, text: e.target.value })} />
            <input className="input" value={f.variants} onChange={(e) => setF({ ...f, variants: e.target.value })} placeholder="其他寫法" />
          </div>
        ) : (
          <div className="min-w-0 flex-1">
            <div className="flex flex-wrap items-center gap-1.5">
              <span className="text-base font-semibold">「{p.text}」</span>
              {p.lang && <Badge>{LANGS[p.lang] ?? p.lang}</Badge>}
              {p.variants.map((v) => <span key={v} className="rounded-full bg-zinc-100 px-2 py-0.5 text-[11px] text-zinc-500 line-through decoration-zinc-400 dark:bg-zinc-800">{v}</span>)}
            </div>
            <div className="mt-1 text-xs text-zinc-500">
              訓練資料裡 {c.segments ?? 0} 段（已核可 {c.approved ?? 0}）
              <Link to={`/review?voice=${voice.id}&q=${encodeURIComponent(p.text)}`} className="ml-1 text-brand-600 underline">看這些片段</Link>
              {(c.other_spellings ?? 0) > 0 && <> · <span className="text-amber-700 dark:text-amber-300">還有 {c.other_spellings} 段用別的寫法</span>
                <button className="ml-1 text-brand-600 underline" onClick={() => unify.mutate()}>統一寫法</button></>}
              {(c.segments ?? 0) < 20 && <span className="ml-1 text-amber-700 dark:text-amber-300">· 出現不到 20 次，模型可能學不到它的念法，用原音比較保險</span>}
            </div>
          </div>
        )}
        <div className="flex shrink-0 gap-1">
          {editing ? <>
            <Button size="sm" onClick={() => save.mutate()} loading={save.isPending}>儲存</Button>
            <Button size="sm" variant="ghost" onClick={() => setEditing(false)}>取消</Button>
          </> : <>
            <Button size="sm" variant="ghost" onClick={() => setEditing(true)}>編輯</Button>
            <Button size="sm" variant="ghost" onClick={() => confirm(`刪除「${p.text}」和它的原音？`) && del.mutate()}><Trash2 className="size-3.5" /></Button>
          </>}
        </div>
      </div>
      <ErrorText error={save.error ?? unify.error} />

      <div className="mt-3 flex flex-wrap items-center gap-2">
        <span className="text-xs text-zinc-500">原音：</span>
        {p.clips.map((cl) => (
          <span key={cl.id} className="inline-flex items-center gap-1 rounded-full bg-zinc-100 py-0.5 pr-1 pl-0.5 dark:bg-zinc-800">
            <PlayButton small player={player} url={`/api/phrases/${p.id}/clips/${cl.id}/audio`} label={`${cl.duration.toFixed(1)}s`} />
            <select className="rounded-full border-0 bg-transparent py-0 text-[11px]" value={cl.emotion} onChange={(e) => clipEmotion.mutate({ cid: cl.id, emotion: e.target.value })}>
              <option value="">情緒…</option>
              {EMOTIONS.map(([k, l]) => <option key={k} value={k}>{l}</option>)}
            </select>
            <button className="text-zinc-400 hover:text-red-500" onClick={() => delClip.mutate(cl.id)} title="刪除這段原音"><Trash2 className="size-3" /></button>
          </span>
        ))}
        <Button size="sm" variant="secondary" onClick={() => setAdding(true)}><Plus className="size-3.5" />加入原音</Button>
        {!p.clips.length && <span className="text-xs text-zinc-500">還沒有原音：合成時由模型自己念。</span>}
      </div>

      {chk && (
        <div className="mt-3 flex flex-wrap items-center gap-2 rounded-lg bg-zinc-50 px-3 py-2 text-xs dark:bg-zinc-800/50">
          <span className="text-zinc-500">模型念法：</span>
          <PlayButton small player={player} url={`/api/outputs/${chk.output_id}/audio`} label="模型" />
          {p.clips[0] && <PlayButton small player={player} url={`/api/phrases/${p.id}/clips/${p.clips[0].id}/audio`} label="本人" />}
          <Badge tone={chk.match == null ? "zinc" : chk.match >= 0.9 ? "green" : chk.match >= 0.7 ? "amber" : "red"}>念對 {pct(chk.match)}</Badge>
          {chk.sim != null && <Badge tone="brand">聲紋 {chk.sim.toFixed(2)}</Badge>}
          {speed && <Badge tone={chk.dur_ratio != null && Math.abs(1 - chk.dur_ratio) <= 0.1 ? "green" : "amber"}>{speed}</Badge>}
        </div>
      )}
      {adding && <AddClipModal p={p} voice={voice} onClose={() => setAdding(false)} onDone={() => { setAdding(false); onChange(); }} />}
    </div>
  );
}

/** Add an original recording: upload a short file, or cut the phrase out of an imported segment. */
function AddClipModal({ p, voice, onClose, onDone }: { p: Phrase; voice: Voice; onClose: () => void; onDone: () => void }) {
  const [tab, setTab] = useState<"segment" | "file">("segment");
  const [emotion, setEmotion] = useState("");
  const [file, setFile] = useState<File | null>(null);
  const [q, setQ] = useState(p.text);
  const [seg, setSeg] = useState<Segment | null>(null);
  const [range, setRange] = useState({ start: 0, end: 0 });
  const player = usePlayer();
  const segs = useQuery({
    queryKey: ["phrase-segs", voice.id, q],
    queryFn: () => api.get<{ items: Segment[] }>(`/api/segments?voice_id=${voice.id}&q=${encodeURIComponent(q)}&limit=40&sort=score_desc`),
  });
  const choose = (s: Segment) => {
    setSeg(s);
    setEmotion(s.emotion ?? "");
    // first guess: where the phrase sits in the text, as a share of the clip's length
    const i = s.text.indexOf(p.text);
    const len = Math.max(1, s.text.length);
    if (i >= 0) {
      const a = Math.max(0, (s.duration * i) / len - 0.2), b = Math.min(s.duration, (s.duration * (i + p.text.length)) / len + 0.3);
      setRange({ start: +a.toFixed(2), end: +b.toFixed(2) });
    } else setRange({ start: 0, end: +Math.min(s.duration, 2).toFixed(2) });
  };
  const add = useMutation({
    mutationFn: () => {
      const fd = new FormData();
      fd.append("emotion", emotion);
      if (tab === "file" && file) fd.append("file", file);
      else if (seg) { fd.append("segment_id", seg.id); fd.append("start", String(range.start)); fd.append("end", String(range.end)); }
      return api.post(`/api/phrases/${p.id}/clips`, fd);
    },
    onSuccess: onDone,
  });
  return (
    <Modal open onClose={onClose} title={`加入「${p.text}」的原音`} wide>
      <div className="mb-4 flex rounded-lg border border-zinc-300 p-0.5 text-sm dark:border-zinc-700">
        {([["segment", "從匯入的片段剪"], ["file", "上傳檔案"]] as const).map(([k, l]) => (
          <button key={k} onClick={() => setTab(k)} className={clsx("flex-1 rounded-md px-3 py-1.5", tab === k ? "bg-brand-600 text-white" : "text-zinc-600 dark:text-zinc-300")}>{l}</button>
        ))}
      </div>
      {tab === "file" ? (
        <Field label="錄音檔（只有這個口頭禪，0.2–10 秒；前後的靜音會自動去掉）">
          <input type="file" accept="audio/*,video/*" className="input" onChange={(e) => setFile(e.target.files?.[0] ?? null)} />
        </Field>
      ) : (
        <div className="space-y-3">
          <input className="input" value={q} onChange={(e) => { setQ(e.target.value); setSeg(null); }} placeholder="搜尋片段文字" />
          {!seg ? (
            <div className="max-h-[40vh] space-y-1 overflow-y-auto">
              {segs.data?.items.map((s) => (
                <button key={s.id} onClick={() => choose(s)} className="flex w-full items-center gap-2 rounded-lg px-2 py-1.5 text-left text-sm hover:bg-zinc-50 dark:hover:bg-zinc-800/50">
                  <PlayButton small player={player} url={`/api/segments/${s.id}/audio`} />
                  <span className="min-w-0 flex-1 truncate">{s.text}</span>
                  <span className="shrink-0 text-xs text-zinc-500">{s.duration.toFixed(1)} 秒</span>
                </button>
              ))}
              {segs.data && !segs.data.items.length && <p className="text-sm text-zinc-500">找不到含有這段文字的片段。</p>}
            </div>
          ) : (
            <RangePicker seg={seg} range={range} setRange={setRange} onBack={() => setSeg(null)} />
          )}
        </div>
      )}
      <div className="mt-4">
        <Field label="這段原音的情緒" hint="合成時會挑和那一句情緒相同的原音。">
          <select className="input" value={emotion} onChange={(e) => setEmotion(e.target.value)}>
            <option value="">不標記</option>
            {EMOTIONS.map(([k, l]) => <option key={k} value={k}>{l}</option>)}
          </select>
        </Field>
      </div>
      <ErrorText error={add.error} />
      <div className="mt-4 flex justify-end gap-2">
        <Button variant="ghost" onClick={onClose}>取消</Button>
        <Button onClick={() => add.mutate()} loading={add.isPending} disabled={tab === "file" ? !file : !seg || range.end - range.start < 0.2}>
          {tab === "file" ? <Upload className="size-4" /> : <Scissors className="size-4" />}加入
        </Button>
      </div>
    </Modal>
  );
}

function RangePicker({ seg, range, setRange, onBack }: {
  seg: Segment; range: { start: number; end: number }; setRange: (r: { start: number; end: number }) => void; onBack: () => void;
}) {
  const audio = useRef<HTMLAudioElement | null>(null);
  const [playing, setPlaying] = useState(false);
  useEffect(() => () => audio.current?.pause(), []);
  const playRange = () => {
    if (playing) { audio.current?.pause(); setPlaying(false); return; }
    const a = audio.current ?? (audio.current = new Audio(`/api/segments/${seg.id}/audio`));
    const go = () => { a.currentTime = range.start; a.play().then(() => setPlaying(true)).catch(() => setPlaying(false)); };
    a.ontimeupdate = () => { if (a.currentTime >= range.end) { a.pause(); setPlaying(false); } };
    if (a.readyState >= 1) go(); else a.onloadedmetadata = go;
  };
  const clamp = (x: number) => Math.max(0, Math.min(seg.duration, x));
  return (
    <div className="rounded-xl border border-zinc-200 p-3 dark:border-zinc-800">
      <div className="mb-2 text-sm">{seg.text}</div>
      <div className="grid gap-3 sm:grid-cols-[1fr_1fr_auto]">
        <Field label={`開始（秒，共 ${seg.duration.toFixed(1)} 秒）`}>
          <input type="number" step={0.05} className="input" value={range.start} onChange={(e) => setRange({ ...range, start: clamp(+e.target.value) })} />
        </Field>
        <Field label="結束（秒）">
          <input type="number" step={0.05} className="input" value={range.end} onChange={(e) => setRange({ ...range, end: clamp(+e.target.value) })} />
        </Field>
        <Button variant="secondary" className="mt-6" onClick={playRange}>{playing ? <Pause className="size-4" /> : <Play className="size-4" />}聽選取範圍</Button>
      </div>
      <input type="range" min={0} max={seg.duration} step={0.05} value={range.start} onChange={(e) => setRange({ ...range, start: Math.min(+e.target.value, range.end - 0.2) })} className="w-full" aria-label="開始" />
      <input type="range" min={0} max={seg.duration} step={0.05} value={range.end} onChange={(e) => setRange({ ...range, end: Math.max(+e.target.value, range.start + 0.2) })} className="w-full" aria-label="結束" />
      <p className="mt-1 text-xs text-zinc-500">先用預估的範圍聽一次，再調整到剛好只有口頭禪（前後多一點點沒關係，靜音會自動去掉）。</p>
      <button className="mt-2 text-xs text-brand-600 underline" onClick={onBack}>換一段</button>
    </div>
  );
}

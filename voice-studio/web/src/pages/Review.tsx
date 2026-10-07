import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import { Link } from "react-router";
import { keepPreviousData, useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import clsx from "clsx";
import { Check, ChevronLeft, ChevronRight, Database, Pause, Play, Search, Sparkles, Trash2, Undo2, X } from "lucide-react";
import { api, fmtMin, fmtTime, LANGS, type AutoReview, type Dataset, type Segment, type Voice } from "../api";
import { Badge, Button, Card, Empty, ErrorText, Field, PageHeader, Progress } from "../ui";

const FLAGS: Record<string, string> = {
  asr_disagree: "兩個辨識結果不一致", noisy: "雜音多", clipping: "爆音", unknown_speaker: "不確定是誰",
  overlap: "可能多人同時說話", no_text: "沒有文字",
};
// flags written by automatic review (labels for the badges on each segment)
const AUTO: Record<string, [string, "green" | "red" | "blue" | "amber" | "brand"]> = {
  auto_approved: ["自動核可", "green"], auto_rejected: ["自動排除", "red"], auto_unsure: ["需要你聽", "blue"],
  spot_check: ["抽查", "brand"], spot_ok: ["抽查：沒問題", "green"], spot_fail: ["抽查：你排除了", "red"],
};
const REASON: Record<string, string> = {
  agree: "兩個辨識結果不一致", snr: "雜音偏多", clip: "爆音", speaker: "不像這個人", window: "中途可能換人或有別的聲音",
  logprob: "辨識信心低", no_speech: "可能不是說話（笑聲、音樂）", rate: "字數和長度對不上", text: "沒有文字", duration: "長度不適合",
};
const STATUS = [["pending", "待檢查"], ["approved", "已核可"], ["rejected", "已排除"], ["", "全部"]] as const;
const PAGE = 50;

type SegList = { total: number; minutes: number; items: Segment[] };

export default function Review() {
  const qc = useQueryClient();
  const voices = useQuery({ queryKey: ["voices"], queryFn: () => api.get<Voice[]>("/api/voices") });
  const [voiceId, setVoiceId] = useState<string>("");
  const [status, setStatus] = useState<string>("pending");
  const [flag, setFlag] = useState("");
  const [q, setQ] = useState("");
  const [sort, setSort] = useState("score_desc");
  const [page, setPage] = useState(0);
  const [cursor, setCursor] = useState(0);
  const vid = voiceId || voices.data?.[0]?.id || "";
  const voice = voices.data?.find((v) => v.id === vid);
  const filter = useMemo(() => ({ voice_id: vid, status, flag, q, sort }), [vid, status, flag, q, sort]);
  const params = new URLSearchParams({ ...filter, offset: String(page * PAGE), limit: String(PAGE) });
  const segs = useQuery({
    queryKey: ["segments", filter, page], enabled: !!vid, placeholderData: keepPreviousData,
    queryFn: () => api.get<SegList>(`/api/segments?${params}`),
  });
  useEffect(() => { setPage(0); setCursor(0); }, [filter]);
  const refresh = () => { qc.invalidateQueries({ queryKey: ["segments"] }); qc.invalidateQueries({ queryKey: ["voices"] }); };
  const patch = useMutation({
    mutationFn: ({ id, body }: { id: string; body: Partial<Segment> }) => api.patch<Segment>(`/api/segments/${id}`, body),
    onSuccess: (s) => {
      qc.setQueryData<SegList>(["segments", filter, page], (old) => old && { ...old, items: old.items.map((x) => (x.id === s.id ? s : x)) });
      qc.invalidateQueries({ queryKey: ["voices"] });
    },
  });
  const bulk = useMutation({ mutationFn: (body: unknown) => api.post<{ updated: number }>("/api/segments/bulk", body), onSuccess: refresh });

  // one shared player for the whole list
  const player = useRef<HTMLAudioElement | null>(null);
  const [playing, setPlaying] = useState<string | null>(null);
  const play = useCallback((id: string) => {
    if (!player.current) {
      player.current = new Audio();
      player.current.onended = () => setPlaying(null);
    }
    if (playing === id) { player.current.pause(); setPlaying(null); return; }
    player.current.src = `/api/segments/${id}/audio`;
    player.current.play().catch(() => undefined);
    setPlaying(id);
  }, [playing]);
  useEffect(() => () => player.current?.pause(), []);

  const items = segs.data?.items ?? [];
  const setStatusOf = (s: Segment, st: Segment["status"]) => {
    patch.mutate({ id: s.id, body: { status: st } });
    setCursor((c) => Math.min(c + 1, items.length - 1));
  };
  // keyboard: J/K move, Space play, A approve, R reject
  useEffect(() => {
    const k = (e: KeyboardEvent) => {
      const t = e.target as HTMLElement;
      if (t.tagName === "TEXTAREA" || t.tagName === "INPUT" || t.tagName === "SELECT") return;
      const cur = items[cursor];
      if (e.key === "j") setCursor((c) => Math.min(c + 1, items.length - 1));
      else if (e.key === "k") setCursor((c) => Math.max(c - 1, 0));
      else if (e.key === " " && cur) { e.preventDefault(); play(cur.id); }
      else if (e.key === "a" && cur) setStatusOf(cur, "approved");
      else if (e.key === "r" && cur) setStatusOf(cur, "rejected");
    };
    window.addEventListener("keydown", k);
    return () => window.removeEventListener("keydown", k);
  });
  useEffect(() => { document.getElementById(`seg-${cursor}`)?.scrollIntoView({ block: "nearest" }); }, [cursor]);

  if (voices.data && !voices.data.length)
    return (<div><PageHeader title="檢查資料" /><Empty title="還沒有聲音">先到 <Link className="underline" to="/voices">聲音與同意</Link> 建立聲音，再匯入錄音。</Empty></div>);

  const pages = Math.ceil((segs.data?.total ?? 0) / PAGE);
  return (
    <div>
      <PageHeader title="檢查資料"
        subtitle="訓練品質取決於這一步。聽一聽、修正文字、核可或排除。文字必須和說的話一字不差（包括「えっと」「um」這類口頭禪），模型才學得到說話習慣。" />
      <div className="grid gap-6 xl:grid-cols-[1fr_300px]">
        <div className="min-w-0">
          <div className="card mb-4 space-y-3 p-4">
            <div className="flex flex-wrap items-center gap-2">
              <select className="input w-44" value={vid} onChange={(e) => setVoiceId(e.target.value)}>
                {voices.data?.map((v) => <option key={v.id} value={v.id}>{v.name}</option>)}
              </select>
              <div className="flex rounded-lg border border-zinc-300 p-0.5 dark:border-zinc-700">
                {STATUS.map(([k, l]) => (
                  <button key={k} onClick={() => setStatus(k)}
                    className={clsx("rounded-md px-3 py-1 text-sm", status === k ? "bg-brand-600 text-white" : "text-zinc-600 hover:bg-zinc-100 dark:text-zinc-300 dark:hover:bg-zinc-800")}>{l}</button>
                ))}
              </div>
              <select className="input w-40" value={sort} onChange={(e) => setSort(e.target.value)}>
                <option value="score_desc">分數高→低</option>
                <option value="score_asc">分數低→高（先看問題）</option>
                <option value="time">錄音時間順序</option>
                <option value="duration">長度</option>
              </select>
              <div className="relative min-w-40 flex-1">
                <Search className="absolute top-2.5 left-2.5 size-4 text-zinc-400" />
                <input className="input pl-8" placeholder="搜尋文字" value={q} onChange={(e) => setQ(e.target.value)} />
              </div>
            </div>
            <div className="flex flex-wrap gap-1.5">
              <button onClick={() => setFlag("")} className={clsx("rounded-full px-2.5 py-0.5 text-xs", !flag ? "bg-zinc-800 text-white dark:bg-zinc-200 dark:text-zinc-900" : "bg-zinc-100 dark:bg-zinc-800")}>不限警告</button>
              {([["auto_unsure", "需要你聽", "pending"], ["spot_check", "抽查", ""]] as const).map(([k, l, st]) => (
                <button key={k} onClick={() => { if (flag === k) setFlag(""); else { setFlag(k); setStatus(st); } }}
                  className={clsx("rounded-full px-2.5 py-0.5 text-xs", flag === k ? "bg-sky-600 text-white" : "bg-sky-50 text-sky-800 dark:bg-sky-950/50 dark:text-sky-200")}>{l}</button>
              ))}
              {Object.entries(FLAGS).map(([k, l]) => (
                <button key={k} onClick={() => setFlag(flag === k ? "" : k)}
                  className={clsx("rounded-full px-2.5 py-0.5 text-xs", flag === k ? "bg-amber-500 text-white" : "bg-zinc-100 dark:bg-zinc-800")}>{l}</button>
              ))}
            </div>
            <div className="flex flex-wrap items-center justify-between gap-2 text-sm">
              <span className="text-zinc-500">符合 {segs.data?.total ?? 0} 段 · {fmtMin(segs.data?.minutes ?? 0)}</span>
              <div className="flex flex-wrap gap-2">
                <Button size="sm" variant="secondary" onClick={() => bulk.mutate({ ids: items.map((s) => s.id), status: "approved" })} disabled={!items.length}>核可這一頁</Button>
                <Button size="sm" variant="secondary" disabled={!segs.data?.total}
                  onClick={() => confirm(`把符合目前篩選的 ${segs.data?.total} 段全部核可？`) && bulk.mutate({ filter, status: "approved" })}>核可全部符合的</Button>
                <Button size="sm" variant="ghost" disabled={!segs.data?.total}
                  onClick={() => confirm(`把符合目前篩選的 ${segs.data?.total} 段全部排除？`) && bulk.mutate({ filter, status: "rejected" })}>排除全部符合的</Button>
              </div>
            </div>
          </div>

          {!items.length ? (
            <Empty title={segs.isFetching ? "載入中…" : "這裡沒有片段"}>
              {status === "pending" ? "全部檢查完了！可以在右邊建立訓練資料集。" : "換個篩選條件看看。"}
            </Empty>
          ) : (
            <div className="space-y-2">
              {items.map((s, i) => (
                <SegmentRow key={s.id} s={s} index={i} active={i === cursor} playing={playing === s.id}
                  onFocus={() => setCursor(i)} onPlay={() => play(s.id)}
                  onStatus={(st) => setStatusOf(s, st)} onText={(text) => patch.mutate({ id: s.id, body: { text } })} />
              ))}
            </div>
          )}
          {pages > 1 && (
            <div className="mt-4 flex items-center justify-center gap-3 text-sm">
              <Button size="sm" variant="secondary" disabled={page === 0} onClick={() => setPage(page - 1)}><ChevronLeft className="size-4" /></Button>
              <span>{page + 1} / {pages}</span>
              <Button size="sm" variant="secondary" disabled={page + 1 >= pages} onClick={() => setPage(page + 1)}><ChevronRight className="size-4" /></Button>
            </div>
          )}
          <p className="mt-4 text-center text-xs text-zinc-500">
            鍵盤：<span className="kbd">J</span>/<span className="kbd">K</span> 上下 · <span className="kbd">空白</span> 播放 · <span className="kbd">A</span> 核可 · <span className="kbd">R</span> 排除
          </p>
        </div>
        <div className="space-y-4">
          {voice && <AutoReviewCard voice={voice} onShow={(f, st) => { setFlag(f); setStatus(st); }} />}
          {voice && <DatasetPanel voice={voice} />}
          <Card title="怎樣算好片段？">
            <ul className="list-disc space-y-1.5 pl-4 text-sm text-zinc-600 dark:text-zinc-400">
              <li>只有這個人在說話，沒有別人插話或笑聲疊在一起。</li>
              <li>文字和說的話完全一致，口頭禪、重複、說錯再改口都照實寫。</li>
              <li>沒有背景音樂、爆音或明顯回音。</li>
              <li>各種情緒都保留一些（平靜、興奮、小聲），模型才學得到抑揚頓挫。</li>
              <li>不確定就排除。少一點乾淨的資料，比多一點髒資料好。</li>
            </ul>
          </Card>
        </div>
      </div>
    </div>
  );
}

function SegmentRow({ s, index, active, playing, onFocus, onPlay, onStatus, onText }: {
  s: Segment; index: number; active: boolean; playing: boolean; onFocus: () => void; onPlay: () => void;
  onStatus: (st: Segment["status"]) => void; onText: (t: string) => void;
}) {
  const [text, setText] = useState(s.text);
  useEffect(() => setText(s.text), [s.text]);
  const tone = s.score == null ? "zinc" : s.score >= 0.8 ? "green" : s.score >= 0.5 ? "amber" : "red";
  const alt = s.text_alt && s.text_alt !== s.text ? s.text_alt : "";
  return (
    <div id={`seg-${index}`} onClick={onFocus}
      className={clsx("card flex gap-3 p-3 transition", active && "ring-2 ring-brand-500/40",
        s.status === "approved" && "border-emerald-300 dark:border-emerald-900", s.status === "rejected" && "opacity-60")}>
      <button onClick={(e) => { e.stopPropagation(); onPlay(); }}
        className="flex size-9 shrink-0 items-center justify-center rounded-full bg-brand-600 text-white hover:bg-brand-700">
        {playing ? <Pause className="size-4" /> : <Play className="ml-0.5 size-4" />}
      </button>
      <div className="min-w-0 flex-1">
        <textarea className="input min-h-[2.4rem] resize-y py-1.5 leading-6" rows={1} value={text}
          onChange={(e) => setText(e.target.value)} onBlur={() => text !== s.text && onText(text)} />
        {alt && (
          <div className="mt-1 flex items-start gap-2 text-xs text-zinc-500">
            <span className="shrink-0">另一個辨識：</span><span className="flex-1">{alt}</span>
            <button className="shrink-0 text-brand-600 underline" onClick={() => { setText(alt); onText(alt); }}>用這個</button>
          </div>
        )}
        <div className="mt-1.5 flex flex-wrap items-center gap-1.5 text-[11px] text-zinc-500">
          <Badge tone={tone}>分數 {s.score?.toFixed(2) ?? "—"}</Badge>
          <span>{s.duration.toFixed(1)} 秒</span>
          {s.lang && <span>· {LANGS[s.lang] ?? s.lang}</span>}
          {s.spk_sim != null && <span>· 像本人 {(s.spk_sim * 100).toFixed(0)}%</span>}
          {s.edited ? <Badge tone="blue">已修改</Badge> : null}
          {s.flags.map((f) => f.startsWith("auto:") ? <span key={f} className="text-sky-700 dark:text-sky-300">· {REASON[f.slice(5)] ?? f.slice(5)}</span>
            : AUTO[f] ? <Badge key={f} tone={AUTO[f][1]}>{AUTO[f][0]}</Badge> : <Badge key={f} tone="amber">{FLAGS[f] ?? f}</Badge>)}
        </div>
      </div>
      <div className="flex shrink-0 flex-col gap-1.5">
        <button title="核可 (A)" onClick={(e) => { e.stopPropagation(); onStatus(s.status === "approved" ? "pending" : "approved"); }}
          className={clsx("rounded-lg p-2", s.status === "approved" ? "bg-emerald-500 text-white" : "bg-zinc-100 text-zinc-500 hover:bg-emerald-100 dark:bg-zinc-800")}><Check className="size-4" /></button>
        <button title="排除 (R)" onClick={(e) => { e.stopPropagation(); onStatus(s.status === "rejected" ? "pending" : "rejected"); }}
          className={clsx("rounded-lg p-2", s.status === "rejected" ? "bg-red-500 text-white" : "bg-zinc-100 text-zinc-500 hover:bg-red-100 dark:bg-zinc-800")}><X className="size-4" /></button>
      </div>
    </div>
  );
}

function AutoReviewCard({ voice, onShow }: { voice: Voice; onShow: (flag: string, status: string) => void }) {
  const qc = useQueryClient();
  const [profile, setProfile] = useState("balanced");
  const info = useQuery({
    queryKey: ["auto-review", voice.id], queryFn: () => api.get<AutoReview>(`/api/auto-review/${voice.id}`),
    refetchInterval: (q) => (q.state.data?.job && ["queued", "running"].includes(q.state.data.job.status) ? 2000 : false),
  });
  const job = info.data?.job;
  const running = !!job && ["queued", "running"].includes(job.status);
  const wasRunning = useRef(false);
  useEffect(() => {  // refresh the list once the job finishes
    if (wasRunning.current && !running) { qc.invalidateQueries({ queryKey: ["segments"] }); qc.invalidateQueries({ queryKey: ["voices"] }); }
    wasRunning.current = running;
  }, [running, qc]);
  const start = useMutation({
    mutationFn: () => api.post(`/api/auto-review/${voice.id}`, { profile }),
    onSuccess: () => qc.invalidateQueries({ queryKey: ["auto-review", voice.id] }),
  });
  const undo = useMutation({
    mutationFn: () => api.post<{ reset: number }>(`/api/auto-review/${voice.id}/undo`),
    onSuccess: () => { qc.invalidateQueries({ queryKey: ["auto-review", voice.id] }); qc.invalidateQueries({ queryKey: ["segments"] }); qc.invalidateQueries({ queryKey: ["voices"] }); },
  });
  const d = info.data;
  const pending = voice.stats.pending?.count ?? 0;
  const touched = !!d && d.auto_approved + d.auto_rejected + d.unsure + d.spot_ok + d.spot_fail > 0;
  return (
    <Card title={<span className="flex items-center gap-2"><Sparkles className="size-4" />自動審核</span>}>
      <p className="text-xs text-zinc-500">
        幾十小時的錄音不用一段一段聽：平台用兩個辨識模型、聲紋、雜音和語速自動判斷，清楚的直接核可、明顯不行的排除，
        只把拿不準的留給你，另外抽一小部分核可的讓你確認。你自己改過或決定過的片段不會被動到，也可以整批復原。
      </p>
      {running ? (
        <div className="mt-3 space-y-1.5 text-sm">
          <Progress value={job!.progress} />
          <div className="text-xs text-zinc-500">{job!.message || "排隊中…"}</div>
        </div>
      ) : (
        <div className="mt-3 space-y-2">
          <div className="flex rounded-lg border border-zinc-300 p-0.5 text-sm dark:border-zinc-700">
            {([["balanced", "平衡"], ["strict", "嚴格"]] as const).map(([k, l]) => (
              <button key={k} onClick={() => setProfile(k)}
                className={clsx("flex-1 rounded-md px-3 py-1", profile === k ? "bg-brand-600 text-white" : "text-zinc-600 hover:bg-zinc-100 dark:text-zinc-300 dark:hover:bg-zinc-800")}>{l}</button>
            ))}
          </div>
          <p className="text-[11px] text-zinc-500">{profile === "strict" ? "嚴格：只核可非常乾淨的片段，需要你聽的會變多。資料很多（10 小時以上）時建議用這個。" : "平衡：大部分情況用這個。"}</p>
          <Button className="w-full" onClick={() => start.mutate()} loading={start.isPending} disabled={!pending}>
            自動審核 {pending} 段待檢查的片段
          </Button>
          <ErrorText error={start.error} />
        </div>
      )}
      {job?.status === "done" && job.result?.message && <p className="mt-3 rounded-lg bg-emerald-50 px-3 py-2 text-xs text-emerald-800 dark:bg-emerald-950/40 dark:text-emerald-200">上次結果：{job.result.message}</p>}
      {job?.status === "failed" && <p className="mt-3 rounded-lg bg-red-50 px-3 py-2 text-xs text-red-800 dark:bg-red-950/40 dark:text-red-200">上次自動審核失敗：{job.message}（詳情在「工作佇列」）</p>}
      {d && touched && (
        <div className="mt-3 space-y-2 text-sm">
          <button onClick={() => onShow("auto_unsure", "pending")} className="flex w-full items-center justify-between rounded-lg bg-sky-50 px-3 py-2 text-left hover:bg-sky-100 dark:bg-sky-950/40 dark:hover:bg-sky-950/70">
            <span>① 需要你聽</span><span className="font-semibold tabular-nums">{d.unsure} 段</span>
          </button>
          <button onClick={() => onShow("spot_check", "")} className="flex w-full items-center justify-between rounded-lg bg-brand-50 px-3 py-2 text-left hover:bg-brand-100 dark:bg-brand-900/30 dark:hover:bg-brand-900/50">
            <span>② 抽查自動核可的</span><span className="font-semibold tabular-nums">剩 {d.spot_left} 段</span>
          </button>
          {d.spot_ok + d.spot_fail > 0 && <p className="text-xs text-zinc-500">抽查結果：{d.spot_ok} 段沒問題、{d.spot_fail} 段被你排除。</p>}
          {d.advice && <p className="rounded-lg bg-amber-50 px-3 py-2 text-xs text-amber-800 dark:bg-amber-950/40 dark:text-amber-200">{d.advice}</p>}
          <p className="text-xs text-zinc-500">抽查時用 <span className="kbd">A</span> 表示沒問題、<span className="kbd">R</span> 排除。看自動排除的原因：狀態切到「已排除」。</p>
          <Button size="sm" variant="ghost" disabled={running} loading={undo.isPending}
            onClick={() => confirm("把自動核可和自動排除的片段都改回「待檢查」？（你自己決定過的不會變）") && undo.mutate()}>
            <Undo2 className="size-4" />復原自動審核
          </Button>
          <ErrorText error={undo.error} />
        </div>
      )}
    </Card>
  );
}

function DatasetPanel({ voice }: { voice: Voice }) {
  const qc = useQueryClient();
  const sets = useQuery({ queryKey: ["datasets", voice.id], queryFn: () => api.get<Dataset[]>(`/api/datasets?voice_id=${voice.id}`) });
  const [minScore, setMinScore] = useState(0.5);
  const build = useMutation({
    mutationFn: () => api.post<Dataset>("/api/datasets", { voice_id: voice.id, min_score: minScore }),
    onSuccess: () => qc.invalidateQueries({ queryKey: ["datasets", voice.id] }),
  });
  const del = useMutation({ mutationFn: (id: string) => api.del(`/api/datasets/${id}`), onSuccess: () => qc.invalidateQueries({ queryKey: ["datasets", voice.id] }) });
  const approved = voice.stats.approved?.minutes ?? 0;
  return (
    <Card title={<span className="flex items-center gap-2"><Database className="size-4" />訓練資料集</span>}>
      <div className="text-sm">
        <div className="text-2xl font-semibold tabular-nums">{fmtMin(approved)}</div>
        <div className="text-xs text-zinc-500">{voice.name} 已核可的語音</div>
        <div className="mt-2 text-xs text-zinc-500">
          {approved < 30 ? "少於 30 分鐘：先試「免訓練」，微調的效果有限。"
            : approved < 300 ? "30 分鐘到 5 小時：可以先跑一次 LoRA 確認流程；建議目標是 5–10 小時。"
            : approved <= 600 ? "5–10 小時：建議目標。可以比較 VoxCPM2 LoRA、完整微調和 Qwen3-TTS。"
            : "超過 10 小時：多出來的部分要帶來新的語氣、場合或語言才有幫助；可以先用 5、10 小時各跑一次比較。"}
        </div>
      </div>
      {!voice.consent_ok ? (
        <p className="mt-3 rounded-lg bg-amber-50 px-3 py-2 text-xs text-amber-800 dark:bg-amber-950/40 dark:text-amber-200">需要先完成 <Link to={`/voices/${voice.id}`} className="underline">同意紀錄</Link>。</p>
      ) : (
        <div className="mt-4 space-y-3">
          <Field label={`最低分數 ${minScore.toFixed(2)}`} hint="低於這個分數的已核可片段不會放進資料集。">
            <input type="range" min={0} max={0.9} step={0.05} value={minScore} onChange={(e) => setMinScore(+e.target.value)} className="w-full" />
          </Field>
          <Button className="w-full" onClick={() => build.mutate()} loading={build.isPending} disabled={approved === 0}>建立新的資料集</Button>
          <ErrorText error={build.error} />
          <p className="text-xs text-zinc-500">資料集是當下的「快照」：之後再修改片段不會影響已建立的資料集。</p>
        </div>
      )}
      <ul className="mt-4 space-y-2">
        {sets.data?.map((d) => (
          <li key={d.id} className="flex items-center gap-2 rounded-lg bg-zinc-50 px-3 py-2 text-sm dark:bg-zinc-800/50">
            <div className="min-w-0 flex-1">
              <div className="truncate font-medium">{d.name}</div>
              <div className="text-xs text-zinc-500">{d.n_items} 段 · {fmtMin(d.hours * 60)} · {fmtTime(d.created_at)}</div>
            </div>
            <Link to={`/train?dataset=${d.id}`}><Button size="sm">訓練</Button></Link>
            <button className="text-zinc-400 hover:text-red-500" onClick={() => confirm("刪除這個資料集？（不影響片段）") && del.mutate(d.id)}><Trash2 className="size-4" /></button>
          </li>
        ))}
      </ul>
    </Card>
  );
}

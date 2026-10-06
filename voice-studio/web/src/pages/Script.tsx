import { useEffect, useState } from "react";
import { Link } from "react-router";
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { Download, FileText, Play } from "lucide-react";
import { api, fmtTime, LANGS, MODES, type CharacterPreset, type Job, type Model, type Output } from "../api";
import { Badge, Button, Card, Empty, ErrorText, Field, PageHeader, PlayButton, Progress, usePlayer, Wave } from "../ui";

type Cast = { model_id: string; language: string; style: string; mode: string; ref_id: string };
type Parsed = { events: { kind: string; speaker?: string; text?: string; line: number; romaji?: string }[];
  speakers: { name: string; preset: CharacterPreset | null }[] };
type SheetLine = { line: number; speaker: string; text: string; romaji?: string; output: string; match: number | null };

const EXAMPLE = `@@scene 屋上の練習
@@date 2026-10-06
STAGE :: 夕方、屋上。風が少し強い。
我 :: [calm] ねえ、もう一回だけ合わせてみない？
ROMAJI :: Nē, mō ikkai dake awasete minai?
PAUSE :: 0.6
友達 :: [bright, laughing] いいよ。でも今度は笑わないでね。
我 :: [deadpan] それは約束できない。
`;

export default function Script() {
  const qc = useQueryClient();
  const models = useQuery({ queryKey: ["models"], queryFn: () => api.get<Model[]>("/api/models") });
  const [script, setScript] = useState(() => localStorage.getItem("vs-script") ?? "");
  const [cast, setCast] = useState<Record<string, Cast>>(() => JSON.parse(localStorage.getItem("vs-cast") ?? "{}"));
  const [takes, setTakes] = useState(2);
  const [gap, setGap] = useState(0.35);
  const [jobId, setJobId] = useState<string | null>(null);
  useEffect(() => { localStorage.setItem("vs-script", script); }, [script]);
  useEffect(() => { localStorage.setItem("vs-cast", JSON.stringify(cast)); }, [cast]);
  const parsed = useQuery({
    queryKey: ["parse", script], enabled: !!script.trim(),
    queryFn: () => api.post<Parsed>("/api/script/parse", { script }),
  });
  // fill unassigned speakers from character presets (model + language + defaults)
  useEffect(() => {
    const sp = parsed.data?.speakers ?? [];
    setCast((c) => {
      const next = { ...c };
      for (const s of sp) {
        if (next[s.name]) continue;
        const p = s.preset;
        next[s.name] = { model_id: p?.model_id ?? "", language: p?.data.language ?? "auto", style: "",
          mode: p?.data.cast_mode ?? "", ref_id: p?.data.cast_ref_id ?? "" };
      }
      return next;
    });
  }, [parsed.data]);
  const render = useMutation({
    mutationFn: () => api.post<Job>("/api/script/render", {
      script, takes, gap,
      cast: Object.fromEntries((parsed.data?.speakers ?? []).map((s) => {
        const c = cast[s.name];
        return [s.name, { model_id: c.model_id, language: c.language === "auto" ? null : c.language, style: c.style,
          mode: c.mode || null, ref_id: c.ref_id || null }];
      })),
    }),
    onSuccess: (j) => setJobId(j.id),
  });
  const job = useQuery({ queryKey: ["job", jobId], enabled: !!jobId, queryFn: () => api.get<Job>(`/api/jobs/${jobId}`),
    refetchInterval: (q) => (q.state.data && ["done", "failed", "canceled"].includes(q.state.data.status) ? false : 1500) });
  useEffect(() => { if (job.data?.status === "done") qc.invalidateQueries({ queryKey: ["scenes"] }); }, [job.data?.status, qc]);
  const speakers = parsed.data?.speakers ?? [];
  const turns = parsed.data?.events.filter((e) => e.kind === "turn").length ?? 0;
  const missing = speakers.filter((s) => !cast[s.name]?.model_id);
  return (
    <div>
      <PageHeader title="劇本配音"
        subtitle="貼上 novel-lab 格式的場景（角色 :: 台詞），幫每個角色指定一個聲音模型，一次合成整場對話。每句會產生幾個版本自動挑最好的，最後接成一個檔案並附上逐句清單。" />
      <div className="grid gap-6 lg:grid-cols-2">
        <Card title="1. 劇本" actions={<Button size="sm" variant="ghost" onClick={() => setScript(EXAMPLE)}>載入範例</Button>}>
          <textarea className="input min-h-[26rem] font-mono text-[13px] leading-6" value={script} onChange={(e) => setScript(e.target.value)}
            placeholder={"角色名稱 :: [語氣] 台詞\nROMAJI :: 羅馬拼音（選填）\nPAUSE :: 0.8\nSTAGE :: 舞台說明（不會念出來）"} />
          <p className="mt-2 text-xs text-zinc-500">
            {turns ? `${turns} 句台詞、${speakers.length} 個角色。` : ""}
            STAGE、SFX、NOTE、ROMAJI、GLOSS 這些行不會念出來；PAUSE 會插入停頓（秒）。Narrator 的台詞會略過。
          </p>
        </Card>
        <div className="space-y-6">
          <Card title="2. 指定聲音">
            {!speakers.length ? <p className="text-sm text-zinc-500">貼上劇本後，角色會列在這裡。</p> : (
              <div className="space-y-3">
                {speakers.map((s) => {
                  const c = cast[s.name] ?? { model_id: "", language: "auto", style: "", mode: "", ref_id: "" };
                  const m = models.data?.find((x) => x.id === c.model_id);
                  const set = (patch: Partial<Cast>) => setCast({ ...cast, [s.name]: { ...c, ...patch } });
                  return (
                    <div key={s.name} className="rounded-xl border border-zinc-200 p-3 dark:border-zinc-800">
                      <div className="mb-2 flex items-center gap-2 font-medium">{s.name}{s.preset && <Badge tone="blue">有角色預設</Badge>}</div>
                      <div className="grid gap-2 sm:grid-cols-2">
                        <select className="input" value={c.model_id} onChange={(e) => set({ model_id: e.target.value, mode: "", ref_id: "" })}>
                          <option value="">選模型…</option>
                          {models.data?.map((x) => <option key={x.id} value={x.id}>{x.name}</option>)}
                        </select>
                        <select className="input" value={c.language} onChange={(e) => set({ language: e.target.value })}>
                          <option value="auto">語言：自動</option><option value="ja">日文</option><option value="en">英文</option>
                        </select>
                        {m && <select className="input" value={c.mode || m.modes[0]} onChange={(e) => set({ mode: e.target.value })}>
                          {m.modes.map((k) => <option key={k} value={k}>{MODES[k]?.label ?? k}</option>)}</select>}
                        {m && (c.mode || m.modes[0]) !== "plain" && <select className="input" value={c.ref_id} onChange={(e) => set({ ref_id: e.target.value })}>
                          <option value="">參考：預設第一段</option>
                          {m.meta.references?.map((r) => <option key={r.id} value={r.id}>{r.text.slice(0, 20) || r.label}</option>)}</select>}
                        <input className="input sm:col-span-2" placeholder="這個角色整體的風格提示（選填），會加在每句的 [語氣] 後面" value={c.style} onChange={(e) => set({ style: e.target.value })} />
                      </div>
                      {s.preset && <p className="mt-2 text-[11px] text-zinc-500">預設語言 {LANGS[s.preset.data.language]}；常用提示：{s.preset.data.default_tags.join(", ")}</p>}
                    </div>
                  );
                })}
                {!models.data?.length && <p className="text-sm text-amber-700">還沒有模型。<Link to="/models" className="underline">建立一個</Link></p>}
              </div>
            )}
          </Card>
          <Card title="3. 合成">
            <div className="grid grid-cols-2 gap-3">
              <Field label="每句產生幾個版本"><select className="input" value={takes} onChange={(e) => setTakes(+e.target.value)}>{[1, 2, 3, 4].map((n) => <option key={n}>{n}</option>)}</select></Field>
              <Field label={`句子之間的間隔 ${gap.toFixed(2)} 秒`}><input type="range" min={0} max={1.5} step={0.05} value={gap} onChange={(e) => setGap(+e.target.value)} className="mt-3 w-full" /></Field>
            </div>
            <Button className="mt-4 w-full" disabled={!turns || missing.length > 0 || render.isPending || job.data?.status === "running"}
              loading={render.isPending} onClick={() => render.mutate()}><Play className="size-4" />合成整場</Button>
            {missing.length > 0 && turns > 0 && <p className="mt-2 text-xs text-amber-700">還沒指定聲音：{missing.map((s) => s.name).join("、")}</p>}
            <ErrorText error={render.error} />
            {job.data && job.data.status !== "done" && (
              <div className="mt-4"><div className="mb-1 flex justify-between text-xs text-zinc-500"><span>{job.data.message}</span><span>{Math.round(job.data.progress * 100)}%</span></div>
                <Progress value={job.data.progress} />{job.data.status === "failed" && <ErrorText error={job.data.message} />}</div>
            )}
          </Card>
        </div>
      </div>
      <Scenes />
    </div>
  );
}

function Scenes() {
  const scenes = useQuery({ queryKey: ["scenes"], queryFn: () => api.get<Output[]>("/api/outputs?scenes=true&limit=20") });
  const [open, setOpen] = useState<string | null>(null);
  const first = open ?? scenes.data?.[0]?.id ?? null;
  if (!scenes.data?.length) return <Card title="合成好的場景" className="mt-6"><Empty icon={<FileText className="size-8" />} title="還沒有場景" /></Card>;
  return (
    <Card title="合成好的場景" className="mt-6">
      <div className="grid gap-6 lg:grid-cols-[260px_1fr]">
        <ul className="space-y-1.5">{scenes.data.map((o) => (
          <li key={o.id}><button onClick={() => setOpen(o.id)} className={`w-full rounded-lg px-3 py-2 text-left text-sm ${first === o.id ? "bg-brand-50 dark:bg-brand-900/20" : "hover:bg-zinc-50 dark:hover:bg-zinc-800/50"}`}>
            <div className="truncate">{o.text.split("\n").find((l) => l.startsWith("@@scene"))?.slice(8) || "場景"}</div>
            <div className="text-xs text-zinc-500">{o.score.lines} 句 · {o.duration.toFixed(0)} 秒 · {fmtTime(o.created_at)}</div></button></li>))}
        </ul>
        {first && <SceneDetail id={first} />}
      </div>
    </Card>
  );
}

function SceneDetail({ id }: { id: string }) {
  const sheet = useQuery({ queryKey: ["sheet", id], queryFn: () => api.get<SheetLine[]>(`/api/outputs/${id}/sheet`) });
  const player = usePlayer();
  return (
    <div className="min-w-0">
      <Wave src={`/api/outputs/${id}/audio`} />
      <div className="mt-2 flex gap-2">
        <a href={`/api/outputs/${id}/audio`} download><Button size="sm" variant="secondary"><Download className="size-3.5" />WAV</Button></a>
        <a href={`/api/outputs/${id}/audio?format=mp3`} download><Button size="sm" variant="secondary"><Download className="size-3.5" />MP3</Button></a>
      </div>
      <ol className="mt-4 space-y-1.5 text-sm">
        {sheet.data?.map((l) => (
          <li key={l.line} className="flex items-start gap-2">
            <PlayButton small player={player} url={`/api/outputs/${l.output}/audio`} />
            <div className="min-w-0 flex-1"><span className="font-medium">{l.speaker}</span>：{l.text}
              {l.romaji && <div className="text-xs text-zinc-500">{l.romaji}</div>}</div>
            {l.match != null && <Badge tone={l.match >= 0.9 ? "green" : l.match >= 0.75 ? "amber" : "red"}>{(l.match * 100).toFixed(0)}%</Badge>}
          </li>
        ))}
      </ol>
    </div>
  );
}

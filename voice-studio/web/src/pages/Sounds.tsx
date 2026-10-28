import { useState } from "react";
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import clsx from "clsx";
import { Check, Plus, Search, Trash2, Undo2, Wind, X } from "lucide-react";
import { api, EMOTIONS, isSound, type Job, type Phrase, type SoundFind, type Voice } from "../api";
import { Badge, Button, Card, ErrorText, Field, Modal, PlayButton, Progress, usePlayer } from "../ui";
import { AddClipModal, RangePicker } from "./Phrases";

const PRESETS = ["[吸氣]", "[大口吸氣]", "[嘆氣]", "[喘氣]", "[嬌喘]", "[笑聲]", "[輕笑]", "[抽泣]", "[咳嗽]", "[清喉嚨]", "[打哈欠]", "[嘖]"];
const WHERE: Record<string, string> = { before: "在句子前（多半是吸氣）", after: "在句子後（多半是吐氣、嘆氣）", alone: "單獨" };
type Finds = { counts: Record<string, number>; items: SoundFind[]; job: Job | null; kinds: Record<string, string> };

/** Sound tags of one voice ([喘氣], [嘆氣] …): the person's own recordings, played where the tag is written. */
export function SoundsCard({ voice }: { voice: Voice }) {
  const qc = useQueryClient();
  const key = ["phrases", voice.id];
  const list = useQuery({ queryKey: key, queryFn: () => api.get<Phrase[]>(`/api/voices/${voice.id}/phrases`) });
  const inv = () => { qc.invalidateQueries({ queryKey: key }); qc.invalidateQueries({ queryKey: ["phrases", voice.id, "light"] }); };
  const sounds = (list.data ?? []).filter(isSound);
  const [name, setName] = useState("");
  const add = useMutation({
    mutationFn: (tag: string) => api.post(`/api/voices/${voice.id}/phrases`, { text: tag.startsWith("[") ? tag : `[${tag}]`, variants: [] }),
    onSuccess: () => { setName(""); inv(); },
  });
  const have = new Set(sounds.map((s) => s.text));
  return (
    <Card title={<span className="flex items-center gap-2"><Wind className="size-4" />聲音標籤：吸氣、嘆氣、喘氣…（{sounds.length}）</span>}>
      <p className="mb-3 text-sm text-zinc-500">
        模型只學會「說話」，很難自己發出喘氣、嘆氣這種沒有字的聲音。在這裡登記標籤並放進<b>你自己錄到的聲音</b>，在要念的文字裡寫 <code className="kbd">[喘氣]</code>，合成時就會在那個位置播你的原音（音量照原本和說話聲的比例）。還沒放原音的標籤只當語氣提示。
      </p>
      <div className="flex flex-wrap items-center gap-2 rounded-xl bg-zinc-50 p-3 dark:bg-zinc-800/50">
        {PRESETS.filter((t) => !have.has(t)).map((t) => (
          <Button key={t} size="sm" variant="secondary" onClick={() => add.mutate(t)} loading={add.isPending && add.variables === t}><Plus className="size-3.5" />{t}</Button>
        ))}
        <div className="flex items-center gap-1">
          <input className="input w-36" placeholder="其他，例如 呻吟" value={name} onChange={(e) => setName(e.target.value.replace(/[[\]［］【】]/g, ""))}
            onKeyDown={(e) => { if (e.key === "Enter" && name.trim()) add.mutate(name.trim()); }} />
          <Button size="sm" onClick={() => add.mutate(name.trim())} disabled={!name.trim()}>登記</Button>
        </div>
      </div>
      <ErrorText error={add.error} />
      <div className="mt-4 space-y-3">{sounds.map((p) => <SoundRow key={p.id} p={p} voice={voice} onChange={inv} />)}</div>
      <FindPanel voice={voice} sounds={sounds} onKept={inv} />
    </Card>
  );
}

function SoundRow({ p, voice, onChange }: { p: Phrase; voice: Voice; onChange: () => void }) {
  const player = usePlayer();
  const [adding, setAdding] = useState(false);
  const del = useMutation({ mutationFn: () => api.del(`/api/phrases/${p.id}`), onSuccess: onChange });
  const delClip = useMutation({ mutationFn: (cid: string) => api.del(`/api/phrases/${p.id}/clips/${cid}`), onSuccess: onChange });
  const clipEmotion = useMutation({ mutationFn: ({ cid, emotion }: { cid: string; emotion: string }) => api.patch(`/api/phrases/${p.id}/clips/${cid}`, { emotion }), onSuccess: onChange });
  return (
    <div className="flex flex-wrap items-center gap-2 rounded-xl border border-zinc-200 p-3 dark:border-zinc-800">
      <span className="min-w-24 font-semibold">{p.text}</span>
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
      {!p.clips.length && <span className="text-xs text-amber-700 dark:text-amber-300">還沒有原音：現在只當語氣提示</span>}
      <span className="ml-auto flex gap-1">
        <Button size="sm" variant="secondary" onClick={() => setAdding(true)}><Plus className="size-3.5" />加入原音</Button>
        <Button size="sm" variant="ghost" onClick={() => confirm(`刪除 ${p.text} 和它的原音？`) && del.mutate()}><Trash2 className="size-3.5" /></Button>
      </span>
      {adding && <AddClipModal p={p} voice={voice} onClose={() => setAdding(false)} onDone={() => { setAdding(false); onChange(); }} />}
    </div>
  );
}

/** Scan the voice's recordings for breaths, panting, sighs and wordless sounds; listen; keep or dismiss. */
function FindPanel({ voice, sounds, onKept }: { voice: Voice; sounds: Phrase[]; onKept: () => void }) {
  const qc = useQueryClient();
  const player = usePlayer();
  const [kind, setKind] = useState("");
  const [status, setStatus] = useState("new");
  const [keeping, setKeeping] = useState<SoundFind | null>(null);
  const key = ["sound-finds", voice.id, kind, status];
  const finds = useQuery({
    queryKey: key,
    queryFn: () => api.get<Finds>(`/api/voices/${voice.id}/sounds?kind=${kind}&status=${status}&limit=60`),
    refetchInterval: (q) => (q.state.data?.job && ["queued", "running"].includes(q.state.data.job.status) ? 1500 : false),
  });
  const inv = () => qc.invalidateQueries({ queryKey: ["sound-finds", voice.id] });
  const scan = useMutation({ mutationFn: () => api.post<Job>(`/api/voices/${voice.id}/sounds/scan`), onSuccess: inv });
  const mark = useMutation({ mutationFn: ({ id, to }: { id: string; to: "dismiss" | "restore" }) => api.post(`/api/sounds/${id}/${to}`), onSuccess: inv });
  const job = finds.data?.job;
  const running = !!job && ["queued", "running"].includes(job.status);
  const counts = finds.data?.counts ?? {};
  const total = Object.values(counts).reduce((a, b) => a + b, 0);
  return (
    <div className="mt-5 border-t border-zinc-100 pt-4 dark:border-zinc-800">
      <div className="mb-1 flex flex-wrap items-center gap-2">
        <span className="text-sm font-medium">我的錄音裡有沒有這些聲音？</span>
        <Button size="sm" variant="secondary" className="ml-auto" onClick={() => scan.mutate()} loading={scan.isPending} disabled={running}>
          <Search className="size-3.5" />{job ? "重新掃描" : "掃描我的錄音"}
        </Button>
      </div>
      <p className="mb-3 text-xs text-zinc-500">
        掃描這個聲音匯入過的所有錄音（包括被排除的片段和片段之間的空檔），找出像吸氣、喘氣、嘆氣、沒有字的聲音（嗯、啊、呻吟）的地方，還有逐字稿裡有笑聲、哭聲、咳嗽、打噴嚏、嘖…的片段（日文「はぁ・あはは・ゴホッ」、英文「(laughs)・*sighs*・ugh・achoo」、中文「唉・哈哈・咳咳」都會找）。這些是<b>候選</b>：按播放聽，確定是就「收下」放進標籤，不是就按「不是」。背景有音樂或雜音的地方只看逐字稿。
      </p>
      {running && <div className="mb-3"><div className="text-xs text-zinc-500">{job!.message}</div><Progress value={job!.progress} /></div>}
      {job?.status === "failed" && <ErrorText error={job.message} />}
      {job?.status === "done" && <p className="mb-2 text-xs text-zinc-500">{job.message}</p>}
      <ErrorText error={scan.error} />
      {(job || total > 0) && (
        <>
          <div className="mb-2 flex flex-wrap items-center gap-1">
            {[["", `全部 ${total}`], ...Object.entries(finds.data?.kinds ?? {}).map(([k, l]) => [k, `${l} ${counts[k] ?? 0}`])].map(([k, l]) => (
              <button key={k} onClick={() => setKind(k)} className={clsx("rounded-full px-2.5 py-1 text-xs", kind === k ? "bg-brand-600 text-white" : "bg-zinc-100 dark:bg-zinc-800")}>{l}</button>
            ))}
            <select className="input ml-auto w-28 py-1 text-xs" value={status} onChange={(e) => setStatus(e.target.value)}>
              <option value="new">待確認</option><option value="kept">已收下</option><option value="dismissed">不是</option>
            </select>
          </div>
          <div className="max-h-[50vh] space-y-1 overflow-y-auto">
            {finds.data?.items.map((f) => (
              <div key={f.id} className="flex flex-wrap items-center gap-2 rounded-lg px-2 py-1.5 text-sm hover:bg-zinc-50 dark:hover:bg-zinc-800/50">
                <PlayButton small player={player} url={`/api/sounds/${f.id}/audio`} label={`${(f.end - f.start).toFixed(1)}s`} />
                <Badge tone={f.how === "text" ? "blue" : "brand"}>{f.label}</Badge>
                <span className="min-w-0 flex-1 truncate text-xs text-zinc-500">
                  {f.how === "text" ? <>逐字稿：{f.text}</> : f.kind === "voice" ? <>逐字稿：{f.text || "（沒有字）"}</>
                    : f.meta.where ? WHERE[f.meta.where] : f.meta.bursts ? `${f.meta.bursts} 口氣` : ""}
                </span>
                {status === "new" && <>
                  <Button size="sm" onClick={() => setKeeping(f)}><Check className="size-3.5" />收下…</Button>
                  <Button size="sm" variant="ghost" onClick={() => mark.mutate({ id: f.id, to: "dismiss" })}><X className="size-3.5" />不是</Button>
                </>}
                {status === "dismissed" && <Button size="sm" variant="ghost" onClick={() => mark.mutate({ id: f.id, to: "restore" })}><Undo2 className="size-3.5" />復原</Button>}
                {status === "kept" && f.meta.phrase && <span className="text-xs text-zinc-500">→ {sounds.find((s) => s.id === f.meta.phrase)?.text ?? "已刪除的標籤"}</span>}
              </div>
            ))}
            {finds.data && !finds.data.items.length && <p className="text-sm text-zinc-500">{job ? "這裡沒有候選。" : "還沒掃描。"}</p>}
          </div>
        </>
      )}
      {keeping && <KeepModal f={keeping} sounds={sounds} onClose={() => setKeeping(null)} onDone={() => { setKeeping(null); inv(); onKept(); }} />}
    </div>
  );
}

function KeepModal({ f, sounds, onClose, onDone }: { f: SoundFind; sounds: Phrase[]; onClose: () => void; onDone: () => void }) {
  const suggested = f.kind === "breath" && f.meta.where === "after" ? "[嘆氣]" : f.suggest;
  const first = sounds.find((s) => s.text === suggested)?.id ?? (suggested ? "" : sounds[0]?.id ?? "");
  const [pick, setPick] = useState(first);
  const [tag, setTag] = useState(first ? "" : (suggested ?? "").replace(/[[\]]/g, ""));
  const [range, setRange] = useState({ start: +(f.start - f.clip_start).toFixed(2), end: +(f.end - f.clip_start).toFixed(2) });
  const [emotion, setEmotion] = useState("");
  const keep = useMutation({
    mutationFn: () => api.post(`/api/sounds/${f.id}/keep`, { ...(pick ? { phrase_id: pick } : { tag: `[${tag.trim()}]` }), ...range, emotion: emotion || null }),
    onSuccess: onDone,
  });
  return (
    <Modal open onClose={onClose} title={`收下這段${f.label}`} wide>
      <div className="grid gap-3 sm:grid-cols-2">
        <Field label="放進哪個聲音標籤">
          <select className="input" value={pick} onChange={(e) => setPick(e.target.value)}>
            {sounds.map((s) => <option key={s.id} value={s.id}>{s.text}（{s.clips.length} 段原音）</option>)}
            <option value="">新的標籤…</option>
          </select>
        </Field>
        {!pick && <Field label="新標籤的名字"><input className="input" value={tag} placeholder="例如 喘氣" onChange={(e) => setTag(e.target.value.replace(/[[\]［］【】]/g, ""))} /></Field>}
      </div>
      <div className="mt-3">
        <RangePicker url={`/api/sounds/${f.id}/audio`} duration={f.clip_end - f.clip_start} text={f.how === "text" || f.kind === "voice" ? f.text : ""}
          range={range} setRange={setRange} hint="播放的是候選和前後各 0.4 秒。調整到只剩那個聲音（不要包含說話的字）；前後的靜音會自動去掉。" />
      </div>
      <div className="mt-3">
        <Field label="這段聲音的情緒（選填）" hint="一個標籤可以收好幾段：合成時會挑和那一句情緒相同的那段。">
          <select className="input" value={emotion} onChange={(e) => setEmotion(e.target.value)}>
            <option value="">不標記</option>
            {EMOTIONS.map(([k, l]) => <option key={k} value={k}>{l}</option>)}
          </select>
        </Field>
      </div>
      <ErrorText error={keep.error} />
      <div className="mt-4 flex justify-end gap-2">
        <Button variant="ghost" onClick={onClose}>取消</Button>
        <Button onClick={() => keep.mutate()} loading={keep.isPending} disabled={(!pick && !tag.trim()) || range.end - range.start < 0.2}><Check className="size-4" />收下</Button>
      </div>
    </Modal>
  );
}

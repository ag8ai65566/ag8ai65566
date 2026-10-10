import { useEffect, useState } from "react";
import { Link, useSearchParams } from "react-router";
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import clsx from "clsx";
import { Download, Mic2, Power, Star, Trash2 } from "lucide-react";
import { api, EMOTION_LABEL, EMOTIONS, fmtTime, LANGS, MODES, type CharacterPreset, type Model, type Output, type Phrase } from "../api";
import { Badge, Button, Card, Empty, ErrorText, Field, PageHeader, PlayButton, usePlayer, Wave } from "../ui";

const STYLE_CHIPS: [string, string][] = [
  ["開心", "cheerful, bright"], ["興奮", "excited, energetic"], ["平靜", "calm, steady"], ["溫柔", "gentle, warm"],
  ["小聲", "soft, quiet"], ["悄悄話", "whispering"], ["慢慢說", "slow, unhurried"], ["快一點", "slightly faster"],
  ["生氣", "annoyed, sharp"], ["難過", "sad, subdued"], ["無奈", "deadpan, dry"], ["撒嬌", "playful, teasing"],
];

export default function Speak() {
  const [sp, setSp] = useSearchParams();
  const qc = useQueryClient();
  const models = useQuery({ queryKey: ["models"], queryFn: () => api.get<Model[]>("/api/models") });
  const presets = useQuery({ queryKey: ["presets"], queryFn: () => api.get<CharacterPreset[]>("/api/presets") });
  const modelId = sp.get("model") ?? models.data?.[0]?.id ?? "";
  const model = models.data?.find((m) => m.id === modelId);
  const [text, setText] = useState("");
  const [language, setLanguage] = useState("auto");
  const [mode, setMode] = useState("plain");
  const [refId, setRefId] = useState("");
  const [style, setStyle] = useState("");
  const [takes, setTakes] = useState(2);
  const [seed, setSeed] = useState("");
  const [screen, setScreen] = useState(true);
  const [presetId, setPresetId] = useState("");
  const [emotion, setEmotion] = useState("");
  const [usePhrases, setUsePhrases] = useState(true);
  const [result, setResult] = useState<Output[]>([]);
  const player = usePlayer();
  useEffect(() => {
    if (!model) return;
    setMode(model.modes.includes(mode) ? mode : model.modes[0]);
    setRefId(model.meta.references?.[0]?.id ?? "");
    setResult([]);
  }, [model?.id]); // eslint-disable-line react-hooks/exhaustive-deps
  const phrases = useQuery({
    queryKey: ["phrases", model?.voice_id, "light"], enabled: !!model,
    queryFn: () => api.get<Phrase[]>(`/api/voices/${model!.voice_id}/phrases?counts=false`),
  });
  const withClips = (phrases.data ?? []).filter((p) => p.clips.length);
  const pickEmotion = (e: string) => {  // a reference of that mood is the strongest way to get it
    setEmotion(e);
    const r = model?.meta.references?.find((x) => x.emotion === e);
    if (r) setRefId(r.id);
  };
  const preset = presets.data?.find((p) => p.id === presetId);
  useEffect(() => {
    if (!preset) return;
    setLanguage(preset.data.language);
    setStyle(preset.data.default_tags.join(", "));
  }, [presetId]); // eslint-disable-line react-hooks/exhaustive-deps

  const gen = useMutation({
    mutationFn: () => api.post<{ outputs: Output[] }>("/api/tts", {
      model_id: modelId, text, language, style: mode === "hifi" ? "" : style, takes, screen, mode,
      ref_id: refId || null, seed: seed ? Number(seed) : null, emotion: emotion || null, phrases: usePhrases,
    }),
    onSuccess: (r) => { setResult(r.outputs); qc.invalidateQueries({ queryKey: ["outputs", modelId] }); },
  });
  const unload = useMutation({ mutationFn: () => api.post("/api/tts/unload") });
  const refs = model?.meta.references ?? [];
  const needsRef = mode === "ref" || mode === "hifi";

  if (models.data && !models.data.length)
    return (<div><PageHeader title="文字轉語音" /><Empty icon={<Mic2 className="size-8" />} title="還沒有模型">
      先 <Link to="/train" className="underline">訓練一個</Link>，或到 <Link to="/models" className="underline">模型</Link> 建立免訓練模型。
      只想看看介面的話，可以到 <Link to="/settings" className="underline">設定</Link> 建立測試模型。</Empty></div>);

  return (
    <div>
      <PageHeader title="文字轉語音" subtitle="輸入文字，用你訓練好的聲音念出來。一次產生幾個版本，平台會用語音辨識檢查有沒有漏字，標出最好的一個。"
        actions={<Button variant="ghost" size="sm" onClick={() => unload.mutate()} title="把模型從顯示卡移出，讓出記憶體"><Power className="size-4" />釋放顯示卡</Button>} />
      <div className="grid gap-6 lg:grid-cols-[1fr_320px]">
        <Card>
          <div className="space-y-4">
            <div className="grid gap-3 sm:grid-cols-2">
              <Field label="模型">
                <select className="input" value={modelId} onChange={(e) => setSp({ model: e.target.value })}>
                  {models.data?.map((m) => <option key={m.id} value={m.id}>{m.name}</option>)}
                </select>
              </Field>
              <Field label="角色預設（選填）" hint="套用角色的語言與表演提示。">
                <select className="input" value={presetId} onChange={(e) => setPresetId(e.target.value)}>
                  <option value="">不使用</option>
                  {presets.data?.map((p) => <option key={p.id} value={p.id}>{p.name}（{LANGS[p.data.language]}）</option>)}
                </select>
              </Field>
            </div>
            {model && !model.available[0] && <p className="rounded-lg bg-amber-50 px-3 py-2 text-sm text-amber-800 dark:bg-amber-950/40 dark:text-amber-200">本機還不能用 {model.engine_name}：{model.available[1]}。<Link to="/settings#engines" className="underline">安裝引擎</Link></p>}
            <Field label={`文字（${text.length}/2000）`} hint={<>可以用 <code className="kbd">[excited]</code> 這種方括號提示語氣，會轉成引擎看得懂的風格說明。<span className="kbd">Ctrl</span>+<span className="kbd">Enter</span> 產生。</>}>
              <textarea className="input min-h-36 text-base leading-7" value={text} maxLength={2000} onChange={(e) => setText(e.target.value)}
                placeholder="今日はちょっとだけ、ゆっくり話してみようかな。" onKeyDown={(e) => { if (e.key === "Enter" && (e.ctrlKey || e.metaKey) && text.trim()) gen.mutate(); }} />
            </Field>
            {preset && (
              <div className="rounded-lg bg-zinc-50 p-3 text-xs leading-5 text-zinc-600 dark:bg-zinc-800/50 dark:text-zinc-300">
                <div className="font-medium">{preset.name} 的情境提示</div>
                <div className="mt-1 flex flex-wrap gap-1">{preset.data.situations.slice(0, 8).map((s) => (
                  <button key={s.situation} className="rounded-full bg-white px-2 py-0.5 hover:bg-brand-50 dark:bg-zinc-900" title={s.example}
                    onClick={() => setStyle(s.tags.join(", "))}>{s.situation}</button>))}</div>
              </div>
            )}
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
              <Field label="情緒（選填）" hint="會挑這個情緒的參考片段和口頭禪原音。不選時，從風格提示或 [angry] 這類標籤判斷。">
                <select className="input" value={emotion} onChange={(e) => pickEmotion(e.target.value)}>
                  <option value="">自動</option>
                  {EMOTIONS.map(([k, l]) => <option key={k} value={k}>{l}</option>)}
                </select>
              </Field>
              {withClips.length > 0 && (
                <label className="mt-6 flex items-start gap-2 text-sm">
                  <input type="checkbox" className="mt-1" checked={usePhrases} onChange={(e) => setUsePhrases(e.target.checked)} />
                  <span>口頭禪用原音<span className="block text-xs text-zinc-500">{withClips.map((p) => `「${p.text}」`).join("")} 會換成本人的錄音</span></span>
                </label>
              )}
            </div>
            {needsRef && (
              <Field label="參考片段" hint={refs.length ? "挑語氣最接近你想要的那段。" : undefined}>
                {refs.length ? (
                  <div className="space-y-1.5">{refs.map((r) => (
                    <label key={r.id} className={clsx("flex cursor-pointer items-center gap-2 rounded-lg px-2 py-1.5 text-sm", refId === r.id ? "bg-brand-50 dark:bg-brand-900/20" : "hover:bg-zinc-50 dark:hover:bg-zinc-800/50")}>
                      <input type="radio" checked={refId === r.id} onChange={() => setRefId(r.id)} />
                      <PlayButton small player={player} url={`/api/models/${modelId}/references/${r.id}/audio`} />
                      <span className="truncate">{r.text || r.label}</span>
                      {r.emotion && <Badge tone="brand">{EMOTION_LABEL[r.emotion] ?? r.emotion}</Badge>}
                    </label>))}</div>
                ) : <p className="text-sm text-amber-700">這個模型還沒有參考片段，到 <Link to={`/models?id=${modelId}`} className="underline">模型頁</Link> 加入。</p>}
              </Field>
            )}
            {mode !== "hifi" && (
              <Field label="風格提示（選填）" hint="用英文描述通常最穩定。">
                <input className="input" value={style} onChange={(e) => setStyle(e.target.value)} placeholder="calm, slightly slower" />
                <div className="mt-2 flex flex-wrap gap-1">{STYLE_CHIPS.map(([zh, en]) => (
                  <button key={zh} onClick={() => setStyle(style ? `${style}, ${en}` : en)} className="rounded-full bg-zinc-100 px-2 py-0.5 text-xs hover:bg-brand-100 dark:bg-zinc-800">{zh}</button>))}</div>
              </Field>
            )}
            <div className="grid grid-cols-2 gap-3 sm:grid-cols-4">
              <Field label="語言"><select className="input" value={language} onChange={(e) => setLanguage(e.target.value)}>
                <option value="auto">自動</option><option value="ja">日文</option><option value="en">英文</option><option value="zh">中文</option></select></Field>
              <Field label="產生幾個版本"><select className="input" value={takes} onChange={(e) => setTakes(+e.target.value)}>{[1, 2, 3, 4].map((n) => <option key={n}>{n}</option>)}</select></Field>
              <Field label="種子（選填）"><input className="input" value={seed} onChange={(e) => setSeed(e.target.value.replace(/\D/g, ""))} placeholder="隨機" /></Field>
              <label className="mt-6 flex items-center gap-2 text-sm"><input type="checkbox" checked={screen} onChange={(e) => setScreen(e.target.checked)} />檢查漏字</label>
            </div>
            <Button className="w-full" onClick={() => gen.mutate()} loading={gen.isPending} disabled={!text.trim() || !model || (needsRef && !refs.length)}>
              <Mic2 className="size-4" />{gen.isPending ? "合成中…（第一次要載入模型，約 30 秒）" : "產生語音"}
            </Button>
            <ErrorText error={gen.error} />
            {result.length > 0 && (
              <div className="space-y-3 border-t border-zinc-100 pt-4 dark:border-zinc-800">
                {result.map((o, i) => <Take key={o.id} o={o} index={i} />)}
              </div>
            )}
          </div>
        </Card>
        {modelId && <History modelId={modelId} />}
      </div>
    </div>
  );
}

function Take({ o, index }: { o: Output; index: number }) {
  return (
    <div className={clsx("rounded-xl border p-3", o.score.best ? "border-emerald-400 bg-emerald-50/50 dark:border-emerald-800 dark:bg-emerald-950/20" : "border-zinc-200 dark:border-zinc-800")}>
      <div className="mb-2 flex flex-wrap items-center gap-2 text-xs">
        <span className="font-medium">版本 {index + 1}</span>
        {o.score.best && <Badge tone="green">最好</Badge>}
        {o.score.match != null && <Badge tone={o.score.match >= 0.9 ? "green" : o.score.match >= 0.75 ? "amber" : "red"}>念對 {(o.score.match * 100).toFixed(0)}%</Badge>}
        <span className="text-zinc-500">{o.duration.toFixed(1)} 秒 · 種子 {o.params.seed}</span>
        {o.params.phrases?.length ? <Badge tone="blue">含原音：{o.params.phrases.map((p) => p.phrase).join("、")}</Badge> : null}
        {o.params.emotion && <Badge tone="brand">{EMOTION_LABEL[o.params.emotion] ?? o.params.emotion}</Badge>}
        <span className="ml-auto flex gap-1">
          <a href={`/api/outputs/${o.id}/audio`} download><Button size="sm" variant="ghost"><Download className="size-3.5" />WAV</Button></a>
          <a href={`/api/outputs/${o.id}/audio?format=mp3`} download><Button size="sm" variant="ghost">MP3</Button></a>
        </span>
      </div>
      <Wave src={`/api/outputs/${o.id}/audio`} />
      {o.score.heard && o.score.match != null && o.score.match < 0.95 && <p className="mt-2 text-xs text-zinc-500">辨識聽到：{o.score.heard}</p>}
    </div>
  );
}

function History({ modelId }: { modelId: string }) {
  const qc = useQueryClient();
  const [fav, setFav] = useState(false);
  const outs = useQuery({ queryKey: ["outputs", modelId, fav], queryFn: () => api.get<Output[]>(`/api/outputs?model_id=${modelId}&limit=60${fav ? "&favorite=true" : ""}`) });
  const player = usePlayer();
  const star = useMutation({ mutationFn: (o: Output) => api.patch(`/api/outputs/${o.id}`, { favorite: !o.favorite }), onSuccess: () => qc.invalidateQueries({ queryKey: ["outputs", modelId] }) });
  const del = useMutation({ mutationFn: (o: Output) => api.del(`/api/outputs/${o.id}`), onSuccess: () => qc.invalidateQueries({ queryKey: ["outputs", modelId] }) });
  return (
    <Card title="紀錄" actions={<button onClick={() => setFav(!fav)} className={clsx("text-xs", fav ? "text-amber-600" : "text-zinc-500")}><Star className="inline size-3.5" /> 只看收藏</button>}>
      {!outs.data?.length ? <p className="text-sm text-zinc-500">產生的語音會留在這裡。</p> : (
        <ul className="max-h-[70vh] space-y-2 overflow-y-auto">
          {outs.data.map((o) => (
            <li key={o.id} className="rounded-lg bg-zinc-50 p-2 text-sm dark:bg-zinc-800/50">
              <div className="flex items-start gap-2">
                <PlayButton small player={player} url={`/api/outputs/${o.id}/audio`} />
                <div className="min-w-0 flex-1">
                  <div className="line-clamp-2">{o.text}</div>
                  <div className="mt-0.5 text-[11px] text-zinc-500">{MODES[o.params.mode ?? ""]?.label ?? ""} · {fmtTime(o.created_at)}{o.score.best ? " · 最好" : ""}</div>
                </div>
                <button onClick={() => star.mutate(o)} className={o.favorite ? "text-amber-500" : "text-zinc-300 hover:text-amber-500"}><Star className="size-4" fill={o.favorite ? "currentColor" : "none"} /></button>
                <a href={`/api/outputs/${o.id}/audio`} download className="text-zinc-400 hover:text-zinc-600"><Download className="size-4" /></a>
                <button onClick={() => del.mutate(o)} className="text-zinc-300 hover:text-red-500"><Trash2 className="size-4" /></button>
              </div>
            </li>
          ))}
        </ul>
      )}
    </Card>
  );
}

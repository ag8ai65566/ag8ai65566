import { useEffect, useState } from "react";
import { Link, useLocation, useNavigate } from "react-router";
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { BookA, CheckCircle2, Cloud, Download, FlaskConical, KeyRound, Lock, Plus, Server, Shield, SlidersHorizontal, Trash2 } from "lucide-react";
import { api, type EngineInfo, type Job } from "../api";
import { Badge, Button, Card, ErrorText, Field, PageHeader, Progress } from "../ui";

type SettingsResp = { settings: Record<string, any>; secrets: Record<string, boolean> };
type CloudCheck = { ok: boolean; error?: string; volumes?: { id: string; name: string; dataCenterId: string; size: number }[];
  volume?: { id: string } | null };

export default function Settings() {
  const loc = useLocation();
  useEffect(() => { if (loc.hash) document.getElementById(loc.hash.slice(1))?.scrollIntoView(); }, [loc.hash]);
  return (
    <div className="space-y-6">
      <PageHeader title="設定" subtitle="金鑰只存在這台電腦的 Windows 認證管理員裡，不會寫進檔案、紀錄或傳給任何人（只用來呼叫 RunPod）。" />
      <CloudSettings />
      <Engines />
      <Lexicon />
      <DataSettings />
      <Extras />
    </div>
  );
}

function SecretField({ name, label, hint, set }: { name: string; label: string; hint?: React.ReactNode; set: boolean }) {
  const qc = useQueryClient();
  const [v, setV] = useState("");
  const save = useMutation({
    mutationFn: (value: string | null) => api.put("/api/secrets", { name, value }),
    onSuccess: () => { setV(""); qc.invalidateQueries({ queryKey: ["settings"] }); },
  });
  return (
    <Field label={label} hint={hint}>
      <div className="flex gap-2">
        <div className="relative flex-1">
          <Lock className="absolute top-2.5 left-2.5 size-4 text-zinc-400" />
          <input className="input pl-8" type="password" autoComplete="off" value={v} onChange={(e) => setV(e.target.value)}
            placeholder={set ? "已設定（輸入新的值可以取代）" : "貼上金鑰"} />
        </div>
        <Button variant="secondary" disabled={!v.trim()} loading={save.isPending} onClick={() => save.mutate(v.trim())}>儲存</Button>
        {set && <Button variant="ghost" onClick={() => confirm("清除這個金鑰？") && save.mutate(null)}>清除</Button>}
      </div>
      {set && <span className="mt-1 flex items-center gap-1 text-xs text-emerald-600"><CheckCircle2 className="size-3.5" />已安全儲存</span>}
      <ErrorText error={save.error} />
    </Field>
  );
}

function useSettings() {
  return useQuery({ queryKey: ["settings"], queryFn: () => api.get<SettingsResp>("/api/settings") });
}

function CloudSettings() {
  const qc = useQueryClient();
  const st = useSettings();
  const dcs = useQuery({ queryKey: ["dcs"], queryFn: () => api.get<string[]>("/api/cloud/datacenters") });
  const [form, setForm] = useState<Record<string, any>>({});
  useEffect(() => { if (st.data) setForm(st.data.settings); }, [st.data]);
  const save = useMutation({ mutationFn: (b: Record<string, unknown>) => api.put("/api/settings", b), onSuccess: () => qc.invalidateQueries({ queryKey: ["settings"] }) });
  const check = useMutation({ mutationFn: () => api.get<CloudCheck>("/api/cloud/check") });
  const sec = st.data?.secrets ?? {};
  return (
    <Card title={<span className="flex items-center gap-2"><Cloud className="size-4" />雲端 GPU（RunPod）</span>}>
      <ol className="mb-5 list-decimal space-y-1 pl-5 text-sm text-zinc-600 dark:text-zinc-400">
        <li>到 runpod.io 註冊並儲值（建議先 $10–25）。</li>
        <li>Storage → <b>New Network Volume</b>：選一個有 S3 API 的資料中心（下面清單裡的），大小 150 GB 起（完整微調建議 300 GB）。</li>
        <li>Settings → <b>API Keys</b> → Create：權限選 All（或至少 Pods 與 Network Volumes 讀寫），貼到下面第一格。</li>
        <li>Settings → <b>S3 API Keys</b> → Create：把 Access key 和 Secret 分別貼到下面。</li>
        <li>按「測試連線」，在清單裡點你的網路磁碟，會自動填好 ID 和資料中心。</li>
      </ol>
      <p className="mb-5 text-sm"><Link to="/guide/04-cloud" className="text-brand-600 underline">圖文教學（含常見錯誤）</Link></p>
      <div className="grid gap-4 md:grid-cols-2">
        <SecretField name="runpod_api_key" label="RunPod API 金鑰" set={!!sec.runpod_api_key} />
        <div />
        <SecretField name="runpod_s3_access_key" label="S3 Access Key（user_ 開頭）" set={!!sec.runpod_s3_access_key} />
        <SecretField name="runpod_s3_secret_key" label="S3 Secret（rps_ 開頭）" set={!!sec.runpod_s3_secret_key} />
        <Field label="網路磁碟 ID（Network Volume ID）">
          <input className="input font-mono" value={form.runpod_volume_id ?? ""} onChange={(e) => setForm({ ...form, runpod_volume_id: e.target.value.trim() })} />
        </Field>
        <Field label="資料中心">
          <select className="input" value={form.runpod_datacenter ?? ""} onChange={(e) => setForm({ ...form, runpod_datacenter: e.target.value })}>
            <option value="">請選擇</option>{dcs.data?.map((d) => <option key={d}>{d}</option>)}
          </select>
        </Field>
        <Field label={`單次訓練最長時數：${form.runpod_max_hours ?? 12} 小時`} hint="超過就強制關機（防止意外一直計費）。資料很多時再調高。">
          <input type="range" min={1} max={48} step={1} value={form.runpod_max_hours ?? 12} onChange={(e) => setForm({ ...form, runpod_max_hours: +e.target.value })} className="w-full" />
        </Field>
      </div>
      <div className="mt-5 flex flex-wrap gap-2">
        <Button onClick={() => save.mutate({ runpod_volume_id: form.runpod_volume_id, runpod_datacenter: form.runpod_datacenter, runpod_max_hours: form.runpod_max_hours })} loading={save.isPending}>儲存</Button>
        <Button variant="secondary" onClick={() => check.mutate()} loading={check.isPending} disabled={!sec.runpod_api_key}>測試連線</Button>
        {save.isSuccess && <span className="self-center text-sm text-emerald-600">已儲存</span>}
      </div>
      {check.data && (check.data.ok ? (
        <div className="mt-4 rounded-xl bg-zinc-50 p-3 text-sm dark:bg-zinc-800/50">
          <div className="mb-2 font-medium text-emerald-600">API 金鑰有效。你的網路磁碟：</div>
          {!check.data.volumes?.length ? <p className="text-zinc-500">還沒有網路磁碟，請先到 RunPod 建立。</p> : (
            <ul className="space-y-1">{check.data.volumes.map((v) => (
              <li key={v.id}><button className="w-full rounded-lg px-2 py-1 text-left hover:bg-white dark:hover:bg-zinc-900"
                onClick={() => { const f = { ...form, runpod_volume_id: v.id, runpod_datacenter: v.dataCenterId }; setForm(f); save.mutate({ runpod_volume_id: v.id, runpod_datacenter: v.dataCenterId }); }}>
                <span className="font-mono">{v.id}</span> · {v.name} · {v.dataCenterId} · {v.size} GB
                {!dcs.data?.includes(v.dataCenterId) && <Badge tone="red">這個資料中心沒有 S3 API</Badge>}
                {form.runpod_volume_id === v.id && <Badge tone="green">使用中</Badge>}
              </button></li>))}</ul>
          )}
        </div>
      ) : <ErrorText error={check.data.error} />)}
      <ErrorText error={check.error} />
    </Card>
  );
}

function Engines() {
  const qc = useQueryClient();
  const engines = useQuery({ queryKey: ["engines"], queryFn: () => api.get<EngineInfo[]>("/api/engines") });
  const jobs = useQuery({ queryKey: ["jobs", "active"], queryFn: () => api.get<Job[]>("/api/jobs?active=true"), refetchInterval: 2000 });
  const installing = jobs.data?.find((j) => j.kind === "install_engine");
  const install = useMutation({ mutationFn: (id: string) => api.post<Job>(`/api/engines/${id}/install`), onSuccess: () => qc.invalidateQueries({ queryKey: ["jobs"] }) });
  useEffect(() => { if (!installing) qc.invalidateQueries({ queryKey: ["engines"] }); }, [installing, qc]);
  return (
    <Card title={<span id="engines" className="flex items-center gap-2"><Server className="size-4" />引擎（本機合成用）</span>}>
      <p className="mb-4 text-sm text-zinc-500">訓練在雲端進行，不需要安裝。要在這台電腦上用訓練好的模型說話，才需要安裝對應的引擎（每個約 5–8 GB，含模型權重）。</p>
      <div className="space-y-3">
        {engines.data?.filter((e) => e.install).map((e) => (
          <div key={e.id} className="rounded-xl border border-zinc-200 p-4 dark:border-zinc-800">
            <div className="flex flex-wrap items-center gap-2">
              <span className="font-medium">{e.name}</span>
              {e.available ? <Badge tone="green">{e.available_note}</Badge> : <Badge tone="amber">{e.available_note}</Badge>}
              <span className="text-xs text-zinc-500">授權 {e.license} · 合成約需 {e.infer_vram_gb} GB 顯示記憶體</span>
              <div className="ml-auto">
                <Button size="sm" variant={e.available ? "ghost" : "primary"} disabled={!!installing} loading={install.isPending && install.variables === e.id}
                  onClick={() => install.mutate(e.id)}><Download className="size-3.5" />{e.available ? "重新安裝" : "安裝"}</Button>
              </div>
            </div>
            <p className="mt-1 text-xs leading-5 text-zinc-500">{e.license_note}</p>
            {installing?.params?.engine === e.id && (
              <div className="mt-3"><div className="mb-1 truncate text-xs text-zinc-500">{installing.message}</div><Progress value={installing.progress} /></div>
            )}
          </div>
        ))}
      </div>
      <ErrorText error={install.error} />
    </Card>
  );
}

function DataSettings() {
  const qc = useQueryClient();
  const st = useSettings();
  const [f, setF] = useState<Record<string, any>>({});
  useEffect(() => { if (st.data) setF(st.data.settings); }, [st.data]);
  const save = useMutation({ mutationFn: () => api.put("/api/settings", {
    asr_primary: f.asr_primary, asr_secondary: f.asr_secondary, asr_device: f.asr_device, segment_min_s: +f.segment_min_s,
    segment_max_s: +f.segment_max_s, segment_target_s: +f.segment_target_s, speaker_match_threshold: +f.speaker_match_threshold,
  }), onSuccess: () => qc.invalidateQueries({ queryKey: ["settings"] }) });
  return (
    <Card title={<span className="flex items-center gap-2"><SlidersHorizontal className="size-4" />資料處理</span>}>
      <div className="grid gap-4 md:grid-cols-3">
        <Field label="主要語音辨識模型" hint="large-v3 最準。"><select className="input" value={f.asr_primary ?? ""} onChange={(e) => setF({ ...f, asr_primary: e.target.value })}>
          {["large-v3", "large-v3-turbo", "medium"].map((m) => <option key={m}>{m}</option>)}</select></Field>
        <Field label="對照用辨識模型" hint="兩個模型結果不一致的片段會被標出來。"><select className="input" value={f.asr_secondary ?? ""} onChange={(e) => setF({ ...f, asr_secondary: e.target.value })}>
          {["large-v3-turbo", "large-v3", "medium"].map((m) => <option key={m}>{m}</option>)}</select></Field>
        <Field label="辨識用裝置"><select className="input" value={f.asr_device ?? "auto"} onChange={(e) => setF({ ...f, asr_device: e.target.value })}>
          <option value="auto">自動</option><option value="cuda">GPU</option><option value="cpu">CPU</option></select></Field>
        <Field label="片段最短（秒）"><input className="input" type="number" step="0.5" value={f.segment_min_s ?? 2} onChange={(e) => setF({ ...f, segment_min_s: e.target.value })} /></Field>
        <Field label="片段目標長度（秒）"><input className="input" type="number" step="0.5" value={f.segment_target_s ?? 8} onChange={(e) => setF({ ...f, segment_target_s: e.target.value })} /></Field>
        <Field label="片段最長（秒）" hint="VoxCPM 建議 3–30 秒。"><input className="input" type="number" step="0.5" value={f.segment_max_s ?? 15} onChange={(e) => setF({ ...f, segment_max_s: e.target.value })} /></Field>
        <Field label={`說話者比對門檻 ${(+(f.speaker_match_threshold ?? 0.62)).toFixed(2)}`} hint="越高越嚴格：不夠像的片段會標「不確定是誰」。">
          <input type="range" min={0.4} max={0.85} step={0.01} value={f.speaker_match_threshold ?? 0.62} onChange={(e) => setF({ ...f, speaker_match_threshold: e.target.value })} className="w-full" /></Field>
      </div>
      <Button className="mt-4" onClick={() => save.mutate()} loading={save.isPending}>儲存</Button>
      {save.isSuccess && <span className="ml-3 text-sm text-emerald-600">已儲存（之後處理的錄音才會套用）</span>}
    </Card>
  );
}

function Extras() {
  const st = useSettings();
  const nav = useNavigate();
  const demo = useMutation({ mutationFn: () => api.post<{ id: string }>("/api/models/demo"), onSuccess: (m) => nav(`/speak?model=${m.id}`) });
  return (
    <div className="grid gap-6 lg:grid-cols-2">
      <Card title={<span className="flex items-center gap-2"><KeyRound className="size-4" />Hugging Face（選填）</span>}>
        <p className="mb-3 text-sm text-zinc-500">目前用到的模型都是公開的，不需要。只有下載速度被限制、或之後加入需要同意條款的模型時才用得到。</p>
        <SecretField name="hf_token" label="Hugging Face token（read 權限即可）" set={!!st.data?.secrets.hf_token} />
      </Card>
      <Card title={<span className="flex items-center gap-2"><FlaskConical className="size-4" />試用</span>}>
        <p className="mb-3 text-sm text-zinc-500">建立一個「測試模型」（哼聲，不是真的語音），不用 GPU 就能把文字轉語音和劇本配音的畫面全部走一遍。</p>
        <Button variant="secondary" onClick={() => demo.mutate()} loading={demo.isPending}>建立測試模型</Button>
      </Card>
      <Card title={<span className="flex items-center gap-2"><Shield className="size-4" />使用原則與授權</span>} className="lg:col-span-2">
        <ul className="list-disc space-y-1 pl-5 text-sm text-zinc-600 dark:text-zinc-400">
          <li>只訓練你自己、或有簽名同意書的人的聲音，以及原創設計的聲音。不要用來模仿藝人、名人或任何沒有同意的人。</li>
          <li>合成的檔案在中繼資料裡標記為 AI 合成。公開發布時請註明是合成語音。</li>
          <li>VoxCPM2（OpenBMB）、Qwen3-TTS（阿里巴巴 Qwen）：Apache-2.0。faster-whisper、Whisper、Silero VAD：MIT。</li>
          <li>說話者辨識模型 WeSpeaker ResNet34-LM（VoxCeleb 訓練）：CC BY 4.0，© WeSpeaker 團隊。</li>
          <li>人聲分離 BS-RoFormer（python-audio-separator）：MIT，模型權重依各自授權。</li>
        </ul>
      </Card>
    </div>
  );
}

type LexEntry = { from: string; to: string; lang: string };

function Lexicon() {
  const qc = useQueryClient();
  const st = useSettings();
  const [rows, setRows] = useState<LexEntry[]>([]);
  useEffect(() => { if (st.data) setRows((st.data.settings.lexicon as LexEntry[]) ?? []); }, [st.data]);
  const save = useMutation({ mutationFn: (lexicon: LexEntry[]) => api.put("/api/settings", { lexicon }), onSuccess: () => qc.invalidateQueries({ queryKey: ["settings"] }) });
  const set = (i: number, patch: Partial<LexEntry>) => setRows(rows.map((r, j) => (j === i ? { ...r, ...patch } : r)));
  return (
    <Card title={<span id="lexicon" className="flex items-center gap-2"><BookA className="size-4" />讀音字典</span>}>
      <p className="mb-4 text-sm text-zinc-500">模型念錯的人名、專有名詞、多音字，在這裡寫上正確念法（日文寫平假名或片假名最穩）。合成前會自動替換；畫面上和檢查漏字時仍然用你原本寫的字。</p>
      <div className="space-y-2">
        {rows.map((r, i) => (
          <div key={i} className="flex gap-2">
            <input className="input" placeholder="原本的字，例如 推し" value={r.from} onChange={(e) => set(i, { from: e.target.value })} />
            <input className="input" placeholder="念法，例如 おし" value={r.to} onChange={(e) => set(i, { to: e.target.value })} />
            <select className="input w-28" value={r.lang} onChange={(e) => set(i, { lang: e.target.value })}>
              <option value="">所有語言</option><option value="ja">日文</option><option value="en">英文</option>
            </select>
            <Button variant="ghost" onClick={() => setRows(rows.filter((_, j) => j !== i))}><Trash2 className="size-4" /></Button>
          </div>
        ))}
      </div>
      <div className="mt-3 flex gap-2">
        <Button variant="secondary" size="sm" onClick={() => setRows([...rows, { from: "", to: "", lang: "ja" }])}><Plus className="size-3.5" />新增一筆</Button>
        <Button size="sm" onClick={() => save.mutate(rows.filter((r) => r.from.trim() && r.to.trim()))} loading={save.isPending}>儲存</Button>
        {save.isSuccess && <span className="self-center text-sm text-emerald-600">已儲存</span>}
      </div>
    </Card>
  );
}

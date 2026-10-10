import { useState } from "react";
import { Link, useNavigate, useParams } from "react-router";
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { FileCheck2, Plus, ShieldAlert, ShieldCheck, Trash2, Upload, UserRound } from "lucide-react";
import { api, fmtMin, LANGS, type Dataset, type Model, type Voice } from "../api";
import { Badge, Button, Card, Empty, ErrorText, Field, Modal, PageHeader } from "../ui";
import { PhrasesCard } from "./Phrases";

const KIND: Record<string, string> = { self: "我自己", other: "其他人（需簽同意書）", designed: "原創設計聲音" };

export default function Voices() {
  const { id } = useParams();
  const nav = useNavigate();
  const qc = useQueryClient();
  const voices = useQuery({ queryKey: ["voices"], queryFn: () => api.get<Voice[]>("/api/voices") });
  const [creating, setCreating] = useState(false);
  const [form, setForm] = useState({ name: "", kind: "self", languages: ["ja", "en"] as string[], notes: "" });
  const create = useMutation({
    mutationFn: () => api.post<Voice>("/api/voices", form),
    onSuccess: (v) => { qc.invalidateQueries({ queryKey: ["voices"] }); setCreating(false); nav(`/voices/${v.id}`); },
  });
  const current = voices.data?.find((v) => v.id === id) ?? (id ? undefined : voices.data?.[0]);
  return (
    <div>
      <PageHeader title="聲音與同意"
        subtitle="每個要訓練的聲音都是一個「聲音」。訓練前一定要有完整的同意紀錄：自己的聲音簽自己的名字；別人的聲音要有對方簽名的同意書。"
        actions={<Button onClick={() => setCreating(true)}><Plus className="size-4" />新增聲音</Button>} />
      <div className="grid gap-6 lg:grid-cols-[280px_1fr]">
        <div className="space-y-2">
          {voices.data?.length === 0 && <Empty icon={<UserRound className="size-8" />} title="還沒有聲音">按「新增聲音」開始。</Empty>}
          {voices.data?.map((v) => (
            <Link key={v.id} to={`/voices/${v.id}`}
              className={`card flex items-center gap-3 p-3 transition hover:border-brand-300 ${v.id === current?.id ? "border-brand-500 ring-2 ring-brand-500/20" : ""}`}>
              <div className="flex size-9 items-center justify-center rounded-full bg-brand-100 font-semibold text-brand-700 dark:bg-brand-900/40 dark:text-brand-200">{v.name.slice(0, 1)}</div>
              <div className="min-w-0 flex-1">
                <div className="truncate font-medium">{v.name}</div>
                <div className="text-xs text-zinc-500">已核可 {fmtMin(v.stats.approved?.minutes ?? 0)} · 待檢查 {fmtMin(v.stats.pending?.minutes ?? 0)}</div>
              </div>
              {v.consent_ok ? <ShieldCheck className="size-4 text-emerald-500" /> : <ShieldAlert className="size-4 text-amber-500" />}
            </Link>
          ))}
        </div>
        <div>{current ? <VoiceDetail voice={current} /> : voices.data?.length ? <Empty title="選一個聲音查看詳細資料" /> : null}</div>
      </div>
      <Modal open={creating} onClose={() => setCreating(false)} title="新增聲音">
        <div className="space-y-4">
          <Field label="名稱（例如：我、阿明、角色A的配音員）"><input className="input" value={form.name} onChange={(e) => setForm({ ...form, name: e.target.value })} autoFocus /></Field>
          <Field label="這是誰的聲音？">
            <select className="input" value={form.kind} onChange={(e) => setForm({ ...form, kind: e.target.value })}>
              {Object.entries(KIND).map(([k, l]) => <option key={k} value={k}>{l}</option>)}
            </select>
          </Field>
          <Field label="會說的語言">
            <div className="flex gap-4 text-sm">
              {["ja", "en", "zh"].map((l) => (
                <label key={l} className="flex items-center gap-1.5">
                  <input type="checkbox" checked={form.languages.includes(l)}
                    onChange={(e) => setForm({ ...form, languages: e.target.checked ? [...form.languages, l] : form.languages.filter((x) => x !== l) })} />
                  {LANGS[l]}
                </label>
              ))}
            </div>
          </Field>
          <Field label="備註"><textarea className="input" rows={2} value={form.notes} onChange={(e) => setForm({ ...form, notes: e.target.value })} /></Field>
          <ErrorText error={create.error} />
          <div className="flex justify-end gap-2"><Button variant="secondary" onClick={() => setCreating(false)}>取消</Button>
            <Button onClick={() => create.mutate()} disabled={!form.name.trim()} loading={create.isPending}>建立</Button></div>
        </div>
      </Modal>
    </div>
  );
}

function VoiceDetail({ voice }: { voice: Voice }) {
  const qc = useQueryClient();
  const nav = useNavigate();
  const today = new Date().toISOString().slice(0, 10);
  const c = voice.consent;
  const [cf, setCf] = useState({
    signed_name: c?.signed_name ?? "", date: c?.date ?? today, relationship: c?.relationship ?? (voice.kind === "self" ? "本人" : ""),
    train: c ? c.scope.includes("train") : true, generate: c ? c.scope.includes("generate") : true,
    personal_only: c?.personal_only ?? true, document_note: c?.document_note ?? "", agreed: c?.agreed ?? false,
  });
  const [doc, setDoc] = useState<File | null>(null);
  const saveConsent = useMutation({
    mutationFn: () => {
      const fd = new FormData();
      fd.append("signed_name", cf.signed_name); fd.append("date", cf.date); fd.append("relationship", cf.relationship);
      fd.append("scope", [cf.train && "train", cf.generate && "generate"].filter(Boolean).join(","));
      fd.append("personal_only", String(cf.personal_only)); fd.append("document_note", cf.document_note);
      fd.append("agreed", String(cf.agreed));
      if (doc) fd.append("document", doc);
      return api.post<Voice>(`/api/voices/${voice.id}/consent`, fd);
    },
    onSuccess: () => qc.invalidateQueries({ queryKey: ["voices"] }),
  });
  const [enrollFiles, setEnrollFiles] = useState<FileList | null>(null);
  const enroll = useMutation({
    mutationFn: () => {
      const fd = new FormData();
      Array.from(enrollFiles ?? []).forEach((f) => fd.append("files", f));
      return api.post(`/api/voices/${voice.id}/enrollment`, fd);
    },
    onSuccess: () => { setEnrollFiles(null); qc.invalidateQueries({ queryKey: ["voices"] }); },
  });
  const delEnroll = useMutation({
    mutationFn: (i: number) => api.del(`/api/voices/${voice.id}/enrollment/${i}`),
    onSuccess: () => qc.invalidateQueries({ queryKey: ["voices"] }),
  });
  const del = useMutation({
    mutationFn: () => api.del(`/api/voices/${voice.id}`),
    onSuccess: () => { qc.invalidateQueries({ queryKey: ["voices"] }); nav("/voices"); },
  });
  const ds = useQuery({ queryKey: ["datasets", voice.id], queryFn: () => api.get<Dataset[]>(`/api/datasets?voice_id=${voice.id}`) });
  const models = useQuery({ queryKey: ["models", voice.id], queryFn: () => api.get<Model[]>(`/api/models?voice_id=${voice.id}`) });
  const needDoc = voice.kind === "other";
  return (
    <div className="space-y-6">
      <Card title={<span className="flex items-center gap-2">{voice.name} <Badge>{KIND[voice.kind]}</Badge></span>}
        actions={<Button variant="ghost" size="sm" onClick={() => confirm(`刪除「${voice.name}」？片段會保留但不再屬於任何聲音。`) && del.mutate()}><Trash2 className="size-4" />刪除</Button>}>
        <div className="grid gap-4 sm:grid-cols-3">
          {(["approved", "pending", "rejected"] as const).map((k) => (
            <div key={k} className="rounded-xl bg-zinc-50 p-3 dark:bg-zinc-800/50">
              <div className="text-xs text-zinc-500">{{ approved: "已核可", pending: "待檢查", rejected: "已排除" }[k]}</div>
              <div className="text-lg font-semibold">{(voice.stats[k]?.minutes ?? 0).toFixed(1)} 分</div>
              <div className="text-xs text-zinc-500">{voice.stats[k]?.count ?? 0} 段</div>
            </div>
          ))}
        </div>
        <p className="mt-3 text-sm text-zinc-500">建議目標：5–10 小時乾淨的已核可語音，日文英文各至少 2 小時，各種情緒都有一些。<Link to={`/review?voice=${voice.id}`} className="ml-1 text-brand-600 underline">去檢查資料</Link></p>
      </Card>

      <Card title={<span className="flex items-center gap-2">同意紀錄 {voice.consent_ok ? <Badge tone="green"><ShieldCheck className="size-3" />完整</Badge> : <Badge tone="amber"><ShieldAlert className="size-3" />未完成，不能訓練</Badge>}</span>}>
        <div className="grid gap-4 sm:grid-cols-2">
          <Field label="簽名（聲音本人的姓名）"><input className="input" value={cf.signed_name} onChange={(e) => setCf({ ...cf, signed_name: e.target.value })} /></Field>
          <Field label="同意日期"><input type="date" className="input" value={cf.date} onChange={(e) => setCf({ ...cf, date: e.target.value })} /></Field>
          <Field label="和你的關係"><input className="input" value={cf.relationship} onChange={(e) => setCf({ ...cf, relationship: e.target.value })} placeholder="本人／朋友／委託的配音員…" /></Field>
          <Field label={needDoc ? "簽名的同意書（必填其一：上傳檔案或註明存放處）" : "同意書（可選）"}>
            <input type="file" accept=".pdf,.png,.jpg,.jpeg" className="input" onChange={(e) => setDoc(e.target.files?.[0] ?? null)} />
            {voice.consent_doc && <span className="mt-1 flex items-center gap-1 text-xs text-emerald-600"><FileCheck2 className="size-3" />已上傳</span>}
          </Field>
          <Field label="同意書存放處（沒有上傳檔案時填）"><input className="input" value={cf.document_note} onChange={(e) => setCf({ ...cf, document_note: e.target.value })} placeholder="例如：紙本放在工作室資料夾 A-3" /></Field>
          <div className="space-y-2 text-sm">
            <span className="label">同意範圍</span>
            <label className="flex items-center gap-2"><input type="checkbox" checked={cf.train} onChange={(e) => setCf({ ...cf, train: e.target.checked })} />用錄音訓練語音模型</label>
            <label className="flex items-center gap-2"><input type="checkbox" checked={cf.generate} onChange={(e) => setCf({ ...cf, generate: e.target.checked })} />用模型產生新的語音</label>
            <label className="flex items-center gap-2"><input type="checkbox" checked={cf.personal_only} onChange={(e) => setCf({ ...cf, personal_only: e.target.checked })} />僅限個人使用</label>
          </div>
        </div>
        <label className="mt-4 flex items-start gap-2 rounded-xl bg-amber-50 p-3 text-sm dark:bg-amber-950/30">
          <input type="checkbox" className="mt-1" checked={cf.agreed} onChange={(e) => setCf({ ...cf, agreed: e.target.checked })} />
          <span>我確認：聲音本人知道並同意以上範圍，錄音也是我有權使用的。不會用這個平台模仿沒有同意的真人聲音。</span>
        </label>
        <ErrorText error={saveConsent.error} />
        <div className="mt-4 flex justify-end"><Button onClick={() => saveConsent.mutate()} loading={saveConsent.isPending} disabled={!cf.signed_name || !cf.agreed}>儲存同意紀錄</Button></div>
      </Card>

      <Card title={`參考聲紋（${voice.enrolled}/${voice.enrollment.length}）`}>
        <p className="mb-3 text-sm text-zinc-500">上傳 1～5 段「只有這個人在說話」的短錄音（各 5～30 秒）。匯入多人錄音時，平台會用聲紋自動分辨誰在說話。只有一個人的錄音可以略過這步，匯入時指定說話者就好。</p>
        <div className="mb-3 space-y-1">
          {voice.enrollment.map((e, i) => (
            <div key={i} className="flex items-center justify-between rounded-lg bg-zinc-50 px-3 py-1.5 text-sm dark:bg-zinc-800/50">
              <span className="truncate">{e.from}</span>
              <Button variant="ghost" size="sm" onClick={() => delEnroll.mutate(i)}><Trash2 className="size-3.5" /></Button>
            </div>
          ))}
        </div>
        <div className="flex flex-wrap items-center gap-2">
          <input type="file" multiple accept="audio/*,video/*" onChange={(e) => setEnrollFiles(e.target.files)} className="input max-w-sm" />
          <Button variant="secondary" onClick={() => enroll.mutate()} disabled={!enrollFiles?.length} loading={enroll.isPending}><Upload className="size-4" />加入聲紋</Button>
        </div>
      </Card>

      <PhrasesCard voice={voice} />

      <div className="grid gap-6 md:grid-cols-2">
        <Card title="訓練資料版本">
          {ds.data?.length ? ds.data.map((d) => (
            <div key={d.id} className="flex items-center justify-between border-b border-zinc-100 py-2 text-sm last:border-0 dark:border-zinc-800">
              <span>{d.name}</span><span className="text-zinc-500">{d.n_items} 段 · {(d.hours * 60).toFixed(0)} 分</span>
            </div>
          )) : <p className="text-sm text-zinc-500">還沒有。到「雲端訓練」從已核可的片段建立。</p>}
        </Card>
        <Card title="模型">
          {models.data?.length ? models.data.map((m) => (
            <div key={m.id} className="flex items-center justify-between border-b border-zinc-100 py-2 text-sm last:border-0 dark:border-zinc-800">
              <span>{m.name}</span><Link to={`/speak?model=${m.id}`} className="text-brand-600 underline">試聽</Link>
            </div>
          )) : <p className="text-sm text-zinc-500">還沒有訓練好的模型。</p>}
        </Card>
      </div>
    </div>
  );
}

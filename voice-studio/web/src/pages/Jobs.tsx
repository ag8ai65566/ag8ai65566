import { useState } from "react";
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { FileText, RotateCcw, Square } from "lucide-react";
import { api, fmtTime, type Job } from "../api";
import { Badge, Button, Card, Empty, Modal, PageHeader, Progress } from "../ui";

const KIND: Record<string, string> = {
  prepare_source: "處理錄音", enroll_voice: "登錄聲紋", cloud_train: "雲端訓練", evaluate_model: "評分檢查點",
  render_script: "合成場景", install_engine: "安裝引擎",
};
const STATUS: Record<string, [string, "zinc" | "green" | "amber" | "red" | "brand" | "blue"]> = {
  queued: ["排隊中", "zinc"], running: ["執行中", "brand"], done: ["完成", "green"], failed: ["失敗", "red"], canceled: ["已取消", "zinc"],
};

export default function Jobs() {
  const qc = useQueryClient();
  const jobs = useQuery({ queryKey: ["jobs", "all"], queryFn: () => api.get<Job[]>("/api/jobs?limit=100"), refetchInterval: 2000 });
  const [open, setOpen] = useState<string | null>(null);
  const cancel = useMutation({ mutationFn: (id: string) => api.post(`/api/jobs/${id}/cancel`), onSuccess: () => qc.invalidateQueries({ queryKey: ["jobs"] }) });
  const retry = useMutation({ mutationFn: (id: string) => api.post(`/api/jobs/${id}/retry`), onSuccess: () => qc.invalidateQueries({ queryKey: ["jobs"] }) });
  return (
    <div>
      <PageHeader title="工作佇列" subtitle="背景在做的事。用到本機 GPU 的工作（處理錄音、評分、合成場景）一次只跑一個；上傳、雲端訓練和下載在另一條線上同時進行。關掉視窗不會中斷，重新打開 Voice Studio 時沒做完的會標成失敗，可以重試。" />
      <Card>
        {!jobs.data?.length ? <Empty title="沒有工作" /> : (
          <ul className="divide-y divide-zinc-100 dark:divide-zinc-800">
            {jobs.data.map((j) => {
              const [label, tone] = STATUS[j.status] ?? [j.status, "zinc"];
              return (
                <li key={j.id} className="flex flex-wrap items-center gap-3 py-3">
                  <div className="min-w-0 flex-1">
                    <div className="flex items-center gap-2 text-sm"><span className="font-medium">{KIND[j.kind] ?? j.kind}</span><Badge tone={tone}>{label}</Badge>
                      <span className="text-xs text-zinc-500">{fmtTime(j.created_at)}</span></div>
                    <div className="mt-0.5 truncate text-xs text-zinc-500">{j.message}</div>
                    {j.status === "running" && <Progress value={j.progress} className="mt-1.5 max-w-md" />}
                  </div>
                  <Button size="sm" variant="ghost" onClick={() => setOpen(j.id)}><FileText className="size-3.5" />詳細</Button>
                  {(j.status === "running" || j.status === "queued") && <Button size="sm" variant="ghost" onClick={() => cancel.mutate(j.id)}><Square className="size-3.5" />取消</Button>}
                  {(j.status === "failed" || j.status === "canceled") && <Button size="sm" variant="secondary" onClick={() => retry.mutate(j.id)}><RotateCcw className="size-3.5" />重試</Button>}
                </li>
              );
            })}
          </ul>
        )}
      </Card>
      {open && <JobModal id={open} onClose={() => setOpen(null)} />}
    </div>
  );
}

function JobModal({ id, onClose }: { id: string; onClose: () => void }) {
  const j = useQuery({ queryKey: ["job", id], queryFn: () => api.get<Job>(`/api/jobs/${id}`), refetchInterval: 3000 });
  return (
    <Modal open onClose={onClose} title={KIND[j.data?.kind ?? ""] ?? "工作"} wide>
      <div className="text-sm">{j.data?.message}</div>
      {j.data?.result && Object.keys(j.data.result).length > 0 && (
        <pre className="mt-3 overflow-x-auto rounded-lg bg-zinc-100 p-3 text-xs dark:bg-zinc-800">{JSON.stringify(j.data.result, null, 2)}</pre>
      )}
      <div className="label mt-4">紀錄</div>
      <pre className="max-h-[50vh] overflow-auto rounded-xl bg-zinc-950 p-4 text-[11px] leading-5 whitespace-pre-wrap text-zinc-200">{j.data?.log || "（沒有紀錄）"}</pre>
    </Modal>
  );
}

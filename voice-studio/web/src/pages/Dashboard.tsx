import { Link } from "react-router";
import { useQuery } from "@tanstack/react-query";
import { CheckCircle2, Circle, Cpu, HardDrive } from "lucide-react";
import { api, fmtMin, type SystemInfo, type Voice } from "../api";
import { Badge, Card, PageHeader, Stat } from "../ui";

export default function Dashboard() {
  const sys = useQuery({ queryKey: ["system"], queryFn: () => api.get<SystemInfo>("/api/system"), refetchInterval: 10000 });
  const voices = useQuery({ queryKey: ["voices"], queryFn: () => api.get<Voice[]>("/api/voices") });
  const st = useQuery({ queryKey: ["settings"], queryFn: () => api.get<{ secrets: Record<string, boolean>; settings: Record<string, unknown> }>("/api/settings") });
  const c = sys.data?.counts ?? {};
  const approvedMin = (voices.data ?? []).reduce((a, v) => a + (v.stats.approved?.minutes ?? 0), 0);
  const steps = [
    { done: (voices.data ?? []).some((v) => v.consent_ok), label: "建立聲音並填寫同意紀錄", to: "/voices" },
    { done: (c.sources ?? 0) > 0, label: "匯入錄音（自動切音、辨識說話者、轉文字）", to: "/import" },
    { done: approvedMin > 0, label: "檢查並核可片段", to: "/review" },
    { done: !!st.data?.secrets.runpod_api_key && !!st.data?.settings.runpod_volume_id, label: "設定 RunPod 雲端 GPU", to: "/settings" },
    { done: (c.models ?? 0) > 0, label: "開始雲端訓練", to: "/train" },
    { done: (c.outputs ?? 0) > 0, label: "用訓練好的聲音做文字轉語音", to: "/speak" },
  ];
  const next = steps.findIndex((s) => !s.done);
  return (
    <div>
      <PageHeader title="總覽" subtitle="從錄音到可以直接使用的語音模型。照下面的順序走一遍，第一次大約需要半天（大部分時間是雲端訓練）。" />
      <div className="grid gap-4 md:grid-cols-4">
        <Stat label="聲音" value={c.voices ?? 0} />
        <Stat label="已核可語音" value={fmtMin(approvedMin)} sub={`共 ${c.segments ?? 0} 個片段`} />
        <Stat label="模型" value={c.models ?? 0} />
        <Stat label="合成紀錄" value={c.outputs ?? 0} />
      </div>
      <div className="mt-6 grid gap-6 lg:grid-cols-3">
        <Card title="開始使用" className="lg:col-span-2">
          <ol className="space-y-2">
            {steps.map((s, i) => (
              <li key={s.label}>
                <Link to={s.to} className="flex items-center gap-3 rounded-xl px-3 py-2.5 hover:bg-zinc-50 dark:hover:bg-zinc-800/50">
                  {s.done ? <CheckCircle2 className="size-5 text-emerald-500" /> : <Circle className="size-5 text-zinc-300" />}
                  <span className={i === next ? "font-semibold" : s.done ? "text-zinc-500" : ""}>{i + 1}. {s.label}</span>
                  {i === next && <Badge tone="brand">下一步</Badge>}
                </Link>
              </li>
            ))}
          </ol>
          <p className="mt-4 text-sm text-zinc-500">不知道怎麼開始？看 <Link to="/guide" className="text-brand-600 underline">教學</Link>，每一步都有圖文說明。</p>
        </Card>
        <Card title="這台電腦">
          <div className="space-y-3 text-sm">
            <div className="flex items-start gap-2">
              <Cpu className="mt-0.5 size-4 text-zinc-400" />
              <div>
                {sys.data?.gpu.available
                  ? <><div className="font-medium">{sys.data.gpu.name}</div><div className="text-zinc-500">{sys.data.gpu.vram_gb} GB 顯示記憶體（可用 {sys.data.gpu.free_gb} GB）</div>
                    {(sys.data.gpu.vram_gb ?? 0) < 12 && <div className="mt-1 text-xs text-amber-600">VoxCPM2 合成約需 8 GB：放得下，但合成時請關掉遊戲、OBS 等也用顯示卡的程式。檢查漏字會自動改用 CPU。</div>}</>
                  : <div className="text-amber-600">{sys.data?.gpu.note ?? "沒有偵測到 NVIDIA 顯示卡"}</div>}
              </div>
            </div>
            <div className="flex items-start gap-2">
              <HardDrive className="mt-0.5 size-4 text-zinc-400" />
              <div><div>剩餘空間 {sys.data?.disk_free_gb ?? "?"} GB</div><div className="break-all text-xs text-zinc-500">{sys.data?.data_dir}</div></div>
            </div>
            <div className="text-xs text-zinc-400">Voice Studio {sys.data?.version} · Python {sys.data?.python}</div>
          </div>
        </Card>
      </div>
    </div>
  );
}

import { NavLink, Route, Routes } from "react-router";
import { useQuery } from "@tanstack/react-query";
import clsx from "clsx";
import {
  AudioLines, BookOpen, Boxes, ClipboardCheck, Cpu, FileText, Home, ListChecks, Mic2, Moon, Settings2, Sun,
  Upload, Users, Wand2,
} from "lucide-react";
import { api, type Job } from "./api";
import Dashboard from "./pages/Dashboard";
import Voices from "./pages/Voices";
import ImportPage from "./pages/Import";
import Review from "./pages/Review";
import Train from "./pages/Train";
import Models from "./pages/Models";
import Speak from "./pages/Speak";
import Script from "./pages/Script";
import Characters from "./pages/Characters";
import Jobs from "./pages/Jobs";
import Settings from "./pages/Settings";
import Guide from "./pages/Guide";

const NAV = [
  { to: "/", label: "總覽", icon: Home },
  { group: "準備資料" },
  { to: "/voices", label: "聲音與同意", icon: Users },
  { to: "/import", label: "匯入錄音", icon: Upload },
  { to: "/review", label: "檢查資料", icon: ClipboardCheck },
  { group: "訓練" },
  { to: "/train", label: "雲端訓練", icon: Cpu },
  { to: "/models", label: "模型", icon: Boxes },
  { group: "使用" },
  { to: "/speak", label: "文字轉語音", icon: Mic2 },
  { to: "/script", label: "劇本配音", icon: FileText },
  { to: "/characters", label: "角色預設", icon: Wand2 },
  { group: "其他" },
  { to: "/jobs", label: "工作佇列", icon: ListChecks },
  { to: "/settings", label: "設定", icon: Settings2 },
  { to: "/guide", label: "教學", icon: BookOpen },
] as const;

function ActiveJobs() {
  const { data } = useQuery({ queryKey: ["jobs", "active"], queryFn: () => api.get<Job[]>("/api/jobs?active=true"),
    refetchInterval: 2000 });
  if (!data?.length) return null;
  const j = data.find((x) => x.status === "running") ?? data[0];
  return (
    <NavLink to="/jobs" className="flex min-w-0 items-center gap-2 rounded-full bg-brand-50 px-3 py-1 text-xs text-brand-700 dark:bg-brand-900/30 dark:text-brand-200">
      <span className="relative flex size-2"><span className="absolute inline-flex size-full animate-ping rounded-full bg-brand-400 opacity-75" /><span className="relative inline-flex size-2 rounded-full bg-brand-500" /></span>
      <span className="truncate">{data.length} 個工作 · {j.message} {j.status === "running" ? `${Math.round(j.progress * 100)}%` : ""}</span>
    </NavLink>
  );
}

export default function App() {
  const toggle = () => {
    const d = document.documentElement.classList.toggle("dark");
    localStorage.setItem("theme", d ? "dark" : "light");
  };
  return (
    <div className="flex h-full">
      <aside className="hidden w-60 shrink-0 flex-col border-r border-zinc-200 bg-white md:flex dark:border-zinc-800 dark:bg-zinc-900">
        <div className="flex items-center gap-2 px-5 py-5">
          <div className="flex size-8 items-center justify-center rounded-lg bg-brand-600 text-white"><AudioLines className="size-5" /></div>
          <div>
            <div className="font-bold leading-tight">Voice Studio</div>
            <div className="text-[11px] text-zinc-500">聲音訓練與語音合成</div>
          </div>
        </div>
        <nav className="flex-1 overflow-y-auto px-3 pb-4">
          {NAV.map((n, i) =>
            "group" in n ? (
              <div key={i} className="mt-4 mb-1 px-2 text-[11px] font-semibold tracking-wide text-zinc-400 uppercase">{n.group}</div>
            ) : (
              <NavLink key={n.to} to={n.to} end={n.to === "/"}
                className={({ isActive }) => clsx("mb-0.5 flex items-center gap-2.5 rounded-lg px-2.5 py-2 text-sm transition",
                  isActive ? "bg-brand-50 font-medium text-brand-700 dark:bg-brand-900/30 dark:text-brand-200"
                    : "text-zinc-600 hover:bg-zinc-100 dark:text-zinc-400 dark:hover:bg-zinc-800")}>
                <n.icon className="size-4" />{n.label}
              </NavLink>
            ),
          )}
        </nav>
      </aside>
      <div className="flex min-w-0 flex-1 flex-col">
        <header className="flex h-14 shrink-0 items-center justify-between gap-4 border-b border-zinc-200 bg-white/80 px-6 backdrop-blur dark:border-zinc-800 dark:bg-zinc-900/80">
          <ActiveJobs />
          <div className="ml-auto flex items-center gap-2">
            <button onClick={toggle} className="rounded-lg p-2 text-zinc-500 hover:bg-zinc-100 dark:hover:bg-zinc-800" title="切換深色模式">
              <Sun className="hidden size-4 dark:block" /><Moon className="size-4 dark:hidden" />
            </button>
          </div>
        </header>
        <main className="flex-1 overflow-y-auto">
          <div className="mx-auto max-w-6xl px-6 py-8">
            <Routes>
              <Route path="/" element={<Dashboard />} />
              <Route path="/voices" element={<Voices />} />
              <Route path="/voices/:id" element={<Voices />} />
              <Route path="/import" element={<ImportPage />} />
              <Route path="/review" element={<Review />} />
              <Route path="/train" element={<Train />} />
              <Route path="/models" element={<Models />} />
              <Route path="/speak" element={<Speak />} />
              <Route path="/script" element={<Script />} />
              <Route path="/characters" element={<Characters />} />
              <Route path="/jobs" element={<Jobs />} />
              <Route path="/settings" element={<Settings />} />
              <Route path="/guide" element={<Guide />} />
              <Route path="/guide/:doc" element={<Guide />} />
            </Routes>
          </div>
        </main>
      </div>
    </div>
  );
}

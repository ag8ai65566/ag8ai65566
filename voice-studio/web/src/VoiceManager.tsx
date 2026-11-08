import { useEffect, useRef, useState } from "react";
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { AppWindow, Check, ChevronDown, FolderOpen } from "lucide-react";
import { api } from "./api";
import { Button, ErrorText } from "./ui";

type Status = {
  target: string; resolved: string | null; folder: string; folder_exists: boolean; candidates: string[]; is_url: boolean;
};
const URL_RX = /^https?:\/\/\S+$/i;
const base = (p: string) => p.split(/[\\/]/).pop() ?? p;
const dir = (p: string) => p.slice(0, p.length - base(p).length).replace(/[\\/]$/, "");

/** Top-right button: opens the Voice Manager program on this computer in one click (chosen once, then remembered). */
export default function VoiceManagerButton() {
  const qc = useQueryClient();
  const st = useQuery({ queryKey: ["voice-manager"], queryFn: () => api.get<Status>("/api/launcher/voice-manager"), staleTime: 30_000 });
  const [open, setOpen] = useState(false);
  const [path, setPath] = useState("");
  const [done, setDone] = useState(false);
  const box = useRef<HTMLDivElement>(null);
  useEffect(() => {
    if (!open) return;
    const close = (e: MouseEvent) => { if (box.current && !box.current.contains(e.target as Node)) setOpen(false); };
    document.addEventListener("mousedown", close);
    return () => document.removeEventListener("mousedown", close);
  }, [open]);
  const launch = useMutation({
    mutationFn: (target?: string) => api.post<{ opened: string; url: string | null }>("/api/launcher/voice-manager/open",
      target ? { target } : {}),
    onSuccess: () => {
      setOpen(false);
      setDone(true);
      setTimeout(() => setDone(false), 2000);
      qc.invalidateQueries({ queryKey: ["voice-manager"] });
    },
  });
  // a web address opens in a new tab right away (a tab opened after waiting for the server would be blocked)
  const go = (target?: string) => {
    const t = target ?? st.data?.resolved ?? "";
    if (URL_RX.test(t)) window.open(t, "_blank", "noopener");
    launch.mutate(target);
  };
  const click = () => (st.data?.resolved ? go() : setOpen(true));
  const s = st.data;

  return (
    <div className="relative" ref={box}>
      <div className="flex items-center rounded-lg border border-zinc-200 dark:border-zinc-700">
        <button onClick={click} disabled={launch.isPending}
          title={s?.resolved ? `開啟 ${s.resolved}` : "選擇要開啟的 Voice Manager"}
          className="flex items-center gap-1.5 rounded-l-lg px-2.5 py-1.5 text-sm text-zinc-700 hover:bg-zinc-100 disabled:opacity-60 dark:text-zinc-200 dark:hover:bg-zinc-800">
          {done ? <Check className="size-4 text-emerald-600" /> : <AppWindow className="size-4" />}
          {done ? "已開啟" : "Voice Manager"}
        </button>
        <button onClick={() => setOpen(!open)} title="更改要開啟的程式"
          className="rounded-r-lg border-l border-zinc-200 px-1.5 py-1.5 text-zinc-500 hover:bg-zinc-100 dark:border-zinc-700 dark:hover:bg-zinc-800">
          <ChevronDown className="size-3.5" />
        </button>
      </div>
      {open && (
        <div className="absolute right-0 z-40 mt-1 w-[min(30rem,calc(100vw-2rem))] rounded-xl border border-zinc-200 bg-white p-4 text-sm shadow-xl dark:border-zinc-700 dark:bg-zinc-900">
          <div className="font-medium">按 Voice Manager 時要開啟哪一個？</div>
          {s?.target && <div className="mt-1 truncate text-xs text-zinc-500" title={s.target}>目前：{s.target}</div>}
          {s && s.candidates.length > 0 ? (
            <div className="mt-3 space-y-1">
              <div className="text-xs text-zinc-500">在 {s.folder} 找到：</div>
              {s.candidates.map((c) => (
                <button key={c} onClick={() => go(c)}
                  className="flex w-full items-center gap-2 rounded-lg border border-zinc-200 px-3 py-2 text-left hover:border-brand-400 hover:bg-brand-50 dark:border-zinc-700 dark:hover:bg-brand-900/20">
                  <AppWindow className="size-4 shrink-0 text-zinc-400" />
                  <span className="min-w-0"><span className="block truncate font-medium">{base(c)}</span>
                    <span className="block truncate text-[11px] text-zinc-500">{dir(c)}</span></span>
                </button>
              ))}
            </div>
          ) : s && (
            <p className="mt-3 text-xs text-zinc-500">{s.folder_exists ? `在 ${s.folder} 沒有找到 .exe、.bat 或捷徑。` : `找不到 ${s.folder}。`}下面貼上要開啟的檔案路徑。</p>
          )}
          <div className="mt-3 flex gap-2">
            <input className="input flex-1 font-mono text-xs" value={path} onChange={(e) => setPath(e.target.value)}
              placeholder="E:\HololiveVoiceManager\啟動.bat 或 http://127.0.0.1:8000"
              onKeyDown={(e) => e.key === "Enter" && path.trim() && go(path.trim())} />
            <Button size="sm" onClick={() => go(path.trim())} disabled={!path.trim()} loading={launch.isPending}>
              <FolderOpen className="size-3.5" />記住並開啟
            </Button>
          </div>
          <p className="mt-2 text-[11px] leading-5 text-zinc-500">可以是程式（.exe）、批次檔（.bat）、捷徑（.lnk）、資料夾或網址。選一次之後，按 Voice Manager 就直接開啟。路徑可以在檔案總管對檔案按 Shift＋右鍵 →「複製路徑」。</p>
          <ErrorText error={launch.error} />
        </div>
      )}
      {!open && launch.error ? <div className="absolute right-0 z-40 mt-1 w-72"><ErrorText error={launch.error} /></div> : null}
    </div>
  );
}

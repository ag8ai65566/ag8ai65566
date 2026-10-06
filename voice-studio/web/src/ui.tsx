import { useEffect, useRef, useState, type ReactNode } from "react";
import clsx from "clsx";
import WaveSurfer from "wavesurfer.js";
import { Loader2, Pause, Play, X } from "lucide-react";

export function Button({ children, onClick, variant = "primary", size = "md", disabled, loading, type = "button",
  title, className }: {
  children: ReactNode; onClick?: () => void; variant?: "primary" | "secondary" | "ghost" | "danger";
  size?: "sm" | "md"; disabled?: boolean; loading?: boolean; type?: "button" | "submit"; title?: string; className?: string;
}) {
  return (
    <button type={type} title={title} disabled={disabled || loading} onClick={onClick}
      className={clsx(
        "inline-flex items-center justify-center gap-1.5 rounded-lg font-medium transition disabled:cursor-not-allowed disabled:opacity-50",
        size === "sm" ? "px-2.5 py-1.5 text-xs" : "px-4 py-2 text-sm",
        variant === "primary" && "bg-brand-600 text-white shadow-sm hover:bg-brand-700",
        variant === "secondary" && "border border-zinc-300 bg-white hover:bg-zinc-50 dark:border-zinc-700 dark:bg-zinc-900 dark:hover:bg-zinc-800",
        variant === "ghost" && "text-zinc-600 hover:bg-zinc-100 dark:text-zinc-300 dark:hover:bg-zinc-800",
        variant === "danger" && "bg-red-600 text-white hover:bg-red-700",
        className)}>
      {loading && <Loader2 className="size-4 animate-spin" />}
      {children}
    </button>
  );
}

export function Card({ children, className, title, actions }: {
  children: ReactNode; className?: string; title?: ReactNode; actions?: ReactNode;
}) {
  return (
    <section className={clsx("card", className)}>
      {(title || actions) && (
        <header className="flex items-center justify-between gap-3 border-b border-zinc-100 px-5 py-3 dark:border-zinc-800">
          <h3 className="font-semibold">{title}</h3>
          <div className="flex items-center gap-2">{actions}</div>
        </header>
      )}
      <div className="p-5">{children}</div>
    </section>
  );
}

export function PageHeader({ title, subtitle, actions }: { title: string; subtitle?: ReactNode; actions?: ReactNode }) {
  return (
    <div className="mb-6 flex flex-wrap items-end justify-between gap-4">
      <div>
        <h1 className="text-2xl font-bold tracking-tight">{title}</h1>
        {subtitle && <p className="mt-1 max-w-3xl text-sm text-zinc-500 dark:text-zinc-400">{subtitle}</p>}
      </div>
      {actions && <div className="flex gap-2">{actions}</div>}
    </div>
  );
}

export function Badge({ children, tone = "zinc" }: { children: ReactNode; tone?: "zinc" | "green" | "amber" | "red" | "brand" | "blue" }) {
  return (
    <span className={clsx("inline-flex items-center gap-1 rounded-full px-2 py-0.5 text-[11px] font-medium",
      tone === "zinc" && "bg-zinc-100 text-zinc-700 dark:bg-zinc-800 dark:text-zinc-300",
      tone === "green" && "bg-emerald-100 text-emerald-800 dark:bg-emerald-900/40 dark:text-emerald-300",
      tone === "amber" && "bg-amber-100 text-amber-800 dark:bg-amber-900/40 dark:text-amber-300",
      tone === "red" && "bg-red-100 text-red-800 dark:bg-red-900/40 dark:text-red-300",
      tone === "blue" && "bg-sky-100 text-sky-800 dark:bg-sky-900/40 dark:text-sky-300",
      tone === "brand" && "bg-brand-100 text-brand-700 dark:bg-brand-900/40 dark:text-brand-200")}>
      {children}
    </span>
  );
}

export function Progress({ value, className }: { value: number; className?: string }) {
  return (
    <div className={clsx("h-2 w-full overflow-hidden rounded-full bg-zinc-200 dark:bg-zinc-800", className)}>
      <div className="h-full rounded-full bg-brand-500 transition-all" style={{ width: `${Math.round(value * 100)}%` }} />
    </div>
  );
}

export function Field({ label, children, hint }: { label: string; children: ReactNode; hint?: ReactNode }) {
  return (
    <label className="block">
      <span className="label">{label}</span>
      {children}
      {hint && <span className="mt-1 block text-xs text-zinc-500">{hint}</span>}
    </label>
  );
}

export function Empty({ icon, title, children }: { icon?: ReactNode; title: string; children?: ReactNode }) {
  return (
    <div className="flex flex-col items-center justify-center rounded-2xl border border-dashed border-zinc-300 px-6 py-12 text-center dark:border-zinc-700">
      {icon && <div className="mb-3 text-zinc-400">{icon}</div>}
      <p className="font-medium">{title}</p>
      {children && <div className="mt-2 max-w-md text-sm text-zinc-500">{children}</div>}
    </div>
  );
}

export function Modal({ open, onClose, title, children, wide }: {
  open: boolean; onClose: () => void; title: string; children: ReactNode; wide?: boolean;
}) {
  useEffect(() => {
    const k = (e: KeyboardEvent) => e.key === "Escape" && onClose();
    window.addEventListener("keydown", k);
    return () => window.removeEventListener("keydown", k);
  }, [onClose]);
  if (!open) return null;
  return (
    <div className="fixed inset-0 z-50 flex items-start justify-center overflow-y-auto bg-black/40 p-4 pt-16 backdrop-blur-sm" onMouseDown={onClose}>
      <div className={clsx("card w-full", wide ? "max-w-3xl" : "max-w-lg")} onMouseDown={(e) => e.stopPropagation()}>
        <header className="flex items-center justify-between border-b border-zinc-100 px-5 py-3 dark:border-zinc-800">
          <h3 className="font-semibold">{title}</h3>
          <button onClick={onClose} className="rounded p-1 hover:bg-zinc-100 dark:hover:bg-zinc-800"><X className="size-4" /></button>
        </header>
        <div className="p-5">{children}</div>
      </div>
    </div>
  );
}

/** Waveform player (wavesurfer). `compact` draws a small inline wave for lists. */
export function Wave({ src, compact, autoplayKey }: { src: string; compact?: boolean; autoplayKey?: number }) {
  const el = useRef<HTMLDivElement>(null);
  const ws = useRef<WaveSurfer | null>(null);
  const [playing, setPlaying] = useState(false);
  useEffect(() => {
    if (!el.current) return;
    const dark = document.documentElement.classList.contains("dark");
    const w = WaveSurfer.create({
      container: el.current, url: src, height: compact ? 36 : 72, barWidth: 2, barGap: 1, barRadius: 2,
      waveColor: dark ? "#52525b" : "#c4b5fd", progressColor: "#7c3aed", cursorColor: "#7c3aed", normalize: true,
    });
    w.on("play", () => setPlaying(true));
    w.on("pause", () => setPlaying(false));
    w.on("finish", () => setPlaying(false));
    ws.current = w;
    return () => w.destroy();
  }, [src, compact]);
  useEffect(() => {
    if (autoplayKey && ws.current) ws.current.play().catch(() => undefined);
  }, [autoplayKey]);
  return (
    <div className="flex items-center gap-3">
      <button onClick={() => ws.current?.playPause()}
        className="flex size-9 shrink-0 items-center justify-center rounded-full bg-brand-600 text-white hover:bg-brand-700">
        {playing ? <Pause className="size-4" /> : <Play className="ml-0.5 size-4" />}
      </button>
      <div ref={el} className="min-w-0 flex-1" />
    </div>
  );
}

export function Stat({ label, value, sub }: { label: string; value: ReactNode; sub?: ReactNode }) {
  return (
    <div className="card p-4">
      <div className="text-xs text-zinc-500">{label}</div>
      <div className="mt-1 text-2xl font-semibold tabular-nums">{value}</div>
      {sub && <div className="mt-0.5 text-xs text-zinc-500">{sub}</div>}
    </div>
  );
}

export function ErrorText({ error }: { error: unknown }) {
  if (!error) return null;
  return <p className="mt-2 rounded-lg bg-red-50 px-3 py-2 text-sm text-red-700 dark:bg-red-950/40 dark:text-red-300">{String((error as Error).message ?? error)}</p>;
}

export function Steps({ steps, current }: { steps: string[]; current: number }) {
  return (
    <ol className="mb-6 flex flex-wrap items-center gap-2 text-sm">
      {steps.map((s, i) => (
        <li key={s} className="flex items-center gap-2">
          <span className={clsx("flex size-6 items-center justify-center rounded-full text-xs font-semibold",
            i < current ? "bg-emerald-500 text-white" : i === current ? "bg-brand-600 text-white" : "bg-zinc-200 text-zinc-500 dark:bg-zinc-800")}>{i + 1}</span>
          <span className={clsx(i === current ? "font-semibold" : "text-zinc-500")}>{s}</span>
          {i < steps.length - 1 && <span className="mx-1 h-px w-6 bg-zinc-300 dark:bg-zinc-700" />}
        </li>
      ))}
    </ol>
  );
}

/** One shared audio element for lists with many clips (cheaper than a waveform per row). */
let sharedAudio: HTMLAudioElement | null = null;
let sharedSetter: ((u: string | null) => void) | null = null;

export function usePlayer() {
  const [playing, setPlaying] = useState<string | null>(null);
  useEffect(() => () => { if (sharedSetter === setPlaying) { sharedAudio?.pause(); sharedSetter = null; } }, []);
  const toggle = (url: string) => {
    if (!sharedAudio) sharedAudio = new Audio();
    if (sharedSetter && sharedSetter !== setPlaying) sharedSetter(null);
    sharedSetter = setPlaying;
    sharedAudio.onended = () => setPlaying(null);
    if (playing === url) { sharedAudio.pause(); setPlaying(null); return; }
    sharedAudio.src = url;
    sharedAudio.play().catch(() => setPlaying(null));
    setPlaying(url);
  };
  return { playing, toggle };
}

export function PlayButton({ url, player, label, small }: {
  url: string; player: ReturnType<typeof usePlayer>; label?: string; small?: boolean;
}) {
  const on = player.playing === url;
  return (
    <button onClick={(e) => { e.stopPropagation(); player.toggle(url); }} title={label}
      className={clsx("inline-flex items-center gap-1 rounded-full font-medium transition",
        small ? "px-2 py-1 text-[11px]" : "px-3 py-1.5 text-xs",
        on ? "bg-brand-600 text-white" : "bg-zinc-100 text-zinc-700 hover:bg-brand-100 dark:bg-zinc-800 dark:text-zinc-200")}>
      {on ? <Pause className="size-3" /> : <Play className="size-3" />}{label}
    </button>
  );
}

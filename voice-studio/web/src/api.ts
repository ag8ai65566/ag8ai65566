// Thin client for the studio API (same origin; the dev server proxies /api).

export class ApiError extends Error {
  status: number;
  constructor(status: number, message: string) {
    super(message);
    this.status = status;
  }
}

async function request<T>(method: string, url: string, body?: unknown, retried = false): Promise<T> {
  const init: RequestInit = { method, headers: {} };
  if (body instanceof FormData) init.body = body;
  else if (body !== undefined) {
    init.body = JSON.stringify(body);
    (init.headers as Record<string, string>)["Content-Type"] = "application/json";
  }
  const r = await fetch(url, init);
  if (r.status === 401 && !retried) {
    // network mode: the studio was started with VSTUDIO_PASSWORD
    const pw = window.prompt("Voice Studio 密碼");
    if (pw) {
      document.cookie = `studio_pw=${encodeURIComponent(pw)}; path=/; SameSite=Strict; max-age=2592000`;
      return request<T>(method, url, body, true);
    }
  }
  if (!r.ok) {
    let msg = r.statusText;
    try {
      const j = await r.json();
      msg = typeof j.detail === "string" ? j.detail : JSON.stringify(j.detail ?? j);
    } catch {
      /* not json */
    }
    throw new ApiError(r.status, msg);
  }
  return (r.status === 204 ? undefined : await r.json()) as T;
}

export const api = {
  get: <T>(u: string) => request<T>("GET", u),
  post: <T>(u: string, b?: unknown) => request<T>("POST", u, b ?? {}),
  put: <T>(u: string, b?: unknown) => request<T>("PUT", u, b ?? {}),
  patch: <T>(u: string, b?: unknown) => request<T>("PATCH", u, b ?? {}),
  del: <T>(u: string) => request<T>("DELETE", u),
};

// --- types ----------------------------------------------------------------------------------------------------------

export type Consent = {
  agreed: boolean; signed_name: string; date: string; relationship: string; scope: string[];
  personal_only: boolean; document_note: string;
};
export type Voice = {
  id: string; name: string; kind: "self" | "other" | "designed"; languages: string[]; notes: string;
  consent: Consent | null; consent_doc: string | null; consent_ok: boolean;
  enrollment: { path: string; from: string }[]; enrolled: number;
  stats: Record<string, { count: number; minutes: number }>;
  emotions?: Record<string, number>;   // approved minutes per emotion label ("" = unlabelled)
};
export type Source = {
  id: string; filename: string; path: string; duration: number | null; status: string;
  voice_hint: string | null; language: string | null; segments: number; created_at: number; emotion?: string | null;
};
export type Segment = {
  id: string; source_id: string; voice_id: string | null; start: number; end: number; duration: number;
  text: string; text_alt: string; lang: string | null; asr_agree: number | null; spk_sim: number | null;
  snr: number | null; clip: number | null; cluster: number | null; score: number | null;
  status: "pending" | "approved" | "rejected"; flags: string[]; edited: number; emotion?: string | null;
};
export type AutoReview = {
  unsure: number; spot_left: number; spot_ok: number; spot_fail: number; auto_approved: number; auto_rejected: number;
  advice: string;
  job: (Pick<Job, "id" | "status" | "progress" | "message" | "created_at"> & {
    result: { message?: string; counts?: Record<string, number>; minutes?: Record<string, number>; profile?: string } | null;
  }) | null;
};
export type Dataset = {
  id: string; voice_id: string; name: string; n_items: number; hours: number; created_at: number;
  meta: { languages: string[]; n_train: number; n_val: number };
};
export type Job = {
  id: string; kind: string; status: "queued" | "running" | "done" | "failed" | "canceled";
  progress: number; message: string; created_at: number; result: Record<string, unknown>; log?: string;
  params?: Record<string, unknown>;
};
export type Preset = {
  id: string; label: string; description: string; gpu: string[]; params: Record<string, unknown>;
  min_hours: number; recommended: boolean;
};
export type EngineInfo = {
  id: string; name: string; summary: string; license: string; license_note: string; languages: string[];
  supports_tags: boolean; supports_instruct: boolean; needs_reference: boolean; infer_vram_gb: number;
  available: boolean; available_note: string; install: boolean; presets: Preset[];
};
export type TrainProgress = {
  step?: number; total?: number; loss?: number; val_loss?: number; phase?: string; elapsed_s?: number; wall_s?: number;
  epoch?: number; s_per_step?: number; gpu_name?: string; mode?: string;
};
export type Training = {
  id: string; voice_id: string; dataset_id: string; engine: string; status: string; gpu: string; pod_id: string | null;
  progress: TrainProgress; cost_estimate: number; created_at: number; finished_at: number | null;
  preset: { id: string; name?: string; params?: Record<string, unknown> };
  job: { status: string; progress: number; message: string } | null; job_id?: string; log?: string;
  note?: string; pod_state?: string | null; cost_per_hr?: number | null;
};
export type Plan = {
  engine: string; preset: string; gpu: string; usd_per_hour: number; data_hours: number; n_train: number;
  steps: number; estimate_hours: number; estimate_usd: number; estimate_basis: "measured" | "guess";
  max_hours: number; max_usd: number; disk_gb: number; ram_gb: number; warnings: string[];
  epochs_effective?: number | null; blocked?: string | null; params: Record<string, unknown>;
};
export type Orphan = { id: string; name: string; training: string; known: boolean; cost_per_hr?: number };
export type Reference = {
  id: string; file: string; text: string; lang: string; label: string; segment_id?: string; emotion?: string;
};
export type PhraseClip = { id: string; file: string; emotion: string; duration: number; from: string };
export type PhraseCheck = {
  output_id: string; match: number | null; sim: number | null; dur_ratio: number | null; at: number; checkpoint?: string | null;
};
export type Phrase = {
  id: string; voice_id: string; text: string; variants: string[]; lang: string | null; clips: PhraseClip[];
  checks: Record<string, PhraseCheck>; created_at: number;
  counts: { segments?: number; approved?: number; other_spellings?: number };
};
export type Checkpoint = { name: string; step: number; epoch: number; weights: boolean };
export type ConditionScore = { sim: number | null; agree: number | null; n: number; complete: boolean; seen_only?: boolean };
export type CheckpointScore = {
  name: string; sim: number | null; agree: number | null; summary: Record<string, ConditionScore>;
  clips: { line: number; kind: string; sim: number; agree: number | null; seen?: boolean }[];
};
export type SampleLine = { id: string; text: string; lang: string; audio: string; seen?: boolean };
export type Model = {
  id: string; voice_id: string; voice_name: string; engine: string; engine_name: string; name: string; path: string;
  created_at: number; training_id: string | null;
  meta: {
    mode?: string; checkpoint?: string | null; references?: Reference[]; dataset_id?: string; languages?: string[];
    notes?: string; preset?: { id: string; params?: Record<string, unknown> }; checkpoint_chosen_by_user?: boolean;
    sampling?: string;
  };
  metrics: {
    checkpoints?: CheckpointScore[]; recommended?: string | null; baseline_sim?: number | null; asr?: boolean;
    reason?: string; improved_over_base?: boolean | null; held_out_lines?: number; asr_failures?: number;
  };
  modes: string[]; checkpoints: Checkpoint[]; samples: { lines?: SampleLine[]; reference?: SampleLine | null };
  available: [boolean, string]; train_seconds?: number | null;
};
export type Output = {
  id: string; model_id: string | null; text: string; path: string; duration: number; created_at: number;
  favorite: number; batch: string | null;
  params: {
    language?: string; style?: string; seed?: number; engine?: string; scene?: boolean; mode?: string;
    ref?: string | null; checkpoint?: string | null; emotion?: string | null;
    phrases?: { phrase: string; clip: string; emotion: string }[];
  };
  score: { match?: number | null; heard?: string; best?: boolean; lines?: number };
};
export type CharacterPreset = {
  id: string; name: string; source: string; model_id: string | null;
  data: {
    character: string; language: "ja" | "en"; default_tags: string[];
    situations: { situation: string; tags: string[]; example: string }[];
    extra_tags: string[]; people: { with: string; tags: string[] }[]; sounds: string[];
    reading_guide: string; avoid: string; examples: { text: string; romaji?: string }[];
    cast_mode?: string; cast_ref_id?: string; cast_style?: string;
  };
};
export type GpuOffer = { id: string; label: string; vram: number; usd_h: number | null; availability: string | null };
export type SystemInfo = {
  version: string; python: string; os: string; disk_free_gb: number; data_dir: string;
  gpu: { available: boolean; name?: string; vram_gb?: number; free_gb?: number; note?: string };
  counts: Record<string, number>;
};

// emotion / delivery labels (same keys as vstudio/emotions.py); the first nine are keys 1–9 on the review page
export const EMOTIONS: [string, string][] = [
  ["neutral", "平靜"], ["happy", "開心"], ["excited", "興奮"], ["angry", "生氣"], ["sad", "難過"], ["soft", "小聲"],
  ["laughing", "笑著說"], ["surprised", "驚訝"], ["scared", "害怕"], ["whisper", "悄悄話"], ["teasing", "撒嬌"],
  ["narration", "念稿／旁白"],
];
export const EMOTION_LABEL: Record<string, string> = Object.fromEntries(EMOTIONS);

export const fmtMin = (m: number) => (m >= 60 ? `${(m / 60).toFixed(1)} 小時` : `${m.toFixed(1)} 分鐘`);
export const fmtTime = (ts: number) => new Date(ts * 1000).toLocaleString("zh-TW", { hour12: false });
export const LANGS: Record<string, string> = { ja: "日文", en: "英文", zh: "中文" };
export const MODES: Record<string, { label: string; hint: string }> = {
  plain: { label: "只用模型", hint: "訓練好的模型自己說。可以加風格提示，例如「安靜、慢慢說」。" },
  ref: { label: "參考音色", hint: "再給一段參考錄音帶音色；風格提示仍然有效。" },
  hifi: { label: "完整複製", hint: "參考錄音＋逐字稿，模型接著那段錄音說下去，口音、節奏、習慣最像本人。這個模式會忽略風格提示。" },
};
export const fmtDur = (s: number | null | undefined) => {
  if (s == null) return "—";
  const h = Math.floor(s / 3600), m = Math.floor((s % 3600) / 60);
  return h ? `${h} 小時 ${m} 分` : m ? `${m} 分` : `${Math.round(s)} 秒`;
};
export const fmtUsd = (x: number | null | undefined) => (x == null ? "—" : `US$${x.toFixed(2)}`);

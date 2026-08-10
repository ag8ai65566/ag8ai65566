#!/usr/bin/env node
// CANONICAL CALCULATION ENGINE. Every financial number in this system is produced here.
// Renderers format its output; they never recompute anything.
//
//   NODE_USE_ENV_PROXY=1 node gauges.mjs                 # readable panel
//   NODE_USE_ENV_PROXY=1 node gauges.mjs --json          # canonical structured output
//   NODE_USE_ENV_PROXY=1 node gauges.mjs --no-store      # skip the raw-response archive
//
// The one rule the whole file exists to keep:
//   「狠人認為這是危險訊號」與「歷史數據證明這是有效的危險訊號」永遠是兩件事。
// So every gauge separates four things and never blends them:
//   observed  — what the number is
//   empirical — where it sits in its own history
//   henren    — what HIS rule says about it
//   status    — how much any of that can be trusted
//
// Missing data is never neutral. A gauge with no usable reading reports NO_DECISION and
// is excluded from every count.

import { readFileSync, mkdirSync, writeFileSync } from 'node:fs';
import { createHash } from 'node:crypto';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { execSync } from 'node:child_process';
import {
  alignByEffectiveDate, yoyAtAnchor, alignQuarterly, percentileInWindow, priorObservation, shiftYears,
} from '../../../../lib/temporal.mjs';
import { aggregateCapex, HYPERSCALERS } from '../../../../lib/capex.mjs';
import { reconcileAll } from '../../../../lib/capex-reconcile.mjs';

export const CALCULATION_VERSION = '3.4.0';

const here = dirname(fileURLToPath(import.meta.url));
const repo = join(here, '..', '..', '..', '..');
const REGISTRY = JSON.parse(readFileSync(join(repo, 'config', 'data-sources.json'), 'utf8'));
const RUN_AT = new Date();
const STORE = !process.argv.includes('--no-store');

const UA = { 'User-Agent': 'ag8ai6@gmail.com market-research-tool' };
const r2 = (x, n = 2) => (Number.isFinite(x) ? Number(x.toFixed(n)) : null);
const dayDiff = (a, b) => Math.round((new Date(b) - new Date(a)) / 86400000);

let CODE_COMMIT = 'unknown';
try { CODE_COMMIT = execSync('git rev-parse --short HEAD', { cwd: repo }).toString().trim(); } catch {}

function archive(key, body) {
  const h = createHash('sha256').update(body).digest('hex').slice(0, 16);
  if (STORE) {
    const dir = join(repo, 'data', 'raw', RUN_AT.toISOString().slice(0, 10));
    mkdirSync(dir, { recursive: true });
    writeFileSync(join(dir, `${key}.raw`), body);
  }
  return h;
}

// ---------------------------------------------------------------- fetch

async function fredSeries(datasetId) {
  const ds = REGISTRY.datasets[datasetId];
  if (!ds) throw new Error(`dataset ${datasetId} not in registry`);
  const r = await fetch(REGISTRY.sources[ds.source_id].endpoint.replace('{series}', ds.series), { headers: UA });
  if (!r.ok) throw new Error(`HTTP ${r.status}`);
  const body = await r.text();
  const points = body.trim().split('\n').slice(1).map((l) => l.split(','))
    .map(([date, v]) => ({ date, value: Number(v) })).filter((p) => Number.isFinite(p.value));
  if (!points.length) throw new Error('empty series');
  return { datasetId, ds, points, raw_hash: archive(datasetId, body), retrieved_at: new Date().toISOString() };
}

// Cboe publishes the volatility complex itself, one session ahead of FRED's
// redistribution — a higher authority AND a fresher number, which is a rare combination.
async function cboeSeries(datasetId) {
  const ds = REGISTRY.datasets[datasetId];
  if (!ds) throw new Error(`dataset ${datasetId} not in registry`);
  const r = await fetch(REGISTRY.sources.cboe.endpoint.replace('{index}', ds.index), { headers: UA });
  if (!r.ok) throw new Error(`HTTP ${r.status}`);
  const body = await r.text();
  const points = body.trim().split('\n').slice(1).map((l) => l.split(','))
    .map(([d, , , , close]) => {
      const [m, dd, y] = d.trim().split('/');
      return { date: `${y}-${m}-${dd}`, value: Number(close) };
    })
    .filter((p) => Number.isFinite(p.value) && /^\d{4}-\d{2}-\d{2}$/.test(p.date));
  if (!points.length) throw new Error('empty series');
  return { datasetId, ds, points, raw_hash: archive(datasetId, body), retrieved_at: new Date().toISOString() };
}

async function equitySeries(symbol, range = '5y') {
  const ds = REGISTRY.datasets.EQUITY_DAILY;
  const r = await fetch(
    `${REGISTRY.sources[ds.source_id].endpoint.replace('{symbol}', encodeURIComponent(symbol))}?range=${range}&interval=1d`,
    { headers: UA });
  if (!r.ok) throw new Error(`HTTP ${r.status}`);
  const body = await r.text();
  const x = JSON.parse(body)?.chart?.result?.[0];
  if (!x) throw new Error('no chart result');
  const q = x.indicators?.quote?.[0] ?? {};
  const points = (x.timestamp ?? []).map((t, i) => ({
    date: new Date(t * 1000).toISOString().slice(0, 10), value: q.close?.[i],
  })).filter((p) => Number.isFinite(p.value));
  if (!points.length) throw new Error('empty series');
  return { datasetId: 'EQUITY_DAILY', ds, symbol, points,
    raw_hash: archive(`EQUITY_${symbol.replace(/[^\w-]/g, '_')}`, body), retrieved_at: new Date().toISOString() };
}

// ------------------------------------------------------- status + provenance

const AUTHORITY = { fred: 'OFFICIAL_AGGREGATOR', yahoo: 'UNOFFICIAL_FREE', sec_edgar: 'OFFICIAL_PRIMARY', cboe: 'OFFICIAL_PRIMARY', stooq: 'UNOFFICIAL_FREE' };
const AUTHORITY_RANK = { OFFICIAL_PRIMARY: 5, OFFICIAL_AGGREGATOR: 4, LICENSED: 3, MANUAL_PRIMARY: 3, MANUAL_SECONDARY: 2, UNOFFICIAL_FREE: 1, NO_AUTHORITATIVE_SOURCE: 0 };
/** A composite is only as authoritative as its weakest input. */
const weakestAuthority = (...levels) =>
  levels.reduce((w, l) => (AUTHORITY_RANK[l] < AUTHORITY_RANK[w] ? l : w), levels[0]);

/**
 * FRED labels quarterly and monthly observations by period START. Measuring age from the
 * label makes a freshly published quarter look ~90 days stale, which is how the Buffett
 * gauge ended up marked STALE while carrying the most recent Z.1 release there is.
 * Age is measured from the period END.
 */
function effectiveEnd(series) {
  const label = series.points.at(-1).date;
  if (series.ds.period_labeling !== 'start') return label;
  const d = new Date(`${label}T00:00:00Z`);
  const months = series.ds.expected_frequency === 'quarterly' ? 3 : 1;
  d.setUTCMonth(d.getUTCMonth() + months);
  d.setUTCDate(0);                                  // last day of the period
  return d.toISOString().slice(0, 10);
}

// US market holidays are not modelled; weekends are. Good enough to stop a weekend from
// masquerading as staleness, which is the error that actually matters here.
function tradingSessionsBetween(fromIso, to) {
  let n = 0;
  const d = new Date(`${fromIso}T00:00:00Z`);
  const end = new Date(Date.UTC(to.getUTCFullYear(), to.getUTCMonth(), to.getUTCDate()));
  while (d < end) {
    d.setUTCDate(d.getUTCDate() + 1);
    const dow = d.getUTCDay();
    if (dow !== 0 && dow !== 6) n += 1;
  }
  return n;
}

const PERIOD_DAYS = { 'business daily': 1, weekly: 7, monthly: 30, quarterly: 91 };

/**
 * Age a series in the unit it actually moves in. A daily price series is aged in TRADING
 * SESSIONS — on a Sunday, Friday's close is zero sessions old, not three days stale.
 * Everything also reports publication_lag_ratio = age / publication period, which turns
 * "132 days" into "1.4 publication cycles" and makes lag interpretable rather than alarming.
 */
function dataState(series) {
  const end = effectiveEnd(series);
  const { acceptable_age_days: sla, expected_publication_latency_days: lat = 0 } = series.ds;
  const calendarAge = dayDiff(end, RUN_AT);
  const sessionAge = series.ds.measure_age_in === 'trading_sessions'
    ? tradingSessionsBetween(end, RUN_AT) : null;
  const age = sessionAge ?? calendarAge;
  const period = PERIOD_DAYS[series.ds.expected_frequency] ?? 1;
  const common = {
    age_days: calendarAge,
    age_sessions: sessionAge,
    age_effective: age,
    age_unit: sessionAge === null ? 'calendar_days' : 'trading_sessions',
    acceptable_age_days: sla,
    publication_period_days: period,
    // Named for what it measures: distance from the publication cadence. It is NOT a
    // statement about how complete our economic information is — that is `information_scope`.
    publication_lag_ratio: Number((calendarAge / period).toFixed(2)),
    publication_lag_reading: `落後 ${Number((calendarAge / period).toFixed(2))} 個發布週期`
      + (sessionAge !== null ? `（交易日計：${sessionAge} 個 session）` : ''),
  };
  const limit = sessionAge === null ? sla : Math.max(3, Math.round(sla * 5 / 7));
  if (age <= lat + (sessionAge === null ? 1 : 0)) return { data_state: 'CURRENT', ...common };
  if (age <= limit) return { data_state: 'LAGGED_BY_DESIGN', ...common };
  if (age <= limit * 2) return { data_state: 'OVERDUE', ...common };
  return { data_state: 'STALE', ...common };
}

function provenance(series, transformation) {
  return {
    source_id: series.ds.source_id,
    source_authority: AUTHORITY[series.ds.source_id] ?? 'NO_AUTHORITATIVE_SOURCE',
    dataset: series.datasetId + (series.symbol ? `:${series.symbol}` : ''),
    effective_date: series.points.at(-1).date,
    retrieved_at: series.retrieved_at,
    raw_hash: series.raw_hash,
    transformation,
    calculation_version: CALCULATION_VERSION,
    code_commit: CODE_COMMIT,
    point_in_time_metadata: REGISTRY.sources[series.ds.source_id]?.point_in_time_capable === true ? 'PRESENT' : 'ABSENT',
    as_of_query: 'NOT_TESTED',
  };
}

/**
 * Display precision is not storage precision. `0.766` and `2.993` carry more resolution
 * than the underlying inference supports, and precision cues raise perceived confidence
 * independently of accuracy. The surface shows an economically meaningful figure; the
 * audit drawer keeps the exact one. Rounding is arithmetic, so it happens here — the
 * renderer is not allowed to do it.
 */
function displayPrecision(value, unit) {
  if (!Number.isFinite(value)) return { display: value, exact: value, rounded: false };
  const abs = Math.abs(value);
  let display;
  if (unit === '%' || String(unit).includes('個百分點')) display = Number(value.toFixed(abs >= 10 ? 0 : 1));
  else if (String(unit).includes('兆')) display = Number(value.toFixed(2));
  else if (String(unit).includes('十億')) display = Number(value.toFixed(abs >= 100 ? 0 : 1));
  else if (String(unit).includes('基點')) display = Number(value.toFixed(1));
  else if (abs >= 100) display = Number(value.toFixed(0));
  else if (abs >= 10) display = Number(value.toFixed(1));
  else display = Number(value.toFixed(2));
  return { display, exact: value, rounded: display !== value };
}

const rule = (value, bands) => bands.find(([, lo, hi]) => value >= lo && value < hi)?.[0] ?? bands.at(-1)[0];

/**
 * Assemble a gauge. `henren.status` is HIS rule firing — never presented as a validated
 * market signal. Anything not CURRENT/LAGGED_BY_DESIGN becomes NO_DECISION.
 */
function gauge(core, { prov, state, measurement = 'CHECKED', validation = 'UNTESTED', automation = 'AUTOMATED' }) {
  const usable = ['CURRENT', 'LAGGED_BY_DESIGN'].includes(state.data_state);
  if (core.observed && Number.isFinite(core.observed.value)) {
    const d = displayPrecision(core.observed.value, core.observed.unit);
    core.observed.display_value = d.display;
    core.observed.exact_value = d.exact;
    core.observed.display_rounded = d.rounded;
  }
  // Percentiles are inference-resolution figures; P95 is honest, P94.9 is not.
  for (const key of ['percentile_5y', 'percentile_3y', 'percentile_20y', 'change_4w_percentile_5y', 'level_percentile_5y']) {
    const p = core.empirical?.[key];
    if (p?.ok && Number.isFinite(p.value)) { p.display_value = Math.round(p.value); p.exact_value = p.value; }
  }
  return {
    ...core,
    status: {
      data_state: state.data_state,
      source_authority: core.source_authority_override ?? prov.source_authority,
      measurement_integrity: usable ? measurement : 'RAW',
      signal_validation: validation,
      automation_mode: automation,
    },
    age_days: state.age_days,
    acceptable_age_days: state.acceptable_age_days,
    decision: usable ? 'RULE_EVALUATED' : 'NO_DECISION',
    provenance: prov,
  };
}

const noDecision = (id, label, plain, data_state, note, extra = {}) => ({
  id, label, plain, observed: null, empirical: null, henren: null,
  status: { data_state, source_authority: extra.source_authority ?? 'NO_AUTHORITATIVE_SOURCE',
    measurement_integrity: 'RAW', signal_validation: 'UNTESTED',
    automation_mode: extra.automation_mode ?? 'NOT_WIRED' },
  decision: 'NO_DECISION', note, ...extra,
});

const attempt = async (id, label, fn) => {
  try { return await fn(); }
  catch (e) { return noDecision(id, label, '', 'SOURCE_FAILURE', `取得或計算失敗：${e.message ?? e}`); }
};

// ---------------------------------------------------------------- gauges

// Switch 1 — fuel. His rule names a RATE ("快速跌破"), so level alone under-implements it.
const fuel = await attempt('fuel', '開關一 · 燃料（銀行準備金）', async () => {
  const s = await fredSeries('WRESBAL');
  const tn = s.points.at(-1).value / 1e6;
  const levels = s.points.map((p) => ({ date: p.date, value: p.value / 1e6 }));
  const v4 = s.points.at(-5) ? (s.points.at(-1).value / s.points.at(-5).value - 1) * 100 : null;
  const v13 = s.points.at(-14) ? (s.points.at(-1).value / s.points.at(-14).value - 1) * 100 : null;
  const velSeries = s.points.map((p, i) => (i >= 4
    ? { date: p.date, value: (p.value / s.points[i - 4].value - 1) * 100 } : null)).filter(Boolean);
  const velPct = percentileInWindow(velSeries, v4, 5, { now: RUN_AT });
  // "Fast" is defined against this series' own history. An earlier build used a
  // hand-picked −3%/4wk, which fires around the 22nd percentile — not fast, just a
  // number someone chose. Bottom decile is the flag.
  const fastDrain = velPct.ok && velPct.value <= 10;
  const level = rule(tn, [['red', -Infinity, 2.5], ['yellow', 2.5, 2.8], ['green', 2.8, Infinity]]);

  return gauge({
    id: 'fuel', switch: 1, label: '開關一 · 燃料（銀行準備金）',
    plain: '銀行放在聯準會的閒錢。這桶油夠不夠，決定行情還能不能燒。',
    observed: { value: r2(tn, 3), unit: '兆美元', effective_date: s.points.at(-1).date },
    empirical: {
      level_percentile_5y: percentileInWindow(levels, tn, 5, { now: RUN_AT }),
      change_4w_pct: r2(v4), change_13w_pct: r2(v13),
      change_4w_percentile_5y: velPct,
      reading: velPct.ok
        ? `四週變化 ${r2(v4)}%，落在五年分布的 p${velPct.value}${fastDrain ? '（最快流失的一成）' : '，不構成快速流失'}`
        : '歷史樣本不足，無法判斷速度是否異常',
    },
    henren: {
      status: level === 'green' && fastDrain ? 'yellow' : level,
      thresholds: { green: '> 2.8 兆', yellow: '2.5–2.8 兆', red: '< 2.5 兆 → 無條件清倉' },
      quote: '每週一定要看 H.4.1 那個準備金餘額水位。站上 2.8 萬億美元上方，融漲邏輯是成立的。'
        + '如果沒有危機的情況下快速跌破了 2.5 萬億，那就無條件清倉，這條沒有任何討論的餘地。',
      note: fastDrain ? '水位在門檻上方，但速度落在最快的一成 —— 他的原句是「快速跌破」，速度本身是條件。' : null,
    },
  }, { prov: provenance(s, 'level in USD trillions; 4/13-week change; percentile vs 5y'), state: dataState(s) });
});

// Switch 2 — ignition. Yahoo stopped publishing closes for the whole term-structure family
// after 2026-07-17, so the original gauge divided across a three-week gap and printed green.
// FRED fixed that; Cboe now supersedes FRED, being the index publisher itself and running
// one session ahead of FRED's redistribution — higher authority and fresher at once.
const ignition = await attempt('ignition', '開關二 · 點火（期限結構代理）', async () => {
  const [vix, vxv] = await Promise.all([cboeSeries('CBOE_VIX'), cboeSeries('CBOE_VIX3M')]);
  const al = alignByEffectiveDate(vix.points, vxv.points);
  if (!al.ok) return noDecision('ignition', '開關二 · 點火（期限結構代理）', '', 'DATE_MISMATCH', al.reason);
  if (al.lag_days > 3) {
    return noDecision('ignition', '開關二 · 點火（期限結構代理）', '', 'DATE_MISMATCH',
      `VIX 與 3 個月 VIX 的最新日期相差 ${al.lag_days} 天，超過容忍值。`);
  }
  const byDate = new Map(vxv.points.map((p) => [p.date, p.value]));
  const ratios = vix.points.filter((p) => byDate.has(p.date))
    .map((p) => ({ date: p.date, value: p.value / byDate.get(p.date) }));
  const ratio = al.a.value / al.b.value;

  return gauge({
    id: 'ignition', switch: 2, label: '開關二 · 點火（期限結構代理）',
    plain: '市場覺得「現在」比「三個月後」更可怕嗎？怕近的＝恐慌還在；怕遠的＝恐慌已經退了。',
    observed: { value: r2(ratio, 3), unit: 'VIX ÷ 3個月VIX', effective_date: al.anchor,
      detail: { vix: r2(al.a.value), vix_3m: r2(al.b.value) } },
    empirical: {
      percentile_5y: percentileInWindow(ratios, ratio, 5, { now: RUN_AT }),
      reading: ratio < 1 ? '遠月波動率高於近月（Contango）＝ 市場沒有在為「馬上出事」定價'
        : '近月高於遠月（Backwardation）＝ 恐慌集中在眼前',
    },
    henren: {
      status: rule(ratio, [['green', -Infinity, 0.95], ['yellow', 0.95, 1.0], ['red', 1.0, Infinity]]),
      thresholds: { green: '< 0.95（Contango，恐慌退潮）', yellow: '0.95–1.00', red: '> 1.00（倒掛）' },
      quote: 'VIX 期限結構從倒掛回到正常，專業叫做 Contango，意思就是遠月的波動率重新高於近月，'
        + '它的意義就是恐慌退潮了。',
    },
    proxy: true,
    proxy_warning: '他的原始開關二是**選擇權 put/call 偏度極端倒掛＋現貨抗跌**。這裡用期限結構代理，'
      + '兩者相關但不等價：偏度量的是尾部定價的不對稱，期限結構量的是恐慌的時間分布，可能給出相反答案。'
      + '不過他在底部確認清單裡也直接點名了 Contango 這一項，所以此代理至少落在他自己的判準集合內。',
    proxy_replacement: 'Cboe SKEW 或 OPRA 等級選擇權資料（registry → cboe，尚未接線）',
  }, { prov: provenance(vix, 'Cboe VIX / VIX3M closes on a common session; percentile vs 5y'), state: dataState(vix) });
});

// Switch 3 — the escape bell. His rule names the QoQ growth rate ("環比增速的二階導"),
// so QoQ is the rule and YoY is only context. They are kept on separate tracks and YoY is
// never allowed to stand in for the rule.
//
// The QoQ leg depends on quarters recovered by differencing YTD cumulatives, and that
// arithmetic is now checked against issuers' own directly-tagged quarters. 64 of 65
// checkable derivations match to the dollar — but Meta tags no standalone quarters at all,
// so any aggregate containing Meta carries arithmetic nobody has verified. Under
// `transformation_validation: UNVERIFIED` the rule reports NO_DECISION rather than green.
const capex = await attempt('capex', '開關三 · 逃生鈴（雲廠商 capex 增速）', async () => {
  const agg = await aggregateCapex({ archive });
  const s = agg.series;
  if (s.length < 6) throw new Error(`only ${s.length} common quarters`);
  const last = s.at(-1), prev = s.at(-2);
  const recon = await reconcileAll(agg.issuers.map((i) => ({
    ticker: i.ticker, cik: HYPERSCALERS[i.ticker].cik, tag: i.tag })));

  const age = dayDiff(last.information_available_at, RUN_AT);
  const ds = REGISTRY.datasets.SEC_CAPEX;
  const state = age <= ds.acceptable_age_days
    ? { data_state: age <= ds.expected_publication_latency_days + 1 ? 'CURRENT' : 'LAGGED_BY_DESIGN',
      age_days: age, acceptable_age_days: ds.acceptable_age_days,
      publication_period_days: 91, publication_lag_ratio: r2(age / 91),
      publication_lag_reading: `落後 ${r2(age / 91)} 個發布週期` }
    : { data_state: age <= ds.acceptable_age_days * 2 ? 'OVERDUE' : 'STALE',
      age_days: age, acceptable_age_days: ds.acceptable_age_days,
      publication_period_days: 91, publication_lag_ratio: r2(age / 91) };

  // Did the quarter feeding QoQ contain any derived (unverifiable) component?
  const qoqDerivedIssuers = prev.parts.filter((p) => p.derived).map((p) => p.ticker);
  const qoqTainted = qoqDerivedIssuers.some((t) => recon.unverifiable_issuers.includes(t))
    || last.parts.filter((p) => p.derived).some((t) => recon.unverifiable_issuers.includes(t.ticker));
  const transformValidation = recon.verdict === 'RECONCILED' ? 'CHECKED'
    : qoqTainted ? 'UNVERIFIED' : 'PARTIALLY_CHECKED';

  const yoySeries = s.filter((x) => x.yoy_pct !== null);
  const yoyPeak = Math.max(...yoySeries.map((x) => x.yoy_pct));

  const core = {
    id: 'capex', switch: 3, label: '開關三 · 逃生鈴（雲廠商 capex 增速）',
    plain: '微軟、Google、Amazon、Meta 這四家買設備的錢，增加的速度有沒有開始變慢。'
      + '重點不是「還在花」，是「加速度」。',
    observed: {
      value: last.qoq_pct, unit: '% 環比', effective_date: last.period_end,
      detail: {
        total_bn: last.total_bn, yoy_pct: last.yoy_pct,
        prior_quarter: { period_end: prev.period_end, total_bn: prev.total_bn },
        by_issuer: last.parts.map((p) => ({ ticker: p.ticker, bn: r2(p.val / 1e9), derived_from_cumulative: p.derived })),
        information_available_at: last.information_available_at,
        coverage: agg.coverage,
      },
    },
    // YoY lives here — context, never the rule.
    empirical: {
      yoy_pct: last.yoy_pct,
      yoy_peak_in_series: yoyPeak,
      yoy_history: yoySeries.slice(-8).map((x) => ({ period_end: x.period_end, yoy_pct: x.yoy_pct, qoq_pct: x.qoq_pct })),
      measurement_integrity_yoy: 'CHECKED',
      reading: `年增 ${last.yoy_pct}%，是序列內最高（前高 ${yoyPeak}%）。`
        + '年增兩端都是直接申報的單季值，不經差分，所以這個數字本身是可信的 —— '
        + '但它不是他的規則。他要的是環比。',
      information_scope: 'REPORTED_ACTUALS_ONLY',
      interim_event_coverage: 'MISSING',
      coverage_note: '本格只涵蓋已申報的實際支出。法說會的下季指引沒有 XBRL tag，'
        + '未接線 —— 公司可能在季報之間就轉向，而這裡看不到。',
    },
    henren: {
      // The rule is QoQ. It reports its own status, and that status is gated below.
      status: null,
      rule_metric: 'QoQ',
      rule_value: last.qoq_pct,
      thresholds: { green: '環比增速持平或加速', red: '環比增速見頂回落 → 立刻平倉' },
      quote: '你要盯的是下游的雲廠商的資本開支的二階導數，也就是環比增速而不是同比增速。'
        + '如果資本開支的絕對額還在漲，但環比增速已經開始放緩甚至見頂回落的話，'
        + '哪怕當期的淨利潤再創新高也必須立刻平倉。',
      seasonality_treatment: 'NOT_ESTABLISHED',
      seasonality_note: '這四家的環比有明顯季節性（2025Q1 −0.6%、2026Q1 +9.37%），'
        + '但只有 8 季共同資料，不足以建立季節調整。因此環比的原始讀數無法可靠地區分'
        + '「季節性走弱」與「真的見頂回落」。',
    },
    transformation_validation: transformValidation,
    reconciliation: {
      verdict: recon.verdict, totals: recon.totals, by_issuer: recon.by_issuer,
      unverifiable_issuers: recon.unverifiable_issuers, note: recon.note,
      qoq_base_derived_issuers: qoqDerivedIssuers,
    },
    layers: {
      A_reported_cash_capex: 'AUTOMATED · SEC XBRL · 差分已對帳（64/65 分毫不差）',
      B_finance_leases: 'NOT_WIRED · 融資租賃不進現金 capex，本格系統性低估',
      C_management_guidance: 'NOT_WIRED · 下季指引無 XBRL tag',
    },
    source_authority_override: 'OFFICIAL_PRIMARY',
  };

  const prov = {
    source_id: 'sec_edgar', source_authority: 'OFFICIAL_PRIMARY', dataset: 'SEC_CAPEX',
    effective_date: last.period_end, retrieved_at: agg.issuers[0]?.retrieved_at,
    raw_hash: agg.issuers.map((i) => `${i.ticker}:${i.raw_hash}`).join(' '),
    transformation: 'YTD cumulative differenced to discrete quarters; summed across 4 issuers on common period ends; QoQ (rule) and YoY (context)',
    calculation_version: CALCULATION_VERSION, code_commit: CODE_COMMIT,
    point_in_time_metadata: 'PRESENT', as_of_query: 'NOT_TESTED',
    information_available_at: last.information_available_at,
  };

  const g = gauge(core, { prov, state, automation: 'HYBRID',
    measurement: transformValidation === 'CHECKED' ? 'CHECKED' : 'RAW' });

  // The rule cannot be evaluated on arithmetic nobody has checked.
  if (transformValidation !== 'CHECKED') {
    g.decision = 'NO_DECISION';
    g.status.data_state = 'RECONCILIATION_REQUIRED';
    g.henren.status = null;
    g.note = `環比是他的規則，但環比的比較基準（${prev.period_end}）含有無法驗證的差分還原值`
      + `（${recon.unverifiable_issuers.join('、')} 沒有可對照的直接申報單季值）。`
      + '在差分對帳完成以前，規則不評估 —— 年增很強不能代替「環比規則沒有觸發」。';
  }
  return g;
});

// --- liquidity alarms -------------------------------------------------------

const sofr = await attempt('sofr', 'SOFR − IORB 利差', async () => {
  const [s, i] = await Promise.all([fredSeries('SOFR'), fredSeries('IORB')]);
  const al = alignByEffectiveDate(s.points, i.points);
  if (!al.ok || al.lag_days > 5) {
    return noDecision('sofr', 'SOFR − IORB 利差', '', 'DATE_MISMATCH', al.reason ?? `相差 ${al.lag_days} 天`);
  }
  const byDate = new Map(i.points.map((p) => [p.date, p.value]));
  const spreads = s.points.filter((p) => byDate.has(p.date))
    .map((p) => ({ date: p.date, value: (p.value - byDate.get(p.date)) * 100 }));
  const bp = (al.a.value - al.b.value) * 100;
  return gauge({
    id: 'sofr', label: 'SOFR − IORB 利差',
    plain: '銀行之間借隔夜錢，要不要付比聯準會利率更高的價？要付，就代表錢在變緊。',
    observed: { value: r2(bp, 1), unit: '基點', effective_date: al.anchor,
      detail: { sofr: al.a.value, iorb: al.b.value } },
    empirical: { percentile_3y: percentileInWindow(spreads, bp, 3, { now: RUN_AT }),
      note: 'IORB 序列自 2021-07 起，分位數樣本有限。' },
    henren: {
      status: rule(bp, [['green', -Infinity, 1], ['yellow', 1, 3], ['red', 3, Infinity]]),
      thresholds: { green: '< 1 bp', yellow: '1–3 bp', red: '≥ 3 bp' },
      quote: 'SOFR-IRB 這個大家一定要每天都看，黃色預警是利差衝過三個基點，因為這是一個 95 分位的程度。',
    },
  }, { prov: provenance(s, 'SOFR minus IORB in bp on a common effective date; percentile vs 3y'), state: dataState(s) });
});

const tga = await attempt('tga', '財政部 TGA 餘額', async () => {
  const s = await fredSeries('WTREGEN');
  const bn = s.points.at(-1).value / 1000;
  const levels = s.points.map((p) => ({ date: p.date, value: p.value / 1000 }));
  return gauge({
    id: 'tga', label: '財政部 TGA 餘額',
    plain: '財政部的活存帳戶。它變胖是把市場上的錢吸走，變瘦是把錢放回市場。',
    observed: { value: r2(bn, 1), unit: '十億美元', effective_date: s.points.at(-1).date },
    empirical: { percentile_5y: percentileInWindow(levels, bn, 5, { now: RUN_AT }) },
    henren: {
      status: rule(bn, [['green', -Infinity, 950], ['yellow', 950, 1000], ['red', 1000, Infinity]]),
      thresholds: { green: '< 9,500 億', yellow: '9,500 億–1 兆', red: '≥ 1 兆' },
      quote: '財政部計劃在 2026 年的 7 月到 9 月淨市場化借款達到 6710 億美元，'
        + '並且到 9 月底 TGA 帳戶的餘額目標是 9500 億美元。所以從 7 月份開始流動性壓力會逐漸上升。',
    },
  }, { prov: provenance(s, 'level in USD bn; percentile vs 5y'), state: dataState(s) });
});

const rrp = await attempt('rrp', '隔夜逆回購緩衝', async () => {
  const s = await fredSeries('RRPONTSYD');
  const v = s.points.at(-1).value;
  return gauge({
    id: 'rrp', label: '隔夜逆回購緩衝',
    plain: '市場多餘現金的緩衝墊。墊子還厚，抽錢先抽它；墊子見底，就直接抽銀行準備金。',
    observed: { value: r2(v), unit: '十億美元', effective_date: s.points.at(-1).date },
    empirical: { percentile_5y: percentileInWindow(s.points, v, 5, { now: RUN_AT }),
      reading: v < 50 ? '緩衝實質見底 —— 財政部再抽錢會直接打到銀行準備金。' : '仍有緩衝。' },
    henren: { status: v < 50 ? 'yellow' : 'green',
      thresholds: { green: '> 500 億', yellow: '< 500 億（緩衝耗盡）' },
      quote: '（他未給明確數值門檻；此門檻為本系統依其論述設定，不是他的原話。）', threshold_is_ours: true },
  }, { prov: provenance(s, 'level in USD bn; percentile vs 5y'), state: dataState(s) });
});

const hyoas = await attempt('hyoas', '高收益債信用利差', async () => {
  const s = await fredSeries('BAMLH0A0HYM2');
  const v = s.points.at(-1).value;
  return gauge({
    id: 'hyoas', label: '高收益債信用利差 (HY OAS)',
    plain: '借錢給體質最差的公司，投資人要多收多少利息當風險費。這個數字跳起來＝信用真的出事。',
    observed: { value: r2(v), unit: '%', effective_date: s.points.at(-1).date },
    empirical: {
      percentile_5y: percentileInWindow(s.points, v, 5, { now: RUN_AT }),
      percentile_20y: percentileInWindow(s.points, v, 20, { now: RUN_AT }),
    },
    henren: { status: rule(v, [['green', -Infinity, 4], ['yellow', 4, 5], ['red', 5, Infinity]]),
      thresholds: { green: '< 4%', yellow: '4–5%', red: '≥ 5%' },
      quote: '（門檻為本系統設定；他強調的是「基本面沒變而價格崩了」時要看流動性與信用，未給數值。）',
      threshold_is_ours: true },
  }, { prov: provenance(s, 'OAS in percent; percentile vs 5y and 20y'), state: dataState(s) });
});

const nfci = await attempt('nfci', '金融條件指數 NFCI', async () => {
  const s = await fredSeries('NFCI');
  const v = s.points.at(-1).value;
  return gauge({
    id: 'nfci', label: '金融條件指數 (NFCI)',
    plain: '整體金融環境是鬆還是緊的總分。負的＝比平均寬鬆，正的＝比平均緊。',
    observed: { value: r2(v, 3), unit: '標準差', effective_date: s.points.at(-1).date },
    empirical: { percentile_5y: percentileInWindow(s.points, v, 5, { now: RUN_AT }) },
    henren: { status: rule(v, [['green', -Infinity, 0], ['yellow', 0, 0.2], ['red', 0.2, Infinity]]),
      thresholds: { green: '< 0（寬鬆）', yellow: '0–0.2', red: '≥ 0.2' },
      quote: '（門檻為本系統設定，非他的原話。）', threshold_is_ours: true },
  }, { prov: provenance(s, 'index level; percentile vs 5y'), state: dataState(s) });
});

// M2 vs Nasdaq. Anchored on the slower series; both legs use calendar-aware YoY.
const m2gap = await attempt('m2gap', 'M2 年增 − 那斯達克年增', async () => {
  const [m2, ndx] = await Promise.all([fredSeries('M2SL'), equitySeries('^IXIC', '5y')]);
  const al = alignByEffectiveDate(m2.points, ndx.points);
  if (!al.ok) return noDecision('m2gap', 'M2 年增 − 那斯達克年增', '', 'DATE_MISMATCH', al.reason);
  const m2Yoy = yoyAtAnchor(m2.points, al.anchor);
  const eqYoy = yoyAtAnchor(ndx.points, al.anchor, { maxBackfillDays: 10 });
  if (!m2Yoy.ok || !eqYoy.ok) {
    return noDecision('m2gap', 'M2 年增 − 那斯達克年增', '', 'INSUFFICIENT_HISTORY',
      `無法取得一年前對應觀測：${m2Yoy.reason ?? ''} ${eqYoy.reason ?? ''}`.trim());
  }
  const gap = m2Yoy.pct - eqYoy.pct;
  return gauge({
    id: 'm2gap', label: 'M2 年增 − 那斯達克年增（增負差）',
    plain: '市場上的錢一年多了幾 %，股市一年漲了幾 %。股市跑得比錢快太多，多出來的就是估值撐的。',
    observed: { value: r2(gap, 1), unit: '個百分點', effective_date: al.anchor,
      detail: { m2_yoy: r2(m2Yoy.pct), nasdaq_yoy: r2(eqYoy.pct),
        m2_legs: [m2Yoy.then.date, m2Yoy.now.date], nasdaq_legs: [eqYoy.then.date, eqYoy.now.date],
        anchor_set_by: al.anchor_set_by === 'A' ? 'M2（較慢）' : 'Nasdaq' } },
    empirical: { reading: `此讀數描述的是 ${al.anchor}，不是今天 —— M2 每月發布且落後約一個月，`
      + `錨點只能取到兩邊都有觀測的最新日期。` },
    henren: { status: rule(gap, [['red', -Infinity, -25], ['yellow', -25, -15], ['green', -15, Infinity]]),
      thresholds: { green: '> −15', yellow: '−15 至 −25', red: '≤ −25' },
      quote: '第五項 M2 同比增長 5.6% 而同期的納斯達克漲幅是 29.7%，增負差仍在負的 24.1%，這項也觸發了。',
      note: '他 6 月讀到 −24.1 判定觸發。' },
    source_authority_override: weakestAuthority('OFFICIAL_AGGREGATOR', 'UNOFFICIAL_FREE'),
    mixed_authority_note: 'M2 來自 FRED（OFFICIAL_AGGREGATOR），股價來自 Yahoo（UNOFFICIAL_FREE）；'
      + '複合指標取最低者，故本格標為 UNOFFICIAL_FREE。',
  }, { prov: provenance(m2, 'calendar-aware YoY on both legs at a common anchor'), state: dataState(m2) });
});

// Buffett ratio — both legs quarterly, joined on a common period instead of divided blind.
const buffett = await attempt('buffett', '巴菲特指標（總市值 ÷ GDP）', async () => {
  const [eq, gdp] = await Promise.all([fredSeries('NCBEILQ027S'), fredSeries('GDP')]);
  const eqBn = eq.points.map((p) => ({ date: p.date, value: p.value / 1000 }));
  const al = alignQuarterly(eqBn, gdp.points);
  if (!al.ok) {
    return noDecision('buffett', '巴菲特指標（總市值 ÷ GDP）',
      '整個股市值多少錢，跟整個國家一年生產多少錢比一比。', 'DATE_MISMATCH',
      `分子最新 ${al.latest_a}、分母最新 ${al.latest_b}，找不到同一季的配對。`);
  }
  const ratio = (al.a.value / al.b.value) * 100;
  const hist = eqBn.map((e) => {
    const g = gdp.points.find((x) => Math.abs(new Date(x.date) - new Date(e.date)) / 86400000 <= 45);
    return g ? { date: e.date, value: (e.value / g.value) * 100 } : null;
  }).filter(Boolean);
  const periodEnd = (() => { const d = new Date(`${al.period}T00:00:00Z`);
    d.setUTCMonth(d.getUTCMonth() + 3); d.setUTCDate(0); return d.toISOString().slice(0, 10); })();
  const age = dayDiff(periodEnd, RUN_AT);
  const ds = REGISTRY.datasets.NCBEILQ027S;
  return gauge({
    id: 'buffett', label: '巴菲特指標（總市值 ÷ GDP）',
    plain: '整個股市值多少錢，跟整個國家一年生產多少錢比一比。超過 100% 就算貴。',
    observed: { value: r2(ratio, 1), unit: '%', effective_date: al.period,
      detail: { equities_bn: r2(al.a.value), equities_date: al.a.date,
        gdp_bn: r2(al.b.value), gdp_date: al.b.date, offset_days: al.offset_days } },
    empirical: { percentile_20y: percentileInWindow(hist, ratio, 20, { now: RUN_AT }),
      reading: `兩邊都對齊在 ${al.period} 起始的那一季（截至 ${periodEnd}）。此讀數描述的是那一季，`
        + `距季末約 ${age} 天。Z.1 與 GDP 都是季度資料且發布本身就落後，這是設計上的落後不是失效。` },
    henren: { status: rule(ratio, [['green', -Infinity, 150], ['yellow', 150, 200], ['red', 200, Infinity]]),
      thresholds: { green: '< 150%', yellow: '150–200%', red: '≥ 200%' },
      quote: '第四項經典巴菲特指標 234%，也觸發。',
      note: '他讀到 234%；本系統分母定義不同（Z.1 企業股權 ÷ GDP），數值對不齊是預期內的。' },
  }, { prov: { ...provenance(eq, 'Z.1 corporate equities / GDP, joined on a common quarter'),
      effective_date: al.period, period_end: periodEnd },
    state: { data_state: age <= ds.acceptable_age_days ? 'LAGGED_BY_DESIGN' : 'STALE',
      age_days: age, acceptable_age_days: ds.acceptable_age_days } });
});

// Named for what it computes. It is a volatility ratio over a chosen basket — not crowding.
const aiVol = await attempt('ai-basket-rel-vol', 'AI 籃子相對波動（中位數）', async () => {
  const BASKET = ['MU', 'SNDK', 'PLTR', 'AMD', 'NVDA', 'AVGO', 'SMH'];
  const rvol = (pts, len = 21) => {
    if (pts.length < len + 1) return null;
    const w = pts.slice(-(len + 1));
    const rets = w.slice(1).map((p, i) => Math.log(p.value / w[i].value));
    const mean = rets.reduce((s, x) => s + x, 0) / rets.length;
    return Math.sqrt((rets.reduce((s, x) => s + (x - mean) ** 2, 0) / (rets.length - 1)) * 252) * 100;
  };
  const spx = await equitySeries('^GSPC', '1y');
  const spxVol = rvol(spx.points);
  const rows = [];
  for (const sym of BASKET) {
    try {
      const s = await equitySeries(sym, '1y');
      const v = rvol(s.points);
      rows.push({ symbol: sym, rvol21: r2(v), x_index: r2(v / spxVol, 1),
        last: r2(s.points.at(-1).value), as_of: s.points.at(-1).date });
    } catch (e) { rows.push({ symbol: sym, error: String(e.message ?? e) }); }
  }
  const ok = rows.filter((r) => Number.isFinite(r.x_index));
  if (ok.length < 4) {
    return noDecision('ai-basket-rel-vol', 'AI 籃子相對波動（中位數）', '', 'MISSING',
      `僅取得 ${ok.length}/${BASKET.length} 檔，樣本不足。`, { missing: rows.filter((r) => r.error) });
  }
  const sorted = ok.map((r) => r.x_index).sort((a, b) => a - b);
  const median = sorted[Math.floor(sorted.length / 2)];
  return gauge({
    id: 'ai-basket-rel-vol', label: 'AI 籃子相對波動（中位數）',
    plain: '這幾檔 AI 股最近上下跳的幅度，是大盤的幾倍。倍數越大，代表風險越集中在少數股票、不在指數。',
    observed: { value: r2(median, 1), unit: '倍', effective_date: spx.points.at(-1).date,
      detail: { spx_rvol21: r2(spxVol), max: r2(Math.max(...sorted), 1), min: r2(Math.min(...sorted), 1), basket: rows } },
    empirical: { reading: `大盤 21 日已實現波動 ${r2(spxVol)}%，籃子中位數是它的 ${r2(median, 1)} 倍。` },
    henren: { status: rule(median, [['green', -Infinity, 3], ['yellow', 3, 5], ['red', 5, Infinity]]),
      thresholds: { green: '< 3 倍', yellow: '3–5 倍', red: '≥ 5 倍' },
      quote: '（門檻為本系統設定。他談的是「拥挤就是一个金光闪闪的博弈矿」，未給數值門檻。）',
      threshold_is_ours: true },
    naming_note: '本格量的是**已實現波動比值**，不是擁擠度。真正的擁擠度需要部位資料 —— 集中度、廣度、'
      + '橫斷面相關性、成交量異常、選擇權部位、資金流。那些都尚未接線，所以此格不叫 Crowding。',
    selection_bias_note: `籃子是人工挑選的 ${BASKET.length} 檔 AI 相關標的，有主題偏誤；用中位數而非最大值，`
      + '避免單一極端值代表整個市場。它只描述這個籃子。',
  }, { prov: provenance(spx, '21-day annualised realised vol vs ^GSPC; median across a fixed basket'),
    state: dataState(spx) });
});

// --- manual gauges ----------------------------------------------------------

let manual = [];
try {
  const file = JSON.parse(readFileSync(join(here, '..', 'references', 'manual-gauges.json'), 'utf8'));
  manual = file.gauges.filter((g) => g.id !== 'capex-qoq').map((g) => {
    const contract = REGISTRY.manual_datasets[g.dataset_id] ?? {};
    const sla = contract.acceptable_age_days ?? 45;
    const age = g.asOf ? dayDiff(g.asOf, RUN_AT) : null;
    const state = g.value === null ? 'MISSING' : age > sla * 2 ? 'STALE' : age > sla ? 'OVERDUE' : 'LAGGED_BY_DESIGN';
    const usable = ['LAGGED_BY_DESIGN'].includes(state);
    return {
      id: g.id, label: g.label, plain: g.plain,
      observed: { value: g.value, unit: g.unit, effective_date: g.asOf },
      empirical: { reading: g.note },
      henren: { status: g.status, thresholds: g.thresholds, quote: g.quote ?? null },
      status: {
        data_state: state,
        source_authority: contract.authoritative_source_id?.startsWith('NO_') ? 'NO_AUTHORITATIVE_SOURCE' : 'MANUAL_SECONDARY',
        measurement_integrity: usable ? 'CHECKED' : 'RAW',
        signal_validation: 'UNTESTED',
        automation_mode: 'MANUAL_REVIEW_REQUIRED',
      },
      age_days: age, acceptable_age_days: sla,
      decision: usable ? 'RULE_EVALUATED' : 'NO_DECISION',
      note: usable ? null : `${g.asOf} 的讀數已過 SLA（${age} 天 > ${sla} 天），不參與規則評估。`,
      provenance: { source_id: 'manual', source_authority: 'MANUAL_SECONDARY', dataset: g.dataset_id,
        effective_date: g.asOf, retrieved_at: null, raw_hash: null,
        transformation: `hand-entered from ${g.source}`, calculation_version: CALCULATION_VERSION,
        code_commit: CODE_COMMIT, point_in_time_capable: false },
    };
  });
} catch (e) {
  manual = [noDecision('manual-load', 'manual gauges', '', 'SOURCE_FAILURE', String(e.message ?? e))];
}

// ---------------------------------------------------------------- assemble

const all = [fuel, ignition, capex, sofr, tga, rrp, hyoas, nfci, m2gap, buffett, aiVol, ...manual];
const evaluated = all.filter((g) => g.decision === 'RULE_EVALUATED');
const undecided = all.filter((g) => g.decision === 'NO_DECISION');

const ruleTally = evaluated.reduce((a, g) => { a[g.henren.status] = (a[g.henren.status] ?? 0) + 1; return a; }, {});
const dim = (k) => all.reduce((a, g) => { const v = g.status?.[k] ?? 'UNKNOWN'; a[v] = (a[v] ?? 0) + 1; return a; }, {});

const out = {
  schema_version: '3.0.0',
  calculation_version: CALCULATION_VERSION,
  code_commit: CODE_COMMIT,
  generated_at: RUN_AT.toISOString(),
  generated_at_et: RUN_AT.toLocaleString('en-US', { timeZone: 'America/New_York', timeZoneName: 'short' }),
  market_session: (() => {
    const et = new Date(RUN_AT.toLocaleString('en-US', { timeZone: 'America/New_York' }));
    const day = et.getDay(), mins = et.getHours() * 60 + et.getMinutes();
    const open = day >= 1 && day <= 5 && mins >= 570 && mins < 960;
    return { us_market: open ? 'OPEN' : 'CLOSED', timezone: 'America/New_York' };
  })(),
  frame: '基本面管方向、流動性管顛簸、擁擠管斷裂',
  // Two different questions, never merged: did HIS rule fire, and has anyone shown the
  // rule works? The first is a reading; the second is a research programme.
  henren_rule_tally: { ...ruleTally, evaluated: evaluated.length, no_decision: undecided.length, total: all.length },
  status_summary: {
    data_state: dim('data_state'),
    source_authority: dim('source_authority'),
    measurement_integrity: dim('measurement_integrity'),
    signal_validation: dim('signal_validation'),
    automation_mode: dim('automation_mode'),
  },
  no_composite_score: '本系統不輸出任何綜合分數、泡沫指數或 0–100 評分。沒有定義預測目標、沒有樣本外驗證的加權合成，是把不確定性藏起來，不是資訊。',
  // The five layers, stated as system state rather than buried in a disclaimer. This is
  // the most honest thing the page can say about itself: what has been established, and
  // what has not. It costs nothing in precision or traceability.
  maturity: [
    { layer: 'Data Provenance', state: 'ESTABLISHED',
      detail: '每個數字帶來源、權威等級、生效日、抓取時間、轉換、版本、commit、原始回應 hash。' },
    { layer: 'Calculation Integrity', state: 'ESTABLISHED',
      detail: `canonical engine 唯一計算，renderer 零金融運算，測試強制一致。calc v${CALCULATION_VERSION}。` },
    { layer: 'Measurement Validity', state: 'IN_PROGRESS',
      detail: 'capex 差分已對帳（65 筆可驗證中 64 筆分毫不差），但 META 無可對照值，環比因此不評估。'
        + '「抓到的概念是不是我們以為的那個概念」仍在建立中。' },
    { layer: 'Signal Validation', state: 'NOT_STARTED',
      detail: '0 / 16 格經過統計檢驗。所有門檻皆來自一位公開評論者，未回測、未樣本外驗證。' },
    { layer: 'Predictive Track Record', state: 'NOT_STARTED',
      detail: '前瞻假說帳本 3 筆，全部標記 LEGACY_EXPLORATORY，不計入績效。' },
  ],
  point_in_time: 'NOT_IMPLEMENTED',
  point_in_time_note: 'FRED 的預設端點只回傳最新修訂版，所以目前的讀數描述現在、不是可回測的歷史。'
    + '但這是「尚未實作」，不是「結構上不可能」—— ALFRED 提供 vintage 資料，FRED API 也有 '
    + 'series/vintagedates，回測路徑並沒有被資料架構永久封死。SEC 那條已帶 filed 時間戳，'
    + '但 as-of 查詢從未實際執行過（as_of_query: NOT_TESTED）。',
  gauges: all,
};

if (process.argv.includes('--json')) {
  console.log(JSON.stringify(out, null, 2));
} else {
  const icon = { green: '🟢', yellow: '🟡', red: '🔴' };
  const ds = { STALE: '⚪', OVERDUE: '🟤', MISSING: '⛔', NOT_WIRED: '⛔', SOURCE_FAILURE: '❌', DATE_MISMATCH: '⚠️' };
  console.log(`狠人判斷標誌 · ${out.generated_at_et} · 美股 ${out.market_session.us_market}`);
  console.log(`calc v${out.calculation_version} @ ${out.code_commit} · point-in-time: ${out.point_in_time}\n`);
  console.log('— HENREN RULE 已評估 —  (規則觸發，不是已驗證的市場訊號)');
  for (const g of evaluated) {
    const p = g.empirical?.percentile_5y ?? g.empirical?.percentile_3y ?? g.empirical?.percentile_20y;
    console.log(`${icon[g.henren.status]} ${(g.label ?? g.id).padEnd(28)}`
      + `${String(`${g.observed.value} ${g.observed.unit}`).padStart(18)}  ${g.observed.effective_date}`
      + `${p?.ok ? `  p${p.value}` : ''}  ${g.status.automation_mode}`);
  }
  console.log('\n— NO_DECISION —');
  for (const g of undecided) {
    console.log(`${ds[g.status.data_state] ?? '?'} ${(g.label ?? g.id).padEnd(28)} ${g.status.data_state}`);
    if (g.note) console.log(`     ${g.note}`);
  }
  console.log(`\nHenren 規則：${Object.entries(ruleTally).map(([k, v]) => `${icon[k] ?? k}${v}`).join('  ')}`
    + `　已評估 ${evaluated.length} / 未評估 ${undecided.length} / 共 ${all.length}`);
  console.log(`量測完整性：${JSON.stringify(out.status_summary.measurement_integrity)}`);
  console.log(`訊號驗證：  ${JSON.stringify(out.status_summary.signal_validation)}  ← 沒有任何一格經過統計驗證`);
  console.log(`自動化：    ${JSON.stringify(out.status_summary.automation_mode)}`);
}

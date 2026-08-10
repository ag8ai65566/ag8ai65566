#!/usr/bin/env node
// Score 一个狠人's judgment markers against registered data sources.
//
//   NODE_USE_ENV_PROXY=1 node gauges.mjs                 # readable panel
//   NODE_USE_ENV_PROXY=1 node gauges.mjs --json          # machine-readable
//   NODE_USE_ENV_PROXY=1 node gauges.mjs --no-store      # skip raw-response archive
//
// Contract (see docs/review-response.md):
//   * Every gauge names a dataset in config/data-sources.json. No registry entry, no value.
//   * Every gauge carries provenance: source, authority level, effective date, retrieval
//     time, age, and the hash of the raw response it was computed from.
//   * Missing or stale critical data yields NO_DECISION / STALE. It never becomes "neutral",
//     never becomes yellow, never becomes 0. Not-knowing is not a middling risk reading.
//   * Freshness is judged per dataset against its own SLA, not one global day count.
//   * Hardcoded thresholds are reported ALONGSIDE a rolling percentile of the same series,
//     because a fixed cut-off silently expires when market structure moves.
//
// Not yet true, and deliberately not papered over:
//   * FRED serves latest-vintage only, so nothing here is point-in-time. These readings
//     describe today. They are not a backtestable history.
//   * Thresholds are the author's asserted values. None has a measured false-positive rate.

import { readFileSync, mkdirSync, writeFileSync } from 'node:fs';
import { createHash } from 'node:crypto';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const repo = join(here, '..', '..', '..', '..');
const REGISTRY = JSON.parse(readFileSync(join(repo, 'config', 'data-sources.json'), 'utf8'));
const RUN_AT = new Date();
const STORE = !process.argv.includes('--no-store');

const UA = { 'User-Agent': 'Mozilla/5.0 (compatible; market-gauges/2.0)' };
const round = (x, n = 2) => (Number.isFinite(x) ? Number(x.toFixed(n)) : null);
const hash = (s) => createHash('sha256').update(s).digest('hex').slice(0, 16);
const dayDiff = (a, b) => Math.round((new Date(b) - new Date(a)) / 86400000);

function archive(key, body) {
  const h = hash(body);
  if (STORE) {
    const dir = join(repo, 'data', 'raw', RUN_AT.toISOString().slice(0, 10));
    mkdirSync(dir, { recursive: true });
    writeFileSync(join(dir, `${key}.raw`), body);
  }
  return h;
}

// ---------------------------------------------------------------- fetch layer

async function fredSeries(datasetId) {
  const ds = REGISTRY.datasets[datasetId];
  if (!ds) throw new Error(`dataset ${datasetId} not in registry`);
  const url = REGISTRY.sources[ds.source_id].endpoint.replace('{series}', ds.series);
  const r = await fetch(url, { headers: UA });
  if (!r.ok) throw new Error(`HTTP ${r.status}`);
  const body = await r.text();
  const points = body.trim().split('\n').slice(1)
    .map((l) => l.split(','))
    .map(([date, v]) => ({ date, value: Number(v) }))
    .filter((p) => Number.isFinite(p.value));
  if (!points.length) throw new Error('empty series');
  return { datasetId, ds, points, raw_hash: archive(datasetId, body), retrieved_at: new Date().toISOString() };
}

async function equitySeries(symbol, range = '5y') {
  const ds = REGISTRY.datasets.EQUITY_DAILY;
  const url = REGISTRY.sources[ds.source_id].endpoint.replace('{symbol}', encodeURIComponent(symbol))
    + `?range=${range}&interval=1d`;
  const r = await fetch(url, { headers: UA });
  if (!r.ok) throw new Error(`HTTP ${r.status}`);
  const body = await r.text();
  const x = JSON.parse(body)?.chart?.result?.[0];
  if (!x) throw new Error('no chart result');
  const q = x.indicators?.quote?.[0] ?? {};
  const points = (x.timestamp ?? [])
    .map((t, i) => ({ date: new Date(t * 1000).toISOString().slice(0, 10), value: q.close?.[i] }))
    .filter((p) => Number.isFinite(p.value));
  if (!points.length) throw new Error('empty series');
  return {
    datasetId: 'EQUITY_DAILY', ds, symbol, points, meta: x.meta,
    raw_hash: archive(`EQUITY_${symbol.replace(/[^\w-]/g, '_')}`, body),
    retrieved_at: new Date().toISOString(),
  };
}

// ------------------------------------------------------------ freshness + stats

// Judge each dataset against its own contract, never one global rule.
function freshness(series) {
  const last = series.points.at(-1);
  const age = dayDiff(last.date, RUN_AT);
  const { acceptable_age_days: sla, expected_publication_latency_days: latency = 0 } = series.ds;
  let status;
  if (age <= latency + 1) status = 'CURRENT_AS_PUBLISHED';
  else if (age <= sla) status = 'LAGGED_BY_DESIGN';
  else if (age <= sla * 2) status = 'OVERDUE';
  else status = 'STALE';
  return { effective_date: last.date, age_days: age, acceptable_age_days: sla, freshness_status: status };
}

function provenance(series, transformation, transformation_version = '2.0.0') {
  const src = REGISTRY.sources[series.ds.source_id];
  return {
    source_id: series.ds.source_id,
    authority_level: src.authority_level,
    dataset: series.datasetId + (series.symbol ? `:${series.symbol}` : ''),
    ...freshness(series),
    retrieved_at: series.retrieved_at,
    raw_hash: series.raw_hash,
    transformation,
    transformation_version,
    point_in_time_capable: src.point_in_time_capable === true,
  };
}

// Where does today's reading sit in its own history? A percentile survives a change in
// market structure; a hardcoded cut-off does not.
function percentile(points, value, years) {
  const cutoff = new Date(RUN_AT); cutoff.setFullYear(cutoff.getFullYear() - years);
  const window = points.filter((p) => new Date(p.date) >= cutoff).map((p) => p.value);
  const MIN_N = 30;
  if (window.length < MIN_N) return { status: 'INSUFFICIENT_HISTORY', n: window.length, required: MIN_N };
  const below = window.filter((v) => v < value).length;
  return { value: round((below / window.length) * 100, 1), window_years: years, n: window.length };
}

const change = (points, back) => {
  const last = points.at(-1), prior = points.at(-1 - back);
  return prior ? round(((last.value / prior.value) - 1) * 100, 2) : null;
};

// A gauge whose data failed or expired reports that, and is excluded from every count.
const undecided = (id, label, plain, status, note, extra = {}) =>
  ({ id, label, plain, value: null, status, decision: 'NO_DECISION', note, ...extra });

const band = (value, bands) => bands.find(([, lo, hi]) => value >= lo && value < hi)?.[0] ?? bands.at(-1)[0];

// Only a gauge whose data is inside its own SLA may show a colour.
function gate(g, prov) {
  if (prov.freshness_status === 'STALE') {
    return { ...g, status: 'STALE', decision: 'NO_DECISION',
      note: `${prov.dataset} 已過 SLA（${prov.age_days} 天 > ${prov.acceptable_age_days} 天），不參與計分。`,
      provenance: prov };
  }
  return { ...g, decision: 'SCORED', provenance: prov };
}

const attempt = async (id, fn) => {
  try { return await fn(); }
  catch (e) {
    return undecided(id, id, '', 'SOURCE_FAILURE', `取得或計算失敗：${e.message ?? e}`);
  }
};

// ---------------------------------------------------------------- the gauges

// Switch 1 — fuel. His thesis is a RATE ("快速跌破"), not only a level, so level alone
// under-implements it. Velocity and its own percentile are reported beside the level.
const fuel = await attempt('fuel', async () => {
  const s = await fredSeries('WRESBAL');
  const tn = s.points.at(-1).value / 1e6;
  const levels = s.points.map((p) => ({ ...p, value: p.value / 1e6 }));
  const v4 = change(s.points, 4), v13 = change(s.points, 13);
  const velocitySeries = s.points.map((p, i) => i >= 4
    ? { date: p.date, value: ((p.value / s.points[i - 4].value) - 1) * 100 } : null).filter(Boolean);

  const levelBand = band(tn, [['red', -Infinity, 2.5], ['yellow', 2.5, 2.8], ['green', 2.8, Infinity]]);
  // "Fast" has to be defined against this series' own history, not a number picked by hand.
  // A first pass used −3% per 4 weeks; that fires around the 22nd percentile, which is not
  // fast by any reasonable reading — it was an invented cut-off producing a false alarm.
  // Bottom decile of 4-week changes is the flag.
  const velPct = percentile(velocitySeries, v4, 5);
  const draining = Number.isFinite(velPct?.value) && velPct.value <= 10;
  const status = levelBand === 'green' && draining ? 'yellow' : levelBand;

  return gate({
    id: 'fuel', switch: 1, label: '開關一 · 燃料（準備金）',
    plain: '銀行放在聯準會的閒錢。這桶油夠不夠，決定行情還能不能燒。',
    value: round(tn, 3), unit: '兆美元',
    thresholds: { green: '> 2.8 兆', yellow: '2.5–2.8 兆，或四週內急跌 ≥3%', red: '< 2.5 兆 → 他的規則是無條件清倉' },
    velocity: { change_4w_pct: v4, change_13w_pct: v13, velocity_percentile_5y: velPct },
    level_percentile_5y: percentile(levels, tn, 5),
    status,
    interpretation_note: draining
      ? `水位仍在門檻上方，但四週變化 ${v4}% 落在五年最快流失的一成（p${velPct.value}）—— 他的原句是「快速跌破」，速度本身是訊號。`
      : `水位在門檻上方；四週變化 ${v4}% 落在 p${velPct?.value ?? '—'}，不構成「快速」流失。`,
  }, provenance(s, 'level in trillions; 4/13-week pct change; percentile vs 5y'));
});

// Switch 2 — ignition. His signal is an options SKEW inversion. This is the VIX term
// structure standing in for it. The two measure different things (tail-pricing asymmetry
// vs the time distribution of fear) and CAN disagree. Named as a proxy, everywhere.
const ignition = await attempt('ignition', async () => {
  const [vix, vix3m] = await Promise.all([equitySeries('^VIX', '5y'), equitySeries('^VIX3M', '5y')]);
  const a = vix.points.at(-1), b = vix3m.points.at(-1);
  if (a.date !== b.date) {
    return undecided('ignition', '開關二 · 點火（代理指標）', '',
      'DATE_MISMATCH', `^VIX 收在 ${a.date}、^VIX3M 收在 ${b.date}，不同交易日不可相除。`);
  }
  const byDate = new Map(vix3m.points.map((p) => [p.date, p.value]));
  const ratios = vix.points.filter((p) => byDate.has(p.date))
    .map((p) => ({ date: p.date, value: p.value / byDate.get(p.date) }));
  const ratio = a.value / b.value;

  return gate({
    id: 'ignition', switch: 2, label: '開關二 · 點火（代理指標）',
    plain: '市場覺得「現在」比「三個月後」更可怕嗎？怕近的＝恐慌還在；怕遠的＝恐慌退潮了。',
    value: round(ratio, 3), unit: 'VIX ÷ VIX3M',
    detail: { vix: round(a.value), vix3m: round(b.value), common_date: a.date },
    thresholds: { green: '< 0.95（Contango，恐慌退潮）', yellow: '0.95–1.00', red: '> 1.00（倒掛，恐慌未退）' },
    percentile_5y: percentile(ratios, ratio, 5),
    status: band(ratio, [['green', -Infinity, 0.95], ['yellow', 0.95, 1.0], ['red', 1.0, Infinity]]),
    proxy: true,
    proxy_warning: '他的原始訊號是選擇權 put/call 偏度極端倒掛＋現貨抗跌。期限結構與偏度相關但不等價，'
      + '可能出現期限結構已轉綠而偏度尚未觸發（或相反）的情況。此格不可視為他的開關二本身。',
    proxy_replacement: 'Cboe SKEW 或 OPRA 等級選擇權資料（config/data-sources.json → cboe，尚未接線）',
  }, provenance(vix, 'front/3-month VIX ratio on a common session date; percentile vs 5y'));
});

// September liquidity alarms he names by number.
const sofr = await attempt('sofr', async () => {
  const [s, i] = await Promise.all([fredSeries('SOFR'), fredSeries('IORB')]);
  if (s.points.at(-1).date !== i.points.at(-1).date) {
    // A 1-day offset is normal publication cadence, not an error — align on the common date.
    const common = i.points.map((p) => p.date).filter((d) => s.points.some((q) => q.date === d)).at(-1);
    if (!common) return undecided('sofr', 'SOFR − IORB 利差', '', 'DATE_MISMATCH', '兩序列無共同日期。');
    const sv = s.points.find((p) => p.date === common).value;
    const iv = i.points.find((p) => p.date === common).value;
    return finishSofr(s, i, sv, iv, common);
  }
  return finishSofr(s, i, s.points.at(-1).value, i.points.at(-1).value, s.points.at(-1).date);
});

function finishSofr(s, i, sv, iv, date) {
  const bp = (sv - iv) * 100;
  const byDate = new Map(i.points.map((p) => [p.date, p.value]));
  const spreads = s.points.filter((p) => byDate.has(p.date))
    .map((p) => ({ date: p.date, value: (p.value - byDate.get(p.date)) * 100 }));
  return gate({
    id: 'sofr', label: 'SOFR − IORB 利差',
    plain: '銀行之間借隔夜錢，要不要付比聯準會利率更高的價？要付，就代表錢在變緊。',
    value: round(bp, 1), unit: '基點 (bp)',
    detail: { sofr: sv, iorb: iv, common_date: date },
    thresholds: { green: '< 1 bp', yellow: '1–3 bp', red: '≥ 3 bp（他引用的 95 分位黃色警報）' },
    percentile_3y: percentile(spreads, bp, 3),
    percentile_note: 'IORB 序列自 2021-07 才開始，三年以上的分位數僅有有限樣本。',
    status: band(bp, [['green', -Infinity, 1], ['yellow', 1, 3], ['red', 3, Infinity]]),
  }, provenance(s, 'SOFR minus IORB in bp on a common date; percentile vs 3y'));
}

const tga = await attempt('tga', async () => {
  const s = await fredSeries('WTREGEN');
  const bn = s.points.at(-1).value / 1000;
  const levels = s.points.map((p) => ({ ...p, value: p.value / 1000 }));
  return gate({
    id: 'tga', label: '財政部 TGA 帳戶餘額',
    plain: '財政部的活存帳戶。它變胖是把市場上的錢吸走，變瘦是把錢放回市場。',
    value: round(bn, 1), unit: '十億美元',
    thresholds: { green: '< 9,500 億', yellow: '9,500 億 – 1 兆', red: '≥ 1 兆' },
    percentile_5y: percentile(levels, bn, 5),
    context: '財政部自訂 9 月底目標 9,500 億美元；7–9 月淨市場化借款計畫 6,710 億美元。'
      + '此為財政部公告，非本系統推算。',
    status: band(bn, [['green', -Infinity, 950], ['yellow', 950, 1000], ['red', 1000, Infinity]]),
  }, provenance(s, 'level in USD bn; percentile vs 5y'));
});

const rrp = await attempt('rrp', async () => {
  const s = await fredSeries('RRPONTSYD');
  const v = s.points.at(-1).value;
  return gate({
    id: 'rrp', label: '隔夜逆回購 (RRP) 緩衝',
    plain: '市場多餘現金的緩衝墊。墊子還厚，抽錢先抽它；墊子見底，就直接抽銀行準備金。',
    value: round(v, 2), unit: '十億美元',
    thresholds: { green: '> 500 億（仍有緩衝）', yellow: '< 500 億（緩衝耗盡，壓力直達準備金）' },
    percentile_5y: percentile(s.points, v, 5),
    status: v < 50 ? 'yellow' : 'green',
  }, provenance(s, 'level in USD bn; percentile vs 5y'));
});

const hyoas = await attempt('hyoas', async () => {
  const s = await fredSeries('BAMLH0A0HYM2');
  const v = s.points.at(-1).value;
  return gate({
    id: 'hyoas', label: '高收益債信用利差 (HY OAS)',
    plain: '借錢給體質最差的公司，投資人要多收多少利息當風險費。這個數字跳起來＝信用真的出事。',
    value: round(v, 2), unit: '%',
    thresholds: { green: '< 4%', yellow: '4–5%', red: '≥ 5%' },
    percentile_5y: percentile(s.points, v, 5),
    percentile_20y: percentile(s.points, v, 20),
    status: band(v, [['green', -Infinity, 4], ['yellow', 4, 5], ['red', 5, Infinity]]),
  }, provenance(s, 'OAS in percent; percentile vs 5y and 20y'));
});

const nfci = await attempt('nfci', async () => {
  const s = await fredSeries('NFCI');
  const v = s.points.at(-1).value;
  return gate({
    id: 'nfci', label: '芝加哥聯準會金融條件指數 (NFCI)',
    plain: '整體金融環境是鬆還是緊的總分。負的＝比平均寬鬆，正的＝比平均緊。',
    value: round(v, 3), unit: '標準差',
    thresholds: { green: '< 0（寬鬆）', yellow: '0–0.2', red: '≥ 0.2（明顯收緊）' },
    percentile_5y: percentile(s.points, v, 5),
    status: band(v, [['green', -Infinity, 0], ['yellow', 0, 0.2], ['red', 0.2, Infinity]]),
  }, provenance(s, 'index level; percentile vs 5y'));
});

// M2 vs Nasdaq. The prior version compared M2 as of June against equities as of August.
// Both legs now use the same anchor date t, and t is capped by the slower series.
const m2gap = await attempt('m2gap', async () => {
  const [m2, ndx] = await Promise.all([fredSeries('M2SL'), equitySeries('^IXIC', '5y')]);
  const anchor = m2.points.at(-1).date;                       // slower series sets t
  const equityAsOfT = ndx.points.filter((p) => p.date <= anchor).at(-1);
  if (!equityAsOfT) return undecided('m2gap', 'M2 年增 − 那斯達克年增', '', 'DATE_MISMATCH',
    `找不到 ${anchor} 或之前的股價收盤。`);

  // Calendar-aware year-ago lookup on both legs, not "minus 365 days".
  const yearBefore = (iso) => { const d = new Date(iso); d.setFullYear(d.getFullYear() - 1); return d.toISOString().slice(0, 10); };
  const m2Prior = m2.points.filter((p) => p.date <= yearBefore(anchor)).at(-1);
  const eqPrior = ndx.points.filter((p) => p.date <= yearBefore(equityAsOfT.date)).at(-1);
  if (!m2Prior || !eqPrior) return undecided('m2gap', 'M2 年增 − 那斯達克年增', '',
    'INSUFFICIENT_HISTORY', '缺少一年前的對應觀測值。');

  const m2Yoy = (m2.points.at(-1).value / m2Prior.value - 1) * 100;
  const eqYoy = (equityAsOfT.value / eqPrior.value - 1) * 100;
  const gap = m2Yoy - eqYoy;
  const prov = provenance(m2, 'calendar-aware YoY on both legs, anchored to the M2 effective date');

  return gate({
    id: 'm2gap', label: 'M2 年增 − 那斯達克年增（增負差）',
    plain: '市場上的錢一年多了幾 %，股市一年漲了幾 %。股市跑得比錢快太多，多出來的就是估值撐的。',
    value: round(gap, 1), unit: '個百分點',
    detail: {
      anchor_date: anchor, m2_yoy: round(m2Yoy, 2), nasdaq_yoy: round(eqYoy, 2),
      nasdaq_close_used: { date: equityAsOfT.date, value: round(equityAsOfT.value, 2) },
      m2_year_ago: m2Prior.date, nasdaq_year_ago: eqPrior.date,
    },
    thresholds: { green: '> −15', yellow: '−15 至 −25', red: '≤ −25' },
    status: band(gap, [['red', -Infinity, -25], ['yellow', -25, -15], ['green', -15, Infinity]]),
    alignment_note: `兩邊都錨定在 ${anchor}（由較慢的 M2 決定）。股價因此使用 ${equityAsOfT.date} 收盤，`
      + `而非最新收盤 —— 這個讀數描述的是 ${anchor}，不是今天。`,
    mixed_authority: '此格混合 OFFICIAL_AGGREGATOR（M2）與 UNOFFICIAL_FREE（股價），以較低者為準。',
  }, prov);
});

// Buffett ratio. Both legs are quarterly and lag by months; if they land in different
// quarters the gauge says so rather than dividing them anyway.
const buffett = await attempt('buffett', async () => {
  const [eq, gdp] = await Promise.all([fredSeries('NCBEILQ027S'), fredSeries('GDP')]);
  const e = eq.points.at(-1), g = gdp.points.at(-1);
  const prov = provenance(eq, 'corporate equities liability / GDP, both quarterly');
  const offset = Math.abs(dayDiff(e.date, g.date));
  if (offset > 45) {
    return { ...undecided('buffett', '巴菲特指標（總市值 ÷ GDP）',
      '整個股市值多少錢，跟整個國家一年生產多少錢比一比。', 'DATE_MISMATCH',
      `分子 ${e.date}、分母 ${g.date}，相差 ${offset} 天（超過一季）。兩者不同期，相除的結果沒有定義。`),
      detail: { equities_date: e.date, gdp_date: g.date, offset_days: offset },
      provenance: prov,
      would_have_been: round((e.value / 1000 / g.value) * 100, 1) };
  }
  const ratio = (e.value / 1000 / g.value) * 100;
  return gate({
    id: 'buffett', label: '巴菲特指標（總市值 ÷ GDP）',
    plain: '整個股市值多少錢，跟整個國家一年生產多少錢比一比。超過 100% 就算貴。',
    value: round(ratio, 1), unit: '%',
    thresholds: { green: '< 150%', yellow: '150–200%', red: '≥ 200%' },
    status: band(ratio, [['green', -Infinity, 150], ['yellow', 150, 200], ['red', 200, Infinity]]),
  }, prov);
});

// Renamed. The prior version took max(single-name vol / index vol) over a hand-picked AI
// basket and called the result "crowding". It is not crowding: the basket is selected, the
// max is an extreme-value statistic, and realised volatility is not positioning. It now
// says what it actually computes, and reports the whole distribution.
const aiVol = await attempt('ai-basket-rel-vol', async () => {
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
      rows.push({ symbol: sym, rvol21: round(v), x_index: round(v / spxVol, 1),
        last: round(s.points.at(-1).value, 2), as_of: s.points.at(-1).date });
    } catch (e) { rows.push({ symbol: sym, status: 'SOURCE_FAILURE', note: String(e.message ?? e) }); }
  }
  const ok = rows.filter((r) => Number.isFinite(r.x_index));
  if (ok.length < 4) return undecided('ai-basket-rel-vol', 'AI 籃子相對波動', '',
    'MISSING', `僅取得 ${ok.length}/${BASKET.length} 檔，樣本不足。`);
  const sorted = ok.map((r) => r.x_index).sort((a, b) => a - b);
  const median = sorted[Math.floor(sorted.length / 2)];

  return gate({
    id: 'ai-basket-rel-vol', label: 'AI 籃子相對波動（中位數）',
    plain: '這幾檔 AI 股最近上下跳的幅度，是大盤的幾倍。倍數越大，代表風險越集中在少數股票、不在指數。',
    value: round(median, 1), unit: '倍（中位數）',
    detail: { spx_rvol21: round(spxVol), basket: rows, max: round(Math.max(...sorted), 1), min: round(Math.min(...sorted), 1) },
    thresholds: { green: '< 3 倍', yellow: '3–5 倍', red: '≥ 5 倍' },
    status: band(median, [['green', -Infinity, 3], ['yellow', 3, 5], ['red', 5, Infinity]]),
    naming_note: '本格量的是「已實現波動比值」，不是擁擠度。真正的擁擠度需要部位資料 —— '
      + '集中度、廣度、橫斷面相關性、成交量異常、選擇權部位。這些都尚未接線，所以此格'
      + '不再命名為 Crowding，改為描述它實際計算的東西。',
    selection_bias_note: `籃子是人工挑選的 ${BASKET.length} 檔 AI 相關標的，本身就有主題偏誤；`
      + '改用中位數而非最大值，是為了避免單一極端值代表整個市場。它仍然只描述這個籃子。',
  }, provenance(spx, '21-day annualised realised vol vs ^GSPC; median across a fixed basket'));
});

// -------------------------------------------------- manual gauges (no free feed)

let manual = [];
try {
  const file = JSON.parse(readFileSync(join(here, '..', 'references', 'manual-gauges.json'), 'utf8'));
  manual = file.gauges.map((g) => {
    const contract = REGISTRY.manual_datasets[g.dataset_id] ?? {};
    const sla = contract.acceptable_age_days ?? g.refreshDays ?? 45;
    const age = g.asOf ? dayDiff(g.asOf, RUN_AT) : null;
    const stale = age === null || age > sla;
    return {
      ...g,
      status: g.value === null ? 'NOT_WIRED' : stale ? 'STALE' : g.status,
      decision: (g.value === null || stale) ? 'NO_DECISION' : 'SCORED',
      provenance: {
        source_id: 'manual',
        authority_level: contract.authoritative_source_id ?? 'NO_AUTHORITATIVE_SOURCE',
        dataset: g.dataset_id ?? g.id,
        effective_date: g.asOf ?? null, age_days: age, acceptable_age_days: sla,
        freshness_status: g.value === null ? 'MISSING' : stale ? 'STALE' : 'LAGGED_BY_DESIGN',
        retrieved_at: null, raw_hash: null,
        transformation: 'hand-entered from the cited publication',
        point_in_time_capable: false,
      },
      blocker: contract.blocker,
    };
  });
} catch (e) {
  manual = [undecided('manual-load', 'manual gauges', '', 'SOURCE_FAILURE', String(e.message ?? e))];
}

// ---------------------------------------------------------------- assemble

const auto = [fuel, ignition, sofr, tga, rrp, hyoas, nfci, m2gap, buffett, aiVol];
const all = [...auto, ...manual];
const scored = all.filter((g) => g.decision === 'SCORED');
const undecidedGauges = all.filter((g) => g.decision === 'NO_DECISION');

const tally = scored.reduce((a, g) => { a[g.status] = (a[g.status] ?? 0) + 1; return a; }, {});

const out = {
  schema_version: '2.0.0',
  generated_at: RUN_AT.toISOString(),
  generated_at_local: RUN_AT.toLocaleString('en-US', { timeZone: 'America/New_York', timeZoneName: 'short' }),
  frame: '基本面管方向、流動性管顛簸、擁擠管斷裂',
  // Counts cover SCORED gauges only. Anything undecided is listed separately and never
  // folded into a colour count — that is how "we don't know" becomes "looks fine".
  tally: { ...tally, scored: scored.length, no_decision: undecidedGauges.length, total: all.length },
  no_composite_score: 'This build emits no bubble score, no market score, and no 0-100 index. '
    + 'None has been validated against a defined target, so none is reported. Read the components.',
  point_in_time: false,
  point_in_time_note: 'FRED serves latest-vintage data only. These readings describe the present. '
    + 'They are not a point-in-time history and must not be used for backtesting.',
  gauges: all,
};

if (process.argv.includes('--json')) {
  console.log(JSON.stringify(out, null, 2));
} else {
  const icon = { green: '🟢', yellow: '🟡', red: '🔴', STALE: '⚪', NOT_WIRED: '⛔',
    SOURCE_FAILURE: '❌', DATE_MISMATCH: '⚠️', MISSING: '⛔', INSUFFICIENT_HISTORY: '⚠️' };
  console.log(`狠人判斷標誌 · ${out.generated_at_local}`);
  console.log(`資料來源見 config/data-sources.json · point-in-time: ${out.point_in_time}\n`);
  console.log('— 已計分 —');
  for (const g of scored) {
    const pc = g.percentile_5y?.value ?? g.percentile_3y?.value;
    console.log(`${icon[g.status] ?? '?'} ${(g.label ?? g.id).padEnd(30)}`
      + `${String(`${g.value} ${g.unit ?? ''}`).padStart(20)}  `
      + `${(g.provenance?.effective_date ?? '').padEnd(11)}`
      + `${pc !== undefined ? ` p${pc}` : ''}`);
  }
  console.log('\n— 未計分（NO_DECISION） —');
  for (const g of undecidedGauges) {
    console.log(`${icon[g.status] ?? '?'} ${(g.label ?? g.id).padEnd(30)} ${g.status}`);
    if (g.note) console.log(`     ${g.note}`);
    if (g.blocker) console.log(`     blocker: ${g.blocker}`);
  }
  console.log(`\n計分：${Object.entries(tally).map(([k, v]) => `${icon[k] ?? k}${v}`).join('  ')}`
    + `　（已計分 ${scored.length} / 未計分 ${undecidedGauges.length} / 共 ${all.length}）`);
  console.log('\n本版本不輸出任何綜合分數。未經驗證的加權合成不是資訊，是雜訊。');
}

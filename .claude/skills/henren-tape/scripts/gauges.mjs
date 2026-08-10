#!/usr/bin/env node
// Score 一个狠人's judgment markers against live data.
//
//   NODE_USE_ENV_PROXY=1 node gauges.mjs            # readable
//   NODE_USE_ENV_PROXY=1 node gauges.mjs --json     # for the dashboard
//
// Two sources: FRED (fredgraph.csv, no key needed) and Yahoo Finance.
//
// Some of his markers have no free live feed — FINRA margin debt, CBOE 0DTE share,
// index concentration, insider ratios, forward P/E, and cloud-capex QoQ. Those live in
// `references/manual-gauges.json` with the reading he last stated, its as-of date and
// where to refresh it. They are reported as STALE with their age, never silently
// treated as current. A gauge you cannot see is a gauge that is off.

import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const here = dirname(fileURLToPath(import.meta.url));
const UA = { 'User-Agent': 'Mozilla/5.0' };
const num = (x) => (Number.isFinite(x) ? x : null);
const round = (x, n = 2) => (Number.isFinite(x) ? Number(x.toFixed(n)) : null);

async function fred(seriesId) {
  const r = await fetch(`https://fred.stlouisfed.org/graph/fredgraph.csv?id=${seriesId}`, { headers: UA });
  if (!r.ok) throw new Error(`FRED ${seriesId}: HTTP ${r.status}`);
  const rows = (await r.text()).trim().split('\n').slice(1)
    .map((l) => l.split(','))
    .map(([date, v]) => ({ date, value: Number(v) }))
    .filter((p) => Number.isFinite(p.value));
  return rows;
}

async function yahoo(symbol, range = '2y') {
  const r = await fetch(
    `https://query1.finance.yahoo.com/v8/finance/chart/${encodeURIComponent(symbol)}?range=${range}&interval=1d`,
    { headers: UA });
  if (!r.ok) throw new Error(`Yahoo ${symbol}: HTTP ${r.status}`);
  const x = (await r.json())?.chart?.result?.[0];
  const q = x?.indicators?.quote?.[0] ?? {};
  return (x?.timestamp ?? [])
    .map((t, i) => ({ date: new Date(t * 1000).toISOString().slice(0, 10), value: q.close?.[i] }))
    .filter((p) => Number.isFinite(p.value));
}

const daysOld = (date) => Math.round((Date.now() - new Date(date).getTime()) / 86400000);
const settle = async (label, fn) => {
  try { return await fn(); } catch (e) { return { id: label, status: 'error', note: String(e.message ?? e) }; }
};

// --- Switch 1: fuel. His rule, verbatim: above $2.8T the melt-up holds; a fast break
// below $2.5T with no crisis is an unconditional exit. ---
const fuel = await settle('fuel', async () => {
  const s = await fred('WRESBAL');
  const last = s.at(-1);
  const tn = last.value / 1e6;                       // millions -> trillions
  const wow = (last.value - s.at(-2).value) / 1e6;
  const status = tn < 2.5 ? 'red' : tn < 2.8 ? 'yellow' : 'green';
  return {
    id: 'fuel', switch: 1, label: '開關一 · 燃料',
    plain: '銀行放在聯準會的閒錢。這桶油夠不夠，決定行情還能不能燒。',
    value: round(tn, 3), unit: '兆美元', asOf: last.date, changeWoW: round(wow, 3),
    thresholds: { green: '> 2.8 兆', yellow: '2.5–2.8 兆', red: '< 2.5 兆 → 他的規則是無條件清倉' },
    status, source: 'FRED WRESBAL (Fed H.4.1)',
  };
});

// --- Switch 2: ignition. He reads an extreme put/call skew flip plus spot refusing to
// fall. No free options-skew feed, so this is the VIX term structure standing in:
// backwardation (front > 3-month) is panic, contango is calm. He named the same
// contango flip as a bottom-confirmation signal. It is a proxy, and says so. ---
const ignition = await settle('ignition', async () => {
  const [vix, vix3m] = await Promise.all([yahoo('^VIX', '6mo'), yahoo('^VIX3M', '6mo')]);
  const v = vix.at(-1), v3 = vix3m.at(-1);
  const ratio = v.value / v3.value;
  const status = ratio > 1.0 ? 'red' : ratio > 0.95 ? 'yellow' : 'green';
  return {
    id: 'ignition', switch: 2, label: '開關二 · 點火（代理指標）',
    plain: '市場覺得「現在」比「三個月後」更可怕嗎？怕近的＝恐慌還在；怕遠的＝恐慌退潮了。',
    value: round(ratio, 3), unit: 'VIX / VIX3M', asOf: v.date,
    detail: { vix: round(v.value), vix3m: round(v3.value) },
    thresholds: { green: '< 0.95 期限結構正常（Contango），恐慌退潮', yellow: '0.95–1.00 拉平', red: '> 1.00 倒掛（Backwardation），還在恐慌' },
    status, proxy: true,
    source: 'Yahoo ^VIX / ^VIX3M — 他原話用的是選擇權偏度，這裡用期限結構代替',
  };
});

// --- Switch 3: escape. Cloud-capex QoQ growth rolling over. Manual by nature: it comes
// out of earnings decks four times a year. ---

// --- Liquidity alarms he names for September ---
const sofrSpread = await settle('sofr', async () => {
  const [sofr, iorb] = await Promise.all([fred('SOFR'), fred('IORB')]);
  const s = sofr.at(-1), i = iorb.at(-1);
  const bp = (s.value - i.value) * 100;
  const status = bp >= 3 ? 'red' : bp >= 1 ? 'yellow' : 'green';
  return {
    id: 'sofr', label: 'SOFR − IORB 利差',
    plain: '銀行之間借隔夜錢，要不要付比聯準會利率更高的價？要付，就代表錢在變緊。',
    value: round(bp, 1), unit: '基點 (bp)', asOf: s.date,
    detail: { sofr: s.value, iorb: i.value, sofrDate: s.date, iorbDate: i.date },
    thresholds: { green: '< 1 bp', yellow: '1–3 bp', red: '≥ 3 bp（他說的 95 分位黃色警報）' },
    status, source: 'FRED SOFR, IORB',
  };
});

const tga = await settle('tga', async () => {
  const s = await fred('WTREGEN');
  const last = s.at(-1);
  const bn = last.value / 1000;
  // He flags TGA climbing toward $1T as reserve-draining.
  const status = bn >= 1000 ? 'red' : bn >= 950 ? 'yellow' : 'green';
  return {
    id: 'tga', label: '財政部 TGA 帳戶餘額',
    plain: '財政部的活存帳戶。它變胖，是把市場上的錢吸走；它變瘦，是把錢放回市場。',
    value: round(bn, 1), unit: '十億美元', asOf: last.date,
    thresholds: { green: '< 9,500 億', yellow: '9,500 億–1 兆', red: '≥ 1 兆（他說的向 1 兆靠攏＝警報）' },
    note: '財政部自訂的 9 月底目標是 9,500 億美元，且 7–9 月淨市場化借款計畫 6,710 億美元。',
    status, source: 'FRED WTREGEN',
  };
});

const rrp = await settle('rrp', async () => {
  const s = await fred('RRPONTSYD');
  const last = s.at(-1);
  const status = last.value < 50 ? 'yellow' : 'green';
  return {
    id: 'rrp', label: '隔夜逆回購 (RRP) 餘額',
    plain: '市場多餘現金的緩衝墊。墊子還厚，抽錢先抽它；墊子見底，就直接抽銀行準備金。',
    value: round(last.value, 1), unit: '十億美元', asOf: last.date,
    thresholds: { green: '> 500 億（還有緩衝）', yellow: '< 500 億（緩衝用完，壓力直接打到準備金）' },
    status, source: 'FRED RRPONTSYD',
  };
});

const hyOas = await settle('hyoas', async () => {
  const s = await fred('BAMLH0A0HYM2');
  const last = s.at(-1);
  const y1 = s.filter((p) => daysOld(p.date) <= 365);
  const lo = Math.min(...y1.map((p) => p.value));
  const status = last.value >= 5 ? 'red' : last.value >= 4 ? 'yellow' : 'green';
  return {
    id: 'hyoas', label: '高收益債信用利差 (HY OAS)',
    plain: '借錢給體質最差的公司，投資人要多收多少利息當風險費。這個數字跳起來＝信用真的出事。',
    value: round(last.value, 2), unit: '%', asOf: last.date,
    detail: { low52w: round(lo, 2) },
    thresholds: { green: '< 4%', yellow: '4–5%', red: '≥ 5%（信用層真的動了）' },
    status, source: 'FRED BAMLH0A0HYM2 (ICE BofA)',
  };
});

const nfci = await settle('nfci', async () => {
  const s = await fred('NFCI');
  const last = s.at(-1);
  const status = last.value >= 0.2 ? 'red' : last.value >= 0 ? 'yellow' : 'green';
  return {
    id: 'nfci', label: '芝加哥聯準會金融條件指數 (NFCI)',
    plain: '整體金融環境是鬆還是緊的總分。負的＝比平均寬鬆，正的＝比平均緊。',
    value: round(last.value, 3), unit: '標準差', asOf: last.date,
    thresholds: { green: '< 0（寬鬆）', yellow: '0–0.2', red: '≥ 0.2（明顯收緊）' },
    status, source: 'FRED NFCI',
  };
});

// --- Bubble marker 5: M2 growth vs Nasdaq growth. His "增負差" — how far the index has
// run ahead of the money supply behind it. ---
const m2gap = await settle('m2gap', async () => {
  const [m2, ndx] = await Promise.all([fred('M2SL'), yahoo('^IXIC', '2y')]);
  const m2Last = m2.at(-1);
  const m2Yr = m2.find((p) => daysOld(p.date) <= 400 && daysOld(p.date) >= 350) ?? m2.at(-13);
  const m2Yoy = (m2Last.value / m2Yr.value - 1) * 100;
  const nLast = ndx.at(-1);
  const nYr = ndx.find((p) => daysOld(p.date) <= 372 && daysOld(p.date) >= 358) ?? ndx[0];
  const nYoy = (nLast.value / nYr.value - 1) * 100;
  const gap = m2Yoy - nYoy;
  const status = gap <= -25 ? 'red' : gap <= -15 ? 'yellow' : 'green';
  return {
    id: 'm2gap', label: 'M2 年增 − 那斯達克年增（增負差）',
    plain: '市場上的錢一年多了幾 %，股市一年漲了幾 %。股市跑得比錢快太多，多出來的就是估值撐的。',
    value: round(gap, 1), unit: '個百分點', asOf: `${m2Last.date} / ${nLast.date}`,
    detail: { m2Yoy: round(m2Yoy, 1), nasdaqYoy: round(nYoy, 1), m2AsOf: m2Last.date },
    thresholds: { green: '> −15', yellow: '−15 至 −25', red: '≤ −25（他 6 月讀到 −24.1 判定觸發）' },
    status, source: 'FRED M2SL + Yahoo ^IXIC',
  };
});

// --- Bubble marker 4: Buffett indicator, total market cap / GDP ---
const buffett = await settle('buffett', async () => {
  // FRED retired the Wilshire 5000 level series; the Fed's Z.1 corporate-equities
  // liability line is the standard stand-in numerator.
  const [equities, gdp] = await Promise.all([fred('NCBEILQ027S'), fred('GDP')]);
  const w = { date: equities.at(-1).date, value: equities.at(-1).value / 1000 }; // $mn -> $bn
  const g = gdp.at(-1);
  const ratio = (w.value / g.value) * 100;
  const status = ratio >= 200 ? 'red' : ratio >= 150 ? 'yellow' : 'green';
  return {
    id: 'buffett', label: '巴菲特指標（總市值 / GDP）',
    plain: '整個股市值多少錢，跟整個國家一年生產多少錢，比一比。超過 100% 就算貴。',
    value: round(ratio, 1), unit: '%', asOf: `${w.date} / GDP ${g.date}`,
    detail: { equitiesBn: round(w.value, 1), equitiesAsOf: w.date, gdp: round(g.value, 1), gdpAsOf: g.date },
    thresholds: { green: '< 150%', yellow: '150–200%', red: '≥ 200%（他讀到 234 判定觸發）' },
    status, source: 'FRED NCBEILQ027S / GDP',
    caveat: '兩邊都是季度資料且落後好幾個月，分子分母日期還不同步；他用的分母定義也和這裡不同（所以數字對不齊）。當方向指標看，別當精算值。',
  };
});

// --- Positioning / crowding, from prices ---
const crowding = await settle('crowding', async () => {
  const names = ['MU', 'PLTR', 'AMD', 'NVDA', 'SNDK', 'AVGO', 'SMH'];
  const rvol = (series, len = 21) => {
    if (series.length < len + 1) return null;
    const w = series.slice(-(len + 1));
    const rets = w.slice(1).map((p, i) => Math.log(p.value / w[i].value));
    const mean = rets.reduce((s, x) => s + x, 0) / rets.length;
    const varr = rets.reduce((s, x) => s + (x - mean) ** 2, 0) / (rets.length - 1);
    return Math.sqrt(varr * 252) * 100;
  };
  const spx = await yahoo('^GSPC', '6mo');
  const spxVol = rvol(spx);
  const rows = [];
  for (const n of names) {
    try {
      const s = await yahoo(n, '6mo');
      const v = rvol(s);
      rows.push({ symbol: n, rvol21: round(v), xIndex: round(v / spxVol, 1), last: round(s.at(-1).value, 2) });
    } catch { rows.push({ symbol: n, rvol21: null, xIndex: null }); }
  }
  const worst = Math.max(...rows.map((r) => r.xIndex ?? 0));
  const status = worst >= 5 ? 'red' : worst >= 3 ? 'yellow' : 'green';
  return {
    id: 'crowding', label: '擁擠度：個股波動 ÷ 大盤波動',
    plain: '大盤很平靜，但少數幾檔在瘋狂上下跳 — 差距越大，代表大家把錢越集中壓在那幾檔上，斷起來越痛。',
    value: round(worst, 1), unit: '倍', asOf: spx.at(-1).date,
    detail: { spxRvol21: round(spxVol), names: rows },
    thresholds: { green: '< 3 倍', yellow: '3–5 倍', red: '≥ 5 倍（風險集中在個股，不在指數）' },
    status, source: 'Yahoo — 21 日已實現波動率年化',
  };
});

// --- Manual gauges: no free live feed, carried with their age ---
let manual = [];
try {
  manual = JSON.parse(readFileSync(join(here, '..', 'references', 'manual-gauges.json'), 'utf8')).gauges;
  manual = manual.map((g) => {
    const age = daysOld(g.asOf);
    return { ...g, ageDays: age, stale: age > (g.refreshDays ?? 45), status: age > (g.refreshDays ?? 45) ? 'stale' : g.status };
  });
} catch (e) {
  manual = [{ id: 'manual-load-error', status: 'error', note: String(e.message ?? e) }];
}

const auto = [fuel, ignition, sofrSpread, tga, rrp, hyOas, nfci, m2gap, buffett, crowding];
const all = [...auto, ...manual];

const tally = all.reduce((acc, g) => { acc[g.status] = (acc[g.status] ?? 0) + 1; return acc; }, {});
const out = {
  generatedAt: new Date().toISOString(),
  frame: '基本面管方向、流動性管顛簸、擁擠管斷裂',
  tally,
  gauges: all,
};

if (process.argv.includes('--json')) {
  console.log(JSON.stringify(out, null, 2));
} else {
  const icon = { green: '🟢', yellow: '🟡', red: '🔴', stale: '⚪', error: '❌' };
  console.log(`狠人判斷標誌 · ${new Date().toISOString().slice(0, 10)}\n`);
  for (const g of all) {
    if (g.status === 'error') { console.log(`❌ ${g.id}: ${g.note}`); continue; }
    const v = g.value === undefined ? '' : `${g.value}${g.unit ? ' ' + g.unit : ''}`;
    console.log(`${icon[g.status] ?? '?'} ${(g.label ?? g.id).padEnd(30)} ${String(v).padStart(18)}   as of ${g.asOf}${g.stale ? `  (STALE ${g.ageDays}d)` : ''}`);
  }
  console.log(`\n計分：${Object.entries(tally).map(([k, v]) => `${icon[k] ?? k}${v}`).join('  ')}`);
}

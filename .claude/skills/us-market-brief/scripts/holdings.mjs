#!/usr/bin/env node
// Runs the Serenity Buffett gate on the portfolio using real filed fundamentals.
//
//   NODE_USE_ENV_PROXY=1 node holdings.mjs --json > data/holdings.json
//
// This is the file that moves serenity-method from NOT_EXECUTED to EXECUTED. Until SEC
// fundamentals were wired, every gate field was pinned at `unverified` — not because the
// companies were unproven, but because the system had no evidence to grade them with.
//
// The gate's own rule, kept intact: a field escalates above `unverified` ONLY with cited
// evidence, and a citation here means an accession number and a filing date. Fields that
// XBRL cannot speak to — moat, customer-replacement risk — stay `unverified`, and that is
// the correct answer rather than a gap to paper over.
//
// It produces no buy/sell call, no target price, and no position sizing.

import { readFileSync, mkdirSync, writeFileSync } from 'node:fs';
import { createHash } from 'node:crypto';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { execSync } from 'node:child_process';
import { fetchFundamentals, deriveMetrics } from '../../../../lib/fundamentals.mjs';

export const HOLDINGS_VERSION = '1.0.0';

const here = dirname(fileURLToPath(import.meta.url));
const repo = join(here, '..', '..', '..', '..');
const PORTFOLIO = JSON.parse(readFileSync(join(repo, 'config', 'portfolio.json'), 'utf8'));
const RUN_AT = new Date();
const UA = { 'User-Agent': 'ag8ai6@gmail.com market-research-tool' };

let CODE_COMMIT = 'unknown';
try { CODE_COMMIT = execSync('git rev-parse --short HEAD', { cwd: repo }).toString().trim(); } catch {}

const archive = (key, body) => {
  const h = createHash('sha256').update(body).digest('hex').slice(0, 16);
  const dir = join(repo, 'data', 'raw', RUN_AT.toISOString().slice(0, 10));
  mkdirSync(dir, { recursive: true });
  writeFileSync(join(dir, `${key}.raw`), body);
  return h;
};

const r2 = (x, n = 2) => (Number.isFinite(x) ? Number(x.toFixed(n)) : null);
const bn = (x) => (Number.isFinite(x) ? Number((x / 1e9).toFixed(2)) : null);

async function priceHistory(symbol) {
  const r = await fetch(
    `https://query1.finance.yahoo.com/v8/finance/chart/${encodeURIComponent(symbol)}?range=2y&interval=1d`,
    { headers: UA });
  if (!r.ok) throw new Error(`HTTP ${r.status}`);
  const body = await r.text();
  const x = JSON.parse(body)?.chart?.result?.[0];
  const q = x?.indicators?.quote?.[0] ?? {};
  const points = (x?.timestamp ?? []).map((t, i) => ({
    date: new Date(t * 1000).toISOString().slice(0, 10), value: q.close?.[i],
  })).filter((p) => Number.isFinite(p.value));
  return { points, raw_hash: archive(`EQUITY_${symbol}_2y`, body) };
}

function priceFacts(points) {
  const last = points.at(-1);
  const closes = points.map((p) => p.value);
  const hi = Math.max(...closes);
  const ma = (n) => (points.length >= n ? points.slice(-n).reduce((s, p) => s + p.value, 0) / n : null);
  const back = (n) => points.at(-1 - n)?.value ?? null;
  const pct = (a, b) => (Number.isFinite(a) && Number.isFinite(b) ? r2((a / b - 1) * 100) : null);
  const rvol = (n = 21) => {
    if (points.length < n + 1) return null;
    const w = points.slice(-(n + 1));
    const rets = w.slice(1).map((p, i) => Math.log(p.value / w[i].value));
    const mean = rets.reduce((s, x) => s + x, 0) / rets.length;
    return r2(Math.sqrt((rets.reduce((s, x) => s + (x - mean) ** 2, 0) / (rets.length - 1)) * 252) * 100);
  };
  return {
    as_of: last.date, close: r2(last.value),
    from_2y_high_pct: pct(last.value, hi), high_2y: r2(hi),
    high_2y_date: points.find((p) => p.value === hi)?.date,
    vs_50dma_pct: pct(last.value, ma(50)), vs_200dma_pct: pct(last.value, ma(200)),
    m1_pct: pct(last.value, back(21)), m3_pct: pct(last.value, back(63)),
    rvol21_pct: rvol(),
  };
}

/**
 * The gate. Every escalation carries the accession it rests on; anything XBRL cannot
 * answer stays `unverified` by design, not by omission.
 */
function buffettGate(m) {
  const cite = (k) => {
    const s = m.sources[k];
    return s ? `${s.form} ${s.accession}（期間 ${s.period}，申報 ${s.filed}）` : null;
  };
  const gate = {};

  // Profitability — the one field filed numbers CAN settle.
  const haveProfit = m.revenue_usd !== null && m.net_income_usd !== null;
  const growing = (m.revenue_yoy_pct ?? -1) > 0;
  const cashPositive = (m.free_cash_flow_usd ?? -1) > 0;
  // One quarter of positive numbers supports a claim about THAT quarter. It does not
  // establish a track record, and `proven` — the framework's own word — reads as though it
  // does. The framework label is preserved for fidelity but never shown on its own.
  const blocked = new Set(m.plausibility?.blocks_metrics ?? []);
  const revBlocked = blocked.has('revenue_usd') || blocked.has('net_income_usd');
  gate.profitability = haveProfit && growing && cashPositive && !revBlocked
    ? { value: 'SUPPORTED', scope: 'CURRENT_PERIOD', framework_label: 'proven',
      period: m.period_end,
      evidence: ['revenue', 'net_income', 'free_cash_flow'],
      evidence_detail: [`營收 $${bn(m.revenue_usd)}B、年增 ${m.revenue_yoy_pct}%`,
        m.gross_margin_pct !== null ? `毛利率 ${m.gross_margin_pct}%` : null,
        `自由現金流 $${bn(m.free_cash_flow_usd)}B（營運現金流 − capex，同一季）`].filter(Boolean),
      missing: m.gross_margin_pct === null ? ['gross_profit'] : [],
      coverage: m.gross_margin_pct === null ? 'PARTIAL' : 'COMPLETE',
      citations: [cite('revenue'), cite('netIncome'), cite('operatingCashFlow')].filter(Boolean),
      scope_note: '只證明最新一期的獲利與現金流為正，不證明長期獲利紀錄。'
        + '要談 track record 需要連續數年的資料，本管線目前只讀最新季度。' }
    : { value: 'unverified',
      reason: revBlocked ? '損益相關欄位被 STRUCTURAL_ERROR 封鎖。' : '缺少營收／獲利／現金流其一，或成長為負。' };

  // Everything below needs qualitative evidence XBRL does not contain.
  gate.moat = { value: 'unverified',
    reason: '護城河需要的是認證週期、轉換成本、設計導入、第二來源可得性等證據 —— '
      + 'XBRL 財報數字無法回答。高毛利率是結果，不是護城河本身，'
      + '記憶體產業歷史上就是高毛利與虧損交替的週期股。',
    what_would_settle_it: ['客戶的 10-K 是否揭露單一來源依賴', '認證／設計導入的合約期限',
      '產能擴張的前置時間', '競爭對手量產時程'] };
  gate.customer_replacement_risk = { value: 'unverified',
    reason: '需要客戶集中度揭露與第二來源狀況；本管線尚未抓取客戶集中度段落。',
    what_would_settle_it: ['10-K 的客戶集中度揭露', '大客戶自製化的公開跡象'] };
  gate.capital_allocation = m.capex_usd !== null && m.operating_cash_flow_usd !== null
    ? { value: 'observed_not_judged',
      evidence: [`本季 capex $${bn(m.capex_usd)}B，佔營運現金流 ${r2((m.capex_usd / m.operating_cash_flow_usd) * 100)}%`],
      note: '這是事實觀測，不是品質判斷。判斷需要多年期的投入報酬紀錄。' }
    : { value: 'unverified' };

  gate.is_buffett_quality = { value: 'not_yet',
    reason: '需要護城河、賺錢能力、資本配置三項同時高於 unverified。目前只有賺錢能力可判定。' };
  gate.conclusion = { value: '研究地图',
    reason: 'Serenity 方法要求四個條件同時成立才升級：客戶非有不可、供給無法快速增加、'
      + '公司已認證／設計導入、且相對於機會而言便宜。前三項本管線尚無證據，第四項需要估值工作。'
      + '要到「可投资结论」，缺的是質性證據與估值，不是價格動能。' };
  return gate;
}

const rows = [];
for (const h of PORTFOLIO.holdings) {
  const entry = { ...h, errors: [] };
  try {
    const f = await fetchFundamentals(h.ticker, h.cik, { archive });
    entry.fundamentals = deriveMetrics(f);
    // Pre-format the unit conversions here. The renderer is forbidden from doing arithmetic,
    // and `/ 1e9` is arithmetic — the integrity test caught exactly this.
    for (const k of ['revenue_usd', 'net_income_usd', 'operating_cash_flow_usd', 'capex_usd',
      'free_cash_flow_usd', 'equity_usd', 'assets_usd']) {
      entry.fundamentals[k.replace('_usd', '_bn')] = bn(entry.fundamentals[k]);
    }
    entry.fundamentals_age_days = entry.fundamentals.information_available_at
      ? Math.round((RUN_AT - new Date(entry.fundamentals.information_available_at)) / 86400000) : null;
    entry.serenity_gate = buffettGate(entry.fundamentals);
  } catch (e) { entry.errors.push(`fundamentals: ${e.message ?? e}`); }
  try {
    const p = await priceHistory(h.ticker);
    entry.price = priceFacts(p.points);
    entry.price_series = p.points.slice(-260);
    entry.price_raw_hash = p.raw_hash;
  } catch (e) { entry.errors.push(`price: ${e.message ?? e}`); }
  rows.push(entry);
}

// Concentration is judged on the BROAD sector. Grading it on the niche label defeats the
// check: "DRAM" and "NAND" read as two categories while trading as one — same buyers, same
// capex cycle, same drawdown. An over-specific taxonomy manufactures false diversification.
const sectors = [...new Set(rows.map((r) => r.sector))];
const niches = [...new Set(rows.map((r) => r.niche ?? r.sector))];
// Do the prices agree with the labels? Correlation of daily returns settles it.
const corr = (() => {
  const withPx = rows.filter((r) => r.price_series?.length);
  if (withPx.length < 2) return null;
  const [a, b] = withPx;
  const map = new Map(b.price_series.map((p) => [p.date, p.value]));
  const pairs = a.price_series.filter((p) => map.has(p.date));
  if (pairs.length < 60) return null;
  const ra = [], rb = [];
  for (let i = 1; i < pairs.length; i++) {
    ra.push(Math.log(pairs[i].value / pairs[i - 1].value));
    rb.push(Math.log(map.get(pairs[i].date) / map.get(pairs[i - 1].date)));
  }
  const mean = (x) => x.reduce((s, v) => s + v, 0) / x.length;
  const ma = mean(ra), mb = mean(rb);
  const cov = ra.reduce((s, v, i) => s + (v - ma) * (rb[i] - mb), 0);
  const va = Math.sqrt(ra.reduce((s, v) => s + (v - ma) ** 2, 0));
  const vb = Math.sqrt(rb.reduce((s, v) => s + (v - mb) ** 2, 0));
  return { pair: [a.ticker, b.ticker], value: r2(cov / (va * vb), 3), n_days: ra.length };
})();
const concentration = {
  holdings: rows.length,
  distinct_sectors: sectors.length,
  distinct_niches: niches.length,
  same_sector: sectors.length === 1,
  daily_return_correlation: corr,
  reading: sectors.length === 1
    ? `全部 ${rows.length} 檔都在「${sectors[0]}」`
      + (niches.length > 1 ? `（細分為 ${niches.join('、')}，但那是同一個因子）` : '')
      + '，這是一個因子，不是一個組合。'
    : `分布在 ${sectors.length} 個寬分類。`,
  correlation_reading: corr
    ? `${corr.pair.join(' 與 ')} 的日報酬相關係數 ${corr.value}（${corr.n_days} 個交易日）。`
      + (corr.value > 0.7 ? '價格證實它們是同一筆交易，標籤上的細分沒有帶來分散。' : '相關性中等以下。')
    : '樣本不足，無法計算相關係數。',
  note: '本系統不做部位建議，也不知道你的部位大小。這裡只陳述暴露事實。',
};

for (const r of rows) delete r.price_series;   // used for correlation only, not an output
const out = {
  schema_version: HOLDINGS_VERSION,
  generated_at: RUN_AT.toISOString(),
  generated_at_et: RUN_AT.toLocaleString('en-US', { timeZone: 'America/New_York', timeZoneName: 'short' }),
  code_commit: CODE_COMMIT,
  lens_status: {
    'serenity-method': rows.some((r) => r.serenity_gate) ? 'EXECUTED' : 'NOT_EXECUTED',
    'serenity-bottleneck-hunter': 'NOT_EXECUTED',
    'equity-research': 'NOT_EXECUTED',
  },
  guardrail: '本檔不輸出買賣訊號、目標價或部位建議。所有品質欄位遵守 serenity-method 的規則：'
    + '沒有引用證據就維持 unverified。',
  concentration,
  holdings: rows,
};

if (process.argv.includes('--json')) {
  console.log(JSON.stringify(out, null, 2));
} else {
  for (const r of rows) {
    const f = r.fundamentals, p = r.price;
    console.log(`\n### ${r.ticker} · ${r.name}`);
    if (r.errors.length) console.log(`  ⚠️ ${r.errors.join(' | ')}`);
    if (f) {
      console.log(`  財報期間 ${f.period_end}　申報於 ${f.information_available_at}（${r.fundamentals_age_days} 天前）`);
      console.log(`  營收 $${bn(f.revenue_usd)}B (年增 ${f.revenue_yoy_pct}%)　毛利率 ${f.gross_margin_pct ?? '—'}%　`
        + `淨利率 ${f.net_margin_pct}%　FCF $${bn(f.free_cash_flow_usd)}B`);
      if (f.plausibility.level !== 'PASS') {
        console.log(`  合理性: ${f.plausibility.level}`);
        for (const x of [...f.plausibility.structural, ...f.plausibility.outliers])
          console.log(`     ${x.check}: ${x.issue}${x.advisory_only ? ' [僅提醒，不封鎖]' : ' [封鎖]'}`);
      }
    }
    if (p) console.log(`  股價 ${p.close}（${p.as_of}）　距兩年高點 ${p.from_2y_high_pct}%　`
      + `vs 50日線 ${p.vs_50dma_pct}%　21日波動 ${p.rvol21_pct}%`);
    if (r.serenity_gate) {
      const g = r.serenity_gate;
      console.log(`  Serenity 閘門：賺錢能力=${g.profitability.value}`
        + (g.profitability.scope ? `（${g.profitability.scope}，覆蓋 ${g.profitability.coverage}）` : '')
        + `　護城河=${g.moat.value}　結論=${g.conclusion.value}`);
    }
  }
  console.log(`\n集中度：${concentration.reading}`);
  console.log(`相關性：${concentration.correlation_reading}`);
  console.log(`鏡頭狀態：${JSON.stringify(out.lens_status)}`);
}

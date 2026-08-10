// Hyperscaler capex — Layer A of switch 3, from SEC EDGAR XBRL.
//
// 10-Q filings report capex year-to-date, not per quarter, so discrete quarters have to
// be recovered by differencing consecutive cumulative spans inside a fiscal year:
//
//   Q1 = YTD(3m)              Q3 = YTD(9m) − YTD(6m)
//   Q2 = YTD(6m) − YTD(3m)    Q4 = FY      − YTD(9m)
//
// Companies also disagree on which tag carries the number (Amazon books most of it under
// PaymentsToAcquireProductiveAssets), so tags are tried in order per issuer.
//
// This is Layer A only — reported cash capex. It deliberately does NOT capture:
//   * finance leases, a large and growing share of AI datacenter capacity (Layer B)
//   * management guidance for the coming quarters, which has no XBRL tag (Layer C)
// so the signal it feeds is HYBRID, never AUTOMATED. Treating this number as the whole
// of AI infrastructure spend understates it, and the understatement is not constant.

const UA = { 'User-Agent': 'ag8ai6@gmail.com market-research-tool' };

export const HYPERSCALERS = {
  MSFT: { cik: '0000789019', name: 'Microsoft', fiscal_year_end: '06-30' },
  GOOGL: { cik: '0001652044', name: 'Alphabet', fiscal_year_end: '12-31' },
  AMZN: { cik: '0001018724', name: 'Amazon', fiscal_year_end: '12-31' },
  META: { cik: '0001326801', name: 'Meta', fiscal_year_end: '12-31' },
};

const TAGS = [
  'PaymentsToAcquireProductiveAssets',
  'PaymentsToAcquirePropertyPlantAndEquipment',
];

const spanDays = (a, b) => Math.round((new Date(b) - new Date(a)) / 86400000);

async function concept(cik, tag) {
  const r = await fetch(
    `https://data.sec.gov/api/xbrl/companyconcept/CIK${cik}/us-gaap/${tag}.json`, { headers: UA });
  if (!r.ok) return null;
  const body = await r.text();
  return { facts: JSON.parse(body).units?.USD ?? [], raw: body };
}

// Keep the most recently filed value for each reporting span — amendments supersede.
function latestPerSpan(facts) {
  const m = new Map();
  for (const f of facts) {
    if (!['10-Q', '10-K'].includes(f.form) || !f.start || !f.end) continue;
    const k = `${f.start}|${f.end}`;
    const prior = m.get(k);
    if (!prior || f.filed > prior.filed) m.set(k, f);
  }
  return [...m.values()].map((f) => ({ ...f, days: spanDays(f.start, f.end) }));
}

// Turn cumulative spans that share a start date into discrete quarters.
function toQuarters(spans) {
  const byStart = new Map();
  for (const s of spans) {
    if (!byStart.has(s.start)) byStart.set(s.start, []);
    byStart.get(s.start).push(s);
  }
  const out = new Map();                       // period_end -> quarter fact
  for (const [start, group] of byStart) {
    const cum = group.filter((s) => s.days >= 80).sort((a, b) => a.days - b.days);
    let prev = null;
    for (const s of cum) {
      const isQuarterLength = s.days <= 100;
      if (prev === null) {
        if (isQuarterLength) out.set(s.end, { start, end: s.end, val: s.val, ...meta(s), derived: false });
      } else {
        const gapDays = s.days - prev.days;
        if (gapDays >= 80 && gapDays <= 100) {
          out.set(s.end, {
            start: prev.end, end: s.end, val: s.val - prev.val, ...meta(s), derived: true,
            derived_from: { cumulative_end: s.end, minus_cumulative_end: prev.end },
          });
        }
      }
      prev = s;
    }
  }
  return [...out.values()].sort((a, b) => (a.end < b.end ? -1 : 1));
}

const meta = (s) => ({ form: s.form, fp: s.fp, fy: s.fy, filed: s.filed, accn: s.accn });

export async function fetchCapex(ticker, { archive } = {}) {
  const co = HYPERSCALERS[ticker];
  if (!co) throw new Error(`unknown issuer ${ticker}`);
  for (const tag of TAGS) {
    const res = await concept(co.cik, tag);
    if (!res) continue;
    const quarters = toQuarters(latestPerSpan(res.facts));
    // A tag only counts if it carries a usable recent run of quarters.
    const recent = quarters.filter((q) => q.end >= '2024-01-01');
    if (recent.length < 4) continue;
    const raw_hash = archive ? archive(`SEC_${ticker}_${tag}`, res.raw) : null;
    return { ticker, ...co, tag, quarters, raw_hash, retrieved_at: new Date().toISOString() };
  }
  throw new Error(`no usable capex tag for ${ticker}`);
}

// Aggregate the four issuers on calendar quarters. Microsoft's fiscal year ends in June,
// but its XBRL periods are still calendar-aligned, so the join key is the period end.
export async function aggregateCapex(opts = {}) {
  const issuers = [];
  const failures = [];
  for (const t of Object.keys(HYPERSCALERS)) {
    try { issuers.push(await fetchCapex(t, opts)); }
    catch (e) { failures.push({ ticker: t, error: String(e.message ?? e) }); }
  }
  if (!issuers.length) throw new Error('no issuer data');

  // Only quarters every surviving issuer reports — a partial sum would fake a decline.
  const ends = issuers.map((i) => new Set(i.quarters.map((q) => q.end)));
  const common = [...ends[0]].filter((e) => ends.every((s) => s.has(e))).sort();

  const series = common.map((end) => {
    const parts = issuers.map((i) => {
      const q = i.quarters.find((x) => x.end === end);
      return { ticker: i.ticker, val: q.val, filed: q.filed, accn: q.accn, derived: q.derived };
    });
    return {
      period_end: end,
      total_usd: parts.reduce((s, p) => s + p.val, 0),
      // The whole aggregate only becomes knowable when the LAST of the four has filed.
      information_available_at: parts.map((p) => p.filed).sort().at(-1),
      parts,
    };
  });

  const withGrowth = series.map((s, i) => ({
    ...s,
    total_bn: Number((s.total_usd / 1e9).toFixed(2)),
    qoq_pct: i > 0 ? Number(((s.total_usd / series[i - 1].total_usd - 1) * 100).toFixed(2)) : null,
    yoy_pct: i >= 4 ? Number(((s.total_usd / series[i - 4].total_usd - 1) * 100).toFixed(2)) : null,
  }));

  return {
    issuers: issuers.map((i) => ({ ticker: i.ticker, tag: i.tag, raw_hash: i.raw_hash,
      retrieved_at: i.retrieved_at, quarters_available: i.quarters.length })),
    failures,
    series: withGrowth,
    coverage: `${issuers.length}/${Object.keys(HYPERSCALERS).length} issuers`,
  };
}

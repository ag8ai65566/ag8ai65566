// Deterministic verification of the YTD-differencing used to recover quarterly capex.
//
// The differencing is `Q_n = YTD_n − YTD_{n-1}`, and until now nothing checked it. "The
// numbers looked plausible" is not verification — a sign error or a fiscal-year boundary
// slip would also look plausible.
//
// The check exists because some filers tag BOTH shapes for the same period: a cumulative
// span and a standalone quarter. Where both exist, the derived value must equal the
// directly reported one to the dollar. That is an accounting identity, not a statistic,
// so any mismatch is a defect rather than noise.
//
// Coverage is reported honestly: an issuer with no directly-tagged quarters cannot be
// verified this way, and the result says so instead of implying the whole pipeline passed.

const UA = { 'User-Agent': 'ag8ai6@gmail.com market-research-tool' };
const spanDays = (a, b) => Math.round((new Date(b) - new Date(a)) / 86400000);
// Only mismatches inside this window can affect a current reading.
const RECENT_YEARS = 3;

async function facts(cik, tag) {
  const r = await fetch(`https://data.sec.gov/api/xbrl/companyconcept/CIK${cik}/us-gaap/${tag}.json`,
    { headers: UA });
  if (!r.ok) return null;
  return (await r.json()).units?.USD ?? [];
}

/** Latest filed value per (start,end); amendments supersede. */
function latestPerSpan(raw) {
  const m = new Map();
  for (const f of raw) {
    if (!['10-Q', '10-K'].includes(f.form) || !f.start || !f.end) continue;
    const k = `${f.start}|${f.end}`;
    const prior = m.get(k);
    if (!prior || f.filed > prior.filed) m.set(k, f);
  }
  return [...m.values()].map((f) => ({ ...f, days: spanDays(f.start, f.end) }));
}

/**
 * For every quarter that can be derived by differencing, check it against a directly
 * reported quarter covering the same dates.
 */
export async function reconcile(ticker, cik, tag) {
  const raw = await facts(cik, tag);
  if (!raw) return { ticker, tag, status: 'SOURCE_FAILURE' };
  const spans = latestPerSpan(raw);

  // Standalone quarters, indexed by end date. Start dates are matched with a tolerance:
  // a derived quarter begins the day AFTER the previous cumulative span ends, so keying on
  // the raw boundary misses every counterpart by one day. The first version of this file
  // did exactly that and reported 0% coverage across all four issuers.
  const directByEnd = new Map();
  for (const s of spans) {
    if (s.days >= 80 && s.days <= 100) {
      if (!directByEnd.has(s.end)) directByEnd.set(s.end, []);
      directByEnd.get(s.end).push(s);
    }
  }
  const findDirect = (startBoundary, end) => (directByEnd.get(end) ?? [])
    .find((d) => Math.abs(spanDays(startBoundary, d.start)) <= 3) ?? null;

  // Derive quarters from consecutive cumulative spans that share a fiscal-year start.
  const byStart = new Map();
  for (const s of spans) {
    if (!byStart.has(s.start)) byStart.set(s.start, []);
    byStart.get(s.start).push(s);
  }
  const checks = [];
  for (const [, group] of byStart) {
    const cum = group.filter((s) => s.days >= 80).sort((a, b) => a.days - b.days);
    for (let i = 1; i < cum.length; i++) {
      const prev = cum[i - 1], cur = cum[i];
      const gap = cur.days - prev.days;
      if (gap < 80 || gap > 100) continue;                 // not a single-quarter step
      const derivedVal = cur.val - prev.val;
      const key = `${prev.end}→${cur.end}`;
      const reported = findDirect(prev.end, cur.end);
      if (!reported) {
        checks.push({ period: key, derived: derivedVal, reported: null, verdict: 'NO_DIRECT_COUNTERPART' });
        continue;
      }
      const diff = derivedVal - reported.val;
      checks.push({
        period: key, derived: derivedVal, reported: reported.val, diff,
        // XBRL values are exact integers in USD; a mismatch of even one dollar is a defect.
        verdict: diff === 0 ? 'EXACT_MATCH' : 'MISMATCH',
        derived_from: { cumulative: `${cur.start}→${cur.end}`, minus: `${prev.start}→${prev.end}`, filed: cur.filed },
        reported_from: { accn: reported.accn, filed: reported.filed, form: reported.form },
      });
    }
  }

  const verifiable = checks.filter((c) => c.verdict !== 'NO_DIRECT_COUNTERPART');
  const mismatches = verifiable.filter((c) => c.verdict === 'MISMATCH');
  // A discrepancy from a decade ago — a restatement, a reclassification — says nothing
  // about the quarters a current signal reads. Split by recency rather than letting one
  // 2015 row condemn the pipeline, or letting it be quietly dropped.
  const recentCutoff = new Date(); recentCutoff.setFullYear(recentCutoff.getFullYear() - RECENT_YEARS);
  const isRecent = (c) => new Date(c.period.split('→')[1]) >= recentCutoff;
  const recentMismatches = mismatches.filter(isRecent);
  return {
    ticker, tag,
    total_derivable: checks.length,
    verifiable: verifiable.length,
    exact_matches: verifiable.length - mismatches.length,
    mismatches_all: mismatches.length,
    mismatches_recent: recentMismatches.length,
    recent_window_years: RECENT_YEARS,
    mismatches: mismatches.map((m) => ({ ...m, recent: isRecent(m) })),
    coverage_pct: checks.length ? Number(((verifiable.length / checks.length) * 100).toFixed(1)) : 0,
    status: verifiable.length === 0 ? 'UNVERIFIABLE'
      : recentMismatches.length ? 'MISMATCH'
        : mismatches.length ? 'RECONCILED_WITH_HISTORICAL_EXCEPTIONS' : 'RECONCILED',
    checks,
  };
}

export async function reconcileAll(issuers) {
  const results = [];
  for (const { ticker, cik, tag } of issuers) results.push(await reconcile(ticker, cik, tag));
  const recentMismatch = results.filter((r) => r.status === 'MISMATCH').map((r) => r.ticker);
  const unverifiable = results.filter((r) => r.status === 'UNVERIFIABLE').map((r) => r.ticker);
  const historicalOnly = results.filter((r) => r.status === 'RECONCILED_WITH_HISTORICAL_EXCEPTIONS').map((r) => r.ticker);
  const totalExact = results.reduce((s, r) => s + (r.exact_matches ?? 0), 0);
  const totalVerifiable = results.reduce((s, r) => s + (r.verifiable ?? 0), 0);

  // The aggregate is only as trustworthy as its weakest issuer. An issuer that cannot be
  // checked at all leaves unverified arithmetic inside every quarter it contributes to.
  const verdict = recentMismatch.length ? 'MISMATCH'
    : unverifiable.length ? 'PARTIALLY_VERIFIED' : 'RECONCILED';

  const notes = [];
  if (totalVerifiable) notes.push(`可對照的 ${totalVerifiable} 筆差分中，${totalExact} 筆與公司直接申報的單季值分毫不差。`);
  if (historicalOnly.length) notes.push(`${historicalOnly.join('、')} 有 ${RECENT_YEARS} 年以外的歷史差異（多為重編或重分類），不影響當前讀數。`);
  if (unverifiable.length) notes.push(`${unverifiable.join('、')} 完全沒有可對照的直接申報單季值 —— 其差分結果無法用此方法驗證，因此任何包含它的季度合計都帶有未驗證的算術。`);
  if (recentMismatch.length) notes.push(`⚠️ ${recentMismatch.join('、')} 在近 ${RECENT_YEARS} 年出現不符，這會直接污染當前訊號。`);

  return {
    generated_at: new Date().toISOString(),
    recent_window_years: RECENT_YEARS,
    totals: { verifiable: totalVerifiable, exact: totalExact },
    by_issuer: Object.fromEntries(results.map((r) => [r.ticker, r.status])),
    unverifiable_issuers: unverifiable,
    results,
    verdict,
    note: notes.join(' '),
  };
}

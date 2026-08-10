// Company fundamentals from SEC EDGAR XBRL — the missing input that kept every
// Serenity Buffett-gate field pinned at `unverified`.
//
// Point-in-time by construction: every fact carries `filed`, the date the number first
// became knowable. A model asking "what did we know on date X" filters on that, never on
// period_end. A quarter ending 2026-06-30 filed on 2026-08-06 was invisible on 2026-07-15.
//
// Two fact shapes in XBRL, handled separately:
//   duration (revenue, profit, cash flow) — has start+end; 10-Qs report YTD cumulative,
//     so discrete quarters are recovered by differencing, same as capex.
//   instant  (assets, equity, cash)       — has end only; taken as-is.
//
// Tags differ by filer and by era, so candidates are tried in order per concept.

const UA = { 'User-Agent': 'ag8ai6@gmail.com market-research-tool' };

export const CONCEPTS = {
  revenue: {
    kind: 'duration',
    tags: ['RevenueFromContractWithCustomerExcludingAssessedTax',
      'RevenueFromContractWithCustomerIncludingAssessedTax', 'Revenues', 'SalesRevenueNet'],
  },
  grossProfit: { kind: 'duration', tags: ['GrossProfit'] },
  netIncome: { kind: 'duration', tags: ['NetIncomeLoss', 'ProfitLoss'] },
  operatingCashFlow: {
    kind: 'duration',
    tags: ['NetCashProvidedByUsedInOperatingActivities',
      'NetCashProvidedByUsedInOperatingActivitiesContinuingOperations'],
  },
  capex: {
    kind: 'duration',
    tags: ['PaymentsToAcquireProductiveAssets', 'PaymentsToAcquirePropertyPlantAndEquipment'],
  },
  assets: { kind: 'instant', tags: ['Assets'] },
  equity: {
    kind: 'instant',
    tags: ['StockholdersEquity', 'StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest'],
  },
};

const days = (a, b) => Math.round((new Date(b) - new Date(a)) / 86400000);

async function concept(cik, tag) {
  const r = await fetch(`https://data.sec.gov/api/xbrl/companyconcept/CIK${cik}/us-gaap/${tag}.json`,
    { headers: UA });
  if (!r.ok) return null;
  const body = await r.text();
  const json = JSON.parse(body);
  const unit = json.units?.USD ?? json.units?.shares ?? [];
  return { facts: unit, raw: body, label: json.label };
}

/** Latest filed value per reporting span; amendments supersede. */
const dedupe = (facts, key) => {
  const m = new Map();
  for (const f of facts) {
    if (!['10-Q', '10-K'].includes(f.form)) continue;
    const k = key(f);
    if (!k) continue;
    const prior = m.get(k);
    if (!prior || f.filed > prior.filed) m.set(k, f);
  }
  return [...m.values()];
};

function durationQuarters(facts) {
  const spans = dedupe(facts, (f) => (f.start && f.end ? `${f.start}|${f.end}` : null))
    .map((f) => ({ ...f, days: days(f.start, f.end) }));
  const byStart = new Map();
  for (const s of spans) {
    if (!byStart.has(s.start)) byStart.set(s.start, []);
    byStart.get(s.start).push(s);
  }
  const out = new Map();
  for (const [start, group] of byStart) {
    const cum = group.filter((s) => s.days >= 80).sort((a, b) => a.days - b.days);
    let prev = null;
    for (const s of cum) {
      if (prev === null) {
        if (s.days <= 100) out.set(s.end, { start, end: s.end, val: s.val, filed: s.filed, accn: s.accn, form: s.form, derived: false });
      } else {
        const gap = s.days - prev.days;
        if (gap >= 80 && gap <= 100) {
          out.set(s.end, { start: prev.end, end: s.end, val: s.val - prev.val, filed: s.filed, accn: s.accn, form: s.form, derived: true });
        }
      }
      prev = s;
    }
  }
  return [...out.values()].sort((a, b) => (a.end < b.end ? -1 : 1));
}

const instantPoints = (facts) =>
  dedupe(facts, (f) => (!f.start && f.end ? f.end : null))
    .map((f) => ({ end: f.end, val: f.val, filed: f.filed, accn: f.accn, form: f.form }))
    .sort((a, b) => (a.end < b.end ? -1 : 1));

export async function fetchFundamentals(ticker, cik, { archive, asOf = null } = {}) {
  const out = { ticker, cik, concepts: {}, missing: [], raw_hashes: {}, retrieved_at: new Date().toISOString() };
  for (const [name, spec] of Object.entries(CONCEPTS)) {
    let got = null;
    for (const tag of spec.tags) {
      const res = await concept(cik, tag);
      if (!res || !res.facts.length) continue;
      const series = spec.kind === 'duration' ? durationQuarters(res.facts) : instantPoints(res.facts);
      // Point-in-time filter: only what had been filed by asOf.
      const visible = asOf ? series.filter((p) => p.filed <= asOf) : series;
      if (visible.length < 2) continue;
      got = { tag, label: res.label, series: visible };
      if (archive) out.raw_hashes[`${name}:${tag}`] = archive(`SEC_${ticker}_${tag}`, res.raw);
      break;
    }
    if (got) out.concepts[name] = got;
    else out.missing.push(name);
  }
  return out;
}

/** Derived ratios. Each states which quarter it describes and when that became knowable. */
export function deriveMetrics(f) {
  const liabilitiesKnown = null;   // not fetched by this pipeline
  const last = (name) => f.concepts[name]?.series.at(-1) ?? null;
  const yearAgo = (name) => {
    const s = f.concepts[name]?.series;
    return s && s.length >= 5 ? s.at(-5) : null;
  };
  const rev = last('revenue'), revY = yearAgo('revenue');
  const gp = last('grossProfit');
  const ni = last('netIncome'), niY = yearAgo('netIncome');
  const ocf = last('operatingCashFlow'), cap = last('capex');
  const eq = last('equity'), assets = last('assets');

  const pct = (a, b) => (Number.isFinite(a) && Number.isFinite(b) && b !== 0 ? Number(((a / b - 1) * 100).toFixed(2)) : null);
  const ratio = (a, b) => (Number.isFinite(a) && Number.isFinite(b) && b !== 0 ? Number(((a / b) * 100).toFixed(2)) : null);

  // Gross margin only where the two legs describe the same quarter.
  const gmAligned = gp && rev && gp.end === rev.end;
  // FCF needs both legs from the same period too.
  const fcfAligned = ocf && cap && ocf.end === cap.end;

  return {
    period_end: rev?.end ?? ni?.end ?? null,
    information_available_at: [rev, gp, ni, ocf, cap].filter(Boolean).map((x) => x.filed).sort().at(-1) ?? null,
    revenue_usd: rev?.val ?? null,
    revenue_yoy_pct: rev && revY ? pct(rev.val, revY.val) : null,
    gross_margin_pct: gmAligned ? ratio(gp.val, rev.val) : null,
    gross_margin_alignment: gmAligned ? 'same_quarter' : 'MISALIGNED_OR_MISSING',
    net_income_usd: ni?.val ?? null,
    net_income_yoy_pct: ni && niY ? pct(ni.val, niY.val) : null,
    net_margin_pct: ni && rev && ni.end === rev.end ? ratio(ni.val, rev.val) : null,
    operating_cash_flow_usd: ocf?.val ?? null,
    capex_usd: cap?.val ?? null,
    free_cash_flow_usd: fcfAligned ? ocf.val - cap.val : null,
    free_cash_flow_alignment: fcfAligned ? 'same_quarter' : 'MISALIGNED_OR_MISSING',
    // Quarterly earnings annualised over latest equity — a rough ROE, labelled as such.
    roe_annualised_pct: ni && eq ? ratio(ni.val * 4, eq.val) : null,
    roe_caveat: 'Quarterly net income × 4 over latest reported equity. A rough read, not a trailing-twelve-month ROE.',
    equity_usd: eq?.val ?? null,
    assets_usd: assets?.val ?? null,
    // Anomaly ≠ error. An accounting identity that fails means the data IS wrong; a ratio
    // outside a hand-drawn band only means unusual, and the two must not share a siren.
    // A first version blocked on `asset_turnover < 0.25`, a number with nothing behind it —
    // the same mistake as the invented reserve-velocity threshold before it.
    plausibility: (() => {
      const structural = [];
      const reconciliation = [];
      const outliers = [];

      // STRUCTURAL — identities that cannot fail unless something is genuinely wrong.
      if (eq && assets && eq.val > assets.val) {
        structural.push({ check: 'equity_exceeds_assets',
          detail: `股東權益 ${(eq.val / 1e9).toFixed(2)}B > 總資產 ${(assets.val / 1e9).toFixed(2)}B`,
          issue: '會計恆等式不成立，兩者必有一個抓錯。', blocks: ['roe_annualised_pct', 'assets_usd', 'equity_usd'] });
      }
      if (gmAligned && (gp.val > rev.val)) {
        structural.push({ check: 'gross_profit_exceeds_revenue',
          issue: '毛利大於營收，不可能。', blocks: ['gross_margin_pct'] });
      }
      if (rev && rev.val < 0) {
        structural.push({ check: 'negative_revenue', issue: '營收為負，抓到的很可能不是營收。', blocks: ['revenue_usd'] });
      }

      // RECONCILIATION — internally consistent but needs a human against the filing.
      if (assets && eq && liabilitiesKnown === null) {
        // no-op placeholder: liabilities not fetched in this pipeline
      }

      // ECONOMIC OUTLIER — unusual, not wrong. Advisory only; blocks nothing.
      const turnover = assets && rev ? (rev.val * 4) / assets.val : null;
      if (turnover !== null && turnover < 0.25) {
        outliers.push({ check: 'asset_turnover', value: Number(turnover.toFixed(3)),
          detail: `年化營收為總資產的 ${(turnover * 100).toFixed(1)}%`,
          issue: '資產週轉率遠低於一般製造業常態。可能是合併合資廠資產、實體範圍不同，'
            + '或這門生意本來就極度資本密集。',
          note: '此門檻（0.25）沒有統計依據，是人為設定的注意線，不是資料錯誤的證據。',
          advisory_only: true, affects_interpretation_of: ['roe_annualised_pct'] });
      }
      const gmv = gmAligned ? gp.val / rev.val : null;
      if (gmv !== null && gmv > 0.9 && gmv <= 1) {
        outliers.push({ check: 'very_high_gross_margin', value: Number((gmv * 100).toFixed(2)),
          issue: '毛利率極高。對軟體正常，對硬體製造罕見 —— 值得確認是不是週期高點。',
          advisory_only: true });
      }

      const level = structural.length ? 'STRUCTURAL_ERROR'
        : reconciliation.length ? 'RECONCILIATION_REQUIRED'
          : outliers.length ? 'ECONOMIC_OUTLIER' : 'PASS';
      return {
        level,
        blocks_metrics: structural.flatMap((x) => x.blocks ?? []),
        structural, reconciliation, outliers,
        policy: 'STRUCTURAL_ERROR 會封鎖其所指的欄位；RECONCILIATION_REQUIRED 需人工對照原始申報；'
          + 'ECONOMIC_OUTLIER 只是提醒，不封鎖任何欄位，也不使用警報視覺。',
      };
    })(),
    sources: Object.fromEntries(Object.entries(f.concepts).map(([k, v]) => [k, {
      tag: v.tag, period: v.series.at(-1)?.end, filed: v.series.at(-1)?.filed,
      accession: v.series.at(-1)?.accn, form: v.series.at(-1)?.form,
      derived_from_cumulative: v.series.at(-1)?.derived ?? null,
    }])),
    missing: f.missing,
  };
}

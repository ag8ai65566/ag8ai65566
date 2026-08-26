// Three-layer freshness, and whether an unverified component could actually change the
// answer. Both exist because of one failure mode:
//
//   The dashboard sat on 2026-03-31 capex and labelled it LAGGED_BY_DESIGN, while three
//   of four issuers had already filed the next quarter. "The source is slow by nature"
//   became cover for "the pipeline did not pick up new data."
//
//   expected  — what SHOULD be published by now, from the calendar
//   available — what the issuers HAVE actually filed
//   ingested  — what this pipeline actually holds
//
// available > ingested is an INGESTION problem and must never read as source lag.

const iso = (d) => d.toISOString().slice(0, 10);

/** Quarter end immediately before `date`, plus the usual reporting lag. */
export function expectedLatestPeriod(now = new Date(), reportingLagDays = 40) {
  const cutoff = new Date(now);
  cutoff.setDate(cutoff.getDate() - reportingLagDays);
  const y = cutoff.getUTCFullYear();
  const m = cutoff.getUTCMonth();            // 0-11
  const qEndMonth = [2, 5, 8, 11].filter((x) => x <= m).pop();
  if (qEndMonth === undefined) return iso(new Date(Date.UTC(y - 1, 11, 31)));
  return iso(new Date(Date.UTC(y, qEndMonth + 1, 0)));
}

export const quarterLabel = (periodEnd) => {
  const d = new Date(`${periodEnd}T00:00:00Z`);
  return `${d.getUTCFullYear()}-Q${Math.floor(d.getUTCMonth() / 3) + 1}`;
};

/**
 * Compare the three layers and say which kind of lateness this is.
 */
export function freshnessLayers(issuers, ingestedPeriodEnd, { now = new Date() } = {}) {
  const expected = expectedLatestPeriod(now);
  const perIssuer = issuers.map((i) => ({
    ticker: i.ticker,
    latest_available: i.quarters.at(-1)?.end ?? null,
    latest_filed: i.quarters.at(-1)?.filed ?? null,
    has_expected: (i.quarters.at(-1)?.end ?? '') >= expected,
  }));
  const available = perIssuer.map((p) => p.latest_available).filter(Boolean).sort().at(-1) ?? null;
  const behind = perIssuer.filter((p) => !p.has_expected).map((p) => p.ticker);

  // Which issuers are holding the aggregate back? An aggregate that requires every
  // component cannot advance past its slowest member, so name that member rather than
  // implying the whole pipeline stalled.
  const blocking = perIssuer.filter((p) => (p.latest_available ?? '') < available).map((p) => p.ticker);

  let state;
  if (ingestedPeriodEnd >= expected) state = 'CURRENT';
  else if (available && available > ingestedPeriodEnd) state = 'INGESTION_OVERDUE';
  else if (behind.length) state = 'SOURCE_PUBLICATION_LAG';
  else state = 'LAGGED_BY_DESIGN';

  return {
    latest_expected_period: expected,
    latest_expected_label: quarterLabel(expected),
    latest_available_period: available,
    latest_available_label: available ? quarterLabel(available) : null,
    latest_ingested_period: ingestedPeriodEnd,
    latest_ingested_label: quarterLabel(ingestedPeriodEnd),
    state,
    issuers_without_expected_quarter: behind,
    blocking_issuers: blocking,
    per_issuer: perIssuer,
    reading: state === 'INGESTION_OVERDUE'
      ? `${perIssuer.filter((p) => p.latest_available === available).map((p) => p.ticker).join('、')}`
        + ` 已申報到 ${quarterLabel(available)}，但合計仍停在 ${quarterLabel(ingestedPeriodEnd)}，`
        + `因為 ${blocking.join('、')} 在本管線讀取的路徑（10-Q XBRL）上尚無該季資料。`
        + '這是取得路徑的限制，不是來源沒有公布 —— 該公司的財報新聞稿已有單季數字，'
        + '只是本管線尚未接上 issuer-direct 路徑。'
      : state === 'SOURCE_PUBLICATION_LAG'
        ? `${behind.join('、')} 尚未申報 ${quarterLabel(expected)}，合計因此無法推進 —— 這是來源落後。`
        : state === 'CURRENT' ? '已到達日曆上應有的最新季度。' : '在來源的正常發布節奏內。',
  };
}

/**
 * Would the answer change if the unverified components were wrong?
 *
 * Amount coverage is NOT confidence. A component that is 15% of the level can be 100% of
 * the change — so the question is never "how much is verified" but "could the unverified
 * part move the decision across its threshold". Shocks are applied over a stated range and
 * the rule is re-evaluated; the output is a sensitivity range, never a probability.
 */
export function decisionRobustness({ series, unverifiedTickers, shockPct = 0.25, ruleFn }) {
  if (!unverifiedTickers.length) {
    return { robustness: 'ROBUST', reason: '所有成分皆已對帳，無未驗證部分。', shock_pct: null };
  }
  const last = series.at(-1), prev = series.at(-2);
  if (!last || !prev) return { robustness: 'UNKNOWN', reason: '季度樣本不足以做敏感度測試。' };

  const shockOne = (q, mult) => q.parts.reduce(
    (sum, p) => sum + p.val * (unverifiedTickers.includes(p.ticker) ? mult : 1), 0);

  const outcomes = [];
  for (const lastMult of [1 - shockPct, 1, 1 + shockPct]) {
    for (const prevMult of [1 - shockPct, 1, 1 + shockPct]) {
      const qoq = (shockOne(last, lastMult) / shockOne(prev, prevMult) - 1) * 100;
      outcomes.push({ last_mult: lastMult, prev_mult: prevMult, qoq_pct: Number(qoq.toFixed(2)),
        rule: ruleFn(qoq) });
    }
  }
  const verdicts = [...new Set(outcomes.map((o) => o.rule))];
  const qoqs = outcomes.map((o) => o.qoq_pct);

  return {
    robustness: verdicts.length === 1 ? 'ROBUST' : 'SENSITIVE',
    shock_pct: shockPct,
    unverified_components: unverifiedTickers,
    sensitivity_range: { min_qoq_pct: Math.min(...qoqs), max_qoq_pct: Math.max(...qoqs) },
    outcomes_seen: verdicts,
    // Deliberately not called a confidence interval. No probability model stands behind it.
    label: 'SENSITIVITY_RANGE',
    label_note: '這是敏感度範圍，不是信賴區間。它假設未驗證成分在 ±' + (shockPct * 100)
      + '% 內任意變動，沒有機率模型支撐，也不代表任何分佈。',
    reading: verdicts.length === 1
      ? `即使未驗證成分（${unverifiedTickers.join('、')}）在 ±${shockPct * 100}% 內任意變動，`
        + `規則判定都維持「${verdicts[0]}」。決策對未驗證部分不敏感。`
      : `未驗證成分在 ±${shockPct * 100}% 內變動，就足以讓規則判定在 ${verdicts.join(' / ')} 之間翻轉。`
        + '決策對未驗證部分敏感，因此不評估。',
  };
}

/** Evidence coverage. Named so it can never be mistaken for statistical confidence. */
export function coverageMetadata(series, reconResults, unverifiedTickers) {
  const last = series.at(-1);
  const total = last.parts.reduce((s, p) => s + p.val, 0);
  const verifiedAmount = last.parts
    .filter((p) => !unverifiedTickers.includes(p.ticker))
    .reduce((s, p) => s + p.val, 0);
  const n = last.parts.length;
  return {
    issuer_coverage: `${n - unverifiedTickers.length}/${n}`,
    amount_coverage: Number((verifiedAmount / total).toFixed(4)),
    transformation_coverage: Number(((reconResults.totals?.exact ?? 0)
      / Math.max(1, reconResults.totals?.verifiable ?? 1)).toFixed(4)),
    aggregate_measurement_status: unverifiedTickers.length ? 'PARTIALLY_RECONCILED' : 'RECONCILED',
    _naming_rule: 'These are EVIDENCE COVERAGE figures. Coverage is not a confidence level and '
      + 'must never be rendered as one. Amount coverage in particular says nothing about how much '
      + 'of the CHANGE is verified — a component that is 15% of the level can be the whole of the '
      + 'movement, which is why the decision test is sensitivity, not coverage.',
  };
}

// Temporal joins, in one place, so no signal invents its own date logic.
//
// The bug this exists to prevent: taking `latest(A)` and `latest(B)` from two series that
// publish at different cadences and treating the pair as contemporaneous. M2 is monthly
// and lands ~30 days late; the Nasdaq closes daily. Comparing their newest points compares
// June to August and calls the difference a year-over-year gap.

export const isoDay = (d) => new Date(d).toISOString().slice(0, 10);

/** Calendar-aware shift. Not `minus 365 days` — that drifts through leap years. */
export function shiftYears(iso, years) {
  const d = new Date(`${iso}T00:00:00Z`);
  d.setUTCFullYear(d.getUTCFullYear() - years);
  return isoDay(d);
}

export function shiftMonths(iso, months) {
  const d = new Date(`${iso}T00:00:00Z`);
  const day = d.getUTCDate();
  d.setUTCDate(1);
  d.setUTCMonth(d.getUTCMonth() - months);
  const lastDay = new Date(Date.UTC(d.getUTCFullYear(), d.getUTCMonth() + 1, 0)).getUTCDate();
  d.setUTCDate(Math.min(day, lastDay));
  return isoDay(d);
}

/** The newest observation at or before `asOf`. Never looks forward. */
export function priorObservation(points, asOf) {
  let best = null;
  for (const p of points) if (p.date <= asOf && (!best || p.date > best.date)) best = p;
  return best;
}

/**
 * Anchor two series on a date both can actually speak to: the older of their two latest
 * effective dates. The slower series sets the anchor, and the result describes THAT date.
 */
export function alignByEffectiveDate(seriesA, seriesB) {
  const lastA = seriesA.at(-1), lastB = seriesB.at(-1);
  if (!lastA || !lastB) return { ok: false, reason: 'EMPTY_SERIES' };
  const anchor = lastA.date < lastB.date ? lastA.date : lastB.date;
  const a = priorObservation(seriesA, anchor), b = priorObservation(seriesB, anchor);
  if (!a || !b) return { ok: false, reason: 'NO_COMMON_ANCHOR' };
  return {
    ok: true, anchor, a, b,
    lag_days: Math.abs(Math.round((new Date(lastA.date) - new Date(lastB.date)) / 86400000)),
    anchor_set_by: lastA.date < lastB.date ? 'A' : 'B',
  };
}

/** Year-over-year at a given anchor, with the year-ago leg found by calendar, not offset. */
export function yoyAtAnchor(points, anchor, { maxBackfillDays = 45 } = {}) {
  const now = priorObservation(points, anchor);
  if (!now) return { ok: false, reason: 'NO_ANCHOR_OBSERVATION' };
  const target = shiftYears(anchor, 1);
  const then = priorObservation(points, target);
  if (!then) return { ok: false, reason: 'NO_YEAR_AGO_OBSERVATION' };
  const drift = Math.abs(Math.round((new Date(target) - new Date(then.date)) / 86400000));
  if (drift > maxBackfillDays) {
    return { ok: false, reason: 'YEAR_AGO_TOO_FAR', drift_days: drift, found: then.date };
  }
  return {
    ok: true, pct: (now.value / then.value - 1) * 100,
    now: { date: now.date, value: now.value }, then: { date: then.date, value: then.value },
    target_date: target, drift_days: drift,
  };
}

/**
 * Two quarterly series only divide cleanly when they describe the same quarter. Returns
 * the newest period both cover, or a DATE_MISMATCH the caller must surface rather than
 * dividing anyway.
 */
export function alignQuarterly(seriesA, seriesB, { toleranceDays = 45 } = {}) {
  for (let i = seriesA.length - 1; i >= 0; i--) {
    const a = seriesA[i];
    const b = seriesB.find((p) => Math.abs(new Date(p.date) - new Date(a.date)) / 86400000 <= toleranceDays);
    if (b) return { ok: true, a, b, period: a.date,
      offset_days: Math.abs(Math.round((new Date(a.date) - new Date(b.date)) / 86400000)) };
  }
  return { ok: false, reason: 'DATE_MISMATCH',
    latest_a: seriesA.at(-1)?.date, latest_b: seriesB.at(-1)?.date };
}

/** Where a value sits in its own recent history. Refuses to guess on a thin window. */
export function percentileInWindow(points, value, years, { now = new Date(), minN = 30 } = {}) {
  const cutoff = shiftYears(isoDay(now), years);
  const window = points.filter((p) => p.date >= cutoff).map((p) => p.value);
  if (window.length < minN) return { ok: false, reason: 'INSUFFICIENT_HISTORY', n: window.length, required: minN };
  const below = window.filter((v) => v < value).length;
  return { ok: true, value: Number(((below / window.length) * 100).toFixed(1)), window_years: years, n: window.length };
}

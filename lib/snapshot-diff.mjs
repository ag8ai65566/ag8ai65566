// "What changed since last run", as a pure function over two snapshots.
//
// This lives here rather than inside the engine for one reason: with a single day of
// history there is nothing to diff against, and the only ways to exercise the code would
// be to fabricate a prior snapshot — writing invented readings into the real history file
// — or to ship it untested. Neither is acceptable, so the logic takes its inputs as
// arguments and fixtures supply them.
//
// It also does not belong in the renderer. A delta is arithmetic, and the renderer is
// forbidden from arithmetic; a "what changed" panel is precisely where that rule would
// otherwise get quietly broken.

const r2 = (x, n = 2) => (Number.isFinite(x) ? Number(x.toFixed(n)) : null);

/**
 * @param prior   a snapshot object ({ date, gauges: [{id, value, rule_state, data_state, ...}] })
 *                or null when no earlier run exists
 * @param current the gauges array from this run
 */
export function diffSnapshots(prior, current) {
  if (!prior) {
    return { available: false, reason: '尚無更早的快照可供比較 —— 這是第一次留下歷史。',
      prior_date: null, rule_changes: [], state_changes: [], moves: [] };
  }
  const byId = new Map(prior.gauges.map((g) => [g.id, g]));
  const rule_changes = [], state_changes = [], moves = [];

  for (const g of current) {
    const p = byId.get(g.id);
    if (!p) {
      state_changes.push({ id: g.id, label: g.label, from: 'NEW', to: g.status?.data_state ?? null });
      continue;
    }
    const now = g.henren?.status ?? null;
    if (p.rule_state !== now) rule_changes.push({ id: g.id, label: g.label, from: p.rule_state, to: now });
    if (p.data_state !== (g.status?.data_state ?? null)) {
      state_changes.push({ id: g.id, label: g.label, from: p.data_state, to: g.status?.data_state ?? null });
    }
    const a = p.value, b = g.observed?.value;
    if (typeof a === 'number' && typeof b === 'number' && a !== b) {
      moves.push({
        id: g.id, label: g.label, from: a, to: b, delta: r2(b - a),
        unit: g.observed?.unit ?? '',
        // Only the absolute move is published. Percent change is undefined through zero,
        // and several of these gauges ARE percentages — "the percent change of a percent"
        // reads as two different things depending on who is looking.
        effective_from: p.effective_date ?? null,
        effective_to: g.observed?.effective_date ?? null,
        // A run can produce a new number without the source having published anything new;
        // it can also produce the same number from a genuinely new observation. The pair of
        // effective dates is the only way to tell those apart, so it travels with the delta.
        source_updated: (p.effective_date ?? null) !== (g.observed?.effective_date ?? null),
      });
    }
  }

  // A gauge the engine has stopped producing is a change too, and the noisiest kind to
  // discover later from a count that quietly dropped by one.
  const currentIds = new Set(current.map((g) => g.id));
  for (const p of prior.gauges) {
    if (!currentIds.has(p.id)) {
      state_changes.push({ id: p.id, label: p.id, from: p.data_state, to: 'DISAPPEARED' });
    }
  }

  return {
    available: true,
    prior_date: prior.date,
    prior_calculation_version: prior.calculation_version ?? null,
    rule_changes, state_changes, moves,
    note: '比較的是兩次執行之間的變化，不是市場報酬。讀數的生效日可能與執行日不同，'
      + '所以每筆都附上生效日 —— 引擎跑了不代表來源更新了。',
  };
}

/** Pick the most recent snapshot filename strictly before `today`. */
export function priorSnapshotFile(files, today) {
  return files.filter((f) => f.endsWith('.json') && f < today).sort().at(-1) ?? null;
}

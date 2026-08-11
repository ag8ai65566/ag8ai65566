// Output contract: the structural guardrail that replaces scanning rendered HTML.
//
// Why the old approach kept failing. Everything — engine output, static UI copy,
// disclaimers, source names, schema keys — was flattened into one HTML string, and a regex
// then tried to infer from wording alone which sentence was a system claim and which was
// boilerplate. It policed its own disclaimer three separate times:
//   1. the composite-score check matched `no_composite_score`, the field declaring compliance
//   2. the buy/sell check matched 「不輸出目標價」
//   3. the point-in-time check matched 「不是結構上不可能」
// Each fix made the regex cleverer. None removed the cause.
//
// The cause is that guardrails ran at the wrong layer. They now run BEFORE rendering,
// against structured data, where a system claim and a piece of static copy are different
// objects rather than adjacent substrings:
//
//   engine → typed JSON → schema (reject unknown keys) → prose guardrail → renderer + static UI
//
// Static copy never enters the guardrail, so it can say "no price targets" forever.

/** Keys a gauge may carry. Anything else is a contract violation, not something to ignore. */
export const GAUGE_KEYS = new Set([
  'id', 'switch', 'label', 'plain',
  'observed', 'empirical', 'henren', 'status', 'provenance', 'decision',
  'age_days', 'age_sessions', 'age_effective', 'age_unit', 'acceptable_age_days',
  'publication_period_days', 'publication_lag_ratio', 'publication_lag_reading',
  'note', 'proxy', 'proxy_warning', 'proxy_replacement',
  'naming_note', 'selection_bias_note', 'mixed_authority_note',
  'transformation_validation', 'reconciliation', 'coverage', 'decision_robustness',
  'freshness_layers', 'ingestion_alert', 'superseded_note', 'layers', 'source_authority_override',
  'would_have_been', 'missing', 'blocker', 'stale', 'ageDays',
]);

/**
 * Keys that must NEVER appear anywhere in the output. Not renamed, not nested, not
 * "ignored by the renderer" — rejected at validation, because a renderer that silently
 * drops them hides that an upstream producer already broke the contract.
 */
export const FORBIDDEN_KEYS = new Set([
  'recommendation', 'target_price', 'price_target', 'position_size', 'position_sizing',
  'trade_action', 'action', 'buy', 'sell', 'rating', 'conviction',
  'expected_return', 'probability_of_gain', 'allocation', 'weight_recommendation',
  'bubble_score', 'market_score', 'composite_score', 'overall_score', 'risk_score',
]);

/**
 * Fields that may contain model-generated prose. ONLY these are scanned for advisory
 * language. Everything else — labels, thresholds, source names, static copy — is out of
 * scope by construction.
 */
export const PROSE_FIELDS = [
  'observation_text', 'framework_text', 'uncertainty_text', 'falsifier_text',
  'commentary', 'summary_text', 'analysis_text',
];

/** Assertive advisory constructions. Second line of defence, not the safety system. */
const ADVISORY_PATTERNS = [
  /STRONG\s+(BUY|SELL)/i,
  /\b(BUY|SELL)\s+RATING\b/i,
  // No \b here: JavaScript word boundaries are defined on ASCII word characters, so `\b建`
  // never matches at the start of a string. The first version of this pattern silently let
  // 「建議加碼」 through — a guardrail that looks strict and matches nothing.
  /(建議|應該|值得)\s*(買進|買入|賣出|加碼|減碼|清倉|出清|進場|出場)/,
  /目標價\s*[:：$＄\d]/,
  /price\s+target\s*[:：$\d]/i,
  /風險報酬比?\s*(極|很|相當)?\s*(具吸引力|吸引人|好)/,
  /\b(risk[- ]reward)\b.{0,20}\b(attractive|compelling|favou?rable)\b/i,
];

function walkKeys(node, path, visit) {
  if (Array.isArray(node)) return node.forEach((v, i) => walkKeys(v, `${path}[${i}]`, visit));
  if (!node || typeof node !== 'object') return;
  for (const [k, v] of Object.entries(node)) {
    visit(k, v, path);
    walkKeys(v, `${path}.${k}`, visit);
  }
}

/**
 * Validate structured output. Returns violations rather than throwing, so a caller can
 * report every problem at once instead of one per run.
 */
export function validateOutput(payload, { allowedTopLevelGaugeKeys = GAUGE_KEYS } = {}) {
  const violations = [];

  walkKeys(payload, '$', (key, value, path) => {
    if (FORBIDDEN_KEYS.has(key)) {
      violations.push({ type: 'FORBIDDEN_KEY', key, path: `${path}.${key}`,
        detail: '此鍵在契約中被禁止。renderer 忽略它並不算修好 —— 上游已經違約了。' });
    }
  });

  for (const g of payload.gauges ?? []) {
    for (const k of Object.keys(g)) {
      if (!allowedTopLevelGaugeKeys.has(k)) {
        violations.push({ type: 'UNKNOWN_KEY', key: k, path: `$.gauges[${g.id}].${k}`,
          detail: '未在契約中宣告的鍵。新增欄位必須先加進 GAUGE_KEYS，'
            + '這樣才有人審查過它會不會出現在使用者面前。' });
      }
    }
  }

  // Prose scan, scoped to fields that can actually carry generated text.
  walkKeys(payload, '$', (key, value, path) => {
    if (!PROSE_FIELDS.includes(key) || typeof value !== 'string') return;
    for (const re of ADVISORY_PATTERNS) {
      if (re.test(value)) {
        violations.push({ type: 'ADVISORY_LANGUAGE', key, path: `${path}.${key}`,
          pattern: String(re), excerpt: value.slice(0, 120) });
      }
    }
  });

  return {
    valid: violations.length === 0,
    violations,
    scanned_prose_fields: PROSE_FIELDS,
    scope_note: 'Static UI copy and disclaimers are NOT scanned. They are not system claims, '
      + 'and scanning them is what made the previous guardrail flag its own compliance text.',
  };
}

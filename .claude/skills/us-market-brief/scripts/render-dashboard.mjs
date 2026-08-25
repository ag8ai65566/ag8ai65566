#!/usr/bin/env node
// RENDERER ONLY. Formats the canonical engine's output. It performs no financial
// calculation — no YoY, no percentile, no median, no velocity, no spread, no signal
// logic. Every number below is read from gauges.json exactly as the engine produced it.
//
//   node render-dashboard.mjs data/gauges.json data/snapshot.json > reports/us-market-dashboard.html
//
// Layout follows one rule: 「狠人認為這是危險訊號」and「歷史數據證明這是有效訊號」are
// different claims, so OBSERVED / EMPIRICAL CONTEXT / HENREN RULE / VALIDATION are four
// separate blocks in every card and are never merged into one traffic light.

import { readFileSync } from 'node:fs';

const data = JSON.parse(readFileSync(process.argv[2], 'utf8'));
const snap = process.argv[3] ? JSON.parse(readFileSync(process.argv[3], 'utf8')) : null;
const hold = process.argv[4] ? JSON.parse(readFileSync(process.argv[4], 'utf8')) : null;
const tests = process.argv[5] ? JSON.parse(readFileSync(process.argv[5], 'utf8')) : null;
const esc = (s) => String(s ?? '').replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

// Bucketing must be exhaustive. When the engine gained a third decision state, this file
// still filtered on `=== 'RULE_EVALUATED'`, and the capex card silently disappeared from
// the page while the summary above it kept counting 13 rules — a gauge can now only vanish
// if every bucket misses it, and the last bucket catches whatever the others do not.
const EVALUATED_DECISIONS = ['RULE_EVALUATED', 'RULE_EVALUATED_ON_SUPERSEDED_PERIOD'];
const evaluated = data.gauges.filter((g) => EVALUATED_DECISIONS.includes(g.decision));
const undecided = data.gauges.filter((g) => g.decision === 'NO_DECISION');
const unbucketed = data.gauges.filter((g) =>
  !EVALUATED_DECISIONS.includes(g.decision) && g.decision !== 'NO_DECISION');
const t = data.henren_rule_tally;
const chg = data.changes_since_last_run;
// Gauges that will expire out of rule evaluation before their source is next due to
// publish. Worth its own banner: when one of these drops out, the red count falls, and a
// falling red count is indistinguishable from a risk receding unless the page said so first.
const goingDark = data.gauges.filter((g) => g.sla_countdown);

const px = (sym) => snap?.rows?.find((r) => r.symbol === sym);

const SEV = { green: 'var(--ok)', yellow: 'var(--warn)', red: 'var(--bad)' };
const RULE_LABEL = { green: '未觸發', yellow: '接近', red: '觸發' };
const STATE_LABEL = {
  CURRENT: '當前', LAGGED_BY_DESIGN: '設計上落後', OVERDUE: '逾期未更新', STALE: '過期',
  MISSING: '缺漏', DATE_MISMATCH: '日期不一致', SOURCE_FAILURE: '來源失敗', NOT_WIRED: '未接線',
};
const AUTH_LABEL = {
  OFFICIAL_PRIMARY: '官方一手', OFFICIAL_AGGREGATOR: '官方彙整', LICENSED: '授權',
  UNOFFICIAL_FREE: '非官方免費', MANUAL_SECONDARY: '人工二手', NO_AUTHORITATIVE_SOURCE: '無權威來源',
};
const AUTO_LABEL = {
  AUTOMATED: '自動', HYBRID: '混合', MANUAL_REVIEW_REQUIRED: '需人工', NOT_WIRED: '未接線',
};

// The three summary boxes used to carry a hardcoded colour and headline. That is the same
// failure as every other one in this file's history: static prose asserting a state the
// data no longer supports. When TGA flipped to yellow the liquidity box went on saying
// 「平靜」in green, because nothing connected the sentence to the gauges underneath it.
// The verdict is now the worst rule state among the layer's own gauges — still presentation
// logic (a lookup, not a calculation), but it cannot disagree with the cards below.
const RANK = { green: 0, yellow: 1, red: 2 };
const layerVerdict = (ids) => {
  const states = ids.map((id) => data.gauges.find((g) => g.id === id))
    .filter((g) => g && g.henren?.status).map((g) => g.henren.status);
  if (!states.length) return { sev: 'var(--off)', status: null, evaluated: 0 };
  const worst = states.reduce((a, b) => (RANK[b] > RANK[a] ? b : a));
  return { sev: SEV[worst], status: worst, evaluated: states.length,
    counts: states.reduce((a, s) => { a[s] = (a[s] ?? 0) + 1; return a; }, {}) };
};
const LIQUIDITY_GAUGES = ['fuel', 'sofr', 'tga', 'rrp', 'hyoas', 'nfci'];
const CROWDING_GAUGES = ['ai-basket-rel-vol', 'zero-dte', 'top10-weight', 'margin-debt', 'insider-ratio'];
const liq = layerVerdict(LIQUIDITY_GAUGES);
const crowd = layerVerdict(CROWDING_GAUGES);

// The masthead said 「收在」 over an intraday print whenever the run happened during market
// hours. A price is a close or it is not; the label has to follow the session, not the habit.
const live = data.market_session?.us_market === 'OPEN';
const priceVerb = live ? '現價' : '收在';

const pct = (g) => {
  const p = g.empirical?.percentile_5y ?? g.empirical?.percentile_3y ?? g.empirical?.percentile_20y;
  return p?.ok ? p : null;
};

const dv = (o) => (o?.display_value ?? o?.value);
const pv = (p) => (p?.display_value ?? p?.value);

function card(g) {
  const p = pct(g);
  const sev = SEV[g.henren?.status] ?? 'var(--off)';
  const th = g.henren?.thresholds ?? {};
  const validation = g.status.signal_validation;
  const o = g.observed;
  // A rule that did not trigger on a quarter which has since been superseded is not a green
  // card. The colour has to carry the same qualification the label does, or the eye reads a
  // green light and the words never get a chance.
  const superseded = g.decision === 'RULE_EVALUATED_ON_SUPERSEDED_PERIOD';
  return `<article class="g" style="--sev:${superseded ? 'var(--brass)' : g.henren?.status ? sev : 'var(--off)'}">

  <!-- Validation status leads. It is read before the number, not after it. -->
  <div class="vstrip">
    <span class="vbadge">${esc(validation)}</span>
    <span class="vtext">此門檻尚未經過任何回測或樣本外檢驗</span>
    <span class="vchips">
      <span class="chip">${STATE_LABEL[g.status.data_state] ?? g.status.data_state}</span>
      <span class="chip${g.status.source_authority === 'UNOFFICIAL_FREE' ? ' weak' : ''}">${AUTH_LABEL[g.status.source_authority] ?? g.status.source_authority}</span>
      <span class="chip">${AUTO_LABEL[g.status.automation_mode] ?? g.status.automation_mode}</span>
    </span>
  </div>

  <h3>${esc(g.label)}${g.proxy ? '<span class="tag">代理</span>' : ''}${g.henren?.threshold_is_ours ? '<span class="tag tag-ours">門檻非原話</span>' : ''}${superseded ? '<span class="tag tag-sup">讀數已被更新的一季超過</span>' : ''}${g.sla_countdown ? `<span class="tag tag-dark">${g.sla_countdown.days_until_no_decision} 天後失效</span>` : ''}</h3>
  <p class="plain">${esc(g.plain)}</p>

  ${g.sla_countdown ? `<p class="note going-dark"><b>⏳ 這一格快要看不到了：</b>${esc(g.sla_countdown.reading)}
  ${esc(g.sla_countdown.tally_note)}</p>` : ''}

  ${g.freshness_layers ? `<div class="fresh fresh-${g.freshness_layers.state.toLowerCase()}">
    <div class="freshlab">資料新鮮度 · 三層</div>
    <div class="freshrow">
      <div class="fl"><span>日曆上應該有</span><b class="num">${esc(g.freshness_layers.latest_expected_label)}</b></div>
      <div class="fl"><span>發行人已申報</span><b class="num">${esc(g.freshness_layers.latest_available_label ?? '—')}</b></div>
      <div class="fl"><span>本管線實際有</span><b class="num">${esc(g.freshness_layers.latest_ingested_label)}</b></div>
    </div>
    <p class="freshread">${esc(g.freshness_layers.reading)}</p>
    ${g.freshness_layers.blocking_issuers?.length ? `<p class="qmeta">卡住合計的是：${g.freshness_layers.blocking_issuers.map(esc).join('、')}。</p>` : ''}
  </div>` : ''}

  ${g.decision_robustness && g.decision_robustness.label === 'SENSITIVITY_RANGE' ? `<p class="note rob">
    <b>未驗證成分會不會改變答案（${esc(g.decision_robustness.robustness)}）：</b>${esc(g.decision_robustness.reading)}
    區間 ${esc(g.decision_robustness.sensitivity_range.min_qoq_pct)}% ～ ${esc(g.decision_robustness.sensitivity_range.max_qoq_pct)}%。
    <i>${esc(g.decision_robustness.label_note)}</i></p>` : ''}

  ${g.coverage ? `<p class="note"><b>證據覆蓋（不是信心水準）：</b>
    發行人 ${esc(g.coverage.issuer_coverage)}　金額 ${esc(g.coverage.amount_coverage)}　轉換對帳 ${esc(g.coverage.transformation_coverage)}
    合計狀態 ${esc(g.coverage.aggregate_measurement_status)}。覆蓋率說的是「有多少被驗證過」，
    不是「有多大機率是對的」—— 佔水位 15% 的成分，可能就是變動的全部。</p>` : ''}

  <div class="split">
    <!-- Measurement -->
    <section class="side side-obs">
      <div class="sidelab">觀測到的事實</div>
      ${o && dv(o) !== null && dv(o) !== undefined ? `
        <div class="bignum num">${esc(dv(o))}<span class="qunit">${esc(o.unit)}</span></div>
        <div class="qmeta num">${esc(o.effective_date)}　·　${g.age_sessions !== null && g.age_sessions !== undefined ? `${g.age_sessions} 個交易日前` : `${g.age_days} 天前`}</div>
        ${g.publication_lag_ratio !== undefined ? `<div class="qmeta">落後 ${g.publication_lag_ratio} 個發布週期</div>` : ''}
      ` : '<div class="bignum muted">—</div>'}
      ${p ? `
        <div class="pctrow"><span>歷史位置</span><b class="num">P${esc(pv(p))}</b></div>
        <div class="pbar"><div class="pfill" style="width:${pv(p)}%"></div><div class="pneedle" style="left:calc(${pv(p)}% - 1px)"></div></div>
        <div class="qmeta">過去 ${p.window_years} 年，n=${p.n}</div>` : ''}
      ${g.empirical?.reading ? `<p class="qnote">${esc(g.empirical.reading)}</p>` : ''}
      ${g.empirical?.interim_event_coverage === 'MISSING' ? `<p class="qnote cov"><b>資訊涵蓋範圍：</b>僅限已申報實績。${esc(g.empirical.coverage_note ?? '')}</p>` : ''}
    </section>

    <!-- Interpretation. A separate object, never fused with the measurement. -->
    <section class="side side-rule">
      <div class="sidelab">狠人的規則怎麼說</div>
      ${g.henren?.status ? `
        <div class="rulestat" style="color:${sev}">${RULE_LABEL[g.henren.status]}</div>
        <div class="ths">${Object.entries(th).map(([k, v]) => `<span class="th th-${k}">${esc(v)}</span>`).join('')}</div>
      ` : `<div class="rulestat muted">不評估</div>
        <div class="qmeta">${esc(g.note ?? '此格沒有可用於規則評估的讀數。')}</div>`}
      ${g.henren?.quote ? `<blockquote>${esc(g.henren.quote)}</blockquote>` : ''}
    </section>
  </div>

  ${[
    g.henren?.note && ['他的說明', g.henren.note],
    g.henren?.seasonality_note && ['季節性', g.henren.seasonality_note],
    g.proxy_warning && ['代理指標警告', g.proxy_warning],
    g.naming_note && ['命名', g.naming_note],
    g.selection_bias_note && ['選樣偏誤', g.selection_bias_note],
    g.mixed_authority_note && ['來源權威', g.mixed_authority_note],
    g.reconciliation && ['差分對帳', `${g.reconciliation.verdict} — ${g.reconciliation.note}`],
    g.superseded_note && ['這個判定成立於哪一季', g.superseded_note],
    g.ingestion_alert && ['⚠️ 這是取得落後，不是來源落後', g.ingestion_alert],
  ].filter(Boolean).map(([k, v]) => `<p class="note"><b>${k}：</b>${esc(v)}</p>`).join('')}
  ${g.layers ? `<div class="layers">${Object.entries(g.layers).map(([k, v]) =>
    `<div class="layer"><b>${esc(k.replace(/^._/, '').replace(/_/g, ' '))}</b><span>${esc(v)}</span></div>`).join('')}</div>` : ''}

  <details class="prov"><summary>稽核抽屜 · 完整精度與來源鏈</summary>
    ${o?.display_rounded ? `<p class="exact">畫面顯示 <b class="num">${esc(dv(o))}</b>，實際值 <b class="num">${esc(o.exact_value)}</b>${p?.exact_value !== undefined ? `；百分位 P${esc(pv(p))} 的實際值為 ${esc(p.exact_value)}` : ''}。</p>` : ''}
    <dl>${Object.entries(g.provenance ?? {}).map(([k, v]) =>
      `<div><dt>${esc(k)}</dt><dd class="num">${esc(typeof v === 'boolean' ? (v ? 'true' : 'false') : v)}</dd></div>`).join('')}</dl>
  </details>
</article>`;
}

const G = (id) => data.gauges.find((x) => x.id === id);
const obs = (id) => G(id)?.observed;
const st = (id) => G(id)?.henren?.status;
const capex = G('capex');

// The summary reads canonical fields. It composes sentences; it computes nothing.
const summary = `
<section class="verdict" id="today">
  <h2>Today</h2>
  <p class="h2sub">狠人版總結 · 今天的市場</p>

  <div class="vgrid">
    <div class="vbox">
      <div class="vlab">基本面 · 管方向</div>
      <div class="vstat" style="--sev:var(--ok)">沒有裂縫</div>
      <p>標普${priceVerb} <b class="num">${px('^GSPC')?.close}</b>，${px('^GSPC')?.ddFromHigh === 0
        ? `<b>就是 52 週最高點本身</b>（${esc(px('^GSPC')?.hi52Date)}）`
        : `距 52 週高點 <b class="num">${px('^GSPC')?.ddFromHigh}%</b>`}。
      等權重 RSP 年初至今 <b class="num">${px('RSP')?.ytd}%</b>、羅素 2000 <b class="num">${px('^RUT')?.ytd}%</b>，
      都不輸市值權重的 <b class="num">${px('^GSPC')?.ytd}%</b> —— 這不是少數幾檔撐起來的盤。
      防禦股 XLU 近一月 <b class="num">${px('XLU')?.m1}%</b>，落後。</p>
    </div>
    <div class="vbox">
      <div class="vlab">流動性 · 管顛簸</div>
      <div class="vstat" style="--sev:${liq.sev}">${liq.status === 'green' ? '平靜，緩衝仍在'
        : liq.status === 'yellow' ? '價格面平靜，緩衝已經沒了' : '價格面開始承認'}</div>
      <p>銀行準備金 <b class="num">${obs('fuel')?.value}</b> 兆（清倉線 2.5 兆）、隔夜拆款利差
      <b class="num">${obs('sofr')?.value}</b> bp、垃圾債利差 <b class="num">${obs('hyoas')?.value}%</b>（五年 P${pct(G('hyoas'))?.value}）、
      VIX <b class="num">${px('^VIX')?.close}</b>。<b>唯一缺口：逆回購緩衝只剩
      <span class="num">${obs('rrp')?.value}</span> 億美元</b> —— 財政部再抽錢會直接打到準備金。</p>
    </div>
    <div class="vbox">
      <div class="vlab">擁擠 · 管斷裂</div>
      <div class="vstat" style="--sev:${crowd.sev}">${crowd.status === 'red'
        ? `${crowd.counts.red} 格觸發` : crowd.status === 'yellow' ? '接近門檻' : '未觸發'}</div>
      <p>大盤 21 日已實現波動 <b class="num">${px('^GSPC')?.rvol21}%</b>，但 AI 籃子中位數是它的
      <b class="num">${obs('ai-basket-rel-vol')?.value}</b> 倍，最高
      <b class="num">${obs('ai-basket-rel-vol')?.detail?.max}</b> 倍（SNDK）。
      指數在睡覺、少數幾檔用年化三位數波動在跑 —— 斷裂風險在個股，不在指數。</p>
    </div>
  </div>

  <div class="bell${capex?.decision === 'RULE_EVALUATED_ON_SUPERSEDED_PERIOD' ? ' bell-sup' : ''}">
    <div class="belllab">逃生鈴 · 開關三</div>
    <div class="bellval">${capex?.decision === 'RULE_EVALUATED_ON_SUPERSEDED_PERIOD'
      ? '還沒響 —— 但這是上一季的鈴' : '還沒響'}</div>
    <!-- The two growth rates were swapped here: observed.value is the QoQ figure (its unit
         says so), and the YoY lives in detail.yoy_pct. The page labelled the QoQ as 年增 and
         printed "undefined%" for the other. Read the unit, do not assume which one is which. -->
    <p>四家雲廠商 capex 合計 <b class="num">$${capex?.observed?.detail?.total_bn}B</b>
    （${esc(capex?.observed?.effective_date)} 季，資訊可得於 ${esc(capex?.observed?.detail?.information_available_at)}），
    環比 <b class="num">${capex?.observed?.value}%</b>、年增 <b class="num">${capex?.observed?.detail?.yoy_pct}%</b>
    （上一季 $${capex?.observed?.detail?.prior_quarter?.total_bn}B）。
    他的規則是「增速見頂回落就立刻平倉」，而這一季沒有回落，是在加速。</p>
    ${capex?.freshness_layers?.state === 'INGESTION_OVERDUE' ? `
    <p class="bellstale"><b>先講最重要的一件事：這不是最新的一季。</b>
    日曆上應該已經有 <b class="num">${esc(capex.freshness_layers.latest_expected_label)}</b>，
    發行人也已經申報到 <b class="num">${esc(capex.freshness_layers.latest_available_label)}</b>，
    但本管線手上只有 <b class="num">${esc(capex.freshness_layers.latest_ingested_label)}</b>。
    差距卡在 ${capex.freshness_layers.blocking_issuers.map(esc).join('、')} ——
    ${esc(capex.freshness_layers.blocking_issuers.join('、'))} 的單季數字在財報新聞稿裡有，
    只是本管線走的 10-Q XBRL 這條路上還沒有。
    <b>所以「還沒響」的正確讀法是：上一季沒響，這一季還沒看。</b>
    這一格因此標為「已評估、但讀數已被更新的一季超過」，不是綠燈也不是無讀數 ——
    把它算成綠燈，等於用舊資料背書現在。</p>` : ''}
    <p class="bellcaveat">另外，這只是 Layer A（申報現金 capex）。概念契約寫死不含融資租賃，
    下季指引也沒有 XBRL 標籤可接 —— 兩者都是 AI 資料中心支出裡會成長的部分。
    所以這個「還沒響」是<b>系統性低估後的還沒響</b>，而且低估的幅度不是固定的。</p>
  </div>

  <div class="oneline">
    <b>一句話：</b>方向沒問題、油還夠、逃生鈴上一季沒響 —— 但估值與擁擠度都在歷史極端
    （巴菲特指標 P${pct(G('buffett'))?.value}、AI 籃子波動是大盤 ${obs('ai-basket-rel-vol')?.value} 倍）。
    這不是「安全」，是<b>「還能燒，而且燒得很快」</b>。
    <b>${t.evaluated}</b> 條狠人規則已評估、其中 <b>${t.red ?? 0}</b> 條觸發${t.evaluated_on_superseded_period
      ? `，其中 <b>${t.evaluated_on_superseded_period}</b> 條評估在已被超過的季度上`
      : ''}，另有 <b>${t.no_decision}</b> 格沒有可用讀數。
    經統計驗證的訊號：<b>0</b>。
  </div>
  <p class="vwhatnot"><b>這段總結不會告訴你的事：</b>它不說該買或該賣，不給目標價，也不給部位大小。
  它只把「他的規則今天有沒有觸發」和「這條規則有沒有被證明過」分開講 ——
  第二個問題目前 16 格全部是「沒有」。</p>
  <p class="vdisc">以上每個數字都來自 canonical engine（calc v${esc(data.calculation_version)} @ ${esc(data.code_commit)}）。
  「狠人規則觸發」不等於「統計上證明危險」—— 全部 16 格的訊號驗證狀態都是 UNTESTED。</p>
</section>`;

// What moved since the previous run. Every delta below was computed by the engine — this
// file is not allowed to subtract two numbers, and a "what changed" panel is exactly where
// that rule would otherwise get quietly broken.
const changesSection = !chg ? '' : `
<section id="changes">
  <h2>Since last run</h2>
  <p class="h2sub">上一次執行之後，有什麼真的變了</p>
  ${!chg.available ? `<p class="lede">${esc(chg.reason)}</p>
  <div class="chempty">
    <p><b>這一區從下一次執行開始才有內容。</b>每次執行都會留下一份當日快照，之後這裡會列出三件事：
    哪一格的規則判定翻了顏色、哪一格的資料狀態變了（例如從 CURRENT 掉到 OVERDUE），
    以及每個讀數的絕對變動。</p>
    <p>最右邊那欄會標明<b>來源到底有沒有重新發布</b> —— 因為數字變了不代表市場動了，
    也可能只是同一個生效日的資料被修訂，或單純被重讀了一次。這兩件事在儀表板上長得一模一樣，
    但意思完全不同。</p>
  </div>` : `
  <p class="lede">與 <b class="num">${esc(chg.prior_date)}</b> 的快照相比。
  ${esc(chg.note)}</p>
  <div class="chgrid">
    <div class="chbox">
      <div class="chlab">規則狀態改變</div>
      ${chg.rule_changes.length ? `<ul class="chlist">${chg.rule_changes.map((c) =>
        `<li><b>${esc(c.label)}</b><span class="chmove">${esc(c.from ?? '—')} → ${esc(c.to ?? '—')}</span></li>`).join('')}</ul>`
        : '<p class="chnone">沒有任何一格的規則判定改變。</p>'}
    </div>
    <div class="chbox">
      <div class="chlab">資料狀態改變</div>
      ${chg.state_changes.length ? `<ul class="chlist">${chg.state_changes.map((c) =>
        `<li><b>${esc(c.label)}</b><span class="chmove">${esc(c.from ?? '—')} → ${esc(c.to ?? '—')}</span></li>`).join('')}</ul>`
        : '<p class="chnone">沒有任何一格的資料狀態改變。</p>'}
    </div>
  </div>
  ${chg.moves.length ? `<table class="chtab">
    <thead><tr><th>指標</th><th class="r">上次</th><th class="r">這次</th><th class="r">變動</th>
    <th>生效日</th><th>來源有更新嗎</th></tr></thead>
    <tbody>${chg.moves.map((m) => `<tr>
      <td>${esc(m.label)}</td>
      <td class="r num">${esc(m.from)}</td>
      <td class="r num">${esc(m.to)}</td>
      <!-- Deliberately not coloured green/red. Up is not good here: a rise in HY OAS is
           stress, a fall in reserves is stress, and a rise in capex growth is the thing the
           escape-bell rule is watching for the ABSENCE of. Direction is the sign's job;
           colouring it would assert a judgement the engine never made. -->
      <td class="r num delta">${m.delta > 0 ? '+' : ''}${esc(m.delta)}</td>
      <td class="num">${esc(m.effective_from)} → ${esc(m.effective_to)}</td>
      <td class="${m.source_updated ? 'up' : 'reread'}">${m.source_updated ? '是，新發布' : '否，同一天重讀'}</td>
      </tr>`).join('')}</tbody>
  </table>
  <p class="qmeta">只列絕對變動。百分比變動在通過零時沒有定義，而這裡有好幾格本身就是百分比 ——
  「百分比的百分比變動」會讀成兩種完全不同的意思。最後一欄很重要：數字變了不代表市場動了，
  也可能只是同一個生效日的資料被修訂或重讀。</p>` : '<p class="chnone">沒有任何讀數改變。</p>'}
  `}
</section>`;

// Test suite, by the question each category answers. Reads data/test-report.json.
const testSection = !tests ? '' : `
<section id="tests">
  <h2>What the tests actually test</h2>
  <p class="h2sub">測試分類 · 「${tests.passed}/${tests.total} 通過」本身不是保證</p>
  <p class="lede">一個總數聽起來像保證，但它沒說通過的是<strong>哪一個問題</strong>。
  這裡把測試依照它們回答的問題分開 —— 最後一格是空的，而那格才是重點。</p>
  <div class="tgrid">
    ${tests.categories.map((c) => `<div class="tbox ${c.passed === c.total ? 'tok' : 'tbad'}">
      <div class="tnum num">${c.passed}<span class="tof">/${c.total}</span></div>
      <div class="tlab">${esc(c.label)}</div>
      <p class="task">${esc(c.asks)}</p>
      <p class="twhy">${esc(c.why)}</p>
      ${c.failed.length ? `<p class="tfail">失敗：${c.failed.map(esc).join('；')}</p>` : ''}
    </div>`).join('')}
    <div class="tbox tempty">
      <div class="tnum num">0<span class="tof">/0</span></div>
      <div class="tlab">${esc(tests.absent_category.label)}</div>
      <p class="task">${esc(tests.absent_category.asks)}</p>
      <p class="twhy">${esc(tests.absent_category.why)}</p>
      <p class="tfail">${esc(tests.absent_category.state)}</p>
    </div>
  </div>
  <p class="nocomp">${esc(tests.reading)}</p>
</section>`;

// Holdings block. Reads holdings.json; computes nothing.
const holdingsSection = !hold ? '' : `
<section id="holdings">
  <h2>Holdings</h2>
  <p class="h2sub">持股 · Serenity 閘門（首次實際執行）</p>
  <p class="lede">在接上 SEC 財報之前，這個鏡頭的每一格都卡在 <code>unverified</code> ——
  不是因為公司未經證實，而是<strong>系統沒有證據可以評分</strong>。現在有了。
  規則不變：<strong>沒有引用就不得升級</strong>，XBRL 回答不了的欄位維持 <code>unverified</code>，
  那是正確答案，不是缺口。</p>
  <div class="conc">
    <div class="conclab">集中度</div>
    <p>${esc(hold.concentration.reading)}</p>
    <p class="corr">${esc(hold.concentration.correlation_reading)}</p>
    <p class="qmeta">${esc(hold.concentration.note)}</p>
  </div>
  <div class="grid">
  ${hold.holdings.map((h) => {
    const f = h.fundamentals, p = h.price, g = h.serenity_gate;
    const plaus = f?.plausibility;
    const structural = plaus?.structural?.length ? plaus.structural : null;
    const outliers = plaus?.outliers?.length ? plaus.outliers : null;
    return `<article class="g" style="--sev:var(--brass)">
      <header>
        <div class="ghead"><h3>${esc(h.ticker)} · ${esc(h.name)}<span class="tag">${esc(h.niche ?? h.sector)}</span></h3>
        <p class="plain">${esc(h.note ?? '')}</p></div>
        <div class="chips">
          <span class="chip chip-state">財報 ${esc(f?.information_available_at ?? '—')}（${h.fundamentals_age_days ?? '—'} 天）</span>
          <span class="chip chip-auth">官方一手</span>
        </div>
      </header>
      <div class="quad">
        <section class="q"><div class="qlab">營收（季）</div>
          <div class="qval num">${f?.revenue_bn ? '$' + f.revenue_bn + 'B' : '—'}</div>
          <div class="qmeta">年增 <b>${f?.revenue_yoy_pct ?? '—'}%</b>　期間 ${esc(f?.period_end ?? '—')}</div></section>
        <section class="q"><div class="qlab">獲利品質</div>
          <div class="qval num">${f?.net_margin_pct ?? '—'}%</div>
          <div class="qmeta">淨利率　毛利率 ${f?.gross_margin_pct ?? '未揭露'}${f?.gross_margin_pct ? '%' : ''}<br>
          FCF ${f?.free_cash_flow_bn ? '$' + f.free_cash_flow_bn + 'B' : '—'}</div></section>
        <section class="q"><div class="qlab">價格位置</div>
          <div class="qval num">${p?.from_2y_high_pct ?? '—'}%</div>
          <div class="qmeta">距兩年高點　vs 50日線 <b>${p?.vs_50dma_pct ?? '—'}%</b><br>
          21日波動 <b>${p?.rvol21_pct ?? '—'}%</b></div></section>
        <section class="q q-rule"><div class="qlab">Serenity 閘門</div>
          <div class="qval" style="font-size:15px;color:var(--ok)">賺錢能力 ${esc(g?.profitability.value ?? '—')}</div>
          <div class="qmeta">${g?.profitability.scope ? `範圍 <b>${esc(g.profitability.scope)}</b>　覆蓋 <b>${esc(g.profitability.coverage)}</b><br>` : ''}
          護城河 <b>${esc(g?.moat.value ?? '—')}</b>　結論 <b>${esc(g?.conclusion.value ?? '—')}</b></div></section>
      </div>
      ${g?.profitability.citations?.length ? `<p class="note"><b>賺錢能力的引用：</b>${g.profitability.citations.map(esc).join('；')}</p>` : ''}
      ${g?.moat ? `<p class="note"><b>護城河為何仍是 unverified：</b>${esc(g.moat.reason)}</p>` : ''}
      ${g?.profitability.scope_note ? `<p class="note"><b>為什麼是 SUPPORTED 而不是 proven：</b>${esc(g.profitability.scope_note)}${g.profitability.missing?.length ? ` 另缺 ${g.profitability.missing.join('、')}，覆蓋為 PARTIAL。` : ''}</p>` : ''}
      ${structural ? `<p class="note blocker"><b>⚠️ 合理性檢查未通過（STRUCTURAL_ERROR）：</b>${structural.map((x) => esc(x.issue)).join(' ')}
        已封鎖欄位：${structural.flatMap((x) => x.blocks ?? []).join('、')}。</p>` : ''}
      ${outliers ? `<p class="note advisory"><b>經濟異常值（${esc(plaus.level)}，僅提醒不封鎖）：</b>
        ${outliers.map((x) => `${esc(x.check)} = ${esc(x.value)} — ${esc(x.issue)}${x.note ? ` <i>${esc(x.note)}</i>` : ''}`).join('　')}</p>` : ''}
      ${g?.conclusion ? `<p class="note"><b>結論為何停在研究地图：</b>${esc(g.conclusion.reason)}</p>` : ''}
    </article>`;
  }).join('')}
  </div>
  <p class="nocomp"><b>三條分析流程的執行狀態：</b>${Object.entries(hold.lens_status).map(([k, v]) =>
    `${k} = <b>${v}</b>`).join('　·　')}。${esc(hold.guardrail)}<br>
  <b>為什麼不叫「三個鏡頭」：</b>三條流程跑在同一批 SEC 與市場資料上，看得再多次也還是同一個來源。
  證據的多樣性取決於<strong>每次分析背後有幾個彼此獨立的資料出處</strong>，不取決於跑了幾條流程 ——
  三條流程一起同意，可能只是同一筆資料被讀了三次。</p>
</section>`;

const html = `<title>美股儀表板 · 狠人規則 × 實證脈絡</title>
<style>
:root{--ground:#EDEFF2;--panel:#F8F9FB;--panel-2:#E7EAEF;--panel-3:#DDE2E9;--rule:#CDD3DC;--rule-soft:#DFE4EA;
--ink:#171C24;--ink-2:#4A5464;--ink-3:#78828F;--brass:#A8781C;--ok:#1F7A54;--warn:#B36A12;--bad:#B03047;
--ok-bg:#DDEEE6;--warn-bg:#F6E7CF;--bad-bg:#F4DDE1;--off:#C3CAD3;
--shadow:0 1px 2px rgba(23,28,36,.06),0 8px 24px -12px rgba(23,28,36,.16);}
@media(prefers-color-scheme:dark){:root:not([data-theme="light"]){--ground:#0C1017;--panel:#141A23;--panel-2:#1B222D;
--panel-3:#222A36;--rule:#2A3341;--rule-soft:#212936;--ink:#E8ECF2;--ink-2:#A3AEBD;--ink-3:#737F8E;--brass:#D9A43F;
--ok:#4CBF8B;--warn:#E3A44E;--bad:#E86A80;--ok-bg:#14312A;--warn-bg:#33280F;--bad-bg:#371A22;--off:#3A4453;
--shadow:0 1px 2px rgba(0,0,0,.4),0 10px 30px -14px rgba(0,0,0,.7);}}
:root[data-theme="dark"]{--ground:#0C1017;--panel:#141A23;--panel-2:#1B222D;--panel-3:#222A36;--rule:#2A3341;
--rule-soft:#212936;--ink:#E8ECF2;--ink-2:#A3AEBD;--ink-3:#737F8E;--brass:#D9A43F;--ok:#4CBF8B;--warn:#E3A44E;
--bad:#E86A80;--ok-bg:#14312A;--warn-bg:#33280F;--bad-bg:#371A22;--off:#3A4453;
--shadow:0 1px 2px rgba(0,0,0,.4),0 10px 30px -14px rgba(0,0,0,.7);}
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--ink);font-size:16px;line-height:1.65;
font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang TC","Noto Sans TC","Microsoft JhengHei",system-ui,sans-serif;
-webkit-font-smoothing:antialiased}
.num{font-family:ui-monospace,"SF Mono",Menlo,Consolas,monospace;font-variant-numeric:tabular-nums}
.wrap{max-width:1040px;margin:0 auto;padding:30px 20px 90px}
.mast{border-bottom:2px solid var(--ink);padding-bottom:16px;margin-bottom:20px}
.kicker{font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--brass);font-weight:700;margin-bottom:9px}
h1{font-size:clamp(24px,4.2vw,36px);line-height:1.15;margin:0 0 11px;letter-spacing:-.02em;font-weight:750;text-wrap:balance}
.standfirst{font-size:15.5px;color:var(--ink-2);margin:0;max-width:66ch}
.session{margin-top:16px;display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:9px 18px;
background:var(--panel);border:1px solid var(--rule);border-radius:4px;padding:13px 15px;box-shadow:var(--shadow)}
.session dt{color:var(--ink-3);font-size:10.5px;letter-spacing:.05em;text-transform:uppercase}
.session dd{margin:2px 0 0;font-weight:600;font-size:12.5px}
h2{font-size:11.5px;letter-spacing:.15em;text-transform:uppercase;color:var(--ink-3);font-weight:700;
margin:40px 0 4px;display:flex;align-items:center;gap:12px}
h2::after{content:"";flex:1;height:1px;background:var(--rule)}
.h2sub{font-size:20px;font-weight:720;margin:0 0 6px;letter-spacing:-.015em}
.lede{color:var(--ink-2);margin:0 0 16px;max-width:68ch;font-size:14.5px}

/* verdict */
.verdict{margin:26px 0 0}
.vgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:14px 0}
@media(max-width:840px){.vgrid{grid-template-columns:1fr}}
.vbox{background:var(--panel);border:1px solid var(--rule);border-top:3px solid var(--sev,var(--off));
border-radius:4px;padding:16px;box-shadow:var(--shadow)}
.vlab{font-size:10.5px;letter-spacing:.11em;text-transform:uppercase;color:var(--ink-3);font-weight:700}
.vstat{font-size:20px;font-weight:750;color:var(--sev);margin:3px 0 8px;letter-spacing:-.015em}
.vbox p{margin:0;font-size:13.5px;color:var(--ink-2);line-height:1.6}
.bell{background:var(--panel);border:1px solid var(--rule);border-left:4px solid var(--ok);border-radius:4px;
padding:18px;box-shadow:var(--shadow);margin:12px 0}
.belllab{font-size:10.5px;letter-spacing:.11em;text-transform:uppercase;color:var(--ink-3);font-weight:700}
.bellval{font-size:26px;font-weight:770;color:var(--ok);letter-spacing:-.02em;margin:2px 0 8px}
/* A bell that rang on a quarter which has since been superseded is not a green light.
   Colouring it green is the visual form of the same mistake the label is there to prevent. */
.bell-sup{border-left-color:var(--brass)}
.bell-sup .bellval{color:var(--brass)}
.bell p{margin:0 0 8px;font-size:14px;color:var(--ink-2);line-height:1.62}
.bellcaveat{font-size:13px !important;border-top:1px dashed var(--rule);padding-top:9px;margin-top:10px !important}
.oneline{background:var(--panel-2);border:1px solid var(--rule);border-left:4px solid var(--brass);
border-radius:4px;padding:16px 18px;font-size:15px;line-height:1.7;color:var(--ink-2)}
.oneline b{color:var(--ink)}
.vdisc{font-size:12.5px;color:var(--ink-3);margin:10px 0 0;line-height:1.6}

/* tally */
.tallybar{display:flex;gap:9px;flex-wrap:wrap;margin:16px 0 10px}
.tchip{display:flex;align-items:baseline;gap:6px;background:var(--panel);border:1px solid var(--rule);
border-radius:4px;padding:9px 13px;box-shadow:var(--shadow)}
.tchip b{font-size:20px;font-weight:760;letter-spacing:-.02em}.tchip span{font-size:12px;color:var(--ink-2)}
.t-red b{color:var(--bad)}.t-yellow b{color:var(--warn)}.t-green b{color:var(--ok)}.t-undec b{color:var(--ink-3)}
.dims{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:10px;margin:12px 0 0}
.dim{background:var(--panel);border:1px solid var(--rule);border-radius:4px;padding:12px 14px;box-shadow:var(--shadow)}
.dim h4{margin:0 0 6px;font-size:10.5px;letter-spacing:.09em;text-transform:uppercase;color:var(--ink-3);font-weight:700}
.dim div{font-size:12.5px;color:var(--ink-2);display:flex;justify-content:space-between;gap:10px}
.dim b{color:var(--ink);font-weight:700}
.nocomp{background:var(--panel-2);border:1px solid var(--rule);border-left:4px solid var(--brass);border-radius:4px;
padding:13px 15px;font-size:13.5px;color:var(--ink-2);margin:14px 0 0}

/* gauge cards */
.grid{display:flex;flex-direction:column;gap:11px}
.g{background:var(--panel);border:1px solid var(--rule);border-left:4px solid var(--sev);border-radius:4px;
padding:17px;box-shadow:var(--shadow)}
.g header{display:flex;justify-content:space-between;gap:14px;flex-wrap:wrap;align-items:flex-start}
.g h3{margin:0;font-size:16.5px;font-weight:720;letter-spacing:-.01em}
.tag{font-size:10px;font-weight:700;padding:2px 6px;border-radius:3px;background:var(--panel-3);
color:var(--ink-3);margin-left:7px;vertical-align:middle;letter-spacing:.04em}
.tag-ours{background:var(--warn-bg);color:var(--warn)}
.plain{margin:5px 0 0;font-size:13px;color:var(--ink-2);max-width:62ch;line-height:1.55}
.chips{display:flex;gap:5px;flex-wrap:wrap;flex:none}
.chip{font-size:10.5px;font-weight:700;padding:3px 8px;border-radius:3px;background:var(--panel-2);
color:var(--ink-3);border:1px solid var(--rule-soft);white-space:nowrap}
.chip-auth.weak{color:var(--warn);background:var(--warn-bg);border-color:transparent}
.quad{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:var(--rule-soft);
border:1px solid var(--rule-soft);border-radius:4px;margin:15px 0 0;overflow:hidden}
@media(max-width:820px){.quad{grid-template-columns:repeat(2,1fr)}}
.q{background:var(--panel);padding:12px 13px}
.q-rule{background:var(--panel-2)}
.qlab{font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-3);font-weight:700;margin-bottom:5px}
.qval{font-size:21px;font-weight:750;letter-spacing:-.02em;line-height:1.2}
.qval.muted{color:var(--ink-3)}
.val-untested{font-size:13px;font-weight:700;color:var(--warn);letter-spacing:.02em}
.qunit{font-size:11px;color:var(--ink-3);font-weight:500;margin-left:4px}
.qmeta{font-size:11px;color:var(--ink-3);margin-top:4px}
.qnote{font-size:11.5px;color:var(--ink-2);margin:7px 0 0;line-height:1.5}
.pbar{position:relative;height:6px;background:var(--panel-3);border-radius:2px;margin:7px 0 0;overflow:hidden}
.pfill{position:absolute;inset:0 auto 0 0;background:var(--sev);opacity:.35}
.pneedle{position:absolute;top:-3px;bottom:-3px;width:2px;background:var(--ink);border-radius:1px}
.ths{display:flex;flex-direction:column;gap:3px;margin-top:7px}
.th{font-size:10.5px;padding:2px 7px;border-radius:3px;background:var(--panel);border:1px solid var(--rule-soft);color:var(--ink-2)}
.th-green{color:var(--ok);background:var(--ok-bg);border-color:transparent}
.th-yellow{color:var(--warn);background:var(--warn-bg);border-color:transparent}
.th-red{color:var(--bad);background:var(--bad-bg);border-color:transparent}
blockquote{margin:14px 0 0;padding:10px 14px;border-left:3px solid var(--brass);background:var(--panel-2);
border-radius:0 3px 3px 0;font-size:13px;color:var(--ink-2);line-height:1.6}
.note{font-size:12.5px;color:var(--ink-2);margin:10px 0 0;line-height:1.6;max-width:76ch}
.note b{color:var(--ink)}
.layers{margin:12px 0 0;display:flex;flex-direction:column;gap:5px}
.layer{display:flex;gap:10px;font-size:12px;background:var(--panel-2);padding:7px 10px;border-radius:3px}
.layer b{color:var(--ink);flex:none;min-width:170px;font-weight:700}
.layer span{color:var(--ink-2)}
.prov{margin-top:13px;font-size:12px}
.prov summary{cursor:pointer;color:var(--brass);font-weight:600;font-size:11.5px;letter-spacing:.04em}
.prov dl{margin:9px 0 0;display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:5px 18px}
.prov dt{color:var(--ink-3);font-size:10px;letter-spacing:.04em;text-transform:uppercase}
.prov dd{margin:1px 0 0;color:var(--ink-2);font-size:11.5px;word-break:break-all}
footer{margin-top:48px;padding-top:18px;border-top:1px solid var(--rule);font-size:12.5px;color:var(--ink-3);line-height:1.7}
.conc{background:var(--panel);border:1px solid var(--rule);border-left:4px solid var(--brass);
border-radius:4px;padding:15px 17px;margin:0 0 14px;box-shadow:var(--shadow)}
.conclab{font-size:10.5px;letter-spacing:.11em;text-transform:uppercase;color:var(--ink-3);font-weight:700;margin-bottom:4px}
.conc p{margin:0 0 6px;font-size:14px;color:var(--ink-2);line-height:1.6}
.conc .corr{color:var(--ink);font-weight:600}
code{font-family:ui-monospace,Menlo,monospace;font-size:.9em;background:var(--panel-2);padding:1px 5px;border-radius:3px}

/* validation-first strip */
.vstrip{display:flex;align-items:center;gap:10px;flex-wrap:wrap;padding:8px 11px;margin:-17px -17px 14px;
background:var(--warn-bg);border-bottom:1px solid var(--rule);border-radius:3px 3px 0 0}
.vbadge{font-size:11px;font-weight:800;letter-spacing:.09em;color:var(--warn);
background:var(--panel);padding:3px 9px;border-radius:3px;border:1px solid var(--warn)}
.vtext{font-size:12px;color:var(--warn);font-weight:600}
.vchips{margin-left:auto;display:flex;gap:5px;flex-wrap:wrap}
.g h3{margin:0 0 4px;font-size:17px;font-weight:730;letter-spacing:-.01em}
.split{display:grid;grid-template-columns:1.15fr .85fr;gap:1px;background:var(--rule-soft);
border:1px solid var(--rule-soft);border-radius:4px;margin:14px 0 0;overflow:hidden}
@media(max-width:800px){.split{grid-template-columns:1fr}}
.side{background:var(--panel);padding:14px 15px}
.side-rule{background:var(--panel-2)}
.sidelab{font-size:10px;letter-spacing:.11em;text-transform:uppercase;color:var(--ink-3);font-weight:700;margin-bottom:7px}
.bignum{font-size:30px;font-weight:760;letter-spacing:-.025em;line-height:1.1}
.bignum.muted{color:var(--ink-3)}
.rulestat{font-size:24px;font-weight:760;letter-spacing:-.02em;line-height:1.15;margin-bottom:8px}
.rulestat.muted{color:var(--ink-3);font-size:19px}
.pctrow{display:flex;justify-content:space-between;align-items:baseline;margin:13px 0 5px;
font-size:11.5px;color:var(--ink-3);border-top:1px dotted var(--rule);padding-top:11px}
.pctrow b{font-size:16px;color:var(--ink)}
.qnote.cov{border-left:2px solid var(--warn);padding-left:9px;margin-top:10px}
.note.advisory{border-left:2px dotted var(--ink-3);padding-left:10px;color:var(--ink-2)}
.note.advisory i{font-style:normal;color:var(--ink-3);font-size:.94em}
.exact{font-size:12.5px;color:var(--ink-2);margin:0 0 10px;padding:9px 11px;
background:var(--panel-2);border-radius:3px}
/* maturity ladder */
.ladder{list-style:none;padding:0;margin:0 0 18px;display:flex;flex-direction:column;gap:2px;
border:1px solid var(--rule);border-radius:4px;overflow:hidden;box-shadow:var(--shadow)}
.rung{display:grid;grid-template-columns:auto 1fr auto;gap:14px;align-items:center;
padding:13px 16px;background:var(--panel);border-left:4px solid var(--off)}
.rung-established{border-left-color:var(--ok);background:var(--panel)}
.rung-in_progress{border-left-color:var(--warn);background:var(--panel)}
.rung-not_started{border-left-color:var(--bad);background:var(--panel-2);opacity:.9}
.rungno{font-size:12px;font-weight:800;color:var(--ink-3);width:16px;text-align:center}
.rungbody{display:flex;flex-direction:column;gap:2px}
.rungbody b{font-size:14.5px;font-weight:720}
.rungdetail{font-size:12.5px;color:var(--ink-2);line-height:1.55}
.rungstate{font-size:11.5px;font-weight:700;white-space:nowrap;padding:3px 9px;border-radius:3px}
.rung-established .rungstate{color:var(--ok);background:var(--ok-bg)}
.rung-in_progress .rungstate{color:var(--warn);background:var(--warn-bg)}
.rung-not_started .rungstate{color:var(--bad);background:var(--bad-bg)}
.counts{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px;margin:0 0 12px}
.cnt{background:var(--panel);border:1px solid var(--rule);border-radius:4px;padding:12px 14px;box-shadow:var(--shadow)}
.cnt b{display:block;font-size:26px;font-weight:770;letter-spacing:-.02em;line-height:1.1}
.cnt span{font-size:12px;color:var(--ink-2)}
.cnt-zero{border-color:var(--bad)}.cnt-zero b{color:var(--bad)}

/* Sticky section nav. The page got long enough that "scroll until you find it" became the
   navigation model, which buries the caveats under the numbers. */
.nav{position:sticky;top:0;z-index:20;display:flex;flex-wrap:wrap;gap:2px;margin:0 0 22px;
padding:8px 0;background:var(--ground);border-bottom:1px solid var(--rule)}
.nav a{padding:5px 11px;font-size:12px;color:var(--ink-2);text-decoration:none;border:1px solid transparent;
border-radius:3px;letter-spacing:.02em}
.nav a:hover{background:var(--panel);border-color:var(--rule);color:var(--ink)}
/* Without this the sticky bar lands on top of whatever heading you jumped to. */
section[id]{scroll-margin-top:56px}
.chempty{padding:13px 15px;background:var(--panel);border:1px dashed var(--rule);border-radius:4px;
font-size:12.5px;color:var(--ink-2);line-height:1.8}
.chempty p{margin:0 0 8px}.chempty p:last-child{margin:0}

/* Going dark. Deliberately above the fold: a gauge that expires takes a red light with it,
   and the tally moving down reads as improvement unless this is said in advance. */
.darkwarn{margin:0 0 22px;padding:14px 16px;background:#FBF6EC;border:1px solid var(--brass);
border-left:4px solid var(--brass);border-radius:4px}
.dwlab{font-size:10.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--brass);margin-bottom:7px}
.darkwarn p{margin:0 0 9px;font-size:12.5px;line-height:1.8;color:var(--ink)}
.dwlist{margin:0;padding:0;list-style:none;display:grid;gap:6px}
.dwlist li{display:flex;flex-wrap:wrap;align-items:baseline;gap:10px;padding:7px 10px;
background:var(--panel);border:1px solid var(--rule-soft);border-radius:3px;font-size:12.5px}
.dwdays{font-variant-numeric:tabular-nums;font-weight:700;color:var(--brass)}
.dwwhy{color:var(--ink-3);font-size:11.5px}
.tag-dark{background:#FBF6EC;border-color:var(--brass);color:var(--brass)}
.note.going-dark{border-left-color:var(--brass);background:#FBF6EC}

/* Three-layer freshness. Laid out as three columns because the whole point is the GAP
   between them — a single "as of" date cannot show that the pipeline is the slow part. */
.fresh{margin:12px 0;padding:11px 13px;border:1px solid var(--rule);border-left:3px solid var(--ink-3);
border-radius:3px;background:var(--panel-2)}
.fresh-ingestion_overdue{border-left-color:var(--bad);background:#FBF1F3}
.fresh-source_publication_lag{border-left-color:var(--warn)}
.fresh-current{border-left-color:var(--ok)}
.freshlab{font-size:10.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--ink-3);margin-bottom:7px}
.freshrow{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}
.fl{padding:6px 8px;background:var(--panel);border:1px solid var(--rule-soft);border-radius:3px}
.fl span{display:block;font-size:10.5px;color:var(--ink-3);margin-bottom:2px}
.fl b{font-size:14px;color:var(--ink)}
.freshread{margin:8px 0 0;font-size:12px;color:var(--ink-2);line-height:1.65}
.note.rob{border-left-color:var(--brass)}
.note.rob i{color:var(--ink-3);font-style:normal;font-size:11.5px}
.tag-sup{background:#FBF1F3;border-color:var(--bad);color:var(--bad)}
.bellstale{margin-top:10px;padding:11px 13px;background:#FBF1F3;border:1px solid var(--bad);
border-radius:3px;font-size:12.5px;line-height:1.75;color:var(--ink)}
.vwhatnot{margin-top:12px;padding:10px 13px;border:1px dashed var(--rule);border-radius:3px;
font-size:12px;color:var(--ink-2);line-height:1.7}

/* Since last run. */
.chgrid{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:14px}
.chbox{padding:12px 14px;background:var(--panel);border:1px solid var(--rule);border-radius:4px}
.chlab{font-size:10.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--ink-3);margin-bottom:8px}
.chlist{margin:0;padding:0;list-style:none}
.chlist li{display:flex;justify-content:space-between;gap:10px;padding:5px 0;border-bottom:1px solid var(--rule-soft);
font-size:12.5px}
.chlist li:last-child{border-bottom:none}
.chmove{font-variant-numeric:tabular-nums;color:var(--ink-2);white-space:nowrap}
.chnone{margin:0;font-size:12.5px;color:var(--ink-3)}
.chtab{width:100%;border-collapse:collapse;font-size:12.5px;background:var(--panel);
border:1px solid var(--rule);border-radius:4px;overflow:hidden}
.chtab th,.chtab td{padding:7px 11px;border-bottom:1px solid var(--rule-soft);text-align:left}
.chtab th{font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-3);background:var(--panel-2)}
.chtab .r{text-align:right}
.chtab tr:last-child td{border-bottom:none}
.chtab .delta{color:var(--ink);font-weight:600}.chtab .up{color:var(--ok)}.chtab .reread{color:var(--ink-3)}

/* Tests by category. The empty fifth box is the message, so it is styled to be read. */
.tgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(215px,1fr));gap:12px;margin-bottom:12px}
.tbox{padding:13px 15px;background:var(--panel);border:1px solid var(--rule);border-top:3px solid var(--ok);
border-radius:4px}
.tbad{border-top-color:var(--bad)}
.tempty{border-top-color:var(--bad);border-style:dashed;background:var(--panel-2)}
.tnum{font-size:26px;line-height:1;color:var(--ink)}
.tempty .tnum{color:var(--bad)}
.tof{font-size:14px;color:var(--ink-3)}
.tlab{margin-top:5px;font-size:13px;font-weight:600;color:var(--ink)}
.task{margin:7px 0 0;font-size:12px;color:var(--ink-2);line-height:1.6}
.twhy{margin:6px 0 0;font-size:11.5px;color:var(--ink-3);line-height:1.65}
.tfail{margin:7px 0 0;font-size:11.5px;color:var(--bad);line-height:1.6}

@media (max-width:720px){
  .chgrid,.freshrow{grid-template-columns:1fr}
  .nav{gap:0}
  .nav a{padding:5px 8px;font-size:11.5px}
}
.disc{margin-top:13px;padding:13px 15px;background:var(--panel-2);border:1px solid var(--rule);border-radius:4px;
color:var(--ink-2);font-size:12.5px}
</style>
<div class="wrap">
<header class="mast">
  <div class="kicker">Henren Framework + Empirical Context Layer</div>
  <h1>狠人的規則，配上它自己的歷史脈絡</h1>
  <p class="standfirst">每一格分成四塊：<b>觀測值</b>（數字是多少）、<b>歷史脈絡</b>（在自己的歷史裡多極端）、
  <b>狠人規則</b>（按他的原話有沒有觸發）、<b>訊號驗證</b>（有沒有人證明過這條規則有效）。
  這四件事永遠分開 —— 因為「他認為危險」和「數據證明危險」是兩個不同的主張，而目前
  <b>沒有任何一格通過統計驗證</b>。</p>
  <dl class="session">
    <div><dt>產生時間</dt><dd class="num">${esc(data.generated_at_et)}</dd></div>
    <div><dt>美股狀態</dt><dd>${esc(data.market_session.us_market)}</dd></div>
    <div><dt>${live ? '價格為' : '最近收盤'}</dt><dd class="num">${esc(px('^GSPC')?.asOf ?? '—')}${live ? ' 盤中' : ''}</dd></div>
    <div><dt>計算版本</dt><dd class="num">v${esc(data.calculation_version)} @ ${esc(data.code_commit)}</dd></div>
    <!-- This tested data.point_in_time for truthiness and printed 「是」, because the engine
         emits the STRING 'NOT_IMPLEMENTED' and every non-empty string is truthy. The page
         was claiming point-in-time was implemented directly underneath a footer explaining
         that it is not. A status field is never a boolean. -->
    <div><dt>Point-in-time</dt><dd>${data.point_in_time === 'IMPLEMENTED' ? '是'
      : `否 · <span class="num">${esc(data.point_in_time)}</span>`}</dd></div>
    <div><dt>SEC as-of 查詢</dt><dd>${data.as_of_query === 'TESTED' ? '已實測' : esc(data.as_of_query ?? '—')}</dd></div>
  </dl>
</header>

<nav class="nav">
  <a href="#today">今天</a><a href="#maturity">系統成熟度</a><a href="#changes">上次之後的變化</a>
  <a href="#triggers">規則已評估</a>${hold ? '<a href="#holdings">持股</a>' : ''}
  <a href="#nodecision">無可用讀數</a>${tests ? '<a href="#tests">測試在測什麼</a>' : ''}
</nav>

${goingDark.length ? `<section class="darkwarn">
  <div class="dwlab">即將失效</div>
  <p><b>${goingDark.length} 格讀數會在來源下一次發布之前先過期。</b>
  它們過期之後就不再參與規則評估，計數會跟著少 —— <b>而計數變少不代表風險變小，
  只代表那一格看不到了。</b>先在這裡講，是因為事後解釋「為什麼紅燈少了一個」永遠來不及。</p>
  <ul class="dwlist">${goingDark.map((g) => `<li>
    <b>${esc(g.label)}</b>
    <span class="dwdays">${g.sla_countdown.days_until_no_decision} 天後失效</span>
    <span class="dwwhy">目前判定 ${g.henren?.status ? RULE_LABEL[g.henren.status] : '不評估'}　·　
    來源每 ${g.sla_countdown.publication_period_days} 天發布一次</span></li>`).join('')}</ul>
</section>` : ''}

${summary}

<section id="maturity">
  <h2>System maturity</h2>
  <p class="h2sub">這套系統目前完成到哪一層</p>
  <p class="lede">這比任何免責聲明都準確。上面兩層已經建立，下面兩層還沒開始 ——
  <strong>可稽核不等於已驗證</strong>，而這個頁面的專業度只應該反映前者。</p>
  <ol class="ladder">
    ${data.maturity.map((m, i) => `<li class="rung rung-${m.state.toLowerCase()}">
      <span class="rungno num">${i + 1}</span>
      <span class="rungbody"><b>${esc(m.layer)}</b><span class="rungdetail">${esc(m.detail)}</span></span>
      <span class="rungstate">${{ ESTABLISHED: '已建立', IN_PROGRESS: '建立中', NOT_STARTED: '尚未開始' }[m.state]}</span>
    </li>`).join('')}
  </ol>

  <div class="counts">
    <div class="cnt"><b class="num">${t.evaluated}</b><span>規則已評估</span></div>
    <div class="cnt"><b class="num">${t.red ?? 0}</b><span>規則觸發</span></div>
    <div class="cnt"><b class="num">${t.no_decision}</b><span>無可用讀數</span></div>
    <div class="cnt cnt-zero"><b class="num">0</b><span>經統計驗證的訊號</span></div>
  </div>
  <p class="nocomp">${esc(data.no_composite_score)}</p>
</section>

${changesSection}

<section id="triggers">
  <h2>Framework Triggers</h2>
  <p class="h2sub">狠人規則已評估的 ${evaluated.length} 格</p>
  <p class="lede">這是<strong>規則評估</strong>，不是校準過的評分。紅色代表「按他的原話，這格觸發了」，
  不代表統計上已證明市場風險升高。標「門檻非原話」的格子，門檻是本系統設的，不是他講的。
  ${t.evaluated_on_superseded_period ? `其中 <strong>${t.evaluated_on_superseded_period}</strong> 格標示為
  「讀數已被更新的一季超過」—— 判定本身有效，但它成立在已經不是最新的期間上。` : ''}</p>
  <div class="grid">${evaluated.map(card).join('')}</div>
</section>

${holdingsSection}

<section id="nodecision">
  <h2>No Decision</h2>
  <p class="h2sub">沒有可用讀數的 ${undecided.length} 格</p>
  <p class="lede">資料逾期、過期或缺漏。這些格子<strong>不會被當成「中性」或「黃燈」</strong>，也不進任何計數。</p>
  <div class="grid">${undecided.map(card).join('')}</div>
  ${unbucketed.length ? `<p class="note blocker"><b>⚠️ 未分類的判定狀態：</b>
  ${unbucketed.map((g) => `${esc(g.label)}（${esc(g.decision)}）`).join('、')} ——
  這些格子的 decision 值不在本頁認得的清單裡。它們被印在這裡而不是被丟掉，
  因為上一次同樣的情況讓一整張卡片從頁面上消失，而總數還繼續數著它。</p>
  <div class="grid">${unbucketed.map(card).join('')}</div>` : ''}
</section>

${testSection}

<footer>
  <p><b>Canonical data flow</b>　<span class="num">FRED / SEC EDGAR / Yahoo → data/raw/ → gauges.mjs
  (calc v${esc(data.calculation_version)}) → data/gauges.json → render-dashboard.mjs → 本頁</span>。
  這個 renderer <b>不做任何金融計算</b> —— 沒有 YoY、沒有百分位、沒有中位數、沒有利差、沒有訊號邏輯。
  頁面上每個數字都是引擎算好的欄位。</p>
  <p><b>${esc(data.point_in_time_note)}</b></p>
  <div class="disc">研究工具，不是投資建議。不輸出買賣訊號、目標價、部位建議或綜合評分。
  所有訊號驗證狀態皆為 UNTESTED —— 這些門檻來自一位公開評論者，尚未經回測或樣本外檢驗。
  <br>仅作信息跟踪，不构成投资建议。</div>
</footer>
</div>`;

process.stdout.write(html);

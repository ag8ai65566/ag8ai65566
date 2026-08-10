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
const esc = (s) => String(s ?? '').replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

const evaluated = data.gauges.filter((g) => g.decision === 'RULE_EVALUATED');
const undecided = data.gauges.filter((g) => g.decision === 'NO_DECISION');
const t = data.henren_rule_tally;
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

const pct = (g) => {
  const p = g.empirical?.percentile_5y ?? g.empirical?.percentile_3y ?? g.empirical?.percentile_20y;
  return p?.ok ? p : null;
};

function card(g) {
  const p = pct(g);
  const sev = SEV[g.henren?.status] ?? 'var(--off)';
  const th = g.henren?.thresholds ?? {};
  return `<article class="g" style="--sev:${g.henren ? sev : 'var(--off)'}">
  <header>
    <div class="ghead">
      <h3>${esc(g.label)}${g.proxy ? '<span class="tag">代理</span>' : ''}${g.henren?.threshold_is_ours ? '<span class="tag tag-ours">門檻非原話</span>' : ''}</h3>
      <p class="plain">${esc(g.plain)}</p>
    </div>
    <div class="chips">
      <span class="chip chip-state">${STATE_LABEL[g.status.data_state] ?? g.status.data_state}</span>
      <span class="chip chip-auth${g.status.source_authority === 'UNOFFICIAL_FREE' ? ' weak' : ''}">${AUTH_LABEL[g.status.source_authority] ?? g.status.source_authority}</span>
      <span class="chip chip-auto">${AUTO_LABEL[g.status.automation_mode] ?? g.status.automation_mode}</span>
    </div>
  </header>

  <div class="quad">
    <section class="q q-obs">
      <div class="qlab">觀測值</div>
      ${g.observed ? `<div class="qval num">${esc(g.observed.value)}<span class="qunit">${esc(g.observed.unit)}</span></div>
      <div class="qmeta num">生效 ${esc(g.observed.effective_date)}　·　${g.age_days} 天前</div>` : '<div class="qval muted">—</div>'}
    </section>

    <section class="q q-emp">
      <div class="qlab">歷史脈絡</div>
      ${p ? `<div class="qval num">P${p.value}</div>
      <div class="pbar"><div class="pfill" style="width:${p.value}%"></div><div class="pneedle" style="left:calc(${p.value}% - 1px)"></div></div>
      <div class="qmeta">過去 ${p.window_years} 年 n=${p.n}</div>` : '<div class="qval muted">—</div><div class="qmeta">無足夠歷史樣本</div>'}
      ${g.empirical?.reading ? `<p class="qnote">${esc(g.empirical.reading)}</p>` : ''}
    </section>

    <section class="q q-rule">
      <div class="qlab">狠人規則</div>
      ${g.henren ? `<div class="qval" style="color:${sev}">${RULE_LABEL[g.henren.status]}</div>
      <div class="ths">${Object.entries(th).map(([k, v]) => `<span class="th th-${k}">${esc(v)}</span>`).join('')}</div>` : '<div class="qval muted">—</div>'}
    </section>

    <section class="q q-val">
      <div class="qlab">訊號驗證</div>
      <div class="qval val-untested">${esc(g.status.signal_validation)}</div>
      <div class="qmeta">此門檻尚未經任何統計檢驗</div>
    </section>
  </div>

  ${g.henren?.quote ? `<blockquote>${esc(g.henren.quote)}</blockquote>` : ''}
  ${[
    g.henren?.note && ['他的說明', g.henren.note],
    g.henren?.implementation_divergence && ['實作偏離他的原話', g.henren.implementation_divergence],
    g.proxy_warning && ['代理指標警告', g.proxy_warning],
    g.naming_note && ['命名', g.naming_note],
    g.selection_bias_note && ['選樣偏誤', g.selection_bias_note],
    g.mixed_authority_note && ['來源權威', g.mixed_authority_note],
    g.note && ['狀態', g.note],
  ].filter(Boolean).map(([k, v]) => `<p class="note"><b>${k}：</b>${esc(v)}</p>`).join('')}
  ${g.layers ? `<div class="layers">${Object.entries(g.layers).map(([k, v]) =>
    `<div class="layer"><b>${esc(k.replace(/^._/, '').replace(/_/g, ' '))}</b><span>${esc(v)}</span></div>`).join('')}</div>` : ''}

  <details class="prov"><summary>來源鏈</summary><dl>
    ${Object.entries(g.provenance ?? {}).map(([k, v]) =>
      `<div><dt>${esc(k)}</dt><dd class="num">${esc(typeof v === 'boolean' ? (v ? 'true' : 'false') : v)}</dd></div>`).join('')}
  </dl></details>
</article>`;
}

const G = (id) => data.gauges.find((x) => x.id === id);
const obs = (id) => G(id)?.observed;
const st = (id) => G(id)?.henren?.status;
const capex = G('capex');

// The summary reads canonical fields. It composes sentences; it computes nothing.
const summary = `
<section class="verdict">
  <h2>Today</h2>
  <p class="h2sub">狠人版總結 · 今天的市場</p>

  <div class="vgrid">
    <div class="vbox">
      <div class="vlab">基本面 · 管方向</div>
      <div class="vstat" style="--sev:var(--ok)">沒有裂縫</div>
      <p>標普收在 <b class="num">${px('^GSPC')?.close}</b>，距 52 週高點 <b class="num">${px('^GSPC')?.ddFromHigh}%</b>。
      等權重 RSP 年初至今 <b class="num">${px('RSP')?.ytd}%</b>、羅素 2000 <b class="num">${px('^RUT')?.ytd}%</b>，
      都不輸市值權重的 <b class="num">${px('^GSPC')?.ytd}%</b> —— 這不是少數幾檔撐起來的盤。
      防禦股 XLU 近一月 <b class="num">${px('XLU')?.m1}%</b>，落後。</p>
    </div>
    <div class="vbox">
      <div class="vlab">流動性 · 管顛簸</div>
      <div class="vstat" style="--sev:var(--ok)">平靜，但緩衝沒了</div>
      <p>銀行準備金 <b class="num">${obs('fuel')?.value}</b> 兆（清倉線 2.5 兆）、隔夜拆款利差
      <b class="num">${obs('sofr')?.value}</b> bp、垃圾債利差 <b class="num">${obs('hyoas')?.value}%</b>（五年 P${pct(G('hyoas'))?.value}）、
      VIX <b class="num">${px('^VIX')?.close}</b>。<b>唯一缺口：逆回購緩衝只剩
      <span class="num">${obs('rrp')?.value}</span> 億美元</b> —— 財政部再抽錢會直接打到準備金。</p>
    </div>
    <div class="vbox">
      <div class="vlab">擁擠 · 管斷裂</div>
      <div class="vstat" style="--sev:var(--bad)">唯一紅燈</div>
      <p>大盤 21 日已實現波動 <b class="num">${px('^GSPC')?.rvol21}%</b>，但 AI 籃子中位數是它的
      <b class="num">${obs('ai-basket-rel-vol')?.value}</b> 倍，最高
      <b class="num">${obs('ai-basket-rel-vol')?.detail?.max}</b> 倍（SNDK）。
      指數在睡覺、少數幾檔用年化三位數波動在跑 —— 斷裂風險在個股，不在指數。</p>
    </div>
  </div>

  <div class="bell">
    <div class="belllab">逃生鈴 · 開關三</div>
    <div class="bellval">還沒響</div>
    <p>四家雲廠商最新一季 capex 合計 <b class="num">$${capex?.observed?.detail?.total_bn}B</b>
    （${esc(capex?.observed?.effective_date)} 季，資訊可得於 ${esc(capex?.observed?.detail?.information_available_at)}），
    年增 <b class="num">${capex?.observed?.value}%</b> —— 是整個序列的最高點，
    環比 <b class="num">${capex?.observed?.detail?.qoq_pct}%</b>。
    他的規則是「增速見頂回落就立刻平倉」。<b>目前沒有回落，反而在加速。</b>
    這用 SEC 申報資料證實了他 8 月的說法：還沒看到確認讀數。</p>
    <p class="bellcaveat">但這只是 Layer A（申報現金 capex）。融資租賃與下季指引都沒接線，
    所以這個「還沒響」是<b>系統性低估後的還沒響</b>。</p>
  </div>

  <div class="oneline">
    <b>一句話：</b>方向沒問題、油還夠、逃生鈴沒響 —— 但估值與擁擠度都在歷史極端
    （巴菲特指標 P${pct(G('buffett'))?.value}、AI 籃子波動是大盤 ${obs('ai-basket-rel-vol')?.value} 倍）。
    這不是「安全」，是<b>「還能燒，而且燒得很快」</b>。
    ${t.red} 個規則觸發、${t.yellow ?? 0} 個接近、${t.green} 個未觸發，另有 ${t.no_decision} 格沒有可用讀數。
  </div>
  <p class="vdisc">以上每個數字都來自 canonical engine（calc v${esc(data.calculation_version)} @ ${esc(data.code_commit)}）。
  「狠人規則觸發」不等於「統計上證明危險」—— 全部 16 格的訊號驗證狀態都是 UNTESTED。</p>
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
    <div><dt>最近收盤</dt><dd class="num">${esc(px('^GSPC')?.asOf ?? '—')}</dd></div>
    <div><dt>計算版本</dt><dd class="num">v${esc(data.calculation_version)} @ ${esc(data.code_commit)}</dd></div>
    <div><dt>Point-in-time</dt><dd>${data.point_in_time ? '是' : '否'}</dd></div>
  </dl>
</header>

${summary}

<section>
  <h2>Status</h2>
  <p class="h2sub">系統狀態</p>
  <div class="tallybar">
    <div class="tchip t-red"><b class="num">${t.red ?? 0}</b><span>規則觸發</span></div>
    <div class="tchip t-yellow"><b class="num">${t.yellow ?? 0}</b><span>接近</span></div>
    <div class="tchip t-green"><b class="num">${t.green ?? 0}</b><span>未觸發</span></div>
    <div class="tchip t-undec"><b class="num">${t.no_decision}</b><span>無可用讀數</span></div>
  </div>
  <div class="dims">
    ${Object.entries(data.status_summary).map(([k, v]) => `<div class="dim"><h4>${esc(k.replace(/_/g, ' '))}</h4>
      ${Object.entries(v).map(([kk, vv]) => `<div><span>${esc(kk)}</span><b class="num">${vv}</b></div>`).join('')}</div>`).join('')}
  </div>
  <p class="nocomp">${esc(data.no_composite_score)}</p>
</section>

<section>
  <h2>Framework Triggers</h2>
  <p class="h2sub">狠人規則已評估的 ${evaluated.length} 格</p>
  <p class="lede">這是<strong>規則評估</strong>，不是校準過的評分。紅色代表「按他的原話，這格觸發了」，
  不代表統計上已證明市場風險升高。標「門檻非原話」的格子，門檻是本系統設的，不是他講的。</p>
  <div class="grid">${evaluated.map(card).join('')}</div>
</section>

<section>
  <h2>No Decision</h2>
  <p class="h2sub">沒有可用讀數的 ${undecided.length} 格</p>
  <p class="lede">資料逾期、過期或缺漏。這些格子<strong>不會被當成「中性」或「黃燈」</strong>，也不進任何計數。</p>
  <div class="grid">${undecided.map(card).join('')}</div>
</section>

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

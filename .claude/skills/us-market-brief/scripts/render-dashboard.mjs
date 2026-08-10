#!/usr/bin/env node
// Render the dashboard FROM gauges.json. Nothing is transcribed by hand.
//
//   NODE_USE_ENV_PROXY=1 node ../../henren-tape/scripts/gauges.mjs --json > /tmp/gauges.json
//   node render-dashboard.mjs /tmp/gauges.json > ../../../../reports/us-market-dashboard.html
//
// Two rules this file exists to enforce:
//   1. No composite score. There is no bubble number, no 0-100 index, no weighted blend.
//      None of them has been validated against a defined target, so none is rendered.
//   2. SCORED and NO_DECISION are rendered in separate blocks with different visual weight.
//      An undecided gauge must never read as a mild warning.

import { readFileSync } from 'node:fs';

const data = JSON.parse(readFileSync(process.argv[2] ?? '/dev/stdin', 'utf8'));
const esc = (s) => String(s ?? '').replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

const scored = data.gauges.filter((g) => g.decision === 'SCORED');
const undecided = data.gauges.filter((g) => g.decision === 'NO_DECISION');
const counts = ['green', 'yellow', 'red'].map((k) => data.tally[k] ?? 0);

const SEV = { green: 'var(--ok)', yellow: 'var(--warn)', red: 'var(--bad)' };
const LABEL = { green: '綠燈', yellow: '注意', red: '紅燈' };
const UNDECIDED_LABEL = {
  STALE: '資料過期', NOT_WIRED: '未接線', SOURCE_FAILURE: '來源失敗',
  DATE_MISMATCH: '日期不一致', MISSING: '資料缺漏', INSUFFICIENT_HISTORY: '歷史不足',
};

const pctOf = (g) => g.percentile_5y ?? g.percentile_3y ?? g.percentile_20y;

function meter(g) {
  const t = g.thresholds;
  if (!t) return '';
  const p = pctOf(g);
  const pv = Number.isFinite(p?.value) ? p.value : null;
  const bar = pv === null ? '' : `
    <div class="meter"><div class="fillbar" style="width:${pv}%"></div>
      <div class="needle" style="left:calc(${pv}% - 1.5px)"></div></div>
    <div class="meter-legend"><span>歷史最低</span>
      <span>此讀數在過去 ${p.window_years} 年落在 <b>第 ${pv} 百分位</b>（n=${p.n}）</span>
      <span>最高</span></div>`;
  return `<div class="meter-wrap">${bar}
    <div class="thresholds">${Object.entries(t).map(([k, v]) =>
      `<span class="th th-${k}">${esc(v)}</span>`).join('')}</div></div>`;
}

function prov(g) {
  const p = g.provenance;
  if (!p) return '';
  const auth = p.authority_level ?? '—';
  const warn = auth === 'UNOFFICIAL_FREE' || auth === 'NO_AUTHORITATIVE_SOURCE';
  return `<details class="prov"><summary>來源與時效</summary><dl>
    <div><dt>來源</dt><dd>${esc(p.source_id)} · <span class="${warn ? 'auth-warn' : 'auth-ok'}">${esc(auth)}</span></dd></div>
    <div><dt>資料集</dt><dd class="num">${esc(p.dataset)}</dd></div>
    <div><dt>生效日</dt><dd class="num">${esc(p.effective_date)}（${p.age_days} 天前，SLA ${p.acceptable_age_days} 天）</dd></div>
    <div><dt>時效狀態</dt><dd class="num">${esc(p.freshness_status)}</dd></div>
    <div><dt>抓取時間</dt><dd class="num">${esc(p.retrieved_at ?? '手動輸入')}</dd></div>
    <div><dt>計算</dt><dd>${esc(p.transformation)} <span class="num">v${esc(p.transformation_version ?? '—')}</span></dd></div>
    <div><dt>原始回應 hash</dt><dd class="num">${esc(p.raw_hash ?? '—')}</dd></div>
    <div><dt>point-in-time</dt><dd>${p.point_in_time_capable ? '是' : '<b>否</b> — 此來源只提供最新修訂版，不可用於回測'}</dd></div>
  </dl></details>`;
}

const notes = (g) => [
  g.interpretation_note && ['判讀', g.interpretation_note],
  g.alignment_note && ['時間對齊', g.alignment_note],
  g.naming_note && ['命名', g.naming_note],
  g.selection_bias_note && ['選樣偏誤', g.selection_bias_note],
  g.proxy_warning && ['代理指標警告', g.proxy_warning],
  g.percentile_note && ['分位數樣本', g.percentile_note],
  g.mixed_authority && ['來源權威', g.mixed_authority],
  g.context && ['背景', g.context],
].filter(Boolean).map(([k, v]) => `<p class="note"><b>${k}：</b>${esc(v)}</p>`).join('');

const scoredCard = (g) => `
  <article class="g" style="--sev:${SEV[g.status] ?? 'var(--ink-3)'}">
    <header>
      <div><h3>${esc(g.label)}</h3><p class="plain">${esc(g.plain)}</p></div>
      <div class="readout">
        <div class="val num">${esc(g.value)}<span class="unit">${esc(g.unit ?? '')}</span></div>
        <span class="pill"><span class="dot"></span>${LABEL[g.status] ?? esc(g.status)}</span>
      </div>
    </header>
    ${meter(g)}${notes(g)}${prov(g)}
  </article>`;

const undecidedCard = (g) => `
  <article class="g undec">
    <header>
      <div><h3>${esc(g.label ?? g.id)}</h3>${g.plain ? `<p class="plain">${esc(g.plain)}</p>` : ''}</div>
      <div class="readout">
        <div class="val num muted">—</div>
        <span class="pill pill-undec">${UNDECIDED_LABEL[g.status] ?? esc(g.status)}</span>
      </div>
    </header>
    ${g.note ? `<p class="note">${esc(g.note)}</p>` : ''}
    ${g.blocker ? `<p class="note blocker"><b>接線阻礙：</b>${esc(g.blocker)}</p>` : ''}
    ${g.would_have_been !== undefined ? `<p class="note"><b>若強行相除會得到：</b><span class="num">${g.would_have_been}</span> — 本系統不採用，因為它沒有定義。</p>` : ''}
    ${g.proxy_replacement ? `<p class="note"><b>應改用：</b>${esc(g.proxy_replacement)}</p>` : ''}
    ${prov(g)}
  </article>`;

const html = `<title>美股儀表板 · 判斷標誌與其來源</title>
<style>
:root{--ground:#EDEFF2;--panel:#F8F9FB;--panel-2:#E7EAEF;--rule:#CDD3DC;--rule-soft:#DFE4EA;
--ink:#171C24;--ink-2:#4A5464;--ink-3:#78828F;--brass:#A8781C;--ok:#1F7A54;--warn:#B36A12;--bad:#B03047;
--ok-bg:#DDEEE6;--warn-bg:#F6E7CF;--bad-bg:#F4DDE1;--off:#C3CAD3;
--shadow:0 1px 2px rgba(23,28,36,.06),0 8px 24px -12px rgba(23,28,36,.16);}
@media(prefers-color-scheme:dark){:root:not([data-theme="light"]){--ground:#0C1017;--panel:#141A23;--panel-2:#1B222D;
--rule:#2A3341;--rule-soft:#212936;--ink:#E8ECF2;--ink-2:#A3AEBD;--ink-3:#737F8E;--brass:#D9A43F;
--ok:#4CBF8B;--warn:#E3A44E;--bad:#E86A80;--ok-bg:#14312A;--warn-bg:#33280F;--bad-bg:#371A22;--off:#3A4453;
--shadow:0 1px 2px rgba(0,0,0,.4),0 10px 30px -14px rgba(0,0,0,.7);}}
:root[data-theme="dark"]{--ground:#0C1017;--panel:#141A23;--panel-2:#1B222D;--rule:#2A3341;--rule-soft:#212936;
--ink:#E8ECF2;--ink-2:#A3AEBD;--ink-3:#737F8E;--brass:#D9A43F;--ok:#4CBF8B;--warn:#E3A44E;--bad:#E86A80;
--ok-bg:#14312A;--warn-bg:#33280F;--bad-bg:#371A22;--off:#3A4453;
--shadow:0 1px 2px rgba(0,0,0,.4),0 10px 30px -14px rgba(0,0,0,.7);}
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--ink);font-size:16px;line-height:1.65;
font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang TC","Noto Sans TC","Microsoft JhengHei",system-ui,sans-serif;
-webkit-font-smoothing:antialiased}
.num{font-family:ui-monospace,"SF Mono",Menlo,Consolas,monospace;font-variant-numeric:tabular-nums}
.wrap{max-width:1000px;margin:0 auto;padding:32px 20px 96px}
.mast{border-bottom:2px solid var(--ink);padding-bottom:18px;margin-bottom:24px}
.kicker{font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--brass);font-weight:700;margin-bottom:10px}
h1{font-size:clamp(25px,4.4vw,38px);line-height:1.15;margin:0 0 12px;letter-spacing:-.02em;font-weight:750;text-wrap:balance}
.standfirst{font-size:16px;color:var(--ink-2);margin:0;max-width:64ch}
.session{margin-top:18px;background:var(--panel);border:1px solid var(--rule);border-radius:4px;padding:14px 16px;
display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:10px 20px;box-shadow:var(--shadow)}
.session div{font-size:12.5px}.session dt{color:var(--ink-3);font-size:11px;letter-spacing:.05em;text-transform:uppercase}
.session dd{margin:2px 0 0;color:var(--ink);font-weight:600}
.tallybar{display:flex;gap:10px;flex-wrap:wrap;margin:22px 0 8px}
.tchip{display:flex;align-items:baseline;gap:7px;background:var(--panel);border:1px solid var(--rule);
border-radius:4px;padding:10px 14px;box-shadow:var(--shadow)}
.tchip b{font-size:22px;font-weight:760;letter-spacing:-.02em}
.tchip span{font-size:12.5px;color:var(--ink-2)}
.t-green b{color:var(--ok)}.t-yellow b{color:var(--warn)}.t-red b{color:var(--bad)}.t-undec b{color:var(--ink-3)}
.nocomp{background:var(--panel-2);border:1px solid var(--rule);border-left:4px solid var(--brass);border-radius:4px;
padding:14px 16px;font-size:13.5px;color:var(--ink-2);margin:14px 0 0}
.nocomp b{color:var(--ink)}
h2{font-size:12px;letter-spacing:.15em;text-transform:uppercase;color:var(--ink-3);font-weight:700;
margin:44px 0 4px;display:flex;align-items:center;gap:12px}
h2::after{content:"";flex:1;height:1px;background:var(--rule)}
.h2sub{font-size:21px;font-weight:700;margin:0 0 6px;letter-spacing:-.015em}
.lede{color:var(--ink-2);margin:0 0 18px;max-width:66ch;font-size:15px}
.grid{display:flex;flex-direction:column;gap:12px}
.g{background:var(--panel);border:1px solid var(--rule);border-left:4px solid var(--sev,var(--off));
border-radius:4px;padding:18px;box-shadow:var(--shadow)}
.g.undec{border-left-style:dashed;border-left-color:var(--off);background:var(--panel-2)}
.g header{display:flex;justify-content:space-between;align-items:flex-start;gap:18px;flex-wrap:wrap}
.g h3{margin:0;font-size:17px;font-weight:700;letter-spacing:-.01em}
.plain{margin:5px 0 0;font-size:13.5px;color:var(--ink-2);max-width:60ch;line-height:1.55}
.readout{text-align:right;flex:none;display:flex;flex-direction:column;align-items:flex-end;gap:6px}
.val{font-size:26px;font-weight:750;letter-spacing:-.02em;color:var(--sev,var(--ink))}
.val.muted{color:var(--ink-3)}
.unit{font-size:12px;color:var(--ink-3);font-weight:500;margin-left:5px}
.pill{display:inline-flex;align-items:center;gap:5px;font-size:11.5px;font-weight:700;padding:3px 10px;
border-radius:100px;color:var(--sev);background:var(--panel-2)}
.dot{width:7px;height:7px;border-radius:50%;background:currentColor}
.pill-undec{color:var(--ink-3);background:var(--panel);border:1px dashed var(--rule)}
.meter-wrap{margin:16px 0 0}
.meter{position:relative;height:8px;border-radius:2px;background:var(--panel-2);border:1px solid var(--rule-soft);overflow:hidden}
.fillbar{position:absolute;inset:0 auto 0 0;background:var(--sev,var(--off));opacity:.32}
.needle{position:absolute;top:-4px;bottom:-4px;width:3px;background:var(--ink);border-radius:1px;box-shadow:0 0 0 2px var(--panel)}
.meter-legend{display:flex;justify-content:space-between;gap:12px;font-size:11px;color:var(--ink-3);margin-top:7px}
.meter-legend b{color:var(--ink-2)}
.thresholds{display:flex;flex-wrap:wrap;gap:6px;margin-top:10px}
.th{font-size:11.5px;padding:2px 8px;border-radius:3px;color:var(--ink-2);background:var(--panel-2);border:1px solid var(--rule-soft)}
.th-green{color:var(--ok);background:var(--ok-bg)}.th-yellow{color:var(--warn);background:var(--warn-bg)}
.th-red{color:var(--bad);background:var(--bad-bg)}
.note{font-size:13px;color:var(--ink-2);margin:12px 0 0;line-height:1.6;max-width:74ch}
.note b{color:var(--ink)}
.note.blocker{border-left:2px solid var(--warn);padding-left:10px}
.prov{margin-top:14px;font-size:12.5px}
.prov summary{cursor:pointer;color:var(--brass);font-weight:600;font-size:12px;letter-spacing:.04em}
.prov dl{margin:10px 0 0;display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:6px 20px}
.prov dt{color:var(--ink-3);font-size:11px;letter-spacing:.04em;text-transform:uppercase}
.prov dd{margin:1px 0 0;color:var(--ink-2);font-size:12.5px;word-break:break-all}
.auth-warn{color:var(--warn);font-weight:700}.auth-ok{color:var(--ok);font-weight:700}
footer{margin-top:52px;padding-top:20px;border-top:1px solid var(--rule);font-size:12.5px;color:var(--ink-3);line-height:1.7}
.disc{margin-top:14px;padding:14px 16px;background:var(--panel-2);border:1px solid var(--rule);border-radius:4px;
color:var(--ink-2);font-size:13px}
</style>
<div class="wrap">
<header class="mast">
  <div class="kicker">狠人判斷標誌 · 每一格都標明來源與時效</div>
  <h1>${scored.length} 個儀表有讀數，${undecided.length} 個沒有</h1>
  <p class="standfirst">這一版拿掉了所有綜合分數。沒有泡沫指數、沒有 0–100 分、沒有加權合成 ——
  那些數字沒有經過任何可重現的驗證，所以不報。下面是各個組成，以及每一格的資料從哪來、什麼時候有效、
  是不是已經過期。<b>沒有讀數的儀表用虛線框單獨列出，不會混進燈號計數。</b></p>
  <dl class="session">
    <div><dt>產生時間</dt><dd class="num">${esc(data.generated_at_local)}</dd></div>
    <div><dt>UTC</dt><dd class="num">${esc(data.generated_at)}</dd></div>
    <div><dt>Point-in-time</dt><dd>${data.point_in_time ? '是' : '否（僅最新修訂版）'}</dd></div>
    <div><dt>Schema</dt><dd class="num">v${esc(data.schema_version)}</dd></div>
  </dl>
</header>

<div class="tallybar">
  <div class="tchip t-green"><b class="num">${counts[0]}</b><span>綠燈</span></div>
  <div class="tchip t-yellow"><b class="num">${counts[1]}</b><span>注意</span></div>
  <div class="tchip t-red"><b class="num">${counts[2]}</b><span>紅燈</span></div>
  <div class="tchip t-undec"><b class="num">${undecided.length}</b><span>無讀數 · 不計分</span></div>
</div>
<p class="nocomp"><b>為什麼沒有總分。</b>${esc(data.no_composite_score)}
把 ${scored.length} 個性質不同的指標加權成一個數字，需要先定義它預測什麼、再用樣本外資料驗證權重。
兩件事都還沒做，所以任何總分都只是把不確定性藏起來。</p>

<section>
  <h2>Scored</h2>
  <p class="h2sub">有讀數的 ${scored.length} 個</p>
  <p class="lede">刻度條顯示的是<strong>百分位</strong>，不是絕對門檻 —— 因為市場結構會變，寫死的數字會悄悄過期。
  門檻值仍然列在下方，那是他講的原始規則。</p>
  <div class="grid">${scored.map(scoredCard).join('')}</div>
</section>

<section>
  <h2>No decision</h2>
  <p class="h2sub">沒有讀數的 ${undecided.length} 個</p>
  <p class="lede">資料缺漏、過期、來源失敗或日期對不上。這些格子<strong>不會被當成「中性」或「黃燈」</strong> ——
  把「不知道」轉換成「風險普通」是這類系統最常見也最危險的錯誤。</p>
  <div class="grid">${undecided.map(undecidedCard).join('')}</div>
</section>

<footer>
  <p><b>資料來源註冊表</b>　<span class="num">config/data-sources.json</span> ——
  每個資料集的權威等級、發布頻率、預期延遲、可接受時效、修訂政策都在那裡定義。
  每一格的「來源與時效」可以展開查看，含原始回應的 hash。</p>
  <p><b>${esc(data.point_in_time_note)}</b></p>
  <div class="disc">這是研究筆記，不是投資建議。本系統不輸出買賣訊號、不給目標價、不輸出綜合評分。
  它只做一件事：把判斷標準攤開成可以查證的數字，並且在數字不可信的時候明講。
  <br>仅作信息跟踪，不构成投资建议。</div>
</footer>
</div>`;

process.stdout.write(html);

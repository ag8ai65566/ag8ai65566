#!/usr/bin/env node
// Pull a US-market snapshot from Yahoo Finance's public chart endpoint.
//
//   node market-snapshot.mjs                 # default ticker set, table to stdout
//   node market-snapshot.mjs --json          # machine-readable
//   node market-snapshot.mjs --add MU,META   # extra tickers
//   node market-snapshot.mjs --days 2        # also print the last N daily bars per ticker
//
// Behind an HTTPS proxy, run with NODE_USE_ENV_PROXY=1 so node:fetch honours HTTPS_PROXY.
//
// Every number this prints is a real close from the endpoint. Nothing is modelled or
// estimated — if a field is missing it prints `null`, and the analysis must say so.

const GROUPS = {
  index: ['^GSPC', '^IXIC', '^DJI', '^RUT', 'RSP'],
  vol: ['^VIX', '^VVIX', '^MOVE'],
  rates: ['^TNX', '^TYX', '^IRX', 'TLT'],
  credit: ['HYG', 'LQD', 'JNK'],
  fx_cmd: ['DX-Y.NYB', 'GC=F', 'CL=F', 'BTC-USD'],
  ai: ['NVDA', 'MU', 'AVGO', 'AMD', 'TSM', 'SMH', 'MSFT', 'META', 'GOOGL', 'AMZN', 'AAPL', 'PLTR'],
  defensive: ['XLU', 'XLP', 'XLV'],
};

const args = process.argv.slice(2);
const flag = (name) => args.includes(name);
const value = (name, dflt) => {
  const i = args.indexOf(name);
  return i >= 0 && args[i + 1] ? args[i + 1] : dflt;
};

const tickers = [...new Set([
  ...Object.values(GROUPS).flat(),
  ...String(value('--add', '')).split(',').filter(Boolean),
])];

const groupOf = (t) => Object.entries(GROUPS).find(([, list]) => list.includes(t))?.[0] ?? 'extra';

async function chart(symbol) {
  const url = `https://query1.finance.yahoo.com/v8/finance/chart/${encodeURIComponent(symbol)}`
    + `?range=1y&interval=1d`;
  const res = await fetch(url, { headers: { 'User-Agent': 'Mozilla/5.0' } });
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  const body = await res.json();
  const r = body?.chart?.result?.[0];
  if (!r) throw new Error(body?.chart?.error?.description ?? 'no result');

  const ts = r.timestamp ?? [];
  const q = r.indicators?.quote?.[0] ?? {};
  const bars = ts
    .map((t, i) => ({ t, close: q.close?.[i], high: q.high?.[i], low: q.low?.[i], volume: q.volume?.[i] }))
    .filter((b) => Number.isFinite(b.close));

  return { meta: r.meta, bars };
}

const pct = (a, b) => (Number.isFinite(a) && Number.isFinite(b) && b !== 0 ? ((a / b - 1) * 100) : null);
const round = (x, n = 2) => (Number.isFinite(x) ? Number(x.toFixed(n)) : null);
const iso = (t) => new Date(t * 1000).toISOString().slice(0, 10);

// Largest single-day gain in the trailing window — used to check claims like "MU +18.4% in a day".
function biggestDay(bars, lookback = 90) {
  const w = bars.slice(-lookback);
  let best = null;
  for (let i = 1; i < w.length; i++) {
    const chg = pct(w[i].close, w[i - 1].close);
    if (chg !== null && (best === null || chg > best.chg)) best = { chg, date: iso(w[i].t) };
  }
  return best;
}

function metrics(symbol, { meta, bars }) {
  const n = bars.length;
  const last = bars[n - 1];
  const at = (back) => bars[n - 1 - back]?.close;
  const ma = (len) => {
    if (n < len) return null;
    return bars.slice(-len).reduce((s, b) => s + b.close, 0) / len;
  };

  const closes = bars.map((b) => b.close);
  const hi52 = Math.max(...closes);
  const lo52 = Math.min(...closes);
  const hiIdx = closes.lastIndexOf(hi52);

  // Annualised realised vol from daily log returns.
  const rvol = (len) => {
    if (n < len + 1) return null;
    const w = bars.slice(-(len + 1));
    const rets = w.slice(1).map((b, i) => Math.log(b.close / w[i].close));
    const mean = rets.reduce((s, x) => s + x, 0) / rets.length;
    const varr = rets.reduce((s, x) => s + (x - mean) ** 2, 0) / (rets.length - 1);
    return Math.sqrt(varr * 252) * 100;
  };

  const jan1 = new Date(Date.UTC(new Date(last.t * 1000).getUTCFullYear(), 0, 1)).getTime() / 1000;
  const ytdBase = bars.find((b) => b.t >= jan1)?.close ?? bars[0].close;

  return {
    symbol,
    group: groupOf(symbol),
    name: meta?.shortName ?? meta?.symbol ?? symbol,
    asOf: iso(last.t),
    close: round(last.close, 2),
    d1: round(pct(last.close, at(1))),
    d5: round(pct(last.close, at(5))),
    m1: round(pct(last.close, at(21))),
    m3: round(pct(last.close, at(63))),
    ytd: round(pct(last.close, ytdBase)),
    y1: round(pct(last.close, bars[0].close)),
    hi52: round(hi52, 2),
    hi52Date: iso(bars[hiIdx].t),
    lo52: round(lo52, 2),
    ddFromHigh: round(pct(last.close, hi52)),
    vs50dma: round(pct(last.close, ma(50))),
    vs200dma: round(pct(last.close, ma(200))),
    rvol21: round(rvol(21)),
    rvol63: round(rvol(63)),
    bestDay90: biggestDay(bars, 90),
    bars: Number(value('--days', 0)) > 0
      ? bars.slice(-Number(value('--days', 0))).map((b) => ({ date: iso(b.t), close: round(b.close, 2) }))
      : undefined,
  };
}

const out = [];
const failed = [];
for (const t of tickers) {
  try {
    out.push(metrics(t, await chart(t)));
  } catch (e) {
    failed.push({ symbol: t, error: String(e.message ?? e) });
  }
}

if (flag('--json')) {
  console.log(JSON.stringify({ generatedAt: new Date().toISOString(), rows: out, failed }, null, 2));
} else {
  const cols = ['symbol', 'asOf', 'close', 'd1', 'd5', 'm1', 'm3', 'ytd', 'ddFromHigh', 'vs50dma', 'vs200dma', 'rvol21'];
  const pad = (s, w) => String(s ?? '').padStart(w);
  console.log(cols.map((c) => pad(c, c === 'symbol' ? 10 : 11)).join(''));
  let lastGroup = null;
  for (const r of out) {
    if (r.group !== lastGroup) { console.log(`-- ${r.group}`); lastGroup = r.group; }
    console.log(cols.map((c) => pad(r[c], c === 'symbol' ? 10 : 11)).join(''));
  }
  console.log('\n-- biggest single day, trailing 90 sessions');
  for (const r of out) {
    if (r.bestDay90) console.log(`${pad(r.symbol, 10)}  ${r.bestDay90.date}  ${pad(round(r.bestDay90.chg), 8)}%`);
  }
  if (failed.length) console.log('\n-- failed\n' + failed.map((f) => `${f.symbol}: ${f.error}`).join('\n'));
}

---
name: us-market-brief
description: Produce a current US equity market read by running one live price snapshot through two lenses — 一个狠人's three-layer 基本面/流動性/擁擠 frame (henren-tape) for market state, and Serenity's chokepoint + Buffett-gate method (serenity-method) for anything single-name. Trigger on "給我一個當前美股分析", "現在美股怎麼看", "美股 brief", "current US market analysis", "AI 泡沫現在什麼狀態", or any request for a dated market state-of-play. Every number comes from the snapshot script; nothing is estimated. Research and education only, never a buy or sell instruction.
---

# US Market Brief

One snapshot, two lenses, a dated file. **State of play, not a forecast.**

## Workflow

### 1. Pull the tape first
```bash
NODE_USE_ENV_PROXY=1 node scripts/market-snapshot.mjs --json > /tmp/snapshot.json
NODE_USE_ENV_PROXY=1 node scripts/market-snapshot.mjs            # readable table
```
Indices, vol, rates, credit, FX/commodities, the AI cohort, defensives. Per ticker:
returns across six horizons, drawdown from the 52w high, distance from the 50/200dma,
21- and 63-day realised vol, and the largest single-day gain in 90 sessions.

Add names with `--add TICKER,TICKER`. **Do this before reading any commentary** — the
order matters, because a snapshot read after the narrative is a snapshot read through it.

### 2. Score the three layers — `henren-tape`
Direction from breadth and trend, turbulence from vol and credit, rupture risk from
single-name realised vol against index vol. Then the 洗盤/葬禮 call on any drawdown in
play. Full procedure in `../henren-tape/SKILL.md`.

### 3. Single names — `serenity-method`
Any ticker the brief wants to say something about goes through the chokepoint frame and
the Buffett gate, every field starting at `unverified`. Momentum is not a moat. For a
theme rather than a ticker, `../serenity-bottleneck-hunter/SKILL.md` reverse-maps the
supply chain instead.

### 4. Check the numbers that are being repeated
If the brief is prompted by someone's call, check it against the tape and log the
result in `../henren-tape/references/claim-checks.md` — hits and misses both. This is
the habit that keeps the frame a tool rather than a fandom.

### 5. Write it to a dated file
`reports/us-market-YYYY-MM-DD.md`, structured as:

1. **一句話** — the state of play in one sentence.
2. **三層計分** — a row per layer: reading, the specific numbers, verdict.
3. **本週的不對稱** — where the layers disagree. This is the whole point of the brief.
4. **單一標的** — Serenity blocks, defaulting to `研究地图`.
5. **會推翻這個判斷的東西** — named, checkable falsifiers. Not hedging — specific prints.
6. **數據來源與日期** — as-of date, source, what could not be verified.

## Hard rules

- **Every number traces to the snapshot.** No recalled prices, no estimated levels. A
  field the script could not fetch is reported as unavailable, never filled in.
- **Date the close.** Yahoo's last close is often the prior session; say which.
- **Name the falsifiers.** A read with no stated way to be wrong is a horoscope.
- **Never a buy/sell instruction or price target.** Layer diagnosis, asymmetry, and
  things to watch.
- **Say what was not checkable.** Unverified claims stay labelled unverified.

---
仅作信息跟踪，不构成投资建议。 / For information tracking only; not investment advice.

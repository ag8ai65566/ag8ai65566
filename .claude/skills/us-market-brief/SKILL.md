---
name: us-market-brief
description: The one-button US market read. Runs a live price snapshot plus 一个狠人's own judgment gauges, then scores them through three lenses — his 基本面/流動性/擁擠 three-layer frame (henren-tape), Serenity's chokepoint + Buffett gate (serenity-method), and Anthropic's equity-research skills — and writes both a dated brief and a plain-language dashboard. Trigger on "給我一個當前美股分析", "現在美股怎麼看", "跑一次儀表板", "泡沫到什麼程度", "美股 brief", "current US market analysis", or any request for a dated market state-of-play. Every number comes from a fetch; nothing is estimated. Research and education only, never a buy or sell instruction.
---

# US Market Brief

One command, three lenses, two artefacts. **State of play, not a forecast.**

## Workflow

### 1. Pull the tape and the gauges first
```bash
NODE_USE_ENV_PROXY=1 node scripts/market-snapshot.mjs --json > /tmp/snapshot.json
NODE_USE_ENV_PROXY=1 node ../henren-tape/scripts/gauges.mjs --json > /tmp/gauges.json
NODE_USE_ENV_PROXY=1 node scripts/market-snapshot.mjs            # readable table
NODE_USE_ENV_PROXY=1 node ../henren-tape/scripts/gauges.mjs      # readable panel
```
The snapshot covers indices, vol, rates, credit, FX/commodities, the AI cohort and
defensives — returns across six horizons, drawdown from the 52w high, distance from the
50/200dma, 21/63-day realised vol, largest single-day gain in 90 sessions. Add names
with `--add TICKER,TICKER`; **always add whatever the user actually holds.**

`gauges.mjs` scores his named markers off FRED and Yahoo and flags the manual ones as
stale past their refresh window.

**Do both before reading any commentary** — a snapshot read after the narrative is a
snapshot read through it.

### 1b. Then read the news, and check it against what you just pulled
Search for what is being said this week, then treat every claim in it as a hypothesis
the snapshot can test. Report where the coverage and the tape disagree — that gap is
usually the most useful paragraph in the brief.

### 2. Score the three layers — `henren-tape`
Direction from breadth and trend, turbulence from vol and credit, rupture risk from
single-name realised vol against index vol. Then the 洗盤/葬禮 call on any drawdown in
play. Full procedure in `../henren-tape/SKILL.md`.

### 3. Single names — `serenity-method` and `equity-research`
Any ticker the brief speaks to goes through Serenity's chokepoint frame and the Buffett
gate, every field starting at `unverified`. Momentum is not a moat. For a theme rather
than a ticker, `../serenity-bottleneck-hunter/SKILL.md` reverse-maps the supply chain.

For the sell-side view — earnings quality, catalyst calendars, thesis tracking — the
vendored `../equity-research/` skills (Anthropic, Apache-2.0) carry `earnings-analysis`,
`earnings-preview`, `catalyst-calendar`, `thesis-tracker`, `sector-overview` and
`morning-note`. Deliberately a **third, differently-biased lens**: Serenity hunts
un-priced bottlenecks, 狠人 reads positioning and liquidity, equity-research works the
fundamentals the way a covering analyst would. When all three agree, say so. When they
disagree, that disagreement is the finding — report it rather than averaging it away.

### 4. Check the numbers that are being repeated
If the brief is prompted by someone's call, check it against the tape and log the
result in `../henren-tape/references/claim-checks.md` — hits and misses both. This is
the habit that keeps the frame a tool rather than a fandom.

### 5. Write both artefacts
**The brief** — `reports/us-market-YYYY-MM-DD.md`:

1. **一句話** — the state of play in one sentence.
2. **三層計分** — a row per layer: reading, the specific numbers, verdict.
3. **本週的不對稱** — where the layers disagree. This is the whole point of the brief.
4. **單一標的** — Serenity blocks, defaulting to `研究地图`.
5. **會推翻這個判斷的東西** — named, checkable falsifiers. Not hedging — specific prints.
6. **數據來源與日期** — as-of date, source, what could not be verified.

**The dashboard** — `reports/us-market-dashboard.html`, then publish it as an artifact.
Refresh the same file so the URL stays stable. It is the plain-language surface: every
gauge carries a one-line explanation a 13-year-old could follow, a meter showing where
the current reading sits between his thresholds, and an explicit `stale` state for any
manual gauge past its refresh window. **Never render a stale gauge as current** — a
gauge you cannot see is a gauge that is off, and the dashboard has to say so.

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

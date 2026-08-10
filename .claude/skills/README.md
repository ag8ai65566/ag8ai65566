# Skills

Agent skills available to Claude Code in this repo. Claude picks one up automatically
when a request matches its `description`; you can also name it (`用 Serenity 框架分析
NVDA`, `給我一個當前美股分析`).

## Market research

| Skill | What it does | Origin |
| --- | --- | --- |
| `serenity-method` | Apply Serenity (@aleabitoreddit)'s method to any ticker: critical-chokepoint discovery, first-principles value-chain decomposition, a Buffett quality gate where every field starts `unverified`, narrative-vs-fundamentals hygiene | Vendored, MIT |
| `serenity-bottleneck-hunter` | Theme → reverse-mapped supply chain → overlooked upstream bottleneck candidates, with price-verification and report-lint scripts | Vendored, MIT |
| `equity-research` | Sell-side workflow: earnings analysis and previews, catalyst calendars, thesis tracking, sector overviews, morning notes, initiating coverage | Vendored, Apache-2.0 |
| `henren-tape` | 一个狠人 (@henren778)'s three-layer frame: 基本面管方向 / 流動性管顛簸 / 擁擠管斷裂, his 二波打法五步三開關, and the 洗盤-vs-葬禮 test. Gauges scored from FRED + live prices | Written here |
| `us-market-brief` | The one-button read: runs the snapshot and the gauges, scores them through all three lenses, writes a dated brief and a plain-language dashboard | Written here |

The three lenses are deliberately biased differently, and that is the point:
`serenity-method` hunts **un-priced bottlenecks**, `henren-tape` reads **positioning and
liquidity**, `equity-research` works the **fundamentals** the way a covering analyst
would. `us-market-brief` runs all three over one dataset — and when they disagree, the
disagreement is the finding, not something to average away.

### Attribution

The two `serenity-*` skills are vendored from public MIT-licensed repositories, licences
included in each directory:

- `serenity-method` — from [lanfuli/aleabito-serenity-skills](https://github.com/lanfuli/aleabito-serenity-skills)
  (MIT, © 2026 lanfuli). That repo also ships `follow-aleabito` and `serenity-radar`,
  **not vendored here** because both need an X API bearer token to do anything. Add them
  from upstream if you get one.
- `serenity-bottleneck-hunter` — from [Mrjie7205/serenity-bottleneck-hunter](https://github.com/Mrjie7205/serenity-bottleneck-hunter)
  (MIT, © 2026 Mrjie7205).
- `equity-research` — from Anthropic's [financial-services](https://github.com/anthropics/financial-services)
  repo, `plugins/vertical-plugins/equity-research` (Apache-2.0). That repo also ships
  agent plugins for modelling, pitching, GL reconciliation and month-end close; only the
  equity-research bundle is vendored here.

The two `serenity-*` skills are independent educational distillations of a public
trader's methodology, not affiliated with or endorsed by Serenity. `henren-tape` is
likewise an unaffiliated reading of a public YouTube channel — see its
`references/corpus.md` for exactly what is transcript-backed and what is title-only, and
`references/claim-checks.md` for how his claims score against the tape (including a
correction where this repo's own first reading got a row backwards).

### Running the scripts

Both fetch scripts use `node:fetch`, which ignores `HTTPS_PROXY` unless told to:

```bash
NODE_USE_ENV_PROXY=1 node .claude/skills/us-market-brief/scripts/market-snapshot.mjs
NODE_USE_ENV_PROXY=1 node .claude/skills/henren-tape/scripts/gauges.mjs
NODE_USE_ENV_PROXY=1 node .claude/skills/henren-tape/scripts/fetch-channel.mjs
```

`gauges.mjs` needs no API key — it reads FRED's public CSV endpoint and Yahoo Finance.
Markers with no free feed live in `henren-tape/references/manual-gauges.json`; refresh
them by hand and they stop reporting as stale.

`serenity-bottleneck-hunter`'s scripts are Python and want `EODHD_API_KEY` (falling back
to `yfinance`) — see its `.env.example`.

### Standing caveat

These skills produce research notes. They never emit buy/sell instructions or price
targets, every quality field starts at `unverified`, and every number is expected to
trace to a fetched price. 仅作信息跟踪，不构成投资建议。

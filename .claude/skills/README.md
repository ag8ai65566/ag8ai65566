# Skills

Agent skills available to Claude Code in this repo. Claude picks one up automatically
when a request matches its `description`; you can also name it (`用 Serenity 框架分析
NVDA`, `給我一個當前美股分析`).

## Market research

| Skill | What it does | Origin |
| --- | --- | --- |
| `serenity-method` | Apply Serenity (@aleabitoreddit)'s method to any ticker: critical-chokepoint discovery, first-principles value-chain decomposition, a Buffett quality gate where every field starts `unverified`, narrative-vs-fundamentals hygiene | Vendored, MIT |
| `serenity-bottleneck-hunter` | Theme → reverse-mapped supply chain → overlooked upstream bottleneck candidates, with price-verification and report-lint scripts | Vendored, MIT |
| `henren-tape` | 一个狠人 (@henren778)'s three-layer frame: 基本面管方向 / 流動性管顛簸 / 擁擠管斷裂, plus the 洗盤-vs-葬禮 and 分層塌方 tests. Layers scored from live prices | Written here |
| `us-market-brief` | Runs one live snapshot through both lenses and writes a dated brief to `reports/` | Written here |

`serenity-method` and `henren-tape` complement each other on purpose: one asks *which
company is a real bottleneck*, the other asks *which layer of the market is moving right
now*. `us-market-brief` is the two of them over a single dataset.

### Attribution

The two `serenity-*` skills are vendored from public MIT-licensed repositories, licences
included in each directory:

- `serenity-method` — from [lanfuli/aleabito-serenity-skills](https://github.com/lanfuli/aleabito-serenity-skills)
  (MIT, © 2026 lanfuli). That repo also ships `follow-aleabito` and `serenity-radar`,
  **not vendored here** because both need an X API bearer token to do anything. Add them
  from upstream if you get one.
- `serenity-bottleneck-hunter` — from [Mrjie7205/serenity-bottleneck-hunter](https://github.com/Mrjie7205/serenity-bottleneck-hunter)
  (MIT, © 2026 Mrjie7205).

Both are independent educational distillations of a public trader's methodology, not
affiliated with or endorsed by Serenity. `henren-tape` is likewise an unaffiliated
reading of a public YouTube channel — see its `references/corpus.md` for exactly how
much of it is sourced and how much is missing.

### Running the scripts

Both fetch scripts use `node:fetch`, which ignores `HTTPS_PROXY` unless told to:

```bash
NODE_USE_ENV_PROXY=1 node .claude/skills/us-market-brief/scripts/market-snapshot.mjs
NODE_USE_ENV_PROXY=1 node .claude/skills/henren-tape/scripts/fetch-channel.mjs
```

`serenity-bottleneck-hunter`'s scripts are Python and want `EODHD_API_KEY` (falling back
to `yfinance`) — see its `.env.example`.

### Standing caveat

These skills produce research notes. They never emit buy/sell instructions or price
targets, every quality field starts at `unverified`, and every number is expected to
trace to a fetched price. 仅作信息跟踪，不构成投资建议。

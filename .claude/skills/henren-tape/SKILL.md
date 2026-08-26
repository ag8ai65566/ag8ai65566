---
name: henren-tape
description: Read the US market through 一个狠人 (@henren778)'s three-layer pricing frame — 基本面管方向 (fundamentals set direction), 流動性管顛簸 (liquidity sets turbulence), 擁擠管斷裂 (crowding sets rupture) — plus his shakeout-vs-funeral (洗盤/葬禮) and layered-collapse (分層塌方) tests. Every layer is scored from live prices, never from the narrative. Trigger on "用狠人的框架", "三層定價", "洗盤還是葬禮", "現在美股怎麼看", "AI 泡沫是不是要崩", "擁擠度", "second-wave setup", or any request to judge whether a drawdown is positioning or regime change. Research and education only, never a buy or sell instruction.
---

# Henren Tape — 三層定價框架

A market-state lens distilled from the trading videos of **一个狠人 / @henren778**. It
answers one question: *when the tape moves, which layer moved?* Getting that right is
the difference between adding to a shakeout and averaging into a regime change.

> **Provenance.** The two core trading videos are now **transcript-backed** — his
> 五步三開關, bottom-confirmation checklist and September triggers are in
> `references/playbook.md` in his own terms. The rest of the channel's markets entries
> are still title-only (`references/corpus.md`). His checkable claims are scored in
> `references/claim-checks.md` — but read that file's opening block before its table: the
> sample comes from his own recap video, so it selects for hits and **no hit-rate can be
> inferred from it**. It establishes that his mechanisms are visible in the tape, nothing
> more. The frame earns its place here because its three layers are *separable and
> independently measurable*, not because anyone has a scorecard. Borrow the structure,
> re-derive every number. Forward scoring: `data/predictions.jsonl`.

## The frame

> **基本面管方向、流動性管顛簸、擁擠管斷裂 —— 一個失控拖垮全部。**

| Layer | Governs | What it looks like when it breaks |
| --- | --- | --- |
| **基本面 · Fundamentals** | *Direction* — where price goes over quarters | Earnings and demand actually roll over. Slow, and it re-rates everything |
| **流動性 · Liquidity** | *Turbulence* — how violent the path is | Funding tightens, dealers step back, vol-of-vol rises. Price gaps with no news |
| **擁擠 · Crowding** | *Rupture* — where the discontinuity lands | One-way positioning unwinds into an empty book. Local, fast, and violent |

The three run on different clocks, and **the layer that moves is rarely the layer the
headline blames**. The market's core failure mode is reading a crowding rupture as a
fundamental verdict — selling the bottom of a flush — or reading a fundamental
deterioration as "just positioning" and buying a falling knife.

## Workflow

### Step 1 — Get the tape before the narrative
```bash
NODE_USE_ENV_PROXY=1 node ../us-market-brief/scripts/market-snapshot.mjs --json
NODE_USE_ENV_PROXY=1 node scripts/gauges.mjs --json     # his own markers, scored live
```
Never score a layer from commentary you have read. Score it from closes, then read
commentary to see who is wrong.

`gauges.mjs` scores his named markers against sources registered in
`config/data-sources.json`: the fuel switch (`WRESBAL` level **and** its 4/13-week
velocity, since his rule is "快速跌破" — a rate, not only a level), SOFR−IORB, TGA, RRP,
HY OAS, NFCI, the M2-vs-Nasdaq gap, the Buffett ratio, and AI-basket relative volatility.

Four rules it enforces, and none of them is optional:

- **Missing or stale ⇒ `NO_DECISION`.** Never neutral, never yellow, never zero. Turning
  "we don't know" into "risk looks moderate" is the failure this system most has to avoid.
  Undecided gauges are listed separately and excluded from every count.
- **Freshness is per dataset.** GDP lagging a quarter is by design; a daily series lagging
  a week is broken. One global day-count cannot tell those apart.
- **Percentiles alongside thresholds.** His cut-offs are asserted values with no measured
  false-positive rate. Every gauge also reports where it sits in its own history, because
  a fixed number silently expires when market structure moves.
- **Provenance on every value** — source, authority level, effective date, age, retrieval
  time, transformation, and the hash of the raw response it came from.

Markers with no free feed (FINRA margin debt, 0DTE share, index concentration, insider
ratio, forward P/E, hyperscaler capex QoQ) sit in `references/manual-gauges.json` against
contracts in the registry. A gauge you cannot see is a gauge that is off, and it must say
so rather than showing a colour.

### Step 2 — Score each layer independently

**基本面 · direction.** Index level vs its own 52-week high and 200dma; breadth
(equal-weight `RSP` vs cap-weight `^GSPC`, and `^RUT`); whether defensives (`XLU`,
`XLP`, `XLV`) lead or lag. *Broad participation with defensives lagging = direction is
up, whatever the drawdown in any one theme.*

**流動性 · turbulence.** `^VIX` and `^VVIX`; `^MOVE` for bond vol; credit via `HYG`,
`JNK`, `LQD` drawdown from highs; the long end via `^TNX`, `^TYX`, `TLT`; `DX-Y.NYB`.
*Credit is the honest one.* Equity vol lies during melt-ups; high yield holding its
level while equities gap is near-proof the move is positioning, not funding.

**擁擠 · rupture risk.** This is the layer people skip and it is where the money is
lost. Look at **realised vol on the leaders, not the index**: `rvol21` per name in the
snapshot. Then 1-month and 3-month gains on the crowded names, distance above the
50dma, and how much of the recent index gain is a handful of tickers.

> The tell: **index vol calm while single-name realised vol runs 3–7x the index.** That
> gap *is* the crowding. It says the market has concentrated its risk-taking into a few
> names, and those names — not the index — carry the rupture.

### Step 3 — 洗盤 or 葬禮?
The signature call. For a drawdown in progress:

| | 洗盤 · shakeout | 葬禮 · funeral |
| --- | --- | --- |
| Which layer moved | Crowding, sometimes liquidity | Fundamentals |
| Credit | Unbothered | Widening with equities |
| Breadth | Narrow damage, index holds | Broad, defensives bid |
| Fundamental news | Nothing changed | Guidance, demand, or capex actually cut |
| Recovery shape | Violent, days not months | Lower highs for quarters |

His own worked case: June–July 2026 took `SMH` −24.6% and `MU` −39.1% while `^GSPC`
never made a lower low. Credit never widened. Nothing fundamental changed. Shakeout —
and it retraced in three weeks. See `references/claim-checks.md`.

**分層塌方 · layered collapse.** The corollary for a late-cycle theme: a bubble in a
market this broad does not detonate at index level, it collapses one layer at a time —
the most-levered cohort first, while the index prints highs. Local −25% inside a market
at record highs *is* the bubble deflating, on schedule. Do not wait for a bang.

### Step 4 — State the asymmetry, not a prediction
Close with which layer is loaded and what would falsify the read. Concretely: *the
index is doing X, the crowded cohort is doing Y, the gap between them is the risk, and
here is the specific print that would flip this.* Never a price target, never a buy or
sell.

### Step 5 — Run the playbook switches
`references/playbook.md` holds his 二波打法五步三開關 verbatim, plus the
bottom-confirmation checklist and the September liquidity triggers. The three switches
are the actionable part and `gauges.mjs` scores two of them automatically:

| 開關 | 讀什麼 | 動作線 |
| --- | --- | --- |
| 1 燃料 | `WRESBAL` 準備金 | 無危機下快速跌破 **$2.5T** → 無條件清倉 |
| 2 點火 | 選擇權偏度倒掛 + 現貨抗跌（腳本用 VIX 期限結構代理） | 倒掛出現 → 二波點火倒數 |
| 3 逃生 | 雲廠商 capex **環比**增速 | **見頂回落 → 立刻平倉**，不看當期獲利 |

Switch 3 is the one that actually flips the fundamental layer, it is manual, and it is
the one people skip. Never report a read as complete without stating switch 3's status.

## Cross-checks from the rest of the channel

Apply these as hygiene on any conclusion:

- **止損簇是燃料.** ~3% of displayed single-stock quotes execute (<1% for QQQ); retail
  is ~2% of driving force. Visible liquidity is a screen, and clustered stops are the
  fuel a flush burns. *A low that reverses violently the next session is the signature —
  MU bottomed 2026-07-29 and printed +18.36% on 07-30.*
- **勝率51%就夠.** Edge is expected value over many draws, not being right once. Any
  read that only pays if a single call lands is not a strategy.
- **賭徒破產定理.** Sizing cannot rescue wrong direction. If the fundamental layer has
  actually turned, position size is not the lever.
- **AI capex vs revenue.** ~$725B capex against ~$70B revenue is the fundamental-layer
  clock on the AI trade. It is a *direction* input on a multi-quarter horizon — not a
  timing signal, and not a reason to read this week's tape as the top.
- **TACO 週期.** Policy rhetoric mean-reverts on a measurable period. Treat headline
  shocks as a liquidity/crowding event with a half-life, not a fundamental input.

## Hard rules

- **Score layers from prices.** Every claim in the output traces to a number in the
  snapshot, or it is labelled unverified.
- **Re-derive his numbers.** They are load-bearing when checkable and inflated when
  rhetorical (`腰斬` for a −33.5% drawdown). Cite the tape, not the title.
- **Never fabricate in-video content.** What is transcript-backed lives in
  `references/playbook.md`; what is title-only is marked as such in `references/corpus.md`.
  Never read a title's claim without its referent — that is how the claim log got a row
  backwards.
- **Separate the channel's politics from its market work.** Most of the channel is China
  commentary. This skill uses the trading videos; do not import the political framing
  into a market call.
- **No buy/sell instructions, no price targets.** Layer diagnosis and asymmetry only.

## Pairs with

`serenity-method` — this skill says *which layer is moving and how violent the path is*;
`serenity-method` says *which company is a real bottleneck worth owning through it*.
`us-market-brief` runs both against one snapshot. Use them together: a crowding rupture
in a name that survives the Buffett gate is an opportunity; the same rupture in a name
that fails it is just a rupture.

---
仅作信息跟踪，不构成投资建议。 / For information tracking only; not investment advice.

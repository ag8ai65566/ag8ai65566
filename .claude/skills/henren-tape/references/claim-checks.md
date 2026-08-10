# Claim log — @henren778's checkable market claims vs the tape

Every row was checked against Yahoo Finance daily closes on 2026-08-10 (last close
2026-08-07) using `../../us-market-brief/scripts/market-snapshot.mjs`. Rerun it before
relying on any of this; numbers move.

The point of this file is **calibration, not fandom**. A framework is worth borrowing
in proportion to how its author's falsifiable statements hold up. Keep scoring new ones
here, including the misses.

## Verified

| Claim | Tape | Verdict |
| --- | --- | --- |
| 納指洗完近一成 | ^IXIC 27,093.90 (2026-06-02) → 24,442.94 (2026-07-29) = **−9.78%** | ✅ "近一成" is accurate to two decimals |
| 二波窗口鎖死 7月底8月初 | Nasdaq bottomed **2026-07-29**; +9.20% since, SMH +15.56%, NVDA +17.87%, MU +18.75% | ✅ The window was called before the fact and the low landed inside it |
| 美光單日暴拉 18.4% | MU **+18.36% on 2026-07-30** — the session after the low | ✅ Correct to one decimal |
| 道指標普齊創新高 | ^GSPC closed at its 52w high 2026-08-07 (0.00% off); ^DJI 52w high 2026-08-05, −0.57% off on 8/7 | ✅ S&P exact; Dow within half a percent of a two-day-old record |
| 鬼故事是洗盤不是葬禮 | Index drawdown −9.78% and fully recovered; SMH −24.62% and back to −12.89% off its high | ✅ A flush inside an intact uptrend, which is what 洗盤 means |
| 泡沫分層塌方，不是巨響崩盤 | SMH −24.62% and MU −39.10% June→July **while ^GSPC never broke to a new low** and now prints records | ✅ Damage stayed local; no index-level rupture |

## Overstated

| Claim | Tape | Verdict |
| --- | --- | --- |
| Meta 砸448億美元回購照樣**腰斬** | META peak 790.00 (2025-08-12) → trough 525.72 (2026-03-27) = **−33.5%**; now 592.10 = −25.1% off | ⚠️ Directionally right, magnitude inflated. 腰斬 means −50%; the worst was −33.5%. The *shape* of his argument survives — a $44.8B buyback did not stop a large drawdown — but the number is rhetoric |

## Not checkable here

| Claim | Why |
| --- | --- |
| 垃圾股一個月暴漲27倍 | No ticker named in the title; the `#GameStop` hashtag hints but does not identify it |
| 最安全的英國國債被血洗 | Yahoo serves no usable gilt-yield series through this proxy. IGLT.L (gilt ETF) is only −0.72% over 3m, so any bloodbath was a single-day or long-bond event this proxy cannot see |
| 五步三開關 / any in-video reasoning | Title-only corpus — see `corpus.md` |

## How to read this scorecard

Six of seven checkable market claims land, several to the decimal, including a
**pre-registered timing window** — that is a genuinely hard thing to do and it is why
the framework in `SKILL.md` is worth using as a lens.

It is not a reason to treat the next call as true. The one miss is instructive about the
failure mode: when a number serves the rhetoric (腰斬), it inflates. So the working rule
for this skill is **borrow the structure, re-derive every number**. The framework tells
you which layer to look at; the tape tells you what the layer is doing.

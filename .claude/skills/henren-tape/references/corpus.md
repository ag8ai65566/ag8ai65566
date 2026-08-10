# 一个狠人 (@henren778) — US-market corpus

Channel ID `UCJAPsTtcJJWGk8e-_CJL8TQ`. Regenerate the full list with
`node scripts/fetch-channel.mjs`.

**Provenance warning, read this first.** Every entry below is reconstructed from the
**public title and hashtags only**. No transcript has been ingested — see
`scripts/fetch-channel.mjs --transcript-help` for why, and for how to add them. His
titles are unusually load-bearing (they state the thesis, the numbers, and the call),
which is what makes a title-only corpus usable at all, but a title is a claim, not an
argument. Anywhere the framework below needs a step he actually walks through in the
video, it is marked `【缺逐字稿】`.

The channel is mostly China-politics commentary. These are the trading/markets entries.

## The two the user singled out

### `MrnjBdgQPLU` · 2026-08-10 · 二波復盤
> 一個月前全網喊AI泡沫要崩，我說鬼故事是洗盤不是葬禮，二波窗口鎖死7月底8月初！對賬：納指洗完近一成，道指標普齊創新高，美光單日暴拉18.4%！復盤釘死，二波打法五步三開關全套交付

Hashtags: `#AI泡沫 #美股 #納斯達克 #美光 #輝達 #聯準會 #洗盤 #流動性 #泡沫經濟`

What the title asserts:
- The June–July AI drawdown was a **shakeout (洗盤), not a funeral (葬禮)** — a
  positioning flush inside an intact trend, not a regime change.
- He pre-committed to a **second-wave window of late-July / early-August**.
- Scoreboard: Nasdaq washed out ~10%, Dow and S&P at new highs, Micron +18.4% in a day.
- Deliverable: a **「二波打法五步三開關」** — a five-step second-wave playbook with three
  gating switches. `【缺逐字稿】` The five steps and three switches are named only in the
  video. Do not invent them. Ask the user for the transcript before claiming to apply it.

### `Mtbfh5XA6D0` · 2026-08-09 · 三層定價
> 崩盤那天基本面什麼都沒變！最安全的英國國債被血洗、Meta砸448億美元回購照樣腰斬、垃圾股一個月暴漲27倍，同一個原理：基本面管方向、流動性管顛簸、擁擠管斷裂，一個失控拖垮全部！

Hashtags: `#股市崩盤 #英國國債 #Meta #GameStop #流動性危機 #軋空 #量化交易 #資產定價 #去槓桿`

This one states its framework outright, which is why it anchors the whole skill:

> **基本面管方向、流動性管顛簸、擁擠管斷裂 —— 一個失控拖垮全部。**
> Fundamentals govern *direction*. Liquidity governs *turbulence*. Crowding governs
> *rupture*. Let any one layer run out of control and it drags down the other two.

The three worked examples in the title are each a case of one layer detaching from the
others: a gilt selloff with no change in UK credit quality (liquidity), a
buyback-supported mega-cap falling anyway (crowding beats fundamentals), a junk name up
27x in a month (pure crowding/squeeze). `【缺逐字稿】` for how he sizes each layer.

## Other markets entries on the channel

| ID | Title gist | What it contributes |
| --- | --- | --- |
| `TUt6ZwOoP7M` | 量化不是算命：勝率只有51%怎麼成印鈔機 | Expected value over prediction; algos weigh, they don't forecast; retail wants to be right once, an algo can be wrong 100k times |
| `6V5dlBcfCnY` | 止損為什麼總死在最低點 | Cites SEC data: ~3% of displayed single-stock quotes actually execute, <1% for QQQ; retail ≈2% of driving force; **stop-loss clusters are free fuel** |
| `BBeLGBchxxA` | 美股美債結算上鏈 | Removing netting shrinks capacity ~100x; market makers withdraw at the worst second — a structural liquidity argument |
| `CVKuShIQoxw` | 蘋果告OpenAI挖角、Anthropic洩露 | AI capex ~$725B vs ~$70B revenue; **泡沫不會巨響崩盤，只會分層塌方** (layered collapse, not one bang) |
| `GYMyDFwNULk` | 賭徒破產定理 | Wrong direction + enough draws → ruin regardless of bankroll; sizing cannot rescue direction |
| `-ygfl-fSZxQ` | 川普 TACO 交易、傅里葉週期 | Rhetoric-to-climbdown has a measurable period (min ~10 min); policy noise is tradable as a cycle, not as news |
| `fI1BMeoZl0M` | 1688 英國國債 40 倍 | Credible commitment compresses rates and expands wealth; the state-capacity lens on asset prices |

## Members-only content

The user asked for the channel's paid-membership US-market videos. Those are **not
retrievable here and were not retrieved** — they sit behind a paid membership, and
scraping past that is neither possible from this container nor appropriate. If the user
holds a membership, route 2 in `--transcript-help` (yt-dlp with their own browser
cookies, run on their own machine) is the way to pull them, and the results can be filed
into `references/transcripts/` and folded into this corpus.

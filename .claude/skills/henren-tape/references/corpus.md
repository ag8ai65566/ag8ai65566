# 一个狠人 (@henren778) — US-market corpus

Channel ID `UCJAPsTtcJJWGk8e-_CJL8TQ`. Regenerate the full list with
`node scripts/fetch-channel.mjs`.

**Provenance, read this first.** Entries are marked **【逐字稿】** or **【僅標題】**.

The two core trading videos are transcript-backed as of 2026-08-10 — the user supplied
them directly, and everything they contain is distilled in `playbook.md`. Everything
else on this page is still reconstructed from **public titles and hashtags only**,
because `/watch` pages serve a bot check from datacenter IPs
(`scripts/fetch-channel.mjs --transcript-help`).

His titles are unusually load-bearing, which is what makes a title-only entry usable at
all. It is still not enough: **a title is a claim with its referent stripped off.** The
first version of `claim-checks.md` scored his 腰斬 line against Meta *today* and marked
it exaggerated; the transcript showed he was describing Meta in **2021–23**, which fell
−76.7% — the opposite error. Treat every 【僅標題】 row below as a lead, not a finding.

The channel is mostly China-politics commentary. These are the trading/markets entries.

## The two the user singled out

### `MrnjBdgQPLU` · 2026-08-10 · 二波復盤 **【逐字稿】**
> 一個月前全網喊AI泡沫要崩，我說鬼故事是洗盤不是葬禮，二波窗口鎖死7月底8月初！對賬：納指洗完近一成，道指標普齊創新高，美光單日暴拉18.4%！復盤釘死，二波打法五步三開關全套交付

Hashtags: `#AI泡沫 #美股 #納斯達克 #美光 #輝達 #聯準會 #洗盤 #流動性 #泡沫經濟`

What the title asserts:
- The June–July AI drawdown was a **shakeout (洗盤), not a funeral (葬禮)** — a
  positioning flush inside an intact trend, not a regime change.
- He pre-committed to a **second-wave window of late-July / early-August**.
- Scoreboard: Nasdaq washed out ~10%, Dow and S&P at new highs, Micron +18.4% in a day.
- Deliverable: the **「二波打法五步三開關」** — now transcript-backed and written out in
  full in **`playbook.md`**, along with his five-point bottom-confirmation checklist, the
  思科悖論 argument for switching from profit levels to the capex second derivative, and
  the three mechanical bids (相對收益考核 / 被動 ETF 飛輪 / Gamma 擠壓) that explain why
  Wall Street cannot stop.

### `Mtbfh5XA6D0` · 2026-08-09 · 三層定價 **【逐字稿】**
> 崩盤那天基本面什麼都沒變！最安全的英國國債被血洗、Meta砸448億美元回購照樣腰斬、垃圾股一個月暴漲27倍，同一個原理：基本面管方向、流動性管顛簸、擁擠管斷裂，一個失控拖垮全部！

Hashtags: `#股市崩盤 #英國國債 #Meta #GameStop #流動性危機 #軋空 #量化交易 #資產定價 #去槓桿`

This one states its framework outright, which is why it anchors the whole skill:

> **基本面管方向、流動性管顛簸、擁擠管斷裂 —— 一個失控拖垮全部。**
> Fundamentals govern *direction*. Liquidity governs *turbulence*. Crowding governs
> *rupture*. Let any one layer run out of control and it drags down the other two.

The three worked examples are each a case of one layer detaching from the others, and
the transcript names all three: **UK LDI gilts 2022** (liquidity — margin calls forced
pension funds to sell the safest, most-liquid, highest-leveraged asset first),
**Meta 2021–23** (fundamentals — a $44.8B buyback provides order-flow depth but cannot
offset FCF halving from $38.4B to $18.4B; the stock fell −76.7%), and **GameStop 2021**
(crowding — short interest above 100% of float, and a short has no symmetric ceiling the
way a long has a zero floor).

Two further mechanisms from the transcript worth carrying:
- **回購是替空頭墊市價衝擊成本.** A buyback bid sitting at the offer lets a short build a
  large position with almost no slippage. Price looks unnaturally stable while short
  positioning accumulates underneath; when the authorisation runs out, the sell pressure
  that never left hits an empty book at once.
- **越安全的資產越先被賣.** In a liquidity event the first thing sold is not the worst
  asset but the *most liquid* one — which is also, structurally, the most leveraged.

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

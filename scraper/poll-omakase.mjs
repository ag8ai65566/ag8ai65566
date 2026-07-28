#!/usr/bin/env node
/**
 * Read every OMAKASE restaurant's published booking state and record it.
 *
 *   node poll-omakase.mjs            # all OMAKASE shops
 *   node poll-omakase.mjs ac366431   # just these slugs
 *
 * Run this on a schedule — daily is right. 次回枠の受付開始日時 is not a rule that
 * can be computed once and reused: it moves every month, the time of day differs
 * per restaurant (08:00, 13:00, 15:00 and 23:00 among the five tracked here), and
 * a shop may answer 未定. Nothing derived from a formula would have got those
 * right, and a reading taken in July is worthless for a trip next spring.
 *
 * Two files come out of this, both under data/ (gitignored):
 *   booking-state.json   latest reading per shop — what the app is built from
 *   booking-state.jsonl  every reading ever taken, appended
 *
 * The history is the part that answers questions a single snapshot can't: whether
 * this shop always releases on the 1st, whether its hour ever moves, how long the
 * window stays open. That is why every reading is kept rather than overwritten.
 */
import fs from "node:fs/promises";
import path from "node:path";
import readline from "node:readline/promises";
import { contextFor, closeBrowser, setHeadful, saveState } from "./lib/browser.mjs";
import { login, isLoggedIn, readBookingState } from "./lib/omakase.mjs";

/* Headless by default — this is meant to run unattended. `--headed` opens a
   window for a run someone is watching, which is what you want the first time
   and whenever Cloudflare wants a checkbox ticked. */
const HEADED = process.argv.includes("--headed");
setHeadful(HEADED);

const HERE = process.cwd();
const PLATFORMS = path.join(HERE, "platforms.json");
const SEED = path.join(HERE, "observed-seed.json");
const OUT_LATEST = path.join(HERE, "..", "data", "booking-state.json");
const OUT_HISTORY = path.join(HERE, "..", "data", "booking-state.jsonl");

const readJson = async (f, fallback = {}) => {
  try { return JSON.parse(await fs.readFile(f, "utf8")); } catch { return fallback; }
};
const realKeys = o => Object.entries(o).filter(([k]) => !k.startsWith("_"));

/** slug → { slug, url, name } for every shop booked through OMAKASE. */
async function targets() {
  const out = new Map();

  /* Shops that also have a Tabelog record. */
  for (const [, p] of realKeys(await readJson(PLATFORMS))) {
    const url = p.bookingSource === "omakase" ? p.bookingUrl
      : p.alt && p.alt.source === "omakase" ? p.alt.url : null;
    if (!url) continue;
    const slug = url.split("/").pop();
    out.set(slug, { slug, url, name: p.name });
  }

  /* Shops that exist only on OMAKASE — acá has no Tabelog page in the list. */
  for (const [slug, s] of realKeys(await readJson(SEED))) {
    if (out.has(slug)) continue;
    out.set(slug, { slug, url: s.url || `https://omakase.in/r/${slug}`, name: s.name });
  }
  return [...out.values()];
}

const only = process.argv.slice(2).filter(a => !a.startsWith("-"));
let list = await targets();
if (only.length) list = list.filter(t => only.includes(t.slug));
if (!list.length) { console.error("nothing to poll"); process.exit(2); }

const ctx = await contextFor("omakase");

try {
  await login(ctx);
} catch (err) {
  /* With a window open, a challenge or an odd login form is something the person
     watching can clear in seconds. Unattended, there is nobody to ask, so fail. */
  if (!HEADED) throw err;
  console.error(`\n自動登入失敗 / login failed: ${err.message}`);
  const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
  await rl.question("請在打開的視窗裡自己登入 OMAKASE，完成後按 Enter… ");
  rl.close();
  if (!await isLoggedIn(ctx)) { console.error("仍未登入，中止。"); process.exit(1); }
  await saveState(ctx, "omakase");
}

const latest = await readJson(OUT_LATEST);
const history = [];
let ok = 0, failed = 0;

for (const t of list) {
  try {
    const state = await readBookingState(ctx, t.url);
    /* Keep the name and slug on the row so the history stands alone. */
    const row = { slug: t.slug, name: t.name, ...state };
    latest[t.slug] = row;
    history.push(row);
    ok++;

    const when = state.nextOpenAt || state.nextOpenAtRaw || "—";
    const extra = state.raffle && state.raffle.applyUntil
      ? `  抽選応募締切 ${state.raffle.applyUntil}` : "";
    console.log(`✓ ${t.name || t.slug}  ${state.acceptingNow ? "予約可" : "枠なし"}  次回 ${when}${extra}`);
  } catch (err) {
    failed++;
    console.error(`✗ ${t.name || t.slug} — ${err.message}`);
  }
}

await closeBrowser();
await fs.mkdir(path.dirname(OUT_LATEST), { recursive: true });
await fs.writeFile(OUT_LATEST, JSON.stringify(latest, null, 2) + "\n", "utf8");
if (history.length)
  await fs.appendFile(OUT_HISTORY, history.map(r => JSON.stringify(r)).join("\n") + "\n", "utf8");

console.log(`\npolled ${ok} ok, ${failed} failed → ${path.relative(HERE, OUT_LATEST)}`);
process.exit(failed && !ok ? 1 : 0);

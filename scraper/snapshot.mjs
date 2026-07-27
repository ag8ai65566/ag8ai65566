#!/usr/bin/env node
/**
 * Take one availability snapshot of every tracked restaurant and append it to
 * ../data/availability.jsonl. Meant to run once a day, unattended.
 *
 *   node snapshot.mjs                 # every restaurant in data/restaurants.json
 *   node snapshot.mjs 13157208 ...    # just these ids
 *   node snapshot.mjs --horizon 120   # look this many days ahead (default 90)
 *
 * The per-source probes below return the shape history.mjs expects. Only the
 * Tabelog one is written out; OMAKASE, TableCheck and TableAll need a logged-in
 * session and their calendar markup can't be read from here yet, so they throw
 * a clear "not implemented" instead of silently recording an empty day — an
 * empty day is indistinguishable from "sold out" once it's in the history, and
 * that would poison the sell-out statistics permanently.
 */
import fs from "node:fs/promises";
import path from "node:path";
import { contextFor, closeBrowser, open } from "./lib/browser.mjs";
import { append } from "./lib/history.mjs";

const IN = path.join(process.cwd(), "..", "data", "restaurants.json");

const argv = process.argv.slice(2);
const horizonIdx = argv.indexOf("--horizon");
const HORIZON = horizonIdx >= 0 ? Number(argv[horizonIdx + 1]) : 90;
const onlyIds = argv.filter(a => /^\d+$/.test(a));

/** Dates we care about: today .. today+HORIZON, in JST. */
function horizonDates() {
  const out = [];
  const now = new Date();
  for (let i = 0; i <= HORIZON; i++) {
    const d = new Date(now.getTime() + i * 864e5);
    const jst = new Date(d.toLocaleString("en-US", { timeZone: "Asia/Tokyo" }));
    out.push(`${jst.getFullYear()}-${String(jst.getMonth() + 1).padStart(2, "0")}-${String(jst.getDate()).padStart(2, "0")}`);
  }
  return out;
}

const PROBES = {
  /**
   * Tabelog's seat-availability calendar lives on the shop page's booking panel.
   * Selectors here follow the long-standing `rstdtl-vacancy` markup and are
   * UNVERIFIED — this environment cannot reach tabelog.com. First live run must
   * confirm them; if the calendar yields nothing the probe throws rather than
   * recording every date as unavailable.
   */
  async tabelog(ctx, r) {
    const page = await open(ctx, `${r.tabelog}yoyaku/`);
    try {
      const cells = await page.$$eval(
        ".rstdtl-vacancy__date, .vacancy-calendar__date, [data-vacancy-date]",
        ns => ns.map(n => ({
          date: n.getAttribute("data-vacancy-date") || n.getAttribute("data-date") || "",
          state: (n.getAttribute("data-vacancy-status") || n.className || "").toLowerCase(),
          text: (n.textContent || "").trim(),
        }))
      );
      if (!cells.length) throw new Error("no calendar cells matched — selectors need updating");
      const wanted = new Set(horizonDates());
      return cells
        .filter(c => wanted.has(c.date))
        .map(c => ({
          diningDate: c.date,
          anyAvailable: !/(満席|full|unavailable|disabled|×)/.test(c.state + c.text),
          slots: [],
        }));
    } finally {
      await page.close();
    }
  },

  async omakase() { throw new Error("omakase probe not implemented — needs a live logged-in page to read the calendar from"); },
  async tablecheck() { throw new Error("tablecheck probe not implemented — needs a live logged-in page to read the calendar from"); },
  async tableall() { throw new Error("tableall probe not implemented — needs a live logged-in page to read the calendar from"); },
};

let restaurants;
try {
  restaurants = JSON.parse(await fs.readFile(IN, "utf8"));
} catch {
  console.error(`no ${path.relative(process.cwd(), IN)} yet — run \`node import.mjs <url>...\` first`);
  process.exit(2);
}
if (onlyIds.length) restaurants = restaurants.filter(r => onlyIds.includes(r.id));
if (!restaurants.length) { console.error("nothing to snapshot"); process.exit(2); }

const ts = new Date().toISOString();
const rows = [];
let ok = 0, failed = 0;

for (const r of restaurants) {
  const source = r.bookingSource || r.source || "tabelog";
  const probe = PROBES[source];
  if (!probe) { console.error(`✗ ${r.id} — no probe for source "${source}"`); failed++; continue; }
  let ctx;
  try {
    ctx = await contextFor(source);
    const found = await probe(ctx, r);
    for (const f of found) rows.push({ ts, restaurantId: r.id, source, ...f });
    ok++;
    const openCount = found.filter(f => f.anyAvailable).length;
    console.log(`✓ ${r.id} ${r.name || ""} — ${found.length} dates, ${openCount} bookable`);
  } catch (err) {
    failed++;
    console.error(`✗ ${r.id} ${r.name || ""} — ${err.message}`);
  } finally {
    if (ctx) await ctx.close();
  }
}

await closeBrowser();
const written = await append(rows);
console.log(`\nsnapshot ${ts}: ${ok} ok, ${failed} failed, ${written} observations appended`);
/* A failed probe is not a reason to lose the rows that did work, but it is a
   reason to exit non-zero so a scheduled run surfaces the problem. */
process.exit(failed ? 1 : 0);

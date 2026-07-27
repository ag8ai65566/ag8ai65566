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

/**
 * What the `available` code on a Tabelog calendar day means.
 *
 * Established on 2026-07-27 by reading live calendars: 3 lands exactly on each
 * restaurant's 定休日 plus the obon week and the September public holidays, and
 * 4 only ever lands on today/tomorrow. 2 is the overwhelmingly common value and
 * is the one `member_by_date` also uses for a party size you can actually pick,
 * against 0 for one you can't.
 *
 * `null` means "this day is not evidence either way" and is deliberately not
 * `false`: a shut restaurant is not a restaurant that sold out, and recording it
 * as one would understate how long its seats really stay open.
 */
const VACANCY = {
  0: { available: false, note: "満席／受付不可" },
  1: { available: null, note: "残席わずか？ code 1 の意味は未確認" },
  2: { available: true, note: "空席あり" },
  3: { available: null, note: "定休日・休業", skip: true },
  4: { available: null, note: "オンライン受付締切（当日・翌日）", skip: true },
};

const PROBES = {
  /**
   * Tabelog's booking calendar is served as JSON by the shop page's own widget
   * endpoint — roughly 66 days of day-level status. It has to be fetched from
   * inside the page: the endpoint is same-origin only and returns the shop's
   * calendar keyed by rst_id.
   */
  async tabelog(ctx, r) {
    const page = await open(ctx, r.tabelog);
    try {
      const payload = await page.evaluate(async id => {
        const res = await fetch(`/booking/calendar/initial_vacancy?rst_id=${id}`,
          { headers: { "X-Requested-With": "XMLHttpRequest" } });
        return res.ok ? res.json() : { __status: res.status };
      }, r.id);

      if (payload.__status) throw new Error(`vacancy endpoint returned HTTP ${payload.__status}`);
      const list = payload?.date_with_status?.dateList;
      if (!Array.isArray(list) || !list.length)
        throw new Error("vacancy calendar was empty — endpoint or payload shape changed");

      const wanted = new Set(horizonDates());
      const out = [];
      for (const d of list) {
        const diningDate =
          `${d.year}-${String(d.month).padStart(2, "0")}-${String(d.day).padStart(2, "0")}`;
        if (!wanted.has(diningDate)) continue;
        const v = VACANCY[d.available];
        if (v?.skip) continue;
        out.push({
          diningDate,
          anyAvailable: v ? v.available : null,
          /* Kept so a day can be reinterpreted later without re-scraping, and so
             an unrecognised code is visible instead of silently becoming false. */
          code: d.available,
          slots: [],
        });
      }
      return out;
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

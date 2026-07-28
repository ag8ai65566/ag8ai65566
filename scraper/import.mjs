#!/usr/bin/env node
/**
 * Read Tabelog URLs (argv, or one per line on stdin) and write structured
 * restaurant records to ../data/restaurants.json, merging with what's there.
 *
 *   node import.mjs https://tabelog.com/tokyo/A1303/A130301/13157208/
 *   cat urls.txt | node import.mjs
 */
import fs from "node:fs/promises";
import path from "node:path";
import { contextFor, closeBrowser } from "./lib/browser.mjs";
import { fetchRestaurant, parseShopUrl } from "./lib/tabelog.mjs";

const OUT = path.join(process.cwd(), "..", "data", "restaurants.json");
const PLATFORMS = path.join(process.cwd(), "platforms.json");

/**
 * Which platform a restaurant actually books through can't be read off its
 * Tabelog page — none of these link out to OMAKASE or TableAll. It's kept as a
 * checked-in mapping and merged on every import so a re-import doesn't drop it
 * along with the rest of gitignored data/.
 */
async function loadPlatforms() {
  try {
    const raw = JSON.parse(await fs.readFile(PLATFORMS, "utf8"));
    return Object.fromEntries(Object.entries(raw).filter(([k]) => !k.startsWith("_")));
  } catch { return {}; }
}

/** Pull the http(s) URLs out of text, ignoring blank lines and # comments. */
const urlsIn = text => (text.match(/https?:\/\/\S+/g) || []).filter(u => !u.startsWith("#"));

async function readUrls() {
  const args = process.argv.slice(2).filter(a => !a.startsWith("-"));
  if (args.length) return args;
  if (!process.stdin.isTTY) {
    const chunks = [];
    for await (const c of process.stdin) chunks.push(c);
    const piped = urlsIn(Buffer.concat(chunks).toString("utf8"));
    if (piped.length) return piped;
  }
  /* Default to the tracked list, so a scheduled run needs no arguments and the
     list itself is version-controlled rather than living in someone's shell. */
  try { return urlsIn(await fs.readFile(path.join(process.cwd(), "watchlist.txt"), "utf8")); }
  catch { return []; }
}

async function loadExisting() {
  try { return JSON.parse(await fs.readFile(OUT, "utf8")); } catch { return []; }
}

const urls = await readUrls();
if (!urls.length) {
  console.error("usage: node import.mjs <tabelog-url>...   (or pipe URLs on stdin)");
  process.exit(2);
}

const bad = urls.filter(u => !parseShopUrl(u));
if (bad.length) console.error(`skipping ${bad.length} unrecognised URL(s):\n  ${bad.join("\n  ")}`);

const ctx = await contextFor("tabelog");
const platforms = await loadPlatforms();
const existing = await loadExisting();
const byId = new Map(existing.map(r => [r.id, r]));
let ok = 0, failed = 0;

for (const url of urls) {
  const ref = parseShopUrl(url);
  if (!ref) continue;
  try {
    const rec = await fetchRestaurant(ctx, url);
    const plat = platforms[rec.id];
    if (plat) Object.assign(rec, {
      bookingSource: plat.bookingSource,
      bookingUrl: plat.bookingUrl,
      bookingVerifiedBy: plat.verifiedBy,
      /* A second, usually paid, way in — recorded separately so the primary
         route's release time is never shown under the other one's name. */
      bookingAlt: plat.alt || null,
    });
    byId.set(rec.id, { ...byId.get(rec.id), ...rec });
    ok++;
    console.log(`✓ ${rec.id}  ${rec.name || "(no name)"}  ${rec.genre || ""}  ` +
      `rule=${rec.rule.kind}  訂位=${plat ? plat.bookingSource : "?"}`);
    if (rec.rule.kind === "unknown" && rec.reservationText)
      console.log(`   予約欄未能判讀，原文保留：${rec.reservationText.replace(/\n/g, " / ")}`);
  } catch (err) {
    failed++;
    console.error(`✗ ${url}\n   ${err.message}`);
  }
}

await ctx.close();
await closeBrowser();

await fs.mkdir(path.dirname(OUT), { recursive: true });
const merged = [...byId.values()].sort((a, b) => (a.name || "").localeCompare(b.name || ""));
await fs.writeFile(OUT, JSON.stringify(merged, null, 2) + "\n", "utf8");

console.log(`\n${ok} imported, ${failed} failed → ${path.relative(process.cwd(), OUT)} (${merged.length} total)`);
process.exit(failed && !ok ? 1 : 0);

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

async function readUrls() {
  const args = process.argv.slice(2).filter(a => !a.startsWith("-"));
  if (args.length) return args;
  if (process.stdin.isTTY) return [];
  const chunks = [];
  for await (const c of process.stdin) chunks.push(c);
  return Buffer.concat(chunks).toString("utf8").split(/\s+/).filter(Boolean);
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
const existing = await loadExisting();
const byId = new Map(existing.map(r => [r.id, r]));
let ok = 0, failed = 0;

for (const url of urls) {
  const ref = parseShopUrl(url);
  if (!ref) continue;
  try {
    const rec = await fetchRestaurant(ctx, url);
    byId.set(rec.id, { ...byId.get(rec.id), ...rec });
    ok++;
    console.log(`✓ ${rec.id}  ${rec.name || "(no name)"}  ${rec.genre || ""}  rule=${rec.rule.kind}`);
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

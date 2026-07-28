#!/usr/bin/env node
/**
 * Log in to OMAKASE and dump each restaurant's page — text, a screenshot, and
 * the calendar-ish markup — into ./dump/.
 *
 *   npm i && cp .env.example .env   # fill in OMAKASE_EMAIL / OMAKASE_PASSWORD
 *   node dump-omakase.mjs
 *
 * Why this exists: OMAKASE's Cloudflare hard-blocks the cloud environment this
 * project was built in, so nobody there has ever seen a logged-in OMAKASE page.
 * Writing a calendar parser against a page you have not seen is how you get
 * selectors that match nothing — this repo has already paid for that lesson
 * twice. Run this from a machine that can reach the site, send the contents of
 * dump/ back, and the probe gets written against what is actually on the page.
 *
 * The dumps contain your logged-in view. Look through them before sharing:
 * the account name appears in the page chrome, and any existing bookings will
 * show up too.
 */
import fs from "node:fs/promises";
import path from "node:path";
import { contextFor, closeBrowser, open } from "./lib/browser.mjs";
import { login } from "./lib/omakase.mjs";

const OUT = path.join(process.cwd(), "dump");

/* The four restaurants on the list that book through OMAKASE. */
const SHOPS = [
  ["蒼", "https://omakase.in/ja/r/iz931441"],
  ["とり茶太郎", "https://omakase.in/r/hn429275"],
  ["明寂", "https://omakase.in/r/ff108237"],
  ["酉囃子", "https://omakase.in/r/cn838977"],
];

await fs.mkdir(OUT, { recursive: true });
const ctx = await contextFor("omakase");

await login(ctx);
console.log("signed in\n");

for (const [name, url] of SHOPS) {
  const slug = url.split("/").pop();
  try {
    const page = await open(ctx, url);
    /* The calendar is drawn after load; give it a moment before capturing. */
    await page.waitForTimeout(4000);

    const text = await page.evaluate(() => document.body.innerText);
    const calendar = await page.evaluate(() => {
      const nodes = [...document.querySelectorAll(
        '[class*="calendar" i],[class*="vacancy" i],[class*="schedule" i],table')];
      return nodes.slice(0, 6).map(n => n.outerHTML.slice(0, 4000)).join("\n\n<!-- ─── -->\n\n");
    });

    await fs.writeFile(path.join(OUT, `${slug}.txt`), `${name}\n${url}\n\n${text}\n`, "utf8");
    await fs.writeFile(path.join(OUT, `${slug}.calendar.html`), calendar || "(nothing matched)", "utf8");
    await page.screenshot({ path: path.join(OUT, `${slug}.png`), fullPage: true });
    await page.close();

    console.log(`✓ ${name}  → dump/${slug}.{txt,calendar.html,png}`);
  } catch (err) {
    console.error(`✗ ${name} — ${err.message}`);
  }
}

await closeBrowser();
console.log(`\nDone. Everything is in ${OUT} — read it before sending it on.`);

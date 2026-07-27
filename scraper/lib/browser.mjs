import { chromium } from "playwright";
import fs from "node:fs/promises";
import path from "node:path";

const STATE_DIR = path.join(process.cwd(), ".auth");
const DELAY = Number(process.env.REQUEST_DELAY_MS || 4000);

/** One shared browser per process. */
let browser;
export async function getBrowser() {
  if (!browser) browser = await chromium.launch({ headless: true });
  return browser;
}
export async function closeBrowser() {
  if (browser) { await browser.close(); browser = undefined; }
}

/**
 * A context for one site. Logged-in cookies are kept on disk under .auth/<site>.json
 * so a later run reuses the session instead of logging in again.
 */
export async function contextFor(site) {
  const b = await getBrowser();
  const statePath = path.join(STATE_DIR, `${site}.json`);
  let storageState;
  try { storageState = JSON.parse(await fs.readFile(statePath, "utf8")); } catch { /* first run */ }
  return b.newContext({
    storageState,
    locale: "ja-JP",
    timezoneId: "Asia/Tokyo",
    viewport: { width: 1400, height: 1000 },
    userAgent:
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 " +
      "(KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
  });
}

export async function saveState(ctx, site) {
  await fs.mkdir(STATE_DIR, { recursive: true });
  await ctx.storageState({ path: path.join(STATE_DIR, `${site}.json`) });
}

const lastHit = new Map();
/** Space out requests per host. These are someone else's servers. */
export async function polite(url) {
  const host = new URL(url).hostname;
  const wait = DELAY - (Date.now() - (lastHit.get(host) || 0));
  if (wait > 0) await new Promise(r => setTimeout(r, wait));
  lastHit.set(host, Date.now());
}

/** Navigate with one retry; returns the page or throws with the URL attached. */
export async function open(ctx, url, { waitFor } = {}) {
  await polite(url);
  const page = await ctx.newPage();
  for (let attempt = 0; attempt < 2; attempt++) {
    try {
      const res = await page.goto(url, { waitUntil: "domcontentloaded", timeout: 45000 });
      if (res && res.status() >= 400) throw new Error(`HTTP ${res.status()}`);
      if (waitFor) await page.waitForSelector(waitFor, { timeout: 15000 });
      return page;
    } catch (err) {
      if (attempt === 1) { await page.close(); throw new Error(`${url} — ${err.message}`); }
      await new Promise(r => setTimeout(r, 3000));
    }
  }
}

export function requireEnv(...keys) {
  const missing = keys.filter(k => !process.env[k]);
  if (missing.length) throw new Error(`missing env: ${missing.join(", ")} — see .env.example`);
  return keys.map(k => process.env[k]);
}

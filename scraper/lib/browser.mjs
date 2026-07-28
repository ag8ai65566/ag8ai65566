import { chromium } from "playwright";
import fs from "node:fs/promises";
import fsSync from "node:fs";
import path from "node:path";
import { X509Certificate, createHash } from "node:crypto";

/**
 * Credentials live in scraper/.env (gitignored).
 *
 * Parsed here rather than with process.loadEnvFile because this file gets
 * written by hand on Windows, where Notepad may prepend a UTF-8 BOM and every
 * line ends CRLF. The BOM would silently attach itself to the first key —
 * "﻿OMAKASE_EMAIL" — and the login would fail with the credentials sitting
 * right there in the file, which is a miserable thing to debug.
 */
function loadEnvFile(file) {
  let raw;
  try { raw = fsSync.readFileSync(file, "utf8"); } catch { return; }
  if (raw.charCodeAt(0) === 0xfeff) raw = raw.slice(1);
  for (const line of raw.split(/\r?\n/)) {
    const m = line.match(/^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.*)$/);
    if (!m) continue;                                   // blank line or # comment
    const value = m[2].trim().replace(/^(["'])(.*)\1$/, "$2");
    if (!(m[1] in process.env)) process.env[m[1]] = value;   // real env wins
  }
}
loadEnvFile(path.join(process.cwd(), ".env"));

const STATE_DIR = path.join(process.cwd(), ".auth");
const DELAY = Number(process.env.REQUEST_DELAY_MS || 4000);

/**
 * Everything below adapts the launch to a sandboxed cloud session (Claude Code
 * on the web). On a normal machine every one of these returns nothing and
 * Playwright's own defaults apply — see docs/network-setup.md.
 */

/**
 * Playwright insists on the exact Chromium build its own version pins. The
 * sandbox image ships a different build under PLAYWRIGHT_BROWSERS_PATH and
 * blocks `playwright install`, so point at whatever is actually on disk.
 */
function findChromium() {
  if (process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE) return process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE;
  const root = process.env.PLAYWRIGHT_BROWSERS_PATH;
  if (!root) return undefined;
  try { if (chromium.executablePath() && fsSync.existsSync(chromium.executablePath())) return undefined; } catch { /* not installed */ }
  const builds = fsSync.readdirSync(root)
    .filter(d => /^chromium-\d+$/.test(d))
    .sort((a, b) => Number(b.split("-")[1]) - Number(a.split("-")[1]));
  for (const b of builds) {
    const exe = path.join(root, b, "chrome-linux", "chrome");
    if (fsSync.existsSync(exe)) return exe;
  }
  return undefined;
}

const CA_PATH = "/root/.ccr/agent-proxy-ca.crt";

/**
 * The sandbox proxy re-terminates TLS, so Chromium sees a certificate signed by
 * a CA it doesn't ship. Playwright launches a throwaway profile, so the image's
 * NSS store never applies. Pin that one CA by its public-key hash: certificates
 * are still verified, only this specific issuer is added.
 */
function proxyCaPin() {
  try {
    const cert = new X509Certificate(fsSync.readFileSync(CA_PATH));
    const spki = createHash("sha256")
      .update(cert.publicKey.export({ type: "spki", format: "der" }))
      .digest("base64");
    return `--ignore-certificate-errors-spki-list=${spki}`;
  } catch { return null; }
}

/**
 * Show the browser window instead of running headless. Worth it for anything a
 * person runs by hand against a Cloudflare-protected site: headless Chromium
 * gets challenged far more often, and when a challenge does appear you can only
 * clear it if you can see it. Call before the first getBrowser().
 */
let headful = !!process.env.HEADFUL;
export function setHeadful(v = true) { headful = v; }

/** One shared browser per process. */
let browser;
export async function getBrowser() {
  if (browser) return browser;

  const proxyUrl = process.env.HTTPS_PROXY || process.env.https_proxy;
  const args = [];
  if (proxyUrl) {
    const pin = proxyCaPin();
    if (pin) args.push(pin);
    /* Chromium's TLS 1.3 handshake is reset by the egress relay; 1.2 completes.
       This caps only the hop to the local proxy — the proxy negotiates its own
       (unrestricted) TLS with the real site, and certificates stay verified. */
    args.push("--ssl-version-max=tls1.2");
  }

  browser = await chromium.launch({
    headless: !headful,
    executablePath: findChromium(),
    proxy: proxyUrl ? { server: proxyUrl } : undefined,
    args,
  });
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

/**
 * Extract a restaurant record from a Tabelog shop page.
 *
 * Strategy: read schema.org JSON-LD first — Tabelog publishes name, address,
 * telephone and aggregateRating there, and structured data survives redesigns
 * that break CSS selectors. Fall back to the page's own table markup for the
 * fields JSON-LD doesn't carry (genre, budget, seats, the 予約 text).
 *
 * NOTE: the fallback selectors below are written from Tabelog's long-standing
 * `rstinfo-table` markup but have NOT been verified against a live page yet —
 * this environment cannot reach tabelog.com. Run `npm run import` once network
 * access is open and reconcile anything that comes back null.
 */
import { open } from "./browser.mjs";

export const SHOP_RE =
  /^https?:\/\/(?:s\.)?tabelog\.com\/([a-z]+)\/([A-Z]\d+)\/([A-Z]\d+)\/(\d+)\/?/i;

export function parseShopUrl(url) {
  const m = String(url).trim().match(SHOP_RE);
  if (!m) return null;
  const [, pref, area1, area2, id] = m;
  return { url: m[0], pref, area1, area2, id, canonical: `https://tabelog.com/${pref}/${area1}/${area2}/${id}/` };
}

async function jsonLd(page) {
  const blocks = await page.$$eval('script[type="application/ld+json"]', ns =>
    ns.map(n => n.textContent || ""));
  const out = [];
  for (const raw of blocks) {
    try {
      const parsed = JSON.parse(raw);
      out.push(...(Array.isArray(parsed) ? parsed : [parsed]));
    } catch { /* Tabelog occasionally emits a malformed block; skip it */ }
  }
  return out;
}

const pickType = (nodes, type) =>
  nodes.find(n => (Array.isArray(n["@type"]) ? n["@type"] : [n["@type"]]).includes(type));

/** Read one label→value row out of the shop-info table. */
async function infoRow(page, label) {
  return page.evaluate(l => {
    const ths = [...document.querySelectorAll("#rstinfo-table th, .rstinfo-table th")];
    const th = ths.find(t => (t.textContent || "").replace(/\s+/g, "").includes(l));
    if (!th) return null;
    const td = th.parentElement && th.parentElement.querySelector("td");
    return td ? (td.innerText || "").trim().replace(/\n{2,}/g, "\n") : null;
  }, label);
}

export async function fetchRestaurant(ctx, url) {
  const ref = parseShopUrl(url);
  if (!ref) throw new Error(`not a Tabelog shop URL: ${url}`);

  const page = await open(ctx, ref.canonical);
  try {
    const nodes = await jsonLd(page);
    const rst = pickType(nodes, "Restaurant") || pickType(nodes, "FoodEstablishment") || {};
    const addr = rst.address || {};

    const record = {
      id: ref.id,
      source: "tabelog",
      tabelog: ref.canonical,
      name: rst.name || (await page.title()).split("-")[0].trim() || null,
      score: rst.aggregateRating ? Number(rst.aggregateRating.ratingValue) : null,
      reviewCount: rst.aggregateRating ? Number(rst.aggregateRating.reviewCount || 0) : null,
      phone: rst.telephone || null,
      address:
        [addr.addressRegion, addr.addressLocality, addr.streetAddress].filter(Boolean).join("") ||
        (await infoRow(page, "住所")),
      lat: rst.geo ? Number(rst.geo.latitude) : null,
      lng: rst.geo ? Number(rst.geo.longitude) : null,
      genre: await infoRow(page, "ジャンル"),
      station: await infoRow(page, "交通手段"),
      hours: await infoRow(page, "営業時間"),
      closed: await infoRow(page, "定休日"),
      seats: await infoRow(page, "席数"),
      budgetDinner: rst.priceRange || (await infoRow(page, "予算")),
      /* The field the whole reservation radar hangs on. Kept verbatim in
         Japanese — interpretation happens later, against the raw text. */
      reservationText: await infoRow(page, "予約可否") || await infoRow(page, "予約"),
      fetchedAt: new Date().toISOString(),
    };
    record.rule = inferRule(record.reservationText);
    return record;
  } finally {
    await page.close();
  }
}

/**
 * Turn Tabelog's free-text 予約 note into one of the radar's rule shapes.
 * Anything it can't read confidently stays `unknown` rather than guessing —
 * a wrong rule sends you to book on the wrong day, which is worse than no rule.
 */
export function inferRule(text) {
  if (!text) return { kind: "unknown" };
  const t = text.replace(/\s+/g, "");
  const num = s => { const m = t.match(s); return m ? Number(m[1].replace(/[０-９]/g, d => "０１２３４５６７８９".indexOf(d))) : null; };

  const hour = num(/(\d{1,2})[時:]/) ?? 10;

  // 毎月1日／翌月分 — the classic omakase counter pattern
  const monthlyDay = num(/毎月(\d{1,2})日/);
  if (monthlyDay !== null) {
    const lead = num(/(\d{1,2})[ヶか]月(?:先|後)/) ?? (/翌々月/.test(t) ? 2 : 1);
    return { kind: "monthlyFirst", day: monthlyDay, hour, lead };
  }
  // Nヶ月前
  const months = num(/(\d{1,2})[ヶか]月前/);
  if (months !== null) return { kind: "monthsBefore", months, hour };
  // N日前
  const days = num(/(\d{1,3})日前/);
  if (days !== null) return { kind: "daysBefore", days, hour };

  return { kind: "unknown", raw: text };
}

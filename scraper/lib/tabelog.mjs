/**
 * Extract a restaurant record from a Tabelog shop page.
 *
 * Strategy: read schema.org JSON-LD first — Tabelog publishes name, address,
 * telephone and aggregateRating there, and structured data survives redesigns
 * that break CSS selectors. Fall back to the page's own table markup for the
 * fields JSON-LD doesn't carry (genre, budget, seats, the 予約 text).
 *
 * Selectors verified against live shop pages on 2026-07-27.
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

/**
 * Read the 営業時間 cell, which carries the closing days too — the current
 * layout has no separate 定休日 row, so both fields come from here. Three
 * shapes occur in the wild and all three are live right now:
 *
 *   1. day label + time ranges, one item per group;
 *   2. the same, plus an item whose detail text is literally 定休日 — its
 *      label is then the list of days the shop is shut;
 *   3. a single item of free text the owner typed, using ■ headings.
 */
async function businessHours(page) {
  return page.evaluate(() => {
    const ths = [...document.querySelectorAll("#rstinfo-table th, .rstinfo-table th")];
    const th = ths.find(t => (t.textContent || "").replace(/\s+/g, "").includes("営業時間"));
    const td = th && th.parentElement && th.parentElement.querySelector("td");
    if (!td) return { hours: null, closed: null };

    const tidy = s => (s || "").trim().replace(/\n{3,}/g, "\n\n");
    const dropHeading = s => tidy(String(s).replace(/^\s*[■◆●▪]?\s*営業時間\s*[：:]?\s*/, ""));

    /* Owner-typed text: split it at the 定休日 heading rather than losing the
       hours above it or guessing the days below it. */
    const splitFreeText = text => {
      const t = tidy(text);
      if (!t) return { hours: "", closed: "" };
      const at = t.match(/(?:^|\n)\s*[■◆●▪・]?\s*定休日\s*[：:]?\s*/);
      if (!at) return { hours: dropHeading(t), closed: "" };
      /* Owners often carry on past the 定休日 answer with cancellation notes.
         The answer is the first paragraph; stop at the blank line or the next
         ■ heading so those notes don't end up recorded as closing days. */
      const rest = t.slice(at.index + at[0].length);
      return {
        hours: dropHeading(t.slice(0, at.index)),
        closed: tidy(rest.split(/\n\s*\n/)[0].split(/\n\s*[■◆●▪]/)[0]),
      };
    };

    const items = [...td.querySelectorAll(".rstinfo-table__business-item")];
    if (!items.length) {
      const { hours, closed } = splitFreeText(td.innerText);
      return { hours: hours || null, closed: closed || null };
    }

    const open = [], shut = [];
    for (const item of items) {
      const label = tidy(item.querySelector(".rstinfo-table__business-title")?.innerText);
      const details = [...item.querySelectorAll(".rstinfo-table__business-dtl-text")]
        .map(n => tidy(n.innerText).replace(/\s*\n\s*/g, " "))
        .filter(Boolean);

      if (!details.length) {                       // shape 3
        const free = splitFreeText(item.innerText);
        if (free.hours) open.push(free.hours);
        if (free.closed) shut.push(free.closed);
        continue;
      }
      if (details.some(d => d.includes("定休日"))) {  // shape 2
        if (label) shut.push(label);
        continue;
      }
      open.push([label, ...details].filter(Boolean).join("\n"));  // shape 1
    }
    return { hours: open.join("\n") || null, closed: shut.join("、") || null };
  });
}

export async function fetchRestaurant(ctx, url) {
  const ref = parseShopUrl(url);
  if (!ref) throw new Error(`not a Tabelog shop URL: ${url}`);

  const page = await open(ctx, ref.canonical);
  try {
    const nodes = await jsonLd(page);
    const rst = pickType(nodes, "Restaurant") || pickType(nodes, "FoodEstablishment") || {};
    const addr = rst.address || {};
    const rating = rst.aggregateRating || {};
    const { hours, closed } = await businessHours(page);

    const record = {
      id: ref.id,
      source: "tabelog",
      tabelog: ref.canonical,
      name: rst.name || (await page.title()).split("-")[0].trim() || null,
      score: rating.ratingValue != null ? Number(rating.ratingValue) : null,
      /* Tabelog publishes this as ratingCount; reviewCount is the schema.org
         spelling and is absent, so reading only that silently yielded 0. */
      reviewCount: rating.ratingCount != null ? Number(rating.ratingCount)
        : rating.reviewCount != null ? Number(rating.reviewCount) : null,
      phone: rst.telephone || null,
      address:
        [addr.addressRegion, addr.addressLocality, addr.streetAddress].filter(Boolean).join("") ||
        (await infoRow(page, "住所")),
      lat: rst.geo ? Number(rst.geo.latitude) : null,
      lng: rst.geo ? Number(rst.geo.longitude) : null,
      genre: await infoRow(page, "ジャンル"),
      station: await infoRow(page, "交通手段"),
      hours,
      closed,
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

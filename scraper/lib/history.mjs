/**
 * The availability history database.
 *
 * Tabelog, OMAKASE and TableCheck all show only *future* availability — none of
 * them expose what a restaurant's calendar looked like last month. So there is
 * nothing to look up retroactively. Instead we take one snapshot a day from now
 * on and accumulate our own history; after two or three weeks it answers the
 * question that actually matters: how fast does this restaurant sell out once
 * booking opens?
 *
 * Storage is append-only JSONL — one line per (restaurant, dining date, day).
 * Cheap to append from a cron job, trivial to diff, and it never rewrites past
 * observations.
 */
import fs from "node:fs/promises";
import path from "node:path";

const FILE = path.join(process.cwd(), "..", "data", "availability.jsonl");

/** @typedef {{ts:string, restaurantId:string, source:string, diningDate:string,
 *             anyAvailable:boolean|null, code?:number,
 *             slots:{time:string,seats:number|null}[]}} Observation */

/* anyAvailable may be null: the source answered, but not with a yes or a no
 * (a closing day, a booking window not open yet, a status we can't read). Every
 * reader below counts only the `true` days, so a null can never be mistaken for
 * a sell-out — which is why sell-out timing is derived from the span of open
 * observations rather than from whatever the first non-open day happens to be. */

export async function append(observations) {
  if (!observations.length) return 0;
  await fs.mkdir(path.dirname(FILE), { recursive: true });
  await fs.appendFile(FILE, observations.map(o => JSON.stringify(o)).join("\n") + "\n", "utf8");
  return observations.length;
}

export async function load() {
  try {
    const raw = await fs.readFile(FILE, "utf8");
    return raw.split("\n").filter(Boolean).map(l => JSON.parse(l));
  } catch (e) {
    if (e.code === "ENOENT") return [];
    throw e;
  }
}

/**
 * For each (restaurant, dining date): the first day we saw it bookable and the
 * last. `soldOutAfterDays` is the gap — the headline number.
 *
 * `stillOpen` marks series where the seat is still available as of the newest
 * snapshot, so the gap is a lower bound, not a measurement. Reporting those two
 * cases as if they were the same would overstate how fast a place fills.
 */
export function sellOutStats(observations) {
  const series = new Map();
  for (const o of observations) {
    const key = `${o.restaurantId}|${o.diningDate}`;
    if (!series.has(key)) series.set(key, []);
    series.get(key).push(o);
  }

  const latestTs = observations.reduce((m, o) => (o.ts > m ? o.ts : m), "");
  const out = [];
  for (const [key, obs] of series) {
    obs.sort((a, b) => a.ts.localeCompare(b.ts));
    const open = obs.filter(o => o.anyAvailable);
    if (!open.length) continue;
    const [restaurantId, diningDate] = key.split("|");
    const first = open[0], last = open[open.length - 1];
    const stillOpen = last.ts === latestTs;
    out.push({
      restaurantId,
      diningDate,
      firstSeenOpen: first.ts,
      lastSeenOpen: last.ts,
      observations: obs.length,
      soldOutAfterDays: Math.round((Date.parse(last.ts) - Date.parse(first.ts)) / 864e5),
      stillOpen,
    });
  }
  return out.sort((a, b) => a.diningDate.localeCompare(b.diningDate));
}

/**
 * Median days-to-sell-out per restaurant, using only series we actually watched
 * close. Returns null for a restaurant with no closed series yet — the honest
 * answer while the history is still filling up.
 */
export function perRestaurant(observations) {
  const stats = sellOutStats(observations).filter(s => !s.stillOpen);
  const grouped = new Map();
  for (const s of stats) {
    if (!grouped.has(s.restaurantId)) grouped.set(s.restaurantId, []);
    grouped.get(s.restaurantId).push(s.soldOutAfterDays);
  }
  const summary = {};
  for (const [id, days] of grouped) {
    days.sort((a, b) => a - b);
    const mid = Math.floor(days.length / 2);
    summary[id] = {
      samples: days.length,
      medianDaysToSellOut: days.length % 2 ? days[mid] : Math.round((days[mid - 1] + days[mid]) / 2),
      fastest: days[0],
      slowest: days[days.length - 1],
    };
  }
  for (const id of new Set(observations.map(o => o.restaurantId))) {
    if (!summary[id]) summary[id] = { samples: 0, medianDaysToSellOut: null };
  }
  return summary;
}

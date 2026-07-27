#!/usr/bin/env node
/** Tests for the parts that don't need network: rule inference and history stats. */
import assert from "node:assert/strict";
import { test } from "node:test";
import { inferRule, parseShopUrl } from "./lib/tabelog.mjs";
import { sellOutStats, perRestaurant } from "./lib/history.mjs";

test("parseShopUrl accepts the shop-page shapes Tabelog serves", () => {
  const a = parseShopUrl("https://tabelog.com/tokyo/A1303/A130301/13157208/");
  assert.equal(a.id, "13157208");
  assert.equal(a.area1, "A1303");
  assert.equal(parseShopUrl("https://s.tabelog.com/tokyo/A1307/A130702/13304401/").id, "13304401");
  assert.equal(parseShopUrl("https://tabelog.com/tokyo/A1316/A131602/13303865").id, "13303865");
  assert.equal(parseShopUrl("https://tabelog.com/tokyo/A1303/A130301/13157208/dtlrvwlst/").canonical,
    "https://tabelog.com/tokyo/A1303/A130301/13157208/");
  assert.equal(parseShopUrl("https://omakase.in/r/abc"), null);
  assert.equal(parseShopUrl("not a url"), null);
});

test("inferRule reads the monthly-release pattern", () => {
  assert.deepEqual(inferRule("毎月1日 10時より翌月分の予約を受付"),
    { kind: "monthlyFirst", day: 1, hour: 10, lead: 1 });
  assert.deepEqual(inferRule("毎月15日 11:00より翌々月分を受付"),
    { kind: "monthlyFirst", day: 15, hour: 11, lead: 2 });
});

test("inferRule reads months-before and days-before", () => {
  assert.deepEqual(inferRule("3ヶ月前の同日10時より予約可能"), { kind: "monthsBefore", months: 3, hour: 10 });
  assert.deepEqual(inferRule("2か月前より受付"), { kind: "monthsBefore", months: 2, hour: 10 });
  assert.deepEqual(inferRule("30日前より予約受付"), { kind: "daysBefore", days: 30, hour: 10 });
  assert.deepEqual(inferRule("14日前 11時より"), { kind: "daysBefore", days: 14, hour: 11 });
});

test("inferRule refuses to guess rather than sending you to book on the wrong day", () => {
  assert.equal(inferRule(null).kind, "unknown");
  assert.equal(inferRule("予約可").kind, "unknown");
  assert.equal(inferRule("完全予約制").kind, "unknown");
  assert.equal(inferRule("お電話にてお問い合わせください").kind, "unknown");
  assert.equal(inferRule("予約不可").raw, "予約不可");
});

const obs = (ts, id, diningDate, anyAvailable) =>
  ({ ts, restaurantId: id, source: "tabelog", diningDate, anyAvailable, slots: [] });

test("sellOutStats measures the open→sold-out gap", () => {
  const rows = [
    obs("2026-08-01T01:00:00Z", "A", "2026-09-10", true),
    obs("2026-08-02T01:00:00Z", "A", "2026-09-10", true),
    obs("2026-08-04T01:00:00Z", "A", "2026-09-10", false),
    obs("2026-08-05T01:00:00Z", "A", "2026-09-10", false),
  ];
  const [s] = sellOutStats(rows);
  assert.equal(s.soldOutAfterDays, 1);
  assert.equal(s.stillOpen, false);
  assert.equal(s.observations, 4);
});

test("a seat still bookable at the newest snapshot is a lower bound, not a measurement", () => {
  const rows = [
    obs("2026-08-01T01:00:00Z", "B", "2026-09-11", true),
    obs("2026-08-06T01:00:00Z", "B", "2026-09-11", true),
  ];
  const [s] = sellOutStats(rows);
  assert.equal(s.stillOpen, true);
  assert.equal(s.soldOutAfterDays, 5);
  // and it must not pollute the per-restaurant median
  assert.equal(perRestaurant(rows).B.samples, 0);
  assert.equal(perRestaurant(rows).B.medianDaysToSellOut, null);
});

test("a date never seen bookable produces no series at all", () => {
  assert.equal(sellOutStats([obs("2026-08-01T01:00:00Z", "C", "2026-09-12", false)]).length, 0);
});

test("perRestaurant takes the median across closed series", () => {
  const rows = [];
  // three dining dates that sold out after 1, 3 and 9 days
  [["2026-09-01", 1], ["2026-09-02", 3], ["2026-09-03", 9]].forEach(([date, gap]) => {
    rows.push(obs("2026-08-01T01:00:00Z", "D", date, true));
    rows.push(obs(`2026-08-${String(1 + gap).padStart(2, "0")}T01:00:00Z`, "D", date, true));
    rows.push(obs("2026-08-20T01:00:00Z", "D", date, false));
  });
  const s = perRestaurant(rows).D;
  assert.equal(s.samples, 3);
  assert.equal(s.medianDaysToSellOut, 3);
  assert.equal(s.fastest, 1);
  assert.equal(s.slowest, 9);
});

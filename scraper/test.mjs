#!/usr/bin/env node
/** Tests for the parts that don't need network: rule inference and history stats. */
import assert from "node:assert/strict";
import { test } from "node:test";
import { inferRule, parseShopUrl, parseAnnouncement, closedDows } from "./lib/tabelog.mjs";
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

/* Real 予約 text from 日本橋 蕎ノ字. The days here are a refund schedule; read as
   a booking rule they produced a confident `daysBefore: 3`, which would have put
   the alarm 27 days late for a shop that opens bookings a month out. */
test("a cancellation policy is not a booking rule", () => {
  assert.equal(inferRule(
    "予約可\n「キャンセルポリシー」\n3日前から50％、前日から100%のキャンセル料がかかります。\n" +
    "蕎麦アレルギーの方、強い香水はご遠慮下さい。").kind, "unknown");
  assert.equal(inferRule("30日前からキャンセル料が発生します").kind, "unknown");
  assert.equal(inferRule("2ヶ月前より変更手数料を頂戴します").kind, "unknown");
  // but a real rule sitting next to a policy still gets read
  assert.deepEqual(inferRule("30日前より予約受付\n3日前からキャンセル料100%"),
    { kind: "daysBefore", days: 30, hour: 10 });
});

/* Real 予約 text from 鳥しき. */
test("inferRule reads 毎月最初の営業日, whose date depends on the shop's calendar", () => {
  assert.deepEqual(
    inferRule("毎月最初の営業日に、お電話にて2ヶ月先のご予約を承ります。（例：1月に3月分）"),
    { kind: "monthlyFirstBusinessDay", lead: 2, hour: null });
  // the （例：1月に3月分） aside must not be mistaken for the lead time
  assert.equal(inferRule("毎月最初の営業日に翌月分を承ります").lead, 1);
});

/* Real 予約 text from オオクサ. */
test("inferRule reads weeks, and takes the hour from the same sentence", () => {
  assert.deepEqual(
    inferRule("電話予約は1週間前の昼12:00からお受け致します"),
    { kind: "daysBefore", days: 7, hour: 12 });
  // 1週間以内／1週間以上先 are not 1週間前 and must not match
  assert.equal(inferRule("1週間以内のお好きな日程でご予約お受け致します").kind, "unknown");
});

test("inferRule distinguishes 'closed to new bookings' from 'rule unknown'", () => {
  assert.equal(inferRule("完全予約制\n新規予約不可").kind, "notAcceptingNew");
  assert.equal(inferRule("完全予約制").kind, "unknown");
});

test("parseAnnouncement prefers the shop's own dated notice", () => {
  const a = parseAnnouncement(
    "毎月最初の営業日に、お電話にて2ヶ月先のご予約を承ります。\n" +
    "【2026年10月分】2026年8月12日（水）17：00～19：00");
  assert.equal(a.forMonth, "2026-10");
  assert.equal(a.opensAt, "2026-08-12T17:00:00+09:00");
  assert.equal(a.opensUntil, "2026-08-12T19:00:00+09:00");
  assert.equal(parseAnnouncement("毎月1日10時より翌月分"), null);
});

test("closedDows reads weekdays without picking them out of other words", () => {
  assert.deepEqual(closedDows("月・火・日"), [0, 1, 2]);
  assert.deepEqual(closedDows("日・祝日、年末年始"), [0]);   // not the 日 in 祝日
  assert.deepEqual(closedDows("日曜日.他不定休"), [0]);
  assert.deepEqual(closedDows("不定休"), []);
  assert.deepEqual(closedDows(null), []);
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

/**
 * OMAKASE — log in, then read a restaurant's booking calendar.
 *
 * Logging in is not optional here. OMAKASE shows a guest a calendar that
 * understates what is actually bookable: some seats are only released to a
 * signed-in member, so a guest snapshot would record them as unavailable and
 * quietly poison the sell-out history with dates that were open all along.
 *
 * Credentials come from the environment (see .env.example) and are never
 * written to disk by this module; the logged-in cookies are, under .auth/.
 */
import { open, saveState, requireEnv } from "./browser.mjs";

const LOGIN = "https://omakase.in/users/sign_in";

/**
 * Turn Cloudflare's 403 into the one sentence that actually helps.
 *
 * Confirmed on 2026-07-28: GitHub's shared runners are blocked exactly as this
 * project's cloud environment is, so the whole pipeline can pass its tests and
 * still die here. Without this the log ends in a stack trace about page.goto,
 * which reads like a bug in the scraper rather than a network that will never
 * work from that machine.
 */
function blocked(err) {
  if (!/403/.test(err.message)) throw err;
  throw new Error(
    "omakase.in returned 403 — Cloudflare is blocking this machine's IP address, " +
    "not rejecting your login. Datacentre IPs (GitHub's runners included) are " +
    "blocked; a home connection is not. Run this workflow on a self-hosted runner " +
    "by setting the repository variable POLL_RUNNER=self-hosted, or run " +
    "`node poll-omakase.mjs` on your own machine. See docs/github-setup.md."
  );
}

/** Are we already signed in on this context? */
export async function isLoggedIn(ctx) {
  const page = await open(ctx, "https://omakase.in/");
  try {
    /* Only a sign-out control proves a session. This used to accept a link to
       /mypage as well, which the guest homepage also carries — so it reported
       "already signed in" on the very first run, login() returned early, and
       every page after that was fetched as a guest. */
    return await page.evaluate(() =>
      !!document.querySelector('a[href*="sign_out"], form[action*="sign_out"], [data-method="delete"][href*="sign_out"]'));
  } finally {
    await page.close();
  }
}

/**
 * Sign in unless the stored session is still good. Returns true when the
 * session is usable afterwards.
 */
export async function login(ctx, { force = false } = {}) {
  if (!force && await isLoggedIn(ctx).catch(blocked)) return true;

  const [email, password] = requireEnv("OMAKASE_EMAIL", "OMAKASE_PASSWORD");
  const page = await open(ctx, LOGIN).catch(blocked);
  try {
    await page.fill('input[name="user[email]"]', email);
    await page.fill('input[name="user[password]"]', password);
    /* Devise's remember_me keeps the cookie alive between nightly runs, which
       matters more than it looks: every extra login is another chance for
       Cloudflare to start challenging us. */
    const remember = await page.$('input[type="checkbox"][name="user[remember_me]"]');
    if (remember) await remember.check().catch(() => {});

    await Promise.all([
      page.waitForNavigation({ waitUntil: "domcontentloaded", timeout: 45000 }).catch(() => {}),
      page.click('input[type="submit"], button[type="submit"]'),
    ]);
    await page.waitForTimeout(1500);

    const failed = await page.evaluate(() => {
      const t = document.body.innerText;
      return /パスワードが違います|メールアドレスまたはパスワード|Invalid Email or password|ログインできません/.test(t)
        || !!document.querySelector('input[name="user[password]"]');
    });
    if (failed) throw new Error("OMAKASE login rejected — check OMAKASE_EMAIL / OMAKASE_PASSWORD");
  } finally {
    await page.close();
  }

  await saveState(ctx, "omakase");
  return true;
}

/* ═══ booking state ═══════════════════════════════════════════════════════
 *
 * OMAKASE does not leave the release time to be inferred — it prints it, in the
 * 予約ルール詳細 panel, as 次回枠の受付開始日時. That is state, not a rule: it
 * moves every month, the time of day differs per restaurant, and a shop may
 * answer 未定. So it gets read and stored with a timestamp, and re-read on a
 * schedule; the text-inferred rule is only a fallback for when no reading exists.
 *
 * DOM extraction and text parsing are deliberately separate. The parsers below
 * are pure and unit-tested against the exact strings these pages serve, so the
 * only part that needs a live page to verify is which element the text came from.
 */

const ascii = s => String(s == null ? "" : s)
  .replace(/[０-９]/g, c => String.fromCharCode(c.charCodeAt(0) - 0xfee0))
  .replace(/[：]/g, ":").replace(/[～〜]/g, "~").replace(/[　]/g, " ");

const pad2 = n => String(n).padStart(2, "0");

/** 「2026年8月1日 08:00」→ 2026-08-01T08:00:00+09:00. 未定/blank → null. */
export function parseJstDateTime(text, { year } = {}) {
  const t = ascii(text);
  if (!t || /未定|未確定/.test(t)) return null;
  const m = t.match(/(?:(\d{4})\s*年)?\s*(\d{1,2})\s*月\s*(\d{1,2})\s*日/);
  if (!m) return null;
  const y = m[1] || year;
  if (!y) return null;
  const time = t.match(/(\d{1,2})\s*:\s*(\d{2})/);
  const hh = time ? pad2(time[1]) : "00";
  const mm = time ? time[2] : "00";
  return `${y}-${pad2(m[2])}-${pad2(m[3])}T${hh}:${mm}:00+09:00`;
}

/** 「2026年10月31日(土)まで」→ 2026-10-31. */
export function parseJstDate(text) {
  const iso = parseJstDateTime(text);
  return iso ? iso.slice(0, 10) : null;
}

/**
 * The lottery shops publish an application window that CLOSES BEFORE the
 * release. Missing it is not losing a race — it removes you from the draw
 * entirely, so this deadline outranks the release time in the radar.
 */
export function parseRaffle(bodyText, { nextOpenAt } = {}) {
  const t = ascii(bodyText);
  if (!/抽選/.test(t)) return null;

  /* Anchor the year on the release we already know; the worked example on the
     page writes 月/日 without one. */
  const year = nextOpenAt ? Number(nextOpenAt.slice(0, 4)) : new Date().getFullYear();

  const apply = t.match(
    /応募期間\s*】?\s*(\d{1,2})\s*月\s*(\d{1,2})\s*日\s*(\d{1,2}):(\d{2})\s*~\s*(\d{1,2})\s*月\s*(\d{1,2})\s*日\s*(\d{1,2}):(\d{2})/);
  const draw = t.match(/抽選発表\s*】?\s*(?:(\d{4})\s*年)?\s*(\d{1,2})\s*月\s*(\d{1,2})\s*日/);
  const lead = t.match(/予約開始月\s*\d{1,2}\s*日の\s*(\d{1,2})\s*日前より応募/);

  /* A window written 7/24 → 8/01 crosses into the next year only if the release
     itself did; keep both ends on the release's own year unless months descend. */
  const at = (mo, d, hh, mm) => `${year}-${pad2(mo)}-${pad2(d)}T${pad2(hh)}:${mm}:00+09:00`;

  return {
    appliesToRelease: nextOpenAt || null,
    applyFrom: apply ? at(apply[1], apply[2], apply[3], apply[4]) : null,
    applyUntil: apply ? at(apply[5], apply[6], apply[7], apply[8]) : null,
    drawOn: draw ? `${draw[1] || year}-${pad2(draw[2])}-${pad2(draw[3])}` : null,
    applyDaysBeforeRelease: lead ? Number(lead[1]) : null,
    info: /omakase\.in\/raffle/.test(t) ? "https://omakase.in/raffle" : null,
  };
}

/**
 * Build the stored reading out of the raw strings lifted off the page.
 * `rows` is the 予約ルール詳細 table as label→value.
 */
export function parseBookingState({ acceptLabel, rows = {}, feeText, bodyText } = {}) {
  const row = key => rows[Object.keys(rows).find(k => k.replace(/\s+/g, "").includes(key))] || null;

  const nextOpenAtRaw = row("次回枠の受付開始") || row("次回枠");
  const nextOpenAt = parseJstDateTime(nextOpenAtRaw);
  const fee = ascii(feeText).match(/一席あたり\s*(\d+)\s*円/);

  const state = {
    observedAt: new Date().toISOString(),
    observedBy: "poll-omakase",
    /* 「このお店を予約する」 is a live button; 「ご予約可能な枠がありません」 is not. */
    acceptingNow: /予約する/.test(ascii(acceptLabel)) && !/ありません/.test(ascii(acceptLabel)),
    acceptingLabel: (acceptLabel || "").trim() || null,
    windowUntil: parseJstDate(row("現在の予約受付期間")),
    nextOpenAt,
    nextOpenAtRaw: (nextOpenAtRaw || "").trim() || null,
    maxFrequency: (row("最大予約頻度") || "").trim() || null,
    feePerSeat: fee ? Number(fee[1]) : null,
    mechanism: /抽選/.test(ascii(bodyText)) ? "raffle" : "firstcome",
  };
  if (state.mechanism === "raffle") state.raffle = parseRaffle(bodyText, { nextOpenAt });
  return state;
}

/** Read one restaurant's booking state off its live page. */
export async function readBookingState(ctx, url) {
  const page = await open(ctx, url);
  try {
    await page.waitForTimeout(2500);
    const raw = await page.evaluate(() => {
      const txt = n => (n ? (n.innerText || "").trim() : "");

      /* Find the 予約ルール詳細 block and read it as label→value pairs. The
         labels are stable Japanese strings; the class names are not. */
      const rows = {};
      const all = [...document.querySelectorAll("*")].filter(n => n.children.length === 0);
      const LABELS = ["現在の予約受付期間", "次回枠の受付開始日時", "最大予約頻度"];
      for (const label of LABELS) {
        const node = all.find(n => (n.textContent || "").replace(/\s+/g, "").includes(label));
        if (!node) continue;
        /* The value is the next leaf with text inside the same row/parent. */
        let cur = node, value = "";
        for (let hop = 0; hop < 4 && !value && cur; hop++) {
          cur = cur.parentElement;
          if (!cur) break;
          const leaves = [...cur.querySelectorAll("*")].filter(n => n.children.length === 0);
          const i = leaves.indexOf(node);
          const next = leaves.slice(i + 1).find(n => (n.innerText || "").trim());
          if (next) value = next.innerText.trim();
        }
        rows[label] = value;
      }

      const body = document.body.innerText;
      const feeNode = all.find(n => /一席あたり/.test(n.textContent || ""));
      const btn = [...document.querySelectorAll("a,button,div")]
        .map(n => txt(n))
        .find(t => /^(このお店を予約する|ご予約可能な枠がありません)$/.test(t));

      return { acceptLabel: btn || "", rows, feeText: txt(feeNode), bodyText: body };
    });

    return { url, ...parseBookingState(raw) };
  } finally {
    await page.close();
  }
}

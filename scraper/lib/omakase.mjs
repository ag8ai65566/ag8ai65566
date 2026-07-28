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

/** Are we already signed in on this context? */
export async function isLoggedIn(ctx) {
  const page = await open(ctx, "https://omakase.in/");
  try {
    return await page.evaluate(() =>
      !!document.querySelector('a[href*="sign_out"], a[href*="/mypage"], form[action*="sign_out"]'));
  } finally {
    await page.close();
  }
}

/**
 * Sign in unless the stored session is still good. Returns true when the
 * session is usable afterwards.
 */
export async function login(ctx, { force = false } = {}) {
  if (!force && await isLoggedIn(ctx)) return true;

  const [email, password] = requireEnv("OMAKASE_EMAIL", "OMAKASE_PASSWORD");
  const page = await open(ctx, LOGIN);
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

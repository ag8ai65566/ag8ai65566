#!/usr/bin/env node
// Pull the public video list for a YouTube channel (titles + IDs + publish dates).
//
//   node fetch-channel.mjs                    # default: @henren778
//   node fetch-channel.mjs --handle someone   # another channel
//   node fetch-channel.mjs --json > out.json
//
// Behind an HTTPS proxy, run with NODE_USE_ENV_PROXY=1.
//
// Two sources, because each is missing something the other has:
//   * the channel /videos page  -> ~30 most recent titles (no descriptions)
//   * the RSS feed              -> 15 most recent with <media:description> (usually just hashtags)
//
// TRANSCRIPTS ARE NOT FETCHED HERE, on purpose. /watch pages and the youtubei
// player endpoint are served a bot-check from datacenter IPs, so any transcript
// route that works from a cloud container is an anti-bot workaround. Run
// `--transcript-help` for the manual paths that stay on the right side of that
// line. Members-only videos are paywalled and are never fetchable this way.

const args = process.argv.slice(2);
const val = (n, d) => { const i = args.indexOf(n); return i >= 0 && args[i + 1] ? args[i + 1] : d; };
const handle = val('--handle', 'henren778').replace(/^@/, '');

if (args.includes('--transcript-help')) {
  console.log(`
Transcripts for @${handle} — options that do not fight YouTube's bot check:

1. Browser, by hand. Open the video, "..." -> Show transcript, copy, save to
   references/transcripts/<videoId>.txt. Slow but always works, including for
   videos you have a paid membership to.

2. yt-dlp from your own machine (residential IP), not from a cloud container:
     yt-dlp --write-auto-sub --sub-lang zh-Hant,zh-Hans --skip-download \\
            --cookies-from-browser chrome "https://www.youtube.com/watch?v=<id>"
   The --cookies-from-browser flag is also what lets it see members-only videos
   your account actually pays for.

3. Paste the transcript into the conversation and ask for it to be filed.

Whatever the route, drop the text in references/transcripts/<videoId>.txt and
note the video in references/corpus.md so the claim log stays honest about
which entries are transcript-backed and which are title-only.
`.trim());
  process.exit(0);
}

const UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36';
const text = async (url) => {
  const r = await fetch(url, { headers: { 'User-Agent': UA, 'Accept-Language': 'zh-TW,zh;q=0.9' } });
  if (!r.ok) throw new Error(`HTTP ${r.status} for ${url}`);
  return r.text();
};

// --- channel page: titles live in lockupViewModel nodes ---
const page = await text(`https://www.youtube.com/@${handle}/videos`);
const initial = page.match(/var ytInitialData = (\{.*?\});<\/script>/s);
if (!initial) throw new Error('ytInitialData not found — YouTube changed its markup');
const data = JSON.parse(initial[1]);

const meta = data?.metadata?.channelMetadataRenderer ?? {};
const videos = [];
(function walk(node) {
  if (Array.isArray(node)) return node.forEach(walk);
  if (!node || typeof node !== 'object') return;
  const lv = node.lockupViewModel;
  if (lv?.contentId) {
    videos.push({
      id: lv.contentId,
      title: lv.metadata?.lockupMetadataViewModel?.title?.content ?? '',
      source: 'channel-page',
    });
  }
  Object.values(node).forEach(walk);
})(data);

// --- RSS: adds publish dates and descriptions for the newest 15 ---
const byId = new Map(videos.map((v) => [v.id, v]));
try {
  const feed = await text(`https://www.youtube.com/feeds/videos.xml?channel_id=${meta.externalId}`);
  const unescape = (s) => s
    .replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'").replace(/&amp;/g, '&');
  for (const entry of feed.match(/<entry>[\s\S]*?<\/entry>/g) ?? []) {
    const id = entry.match(/<yt:videoId>(.*?)<\/yt:videoId>/)?.[1];
    if (!id) continue;
    const row = byId.get(id) ?? { id, source: 'rss' };
    row.title = unescape(entry.match(/<title>([\s\S]*?)<\/title>/)?.[1] ?? row.title ?? '');
    row.published = entry.match(/<published>(.*?)<\/published>/)?.[1] ?? null;
    row.description = unescape(entry.match(/<media:description>([\s\S]*?)<\/media:description>/)?.[1] ?? '');
    if (!byId.has(id)) { videos.push(row); byId.set(id, row); }
  }
} catch (e) {
  console.error(`warning: RSS fetch failed (${e.message}); titles only`);
}

const out = {
  channel: { handle, title: meta.title ?? null, channelId: meta.externalId ?? null, description: meta.description ?? null },
  fetchedAt: new Date().toISOString(),
  videoCount: videos.length,
  videos,
};

if (args.includes('--json')) {
  console.log(JSON.stringify(out, null, 2));
} else {
  console.log(`${out.channel.title} (@${handle})  ${videos.length} videos\n`);
  for (const v of videos) {
    console.log(`${v.id}  ${(v.published ?? '').slice(0, 10).padEnd(10)}  ${v.title}`);
  }
  console.log('\nTranscripts are not fetched here — run with --transcript-help.');
}

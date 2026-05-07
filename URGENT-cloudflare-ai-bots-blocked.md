# URGENT: Cloudflare is overriding our robots.txt and blocking AI bots

## What is happening

When you visit https://zquas.ai/robots.txt, the response shows TWO
robots.txt blocks concatenated together:

1. A **Cloudflare-injected "Managed Content" block** at the top, with
   `Disallow: /` for ClaudeBot, GPTBot, PerplexityBot, CCBot, Bytespider,
   Amazonbot, Applebot-Extended, Google-Extended, meta-externalagent,
   and others.
2. Our actual `robots.txt` from the repo, which says "open to all bots",
   but it appears AFTER the managed block, so it does not override it.

When a well-behaved bot reads robots.txt top-down, the first matching
User-agent rule wins. The managed block tells ClaudeBot/GPTBot/etc. to
stay away. Our file underneath is never reached.

The actual HTTP layer at Cloudflare allows the bots (200 OK at the WAF),
but bots self-regulate based on robots.txt and refuse to index us.

## Fix (3 minutes)

Cloudflare dashboard -> zquas.ai -> there are two places this might be
controlled depending on your dashboard version. Disable BOTH:

### Place 1: AI Crawl Control / AI bots

- Cloudflare dashboard -> zquas.ai -> **Security -> Settings** (or
  **Security -> Bots** on older UIs).
- Find **"AI bots"** or **"AI Crawl Control"**.
- Set **Block AI bots: OFF**.
- If there is a list of specific AI bots (Anthropic, OpenAI, Perplexity,
  Common Crawl, ByteDance, etc.), allow ALL of them.

### Place 2: AI Audit / Managed robots.txt

- Cloudflare dashboard -> zquas.ai -> **AI Audit** (sometimes under
  Analytics & Logs, sometimes a top-level item).
- Find any setting along the lines of:
  - "Add Cloudflare AI policy to robots.txt"
  - "Managed robots.txt"
  - "Content Signals"
- Set **OFF**. Save.

### Place 3 (just in case): Scrape Shield / Hotlink Protection

- Cloudflare dashboard -> zquas.ai -> **Scrape Shield**.
- If anything bot-related is enabled here that is not Bot Fight Mode
  for malicious bots, review and disable for AI traffic.

## How to verify

After saving, wait 30 seconds, then run:

```
curl -s https://zquas.ai/robots.txt
```

The response should ONLY contain our content (the file from this repo,
starting with `# ZQUAS - Maximum AI access`). The Cloudflare managed
block at the top should be gone.

Also test that bots actually get our page:

```
curl -A "ClaudeBot/1.0" -I https://zquas.ai/article-75.html
curl -A "GPTBot/1.0"    -I https://zquas.ai/article-75.html
```

Both should return 200.

## Why this happened

Cloudflare added "AI Audit" and "Block AI Bots" features over the past
year and turned them ON BY DEFAULT for many zones. The defaults reflect
Cloudflare's commercial positioning (offering an AI bot blocking
service to publishers), not your actual policy. The repo's robots.txt
is correct; the Cloudflare overlay is wrong for your use case.

## After the fix

Re-run the IndexNow ping so search engines re-crawl now that AI bots
are no longer blocked at the policy layer:

```
python indexnow_ping.py
```

(IndexNow targets Bing/Yandex/etc., not the AI bots, but it forces a
re-crawl of pages that may have been mis-indexed previously.)

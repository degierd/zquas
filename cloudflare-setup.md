# Cloudflare configuration for zquas.ai

The site is hosted on GitHub Pages with Cloudflare in front (proxied / orange cloud).
This file covers the Cloudflare-side configuration that complements the site.

Each section is self-contained. Skip what you do not want.

---

## 1. Confirm the proxy is on (1 minute)

Cloudflare dashboard -> zquas.ai -> DNS -> Records.

The `zquas.ai` and `www.zquas.ai` records should both have the orange cloud
icon (Proxied). If they are grey (DNS only), Cloudflare Rules and caching
do nothing and you should turn the proxy on.

If you are running into HTTPS edge cases with GitHub Pages, set:
- SSL/TLS -> Overview -> "Full" (not "Full (strict)" unless you have set
  up the GitHub Pages cert-and-Cloudflare-cert chain, which is fiddly).

---

## 2. Fix MIME types for the feeds (3 minutes)

Cloudflare dashboard -> zquas.ai -> Rules -> Transform Rules ->
Modify Response Header -> Create rule.

Create two rules.

### Rule A: feed.xml

- Rule name: `RSS Content-Type`
- When incoming request matches:
  - URI Path **equals** `/feed.xml`
- Then:
  - **Set static** header `content-type` to `application/rss+xml; charset=utf-8`

Click Deploy.

### Rule B: atom.xml

- Rule name: `Atom Content-Type`
- When incoming request matches:
  - URI Path **equals** `/atom.xml`
- Then:
  - **Set static** header `content-type` to `application/atom+xml; charset=utf-8`

Click Deploy.

(Manifest, JSON, and the .well-known/security.txt path are already correct
once `.nojekyll` lands in the repo and GitHub re-deploys.)

---

## 3. Add security headers (5 minutes)

Cloudflare dashboard -> zquas.ai -> Rules -> Transform Rules ->
Modify Response Header -> Create rule.

- Rule name: `Security headers (all routes)`
- When incoming request matches: hostname equals `zquas.ai` (or use the
  catch-all "All incoming requests")
- Add headers (one per Set static action):

| Header                          | Value                                                                                              |
|---------------------------------|----------------------------------------------------------------------------------------------------|
| `strict-transport-security`     | `max-age=31536000; includeSubDomains; preload`                                                     |
| `x-content-type-options`        | `nosniff`                                                                                          |
| `referrer-policy`               | `strict-origin-when-cross-origin`                                                                  |
| `permissions-policy`            | `camera=(), microphone=(), geolocation=(), payment=(), usb=(), interest-cohort=()`                 |
| `x-frame-options`               | `DENY`                                                                                             |

Click Deploy.

These give you the security checklist most penetration testers expect to
see, signal seriousness to compliance buyers, and improve a site's
SecurityHeaders.com grade from C/D to A/A+.

Skip `Content-Security-Policy` for now -- the site uses inline styles
and Google Fonts; a tight CSP needs careful crafting and breaks easily.
Worth a follow-up commit later.

After deploying, submit https://zquas.ai for HSTS preloading at
https://hstspreload.org -- this hardcodes HTTPS into Chrome, Edge, and
Firefox.

---

## 4. /blog redirect to /articles.html (2 minutes)

Cloudflare dashboard -> zquas.ai -> Rules -> Redirect Rules ->
Create rule.

- Rule name: `/blog -> /articles`
- When incoming request matches:
  - URI Path **starts with** `/blog`
- Then:
  - Type: Static
  - URL: `https://zquas.ai/articles.html`
  - Status code: 301
  - Preserve query string: yes

Click Deploy.

(Optional follow-ups for vanity URLs:
- `/positions/article-75` -> `/article-75.html`
- `/paper` -> `/article-75.html`
- `/onepager` -> `/zquas-onepager.pdf`
Set these up the same way if useful.)

---

## 5. Cache rules (3 minutes)

Cloudflare's defaults are fine, but two specific tweaks help:

### A. Cache the feeds for 5 minutes (so feed readers do not pound origin)

Caching -> Cache Rules -> Create rule.
- Rule name: `Cache feeds`
- When incoming request matches: URI Path is in `/feed.xml`, `/atom.xml`,
  `/sitemap.xml`, `/llms.txt`, `/facts.json`
- Then: Eligible for cache, Edge TTL: 5 minutes, Browser TTL: 5 minutes

### B. Cache fonts and images aggressively

Cloudflare already does this via its default behaviour, but if you want
to be explicit:
- Match: file extension is `png`, `jpg`, `jpeg`, `webp`, `svg`, `ico`,
  `woff`, `woff2`
- Then: Edge TTL 1 month, Browser TTL 1 day

---

## 6. Cloudflare Web Analytics (5 minutes, optional but recommended)

Cookieless. GDPR-clean. Free up to 10M page views/month. No banner needed.
Replaces Google Analytics for a privacy-positioned product like ZQUAS.

1. Cloudflare dashboard -> zquas.ai -> Analytics & Logs -> Web Analytics.
2. Click "Add a site" if not already enabled. Choose the "Automatic"
   option, which injects the beacon at the edge with no code changes.
3. After ~24 hours, traffic data starts populating.

If you prefer a script tag approach (so the beacon is in the HTML and
visible to anyone inspecting the page), Cloudflare gives you a snippet
like this:

```html
<script defer src="https://static.cloudflareinsights.com/beacon.min.js"
        data-cf-beacon='{"token": "PUT_YOUR_TOKEN_HERE"}'></script>
```

If you want the script-tag version on the site, send me the token and
I will add it to every page footer just before `</body>`.

---

## 7. Bot Fight Mode (1 minute, optional)

Security -> Bots -> Bot Fight Mode: ON.

Blocks low-quality scrapers and content theft bots automatically. Does
not affect Googlebot, Bingbot, or any of the AI bots we explicitly
allowed in robots.txt.

Note: if bots that should be allowed start hitting CAPTCHAs, switch to
the more conservative "Super Bot Fight Mode" settings (paid plan only)
or turn it off.

---

## 8. Email routing (already on Gmail, optional)

Cloudflare's Email Routing can forward `*@zquas.ai` addresses to your
Gmail without you setting up a real mailbox per address. Useful for
the addresses I have referenced in site files:

- `security@zquas.ai` (referenced in security.txt)
- `careers@zquas.ai` (referenced in the playbook for the careers page)
- `press@zquas.ai` (suggested in the playbook for the press page)

Email -> Email Routing -> Routes -> Add route. One route per address.
All can forward to your Gmail.

---

## After deployment

Run these to verify everything works:

```
curl -I https://zquas.ai/feed.xml
# Should show: content-type: application/rss+xml; charset=utf-8

curl -I https://zquas.ai/.well-known/security.txt
# Should show: 200 OK, content-type: text/plain

curl -I https://zquas.ai/blog/anything
# Should show: 301, location: https://zquas.ai/articles.html

curl -I https://zquas.ai/ | grep -i strict-transport
# Should show: strict-transport-security: max-age=31536000...
```

If any check fails, the rule did not deploy correctly. Most common
cause: typo in the URI Path matcher.

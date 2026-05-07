# Deploying the zquas.ai edge worker

`worker.js` in this directory is a single Cloudflare Worker that does
three things at the edge:

1. Adds RFC 8288 `Link` response headers on every HTML page.
2. Honours `Accept: text/markdown` content negotiation by serving the
   pre-generated `.md` twin of any HTML page.
3. Overrides `Content-Type` for paths where GitHub Pages defaults are
   wrong (`api-catalog` -> `application/linkset+json`, `feed.xml` ->
   `application/rss+xml`, etc.).

## One-time deployment (5 minutes)

1. Cloudflare dashboard -> **Workers & Pages**.
2. Click **Create** -> **Hello World** template -> any name (e.g.
   `zquas-edge`).
3. Replace the template's `worker.js` with the contents of
   `cloudflare-worker/worker.js` from this repo.
4. Click **Deploy**.
5. Open the worker -> **Settings** -> **Triggers** -> **Routes** ->
   **Add route**:
   - Zone: `zquas.ai`
   - Route: `*zquas.ai/*`
6. Click **Save**.

## Verify (1 minute)

```
# 1. Link header present on the homepage
curl -sI https://zquas.ai/ | grep -i ^link

# 2. Markdown content negotiation works
curl -sH "Accept: text/markdown" -I https://zquas.ai/article-75.html | grep -i content-type
# Expect: content-type: text/markdown; charset=utf-8

# 3. Default HTML still works
curl -sI https://zquas.ai/article-75.html | grep -i content-type
# Expect: content-type: text/html; charset=utf-8

# 4. API catalog has the right MIME type
curl -sI https://zquas.ai/.well-known/api-catalog | grep -i content-type
# Expect: content-type: application/linkset+json; charset=utf-8

# 5. RSS feed has the right MIME type
curl -sI https://zquas.ai/feed.xml | grep -i content-type
# Expect: content-type: application/rss+xml; charset=utf-8
```

## Updating the worker

When this file changes (e.g. you want a new Link relation, new MIME
override), open the worker in the Cloudflare dashboard, paste the new
`worker.js`, and click Deploy. Routes do not need to be reconfigured.

## Why a Worker instead of Transform Rules

Transform Rules can do MIME type and header injection too. The worker is
chosen here because:

- It is one config artefact in the repo (worker.js) that travels with
  the code, instead of a list of UI clicks documented in a separate
  markdown file.
- Markdown content negotiation needs server logic (read Accept header,
  fetch a different upstream URL). Transform Rules cannot do that.
- The MIME overrides and the Link headers can live alongside the
  negotiation logic.

If you do not want to run a Worker, the Transform Rule equivalents are
documented in `cloudflare-setup.md` -> sections 2 (MIME types) and 9
(Link headers + Markdown). Cloudflare's native "Markdown for Agents"
feature can replace the negotiation logic entirely. The Worker is the
most flexible option; the others are progressively simpler tradeoffs.

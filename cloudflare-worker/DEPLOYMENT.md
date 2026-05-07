# Deploy the zquas.ai edge worker

Run two commands. Cloudflare handles the rest.

## Prerequisites

- Node.js 20 or newer.
  - Check: `node --version`
  - Install if needed: https://nodejs.org/ (LTS).

That is the only prerequisite. Wrangler installs itself via `npm`, and
it logs into Cloudflare via your browser the first time it runs.

## Two commands

Open a terminal in the repo root.

```
cd cloudflare-worker
npm install
npx wrangler deploy
```

**What you will see:**

1. `npm install` downloads Wrangler into `node_modules/`. Takes ~30s.
2. `npx wrangler deploy` opens a browser tab the first time you run
   it, asking you to authorise Wrangler against your Cloudflare
   account. Click **Allow**. The terminal then proceeds.
3. Wrangler reads `wrangler.toml`, uploads `worker.js`, creates the
   Worker called `zquas-edge`, and binds it to the routes
   `zquas.ai/*` and `www.zquas.ai/*`. Output ends with
   `Current Version ID: <some-uuid>` and the deployed URL.

That is the whole deploy. The Worker is now live on every request to
zquas.ai.

## Verify (1 minute)

```
curl -sI https://zquas.ai/ | grep -i ^link
# Expect: link: </llms.txt>; rel="describedby"...

curl -sH "Accept: text/markdown" -I https://zquas.ai/article-75.html | grep -i content-type
# Expect: content-type: text/markdown; charset=utf-8

curl -sI https://zquas.ai/.well-known/api-catalog | grep -i content-type
# Expect: content-type: application/linkset+json; charset=utf-8

curl -sI https://zquas.ai/article-75.html | grep -i content-type
# Expect: content-type: text/html; charset=utf-8 (browsers still get HTML)
```

If all four match, you are done.

## Updating the Worker later

Whenever `worker.js` changes:

```
cd cloudflare-worker
npx wrangler deploy
```

That is it. No re-routing, no DNS changes.

## Watching logs in real time

```
cd cloudflare-worker
npx wrangler tail
```

Streams every request's status code, latency, and any console output
from the Worker. Useful when debugging.

## What if something goes wrong

- **`Authentication error` from Wrangler:** Re-run, choose
  `npx wrangler login` first if it does not auto-prompt.
- **`Zone "zquas.ai" not found in your account`:** the Cloudflare
  account you authorised does not own the `zquas.ai` zone. Authorise
  the right account: `npx wrangler logout`, then redeploy.
- **Worker deployed but site looks broken:** disable the routes from
  Cloudflare dashboard -> Workers & Pages -> `zquas-edge` ->
  Settings -> Triggers -> remove the routes. The site reverts to
  un-Worker'd in seconds. Then debug locally with
  `npx wrangler dev` (runs the Worker on http://localhost:8787 with
  zquas.ai responses proxied through it).

## What this avoids

The dashboard upload page you saw earlier (the drag-and-drop one) is
Cloudflare's static-site uploader. It refuses Worker scripts because
those need server-side execution, not static hosting. Wrangler is the
official path for Workers. The dashboard "Create Worker" flow is also
fine, but it requires manually pasting the file in and clicking
through routes -- this CLI path does it in two commands.

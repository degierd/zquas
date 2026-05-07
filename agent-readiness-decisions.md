# Agent-readiness scorecard: what we shipped, what we skipped

This file documents which items from the agent-readiness scan we
implemented, which we deliberately skipped, and why. Future maintainers
should not rebuild the skipped items just to chase the score; each was
a conscious decision based on what ZQUAS actually is.

## Implemented

### Link response headers (RFC 8288) — DONE
Cloudflare Worker (`cloudflare-worker/worker.js`) injects Link headers
advertising llms.txt, llms-full.txt, facts.json, agent-skills index,
api-catalog, sitemap, feeds, glossary, and security policy on every
HTML response.

### Markdown content negotiation — DONE
Two ways:
1. Pre-generated `.md` twin for every HTML page at the same path with
   `.md` suffix (45 files). Always available at a stable URL.
2. The Worker also honours `Accept: text/markdown`: if an agent asks
   for markdown on an `.html` URL, the Worker serves the `.md` twin
   with `Content-Type: text/markdown`.

`generate_markdown.py` rebuilds the twins. `rebuild_artifacts.py`
orchestrates this with the other artefact generators.

### API Catalog (RFC 9727) — DONE
`/.well-known/api-catalog` served as `application/linkset+json` (MIME
type set by the Worker since GitHub Pages does not know that type).
The linkset advertises our knowledge resources rather than a
traditional REST API: llms.txt, facts.json, agent-skills index,
sitemap, feeds, glossary.

This is honest use of RFC 9727. The RFC is generic; "API" includes
any machine-callable resource. Publishing fake REST endpoints would
be lying.

### Agent Skills index (RFC v0.2.0) — DONE
`/.well-known/agent-skills/index.json` with nine knowledge skills,
each with a sha256 digest. `generate_agent_skills.py` rebuilds the
file with fresh hashes after any content change.

### Content-Signal directives in robots.txt — DONE
`Content-Signal: search=yes, ai-train=yes, ai-input=yes` declared per
the IETF Content Signals draft. Our policy is open access; the
directive makes that machine-readable.

---

## Skipped — with reasoning

### OAuth/OIDC discovery — SKIPPED

**Specs:** `/.well-known/openid-configuration`, `/.well-known/oauth-authorization-server`

**Why not:** ZQUAS has no public APIs that require authentication. The
website is a static knowledge surface. Publishing OAuth discovery
metadata for endpoints that do not exist would be lying to agents.
Agents that try to authenticate against fake endpoints will fail
noisily and that hurts our reputation more than the scorecard tick is
worth.

**When to revisit:** if we ever publish a public API (e.g. a
proof-bundle verification API, or an FCNS detection scoring API for
researchers), this becomes relevant. Until then, skip.

### OAuth Protected Resource — SKIPPED

**Spec:** `/.well-known/oauth-protected-resource` (RFC 9728)

**Why not:** Same as OAuth discovery. We have no protected resources.
There is nothing on this domain that requires a token. Publishing
protected-resource metadata for unprotected resources is incoherent.

**When to revisit:** alongside any OAuth deployment.

### MCP Server Card — DEFERRED, NOT SKIPPED

**Spec:** `/.well-known/mcp/server-card.json` (SEP-1649)

**Why deferred:** An MCP server is a real engineering project, not a
scorecard hack. The right MCP server for ZQUAS would expose our
knowledge as readable resources (position papers, glossary entries,
facts.json) so a Claude Desktop user could connect to `mcp.zquas.ai`
and ask grounded questions. This is genuinely useful. It is not
five minutes of work; it requires:

- A Worker or hosted endpoint that speaks the MCP protocol.
- Resource handlers that fetch and stream our content.
- Tool handlers if we want agents to be able to search the corpus.
- A capability declaration matching what we actually implement.

Publishing a server-card pointing at a non-functional endpoint would
fail the moment any agent tried to connect.

**When to revisit:** when we have time to build a proper MCP server
(estimate: 1-2 days of focused work). At that point the server-card
follows naturally.

### WebMCP — SKIPPED

**Spec:** `navigator.modelContext.registerTool()` in browser
JavaScript.

**Why not:** WebMCP exposes browser-side tools (search, navigate,
data retrieval actions) to AI agents that browse the page. ZQUAS is
a static knowledge site. There are no actions to expose. Adding
fake tools would mean either:

- Tools that pretend to do something but return canned data (lying
  to agents).
- Tools that wrap our existing static content (better served by
  llms.txt and the agent-skills index, both of which we already
  have).

The site is also intentionally JavaScript-light. Adding a JS
runtime requirement just to register tools no one will use is the
wrong tradeoff.

**When to revisit:** if we add a meaningful interactive surface
(e.g. an interactive proof-bundle verifier in the browser), WebMCP
to expose its actions becomes the right tool.

### Web Bot Auth (HTTP Message Signatures Directory) — SKIPPED

**Spec:** `/.well-known/http-message-signatures-directory`

**Why not:** Web Bot Auth is for sites that need to authenticate
incoming bot traffic via HTTP message signatures. We deliberately
opened access to all bots in robots.txt. Authenticating them is the
opposite of what we want.

**When to revisit:** never, given current strategy.

---

## Commerce protocols — ALL SKIPPED

x402, MPP, UCP, ACP. All assume a machine-to-machine commercial
transaction surface. ZQUAS sells via human conversations to bank
procurement teams. There is no machine-purchasable surface and there
will not be one in the foreseeable future. Skip all.

---

## Score expectation

After Cloudflare Worker deployment (which the user does once, then
forgets), the scorecard should move from 25 (Level 1) to roughly:

- Discoverability: 3/3 (Link headers, sitemap, robots.txt)
- Content: 1/1 (markdown negotiation)
- Bot Access Control: 2/2 (AI bot rules, content signals)
- API/Auth/MCP/Skill: 2/6 (api-catalog, agent-skills) — the rest are
  honest skips
- Commerce: not applicable

Aggregate: roughly 60-65%. We will never hit 100% without lying. The
items we skipped would actively degrade the site if implemented
dishonestly.

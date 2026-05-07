# Screenshot Mission for the Engine Codebase Claude Code Session

Paste the prompt below into a Claude Code session that has access to the
ZQUAS engine codebase (the one with the Playwright UI tests). The prompt
is self-contained: it explains what is needed, why, where to put the
output, and what quality bar to hit.

The website repo (zquas-website) needs operational proof assets to ship
alongside the architecture-heavy prose. ChatGPT reviewed the website and
flagged that the site relies too heavily on prose with too few visual
demonstrations. This mission produces those visuals.

---

## PROMPT TO PASTE

You are working in the ZQUAS engine codebase. The public website
(`C:\dev\zquas-website`) needs screenshots of the live UI to use as
operational proof. An external review of the website flagged that it
is architecture-heavy and outcome-light. Real screenshots of the
running system close that gap.

You already have Playwright tests for the UI. Use the existing fixtures
and selectors. Do not invent test data; use whatever the existing
Playwright suite uses. If the suite has a "demo data" or "seed" mode,
use that.

### What to produce

Eight screenshots, each saved as a 1600x1000 PNG (or the closest
reasonable native viewport for the engine's UI), retina/high-DPI
rendering enabled. Output to `C:\dev\zquas-website\screenshots\`,
filenames as listed.

1. **`alert-lifecycle.png`** -- the alert detail screen. An entity
   that has triggered a policy. Show: entity ID, risk score, the
   policy that fired, the verdict, the timestamp, and the "verify
   proof bundle" affordance. Pick an alert with realistic context
   (transactions, counterparties, jurisdiction) so it looks like
   real compliance work, not a placeholder.

2. **`policy-evaluation.png`** -- the policy bytecode evaluation
   view. The compliance policy language source on the left, the
   compiled bytecode or evaluator state on the right. Or whatever
   our equivalent surface is. The point is: a compliance officer
   can read the policy that fired in plain English.

3. **`entity-graph.png`** -- the GPU-resident entity graph
   visualisation. Multiple linked entities across counterparties.
   At least 30-50 nodes visible with edges. Risk-weighted shading
   if the UI supports it.

4. **`federation-round.png`** -- the cross-institutional federation
   dashboard. Two participating institutions, an in-progress or
   recently completed bilateral MPC round, the elapsed time, and
   the dual Ed25519 attestation status. If we have a real-time
   progress view, capture it mid-round so it is obvious work is
   happening.

5. **`benchmark-throughput.png`** -- the live throughput dashboard
   while running the 500K entities x 100 policies workload. CEPS
   gauge, latency histogram, GPU utilisation. Capture during a
   sustained run, not idle.

6. **`proof-bundle.png`** -- a single cryptographic proof bundle,
   either in the UI's proof viewer or in a hex/structure dump
   from our standalone CLI verifier. Show: policy hash, input
   hash, verdict, Merkle root, Ed25519 signature, total byte
   count (912). The supervisor-side verification view is the
   strongest framing.

7. **`regulator-verifier.png`** -- the standalone CLI verifier
   running in a terminal. Input: a proof bundle path. Output:
   `VALID` (green) plus the structured verification report. This
   is the single most differentiated capability ZQUAS has and
   we do not show it visually anywhere on the site yet.

8. **`fcns-typology-detection.png`** -- the FCNS (Financial Crime
   Network Simulator) results view, showing one of the four FATF
   typologies being detected. Detection rate, false positive rate,
   benchmark conditions visible.

### Quality bar

- Real-looking compliance data. No "Lorem Ipsum", no `Acme Corp
  Customer 1`. Use the existing seeded test fixtures, which are
  designed to look credible.
- Dark theme if the UI supports it (the website is dark; mismatched
  light-mode screenshots will look out of place).
- Hide any obvious internal codenames in window titles, dialog
  headers, or tooltips that appear in the screenshot. The website
  prohibits the public-facing names listed in the website's
  CLAUDE.md (Prometheus, Noumenon, Themis, Janus, Synapse,
  F1Runtime, ZAPB, Apex, Chimera, Eidolon). If the UI itself shows
  these, either pick a screen that doesn't, or use Playwright's
  `page.locator(...).textContent =` / DOM patching to swap them
  for descriptive English before screenshotting. Examples of
  acceptable replacements:
  - "Prometheus" / "Noumenon" / "Themis" -> "the engine" / "the
    policy evaluator"
  - "ZAPB" / "Zero-Trust Adjudication Proof Bundle" ->
    "cryptographic proof bundle"
  - "F1 engine" -> "ZQUAS engine"
- No real customer PII even if the test data is synthetic. Names
  like "Maria Vasquez" are fine; anything that looks like an
  actual real person, account number, or IBAN must be reviewed.
- 16:10 aspect ratio (or whatever matches the existing engine UI's
  primary breakpoint).
- Cursor hidden in screenshots.

### Implementation notes

- Add a Playwright spec file: `tests/e2e/website-screenshots.spec.ts`
  (or `.js`, match the existing convention).
- Run only this spec when capturing: `npx playwright test
  website-screenshots --headed=false` (or whatever the project's
  conventions dictate).
- Use `page.screenshot({ path: '<absolute path>', fullPage: false,
  scale: 'css' })` so the size is predictable.
- For the CLI screenshot, you can either (a) screenshot a real
  terminal via the engine's existing terminal-output test
  helpers if they exist, or (b) render the verifier output into
  a styled HTML page first and screenshot that. Option (a) is
  preferred; option (b) is acceptable as a fallback if no
  terminal-capture helper exists.

### What to deliver back

When done:
1. Confirm the eight files exist at the target paths and report
   their dimensions.
2. Open one of them inline (Read tool) and report whether the
   data on screen passes the quality bar.
3. List any screenshots you could not produce and why (so the
   website team can adapt the page that was going to use them).
4. Do NOT commit the screenshots from this codebase. The website
   repo will commit them on its side after the website team
   reviews them.

### Why this matters

The website currently relies on prose to convey what the engine
does. A bank's Head of AML who has 90 seconds on the site needs
to see compliance work happening, not read about it. These eight
screenshots are the operational proof layer the site is missing.

Be careful, be real, do not fake data. If a screen does not look
credible to a Tier-1 bank compliance officer, do not ship it.
Report instead, and we will adjust the website page rather than
the screenshot.

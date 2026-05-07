# ZQUAS SEO and Distribution Playbook

This is the action list for getting ZQUAS visible across the web. Items
marked **DONE** are already shipped on the site. Items marked **YOU**
require your accounts; I cannot do them for you. Items marked **ASK**
are decisions I need from you before I can proceed.

The order is roughly highest-leverage first.

---

## Already shipped on the site (DONE)

- llms.txt and llms-full.txt at root, listed in robots.txt
- facts.json (machine-readable fact sheet)
- glossary.html with DefinedTermSet + FAQPage JSON-LD
- FAQPage JSON-LD on the homepage
- BreadcrumbList JSON-LD on every article and key page
- Article JSON-LD enriched with image, language, accessibility flags
- og:site_name, og:locale, theme-color, application-name on every page
- manifest.webmanifest (PWA-style icon and theme metadata)
- humans.txt (signals real humans)
- security.txt at /.well-known/security.txt (RFC 9116)
- RSS 2.0 feed at /feed.xml
- Atom 1.0 feed at /atom.xml
- Sitemap with image:image namespace, includes feeds and machine docs
- robots.txt: open to all AI bots (training and retrieval)
- IndexNow key file at root (for instant Bing/Yandex/Naver/Yep notify)
- indexnow_ping.py script (run after pushing content updates)

---

## Search engine submission (YOU, 30 minutes total)

These are one-time. Each gives the search engines explicit permission and
a signed sitemap.

### 1. Google Search Console (highest priority)

1. Go to https://search.google.com/search-console
2. Add property: `https://zquas.ai` (Domain property if you can prove
   DNS ownership; URL prefix property otherwise)
3. Verification: Google will give you a DNS TXT record OR an HTML file
   `googleXXXXXXXXXXXXXXXX.html`. If they give you a file, paste its
   contents into a new file at the root with that exact filename and
   ask me to commit it.
4. Once verified, submit the sitemap: `sitemap.xml`
5. Inspect the URL `https://zquas.ai/` and request indexing.

**Useful follow-ups inside Search Console:**
- Performance tab: discover the queries actually bringing traffic.
- Coverage: spots where Google can't crawl (set this aside; the site
  is small and clean, there should be nothing to fix).
- Enhancements: confirm the BreadcrumbList, FAQ, and Article rich
  results are detected.

### 2. Bing Webmaster Tools

1. Go to https://www.bing.com/webmasters
2. Add `https://zquas.ai`
3. **Shortcut:** Bing accepts "Import from Google Search Console" once
   you have GSC set up. Use that.
4. Submit sitemap.xml.
5. Bing routes IndexNow submissions automatically once verified, so
   the `indexnow_ping.py` script will work.

### 3. Yandex Webmaster

1. Go to https://webmaster.yandex.com
2. Add `https://zquas.ai`
3. Verify (DNS TXT or meta tag).
4. Submit sitemap.xml.
5. (Yandex matters for European compliance research and is one of the
   IndexNow consumers.)

### 4. DuckDuckGo

DuckDuckGo crawls Bing's index. No separate submission needed. Verify
appearance after Bing has indexed the site (usually 7-14 days).

### 5. Brave Search

Brave runs its own index. Submit at https://search.brave.com/help/
webmaster (no sitemap submission portal as of this writing; ensure
robots.txt allows `BraveBot` and the sitemap is discoverable).

---

## AI search engine submission (YOU, where applicable)

### 6. ChatGPT search

Already crawled by `OAI-SearchBot` and `ChatGPT-User`, both allowed in
robots.txt. No portal submission. After GSC + Bing are configured,
ChatGPT search picks up the site within days.

### 7. Perplexity

Already crawled by `PerplexityBot`. No portal. To accelerate visibility:
ask a few specific questions in Perplexity (e.g. "what is AMLR Article
75", "who builds federated AML detection") and click through to ZQUAS
when it appears. Perplexity uses click-through as a ranking signal.

### 8. Claude (Anthropic)

Already crawled by `ClaudeBot`. No portal.

---

## High-value external manifestations (YOU, 1-3 hours each)

These are where ZQUAS becomes citable from outside its own domain. Each
significantly compounds AI training and search visibility.

### 9. Wikipedia

Wikipedia is the single highest-authority backlink class. **Do not
create a "ZQUAS" article**, that gets deleted as promotional. Instead:

- **Edit existing articles** where ZQUAS is a legitimate citation:
  - "Anti-Money Laundering Regulation (European Union)" — add a
    sentence about MPC-based privacy-preserving alternatives to
    centralised data sharing, with article-75.html as the citation.
  - "Multi-party computation" — add ZQUAS under "Applications".
  - "Transaction Monitoring Netherlands" (if it exists; if not,
    consider creating it as a balanced article about TMNL itself,
    citing the tmnl.html analysis).

Rules: third-person, neutral tone, no marketing language, real
citations. Use the talk page if your edit is reverted; explain why
the citation strengthens the article.

### 10. arXiv preprint

The biggest credibility lift available to deep-tech. Two candidate
papers:

- **"FCNS: A Falsifiable Benchmark for AML Detection Accuracy"** —
  the synthetic financial crime network simulator, methodology, and
  detection results. Strongest first publication because it solves
  a problem nobody else in AML has solved (a falsifiable benchmark).
- **"GPU-Native Multi-Party Computation for Real-Time Transaction
  Monitoring"** — the cryptographic engineering side: ECDH-PSI on
  Curve25519, IKNP OT extension, latency budget, throughput results.

Submission:
1. Need an arXiv endorsement (you may already have one through
   academic contacts; if not, this is the first ask).
2. Use cs.CR (cryptography) or cs.CY (computers and society) as
   primary category.
3. arXiv DOIs are crawled by Google Scholar within 48 hours.

### 11. GitHub

You said the engine is private. Consider a separate **public**
repository for one of:

- The FCNS benchmark dataset and scoring tools (no engine code, just
  the synthetic data generator, criminal scenario specs, and scoring
  CLI). Massive credibility boost. If it gets stars from the
  fintech/security community, that becomes social proof on every
  pitch deck.
- A standalone proof bundle verifier CLI. Open source the verifier
  but not the engine. This is the strongest "verify, don't trust"
  demonstration: any regulator can audit the code that audits ZQUAS.
- Reference compliance policies in the policy language, with worked
  examples of Wwft, BSA, and AMLR scenarios.

GitHub repositories with active commits, README, and issues get
indexed strongly by all major search engines and AI training pipes.

### 12. Crunchbase

Free company profile. Banks and investors look here first.
- https://www.crunchbase.com/add-organization
- Add: name, URL, founder, location, funding stage, brief
  description, the FCA Digital Sandbox milestone, NVIDIA Inception.
- Keep "founded" date accurate (2024) and stage honest (pre-seed /
  pilot-ready).

### 13. LinkedIn Company Page

Already implicit through Danny's profile. A separate ZQUAS company
page lets people follow updates, lets ZQUAS appear in employee/
follower searches, and gives Danny's posts a "company tag" for
algorithmic boost. Free, 15 minutes.

### 14. AngelList / Wellfound

If you intend to fundraise or hire, this is where investors and
engineers look.

### 15. Gartner / IDC / industry analyst briefings

Long-tail credibility. Mid-priority. For each major analyst covering
fintech compliance (Gartner Magic Quadrant for Anti-Money Laundering
Solutions; IDC FinTech Rankings), submit a vendor briefing request.
Free for vendors. Even being mentioned in a Magic Quadrant footnote
is gold for procurement teams.

### 16. F6S / EU-Startups / Sifted directory listings

Free, lightweight, and these listings get indexed. Worth 10 minutes
of forms-filling each.

### 17. Product Hunt — DO NOT yet

Product Hunt audiences are consumer/B2C. AML compliance is wrong fit.
Skip until there is a self-service product surface.

### 18. Hacker News

When the FCNS benchmark or the MPC paper publishes, post once with
"Show HN: " or a clean link to the arXiv paper. Do NOT post
marketing pages. HN flags marketing fast and the negative signal
sticks.

---

## Compliance and finance specialist directories (YOU)

These are smaller-traffic but extremely targeted. Each gets you in
front of the right buyer.

### 19. RegTech directories

- https://regtechmarketplace.com — submit ZQUAS as a vendor
- https://regtechanalyst.com — request inclusion in their RegTech 100
- https://www.gowlingwlg.com — RegTech Innovation Hub (UK)

### 20. Compliance directories

- ACAMS (Association of Certified Anti-Money Laundering Specialists)
  vendor directory. Danny is likely already a member. Free for
  members.
- ICA (International Compliance Association) — Danny holds the
  PgDip. Member directory may accept vendor listings.

### 21. EU regulatory innovation pages

- DNB InnovationHub — already engaged. Confirm whether the public
  innovation portfolio page lists ZQUAS.
- EBA Innovation Hub — submit if not already.
- ECB market consultation participation lists — when ECB consults on
  AML, AI in finance, or pseudonymisation guidance, submit a
  response. Responses are public and cite the responding entity.

### 22. NVIDIA Inception ecosystem pages

You're a member. Check that the NVIDIA Inception company finder lists
ZQUAS, with up-to-date description and link.

---

## Backlink hygiene and authority building (YOU + ME)

### 23. Speaking, podcasts, guest articles

The fastest organic backlink growth for a deep-tech B2B is appearing
on industry podcasts and writing guest articles. For each, the host
links back to your site, which compounds.

Targets that match ZQUAS profile:
- AML Talk (podcast)
- KYC360 articles
- Risk.net opinion column
- The Banker thought-leadership pieces
- Compliance Week
- AltFi
- Sifted (European startup focus)

I can draft pitches for any of these if you'd like.

### 24. Conference speaking

- Money 20/20 Europe (June, Amsterdam) — apply for Compliance track
- Sibos (annual SWIFT conference) — vendor showcase
- ACAMS Europe Conference
- DNB Innovation Days (if you're already engaged with the
  InnovationHub, ask for a speaking slot)

Speaker bios always include the company URL. That's a backlink from
a high-authority domain.

### 25. Citations from academic and industry research

When researchers write about MPC for AML, federated learning for
finance, or privacy-preserving compliance, they need real-world
references. The arXiv paper (#10) makes ZQUAS a natural citation.

---

## Technical SEO follow-ups (ASK ME — I need a decision)

### 26. Should I add a /blog or /news redirect?

Some search engines weight `/blog/` paths slightly. We have
`/articles.html`. We could add `Disallow:` for nothing and add a
permanent 301 from `/blog` to `/articles.html`, but it requires
hosting-level config (htaccess or equivalent). **ASK:** what hosting
are we on? Static host (Netlify, Vercel, Cloudflare Pages) or
something else?

### 27. Should I add a careers page placeholder?

Even a single page saying "We are not hiring publicly yet. If you
combine deep regulatory experience with GPU systems programming or
applied cryptography, write to careers@zquas.ai" gets crawled by
LinkedIn, Glassdoor, hire-tech aggregators. **ASK:** ship?

### 28. Should I auto-run indexnow_ping.py from a git hook?

Could add a post-push git hook that pings IndexNow whenever the
remote is updated. **ASK:** want it? Otherwise you can run it
manually after pushes that change content.

### 29. Should I add a JSON-LD `Service` schema for the engine?

Schema.org has a `Service` type that lets you describe a business
service to search engines. Useful for B2B. **ASK:** want it?

### 30. Should I generate a /press page?

A static page with logo assets, founder photo, boilerplate, key
facts, recent news. Expected by every journalist. **ASK:** ship?

---

## Things I deliberately did NOT do

- **No automated link building or directory spam.** It hurts more
  than it helps.
- **No tracking pixel installation.** We have no cookie banner
  because we set no cookies; that's a feature for a privacy-focused
  product. If you want analytics, I recommend Plausible or
  Cloudflare Web Analytics (cookieless, GDPR-clean) — but that's
  your decision.
- **No paid SEO tools.** Ahrefs, SEMrush, Moz are useful but cost
  money and need your decision.

---

## Suggested first 90 minutes

If you want one focused session this week:

1. (10 min) Set up Google Search Console. Submit sitemap.
2. (5 min) Set up Bing Webmaster (import from Google).
3. (15 min) Crunchbase profile.
4. (15 min) LinkedIn ZQUAS Company Page.
5. (30 min) Pick one Wikipedia article to enrich with a single
   well-cited sentence.
6. (15 min) Run `python indexnow_ping.py` after the next push.

Total search-engine and AI visibility uplift from those six steps:
substantial. Each compounds with the next.

After that, the next 3 hours of effort are best spent on either the
Wikipedia edits or the FCNS arXiv paper, depending on your time.

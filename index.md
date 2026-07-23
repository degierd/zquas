# ZQUAS — Sovereign Compliance Infrastructure

> GPU-native compliance engine for financial institutions. Cross-institutional detection without central data pooling.

Source: https://zquas.ai
Site: https://zquas.ai

---
[

                    FCA Supercharged Sandbox · Second Cohort · July 2026 →
                ](article-fca-sandbox.html)


# 
                    Criminals move money

                    across banks.

                    You only see yours.




                    ZQUAS detects cross-institutional laundering patterns
                    without sharing a single byte of customer data.




                    Privacy-preserving multi-party computation across participating banks.



                    [Read the Position Paper →](article-75.html)
                    [Founding Partner Programme](founding-partner.html)

                [Download One-Pager (PDF)](zquas-onepager.pdf)



                    Supervisory replay
                    standalone verifier


                    $ zquas-verify --epoch 2026-07
                    policies100 evaluated · deterministic replay
                    entities500,000 scored in 1,170 ms
                    alertingestion to triage in 3.92 ms
                    federationbilateral round 7.8 s at 100K entities
                    proof912-byte bundle · Ed25519 signed
                    resultVERIFIED · byte-identical replay

                [Every number measured. See the benchmark ↗](benchmark.html)



            Accepted into the FCA Digital Sandbox · March 2026
            DNB InnovationHub · Submission under review
            NVIDIA Inception program member
            12,342 automated tests




        Primary Documents

            [

                    Position Paper
                    HTML · 12 min read

                What Article 75 Was Afraid to Permit
                Cross-institutional AML detection without sharing personal data. Legal analysis, MPC architecture, measured benchmark results, and a proposal for regulatory sandbox engagement.
            ](article-75.html)
            [

                    Technical Benchmark
                    HTML · Verified results

                Federation Performance Across the Full Dutch Banking Sector
                500,000 entities in under 2 seconds. 150 million+ evaluations per second. Alert lifecycle under 10ms. NVIDIA RTX 5090. Every result signed.
            ](benchmark.html)
            [

                    Engineering Standards
                    HTML · Technical

                Cryptographic Architecture and Security Model
                ECDH-PSI, garbled circuits, oblivious transfer. AES-256-GCM transport. Ed25519 attestation. Adversarial threat model with 37 findings identified and remediated.
            ](engineering.html)
            [

                    Programme Document
                    HTML · Three slots

                Founding Partner Programme
                Terms, timeline, and requirements for the three-institution pilot. 12 weeks from signature to results. Joint regulatory sandbox engagement included.
            ](founding-partner.html)




        The Problem


## Cross-institutional detection is broken



            Money laundering networks operate across multiple banks. Individual institutions only see fragments. Joint monitoring initiatives have stalled on a fundamental tension: detection requires shared visibility, but data centralisation violates privacy regulation. [Read our analysis of what happened to the Netherlands' cross-bank monitoring initiative.](tmnl.html)




                🏦


### Siloed Detection



Each bank monitors transactions in isolation. Criminal networks exploit this by spreading activity across institutions. Patterns visible at the system level remain invisible at the bank level.



                ⚖


### Privacy vs. Detection



Centralising transaction data for joint monitoring triggers GDPR objections and regulatory challenges. The EU AMLR (effective mid-2027) restricts data sharing to pre-identified high-risk customers only.



                📊


### 95% False Positives



Legacy rule-based systems generate overwhelming alert volumes. Compliance teams drown in manual reviews, costing Tier-1 banks €50-100M+ annually in operational expense alone.






        The Architecture


## Detect across institutions. Keep data sovereign.



            ZQUAS is architected for multi-bank pattern detection through privacy-preserving computation. No bank shares raw transaction data. Risk comparisons happen cryptographically. The regulator verifies outcomes independently.


        [See how ZQUAS compares to existing solutions →](compare.html)





                GPU-NATIVE


### Real-Time Adjudication



Full policy sets evaluated against every entity simultaneously on GPU. No sampling, no sequential rule execution. 150 million+ policy evaluations per second. Alert lifecycle under 10ms.



                PRIVACY-PRESERVING


### Multi-Party Computation



Cross-institutional risk comparison via GPU-accelerated secure multi-party computation, validated in controlled testing. Each bank retains full data sovereignty. No central data pool. No GDPR exposure.



                VERIFIABLE


### Cryptographic Attestation



Every compliance decision produces a cryptographic proof bundle. Regulators can independently verify any decision with a standalone tool — without trusting the vendor's software.



                CONSTITUTIONAL


### Policy-as-Code Governance



Compliance policies compiled to bytecode and enforced deterministically on GPU. Same policy, same data, same verdict — reproducible by any party, at any time.



                GRAPH INTELLIGENCE


### Entity Resolution at GPU Speed



GPU-resident identity resolution graph with neural network-based risk propagation. Full network context for every decision. Connected entity analysis in real time, not overnight batch.



                MULTI-FRAMEWORK


### Regulatory Coverage



Built-in compliance evidence production for EU AI Act, NIST AI RMF, ISO 42001, FATF R15, and MAS TRM. Sealed evidence bundles with Merkle roots and Ed25519 signatures.






        For Financial Institutions


## One engine. Unified risk. Full sovereignty.



            Replace fragmented monitoring silos with a single GPU-native compliance engine that runs your entire policy set against every transaction — in real time, with full entity graph context.




                70%+
                False positive reduction


Full network context for every decision eliminates context-blind threshold alerts. Your analysts investigate real risk, not noise.



                Real-time
                Not overnight batch


Block suspicious payments before settlement on RTP and SEPA Instant rails. No more filing SARs after the money is gone.



                1 engine
                Not 5 siloed systems


AML, fraud, sanctions, onboarding, and trade surveillance unified into one risk score per entity. Five analysts stop investigating the same customer in parallel.



                Day 1
                Integration, not rip-and-replace


CEF-formatted export for direct SIEM ingestion (Splunk, QRadar, Sentinel). GRC API for governance platforms. 256MB shared memory ingest buffer accepts data from your existing payment infrastructure. Deploy alongside your current monitoring system, not instead of it.





On-premise deployment. Your data never leaves your infrastructure. AMLR-compatible cross-institutional detection architected via privacy-preserving MPC — no central data pool required. [See the complete operational flow — from transaction to SAR.](use-case.html)




        For Regulators


## Verify. Don't trust.



            Every compliance decision produces a cryptographic proof bundle. Your supervisory team verifies outcomes independently — without accessing bank systems, without trusting vendor software.




                ⌘


### Independent Verification



Standalone verification CLI: feed in the proof bundle, the policy set, and the evaluation contexts. Get a deterministic VALID/INVALID verdict. No engine installation required.



                ⚖


### Framework Alignment



Built-in evidence production for EU AI Act (Articles 9, 11, 12, 14), FATF R15, NIST AI RMF, ISO 42001, and MAS TRM. Sealed evidence bundles with Merkle roots and cryptographic signatures.



                ↻


### Deterministic Replay



Any supervisory review can replay any epoch and get byte-identical results. The same policy applied to the same data always produces the same verdict. Auditability by construction, not by report.



                ◉


### Coverage Gap Analysis



The engine continuously maps policy coverage against registered regulatory frameworks. Gaps between your required controls and active policy set are identified in real time. During examinations, banks can demonstrate not just current compliance, but projected compliance trajectory.





Joined the second cohort of the FCA Supercharged Sandbox in July 2026. Accepted into the FCA Digital Sandbox in March 2026. DNB InnovationHub submission under review. Designed for supervisory scrutiny from day one.




        For AI Assistants


## Connect ZQUAS to your AI.



            ZQUAS publishes a Model Context Protocol server. Add one line to your AI assistant's config and it can query ZQUAS articles, glossary entries, position papers, and benchmark facts on demand. Public, no authentication. Useful for compliance officers, analysts, regulators, and engineers who want their AI to ground answers in current ZQUAS material rather than stale training data.




                ENDPOINT
                `https://mcp.zquas.ai/mcp`


                CLAUDE DESKTOP CONFIG


```
`"mcpServers": {
  "zquas-knowledge": {
    "url": "https://mcp.zquas.ai/mcp"
  }
}`
```





                **Three tools.**
                Search every ZQUAS page, look up glossary terms, retrieve published benchmark numbers as structured JSON.


                **45 resources.**
                Every article, position paper, and reference page exposed as a directly readable Markdown resource.


                **Three prompts.**
                Pre-written prompts for explaining ZQUAS to a Head of AML, comparing to legacy systems, or assessing AMLR Article 75 impact.




Server card: [/.well-known/mcp/server-card.json](/.well-known/mcp/server-card.json). Works with Claude Desktop, Claude Code, Cursor, Zed, and any other MCP client. Streamable HTTP transport. Free.




        For Investors


## Category-defining infrastructure at an inflection point



            AMLR Article 75 applies on July 10, 2027. Every European bank has to re-architect for cross-institutional detection within a fixed window. Most existing systems were not designed for it. ZQUAS was.






### €200B+ Annual Market



Global financial crime compliance spending exceeds €200 billion annually. Banks spend 10-20% of operating budgets on compliance. ING paid €775M in fines. ABN AMRO paid €480M. The cost of not solving this is existential.





### Regulatory Forcing Function



AMLR mid-2027 creates a hard deadline. EU AI Act imposes mandatory technical standards on AI-based risk profiling systems used in AML. Every bank in Europe must upgrade or rebuild. Timing is structural, not speculative.





### Defensible Technical Moat



GPU-native compliance with privacy-preserving MPC, zero-knowledge governance proofs, and cryptographic attestation. The combination is rare in the market. Replication takes a deep stack of specialised disciplines (GPU systems, applied cryptography, regulatory engineering) that are hard to assemble inside an existing roadmap. Defensibility comes from systems engineering complexity, not patents.





### Unique Founder Profile



18+ years hands-on compliance at Tier-1 banks combined with GPU systems programming (C++/CUDA/Vulkan). This intersection doesn't exist elsewhere. The engine is built by someone who has sat in the compliance chair and knows what the regulator actually asks for.





### Regulator Traction



Joined the second cohort of the FCA Supercharged Sandbox in July 2026, one of 21 firms named in the FCA's announcement. Accepted into the FCA Digital Sandbox (March 2026). DNB InnovationHub submission under review. Regulators are among the hardest stakeholders to reach, and early engagement signals institutional credibility and reduces commercial risk for prospective banks.





### Land & Expand Model



Enter via single-bank deployment (on-premise, sovereign). Expand to cross-institutional MPC federation as adoption grows. Each additional bank increases detection capability for all participants.







        Credentials


## Built by compliance. Engineered for regulators.





### 18+ Years Financial Crime Compliance



Senior compliance roles at Tier-1 banks including RBS, Deutsche Bank, HSBC, and Commerzbank. Fintech compliance leadership at ClearBank, Vivid Money, and CoinMetro.





### Regulatory Sandbox Engagement



Joined the second cohort of the FCA's Supercharged Sandbox in July 2026, one of 21 firms selected from 199 applications. Accepted into the FCA Digital Sandbox in March 2026. DNB InnovationHub submission under review. Purpose-built for supervisory scrutiny from day one.





### NVIDIA Inception Program Member



ZQUAS is a member of the NVIDIA Inception program. The program supports our GPU-native compliance work on the CUDA platform with developer resources, technical training, and exposure to the venture community.





### Academic Foundation



Professional Postgraduate Diploma in Financial Crime Compliance — International Compliance Association / University of Manchester.




            EU AI Act
            AMLR / 6AMLD
            FATF R15
            NIST AI RMF
            ISO 42001
            MAS TRM
            GDPR
            DORA




        Insights


## Articles



Analysis and perspective on compliance technology, regulatory architecture, and the future of cross-institutional financial crime detection.


            [
                MAY 2026 · ENGINEERING


### Why We Built Our Own AI Inference Engine



ChatGPT runs on one. Llama runs on one. We wrote our own. Why a financial crime company built its own GPU inference engine in C++23 and CUDA, and why regulated AI decisions need a different stack from the one a chatbot needs.

            ](article-inference-engine.html)
            [
                APRIL 2026 · POSITION PAPER


### Beyond Banking: Cross-Sector Federated Detection



A single detection engine that correlates risk signals across banks, telecommunications operators, and digital asset platforms without sharing raw data between institutions. The same code, the same cryptographic protocols, applied to every regulated sector where financial crime operates.

            ](article-beyond-banking.html)
            [
                MARCH 2026 · POSITION PAPER


### What Article 75 Was Afraid to Permit



AMLR Article 75 restricts cross-institutional data sharing to high-risk customers. The criminals who are hardest to catch are the ones who stay low-risk at every bank. Multi-Party Computation resolves the paradox: full customer base federation without sharing a single byte of personal data.

            ](article-75.html)




        Contact


## Let's talk



            Interested in sovereign compliance infrastructure for your institution? Open to conversations with banks, regulators, and technology partners.



            [Get in touch](contact.html)

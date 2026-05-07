# Your New Compliance System Won't Work If It Can't Talk to Your Old One

> The most common reason compliance technology projects fail isn't the technology. It's integration. If the new system can't ingest from your existing payment rails and export to your existing SIEM, it's dead on arrival.

Source: https://zquas.ai/article-integration-reality.html
Site: https://zquas.ai

---
[← Articles](articles.html)
        September 2025 · Banks · 6 min read


# Your New Compliance System Won't Work If It Can't Talk to Your Old One



The most common reason compliance technology projects fail isn't the technology. It's integration. If the new system can't ingest from your existing payment rails and export to your existing SIEM, it's dead on arrival.






I've been involved in enough compliance system implementations to know how they fail. It's rarely the technology itself. The vendor's demo works. The proof of concept passes. The pilot looks good. Then you try to connect it to the bank's actual infrastructure and everything stalls.



The payment gateway uses a proprietary format. The customer data sits in three different systems that don't agree with each other. The SIEM team needs alerts in CEF format, not JSON. The case management system expects alerts via SOAP, not REST. The data warehouse runs batch exports at midnight, but the new system expects real-time feeds.



These aren't exciting problems. Nobody puts them on a pitch deck. But they're the problems that kill implementations. And compliance technology vendors consistently underestimate them because they demo against clean synthetic data, not against the tangled mess of legacy infrastructure that every real bank runs on.



## The Integration Tax



Every bank has what I call the integration tax: the cost of connecting any new system to the existing stack. For compliance technology, this tax is especially high because the monitoring system sits at the intersection of everything. It needs transaction data from payment systems. Customer data from onboarding systems. Account data from core banking. Sanctions lists from external providers. And it needs to output alerts to case management, reports to regulatory systems, and events to SIEM platforms.



A Tier-1 bank might have 15 to 20 integration points for a single monitoring system. Each one has its own format, protocol, frequency, and quirks. Some are real-time APIs. Some are batch file drops. Some are message queues. Some are database views. Getting all of them working, reliably, in production, with proper error handling and monitoring, takes months. Sometimes over a year.



This is why banks hesitate to switch compliance systems even when the new technology is clearly better. The integration tax makes switching so expensive and risky that the improvement needs to be enormous to justify it.



## The Two Failure Modes



Integration failures come in two forms.



The first is ingest failure. The new monitoring system can't reliably consume data from the bank's existing data sources. Transactions arrive late, arrive in the wrong format, arrive with missing fields, or don't arrive at all. The monitoring system generates incomplete or incorrect results. The compliance team loses confidence. The project stalls.



The second is export failure. The monitoring system generates alerts and reports, but they can't be consumed by the bank's existing downstream systems. The SIEM doesn't recognise the format. The case management system can't import the alerts. The regulatory reporting tool can't extract the data it needs. The compliance team ends up doing manual data transformation, which defeats the purpose of the new system.



Both failure modes share a root cause: the vendor designed the system for an idealised integration environment that doesn't match the bank's reality.



## Designing for the Messy Real World



The right approach to integration isn't building the perfect API and hoping the bank's infrastructure can use it. It's designing the system to handle whatever the bank's infrastructure throws at it.



On the ingest side, this means supporting multiple input modes. A shared memory ring buffer for high-throughput real-time feeds from payment systems. A standard JSON/REST API for systems that can't do shared memory. Batch file ingestion for legacy systems that only export overnight. And a raw binary mode for high-frequency environments where JSON parsing overhead is unacceptable.



The critical design choice is backpressure handling. When the ingest queue is full because the monitoring engine is processing a spike, what happens to incoming data? There are three valid answers: drop the newest arrivals (preserving order), drop the oldest (preserving recency), or block the sender (preserving completeness). The right answer depends on the data source and the bank's priority. A good ingest system lets the bank configure this per source, not one-size-fits-all.



On the export side, this means producing output in the formats that existing systems actually consume. CEF (Common Event Format) for SIEM platforms like Splunk and QRadar. Structured JSON for modern case management systems. Flat files for legacy regulatory reporting tools. And crucially, the export format should carry integrity verification. Every exported verdict should be traceable to its cryptographic proof bundle, so the downstream system can verify that the alert it received is authentic and hasn't been modified in transit.



## Deploy Alongside, Not Instead Of



The biggest mistake compliance technology vendors make is positioning their product as a replacement. "Rip out your existing monitoring system and install ours." That pitch terrifies every compliance officer, CTO, and CISO in the room.



The better approach is parallel deployment. The new system runs alongside the existing one. Both ingest the same transaction data. Both generate alerts. The compliance team compares results. Over time, as confidence in the new system grows, the old system's role diminishes.



This requires the new system to play nicely with the existing infrastructure. It can't demand exclusive access to data feeds. It can't require the bank to modify its payment systems. It can't insist on a format that nothing else in the bank produces.



Parallel deployment also provides something that rip-and-replace can't: a quantitative comparison of detection quality. When both systems run on the same data, the compliance team can measure false positive rates, detection coverage, and processing speed head-to-head. This is more convincing than any benchmark or demo because it uses the bank's own data in the bank's own environment.



## Why Integration Is a Competitive Advantage



Most compliance technology companies treat integration as a necessary evil. Something the professional services team handles after the sale. Something that adds cost and delay but doesn't generate revenue.



That's backwards. Integration capability is a competitive advantage precisely because it's the part that determines whether the product actually works in production. A monitoring engine that evaluates 500K entities in under 2 seconds is irrelevant if the bank can't get data into it or alerts out of it.



Designing integration into the architecture from the start, not as an afterthought, means the system is production-ready from day one. Shared memory ring buffers, GPU-Direct bypass, multi-format export, configurable backpressure, integrity-verified output. These aren't features. They're the infrastructure that makes the features usable.



When a CTO evaluates a new compliance system, the first question isn't "how fast is your engine?" The first question is "how does this connect to what we already have?" The vendor that answers that question convincingly wins the deal. The vendor that handwaves it with "our professional services team will handle integration" loses it.


            Danny de Gier

                Founder, ZQUAS. 18+ years in financial crime compliance at Tier-1 banks and fintechs.
                Professional Postgraduate Diploma in Financial Crime Compliance (ICA / University of Manchester).

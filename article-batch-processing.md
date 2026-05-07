# Batch Processing Is a Liability on Real-Time Payment Rails

> Your payment infrastructure settles in seconds. Your AML monitoring runs overnight. That gap is where both criminals and regulators will find you.

Source: https://zquas.ai/article-batch-processing.html
Site: https://zquas.ai

---
[← Articles](articles.html)
        January 2026 · Banks · 6 min read


# Batch Processing Is a Liability on Real-Time Payment Rails



Your payment infrastructure settles in seconds. Your AML monitoring runs overnight. That gap is where both criminals and regulators will find you.






            SEPA Instant settles in under 10 seconds. The UK's Faster Payments clears in minutes. RTP in the US is real-time. Banks have spent billions upgrading payment rails for speed, and it's working. Money moves faster than ever.




            Transaction monitoring hasn't kept up. At most banks, the AML monitoring system ingests a batch of transactions every 15 minutes, every hour, or overnight. It runs rules against that batch. It generates alerts. Analysts review them the next business day.




            Think about what that means. A fraudulent payment lands in a mule account, gets forwarded to three more accounts, converted to crypto, and exits the banking system entirely. All within an hour. The monitoring system doesn't even know the first transaction happened until the next batch cycle. By the time an analyst sees the alert, the money is in a different country.




            This isn't a theoretical risk. It's happening every day. And regulators are starting to ask pointed questions about it.




## The Regulatory Direction Is Clear



            The EU Instant Payments Regulation (2024/886) and the EBA's guidance on fraud prevention for instant payments set clear expectations: screening and risk assessment must happen before or during settlement, not after. AMLR will reinforce this direction when it takes effect in 2027.




            The logic is straightforward. If you offer instant payments, you need instant monitoring. Offering a payment product that settles in seconds while monitoring for fraud and money laundering on a next-day basis is a control gap. Regulators will treat it as one.




            Some banks have tried to address this by adding a pre-screening step before instant payments clear. Run the payment through a quick sanctions check and a basic fraud score, and if it passes, let it go. But this is a thin layer. It catches sanctioned names and obvious velocity anomalies. It doesn't catch the coordinated cross-account patterns that characterise professional money laundering.




## Why Legacy Systems Can't Do Real-Time



            The architecture of most transaction monitoring systems was designed for a batch world. The system pulls a set of transactions from a data warehouse, loads them into memory, runs them through a rule engine sequentially, writes the results to a database, and generates alerts for the case management queue.




            This works fine when you're processing yesterday's transactions today. It doesn't work when you need a decision in milliseconds.




            Making a batch system "real-time" isn't a configuration change. The data pipeline, the rule execution engine, the memory model, and the output handling all need to change. Most vendors have added a real-time API layer on top of their batch engine, which gives you real-time latency for simple checks but not the ability to evaluate complex multi-factor rules with full customer context at payment speed.




            True real-time monitoring means every transaction is evaluated against the full policy set, with access to the customer's complete transaction history and entity relationships, before the payment settles. That's a different class of computational problem. It requires an architecture designed for parallelism from the ground up.




## What GPU-Native Processing Changes



            GPU hardware was designed for exactly this kind of problem: evaluating many conditions against many data points simultaneously. A modern GPU has thousands of cores that can execute in parallel, compared to the tens of cores in a CPU.




            When you run compliance evaluation on GPU, you're not processing transactions one at a time through a rule engine. You're evaluating every policy against every transaction simultaneously. The entire policy set, not a subset, not a simplified version, applied to every event in parallel.




            The practical result is that monitoring keeps pace with payment speed without sacrificing detection depth. You don't have to choose between "fast but shallow" and "deep but slow." The hardware makes both possible at the same time.




            This is what 150 million+ compliance policy evaluations per second looks like in practice. 500,000 entities evaluated against 100 AML policies in under 2 seconds on NVIDIA RTX 5090. Not a burst benchmark. A production-scale workload.




## The Audit Implication



            There's a second problem with batch processing that's less obvious but equally important. When you process in batches, the monitoring system's state at any given moment is ambiguous. Which transactions have been evaluated? Which rules were in effect? If you changed a rule at 2pm and the batch ran at midnight, which version of the rule applied to the 3pm transactions?




            These questions come up in every regulatory examination. Banks spend significant effort reconstructing timelines and proving that the right rules were applied at the right time. Often, they can't prove it definitively because the batch architecture doesn't preserve that granularity.




            Real-time evaluation with cryptographic attestation eliminates this problem. Each batch of evaluations produces a sealed record: these policies, this data, this verdict, this timestamp, cryptographically signed. The question "what rules were in effect at 3pm on March 14th?" has a provable answer, not a reconstructed one.




## What This Means Practically



            Banks rolling out instant payment capabilities need to ask their monitoring vendors a direct question: can your system evaluate our full policy set against every transaction before settlement completes?




            If the answer is "we can do a pre-screening check" or "we process in near-real-time batches," that's not sufficient. It creates a control gap between payment speed and monitoring speed. Regulators will find that gap. If they don't find it during an examination, they'll find it after an incident.




            The technology to close this gap exists now. GPU-native compliance engines can process at payment speed with full detection depth. The question isn't whether real-time monitoring is possible. It's whether your current architecture can deliver it, or whether you need a different one.



            Danny de Gier

                Founder, ZQUAS. 18+ years in financial crime compliance at Tier-1 banks and fintechs.
                Professional Postgraduate Diploma in Financial Crime Compliance (ICA / University of Manchester).

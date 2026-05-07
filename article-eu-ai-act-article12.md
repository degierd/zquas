# Supervising AI in AML: What Article 12 Actually Requires

> The EU AI Act may classify AI-based AML risk profiling as high-risk. Article 12 demands record-keeping. But what does technically adequate record-keeping look like when a system makes millions of decisions per day?

Source: https://zquas.ai/article-eu-ai-act-article12.html
Site: https://zquas.ai

---
[← Articles](articles.html)
        December 2025 · Regulators · 8 min read


# Supervising AI in AML: What Article 12 Actually Requires



The EU AI Act may classify AI-based AML risk profiling as high-risk under Annex III. Article 12 demands record-keeping. But what does technically adequate record-keeping look like when a system makes millions of decisions per day?






            The EU AI Act entered into force in 2024 with a phased implementation schedule. For high-risk AI systems, the core obligations apply from August 2026. Recital 58 excludes standard fraud and AML detection from high-risk classification, but AI-based customer risk profiling may qualify under Annex III point 5(b). Banks using AI to generate individual risk scores should assess their classification now. Among the high-risk obligations, Article 12 on record-keeping is the one most likely to create operational headaches.




            Article 12 requires that high-risk AI systems have logging capabilities that ensure a level of traceability of the system's functioning appropriate to its intended purpose. The system must keep records sufficient to facilitate monitoring of the high-risk AI system's operation and enable post-market monitoring.




            The language sounds reasonable. The challenge is in the implementation.




## The Scale Problem



            A Tier-1 bank's AML monitoring system evaluates millions of transactions daily. Some large banks process tens of millions. Each transaction is evaluated against multiple rules, scenarios, and models. The system produces a risk score, a decision (alert or no alert), and supporting metadata.




            Article 12 requires that this entire chain be logged in a way that allows operations to be traced back. For a batch system running overnight, this is already difficult. The logs are massive, the relationships between inputs and outputs are complex, and the storage costs are significant.




            For a real-time system processing transactions at payment speed, the logging challenge is even greater. You need to capture the input, the model state, the decision logic, and the output for every transaction, in real time, without degrading system performance. And you need to retain these records for the duration required by the regulation.




            Most existing monitoring systems weren't designed with this level of logging granularity. They log alerts (the outputs) and sometimes log the rules that triggered. But they don't systematically log the complete decision chain: which version of the model was running, what features were calculated, what thresholds were applied, what the intermediate scores were, and why the final decision was made.




## What "Tracing Back" Means in Practice



            The requirement for traceability of the system's functioning implies a specific capability: given an output, you should be able to reconstruct exactly how the system arrived at it.




            For a rules-based system, this is conceptually simple. The rule says "if amount > €10,000 and jurisdiction = high-risk, generate alert." You can trace back by showing the transaction amount and the jurisdiction. But real monitoring systems have hundreds of rules interacting with each other, with priority ordering, exception handling, and cascading logic. Tracing back through that web is not trivial.




            For machine learning systems, tracing back is much harder. An ML model produces a risk score based on hundreds of features, weighted by parameters learned during training. Explaining why a specific transaction received a score of 0.73 instead of 0.71 requires either model-specific interpretability tools (SHAP values, attention weights) or a complete record of the model's state at the time of evaluation.




            Most banks use a combination of rules and ML models. The interaction between the two adds another layer of complexity. A transaction might pass the rules-based screening but get flagged by the ML model, or vice versa. Tracing back requires understanding both systems and their interaction.




## The Regulatory Expectation Gap



            The technical standards for Article 12 are still being drafted by CEN/CENELEC working groups. Until they're finalised, banks and vendors are working with the regulation's high-level language and their best interpretation of what regulators will expect.




            Based on the regulation's text and the direction of regulatory thinking, there are a few things that are fairly clear.




            Record retention periods will need to cover the full lifecycle of the AI system, not just the output retention period required by AML regulations. This means keeping records of model versions, training data characteristics, validation results, and deployment decisions alongside the operational logs.




            Records need to be tamper-evident. Article 12 doesn't use the word "tamper-evident" explicitly, but the requirement for records that enable reliable post-market monitoring implies it. If someone can modify the logs after the fact, the monitoring capability is undermined. Banks will need to demonstrate that their logging infrastructure has integrity protections.




            The records need to be structured enough for automated analysis. Regulators won't manually review millions of log entries. They need the records in a format that supports systematic querying, statistical analysis, and anomaly detection. Unstructured log files won't meet this standard.




## How Cryptographic Attestation Satisfies Article 12



            There's a natural alignment between cryptographic attestation and Article 12's requirements.




            When every batch of compliance decisions produces a cryptographic proof bundle that includes: the policy set hash, the input data hash, the individual verdicts, a Merkle root over all verdicts, and an Ed25519 signature binding everything together, you have a complete, tamper-evident, structured record of every decision the system made.




            Tracing back is straightforward. Given any individual verdict, you can verify it against the Merkle root, confirm the policy set that was in effect, and reproduce the decision by replaying the same policy against the same input. If the system is deterministic (same input plus same policy always equals same output), the replay will produce an identical result, confirming the original record.




            The records are tamper-evident by construction. Any modification to a verdict, a policy hash, or a timestamp would invalidate the cryptographic signature. You don't need to trust the logging infrastructure. The mathematics guarantee integrity.




            And the records are structured by design. Proof bundles have a defined schema. They can be queried, aggregated, and analysed automatically. A supervisory tool can process thousands of proof bundles and identify anomalies (unexpected policy changes, verdict distribution shifts, missing epochs) without manual review.




## The Competitive Advantage for Early Movers



            Banks that implement Article 12-compliant logging early will have an advantage during examinations. When the regulator asks "show me how your system complies with Article 12," the bank that hands over a set of cryptographic proof bundles with a verification tool is in a fundamentally different position than the bank that hands over a pile of log files and a PowerPoint explaining how to read them.




            The first conversation takes minutes. The second takes weeks.




            For regulators evaluating new approaches, the practical question is: what should Article 12-compliant record-keeping look like for AI-based AML systems? The answer matters because it will shape the technical standards being drafted now. Cryptographic attestation offers a concrete, implementable answer that satisfies the regulation's requirements while also solving problems (temporal accuracy, completeness verification, tamper evidence) that conventional logging doesn't address.




            The standard-setting process is underway. The decisions made now will define what "adequate record-keeping" means for AI in financial crime for the next decade.



            Danny de Gier

                Founder, ZQUAS. 18+ years in financial crime compliance at Tier-1 banks and fintechs.
                Professional Postgraduate Diploma in Financial Crime Compliance (ICA / University of Manchester).

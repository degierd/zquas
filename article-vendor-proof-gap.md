# What Your AML Vendor Can't Prove

> Your monitoring system generates alerts, case files, and reports. But can it cryptographically prove that a specific policy was applied to specific data at a specific time? That question is coming.

Source: https://zquas.ai/article-vendor-proof-gap.html
Site: https://zquas.ai

---
[← Articles](articles.html)
        December 2025 · Banks · 7 min read


# What Your AML Vendor Can't Prove



Your monitoring system generates alerts, case files, and reports. But can it cryptographically prove that a specific policy was applied to specific data at a specific time? That question is coming.






            Every AML monitoring vendor will tell you their system is auditable. They'll show you dashboards, alert logs, case management workflows, and regulatory reports. They'll walk you through how an analyst can trace an alert back to the rule that triggered it.




            All of that is useful. None of it is proof.




            There's a difference between "we can show you what happened" and "we can mathematically prove what happened." That difference doesn't matter much during routine operations. It matters enormously during a regulatory examination, a legal dispute, or an incident investigation.




## What Vendors Can Show You



            A typical AML monitoring system provides several layers of audit capability.




            Alert logs show which transactions triggered which rules, with timestamps and rule parameters. Case management systems track what the analyst did with the alert, including disposition notes, escalation decisions, and SAR filing records. System configuration records document which rules are active, what thresholds are set, and when changes were made. And some systems provide model monitoring dashboards that track ML model performance over time.




            This is genuinely useful for day-to-day operations. Analysts need to trace alerts. Compliance managers need to review case quality. And internal audit needs to verify that the system is configured correctly.




            The problem is that all of this information comes from the same system. The monitoring platform generates the alerts, records the audit trail, and reports on its own performance. It's self-referential. If there's a bug in the system that causes it to skip certain transactions, the audit trail won't show those transactions because the system didn't process them. If a configuration change wasn't logged properly, the configuration history is incomplete. If the system's clock drifted, the timestamps are wrong.




            You're trusting the system to accurately report on its own behavior. That works until it doesn't.




## What Vendors Can't Prove



            There are four things that no conventional AML monitoring vendor can prove with mathematical certainty.




            Completeness. The system can show you the transactions it processed. It can't prove it processed all transactions. If a batch job failed silently, if a data pipeline dropped records, or if a filter excluded transactions that should have been evaluated, the system's own logs won't show the gap. You'd need an independent reconciliation against the source system to detect missing records, and most banks don't do this systematically.




            Policy integrity. The system can show you its current configuration. It can't prove that the configuration at 3pm on March 14th was what the compliance manual says it should have been. Configuration history depends on change logs, which depend on the logging infrastructure working correctly. There's no cryptographic binding between the documented policy and the running code.




            Temporal accuracy. The system can show you timestamps on alerts and evaluations. It can't prove those timestamps are accurate. If the system processed a batch at midnight but the transactions occurred at 2pm, the "evaluation time" in the log is midnight, not 2pm. The question "was this transaction monitored before or after settlement?" often doesn't have a provable answer.




            Decision determinism. The system can show you the verdict for a specific transaction. It can't prove that reprocessing the same transaction with the same rules would produce the same result. Many monitoring systems have non-deterministic elements: ML models that update continuously, rules that reference external data sources that change, or evaluation order dependencies that produce different results depending on system load.




## Why This Matters Now



            For years, these limitations were accepted as inherent. Monitoring systems are complex. Perfect auditability is impractical. Regulators understood this and worked with what was available.




            Two developments are changing that calculus.




            The EU AI Act, effective for high-risk systems from August 2026, requires record-keeping capabilities that ensure traceability of the system's functioning. This is a higher standard than what most monitoring systems currently meet. Banks will need to demonstrate that their AI-based monitoring systems can reconstruct exactly how any given decision was made. Self-referential logs from the vendor's own system may not satisfy this requirement.




            Separately, regulatory expectations around monitoring effectiveness are increasing. After the ING and ABN AMRO enforcement actions, Dutch regulators specifically examined whether banks could demonstrate that their monitoring systems were operating as intended. The question wasn't "do you have a monitoring system?" It was "can you prove your monitoring system was working correctly?" The shift from "do you have it" to "can you prove it works" represents a fundamental change in supervisory expectations.




## What Cryptographic Proof Looks Like



            A compliance engine with cryptographic attestation works differently. Instead of logging what happened, it proves what happened.




            Each batch of evaluations produces a sealed proof bundle. The bundle contains a hash of the exact policy set that was running, a hash of the input data that was evaluated, each individual verdict, a Merkle root binding all verdicts together, and an Ed25519 signature over the entire bundle.




            This proof has specific properties that conventional audit trails lack.




            It proves completeness for the evaluated batch. The Merkle root covers every verdict in the batch. If a verdict is missing, the root doesn't verify.




            It proves policy integrity. The policy hash is bound into the signed proof. If the policy was different from what's documented, the hash won't match.




            It proves temporal accuracy. The signed timestamp is part of the proof. Modifying the timestamp invalidates the signature.




            And if the underlying engine is deterministic, it proves decision reproducibility. Anyone with the same policy set and the same input data can replay the evaluation and verify that the same verdicts result.




## The Question Your Regulator Will Ask



            During your next examination, consider what happens when the regulator asks: "Can you prove that your monitoring system evaluated every transaction against your stated policies on this date?"




            With a conventional system, you'll spend weeks pulling logs, reconciling records, and building a narrative that you hope the examiner finds convincing.




            With cryptographic attestation, you hand them a proof bundle and a verification tool. The answer takes minutes.




            The technology exists now. The regulatory expectation is heading in this direction. The banks that adopt verifiable compliance first will have a materially easier time during examinations. The ones that wait will be explaining their log files while their peers hand over proofs.



            Danny de Gier

                Founder, ZQUAS. 18+ years in financial crime compliance at Tier-1 banks and fintechs.
                Professional Postgraduate Diploma in Financial Crime Compliance (ICA / University of Manchester).

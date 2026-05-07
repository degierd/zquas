# Same Data, Same Rules, Different Verdict: The Determinism Problem in AML

> Run the same transaction through the same monitoring system tomorrow and you might get a different result. That's not a bug. It's an architecture problem. And regulators are starting to notice.

Source: https://zquas.ai/article-determinism-problem.html
Site: https://zquas.ai

---
[← Articles](articles.html)
        December 2025 · Banks · 6 min read


# Same Data, Same Rules, Different Verdict: The Determinism Problem in AML



Run the same transaction through the same monitoring system tomorrow and you might get a different result. That's not a bug. It's an architecture problem. And regulators are starting to notice.






            A few years ago I was involved in a model validation exercise at a Tier-1 bank. The validation team took a set of historical transactions that had been flagged as alerts, fed them back through the monitoring system, and compared the results. About 12% of the transactions that originally triggered alerts did not trigger alerts on the second run.




            Same data. Same rules. Different results.




            The compliance team was understandably alarmed. If the system produces different results on the same input, what does that say about the reliability of every alert it has ever generated? And what does it say about every transaction it didn't alert on?




            It turned out there were explanations. The ML model had been retrained between the two runs. Some reference data tables had been updated. The evaluation order of certain rules had shifted due to a system upgrade. Each individual cause was understandable. But the aggregate effect was that the system was non-deterministic, and nobody had fully appreciated what that meant until the validation exercise made it visible.




## Why Monitoring Systems Are Non-Deterministic



            Most AML monitoring systems have multiple sources of non-determinism, and most compliance teams aren't aware of all of them.




            ML model updates are the most obvious source. Models are retrained periodically on new data. Each retraining produces slightly different parameters. A transaction that scored 0.68 under last month's model might score 0.72 under this month's model. If the alert threshold is 0.70, the verdict flips. This is by design. The model is learning. But it means that historical verdicts can't be reproduced exactly.




            Reference data dependencies are another source. Many rules check transaction data against external reference lists: country risk ratings, sanctions lists, PEP databases, customer risk scores. These lists change constantly. A transaction to a country that was rated medium-risk last Tuesday might now be rated high-risk. If the system evaluates the transaction against today's reference data instead of the reference data that was in effect when the transaction occurred, the result changes.




            Evaluation order matters in systems with cascading rules. If Rule A excludes a transaction from further evaluation, and Rule B would have flagged it, the result depends on which rule runs first. In some systems, the evaluation order is configuration-dependent or even load-dependent. A system under heavy load might execute rules in a different sequence than the same system under light load.




            Floating point arithmetic introduces subtle non-determinism in ML-based systems. The order in which floating point operations are executed can affect the result due to rounding. GPU-accelerated ML inference can produce different results depending on the specific GPU hardware and driver version. These differences are typically tiny, but when scores are close to alert thresholds, tiny differences change verdicts.




            Race conditions in parallel processing can cause non-determinism in systems that evaluate multiple rules concurrently. If two rules read from the same customer profile and one updates it during evaluation, the result depends on timing.




## Why Determinism Matters for Compliance



            Non-determinism creates three specific problems for compliance operations.




            The first is defensibility. When a regulator asks why a transaction wasn't flagged, the bank needs to explain what the system did and why. If the answer is "the system might have produced a different result if it had run at a different time or in a different order," that's not a strong defence. Regulators expect monitoring systems to be reliable and consistent. Non-deterministic results undermine confidence in the system's overall effectiveness.




            The second is model validation. Validation exercises require reproducing the system's behavior on known data. If the system is non-deterministic, the validation results don't tell you much about the production system's actual behavior. You're validating a different instance of the system, not the one that processed the real transactions.




            The third is legal liability. In enforcement actions, banks need to demonstrate that their monitoring was adequate. If opposing counsel can show that the same system produces different results on the same data, the bank's position weakens significantly. The argument that "our system works" becomes difficult to sustain when the system's output depends on when you ask.




## How Deterministic Evaluation Works



            A deterministic compliance engine eliminates these problems by design.




            The policy set is compiled to bytecode. The bytecode is immutable once deployed. There are no model retraining cycles that change evaluation behavior mid-deployment. When the policy set changes, a new version is compiled, and the transition is recorded with cryptographic hashes of both the old and new versions.




            Reference data is versioned and snapshotted. When a batch of transactions is evaluated, the system records which version of each reference dataset was used. Replaying the evaluation with the same reference data version produces identical results.




            The evaluation is fully parallel but order-independent. Each transaction is evaluated against the full policy set independently. There are no cascading rules that depend on evaluation order. No race conditions. No load-dependent sequencing.




            The arithmetic is deterministic. The policy bytecode executes on GPU with fixed-point or controlled floating-point operations that produce identical results regardless of hardware specifics.




            The practical result: given the same policy version, the same input data, and the same reference data version, the system always produces exactly the same verdict. Not "almost the same." Exactly the same. Byte-identical.




## What This Means for Your Next Examination



            When your regulator asks "how do you know your system is producing consistent results?", the answer matters.




            With a conventional system, you can point to periodic validation exercises and model governance documentation. But you can't guarantee that the production system's behavior matches the validation results, because the system is non-deterministic.




            With a deterministic engine, you can make a stronger claim. The system is mathematically incapable of producing different results on the same input with the same policies. You can demonstrate this by replaying any historical evaluation and showing byte-identical results. And the cryptographic proof bundles provide evidence that the same policy set was in effect throughout the evaluation period.




            This isn't just a theoretical improvement. It changes the nature of the conversation with your regulator. Instead of explaining why your system might sometimes produce inconsistent results and arguing that the inconsistency is acceptable, you can demonstrate that inconsistency is architecturally impossible.




            That's a conversation most compliance officers would prefer to be having.



            Danny de Gier

                Founder, ZQUAS. 18+ years in financial crime compliance at Tier-1 banks and fintechs.
                Professional Postgraduate Diploma in Financial Crime Compliance (ICA / University of Manchester).

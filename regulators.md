# For Regulators

> ZQUAS produces cryptographic proof of every compliance decision. Supervisory teams verify outcomes independently, without accessing bank systems or installing vendor software.

Source: https://zquas.ai/regulators.html
Site: https://zquas.ai

---
For Supervisory Authorities


# Verify compliance decisions. Don't trust vendor reports.



            ZQUAS produces cryptographic proof of every compliance decision. Your supervisory team verifies outcomes independently, without accessing bank systems, without installing vendor software, and without seeing underlying transaction data.




            Accepted into the FCA Digital Sandbox · DNB InnovationHub under review




        Current Limitations


## Trust-based supervision has structural gaps





### System Behavior Is Unverifiable



When a bank describes how its monitoring system works, there is no way to independently confirm that the production system matches the description. Configuration drift, undocumented rule changes, and silent processing failures are invisible to examiners relying on the bank's own reporting.





### Temporal Reconstruction Is Imprecise



The question "what rules were in effect on this date?" requires reconstructing from change logs and deployment records. In batch processing systems, the relationship between rule changes, batch execution times, and which transactions were evaluated under which rule version is often genuinely ambiguous.





### AI Oversight Is Approaching Without Tools



The EU AI Act may classify AI-based AML risk profiling as high-risk under Annex III. Article 12 requires record-keeping that ensures traceability of the system's functioning. Article 14 requires human oversight. Most monitoring systems weren't designed with this level of logging granularity. The technical standards are being drafted now.






        Cryptographic Verification


## Mathematical proof replaces institutional trust



            Every batch of compliance decisions produces a sealed proof bundle. The bundle is self-contained, tamper-evident, and independently verifiable.




                1
                Policy Set
                hashed and signed

            →

                2
                Transaction Data
                evaluated on GPU against full policy set

            →

                3
                Verdicts
                bound together via Merkle root

            →

                4
                Proof Bundle
                Ed25519 signed, timestamped

            →

                5
                Verification
                standalone CLI confirms validity





                COMPLETENESS


### Every verdict is accounted for



The Merkle root covers every verdict in the batch. A missing verdict invalidates the root. Unlike log-based audit trails, gaps are mathematically detectable.



                POLICY INTEGRITY


### The running code matches the documented policy



The proof bundle includes a cryptographic hash of the exact policy set that was executed. If the production configuration differs from the documented policy, the hashes won't match.



                TEMPORAL PRECISION


### Timestamps are part of the signed proof



The evaluation timestamp is bound into the cryptographic signature. Modifying the timestamp invalidates the proof. The question "when was this transaction evaluated?" has a provable answer.






        Verification Tool


## No vendor software required



            The verification tool is independent of the ZQUAS engine. It takes a proof bundle as input, applies standard cryptographic operations, and outputs VALID or INVALID. The tool is auditable, inspectable, and runs without any vendor infrastructure.




```
$ themis-verify --epoch epoch_2026-03-08.bundle --policies /registered/policy-set-v4.2/

Verifying epoch 2026-03-08_14:32:00Z...
Policy hash:     OK (matches registered set v4.2)
Merkle root:     OK (1,247 verdicts verified)
Ed25519 sig:     OK (key: DNB-registered-pub-2026)
Temporal range:  14:30:00Z - 14:35:00Z

Result: VALID
```



            The regulator registers the bank's public key and policy set hashes. Verification confirms that the registered policies produced the claimed verdicts on the claimed data at the claimed time. No access to the bank's systems or the underlying transaction data is needed.





        Regulatory Framework Alignment


## Built-in compliance evidence production



            The engine produces sealed Control Evaluation Records aligned to multiple regulatory frameworks. Evidence bundles include Merkle roots and Ed25519 signatures.






### EU AI Act



Articles 9, 11, 12, 14. Risk management supported by built-in adversarial testing framework that continuously evaluates system robustness (Article 9). Technical documentation via sealed evidence bundles (Article 11). Record-keeping through cryptographic proof bundles with full decision chain traceability (Article 12). Human oversight enforced by constitutional warrant model where no automated action executes without authorization (Article 14).





### AMLR / 6AMLD



Real-time monitoring capability, privacy-preserving cross-institutional detection (architecture validated in controlled testing), and explainable automated decision-making.





### FATF Recommendation 15



New technologies and virtual assets. Risk-based approach to innovation in AML/CFT systems.





### NIST AI RMF



AI risk management framework alignment. Map, measure, manage, and govern AI risks.





### ISO 42001



AI management system standard. Organizational governance requirements for AI systems.





### MAS TRM



Technology Risk Management guidelines. Applicable to financial institutions under Monetary Authority of Singapore supervision.





### GDPR



Data protection by design. Privacy-preserving MPC architecture eliminates cross-institutional data exposure.





### DORA



Digital operational resilience. ICT risk management, incident reporting, and third-party oversight. 12,342 automated tests across the codebase, with 7,218 core engine tests across 12 audited subsystems. Ed25519-signed audit trail for every compliance decision. Binary self-verification and build attestation with embedded cryptographic hashes for runtime integrity verification.






        SupTech Implications


## What this enables for supervisory strategy





### Continuous Supervision



Instead of periodic examinations with sampled reviews, regulators could receive proof bundles on an ongoing basis and verify them automatically. Anomalies like missing epochs, unexpected policy changes, or verdict distribution shifts trigger alerts for human review. Supervision shifts from periodic sampling to continuous monitoring.





### Cross-Jurisdictional Verification



A proof bundle from one jurisdiction can be verified by another jurisdiction's examiner without data sharing or system access. The proof is self-contained. This simplifies supervisory cooperation under frameworks like the ECB's Single Supervisory Mechanism and emerging AMLA coordination requirements.






        Examination Readiness


## Real-time regulatory coverage analysis





### Gap Detection



The engine continuously analyses policy coverage against registered regulatory frameworks. If your active policy set covers 47 out of 50 required controls under a specific framework, the system identifies the three gaps and their regulatory references. Coverage gaps are surfaced in real time, not discovered during an examination. This gives compliance teams a continuous view of their regulatory posture across all covered frameworks.





### Predictive Compliance



The predictive compliance engine simulates governance state forward in time. It predicts when warrants will expire, when agent gas budgets will deplete, and when policy changes will create coverage gaps. Compliance issues are flagged before they materialise. For supervisory planning, this means banks using this system can demonstrate not just current compliance, but projected compliance trajectory.






        Engagement


## Designed for regulatory scrutiny



            ZQUAS is purpose-built for supervisory evaluation. Accepted into the FCA Digital Sandbox in March 2026. DNB InnovationHub submission under review.






### Sandbox Evaluation



We welcome structured evaluation through regulatory sandbox programmes. The architecture is designed to be tested, challenged, and validated under supervisory conditions.





### Standards Contribution



As CEN/CENELEC drafts technical standards for the EU AI Act's high-risk AI requirements, we're available to contribute technical expertise on cryptographic attestation and deterministic compliance evaluation.




            [danny@zquas.ai](mailto:danny@zquas.ai?subject=ZQUAS%20Regulatory%20Inquiry)
            [LinkedIn](https://www.linkedin.com/in/danny-de-gier-prof-pgdip-fcc/)





            **Three Founding Partner slots available**


12 weeks from signature to results. Joint regulatory sandbox engagement included. No customer data leaves your infrastructure.



            [View Programme](founding-partner.html)
            [Position Paper](article-75.html)

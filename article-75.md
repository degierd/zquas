# What Article 75 Was Afraid to Permit

> How Multi-Party Computation enables full customer base federation for AML detection without sharing personal data. ZQUAS position paper on AMLR Article 75 and GDPR.

Source: https://zquas.ai/article-75.html
Site: https://zquas.ai

---
[← Articles](articles.html)
        Position Paper


# What Article 75 Was Afraid to Permit



How Multi-Party Computation Makes Full Customer Base Federation Legal Under GDPR


            DateMarch 2026
            AudienceRegulators, MLROs, Compliance Leaders, Privacy Officers
            Reading time12 min








## The Twenty-Year Deadlock



            For two decades, the fight against money laundering has been trapped in a paradox. Criminals exploit the gaps between institutions: structuring funds across banks, layering transactions through correspondent networks, building shell company webs that span multiple banking relationships. No single bank sees the complete picture. The pattern is only visible when information from multiple institutions is combined.




            Everyone knows this. The Financial Action Task Force has said it. The European Commission has said it. Every MLRO at every bank in Europe knows that their institution's transaction monitoring system is blind to the majority of laundering activity that occurs across institutional boundaries.




            For twenty years, every attempt to solve this problem has failed. The detection works. The data sharing violates privacy law.




## TMNL: The Proof That Detection Works



            The Netherlands came closest. Transaction Monitoring Netherlands (TMNL), a joint initiative of the five largest Dutch banks, demonstrated that cross-institutional transaction analysis could identify laundering patterns invisible to individual institutions. The detection worked.




            Then the Dutch Data Protection Authority intervened. TMNL required centralising pseudonymised transaction data from all participating banks. The DPA ruled that pseudonymised data is still personal data under GDPR. A correct legal interpretation. The processing lacked an adequate legal basis. TMNL was effectively suspended.




            The lesson was clear: centralising data, even pseudonymised data, is not a viable path to cross-institutional AML detection in Europe.




## Article 75: A Door Half-Opened



            The EU Anti-Money Laundering Regulation (AMLR), adopted in May 2024 and applicable from 10 July 2027, attempts to break this deadlock. Article 75 creates, for the first time, a formal legal framework for "partnerships for information sharing" between obliged entities.




            This is genuine progress. Article 75 establishes supervisory oversight, requires Data Protection Impact Assessments, provides a civil liability safe harbour for good-faith sharing, and permits the exchange of customer identification data, transaction information, risk factors, and suspicion reports, with FIU consent.




            But Article 75 has a constraint that significantly limits its effectiveness:





> "Article 75 doesn't appear to go as far as many financial crime fighters would have hoped, and focuses essentially on higher risk customers and/or post-suspicion sharing and is less permissive on sharing information on lower risk customers."

            Financial Crime News, June 2024




            This constraint is not arbitrary. It exists because sharing customer data, even within a supervised partnership, is a GDPR processing operation. Under Article 5(1)(c) of the GDPR (data minimisation) and Article 5(1)(b) (purpose limitation), personal data processing must be proportionate. Blanket sharing of all customers' data across multiple institutions, including the vast majority who present no AML risk, would be disproportionate.




            The result: Article 75 permits sharing on higher-risk customers and post-suspicion cases. The criminals who are most dangerous are the ones who deliberately maintain a low-risk profile at each individual institution. They are precisely the ones excluded from cross-institutional scrutiny.




            The paradox remains: the customers you most need to see across banks are the ones you are least permitted to share data about.




---




## The Resolution: Compute Without Sharing



            There is a class of technologies that resolves this paradox. It does not argue for broader data sharing permissions. It eliminates the need for data sharing entirely.




            Multi-Party Computation (MPC) is a cryptographic technique that allows two or more parties to jointly compute a function over their combined data without any party revealing its individual inputs to any other party. The output of the computation is shared. The inputs are not.




            In the context of cross-institutional AML detection, the operation works as follows. Bank A and Bank B each hold risk scores for their customers. They wish to determine whether any customer's combined cross-bank risk exceeds a defined threshold. Using MPC, they compute this comparison without Bank A learning Bank B's risk score, without Bank B learning Bank A's risk score, and without either bank learning anything about the other's non-shared customers. The output is a binary signal: this entity's combined risk exceeds the threshold, or it does not. Nothing else is revealed.




## Why This Changes the Article 75 Equation



            The Article 75 restriction on low-risk customer sharing exists because sharing means exposing personal data. MPC does not share data. The question is whether MPC computation falls within the scope of "information sharing" as Article 75 defines it, or whether it constitutes a fundamentally different operation. We argue it is fundamentally different, for three reasons.


        Argument 1


What crosses between institutions is not personal data.



            During an MPC federation round, the data transmitted between institutions consists of elliptic curve points (blinded cryptographic values), garbled circuit ciphertexts (encrypted gate evaluations), and oblivious transfer labels (randomly masked keys). None of these values can be attributed to an identified or identifiable natural person. They are computationally indistinguishable from random byte sequences.




            GDPR Article 4(1) defines personal data as "any information relating to an identified or identifiable natural person." GDPR Recital 26 clarifies that the principles of data protection should not apply to anonymous information: information which does not relate to an identified or identifiable natural person, or personal data rendered anonymous in such a manner that the data subject is not or no longer identifiable.




            MPC protocol messages are not pseudonymised data, which remains personal data under GDPR. They are cryptographic material that cannot, even in principle, be de-anonymised by the receiving party without the cooperation of the sending party. The protocol is specifically designed to prevent that cooperation.


        Argument 2


No institution gains access to any other institution's customer data.



            After a complete MPC federation round, each bank learns exactly one thing about each shared customer: whether the combined cross-institutional risk exceeds the threshold. This is a binary signal derived from a computation, not a data transfer. The bank does not learn the other institution's risk score, transaction history, or even which other institution holds the customer.




            This is materially different from the "exchange of information" that Article 75 regulates. Article 75 governs the sharing of customer identification and beneficial ownership information, details of the purpose and nature of business relationships and transactions, customer transactions information, and risk factors associated with customers. In an MPC federation, none of this information is shared.


        Argument 3


The privacy guarantee is mathematical, not administrative.



            Traditional data sharing partnerships rely on contractual obligations, access controls, and supervisory oversight to prevent misuse of shared data. These are administrative safeguards. They work when everyone complies and fail when someone does not.




            MPC privacy is a property of the mathematics. A party cannot extract the other party's input from the protocol messages even if it deviates from the protocol, colludes with external parties, or has unlimited computational resources, in the information-theoretic security model. It is a theorem, not a policy promise.




---




## The Implication: Full Customer Base Federation



            If MPC federation does not constitute personal data sharing under GDPR, then the Article 75 restriction to higher-risk customers has no basis to apply. The restriction exists to limit disproportionate personal data processing. Where no personal data processing occurs, the proportionality analysis is moot.




            MPC-based cross-institutional AML detection can, in principle, cover the entire customer base. Not just the customers already identified as higher risk. Article 75 was afraid to permit this. Effective AML detection requires it.




            The practical difference between the two approaches:








                        Article 75 Sharing | 
                        MPC Federation 
| 
                        Scope | 
                        Higher-risk customers and post-suspicion only | 
                        Entire customer base 
| 
                        Data exposed | 
                        Customer IDs, transactions, risk factors, beneficial ownership | 
                        Nothing. Cryptographic material only. 
| 
                        Privacy model | 
                        Administrative: contracts, access controls, supervision | 
                        Mathematical: cryptographic guarantee 
| 
                        GDPR basis required | 
                        Yes: proportionality analysis, DPIA, supervisory approval | 
                        Arguable that GDPR does not apply to non-personal data 
| 
                        Detects low-risk profile criminals | 
                        No. Excluded from sharing scope. | 
                        Yes. All customers are federated. 
| 
                        DPA risk | 
                        Moderate. TMNL precedent shows DPA will scrutinise. | 
                        Low. No personal data leaves the institution. 
            The criminals Article 75 cannot reach are those who deliberately maintain low-risk profiles at each institution and distribute their laundering across the banking system. MPC federation is designed to detect them. Their combined risk is computed without any institution revealing its individual assessment.




---




## The Evidence: Measured, Not Theoretical



            The ZQUAS platform has been built, tested, and stress-tested. The following results are from actual execution on production hardware (NVIDIA RTX 5090, 32 GB VRAM), not projections or simulations.







| 
                        Capability | 
                        Measured result 
| 
                        Single node: 500,000 entities, 100 AML policies | 
                        under 2 seconds (measured: 1,204ms) 
| 
                        Alert lifecycle: ingestion to agent triage | 
                        under 10ms (full lifecycle breakdown on benchmark page) 
| 
                        Sustained throughput | 
                        150 million+ CEPS (compliance policy evaluations per second) 
| 
                        Detection accuracy | 
                        4/4 typologies detected at every scale, per-entity verified 
| 
                        Federation: 100K entities, bilateral round | 
                        ~15 seconds per bilateral round (TCP localhost; real network adds latency) 
| 
                        Memory stability (50-epoch endurance test) | 
                        0 MB VRAM leak, 0 MB RSS growth 
| 
                        Transport security | 
                        AES-256-GCM encryption, Ed25519 authentication, active on every round 
| 
                        Policy framework | 
                        29 policies, 100 CPL rules, 9 domains, audited line-by-line against 38-page manual, 0 critical discrepancies 
            Four real-world money laundering typologies were tested: trade-based money laundering (over-invoicing across three banks), correspondent banking wire stripping, shell company layering networks, and funnel account structuring with cryptocurrency exit. In each case, no individual bank's monitoring system would have escalated the entity. Only cross-institutional federation detected the pattern.




            Each policy evaluation produces a cryptographic proof bundle: an attestation of the policy that fired, the inputs it read, and the verdict it produced. A regulator can independently verify, years after the fact, that the system correctly applied the approved policy to the available data.




---




## Why Seconds, Not Hours



            Readers accustomed to traditional AML batch processing, where transaction monitoring runs overnight and results are available the next morning, will reasonably question whether the performance figures above contain an error. They do not. The speed difference is not incremental improvement. It is a fundamental architectural shift.




## Why traditional systems are slow



            Conventional AML platforms were designed in the early 2000s. They run on CPU-based architectures, process transactions sequentially or in small batches, and evaluate rules one at a time against each transaction. When a bank processes 10 million daily transactions through 200 monitoring scenarios, the computation is: 10,000,000 transactions multiplied by 200 rules multiplied by CPU evaluation time per rule. On a 32-core server, this takes 4 to 12 hours depending on rule complexity.




            Cross-institutional detection adds another layer. If five banks want to compare customer risk, the traditional approach requires extracting data, pseudonymising it, transferring it to a central facility, loading it into a shared database, and running comparison queries. Each step takes hours. The total cycle is measured in days.




## Why ZQUAS is fundamentally different



1. GPU parallelism, not CPU sequential processing.



            The NVIDIA RTX 5090 has 170 streaming multiprocessors, each capable of running 2,048 concurrent threads. That is 348,160 simultaneous computation units. When ZQUAS evaluates 500,000 entities, it does not process them one at a time. It evaluates thousands simultaneously in a single GPU kernel launch. The 29 compliance policies are compiled to deterministic bytecode that executes directly on the GPU. The comparison is not 500,000 sequential evaluations. It is approximately 1,500 batched parallel launches, each processing hundreds of entities at once.




2. The MPC protocol is computationally lightweight.



            The cryptographic operations in a bilateral MPC round are: elliptic curve scalar multiplication for Private Set Intersection, symmetric-key encryption of garbled circuit gates (AES), and oblivious transfer key derivation. These are not expensive operations. For 5,000 entities, the entire PSI phase, which identifies shared customers without revealing non-shared ones, completes in under 20 milliseconds. The garbled circuit that compares risk scores evaluates in microseconds per entity.




            A common misconception is that "cryptographic" means "slow." Fully homomorphic encryption is slow: roughly 10,000-times overhead. MPC using garbled circuits and oblivious transfer is not. The overhead compared to plaintext computation is approximately 100 to 500 times for the comparison operation. The comparison itself is trivial, so 500-times overhead on a microsecond operation is still sub-millisecond.




3. No data extraction, no transfer, no central database.



            There is no ETL pipeline. There is no data warehouse. Each bank runs the ZQUAS installation alongside its existing infrastructure. The installation reads risk scores from the bank's own transaction monitoring system, encrypts them using the MPC protocol, and exchanges messages directly with peer banks over encrypted TCP. A binary escalation signal per shared entity is available in milliseconds. The entire overnight batch cycle is eliminated because the computation that justified it is replaced by a distributed cryptographic computation that runs in real time.




## Scaling behaviour






| 
                        Entities per bank | 
                        Pipeline time | 
                        Throughput | 
                        Detection | 
                        Policies 
| 
                        1,000 | 
                        228 ms | 
                        — | 
                        4/4 | 
                        29 (100 rules) 
| 
                        5,000 | 
                        344 ms | 
                        — | 
                        4/4 | 
                        29 (100 rules) 
| 
                        10,000 | 
                        492 ms | 
                        — | 
                        4/4 | 
                        29 (100 rules) 
| 
                        50,000 | 
                        1.4 seconds | 
                        — | 
                        4/4 | 
                        29 (100 rules) 
| 
                        100,000 | 
                        2.1 seconds | 
                        — | 
                        4/4 | 
                        29 (100 rules) 
| 
                        500,000 | 
                        under 2 seconds | 
                        150M+ CEPS | 
                        4/4 | 
                        29 (100 rules) 
            Three things to note. Throughput increases with entity count because larger batches amortise the fixed cost of GPU kernel launches. At 500K entities, the engine sustains 150 million+ compliance policy evaluations per second. These times are for GPU policy evaluation including full proof generation (Merkle root + Ed25519 signature). The 29 policies are not simplified test rules. They are the complete policy set spanning sanctions screening, PEP/EDD, transaction monitoring, fraud, KYC, crypto, and conduct, audited line-by-line with zero critical discrepancies.




## Privacy-preserving federation performance






| 
                        Configuration | 
                        Entities per bank | 
                        Per-round time | 
                        Protocol 
| 
                        2-bank bilateral round | 
                        100,000 | 
                        ~15 seconds (TCP localhost) | 
                        ECDH-PSI + GC + IKNP OT 
| 
                        Attestation per round | 
                        Any scale | 
                        Dual Ed25519 | 
                        Both parties sign; regulator verifies 
| 
                        Raw data shared | 
                        Zero bytes. Encrypted protocol messages only (ECDLP-protected) 
            Real network conditions add latency. The ~15 second figure is measured over TCP localhost. Federation rounds are expected to run nightly or on a configurable schedule aligned with existing monitoring cycles.




## Comparison with batch processing






| 
                        Scale | 
                        ZQUAS F1 | 
                        Traditional 24h batch | 
                        Speedup 
| 
                        100,000 entities, 100 policies | 
                        237.7ms | 
                        24 hours | 
                        hundreds of thousands× 
| 
                        500,000 entities, 100 policies | 
                        under 2 seconds | 
                        24 hours | 
                        millions× 
| 
                        Alert: ingestion to triage | 
                        under 10ms | 
                        24 hours | 
                        millions× 
            For comparison: a conventional CPU-based system evaluating 29 policies against 100,000 entities requires extracting the data, running sequential rule evaluation, and waiting for the batch cycle to complete. Conservative estimate: 4 to 12 hours. ZQUAS evaluates the same 100,000 entities in 237.7 milliseconds.




---




## Anticipating Challenges



            A claim this significant invites scrutiny. We welcome it. Below are the objections we expect, and our responses.




## "The MPC protocol hasn't been independently audited."



            Correct. The ZQUAS MPC implementation (ECDH-PSI with Chou-Orlandi oblivious transfer, Yao's garbled circuits with Free-XOR optimisation, and OT extension) has been internally audited against a hostile threat model covering transport authentication, encryption, replay protection, deserialisation bounds, GPU memory safety, and timing side channels. 37 findings were identified and remediated. No independent third-party cryptographic audit has been conducted.




            An independent audit is a prerequisite for production deployment, not for sandbox engagement. The sandbox is precisely the environment in which to conduct such an audit under regulatory supervision.




## "The DPA hasn't confirmed MPC outputs aren't personal data."



            Also correct. Our position is that MPC protocol messages are not personal data under GDPR, because they are computationally indistinguishable from random values. This is a legal argument, not settled law. No EU Data Protection Authority has issued a formal ruling on this question.




            This is one of the three objectives of our sandbox proposal: to engage the Autoriteit Persoonsgegevens or the European Data Protection Board and obtain a formal assessment. If the DPA concludes that MPC protocol messages do constitute personal data, the Article 75 framework would apply and the scope would be limited to higher-risk customers. That is still a significant improvement over the current state (no cross-institutional detection at all), but it would not achieve full customer base federation.




## "The performance numbers can't be real with production-grade policies."



            This is the most important objection to address. The 29 policies used in the benchmark are not toy rules. They are the complete policy set from a 38-page compliance policy manual: 100 individual rules across 9 regulatory domains, 5 cross-domain chains, regulatory traceability to FATF 40, EU AMLD5/6, Wwft, BSA, FCA Handbook, OFAC, and MiCA, and decision logic that includes multi-threshold scoring, temporal aggregation, counterparty risk assessment, and composite EDD weighting. The policies have been audited line-by-line. Zero critical discrepancies remain.




            The performance is real because the bottleneck in cross-institutional detection is not policy evaluation. It is the cryptographic protocol. The 29 policies evaluate in microseconds per entity on GPU. The MPC round (PSI, garbled circuit, oblivious transfer) takes milliseconds. Even if policies were 100 times more complex, the round time would increase only marginally, because the policy evaluation component is already the smaller term.




## "What about false positives at scale?"



            In the production benchmark, 4.1% of background entities produced non-zero risk scores through real policy evaluation. Zero of these entities were falsely escalated through federation, because individual risk scores remained below the combined threshold. The cross-bank correlation acts as a natural filter. Moderate risk at one bank is not suspicious unless corroborated by risk at another bank.




            The relevant question is whether the false positive rate will remain this low with real customer data. We expect it to increase. Real customer bases have sanctions name collisions, PEPs with legitimate business, and cash-intensive entities with ambiguous profiles. Industry-standard AML false positive rates are 90 to 95 percent. A production rate of 1 to 5 percent would be a significant operational improvement. Quantifying this requires a pilot with real or representative data, which is one of the objectives of the sandbox engagement.




## "How does this integrate with our existing Actimize, Oracle, or SAS stack?"



            ZQUAS does not replace a bank's existing transaction monitoring system. It sits alongside it. The bank's existing system produces risk scores for its customers. ZQUAS consumes those scores and federates them across institutions. The integration point is a single data feed: entity identifier plus risk score. No changes to the bank's existing alert workflow, case management, or SAR filing process are required.




            For banks that wish to use ZQUAS for single-institution monitoring as well, the 29 CPL policies can replace or supplement existing rules. This is optional. The cross-institutional detection, the capability no existing system provides, requires only a risk score per entity.




## "What infrastructure does each bank need?"



            For a pilot with 3 to 5 banks, each bank deploys a ZQUAS installation (one server or VM) and opens outbound TCP connections directly to the other participants. A 3-bank pilot requires 2 outbound connections per bank. A 5-bank pilot requires 4. No relay server. No neutral third party. No additional infrastructure beyond the installation itself. All connections are encrypted with AES-256-GCM and authenticated with Ed25519.




            As the network grows beyond 10 to 15 institutions, an optional relay server simplifies the network topology. Each bank then maintains a single outbound connection to the relay instead of N-1 connections to individual peers. The relay is a stateless encrypted message router. It cannot read, modify, or store any message content. The transition from direct to relay mode is a configuration change, not a code change.




            At production scale (50 or more banks), the relay operator should be a regulated AML utility, analogous to CLS Bank in foreign exchange settlement. Jointly owned by participating institutions, independently audited, regulated by the relevant financial authority. That governance discussion follows after the pilot proves the detection works.




## "What if a participating bank is compromised?"



            The MPC protocol is secure against a semi-honest adversary: a bank that follows the protocol correctly but attempts to extract additional information from the messages it receives. Under this model, a compromised bank learns nothing beyond the binary escalation signal.




            Against a fully malicious adversary (a bank that deviates from the protocol), the current bilateral implementation provides limited protection. The mitigation is operational: the cryptographic proof bundle provides a record of every input to every round. If a bank submits anomalous risk scores to probe the other bank's data, this pattern is detectable in the attestation log.




            Stronger malicious-adversary guarantees are architecturally designed for networks exceeding 30 institutions, based on 4-party MPC with guaranteed output delivery. This is not yet implemented. It is the natural evolution for large-scale production deployment.




---




## The Path Forward



            We are not asking regulators to take our word for it. We are asking for the opportunity to demonstrate, in a supervised environment, that MPC federation achieves the detection capability that Article 75 partnerships seek, without the privacy trade-off that Article 75 was forced to accept.




1. Regulatory sandbox engagement (DNB InnovationHub / FCA Digital Sandbox)



            Deploy the ZQUAS federation platform in a sandbox environment with synthetic or historical data from participating banks. Demonstrate cross-institutional detection of known laundering typologies. Measure false positive rates. Validate the cryptographic attestation mechanism. Establish whether MPC protocol messages constitute personal data under GDPR.




2. Data Protection Authority consultation



            Engage the Dutch Autoriteit Persoonsgegevens and the European Data Protection Board to obtain a formal assessment of whether MPC federation falls within the scope of personal data processing under GDPR. If it does not, the Article 75 restrictions on customer scope are inapplicable, and full customer base federation is legally permissible.




3. Pilot with participating institutions



            Conduct a live pilot with 3 to 5 Dutch or UK banks, using the bilateral MPC protocol over direct encrypted peer-to-peer connections. No relay infrastructure required. The pilot would federate real or representative customer risk data across institutions, detect cross-bank patterns, and produce auditable results. No institution accesses any other institution's customer data.




            The technology exists. The regulatory framework exists. The criminal activity that both were designed to address continues at an estimated $800 billion to $2 trillion annually according to the UNODC. What remains is the willingness to test whether mathematics can solve what policy could not.






**Ready to discuss a pilot?**



Three Founding Partner slots available. Direct engagement with your regulator included.



                [Contact us](contact.html)
                [Founding Partner Programme](founding-partner.html)




            This document does not constitute legal advice. The legal position regarding MPC and GDPR should be validated through formal engagement with the relevant Data Protection Authority. Performance figures are from testing on production hardware with synthetic data. False positive rates on live customer data may differ and should be established through a supervised pilot.



            Danny de Gier

                Founder, ZQUAS. 18+ years in financial crime compliance at Tier-1 banks and fintechs.
                Professional Postgraduate Diploma in Financial Crime Compliance (ICA / University of Manchester).

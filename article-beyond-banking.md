# Beyond Banking: Cross-Sector Federated Detection for Financial Crime, Telecommunications Fraud, and Digital Asset Compliance

> A ZQUAS position paper. A single detection engine that correlates risk signals across banks, telecommunications operators, and digital asset platforms without sharing raw data between institutions. The same code, the same cryptographic protocols, the same GPU-native detection pipeline, applied to every regulated sector where financial crime operates.

Source: https://zquas.ai/article-beyond-banking.html
Site: https://zquas.ai

---
[← Articles](articles.html)
        April 2026 · Position Paper · 30 min read


# Beyond Banking: Cross-Sector Federated Detection for Financial Crime, Telecommunications Fraud, and Digital Asset Compliance



A single detection engine that correlates risk signals across banks, telecommunications operators, and digital asset platforms without sharing raw data between institutions. The same code, the same cryptographic protocols, the same GPU-native detection pipeline, applied to every regulated sector where financial crime operates.



*Danny de Gier, Founder ZQUAS. 18 years financial crime compliance: Deutsche Bank, HSBC, RBS, ABN AMRO, ClearBank, Vivid Money. PGDip Financial Crime Compliance, University of Manchester.*







## 1. The Cross-Sector Problem



Financial crime does not respect institutional boundaries. It does not respect sectoral boundaries either.



An Authorised Push Payment fraud starts with a phone call. The fraudster calls the victim, impersonating their bank. The call is routed through a telecommunications network. The victim, convinced their account is compromised, transfers funds to a "safe account" controlled by the fraudster. The money moves through two or three bank accounts within minutes. Within hours, it exits through a cryptocurrency exchange into a stablecoin, crosses a blockchain bridge, and arrives in a jurisdiction with no bilateral cooperation agreement.



The telecommunications operator saw the call. It came from a number that contacted 47 different people in the past week. That pattern is visible in the call detail records. The telco did not share this information with the bank.



The bank saw the payment. A high-value transfer to a first-time payee, initiated within two hours of an inbound call. The bank did not know about the call because it has no access to telecommunications data.



The cryptocurrency exchange saw the deposit. Funds arriving from a bank account that was opened three weeks ago, immediately converted to stablecoin and bridged to another chain. The exchange did not know the funds originated from an impersonation fraud because it has no access to either the banking or telecommunications data.








Three institutions. Three data domains. Three independent compliance systems. Each one sees a fragment. None of them sees the crime.



This is not a technology failure. Current transaction monitoring systems are designed to operate within a single institution. They were never architected to correlate signals across sectors. According to the [UK Finance Annual Fraud Report 2025](https://www.ukfinance.org.uk/news-and-insight/press-release/fraud-report-2025-press-release), criminals stole GBP 1.17 billion through payment fraud in 2024, of which GBP 450.7 million was lost to APP fraud alone. 70 per cent of APP fraud cases started online, while 16 per cent originated through telecommunications networks.



The criminals have cross-sector visibility. The compliance infrastructure does not.



## 2. What Exists Today



Before describing the cross-sector architecture, it is important to establish what is already built and operational. This paper describes a vision that extends from a production-ready foundation, not a theoretical concept that requires everything to be built from scratch.



The ZQUAS F1 Engine is a GPU-native financial crime detection engine comprising approximately 396,000 lines of C++ and CUDA code with 493 GPU kernels. It is not a prototype, a proof of concept, or a roadmap. The banking detection pipeline is production-ready.



### 2.1 Banking Detection: Production-Ready



The engine processes 500,000 entities in under 2 seconds with an alert lifecycle under 10 milliseconds. Total VRAM consumption is under 1 gigabyte. It runs on hardware ranging from a consumer-grade laptop GPU to data centre GPUs (A100, H100). The same binary, the same detection pipeline, different throughput.



The detection pipeline evaluates five layers covering temporal analysis, structural graph analysis, behavioural profiling, corridor analysis, and flow path reconstruction. All five layers execute on GPU with over 100 compiled compliance policies evaluated by the GPU-native policy engine. Transaction processing, entity resolution, policy evaluation, alert lifecycle, case management, and regulatory reporting are all implemented.



### 2.2 Bank-to-Bank Federation: Production-Ready



The federation protocol implements Elliptic Curve Diffie-Hellman Private Set Intersection (ECDH-PSI) for entity matching, bilateral escalation signal propagation, and cryptographic evidence attestation. Federation rounds complete in under 10 seconds per bilateral pair. The protocol has been validated across simulated multi-bank deployments.



This is not a theoretical protocol. It is compiled code that runs, produces verifiable results, and has been tested across multiple simulated banking topologies.



### 2.3 Financial Crime Network Simulator: Production-Ready



The F1 Engine includes a GPU-native simulation environment that generates synthetic banking populations with embedded criminal networks. 15 criminal typologies (8 AML, 7 APP fraud) generate realistic transaction data on GPU. The simulator is calibrated against published national statistics for three jurisdictions (Netherlands, United Kingdom, Germany). Over 300 tests pass with strict assertions.



The simulator enables closed-loop calibration: generate a population with known criminals, run detection, measure results against ground truth, optimise thresholds. The threshold optimisation evaluates thousands of configurations in seconds on GPU across multiple adversarial difficulty levels.



### 2.4 Maturity Summary





| 
                    Capability | 
                    Status 
| 
                    **Banking transaction ingestion** | 
                    Production-ready. Deployed. 
| 
                    **Bank-to-bank federation (ECDH-PSI, escalation propagation)** | 
                    Production-ready. Tested. 
| 
                    **Five-layer detection pipeline (GPU-native)** | 
                    Production-ready. Over 100 policies compiled. 
| 
                    **Financial Crime Network Simulator (15 typologies)** | 
                    Production-ready. Over 300 tests. 
| 
                    **Evidence system with blind assessment workflow** | 
                    Production-ready. Implemented. 
| 
                    **Deterministic entity hashing (pre-PSI)** | 
                    Production-ready. Implemented. 
| 
                    **Cryptographic erasure (hierarchical per-entity keys)** | 
                    Production-ready. Implemented. 
| 
                    **Differential privacy on federation signals** | 
                    Architecture designed. Phase 2. 
| 
                    **Signal velocity circuit breaker on federation** | 
                    Architecture designed. Phase 2. 
| 
                    **Cross-sector score calibration** | 
                    Architecture designed. Calibration infrastructure exists. Phase 2. 
| 
                    **Telecommunications ingestion pipeline (CDR/TMDR)** | 
                    Planned. Phase 2 (Q3 2026). 
| 
                    **Blockchain ingestion pipeline (EVM/UTXO)** | 
                    Planned. Phase 3 (Q4 2026). 
Everything in this paper that is described as "architecture" or "planned" is clearly labelled as such. Everything described without qualification is built, tested, and operational.





## 3. The Regulatory Direction



Regulators are converging on cross-sector responsibility. The evidence is unambiguous.



### 3.1 Singapore: Shared Responsibility Framework



Singapore's Monetary Authority (MAS) and Infocomm Media Development Authority (IMDA) implemented the [Shared Responsibility Framework](https://www.mas.gov.sg/news/media-releases/2024/mas-and-imda-announce-implementation-of-shared-responsibility-framework-from-16-december-2024) on 16 December 2024. It is the first regulatory framework in the world to hold both financial institutions and telecommunications operators jointly liable for fraud losses.



The framework operates on a waterfall principle. If the bank breached its duties (real-time fraud surveillance, cooling-off periods, transaction alerts), the bank bears the loss. If the bank complied but the telco breached its duties (SMS sender ID authentication, scam filtering, authorised aggregator controls), the telco bears the loss. If both complied, the consumer bears the loss.



MAS added a fraud surveillance duty effective 16 June 2025, requiring banks to detect and block suspicious transactions in real time. This is not batch processing with faster turnaround. It is continuous monitoring with the authority to halt transactions before settlement.



As MAS stated in the framework consultation: no other known jurisdiction had included telecommunications operators in a scam reimbursement framework at the time of publication. Singapore positioned itself as the global reference model.








### 3.2 United Kingdom: Converging Frameworks



The UK is assembling the same structure through multiple regulatory instruments.



The Payment Systems Regulator's [APP fraud reimbursement regime](https://www.psr.org.uk/publications/policy-statements/ps247-faster-payments-app-scams-reimbursement-requirement-confirming-the-maximum-level-of-reimbursement/), effective 7 October 2024, requires payment service providers to reimburse victims up to GBP 85,000 within five business days. The cost is split equally between sending and receiving payment firms.



The UK [Telecommunications Fraud Sector Charter](https://www.gov.uk/government/publications/fraud-sector-charter-telecommunications/fraud-sector-charter-telecommunications-accessible-version), published 5 November 2025, commits telecommunications operators to cross-industry intelligence sharing, API-driven fraud data exchange, and AI-powered fraud prevention. The Charter establishes working groups between the Home Office, banks, and telcos.



[Ofcom's consultation on combatting mobile messaging scams](https://www.ofcom.org.uk/phones-and-broadband/scam-calls-and-messages/new-rules-to-protect-people-and--businesses-against-mobile-messaging-scams), published 29 October 2025, proposes mandatory Know Your Customer checks for business message senders, sender ID verification, and anti-scam filtering. An estimated 100 million suspicious messages were reported to operators through the 7726 service in the year to April 2025.



The Data (Use and Access) Act 2025 establishes crime and fraud prevention as a lawful basis for data sharing, as referenced in the [UK Government's Fraud Strategy 2026-2029](https://assets.publishing.service.gov.uk/media/69aea29d917847c0a4c8999e/E03551200_Fraud_Strategy_2026__English__ELAY.pdf). The ICO has confirmed that data protection is not an excuse when tackling scams and fraud.



The UK Government's Fraud Strategy 2026-2029, published March 2026, explicitly calls for cross-sector collaboration between financial, telecommunications, and technology sectors, supported by the new Operational Crime Centre launching April 2026.



### 3.3 European Union: AMLR Article 75 and MiCA



The Anti-Money Laundering Regulation (AMLR) Article 75 mandates mechanisms for cross-institutional information sharing. The Anti-Money Laundering Authority (AMLA) will assume oversight tasks from 2027, as confirmed by the [Netherlands Court of Audit](https://english.rekenkamer.nl/latest/current-audits/consequences-of-anti-money-laundering-policy).



The Markets in Crypto-Assets Regulation (MiCA) became fully applicable in December 2024, following a phased rollout in which stablecoin provisions took effect from June 2024. MiCA requires crypto-asset service providers to implement transaction monitoring, suspicious activity reporting, and customer due diligence equivalent to traditional financial institutions. CASPs are now regulated entities with the same compliance obligations as banks.



When a stablecoin payment originates at a bank, transits through a blockchain, and settles at an exchange, every entity in the chain is a regulated institution under either AMLR or MiCA. The regulatory obligation to detect financial crime exists at every step. The technology to correlate signals across those steps does not.



### 3.4 SWIFT: The Institutional Blockchain Transition



[SWIFT announced on 29 September 2025](https://www.swift.com/news-events/press-releases/swift-add-blockchain-based-ledger-its-infrastructure-stack-groundbreaking-move-accelerate-and-scale-benefits-digital-finance) that it will add a blockchain-based shared ledger to its technology infrastructure, developed in collaboration with over 30 financial institutions including JP Morgan, HSBC, Deutsche Bank, NatWest, and Bank of America.



This transition has a direct consequence for financial crime detection. Today, public blockchains provide full transaction transparency. Compliance tools like Chainalysis and Elliptic operate by analysing this public ledger. When institutional adoption moves settlement onto permissioned chains and private ledgers, that transparency disappears. A bank will not expose its stablecoin transaction flows to competitors on a public chain.



A permissioned ledger with 30 banks does provide shared consensus. Consensus, however, is not detection. Validator participants verify that transactions are structurally valid and properly authorised. They do not evaluate whether a circuit of individually valid transactions constitutes money laundering. Detection requires behavioural analysis across the entity graph over time, which is a fundamentally different computational task from transaction validation. Furthermore, the telecommunications operator and the cryptocurrency exchange are not participants on the bank's private ledger. The cross-sector gap remains even when the intra-sector gap narrows.



## 4. The Architecture



### 4.1 Design Principle



The ZQUAS F1 Engine operates on entities and relationships between entities. A bank customer who is also a mobile subscriber who is also a crypto exchange user is one entity with three institutional views. The detection pipeline evaluates risk based on the combined signal surface, not on any single institutional perspective.



At the federation layer, the engine treats all data sources uniformly: a sender, a receiver, a value, and a timestamp. This uniformity enables the same federation protocol to operate between a bank and a telco as between two banks.



This does not mean that all data sources are equally simple to process. Financial crime detection within a single sector depends on rich, sector-specific features. A banking installation analyses transaction narratives, merchant categories, and payment patterns. A telco installation analyses call patterns, SIM lifecycle events, and network behaviour. A crypto installation analyses wallet clustering, bridge usage, and mixer proximity. These sector-specific features produce entity-level risk assessments that are comparable across sectors through calibration (Section 4.7), even though the underlying feature sets are different.



The banking pipeline is production-ready today. The telecommunications and blockchain pipelines are planned engineering milestones. The detection engine, federation protocol, and scoring infrastructure are already operational and data-agnostic. What remains is building the sector-specific ingestion adapters and tuning the detection parameters per data domain.



### 4.2 The Four-Installation Federation








The federation protocol connects institutional installations as peers. Each installation is architecturally identical regardless of the sector it serves.



**Installation Type 1: Banking Institution.** The bank runs an F1 Edge Installation in its data centre. It ingests transactions from its core banking system. The detection pipeline evaluates every transaction at the point of processing. The installation produces entity-level risk assessments based on the bank's own data.



**Installation Type 2: Telecommunications Operator.** The telco runs an identical F1 Edge Installation. It ingests call detail records (CDRs), text message records (TMDRs), SIM lifecycle events, and customer onboarding data. The detection pipeline evaluates communication patterns: burst calling, SIM swap sequences, call-then-payment timing correlations, and known scam number patterns. The installation produces entity-level risk assessments based on the telco's own data.



**Installation Type 3: Digital Asset Platform.** The exchange runs an identical F1 Edge Installation. It ingests on-chain transactions, deposit and withdrawal events, wallet clustering data, and KYC records. The detection pipeline evaluates patterns indicative of laundering, rapid conversion, and cross-chain obfuscation. The installation produces entity-level risk assessments based on the exchange's own data.



**Installation Type 4: Regulatory Observer.** The regulator connects as a read-only observer. It receives aggregated, anonymised detection metrics without accessing any institution's raw data or entity-level identifiers. It sees: detection rates, alert volumes, federation participation rates, cross-sector signal contribution, and crucially, false positive rates alongside detection rates. This dual reporting (precision and recall, not just detection volume) prevents a "race to the top" where institutions over-calibrate their detection to avoid appearing as regulatory laggards, generating false positive explosions and wrongful de-risking of innocent customers. The observer provides the data for regulators to measure detection quality, not just quantity.



The observer does not receive entity-level data and cannot be used for prosecution. Evidence for law enforcement is handled through a separate mechanism described in Section 4.10.



### 4.3 Cross-Sector Entity Matching



The critical technical challenge is linking the same person across institutional boundaries without sharing personal data.



Banks identify customers by government-issued ID (passport number, national identity number), name, date of birth, and address. Telecommunications operators identify customers by the same government-issued ID, collected during mandatory KYC at SIM registration. Crypto exchanges identify customers by government-issued ID, collected during mandatory onboarding KYC under MiCA or national licensing requirements.



In the target launch jurisdictions, a single government identifier serves as the natural join key across all regulated sectors. In the Netherlands, the BSN (Burgerservicenummer) is mandatory at banks (Wwft), telcos (SIM registration), and crypto exchanges (Wwft). In the United Kingdom, the National Insurance number and passport serve equivalent functions across regulated institutions.



The F1 Engine uses ECDH-PSI to discover common entities without revealing the underlying identity data. Institution A blinds its set of identity hashes. Institution B blinds its set. The protocol produces the intersection: entities present in both sets. Neither institution learns anything about entities that are not in the intersection. The protocol is GPU-accelerated and provably secure under standard cryptographic assumptions.








The matching operates on two tiers, each serving a different detection purpose:



**Tier 1: Government-issued ID hash.** Exact match after normalisation. Highest confidence. Available at all regulated institutions. This is the primary matching mechanism for AML detection, where the same person launders money across institutions using the same identity.



**Tier 2: Phone number hash in E.164 format.** This is the primary matching mechanism for APP fraud detection. In APP fraud, the fraudster and the mule are typically different people. The fraudster uses a burner SIM. The victim sends money to a mule account at a different bank. Government ID matching between the telco and the bank will not link them because they are different individuals. The link is the victim: the same person who is both a telco subscriber being targeted by a scam pattern and a bank customer initiating an unusual payment. Phone number matching identifies the victim across both sectors, enabling the telco's "this subscriber is being targeted" signal to reach the bank before the payment settles.



### 4.3.1 ID Fragmentation in Multi-Document Jurisdictions



Not all jurisdictions have a single universal identifier. A customer might use a passport to open a bank account and a driving licence to register a SIM card. If only one ID type is hashed, the PSI will miss the match.



The protocol addresses this through multi-ID hashing: each institution hashes every government ID type it holds for each entity (passport, driving licence, national ID number) into separate PSI sets. The intersection is computed across all ID-type pairs. A match on any single ID type is sufficient to establish cross-sector linkage. This increases PSI computation linearly (proportional to the number of ID types, typically 2-3), not exponentially. It is an engineering optimisation, not an architectural change.



In the Netherlands and the UK, where a single mandatory identifier covers all regulated sectors, multi-ID hashing is a fallback for edge cases. In jurisdictions without a universal ID, it becomes the primary matching mechanism and carries a higher false-negative rate.



### 4.4 The Normalisation Pipeline



PSI operates on exact hash matches. If Bank A records "J. van de Gier, Hoogstraat 12a, 1234AB" and Telco B records "Johannes van de Gier, Hoogstraat 12A, 1234 AB", a naive hash comparison will fail despite referring to the same person.



The solution is deterministic normalisation before hashing, not fuzzy matching inside the cryptographic protocol. Each institution applies the same normalisation rules to its own data before blinding. The rules include case normalisation, punctuation and whitespace stripping, abbreviation standardisation, and ISO formatting of document numbers and phone numbers (E.164). The normalised output is concatenated into a canonical string and hashed before entering the PSI protocol.



This pipeline runs locally at each institution before any data enters the cryptographic protocol. It is deterministic: the same input always produces the same canonical form. In jurisdictions with standardised address formats (Dutch postcode plus house number, UK postcode plus building number), this achieves near-perfect matching accuracy on the primary government ID identifier, where formatting variation is minimal (BSN is a 9-digit number, NI number follows a fixed alphanumeric pattern).



The current implementation applies deterministic canonical hashing to entity identifiers. The full normalisation pipeline with jurisdiction-specific abbreviation mapping and document formatting is specified and planned for Phase 2.



### 4.5 Signal Propagation and Privacy Protection



Once entities are matched, risk signals propagate through the federation.



Each installation computes local risk assessments for its entities based on its own data and its own detection pipeline. When an installation's detection pipeline determines that an entity warrants cross-institutional attention, an escalation signal propagates to matched peers. The receiving installation incorporates this cross-sector signal as a risk elevation in its own assessment.



No raw transactions, no CDRs, no blockchain addresses, no customer names cross institutional boundaries. The federation shares only the escalation decision, not the underlying data or reasoning.




In the current production architecture, federation signals are binary escalations: escalated or not escalated. Unlike quantitative risk scores, binary signals are mathematically immune to threshold drift. An escalation is either propagated or it is not. There is no intermediate value that noise, rounding, or miscalibration can degrade. This design ensures that no institution can claim a signal was "too ambiguous to act on."





### 4.5.1 Batched Federation Rounds



Escalation signals are not propagated per-event. They are batched into federation rounds that aggregate multiple events. If a telco detects burst messaging at 09:42, a SIM swap at 10:15, and a suspicious CDR pattern at 11:30, the receiving bank sees a single aggregated signal at the next federation round. The bank cannot determine which specific event triggered the escalation or at what time it occurred. This decoupling of signal from event timing defeats inference attacks where a receiving institution attempts to reconstruct the sender's private data from timing correlations.



### 4.5.2 Differential Privacy (Planned)



Phase 2 will introduce quantitative risk deltas alongside binary escalation signals, enabling richer cross-sector intelligence. Each delta will include calibrated noise providing formal differential privacy guarantees. The privacy budget will be configurable per federation agreement.



The differential privacy noise will apply to the inter-institutional signal, not to the receiving institution's internal assessment. The receiving institution will combine the noised cross-sector indicator with its own full-resolution local data. A compliance officer at the receiving bank sees their own bank's complete transaction history plus a cross-sector risk elevation. Their legal duty to act under the UK's APP regime or Singapore's SRF is assessed on this combined picture, not on any single noised input. The local action threshold remains under the sole control of the receiving institution. Privacy-preserving noise never serves as a justification for inaction.



Where a case requires un-noised evidence for prosecution or asset seizure, the evidence attestation mechanism (Section 4.10) produces it under judicial warrant.



### 4.5.3 Signal Velocity Circuit Breaker (Planned)



To prevent any single installation from flooding the federation with escalation signals (whether through miscalibration, adversarial intent, or mule proliferation using compromised identities), a signal velocity check will operate at the federation level. If an installation emits more than a configurable threshold of escalation signals per federation round, propagation will be paused for that installation and flagged for review.



A circuit breaker for alert processing already operates within the engine's case management subsystem. Extending this to federation round throttling is a planned Phase 2 enhancement.



### 4.6 Intersection Privacy and Anti-Leakage Controls



In a bilateral PSI protocol, both parties learn the intersection: which entities they share. While neither party sees the other's full customer list, the intersection itself reveals customer overlap between two specific institutions. In a competitive environment, this metadata has commercial value. This creates a potential tension with GDPR Article 5(1)(b) purpose limitation.



The architecture mitigates this through three controls.



First, the PSI is risk-filtered. Only entities that exceed a local risk threshold enter the PSI set. If a bank has 2 million customers but only 50,000 are in elevated-risk categories, the PSI operates on 50,000 entities, not 2 million. The intersection reveals overlap only within the risk population, not the full customer base.



Second, the intersection result is ephemeral. Matched entity identifiers are used for signal propagation during the federation round and then discarded from the federation working memory. The institution stores "Entity X has cross-sector risk elevation" with a sector label (telecommunications, digital assets), not an institution name.



Third, PSI query budgets limit the number of federation rounds per bilateral pair per period. This prevents an institution from running continuous PSI to incrementally map the other's customer base over time.



### 4.7 Cross-Sector Score Calibration and Signal Quality (Planned)



A risk assessment from a telecommunications operator does not carry the same evidentiary weight as one from a Tier-1 bank. Raw assessments are not directly comparable across sectors.



The F1 Engine's simulation environment addresses this calibration challenge. The simulator generates synthetic populations with activity across multiple sectors. Criminal networks are embedded with known ground truth labels. Each sector's installation runs detection independently. The calibration engine measures the mapping between sector-specific assessments and actual criminal activity.



The calibration is computed bilaterally. Both institutions run the simulator with identical synthetic populations and independently verify the mapping output. Both see the same ground truth. Both can confirm the mapping is fair. ZQUAS provides the calibration infrastructure. The institutions own the calibration outcome.



The bilateral calibration also establishes signal quality floors. Before live signals propagate, both installations run a calibration round using the same synthetic population. If an installation's detection precision or recall on the synthetic ground truth falls below a negotiated minimum, the counterpart installation can automatically quarantine that installation's signals until recalibration. This mechanism forces poorly calibrated installations to improve their detection before they can influence the wider federation. The signal velocity circuit breaker catches aggressive installations (too many signals). The bilateral calibration floor catches negligent installations (low quality signals). Together they bound signal quality from both directions.



The simulation environment currently generates banking populations. Cross-sector simulation is a Phase 2 engineering milestone.



### 4.8 The APP Fraud Detection Example: Victim-Centric Linkage



In most professional APP fraud, the fraudster and the mule are different people. The fraudster uses a burner SIM or stolen identity to make the call. The victim sends money to a mule account at a different bank. Matching the fraudster's identity across sectors will not work because the fraudster takes deliberate steps to avoid identity linkage.



The architecture solves this by centering the linkage on the victim.








**Step 1:** A fraudster operating from a burner SIM calls 200 potential victims. The telco's F1 installation detects that multiple subscribers are receiving calls from a number exhibiting a scam pattern (burst calling to many targets in a short window). Each targeted subscriber's entity is flagged locally: "this subscriber is being targeted by a scam cluster." No data leaves the telco.



**Step 2:** At the next batched federation round, the federation protocol runs a PSI match on Tier 2 (phone number). The victim's phone number appears in both the telco's elevated-risk set and the bank's customer set (because the victim is a bank customer). The match identifies the victim, not the fraudster.



**Step 3:** The telco's escalation signal propagates to the bank: "this customer is being targeted by a telecommunications scam pattern." The bank cannot determine which phone number called the victim, what was said, or when the call occurred. It knows only that its customer has been identified as a scam target by the telecommunications sector.



**Step 4:** Hours later, the victim, convinced by the fraudster's call, initiates a payment to the mule's account. The bank's F1 installation evaluates the transaction in real time (under 10 milliseconds). The victim's entity has a pre-existing cross-sector signal: "targeted by telecommunications scam pattern." The bank's detection pipeline combines this with the transaction characteristics: first-time payee, high-value transfer, unusual payment pattern. Alert generated.



**Step 5:** The bank holds the payment for review. The compliance officer sees: the customer's own transaction history, plus a cross-sector indicator that this customer was recently targeted by a scam pattern on the telecommunications network. The officer investigates the specific payment, not the customer's entire account. The customer's salary deposits, direct debits, and routine transactions continue uninterrupted. Only the specific high-risk payment is held.




Without federation: the bank sees a payment to a new payee. That happens thousands of times per day. It is not suspicious in isolation. With federation: the bank sees a payment to a new payee from a customer who was recently targeted by a telecommunications scam pattern. The telco's targeting signal, which the bank never sees directly, has changed the risk calculus for a transaction the bank processes.





The critical insight: the architecture does not need to unmask the fraudster to protect the victim. By correlating the targeting signal at the telco with the transfer signal at the bank, the fraud lifecycle is broken before the first payment settles.



A note on service continuity: the escalation signal elevates risk on the specific transaction context, not on the victim's account. The victim is a customer being protected, not a suspect being investigated. Their account remains fully functional. Only the specific payment to the suspicious counterparty is held for review. This distinction is enforced by the policy engine, which evaluates risk at the transaction level, not the entity level.



A note on timing: the local bank detection operates in under 10 milliseconds. The federation round (under 10 seconds per bilateral pair) pre-enriches entity risk profiles between transactions. When the payment arrives, the cross-sector signal is already present. The local installation blocks in real time. The federation enriches over rounds.



### 4.9 The Private Blockchain Detection Example



**Step 1:** A bank customer initiates a GBP payment through SWIFT's blockchain-based ledger. The payment settles as a stablecoin transfer on a permissioned chain operated by a consortium of banks.



**Step 2:** The recipient converts the stablecoin to a different token on a public chain through a regulated bridge operated by a licensed CASP.



**Step 3:** The tokens are sent to a mixer on the public chain and redistributed to multiple wallets.



On the permissioned chain: only the participating banks see the transaction. Chain analysis tools have no access. The blockchain's consensus mechanism confirms the transaction is valid, but validity is not innocence. Every individual transaction in a laundering circuit is structurally valid.



On the public chain: the bridge transaction and mixer interaction are visible but there is no link back to the originating bank payment because the permissioned chain is private.



**With cross-sector federation:** The bank's F1 installation assesses the originating entity based on transaction patterns. The CASP's F1 installation assesses the bridge user based on rapid conversion and mixer interaction. The PSI matches the entity across both installations (same government ID at KYC). The CASP's escalation signal propagates to the bank. The bank now knows that the entity it processed a payment for has elevated risk at a crypto-asset service provider, without knowing the specific blockchain addresses or on-chain behaviour.



**Without federation:** the bank sees a settled payment. The CASP sees a bridge user heading to a mixer. Neither connects the dots.



### 4.10 Evidence Attestation



The regulatory observer receives aggregated metrics for supervisory purposes. It does not receive entity-level data.



When a case requires law enforcement action, the F1 Engine generates an evidence package for each cross-sector alert. The package contains: investigation items compiled from the detecting institution's own data (no cross-institutional raw data); a cryptographic attestation transcript signed by each participating installation proving that correlated risk signals were detected at Time T across N institutions; and sector attribution indicating which sectors contributed signals without revealing the specific signals or raw data.



When the FIU or law enforcement agency issues a warrant, each participating institution provides its own raw data under existing production order procedures. The attestation transcript proves the correlation existed and when it was detected. The prosecutor can demonstrate cross-sector criminal activity without the institutions ever having seen each other's files.



The evidence system includes a human assessment workflow where an investigator reviews items without ground truth labels and makes an independent judgment. This produces a documented audit trail of human decision-making, separate from algorithmic detection, essential for regulatory compliance and court proceedings.



### 4.11 Protocol Governance



A federated system raises the question: who decides the rules?



The answer is: nobody decides what to detect. Everybody decides how to share.



Each institution compiles its own detection policies into GPU-evaluable rules using the engine's policy language. Bank A can run 200 policies. Bank B can run 150. A telco can run 50 completely different policies. No institution needs to agree on what constitutes suspicious activity. They only agree on how to share the output: entity-level escalation signals.



The typology lives inside the installation, not inside the protocol. If the FCA publishes guidance on a new APP fraud variant tomorrow, the UK bank updates its policies and recompiles. The Dutch bank does not need to change anything. The federation protocol does not change. The bank's escalation signals for affected entities change, and those signals propagate normally.



ZQUAS can distribute new typology detection modules, but each institution decides whether to enable them and with what parameters. Threshold optimisation runs locally per institution.



The protocol governance is limited to: data format versioning, federation round timing, PSI parameters, privacy budgets, PSI query limits, and signal quality floors. These are negotiated bilaterally, the same way SWIFT governs message formats without dictating what banks do with the messages.



## 5. GDPR Compliance Architecture



### 5.1 No Raw Data Sharing



No institution shares raw customer data, transaction records, CDRs, or blockchain addresses. The federation shares binary escalation signals: derived decisions, not personal data.



### 5.2 Cryptographic Entity Matching



The ECDH-PSI protocol blinds all identity data before comparison. Neither institution reveals its customer list to the other. The intersection is computed on blinded points. The protocol is provably secure under standard cryptographic assumptions.



### 5.3 Lawful Basis



The [Data (Use and Access) Act 2025](https://assets.publishing.service.gov.uk/media/69aea29d917847c0a4c8999e/E03551200_Fraud_Strategy_2026__English__ELAY.pdf) establishes crime and fraud prevention as a lawful basis for data sharing, as referenced in the UK Government's Fraud Strategy 2026-2029. Under AMLR Article 75, cross-institutional information sharing for AML purposes is mandated.



### 5.4 Cryptographic Erasure



The right to erasure under GDPR Article 17 is implemented through cryptographic key deletion. Entity records are encrypted with hierarchical per-entity keys. Deleting the key renders the record unrecoverable. Erasure produces signed destruction receipts.



### 5.5 Purpose Limitation and Minimisation



Escalation signals do not reveal the underlying reason for the escalation. A bank receiving a cross-sector signal learns "elevated risk from telecommunications" but not what specific activity caused it. The intersection privacy controls (Section 4.6) further limit processing to what is necessary and proportionate.



### 5.6 No Mass Surveillance



The PSI operates on risk-filtered entity sets, not full customer bases. Only entities that exceed a local risk threshold enter the PSI. There is no central database. Each institution retains full sovereignty over its own data. The federation is a protocol, not a platform.



## 6. The Telco Value Proposition



### 6.1 Regulatory Compliance



The trajectory is clear. Singapore has implemented shared liability. The UK [Fraud Sector Charter](https://www.gov.uk/government/publications/fraud-sector-charter-telecommunications/fraud-sector-charter-telecommunications-accessible-version) commits telcos to cross-industry intelligence sharing. [Australia's Scam Prevention Framework](https://www.gasa.org/post/singapore-s-shared-responsibility-framework-a-global-model-for-combating-phishing-scams) imposes penalties up to AUD 50 million for non-compliance. The direction is global and irreversible.



### 6.2 The Reputation and Liability Tension



There is an honest tension. Joining a federation implies that an institution's network is used by criminals. Under shared liability frameworks, not participating is more damaging than participating. A telco that could have flagged risk but did not faces financial liability and regulatory enforcement. The risk of inaction exceeds the risk of admission.



The federation protocol shares an escalation signal, not an admission. The bank cannot determine what specific activity caused the elevation. The telco is demonstrating vigilance, not confessing failure.



Without a strict legal mandate in every jurisdiction, Data Protection Officers will debate the lawful basis. The Data (Use and Access) Act 2025 and AMLR Article 75 provide the foundation. Early adopters shape the interpretation.



### 6.3 Revenue Protection



According to the [CFCA's 2023 Global Fraud Loss Survey](https://cfca.org/telecommunications-fraud-increased-12-in-2023-equating-to-an-estimated-38-95-billion-lost-to-fraud/), telecommunications fraud losses reached USD 38.95 billion globally in 2023, representing 2.5 per cent of industry revenues.



### 6.4 No Additional Data Exposure



The telco shares escalation signals, not CDRs. The F1 Edge Installation runs inside the telco's data centre, on the telco's hardware, under the telco's operational control.



## 7. The Crypto Exchange Value Proposition



### 7.1 MiCA Compliance



MiCA requires CASPs to implement transaction monitoring equivalent to traditional financial institutions. Most exchanges check wallet blacklists. They cannot detect novel laundering patterns or the intersection of on-chain and off-chain activity.



### 7.2 The Private Chain Transition



As institutional adoption moves settlement onto permissioned blockchains, public transparency diminishes. Exchanges that correlate risk signals across both public and private chains have a structural advantage.



### 7.3 Travel Rule Compliance



The FATF Travel Rule requires originator and beneficiary information to be transmitted with virtual asset transfers. The federation protocol can facilitate compliance by confirming entity identity matches without revealing underlying data.



## 8. The Market Gap



No company in the world offers a cross-sector federated detection platform.



Telecommunications fraud vendors (Subex, SEON, Vonage) protect telcos from fraud on their own networks. They do not share detection signals with banks.



Banking AML vendors (NICE Actimize, Feedzai, Tookitaki, Oracle Financial Crime) monitor transactions within a single bank. Some offer consortium models but none include telecommunications or blockchain data.



Blockchain analytics firms (Chainalysis, Elliptic, Merkle Science) analyse public chain data. Their model depends on public blockchain transparency, which will diminish.








In the Netherlands, Transactie Monitoring Nederland (TMNL) pioneered joint transaction monitoring across five banks. TMNL operated on a centralised model: banks sent pseudonymised data to a shared utility. The initiative faced sustained scrutiny from the Autoriteit Persoonsgegevens over proportionality. ZQUAS addresses a different architecture and a different scope. The architecture is peer-to-peer: no central database. The scope extends beyond banking to telecommunications and digital assets. The distinction is structural.



ZQUAS is the only platform architected to process banking, telecommunications, and blockchain data in a single GPU-native detection pipeline, connected by a privacy-preserving federation protocol across all three sectors. The banking pipeline is production-ready. The federation protocol is production-ready. The cross-sector extensions are engineering milestones on an operational foundation.



## 9. Honest Limitations



### 9.1 Federation Speed vs. Instant Payments



Local detection operates in under 10 milliseconds. Federation enrichment operates in under 10 seconds per bilateral round. The architecture pre-enriches entity risk profiles between transactions. There is a window (seconds to minutes) where a newly identified signal has not yet propagated, versus hours or days in batch processing.



### 9.2 Adoption Requires Multi-Party Agreement



The network effect requires a minimum viable consortium. Initial deployment targets regulated groups rather than individual institutions.



### 9.3 Jurisdiction-Specific Legal Work



The lawful basis is established in principle but operational boundaries are still being defined. Each jurisdiction requires specific legal analysis and DPO engagement.



### 9.4 Cross-Sector Calibration is New



No cross-sector detection calibration methodology exists today. The simulation-based approach requires validation against real operational data through pilot deployments.



### 9.5 Multi-Hop Signal Attenuation



Bilateral federation propagates signals one hop. Criminal networks spanning three or more institutions require hub-spoke topology (designed but not deployed) or transitive trust agreements.



### 9.6 ID Fragmentation



In jurisdictions without a universal identifier, customers may present different documents to different institutions. Multi-ID hashing mitigates this but does not eliminate false negatives.



## 10. Timeline








**Phase 1 (Current):** Banking federation. Pilot validation. Production-ready.



**Phase 2 (Q3 2026):** Telecommunications integration. CDR/TMDR ingestion. Cross-sector PSI on phone number and government ID. Quantitative risk deltas, differential privacy, signal velocity circuit breaker, full normalisation pipeline, cross-sector calibration.



**Phase 3 (Q4 2026):** Digital asset integration. Blockchain event ingestion. Wallet-to-identity linking via exchange KYC.



**Phase 4 (2027):** Regulatory interface. AMLA Article 75 reporting. Hub-spoke topology.



## 11. Conclusion



The financial crime industry has spent twenty years optimising detection within institutional silos. The criminals have spent twenty years exploiting the gaps between those silos. The gaps are now wider than ever: spanning banking, telecommunications, cryptocurrency, and private institutional blockchains.



The regulatory response is converging. Singapore has implemented cross-sector liability. The UK is building the framework. The EU mandates cross-institutional sharing under AMLR. MiCA brings crypto exchanges into the regulated perimeter.



The technology to match this regulatory direction did not exist. A detection engine that operates across banking, telecommunications, and blockchain data, connected by a federation protocol that shares escalation signals without sharing raw data, running at the speed required for real-time intervention, governed by the institutions that use it rather than a central authority.



We do not need to unmask the fraudster to protect the victim. By correlating the targeting signal at the telco with the transfer signal at the bank, we break the fraud lifecycle before the first payment settles.



The banking detection engine is built. The federation protocol is built. The simulation environment is built. The cross-sector extensions are engineering milestones on an operational foundation.



It exists now.



*ZQUAS. The criminals have cross-sector visibility. Now the compliance infrastructure does too.*



**Contact:** Danny de Gier | danny@zquas.ai | zquas.ai



*© June 2026 ZQUAS. All rights reserved. Implementation details and protocol specifications are proprietary.*

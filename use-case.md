# How Cross-Institutional Detection Works | ZQUAS

> Complete end-to-end operational flow for cross-institutional transaction monitoring using privacy-preserving multi-party computation. From transaction to SAR.

Source: https://zquas.ai/use-case.html
Site: https://zquas.ai

---
Use Case


# How Cross-Institutional Detection Works



From transaction to SAR. The complete operational flow.



            Banks already monitor transactions. Criminals exploit the gaps between banks. ZQUAS adds a privacy-preserving federation layer that makes cross-institutional patterns visible without sharing any data. Each bank keeps its existing systems and processes. The federation layer adds one new capability: the ability to detect patterns that span institutional boundaries.





        The Problem


## What single-bank monitoring misses




A criminal entity (say, a trading company) has accounts at three banks. At each bank, the transaction pattern looks normal. Across all three, the pattern is classic money laundering: money enters through one bank, fragments through a second, and reconsolidates through a third.



No single bank can see this. Each bank's monitoring system scores the entity as low-risk because the local transactions are individually unremarkable.











TMNL proved that cross-institutional analysis detects patterns that single-bank monitoring misses. The project was shut down because centralising the data violated privacy law. [Read the full analysis.](tmnl.html)





        Architecture


## Federation without centralisation




Each participating bank installs ZQUAS on their own infrastructure. The installation sits alongside the bank's existing transaction monitoring system: NICE Actimize, Oracle, SAS, or any other. It reads risk scores that the existing system already produces. No replacement. No migration.










                PEER-TO-PEER


### No central system



Peer-to-peer federation. No central database, no central operator, no single point of failure or breach.



                SOVEREIGN


### No data leaves any bank



Only cryptographic protocol messages cross the private connection. Transaction data, risk scores, and entity information stay on-premise.



                NON-INVASIVE


### Existing monitoring continues



The ZQUAS installation reads risk scores and produces alerts. The bank's existing TM system and case management workflow are unchanged.






        Operational Flow


## From transaction to SAR in six steps




                    STEP 1 / EXISTING PROCESS


### Local Monitoring



Banks monitor transactions using their existing systems. Each bank's system produces risk scores per entity based on local transaction patterns. Banks already do this. Nothing changes.






                    STEP 2 / NEW: THE ZQUAS LAYER


### Federation Round



On a scheduled basis (nightly, or more frequently), the ZQUAS installations execute bilateral federation rounds. For three banks, this means three rounds: A↔B, A↔C, B↔C.



Each round has three phases:



**a) Private Set Intersection:** discovers which entities have accounts at both banks. Neither bank learns which entities the other bank has. Only the overlap is revealed.



**b) Secure Risk Comparison:** for each shared entity, securely compares the combined risk score against a threshold using standard, peer-reviewed cryptographic techniques. Neither bank learns the other's individual score. The only output is a boolean: combined risk exceeds threshold, or it doesn't.



**c) Cryptographic Attestation:** both banks cryptographically sign the result. This creates an unforgeable proof that the computation happened correctly.






                    STEP 3 / NEW: DELIVERED TO EXISTING SYSTEMS


### Escalation Alert



If an entity's combined risk exceeds the threshold in any bilateral round, both participating banks receive an escalation alert.



**The alert contains:**




- Entity identifier (the bank already knows this customer)

- Escalation flag: combined cross-institutional risk threshold exceeded

- Number of bilateral rounds that triggered escalation

- Cryptographic attestation (verifiable proof)




**The alert does NOT contain:**




- The other bank's risk score

- The other bank's transaction data

- Which specific bank triggered the escalation (configurable)




The alert is delivered to the bank's existing case management system via API or file import. No new investigation interface needed.






                    STEP 4 / EXISTING PROCESS


### Enhanced Due Diligence



The bank's compliance analyst receives the alert in their normal workflow. They open the entity's dossier and review their own transactions, the same data they already have access to. The difference: they now know this entity has elevated cross-institutional risk.



Transactions that looked normal in isolation are now suspicious in the cross-institutional context. The analyst applies Enhanced Due Diligence using the bank's existing procedures.






                    STEP 5 / EXISTING PROCESS


### SAR Decision



Each bank independently decides whether to file a Suspicious Activity Report with FIU-Nederland. The bank uses only its own transaction data in the SAR. The cross-institutional escalation is the trigger, not the content.



The SAR references the cross-institutional detection: *"This entity was identified through privacy-preserving cross-institutional analysis. The combined risk score at multiple institutions exceeded the monitoring threshold. Cryptographic attestation of the analysis is available."*



Each participating bank files their own SAR independently. Not a joint SAR. Each bank reports on its own customer relationship.






                    STEP 6 / EXISTING PROCESS


### FIU Investigation



FIU-Nederland receives separate SARs from multiple banks about the same entity. The FIU can now see the complete picture: money entered through Bank A, fragmented through Bank B, and reconsolidated through Bank C. This is the pattern that no single bank could see but that TMNL was designed to reveal.



The FIU investigates using its existing powers and processes. Nothing changes except that they receive more, and more accurate, intelligence.







        Privacy by Design


## Who knows what






| 
                        Information | 
                        Bank A | 
                        Bank B | 
                        Bank C | 
                        FIU 
| 
                        **Own transactions** | 
                        Yes | 
                        Yes | 
                        Yes | 
                        Via SAR 
| 
                        **Own risk scores** | 
                        Yes | 
                        Yes | 
                        Yes | 
                        Via SAR 
| 
                        **Other bank's transactions** | 
                        No | 
                        No | 
                        No | 
                        Via combined SARs 
| 
                        **Other bank's risk scores** | 
                        No | 
                        No | 
                        No | 
                        No 
| 
                        **Which entities are shared** | 
                        Yes (from PSI) | 
                        Yes (from PSI) | 
                        Yes (from PSI) | 
                        Via combined SARs 
| 
                        **Combined risk exceeds threshold** | 
                        Yes (boolean) | 
                        Yes (boolean) | 
                        Yes (boolean) | 
                        Inferred from SARs 
| 
                        **Cryptographic attestation** | 
                        Yes | 
                        Yes | 
                        Yes | 
                        Can verify 
The MPC protocol ensures that each bank learns exactly one new fact about a shared entity: whether the combined risk exceeds the agreed threshold. Not the other bank's score. Not their transactions. One bit of information. Enough to trigger investigation, not enough to compromise privacy.





        Deployment


## What each bank needs




### Per Bank




- One server (on-premise or in the bank's own cloud environment)

- ZQUAS software installed

- Connection to existing TM system (API or file-based risk score export)

- Connection to existing case management (API or file-based alert import)

- Network connection to other participating banks (private VPN or dedicated link)




### Network Options



From most to least isolated:





                OPTION 1


### Dedicated Private Network



Physical or logical private network between participating banks. Highest security isolation. Suitable for production deployment.



                OPTION 2


### Point-to-Point VPN



VPN tunnels between bank pairs. Practical for pilot programmes. Each bank controls their own tunnel endpoint.



                OPTION 3


### Private Cloud Peering



AWS PrivateLink, Azure Private Endpoint. Each bank in their own VPC. Traffic never traverses the public internet.







No central server. No central database. No central operator. The only shared infrastructure is the private connection between banks, and even that carries only encrypted protocol messages that are computationally indistinguishable from random data.



### Trust Registry



Each bank's ZQUAS installation is configured with the public keys of all participating banks. An industry body (such as NVB in the Netherlands) can manage the registry, or banks can configure it bilaterally. The trust registry contains only public keys and connection addresses. No transaction data, no risk scores, no entity information.



### Entity Identification



Participating banks agree on a common entity identifier. For Dutch entities, the KvK (Chamber of Commerce) number is the natural choice. For international entities, the LEI (Legal Entity Identifier). The protocol hashes these identifiers before comparison. The raw identifiers never cross the connection.





        Validation


## Tested with three simulated Dutch banks






| 
                        Metric | 
                        Result 
| 
                        **Banks** | 
                        3 (5,000 + 5,000 + 2,000 accounts) 
| 
                        **Total entities** | 
                        12,017 
| 
                        **Shared entities** | 
                        6 (4 criminal, 2 legitimate) 
| 
                        **Criminal entities detected** | 
                        4/4 (100%) 
| 
                        **Legitimate entities cleared** | 
                        2/2 (0% false positives) 
| 
                        **Total federation time** | 
                        ~2.4 seconds 
| 
                        **Data shared between banks** | 
                        Zero bytes of raw transaction data 
| 
                        **Cryptographic attestation** | 
                        Ed25519 dual-signature per round 
| 
                        **Privacy protocol** | 
                        ECDH-PSI + Garbled Circuits + Oblivious Transfer 
The test reproduced four real-world money laundering typologies: trade-based money laundering (TBML), wire stripping, shell company layering, and funnel account structuring. All four were detected. Both legitimate businesses were correctly cleared.



Independently audited. The test suite, protocol execution, privacy guarantees, and cryptographic attestation have been verified through multiple layers of independent review.





        Regulatory Framework


## Built for the regulatory framework





### AMLR Article 75



Effective July 2027. Cross-institutional information sharing framework: delivered. Privacy-preserving federation enables detection without data centralisation.





### GDPR Article 6



No personal data shared between institutions. By cryptographic construction. Privacy compliance is a mathematical property, not a policy promise.





### DORA Article 9



Cryptographic attestation of all compliance decisions. Ed25519 signed proof bundles for every federation round. Digital operational resilience by design.





### EU AI Act



Deterministic, auditable policy evaluation. GPU-native processing with cryptographic proof bundles. Full traceability of every automated decision.





### Wwft



Dutch AML law. Enhanced due diligence triggers via cross-institutional escalation alerts. Integrates with existing reporting obligations to FIU-Nederland.







Every compliance decision is cryptographically attested. Every federation round produces verifiable proofs. Regulators can independently verify the correctness of the protocol using standard cryptographic tools.





        Pilot Programme


## 20-week pilot. From proof to production.




                    PHASE 0 / 4 WEEKS


### Preparation



Bank selection, scope agreement, legal framework. Define entity identifiers, risk score format, and escalation alert schema. Establish network connectivity between pilot participants.





                    PHASE 1 / 4 WEEKS


### Sandbox



Synthetic data, verify protocol on real infrastructure. Confirm federation rounds execute correctly, privacy guarantees hold, and escalation alerts integrate with existing case management.





                    PHASE 2 / 8 WEEKS


### Controlled Pilot



Historical data, measure against known outcomes. Run federation rounds on real (anonymised) risk scores. Compare detection against known cases to validate detection lift and false positive rate.





                    PHASE 3 / 4 WEEKS


### Evaluation



Results analysis, DNB review, expansion decision. Produce regulatory evidence package. Determine go/no-go for production deployment and network expansion.








ZQUAS has been accepted into the FCA Digital Sandbox. The DNB InnovationHub submission is under review. The technology has been tested. The pilot design is ready. AMLR Article 75 applies on July 10, 2027. The window for pilot initiation is now.





        FAQ


## Frequently asked questions




### Do we need to replace our existing transaction monitoring system?



No. ZQUAS sits alongside your existing system. It reads risk scores your system already produces. Your monitoring continues unchanged.



### What data leaves our bank?



Zero transaction data. The only data that crosses the network are cryptographic protocol messages: elliptic curve points, garbled circuit tables, and encrypted values. These are computationally indistinguishable from random data.



### Who operates the central system?



There is no central system. Each bank runs its own ZQUAS installation on its own infrastructure. The installations communicate peer-to-peer over a private connection.



### How often do federation rounds run?



Configurable. Nightly batches align with existing monitoring cycles. More frequent rounds (hourly, real-time) are technically possible.



### What if a bank joins or leaves the network?



Adding a bank: install ZQUAS, register public keys with existing participants, begin federation rounds. Removing a bank: decommission the installation, remove public keys. No impact on remaining participants.



### Can criminals detect they are being monitored cross-institutionally?



No. The federation runs between bank installations on private connections. No information about the federation reaches the customer or their transactions. From the customer's perspective, nothing changes.



### What about false positives?



The federation layer inherits the risk scores from each bank's existing system. If the local scores are well-calibrated, the combined scores will be too. In our three-bank test, zero legitimate businesses were incorrectly flagged.



### Is this what TMNL was trying to do?



TMNL proved that cross-institutional detection catches criminals that single-bank monitoring misses. The project was shut down because centralising the data violated privacy law. ZQUAS achieves the same detection without centralisation, using cryptographic multi-party computation instead of data pooling. [Read the full TMNL analysis.](tmnl.html)





        Contact


## Discuss a pilot



            If your institution is exploring cross-institutional AML detection, or if you're a regulator evaluating privacy-preserving approaches, I'd like to hear from you.



            [danny@zquas.ai](mailto:danny@zquas.ai?subject=Cross-Institutional%20Detection%20/%20Pilot%20Inquiry)
            [LinkedIn](https://www.linkedin.com/in/danny-de-gier-prof-pgdip-fcc/)

        Zwolle, Netherlands




            **Three Founding Partner slots available**


12 weeks from signature to results. Joint regulatory sandbox engagement included. No customer data leaves your infrastructure.



            [View Programme](founding-partner.html)
            [Position Paper](article-75.html)

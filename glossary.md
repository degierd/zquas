# Glossary

> Definitions for the cryptographic, regulatory, and architectural terms used across the ZQUAS platform. Cross-institutional AML, MPC, AMLR Article 75, ECDH-PSI, Garbled Circuits, and more.

Source: https://zquas.ai/glossary.html
Site: https://zquas.ai

---
# Glossary



Definitions for the cryptographic, regulatory, and architectural terms used across the ZQUAS platform. Each entry stands alone. Each is short enough to quote.



            [Regulatory](#regulatory)
            [Cryptography](#cryptography)
            [Architecture](#architecture)
            [Performance](#performance)
            [Governance](#governance)


        Regulatory




### AMLR Article 75



Article 75 of the EU Anti-Money Laundering Regulation. Permits cross-institutional information sharing for AML purposes, with mandatory pseudonymisation as a technical safeguard.



Applies from July 10, 2027. Cross-institutional monitoring infrastructure typically takes 18 to 24 months to build, which puts the practical decision window in 2026.





### ECCTA Sections 188-189



Sections 188 and 189 of the UK Economic Crime and Corporate Transparency Act 2023. Provide an explicit legal basis for inter-bank AML information sharing in the UK.



In force since January 2024. UK banks already have the legal basis that EU banks gain only in July 2027.





### TMNL (Transaction Monitoring Netherlands)



A joint initiative launched in 2019 by five Dutch banks to pool transaction data for cross-institutional monitoring.



Wound down because its architecture, which centralised transaction data into a joint pool, could not be reconciled with EU privacy law. The detection concept was sound. The architecture was wrong.





### EU AI Act, Article 12



The record-keeping requirement for high-risk AI systems. Mandates automatic logging of events sufficient to ensure traceability of the system's functioning across its lifecycle.



Most AML transaction monitoring is excluded from the high-risk classification, but AI-based customer risk profiling can fall within scope through the profiling exception.





### Wwft



Wet ter voorkoming van witwassen en financieren van terrorisme. The Dutch national AML law that implements EU directives. Sets out customer due diligence, transaction monitoring, and SAR filing obligations for Dutch financial institutions.





### SAR (Suspicious Activity Report)



A formal filing by a regulated institution to its national Financial Intelligence Unit (FIU) describing a transaction or pattern suspected of being linked to money laundering or terrorist financing. In ZQUAS, AI agents cannot file a SAR autonomously. Human MLRO sign-off is required by the engine's governance rules.




        Cryptography




### Multi-Party Computation (MPC)



A family of cryptographic protocols that allow several parties to jointly compute a function over their combined inputs while keeping each input private from the others.



In AML, MPC enables banks to compare risk scores or detect shared customers without sharing the underlying data. The privacy property is mathematical, not contractual.





### Private Set Intersection (PSI)



An MPC primitive that lets two parties identify the entities they have in common without either party revealing its full set to the other.



For two banks, PSI answers the question "which of our customers also bank with you?" without disclosing any customer who is not also at the counterparty.





### ECDH-PSI



A Private Set Intersection construction built on Elliptic Curve Diffie-Hellman key agreement. ZQUAS uses ECDH-PSI over Curve25519 (X25519) for cross-institutional entity matching.



Each party hashes its identifiers to a curve point, applies its private key, exchanges results, and applies its key again. Matching points indicate shared entities. Non-matching points reveal nothing.





### Yao's Garbled Circuits



An MPC technique that lets two parties evaluate a Boolean circuit on their joint inputs while learning only the circuit's output.



ZQUAS uses Yao's Garbled Circuits with the Free-XOR optimisation for risk score comparison. The garbler encrypts the circuit. The evaluator runs it without ever seeing the cleartext gates or wires.





### Oblivious Transfer (OT) and OT Extension



A cryptographic primitive in which a sender transfers one of several messages to a receiver without learning which message was selected, and the receiver learns only the chosen message.



OT Extension protocols (such as IKNP) amplify a small number of base OTs into millions of OTs at low cost. ZQUAS uses IKNP OT Extension built on Chou-Orlandi base OT over P-256.





### Ed25519



An elliptic curve signature scheme defined in RFC 8032. Used in ZQUAS for proof bundle signatures, federation round attestations, and binary integrity checks. Verification requires only a public key.





### BLAKE3



A high-performance cryptographic hash function used in ZQUAS for policy hashing, input hashing, and Merkle tree construction. Tested against the official BLAKE3 vectors.





### Zero-Knowledge Governance Proofs



Cryptographic proofs that a computation was performed correctly without revealing the inputs or intermediate state.



ZQUAS uses GPU-accelerated PLONK to optionally include zero-knowledge governance proofs in proof bundles. Useful when the policy logic itself is sensitive but the supervisor still needs to verify correct execution.




        Architecture




### GPU-native compliance engine



A compliance engine designed from the ground up to execute on GPU. Distinct from a GPU-accelerated engine, where a CPU pipeline offloads selected operations to a GPU.



In a GPU-native engine, data structures, control flow, scheduling, and memory layout are all GPU-resident. The performance difference is typically several orders of magnitude.





### Cross-Institutional AML Detection



Detecting financial crime patterns that span multiple banks by comparing risk indicators across institutions, without any institution exposing its raw customer data.



Required to catch criminal networks that deliberately split activity across multiple banks to stay below per-bank detection thresholds.





### Federated Detection



Detection that runs across multiple institutions without those institutions sharing raw data. Achieved in ZQUAS via cryptographic federation rather than data centralisation.



The opposite of TMNL's centralisation approach. Each institution retains absolute data sovereignty.





### Sovereign Compliance



A deployment model in which a regulated institution retains absolute control of its compliance data and infrastructure. The vendor cannot read, copy, or relocate the institution's data.



ZQUAS deploys on the bank's own infrastructure. Cross-institutional detection is layered on top via MPC, not via a third-party data hub.





### Cryptographic Proof Bundle



A signed, Merkle-included artefact produced for every compliance decision. Contains a hash of the policy set in effect, a hash of the input data, individual verdict hashes, a Merkle root binding all verdicts together, and an Ed25519 signature.



912 bytes per evaluation. Verifiable by a supervisor with a public key alone.





### Deterministic Evaluation



Property of an evaluation engine such that the same inputs and the same policy version always produce the same output, byte for byte, on any compliant deployment.



Without this property, a regulator cannot replay a decision. Determinism is the foundation of cryptographic attestation.





### Bilateral Round



One end-to-end execution of the cross-institutional MPC protocol between two participating institutions.



ZQUAS publishes a benchmark of under 10 seconds for 100,000 entities (measured: 7.8 seconds). Both parties sign the result with Ed25519.





### Policy Language



A domain-specific language for compliance rules. Has its own lexer, parser, semantic analyser, and compiler. Policies compile to bytecode evaluated on GPU.



Each policy version produces a new compilation with a different cryptographic hash, so the exact rule set in effect at any moment is unambiguously identifiable.




        Performance




### CEPS (Compliance Policy Evaluations per Second)



Throughput metric for compliance engines. One CEPS is one entity evaluated against one policy.



The ZQUAS engine sustains 150 million plus CEPS on a single NVIDIA RTX 5090.





### Alert Lifecycle



The wall-clock time from a transaction arriving at the engine to a triaged alert being available to a compliance officer.



ZQUAS publishes a benchmark of under 10ms (measured: 3.92ms). Three orders of magnitude below typical real-time payment settlement windows.





### Real-Time Monitoring



The term has three distinct meanings: (1) intra-day batch, where alerts arrive minutes to hours after a transaction; (2) streaming, where alerts arrive seconds after a transaction; (3) inline, where the alert is generated before the transaction settles.



ZQUAS operates in the inline regime: the alert lifecycle is shorter than the payment settlement window.




        Governance




### Constitutional Governance



An architectural pattern in which AI agents operate under hard-coded rules they cannot modify.



In ZQUAS, agents cannot file a Suspicious Activity Report autonomously. Human MLRO sign-off is required by the engine's governance layer, not by policy or by training.





### Adversarial Self-Testing



A testing discipline in which the system continuously generates adversarial inputs designed to break its own detection logic and tracks how often the resulting flaws are caught.



ZQUAS runs a continuous mutation testing framework against the policy evaluator and the cryptographic primitives.





### Build Attestation



Embedded BLAKE3 plus SHA-256 plus Ed25519 binary integrity verification. Lets a supervisor verify that the binary running on a bank's hardware is the binary the vendor claims to have shipped.





### Predictive Governance



Forward simulation of compliance state. The engine can project the consequences of a policy change before the policy is deployed, so MLROs can compare expected alert volume and false-positive rates against the current baseline.

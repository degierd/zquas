# Technology

> Technical overview of the ZQUAS engine architecture: GPU adjudication, policy compiler, identity graph, cryptographic attestation, and privacy-preserving MPC.

Source: https://zquas.ai/technology.html
Site: https://zquas.ai

---
Technology


# How ZQUAS works



        A technical overview of the engine architecture for CTOs, technical evaluators, and due diligence teams. No source code, no internal codenames. Enough depth to understand what's real and what's different.



        Architecture


## Five layers, one engine



            ZQUAS is a vertically integrated compliance engine. Each layer is purpose-built, not assembled from third-party components. The engine runs on a single GPU installation per institution.






                LAYER 1


### Policy Language & Compiler



Compliance policies are written in a domain-specific language designed for regulatory rules. The language has its own lexer, parser, semantic analyser, and compiler. Policies compile to bytecode that can be evaluated on GPU. The bytecode is immutable once deployed. A new policy version produces a new compilation with a different cryptographic hash. This means the exact policy set in effect at any moment is unambiguously identifiable.





                LAYER 2


### GPU Adjudication Engine



The compiled policy bytecode executes on GPU. Each entity is evaluated against the full policy set in parallel. The engine processes 500,000 entities across 100 AML policies in under 2 seconds, sustaining 150 million+ compliance policy evaluations per second. Alert lifecycle under 10ms. Results are deterministic: same policy version, same input data, same verdict.





                LAYER 3


### Identity Resolution & Graph Intelligence



A GPU-resident entity graph maintains relationships between accounts, individuals, businesses, devices, and counterparties. The graph uses a high-throughput GPU-resident hash table for real-time updates without read contention. Graph neural network inference propagates risk scores across entity relationships, providing full network context for every compliance decision. Entity resolution runs at GPU speed, not in overnight batch.





                LAYER 4


### Cryptographic Attestation



Every batch of compliance decisions produces a sealed proof bundle. The bundle includes: a BLAKE3 hash of the policy set, a hash of the input data, individual verdict hashes, a Merkle root binding all verdicts together, and an Ed25519 signature over the complete bundle. A separate SHA-256 witness hash is produced for regulatory interfaces. Proof bundles can optionally include GPU-accelerated zero-knowledge governance proofs.





                LAYER 5


### Privacy-Preserving Cross-Institutional Layer



When multiple institutions run ZQUAS, cross-bank detection activates via privacy-preserving federation. The protocol combines ECDH-PSI (X25519) for entity matching, Yao's Garbled Circuits (Free-XOR) for risk comparison, and IKNP OT Extension (Chou-Orlandi base OT on P-256) for oblivious transfer. Security model: semi-honest. Transport: AES-256-GCM with X25519 key exchange. Each institution retains full data sovereignty. No raw entity data crosses institutional boundaries. At 100,000 entities, a bilateral round completes in approximately 15 seconds. Both parties sign the result with Ed25519. A regulator verifies the attestation with a public key alone. 361 tests, zero critical findings.






        Data Flow


## From transaction to verified verdict



            The engine uses a triple-stream GPU pipeline for compliance adjudication.






                STREAM A


#### Load



Transaction data serialised to GPU-native evaluation contexts. Asynchronous host-to-device copy via zero-copy memory transfers.



                STREAM B


#### Adjudicate



GPU kernel evaluates N transactions against M policies in parallel. One block per transaction, one thread per policy. Verdict per transaction.



                STREAM C


#### Commit



Results copied device-to-host. Epoch commitment computed. Merkle root constructed. Ed25519 signature applied. Proof bundle sealed.





Inter-stream synchronisation uses CUDA events. Streams execute concurrently. Load, adjudicate, and commit operate on different batches simultaneously, maximising throughput.




        Regulator Verification


## Independent verification without vendor software



            The engine ships with a standalone verification CLI. The tool is independent of the ZQUAS engine. It takes a proof bundle, a registered policy set, and evaluation contexts as input. It replays the evaluation deterministically and confirms that the proof is valid. The tool outputs VALID (exit code 0), INVALID (exit code 1), or ERROR (exit code 2). No GPU required for verification. No vendor infrastructure needed.




```
$ themis-verify --epoch epoch_2026-03-08.bundle --policies /registered/v4.2/ --contexts eval_contexts.bin

Replaying epoch 2026-03-08_14:32:00Z...
Policies:       29 loaded (hash: a3f7c2...)
Contexts:       1,247 evaluated
Verdicts:       1,247 matched
Merkle root:    OK
Ed25519 sig:    OK

Result: VALID (deterministic replay confirmed)
```





        Engineering


## How it's built



Standards and toolchain.





#### Language



C++23 with CUDA. Self-contained CUDA compilation per kernel. No separable compilation dependencies.





#### GPU Targets



NVIDIA architectures: sm_86 (Ampere), sm_89 (Ada Lovelace), sm_100 (Blackwell), sm_120 (next-gen). Tested on RTX 5090.





#### Build Hardening



MSVC /sdl, /guard:cf, /GS, /Qspectre, /fp:strict. Linker: /CETCOMPAT, /DYNAMICBASE, /NXCOMPAT, /HIGHENTROPYVA.





#### Testing



12,342 automated tests across the codebase. 7,218 core engine tests across 12 independently audited subsystems (GTest). 1,845 Playwright browser tests. 1,185 AI agent tests. 826 case management tests. 592 end-to-end pipeline tests. 449 detection pipeline tests. CPL engine: 288 tests. Federation: 361 tests. Crypto KAT tests: Ed25519 (RFC 8032), SHA-256 (FIPS 180-4), Blake3 (official vectors).





#### Cryptography



BLAKE3 (internal), SHA-256 (regulatory), Ed25519 (signatures), ZK-optimised hash functions (ZK circuits). DualHash at domain boundaries.





#### Binary Attestation



Reproducible builds with embedded BLAKE3 + SHA-256 hashes, compiler version, git commit, and Ed25519 signature for runtime self-verification.






        Governance Architecture


## Nothing executes without constitutional authorization



            The engine enforces a zero-bypass governance model. Every computational action requires explicit authorization, every authorization is metered, and every action is cryptographically provable. This is not a logging layer added on top. It's the execution model itself.




                ENFORCEMENT


### policy execution gateway



The single enforcement point through which every governed action must pass. There is no code path that bypasses the gate. If an action lacks a valid warrant, it does not execute. This is enforced architecturally, not by convention.



                AUTHORIZATION


### authorisation framework



Ephemeral Ed25519 keypairs mint cryptographic warrants for authorized actions. Each warrant is scoped to a specific action, agent, and time window. Warrants cannot be reused, extended, or forged. The authority rotates keys to prevent accumulation of stale credentials.



                METERING


### resource governor



Every agent has a monotonic gas ledger. Each action consumes gas. When gas is depleted, the agent cannot act until replenished by an authorized governance decision. This prevents runaway processes, resource exhaustion, and any single agent consuming unbounded compute. Sharded concurrency ensures metering does not become a bottleneck.



                INCLUSION PROOF


### policy hierarchy



A GPU-resident Sparse Merkle Tree maintains policy inclusion proofs. Any party can verify that a specific policy was part of the active policy set at a specific time without accessing the full policy database. This enables selective disclosure during regulatory review.






        Predictive Layer


## Detect problems before they happen



            The predictive compliance engine simulates governance state forward in time without executing policies. It predicts gas depletion, resource violations, cascade failures, and warrant expiry over N future frames. Compliance issues are flagged before they materialise, not after.



            PROJECTION


### Pre-Cognition Engine



The predictive compliance engine uses a discrete-time state machine with fixed-point arithmetic for deterministic projection. It operates on copy-on-write shadow states, meaning projections don't interfere with live governance. The projection scheduler integrates with the decision kernel, feeding predictions directly into policy evaluation. The practical result: the system warns that an agent will exhaust its gas budget in 12 evaluation cycles, or that a warrant will expire before a pending operation completes, or that a policy change will create a coverage gap in a specific compliance domain. Preemptive compliance, not reactive detection.





        Continuous Verification


## The engine attacks itself



            The adversarial testing framework has 13+ subsystems. It continuously generates adversarial inputs, fuzzes policy evaluation boundaries, and maps decision surface coverage. This runs on GPU alongside production workloads.




                FUZZING


### GPU-Accelerated Fuzzing



Adversarial input generation running on dedicated CUDA streams. The fuzzer targets policy evaluation edge cases, threshold boundaries, and entity resolution logic. It finds the inputs that break your rules before criminals do.



                CARTOGRAPHY


### Decision Surface Mapping



GPU-accelerated cartography subsystem maps the complete decision surface of the policy set. It identifies regions of the input space where small changes in transaction parameters flip verdicts. These boundary regions are where evasion attempts concentrate.



                VERIFICATION


### Two-Gate Pipeline



A 6-step pre-commit gate runs before any policy change is deployed. A parallel CI/CD gate runs comprehensive adversarial testing. Resource arbitration manages GPU streams, Z3 solver instances, and VRAM budgets across all subsystems. No policy change reaches production without surviving adversarial scrutiny.






        Semantic Layer


## Reasoning beyond patterns



                KNOWLEDGE GRAPH


### AI-native semantic runtime



A structured ontology across entity existence, relationships, behaviour, epistemic state, and temporal projections provides structured contextual reasoning for agent decision-making. The graph represents not just what entities exist and how they connect, but how they behave over time, what is known about them with what confidence, and what actions they afford. This context feeds into compliance evaluation, giving the engine understanding beyond raw transaction patterns.



                TEMPORAL ANALYSIS


### Multi-Timeline Virtualization



The engine can evaluate the same entity under different temporal contexts simultaneously. Compare this month's transaction pattern against last month's baseline, project forward under different scenarios, or replay historical periods with current policies. Temporal virtualization runs on GPU with per-context isolation. The practical use: scenario analysis at compliance speed, not in overnight batch reports.






        Integration


## Plugs into what you already run



                SIEM / GRC


### Zero-Copy Export



Verdict export in RAW and CEF formats for direct ingestion by SIEM platforms (Splunk, QRadar, Sentinel) and GRC systems. Messages use zero-copy flat encoding with domain-tagged BLAKE3 integrity hashes. Epoch-level export batches align with the cryptographic attestation cycle, so every exported verdict is traceable to its proof bundle.



                DATA INGESTION


### High-Throughput Ingest



256MB shared memory ring buffer with cache-line separated atomic indices for lock-free ingestion. Supports standard JSON payloads via the native language bridge and raw binary payloads via GPU-Direct bypass for high-frequency environments. Backpressure policies (drop newest, drop oldest, block) are configurable per deployment. The engine ingests at the speed your payment infrastructure produces, not the other way around.






        Binary Integrity


## The engine verifies itself


            SUPPLY CHAIN


### Build Attestation



Every compiled binary embeds deterministic hashes (BLAKE3 and SHA-256) of its own content, the compiler version and flags used to build it, the git commit hash, and an Ed25519 signature over all of the above. At runtime, the engine can verify its own binary integrity. If the binary has been modified, patched, or tampered with, verification fails and the engine refuses to start. This is supply chain security at the binary level, relevant for DORA digital operational resilience requirements and for any institution concerned about software integrity in their compliance infrastructure.





        Scope


            This page describes the architecture at a level appropriate for technical evaluation. Implementation details including the policy language syntax, GPU kernel design, MPC protocol specifics, and internal subsystem architecture are available under NDA for qualified evaluation partners. Contact [danny@zquas.ai](mailto:danny@zquas.ai).

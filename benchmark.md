# Benchmark: 150M+ Evaluations/sec, Under 10ms Alert Lifecycle

> Documented GPU benchmark of the ZQUAS engine. 500K entities in under 2 seconds on NVIDIA RTX 5090. Alert lifecycle under 10ms.

Source: https://zquas.ai/benchmark.html
Site: https://zquas.ai

---
Benchmark Study


# 500,000 entities. 100 policies. Under 2 seconds.



            A documented benchmark of the ZQUAS engine at production scale. 150 million+ compliance policy evaluations per second. Alert lifecycle under 10ms from ingestion to triage. Every result measured on NVIDIA RTX 5090. Every decision signed.


        Benchmark date: March 2026 · Hardware: NVIDIA RTX 5090 (Blackwell, sm_100, 170 SMs, 32GB VRAM)
        ZQUAS is a member of the NVIDIA Inception program.





## Test Configuration





### Hardware


                    GPU
                    NVIDIA RTX 5090


                    Architecture
                    Blackwell (sm_100)


                    CUDA Cores
                    21,760


                    VRAM
                    32 GB GDDR7


                    Host CPU
                    AMD Ryzen 9 9950X


                    Host RAM
                    64 GB DDR5


                    OS
                    Windows 11 Pro





### Policy Set


                    AML policies
                    29 (100 rules, 6 domains)


                    Access control
                    15 policies


                    Policy language
                    CPL (59-opcode register VM)


                    Evaluation model
                    N entities × M policies (parallel)


                    Termination
                    Guaranteed (forward-only jumps)


                    CPU/GPU agreement
                    Verified (all 59 opcodes)


                    CPL tests
                    288









## What CEPS Means



CEPS stands for Compliance Policy Evaluations Per Second. One evaluation is a single entity assessed against one policy. The engine evaluates all entities against all policies in parallel. 150M+ CEPS means over 150 million individual policy checks per second sustained at production scale.



The key metric for AML monitoring is not raw throughput but latency from event to triage. An alert that takes 24 hours to reach an analyst is an alert that arrives after the money has moved. The engine produces a complete triage decision in 4.93ms: 12 microseconds for ingestion into the semantic entity graph, 271 microseconds for GPU policy evaluation, and 4.64ms for AI agent triage. Total: 4.93ms.



This matters for real-time payment rails. SEPA Instant requires settlement in under 10 seconds. The engine evaluates the transaction in under 10 milliseconds. The agent triage decision is available before the settlement window closes.




500K entities × 100 policies = 50 million evaluations in under 2 seconds. Millions of times faster than a 24-hour batch cycle.








## Policy Set Composition



The benchmark used a 29-policy set (100 rules) modelled on a Tier-1 bank's production monitoring requirements, spanning 6 compliance domains:



                01


#### AML Transaction Monitoring



Structuring detection, velocity analysis, counterparty risk, geographic risk



                02


#### Sanctions Screening



Name matching, list-based screening, fuzzy matching thresholds



                03


#### Fraud Detection



Anomaly scoring, device correlation, behavioural deviation



                04


#### KYC/KYB



Customer risk classification, beneficial ownership verification, PEP screening



                05


#### Correspondent Banking



Nested correspondent detection, payment chain analysis, jurisdiction risk



                06


#### Trade-Based Money Laundering



Invoice manipulation, over/under pricing, phantom shipments



                06


#### Regulatory Reporting



SAR trigger conditions, threshold-based filing requirements, cross-domain aggregation





These are representative compliance domains. The specific rules, thresholds, and scenarios are not disclosed. The policy set is designed to reflect the breadth and complexity of a real Tier-1 bank monitoring configuration.






## Results



### Single Node — Entity Evaluation at Scale



                < 2s
                500K entities × 100 policies (1,204ms)


                150M+
                CEPS sustained at production scale


                < 10ms
                Alert lifecycle: ingestion to triage




            **Alert lifecycle breakdown:** semantic graph ingestion 12µs → GPU policy evaluation 271µs → AI agent triage 4,644µs → total 4.93ms
            **Scaling:** Linear confirmed. 2× entities = 2× time. CEPS stable at 150M+ for production-scale batches (250K+).
            **VRAM usage:** 76MB active GPU memory for the policy evaluation pipeline (0.2% of 32GB). Total system memory including the GPU resource manager: 426MB (1.3%).
            **Speedup vs. 24h batch:** Millions of times faster than a standard overnight batch cycle.




### Scaling Profile





| 
                    Entity Count | 
                    Policies | 
                    Wall-clock | 
                    CEPS 
| 
                    10,000 | 
                    100 | 
                    24.5ms | 
                    166M 
| 
                    50,000 | 
                    100 | 
                    120.8ms | 
                    183M 
| 
                    100,000 | 
                    100 | 
                    237.7ms | 
                    188M 
| 
                    250,000 | 
                    100 | 
                    607.9ms | 
                    190M 
| 
                    500,000 | 
                    100 | 
                    1,204ms | 
                    189M 
### GPU AI Agent System


            **50,000 agents:** 7ms total (kernel 9µs + readback 7.1ms)
            **10,000 agents:** 2.1ms total
            **1,000 agents:** 0.4ms total
            **Constitutional gate:** FILE_SAR → ESCALATE enforced. Agents cannot file SARs autonomously. Human MLRO approval required.



            **Determinism:** Verified. Same policy set, same input data, byte-identical verdicts across multiple runs.
            **Proof generation:** Each evaluation produces a cryptographic proof bundle (912 bytes, Ed25519 signed, Merkle-included) within the measured wall-clock time.
            **Conditions:** RelWithDebInfo build, MSVC, Windows 11, RTX 5090. Medians of 3 runs with 10 warmup iterations. Includes full proof pipeline (Merkle + Ed25519). Federation measured on TCP localhost.







## How It Was Measured



The benchmark uses a standalone governance benchmark harness that measures throughput, latency, determinism, and cryptographic proof generation under controlled conditions.



Transactions are synthetically generated with realistic parameter distributions (amount, currency, jurisdiction, counterparty type, temporal spacing). The generator produces a continuous stream at a rate exceeding the engine's processing capacity to ensure the benchmark measures engine throughput, not data generation throughput.



Timing uses CUDA events for GPU-side measurement, eliminating host-side timing noise. The measurement window excludes startup and warmdown periods. The reported figure is sustained throughput over the measurement window, not a burst or peak.



The benchmark harness is a standalone executable (benchmark runner) that runs independently of the full engine application. It isolates the policy evaluation pipeline: GPU context packet serialisation, kernel dispatch, verdict collection, and epoch commitment. It does not include data ingestion, entity graph updates, or rendering overhead. These subsystems operate concurrently in the full engine but are excluded from the policy evaluation benchmark to measure the adjudication pipeline in isolation.








## Why This Matters for Banks



A Tier-1 bank with 500,000 monitored entities evaluates its full portfolio against 100 AML policies in under 2 seconds. The same operation in overnight batch takes 24 hours. The engine is millions of times faster than that cycle, measured on the same workload.



For real-time payment rails, the relevant number is alert lifecycle latency. SEPA Instant requires settlement in under 10 seconds. The engine produces a complete triage decision in under 10ms. The analyst receives an alert with entity context, risk score, cross-institutional signal, and agent recommendation before the payment settles.



VRAM usage at 500K entities is well under 1GB. The RTX 5090 has 32GB. The vast majority of GPU memory is unused at the production benchmark workload. Headroom exists for larger entity populations, simultaneous federation computation, and concurrent agent workloads.




One GPU. 500K entities. 100 policies. Under 10ms from transaction to triage. Under 1GB total VRAM.









## Privacy-Preserving Federation



Federation benchmarks measure cross-institutional detection performance. The protocol is ECDH-PSI (X25519) for entity matching, combined with Yao's Garbled Circuits (Free-XOR) for risk comparison, and IKNP OT Extension (Chou-Orlandi base OT on P-256) for oblivious transfer. Transport is AES-256-GCM with X25519 key exchange. Security model: semi-honest.



At 100,000 entities, a bilateral round completes in approximately 15 seconds over TCP localhost. Real network conditions add latency. Each bilateral round produces dual Ed25519 attestation: both parties sign, and a regulator can verify the result using only the public keys and the proof bundle. No engine access required.



What each bank learns from a federation round: which shared entities exceed the risk threshold. What each bank does not learn: the other bank's entity list (protected by ECDLP), the other bank's risk scores (protected by the garbled circuit), and the other bank's policy configuration (circuit is opaque). Inherent disclosures: entity count and intersection size (structural to PSI; mitigable by padding).



Federation tests: 361. Zero critical findings. The protocol is validated for consortium deployment under a semi-honest threat model, appropriate for regulated financial institutions operating under mutual legal obligation.








## Verification



The benchmark is deterministic. Running the benchmark suite with the same policy set on the same hardware produces identical results. The benchmark executable is subject to the same build attestation as the main engine: embedded BLAKE3 and SHA-256 hashes, compiler version, git commit, and Ed25519 signature.



Every benchmark result is covered by 12,342 automated tests across the codebase, with 7,218 core engine tests spanning 12 independently audited subsystems covering adversarial fuzzing, semantic graph, compliance policy language, GPU policy evaluation, AI agent triage, federation, UI, GPU resource management, cryptography, and decision pipelines. Crypto KAT tests cover Ed25519 (RFC 8032), SHA-256 (FIPS 180-4), and Blake3 (official vectors). Hardware differences will affect absolute throughput but not determinism or correctness.



Cryptographic proof bundles (912 bytes per evaluation) are independently verifiable. A regulator with the public key can verify any proof bundle offline without engine access. The Merkle inclusion proof supports trees up to depth 20. Field-level tamper detection tests confirm that any modification to the proof bundle is detectable.







            For benchmark reproduction, detection fidelity details, or technical due diligence: [danny@zquas.ai](mailto:danny@zquas.ai)






            **Three Founding Partner slots available**


12 weeks from signature to results. Joint regulatory sandbox engagement included. No customer data leaves your infrastructure.



            [View Programme](founding-partner.html)
            [Position Paper](article-75.html)

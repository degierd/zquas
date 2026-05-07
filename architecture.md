# Bounded Compliance on an Unbounded Platform

> The architectural philosophy behind ZQUAS: a deterministic, cryptographically attestable compliance layer running on GPU-native infrastructure. Every decision provable. Every policy bounded.

Source: https://zquas.ai/architecture.html
Site: https://zquas.ai

---
Architecture Philosophy


# 
        Bounded compliance
on an unbounded platform.




        The compliance layer is deliberately constrained. Deterministic execution. Guaranteed termination. Cryptographic proof for every verdict. The platform it runs on is not constrained at all. That separation is the design.






            BOUNDED


## CPL



Compliance Policy Language




- 
                    DET
                    **Deterministic execution.** Same inputs always produce the same output. No randomness, no environment dependencies, no side effects.


- 
                    TERM
                    **Guaranteed termination.** Maximum 10,000 instruction steps per evaluation. The system cannot hang. The system cannot loop indefinitely.


- 
                    REC
                    **No recursion.** Policies cannot call themselves. Call depth is statically bounded at compile time.


- 
                    SBX
                    **Sandboxed reads.** A policy can only read fields it has declared in its input schema. Access to undeclared fields fails at compile time, not runtime.


- 
                    ATT
                    **Cryptographically attestable.** Each evaluation produces a cryptographic proof bundle: the policy hash, the inputs read, the verdict produced, and an Ed25519 signature over all three.




                **29 policies. 9 domains. Every decision provable.**
                AMLR, 6AMLD, FATF R15, EU AI Act, GDPR, DORA





            UNBOUNDED


## ZQUAS Engine



GPU-Native Governance Platform




- 
                    GPU
                    **Full GPU compute.** RTX 5090, 32GB VRAM, 170 streaming multiprocessors. No artificial compute ceiling.


- 
                    FED
                    **Real-time federation.** Privacy-preserving cross-bank detection via MPC: ECDH-PSI, garbled circuits, oblivious transfer (OT extension protocol). No raw data shared.


- 
                    SCL
                    **500,000 entities in 3.4 seconds.** Bilateral AML detection at Tier-1 scale. 30 institutions in a single 36-second federation epoch.


- 
                    MPC
                    **64 concurrent MPC rounds.** Zero VRAM leaks. Zero memory growth across sustained federation runs.


- 
                    TLS
                    **Authenticated encrypted transport.** X25519 key exchange, AES-256-GCM data encryption, Ed25519 peer authentication per session.


- 
                    AGT
                    **Agent cognition.** AI-native adaptive monitoring with cryptographic governance at the agent level. Warrants, gas metering, and cryptographic governance at the agent level.




                **The platform computes anything.**
                C++23 · CUDA · Vulkan · 32GB VRAM






        Why This Matters


## The separation is the product.



Unrestricted compute under restricted policy execution means you get performance without sacrificing provability. Neither property compromises the other.



                FOR REGULATORS


### Verify. Don't trust.



Every compliance decision has a mathematical proof. Not a log file. A cryptographic attestation that the correct policy was applied to the stated inputs. **You can verify any verdict independently**, with a standalone CLI tool, without accessing bank systems or trusting vendor software.



                FOR BANKS


### Real-time. Not overnight.



Compliance policies execute on GPU in parallel, not in sequential overnight batch cycles. Cross-bank money laundering detection that TMNL took 24 hours to attempt takes ZQUAS **36 seconds with zero data shared** across institutions.



                FOR COMPLIANCE OFFICERS


### No black boxes.



Every ESCALATE and DENY verdict carries a policy ID, the rule that fired, and the threshold that was exceeded. The EU AI Act requires explainability. **ZQUAS provides it by construction**, not by retrofit. The policy set is readable, auditable, and Board Risk Committee-approved before it executes.





    System Stack


## Four layers. Two modes.



The top two layers are bounded. The bottom two are not. The boundary between them is the engine's core design principle.




                CPL Policy Layer

                    29 policies · 9 domains · deterministic · cryptographically attestable

                    Max 10,000 steps per evaluation · no recursion · sandboxed field access


            BOUNDED



                GPU policy evaluation kernel

                    Executes CPL bytecode on GPU · one block per transaction, one thread per policy

                    Same determinism bounds as CPL · massively parallel evaluation


            BOUNDED



                Federation Layer

                    ECDH-PSI · garbled circuits · oblivious transfer · OT extension protocol

                    Cross-bank MPC · X25519 + AES-256-GCM + Ed25519 · 64 concurrent rounds


            UNBOUNDED



                ZQUAS Engine

                    C++23 · CUDA · Vulkan · 32GB VRAM · sm_86 through sm_120

                    Agent cognition · real-time streaming · GPU-resident entity graph


            UNBOUNDED






> 
            "The compliance layer computes only what it is allowed to compute. The platform underneath it can compute anything. That is not a compromise. That is the architecture."


        ZQUAS DESIGN RATIONALE · MARCH 2026




## Read the detail behind each layer.



The technology overview covers all five engine layers. The benchmark page has the stress test numbers. The engineering page covers the build standards and test suite.


        [Technology Overview](technology.html)
        [Benchmark Results](benchmark.html)
        [Engineering Standards](engineering.html)

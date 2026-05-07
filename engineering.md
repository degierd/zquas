# Engineering Standards | ZQUAS

> Engineering standards behind the ZQUAS compliance engine. 12,342 automated tests, 222,000 lines of test code, FCNS detection benchmark, defence-grade build hardening, reproducible binaries, proven cryptography.

Source: https://zquas.ai/engineering.html
Site: https://zquas.ai

---
Engineering


# Engineering Standards



How we build matters as much as what we build.








## 12,342 Tests



The engine is verified by 12,342 automated tests across 222,000 lines of test code: more test code than most companies have production code. Coverage spans cryptographic correctness, GPU compute validation, governance logic, compliance rules, privacy-preserving federation protocols, financial crime detection, synthetic benchmarking, browser-level UI, and infrastructure. The breakdown: 7,218 core engine tests (GTest, 12 audited subsystems), 1,845 Playwright browser tests, 1,185 AI agent tests, 826 case management tests, 592 end-to-end pipeline tests, 449 detection pipeline tests, plus integration, runner, narrative, config, and Python harnesses. Every test runs on every build. Zero tolerance for failures. Categories include known-answer tests against published cryptographic vectors, cross-validation between independent implementations (GPU vs CPU), boundary value analysis, adversarial input testing, determinism verification across repeated runs, multi-institution federation integration tests with realistic data distributions, and end-to-end browser tests verifying that the operator console renders real data from real detection pipelines.






## FCNS: Falsifiable Detection



The engine includes the Financial Crime Network Simulator (FCNS): the first synthetic benchmark that measures AML detection accuracy against realistic criminal behaviour. Eight FATF typologies. Three jurisdiction packs (NL, UK, DE) calibrated against national statistics. Adversarial criminals that adapt when caught. Systemic noise from real banking infrastructure quirks. Macro-economic shocks. 16 formally defined scoring metrics. Every detection claim is testable, reproducible, and falsifiable. No other vendor can prove their detection works. We publish the proof.






## GPU-Native Computation



All detection, scoring, federation, and simulation runs on GPU. 396,000 lines of C++ and CUDA. 493 GPU kernels covering detection, federation, cryptography, simulation, attestation, and adversarial fuzzing. Over 150 million policy evaluations per second. 500,000 entities evaluated in under 2 seconds. Zero CPU fallback paths in the detection pipeline. Every kernel is a CUDA global function in a dedicated compute file. Tests call GPU kernels directly with device memory. No CPU wrappers hiding GPU execution. The engine does not use GPU as an accelerator. GPU is the only execution path.






## Privacy-Preserving Federation



Cross-bank detection uses Multi-Party Computation: the data never leaves the bank. Private Set Intersection for identity matching. Arithmetic Secret Sharing and Garbled Circuits for joint risk computation. Oblivious Transfer Extension for efficient protocol execution. The federation protocol runs over the open internet. The security is in the cryptography, not the network. Same elliptic curve foundations as Bitcoin, stronger privacy guarantees. Benchmarked at 602 milliseconds for three-bank federation with zero false positives.






## Defence-Grade Build



The engine is compiled with memory protection (buffer overflow detection, address space randomisation, data execution prevention), control flow integrity (preventing return-oriented programming attacks), side-channel mitigations (Spectre variant protection), and runtime memory corruption detection. These protections are enabled for every build configuration, not just release builds. The security posture exceeds typical financial services software requirements and aligns with standards expected in critical national infrastructure.






## Reproducible Binaries



Every compilation of the same source code produces a byte-identical binary. No timestamps, no random seeds, no build environment leakage. A regulator or auditor can independently verify that the deployed binary matches the audited source code. Supply-chain integrity is a build property, not an afterthought.






## Maximum Strictness



The codebase compiles at the highest available warning level with warnings treated as errors. Static analysis runs on every build. The engine enforces C++23 standard conformance with no compiler-specific extensions. Build-time contract enforcement ensures that GPU compute kernels and CPU data structures remain aligned. ABI mismatches between components are detected at compile time, not at runtime.






## Proven Cryptography



All cryptographic operations use published, peer-reviewed algorithms. Ed25519 for digital signatures. X25519 for key agreement. Elliptic curve Diffie-Hellman for oblivious transfer base operations. Blake3 for hashing with domain separation. No custom cryptography. No proprietary ciphers. Every implementation is validated against known-answer test vectors from the relevant specification documents.






## Exact Arithmetic



Financial computations use fixed-point arithmetic with explicit precision guarantees. No floating-point rounding errors in risk score comparisons or threshold evaluations. GPU compute kernels enforce the same precision constraints as CPU reference implementations, verified by cross-validation tests.






                    12,342
                    tests


                    C++23
                    standard


                    0
                    custom crypto


                    Byte-identical
                    builds


                    0
                    floating-point in risk logic


                    150M+
                    policy evaluations per second


                    3
                    jurisdiction packs


                    16
                    detection metrics


                    602ms
                    three-bank federation

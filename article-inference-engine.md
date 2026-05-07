# Why We Built Our Own AI Inference Engine

> ChatGPT runs on one. Llama runs on one. We wrote our own. Why a financial crime company built its own GPU inference engine in C++23 and CUDA, and why regulated AI decisions need a different stack.

Source: https://zquas.ai/article-inference-engine.html
Site: https://zquas.ai

---
[← Articles](articles.html)
        May 2026 · Engineering · 9 min read


# Why We Built Our Own AI Inference Engine



ChatGPT runs on one. Llama runs on one. We wrote our own. Financial crime detection is regulated AI decision-making, and regulated AI decision-making puts requirements on inference that general-purpose stacks were not built to meet.






            When we tell AI engineers that ZQUAS authored its own GPU inference engine, written from scratch in C++23 and CUDA, the reaction is consistent. "Why? vLLM exists. TensorRT-LLM exists. llama.cpp exists. Whatever you're doing, someone has already shipped a better-tested version of it."




            It is a fair question. Writing an inference engine in 2026 looks like architectural hubris.




            The reason ZQUAS wrote its own is not that we think we are better at attention kernels than NVIDIA. We are not. The reason is that financial crime detection is regulated AI decision-making, and regulated AI decision-making puts requirements on inference that general-purpose inference stacks were not built to meet.




            The article that follows covers those requirements, what they imply for engineering, and why the choice that looks like hubris from one angle is regulatory necessity from another.




## First, a definition



            An inference engine is the software that runs an AI model. When ChatGPT answers a question, an inference engine is doing the work. When Llama generates text on your laptop, an inference engine is doing the work. The model is the weights. The engine is the machinery that turns those weights into an answer.




            vLLM, TensorRT-LLM, llama.cpp. These are the well-known engines. They are excellent at what they are for.




            We did not write our own because they are bad. We wrote it because what we are for is different.




## The audit chain runs through every byte



            Every alert ZQUAS surfaces is a regulatory decision. Under the EU AI Act, financial crime detection is high-risk AI. Under AMLD6 and the upcoming AMLR, AI decisions affecting payments must be traceable. Under MiCA and PSD3, the audit chain is examinable.




            A regulator can ask, six months after a decision: show me exactly what produced this output. Reproduce it. Byte for byte.




            That requirement has a property most ML engineers do not think about. Every byte that affects an AI decision must be reproducible across machines, across time, across software versions.




            In a typical inference stack, this is hard to deliver. IEEE 754 floating-point arithmetic is non-associative. `-ffast-math` reorders operations differently between compilers. CUDA reduction order depends on block scheduling. cuBLAS picks different GEMM kernels based on heuristics. FMA fusion happens or does not, depending on architecture flags. Any of these can produce numerically different outputs from numerically identical inputs.




            For most AI applications, none of that matters. A chatbot that responds slightly differently on rerun is fine. When AI hallucinates on a chatbot, it is annoying. When AI hallucinates on a financial crime decision, it is illegal.




## The four properties that drove the rebuild



            The ZQUAS AI inference layer is built around four properties that compound.




            **Byte-exact determinism across installations.** Two banks running the same AI model on the same transaction must produce the same decision. Not approximately. Byte-exact. Federation rounds depend on it. Privacy-preserving cross-bank pattern matching is meaningless if Bank A and Bank B disagree on what the model said.




            **Replay attestation.** Six months after a decision, a regulator must be able to take the signed attestation, replay the inference, and verify the signature. That requires committing the full computational state to a hash. Model weights, tokenizer version, CUDA toolkit version, kernel selection, quantisation scheme, runtime kind. All of it.




            **Cryptographic erasure of model versions.** GDPR Article 17 and the AI Act's data subject rights mean that when a customer requests deletion, the AI model versions trained on their data must be cryptographically inaccessible. Not deleted from disk. Erased at the per-version content key, while leaving the audit chain intact.




            **Multi-tenant isolation under shared substrate.** Multiple banks share platform libraries but cannot share runtime state. Federation rounds operate via secure multi-party primitives, not shared memory. Tenant-scoped compliance policies, tenant-scoped semantic entity ranges, tenant-scoped agent memory.




            None of these are exotic in regulated industries. All of them are inconvenient for general-purpose inference stacks designed for throughput and accuracy, not regulatory primacy.




## What had to be rebuilt



            We did not rebuild everything. The engine vendors a fork of an open-source forward pass for the Stage 1 layer. Where existing code already does the right thing, we use it.




            What we rebuilt is what could not be patched into a general-purpose stack.




            The kernel family runs at fixed template parameters per matmul site. No autotuning. The same input produces the same output on the same hardware, every time, regardless of which run picked which heuristic.




            The forward-pass orchestrator commits the full computational state, model SHA, tokenizer version, runtime kind byte, deployment kind, tier, quantisation scheme, to a determinism attestation signed by a per-runtime Ed25519 key. The attestation is the audit record.




            The KV cache lifecycle is paged and scrub-aware. Per-tenant cache isolation. Per-cycle scrub. Per-tier capacity limits. The cache does not leak between transactions or between tenants.




            The decision pipeline runs integer arithmetic at the decision boundary. Integer reductions before any float crosses a federation boundary. Floats happen inside kernels for matrix arithmetic. Floats do not happen at the decision-commit boundary.




            Specific CUDA toolkit versions known to introduce non-determinism are refused at configure time. Not warned about. Refused. The toolchain is part of the determinism contract. We would rather fail to build than build something that produces different bytes on different machines.




## The architecture follows from the constraints



            Most engineers miss this part. ZQUAS did not decide "let's build an AI platform" and then go looking for problems to apply it to. ZQUAS started from "we have to make AI decisions that regulators can examine in detail months after the fact" and worked backward to what that requires.




            The platform that fell out has properties that go beyond inference. Constitutional governance. Per-version cryptographic erasure. Federation primitives that admit any pair of bank installations that share the protocol. Cognitive-agent registration boundaries that admit additional governed agents without modifying the platform. A two-axis tenancy model where bank deployments and AI agents are orthogonal.




            Our AI inference layer is one piece of that. The piece that says: when the decision-time inference happens, it happens under a platform we can prove is reproducible.




## The choice that looks like hubris from one angle



            Most inference engines optimise for throughput, accuracy, and latency. Ours optimises for replay attestation, federation determinism, and cryptographic auditability. We pay for it in engineering time we would rather not have spent.




            That is a worse trade for almost everyone. For ZQUAS, it is the only trade that makes the regulatory commitment honest.




            When someone asks why we wrote our own inference engine, the answer is not that vLLM is bad. vLLM is excellent at what it is for. The answer is that what we are for is different.




            Regulated AI decision-making at the platform level. Audit-chain primacy. Federation under cryptographic guarantees rather than shared trust. The stack we needed did not exist, so we built it. When an auditor sits down months from now and asks us to replay an AI decision from January, we will be able to.




            That is the case. From outside it looks like hubris. From inside it is the discipline the regulation demands.




## The numbers



            The ZQUAS F1 Engine, of which the AI inference layer is one part, is 396,000 lines of C++ and CUDA across 493 GPU kernels. 222,000 lines of test code. 12,342 automated tests. One codebase, three deployment targets: the banking detection engine, the AI inference layer, and the cross-bank federation layer. Every kernel is a CUDA __global__ function in a .cu file. No CPU fallback. No #ifdef GPU_AVAILABLE. The architecture is GPU-native, not GPU-accelerated.




            The engine has been accepted into the FCA Digital Sandbox and ZQUAS is a member of the NVIDIA Inception programme. Acceptance into the FCA Digital Sandbox is not an endorsement of any firm or product.



            Danny de Gier

                Founder, ZQUAS. 18+ years in financial crime compliance at Tier-1 banks and fintechs.
                Self-taught GPU systems programmer (C++23, CUDA, Vulkan).
                Professional Postgraduate Diploma in Financial Crime Compliance (ICA / University of Manchester).

# Why We Applied to the FCA's Supercharged Sandbox

> Why ZQUAS applied to the FCA's Supercharged Sandbox: how we use AI in a compliance setting, determinism, governance and human oversight, and what participation does and does not mean.

Source: https://zquas.ai/article-fca-sandbox.html
Site: https://zquas.ai

---
[← Articles](articles.html)
        July 2026 · Company · 7 min read


# Why We Applied to the FCA's Supercharged Sandbox



We have joined the second cohort of the FCA's Supercharged Sandbox. This note explains why we applied, how we think about AI in a system that has to answer to regulators, and, just as importantly, what being there does and does not mean. It is the second FCA sandbox we have been admitted to this year, after the FCA's Digital Sandbox in the spring.






## What the Supercharged Sandbox Is



            The Supercharged Sandbox is the FCA's environment for experimenting with advanced AI in financial services. Built on the FCA's Digital Sandbox, it gives participating firms a secure, controlled setting with GPU-accelerated compute, synthetic datasets, technical tooling, and access to regulatory and expert support. The programme builds on support from NayaOne and NVIDIA, and for this cohort Anthropic provides participants with access to Claude, including Claude Code, to accelerate development work. It is cohort-based, and it is aimed at testing and developing AI use cases rather than deploying them.




            The FCA has been explicit that one of the programme's purposes is to generate insight that can inform future regulatory thinking. The FCA [announced the second cohort](https://www.fca.org.uk/news/press-releases/anthropic-supercharged-sandbox) on 22 July 2026: 21 organisations, selected from 199 applications against 132 for the first cohort. The use cases it invites include fraud detection and economic crime, which is our field.




## To Test the Claim, Not Just Make It



            We make strong claims. That financial crime can be detected across institutions without any of them pooling raw customer data. That the detection decision inside an institution can be reached in the low milliseconds, fast enough to keep up with modern payment rails, while the cross-institutional exchange that enriches it is bound by network and protocol rounds and runs on a longer timescale. That richer, cross-institutional context can materially reduce the false positives that bury compliance teams.




            We believe these claims. We have measured the latency and the cross-institutional detection on our own data. The false-positive reduction we argue from how the system is built, since a signal has to be corroborated across sectors before it escalates, rather than present as a number we have yet produced. But a claim tested only against our own benchmarks is still, from the outside, just a claim.




            The sandbox is a structured environment to put these to the test on data and infrastructure we do not control. It is a collaborative, exploratory setting rather than an adversarial audit, and we are not going to dress it up as more than that. But testing our claims somewhere other than our own benchmarks, in the open, is a step we would rather take than skip. It is the kind of step that is easy to avoid when the only marker of your homework is you.





A claim tested only against our own benchmarks is still, from the outside, just a claim.





## How We Think About AI: Determinism Where It Counts



            The programme is not called the Privacy Sandbox. It is about AI, and it is worth being direct about how we use AI, because in a compliance setting the real question is not whether to use it but where it is allowed to decide.




            Some decisions in anti-money laundering carry regulatory weight, and those decisions have to be reproducible, explainable, and auditable. Whether a policy fired, whether a threshold was crossed, whether a defined risk condition is present: a supervisor, an auditor, or a court has to be able to ask why the system did what it did, and get the same answer twice. A probabilistic model that returns a slightly different result each run, for reasons it cannot articulate, is not something you can build a regulatory decision on.




            So we draw a hard line through the system. The load-bearing detection and policy evaluation are deterministic. The same inputs produce the same outputs, every time, with a precise record of why. AI is used deliberately, and in bounded roles, where it adds value without becoming an oracle that no one can question.




## What AI Decides, and What It Does Not



            AI earns its place in the parts of the problem that are genuinely hard for fixed logic: digging into the cases the rules raise, following the counterparty network around them, flagging risk the rules under-scored, prioritising what an overloaded analyst sees first, and drafting a narrative that a human then reads and owns. These are places where a tool that is usually right and occasionally wrong is a real help, because a person stays in the loop and the consequential judgement remains theirs, on the record.




            What AI does not get to do is make the call that carries the weight, silently and unaccountably. A model can raise its hand. It does not file the report, close the account, or reach the finding on its own. That decision belongs to a person, supported by the system, with an audit trail behind it.




            There is a fair objection to this. If a model decides what surfaces and what an analyst sees first, then a model that misses something can cause it to be missed by omission, and a human sign-off at the end does not undo that. We take the point seriously, and it shapes the design. The deterministic detection does not run through the model.




            The policies evaluate on the data directly and fire whatever they fire, whether or not the model has looked at anything alongside them, and a firing below threshold is still logged so compliance can see it happened. The model works on the cases the rules raise and the entities an analyst points it at. There it can raise suspicion the rules under-scored and follow the network around a case, but it cannot lower or suppress what the rules found. It is advisory over the cases in front of it, not a gate in front of the rules.




            What it still influences is order, which cases a stretched analyst reaches first, and that is a real limitation we manage rather than wish away. It does not silently switch off the deterministic layer beneath it.





In compliance, a system that cannot reproduce its own decision, or explain it the same way twice, is not one a regulator can accept. That constraint is not something we work around. It is a design principle.





            Underneath sits a governance layer. The policies that drive detection are written as code: versioned, reviewed, and auditable, so the system's behaviour is governable and every change to it is tracked. Beyond explaining why a decision was made, the system is built to produce a verifiable record of what it actually did, closer to cryptographic attestation than to a log you simply have to trust, because in regulated AI, being able to prove what happened matters as much as being able to describe it. And the models themselves run inside the institution's own environment rather than through an outside service, so no customer data leaves for inference and the model's behaviour stays under the institution's control.




            That last point is a large part of why we built [our own inference engine](article-inference-engine.html) instead of calling out to a third-party API. Running inference inside our own stack is what lets us keep data in place, control how the model behaves, and hold it to the same governance as the rest of the system, rather than accepting whatever a remote service happens to do. We set out the reasoning at the time. The engine is now fully delivered and runs as the default inference path in our own stack.




            We are not asking to be judged on the fact that we use AI. We are asking to be judged on whether the system behaves the way a compliance system must: reproducibly, explainably, under human oversight, with a record that stands up. An AI sandbox built for exactly this kind of experimentation is where those properties can be tested, rather than only asserted.




## Privacy by Design Is the Method, Not a Constraint



            The programme runs on synthetic data, and it expects participants to design for privacy and security from the outset. For many firms that is a discipline to adopt. For us it is simply how the technology already works. ZQUAS is built to detect financial crime without exposing raw customer data, and we test on synthetic data rather than real records as a matter of principle, not compliance.




            So an environment that provides representative synthetic data and expects privacy by design is not a set of rules we are tolerating. It is close to the environment we would have chosen. It lets us test detection quality, including the network patterns that single-institution systems miss, on data that behaves like the real thing, without a single real customer's information ever being involved.




            We should be equally clear about the limit of this. Synthetic data is a starting point, not the finish line. It is generated from patterns that are already known, and real financial crime is adversarial, built to evade the patterns we already know, so performing well against it shows the approach works under controlled conditions, not that it survives contact with live, messy, hostile data.




            That test comes later, with real data inside a real institution, and it is the one that ultimately counts. The sandbox is a serious step toward it, not a substitute for it.




## Building Close to the Questions the Technology Has to Answer



            Our architecture is a direct response to what regulation permits and what privacy law forbids. The reason ZQUAS computes across institutions using private set intersection and multi-party computation, rather than pooling data in a central platform, is that the central-pooling model has run into exactly those limits. Technology whose entire job is to operate inside the rules is best developed close to the people who set them.




            What the sandbox does is put the work in a setting built to surface the questions that matter, at the stage where they are cheapest to answer.




## What We Expect to Get Out of It



            Not, we hope, a tidy confirmation of everything we already believe, because testing is only worth doing if it can tell you that you are wrong. If our approach has weaknesses, under load, on unfamiliar data, at the seams between institutions, this is where we would rather find them: now, in a controlled environment, than later in front of a bank.




            That is the honest reason we applied. Not for a badge, but for a harder test than we can run on our own, of an idea we think is worth testing: that financial crime can be detected across institutions without asking anyone to give up their customers' data, and that AI can play a serious part in it without giving up determinism, governance, or human oversight. The Supercharged Sandbox is a place to find out. We will share what we learn.




            Read more about how the system works on the [architecture page](architecture.html), why we built [our own inference engine](article-inference-engine.html), or about who we are on the [about page](about.html).



            Danny de Gier

                Founder, ZQUAS. 18+ years in financial crime compliance at Tier-1 banks and fintechs.
                Professional Postgraduate Diploma in Financial Crime Compliance (ICA / University of Manchester).

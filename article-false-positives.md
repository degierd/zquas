# The 95% Problem

> Most AML alerts are false positives. Modern systems already use customer context, baselines and machine learning, yet stay bounded by network visibility that ends at the bank's own perimeter.

Source: https://zquas.ai/article-false-positives.html
Site: https://zquas.ai

---
[← Articles](articles.html)
        June 2026 · Analysis · 6 min read


# The 95% Problem



Anti-money laundering systems flag enormous volumes of legitimate activity as suspicious. The cost is not only the wasted review. It is the genuine criminal activity hiding inside the noise, and the fact that the context needed to tell the two apart increasingly lies beyond any single institution's reach.






            Every compliance team knows the number, even if nobody says it out loud. In transaction monitoring, the large majority of alerts are false. Figures above ninety percent are reported routinely in regulatory speeches, supervisory reviews, and industry studies, and the real rate varies widely by bank, jurisdiction, and scenario. But the direction is not in dispute.




            An analyst working through a hundred alerts in a day may find that the overwhelming majority describe nothing more than a customer behaving normally. That is usually discussed as an efficiency problem. The more consequential problem sits underneath it.




## Context Is the Constraint, and It Stops at the Perimeter



            It would be convenient to blame this on primitive technology, and inconvenient for that story that it is largely untrue. Modern monitoring is not a wall of fixed thresholds. Good systems already reason with customer risk scores, behavioural baselines, peer groups, and expected activity. They already draw on KYC data, occupation, geography, adverse media, and watchlists.




            Rules and models can and do reference customer context. The picture of the customer they work from is far richer than a single transaction. The limit is not that these systems are blind. It is that the context each one holds is bounded, and it is bounded most sharply at the edge of the institution.




            A bank can build a detailed picture of how a customer behaves at that bank. It cannot see how the same customer behaves everywhere else, because that activity sits in other institutions and never reaches it. The context runs out exactly where the customer's activity crosses to another bank. That is precisely where a great deal of laundering is designed to live.




## The Cost Is Not the Review. It Is the Miss.



            The direct cost is visible on any compliance budget. Institutions spend heavily on alert review, much of it consumed by cases that were never going to be anything. But the expensive failure is the one that does not appear on a budget line. When most alerts are noise, the ones that matter are buried inside it.




            An analyst working through a long queue of mostly-nothing is not in a strong position to recognise the single case that is actually a laundering network.





Alert fatigue is not a morale issue. It is a detection failure. The false positives are not just wasting time. They are camouflage for the true positives.





            This part is well supported. Work from the FATF, the Wolfsberg Group, and academic studies points the same way: high alert volumes reduce investigation quality, analyst attention, and time per case. A system that floods its analysts with noise is not only inefficient. It is worse at catching criminals, because it has made the real signals harder to see.




## Better Rules and Models Hit the Same Ceiling



            The instinctive response to a missed case is to add a rule, and over years the rule set grows into the hundreds. Mature programmes work hard against the resulting volume. They tune thresholds, add suppression logic, segment customers, and retire rules that have stopped earning their place. Increasingly they layer machine learning on top to suppress false positives and rank what remains.




            That genuinely helps. Models do real work in modern AML, and they often reduce false positives substantially. Dismissing any of it would be wrong. But all of it meets the same ceiling.




            Tuning reshuffles how the system reasons about the information it already has. A model reasons only about the data it was given. Neither adds the information that is missing. A capable model trained on one bank's view is still confined to one bank's view.




            If the underlying data never contained what was needed to separate a criminal from a customer, better technique redistributes the error rather than removing it. Better modelling raises the ceiling the data allows. It does not lift the data's own limit.




## The Rise of Network Context



            One of the most significant recent advances in AML is not a sharper threshold or a bigger model. It is looking at relationships rather than at transactions in isolation. Graph and network analysis have moved to the centre of the field precisely because so much of what matters is relational: mule rings, layering chains, shell structures, hidden beneficial ownership, and coordinated activity that no single transaction reveals. Seen as a network, a set of individually unremarkable accounts can resolve into an obvious pattern.




## Context Has a Ceiling Too, and Only the Network Breaks It



            Context is not a silver bullet, and it is worth saying so plainly. A determined criminal manipulates it. They age mule accounts, build a plausible transaction history, and mimic a legitimate business until the activity looks entirely normal. Richer context alone does not defeat a patient adversary.




            But notice what defeats single-bank context in every one of those cases. The manufactured normality is constructed at one institution, for the eyes of one institution. A criminal can build a clean history at your bank. Building a clean position across the entire network, at every institution they touch at once, is far harder.




            The coordination that makes the scheme work is exactly what becomes visible when the view spans institutions. Synthetic normality is a single-bank illusion. It is the strongest argument for context that does not stop at the perimeter, not against it.




## Investigate Risk, Not Noise



            So the goal is not the impossible one of a system that emits only genuine alerts. Precision and recall trade against each other, and any honest detection system lives with that trade. The goal is to move it: to raise fewer alerts on noise and more on what actually matters, by giving the system the context that decides the difference.




            Better context does not abolish false positives. It reduces how often the system mistakes an ordinary customer for a suspicious one, and how often it misses a suspicious one hiding as ordinary.




## Where the Missing Context Comes From



            The context that breaks the single-bank ceiling has to come from other institutions. That is where earlier attempts came undone. The obvious way to share it is to pool everyone's data in one place, and privacy law has made that road increasingly hard to sustain. GDPR Article 5(1)(c) sets data minimisation against bulk pooling, and AMLR Article 75 opens only a narrow gateway, restricted to customers a bank has already assessed as higher-risk.




            [Transaction Monitoring Netherlands](tmnl.html) was the most ambitious attempt at the pooled model in Europe. It was wound down. The technology worked. The legal basis for centralising customer data across five banks did not.




            This is the problem ZQUAS is built to solve, and the entire point is to solve it without that central database. Two institutions can compute the overlap between their entities and signals without either revealing its underlying customer data, using private set intersection over elliptic-curve Diffie-Hellman (ECDH-PSI). Joint analysis across several parties runs as secure multi-party computation. In both cases the raw data never leaves the institution that holds it.




            Only cryptographically protected values ever cross an institutional boundary, and no central platform holds anyone's records. It is not the pooled model that earlier consortia moved away from, and it is not the prohibitive overhead of fully homomorphic encryption. It is private set intersection and multi-party computation, run peer to peer, with GPU acceleration used to reduce the computational cost of the cryptography and the detection itself.




            GPU acceleration is not what makes the cross-institutional exchange practical. The binding constraints there are communication and protocol rounds, not arithmetic. What the hardware buys is keeping the compute side cheap enough to run at scale.




            The result is the one thing tuning, modelling, and single-bank graphs cannot provide: network context that is substantially harder for a criminal to manipulate by looking normal at any single bank, delivered without a central store of pooled data. This is not a complete solution, and it does not pretend to be. A criminal who deliberately spreads activity through institutions or jurisdictions outside the participating network stays only partially visible. What it removes is the option of hiding in plain sight across the banks that do take part.




            It is not a replacement for rules, models, analysts, or good KYC. It is the missing layer that lets all of them work on a fuller picture.




            See how the [architecture](architecture.html) resolves cross-institutional context without pooling data, or follow [the full detection flow from transaction to SAR](use-case.html).



            Danny de Gier

                Founder, ZQUAS. 18+ years in financial crime compliance at Tier-1 banks and fintechs.
                Professional Postgraduate Diploma in Financial Crime Compliance (ICA / University of Manchester).

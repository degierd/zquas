# When the Money Has Already Moved

> Instant payments do not make AML obsolete or turn monitoring into payment authorisation. They change the economics of time, and raise the premium on detection that keeps pace with the rails.

Source: https://zquas.ai/article-instant-payments.html
Site: https://zquas.ai

---
[← Articles](articles.html)
        June 2026 · Banks · 7 min read


# When the Money Has Already Moved



Euro payments now settle in ten seconds, around the clock, and cannot be undone. That does not make anti-money laundering obsolete, and it does not turn transaction monitoring into payment authorisation. What it changes is the economics of time, and it puts a rising premium on detection that keeps pace with the rails instead of trailing them by a day.






            As of 9 January 2025, every payment service provider in the euro area must be able to receive instant euro credit transfers. As of 9 October 2025, they must be able to send them. An instant transfer settles within ten seconds, runs twenty-four hours a day on any day of the year, and once settled is final. The hundred thousand euro ceiling that used to cap instant transfers is gone.




            This is Regulation (EU) 2024/886, the Instant Payments Regulation, and it is in force now.




            It is worth being precise about what this touches, because it touches different controls differently. Blocking a suspicious payment before it executes is a fraud control. Anti-money laundering monitoring is a separate function, and it has always been substantially retrospective. Banks monitor activity, investigate alerts, and file Suspicious Activity Reports, and where warranted they freeze accounts, close relationships, and refer cases to law enforcement.




            AML is not expected to stop every suspicious payment before it happens, and instant rails do not change that mandate. Anyone arguing that instant payments have made transaction monitoring invalid has run two different functions together.




            So the interesting question is not whether AML must now block payments. It is what instant, irrevocable, always-on rails do to the value of detection that arrives late.




## AML Is Retrospective by Design. Latency Still Has a Cost.



            Concede the point fully. Much of what AML does happens after the money has moved, and much of it remains effective there. Retrospective monitoring surfaces structuring, mule networks, laundering rings, and sanctions-evasion patterns. Those investigations lead to real outcomes: accounts frozen, networks dismantled, proceeds recovered, cases referred.




            But every one of those outcomes depends on time. A freeze only helps while the account still holds funds. A referral is strongest while the trail is warm. Closing a mule account matters most before it has cycled another few hundred thousand euros through it.




            Detect a network within a day and most of that toolkit is still live. Detect it weeks later, which is not unusual, and the money and the accounts have already moved on. On slower payment infrastructures that lag often had less immediate impact, because the money itself moved less quickly. Instant settlement narrows the margin sharply, because by the time a delayed response is ready, the thing it has to reach is already somewhere else.





Retrospective is not the problem. Slowly retrospective is where the value leaks out.





## The Crime Moves at the Speed of the Rails. The Control Often Does Not.



            Layering that once took hours or days can now happen within minutes, at any hour. Funds cycle through mule accounts continuously, across the weekend, overnight, on a public holiday, whenever the periodic batch is not running. If detection sweeps once a night while laundering runs in minutes, the launderer completes many more cycles between sweeps than the control was ever designed to tolerate.




            Many institutions have already recognised this and moved parts of their monitoring onto streaming and event-driven architectures. That is the right direction, and not everything is still an overnight batch.




            The point is not the batch as such. It is that the cadence of the control has to close the gap with the cadence of the crime, and instant rails widened that gap. Closing it is the real work of the next few years.




## Fraud and AML Are Converging, and Real-Time Context Serves Both



            Banks do not defend instant rails with AML alone. They already run real-time fraud engines, velocity checks, device and behavioural analytics, mule detection, and verification of payee. Those controls already stop a great many suspicious instant payments before settlement. None of that should be pretended away.




            What is happening underneath is a convergence of fraud and anti-money laundering, often called FRAML. Instant payments, authorised push payment fraud, and mule networks have blurred the old boundary between the two. The underlying question is the same on both sides: is this entity, seen in the context of its network, behaving like part of a criminal operation.




            Answered in real time, that question feeds the fraud decision that can block a payment, and it sharpens the AML detection that investigates and disrupts one. That is the honest case for real time in an AML context. Not that monitoring must adjudicate payments, but that real-time entity and network intelligence is the shared substrate underneath both.




            It makes the pre-settlement control that can act more accurate, and it lets the retrospective control act while its own tools still work. Both matter. Replacing either with the other would weaken the whole.




## The Hard Part of Real Time Is Context, Not Clock Speed



            Here a common assumption needs correcting. Ten seconds is an enormous amount of computing time. Modern systems perform fraud scoring, sanctions checks, authentication, and routing in tens to low hundreds of milliseconds. Raw speed is not the bottleneck, and any argument for real-time detection that rests on cycle time is arguing the wrong point.




            The bottleneck is context and precision. A verdict is only as good as the picture behind it, and the useful picture includes the entity's full behaviour and the shape of its network, including the parts that sit at other institutions. Assembling that picture, keeping it current, and reaching a precise decision on it, at all hours and at scale, without pooling raw customer data across banks, is a genuinely hard problem.




            A fast decision on thin context is worse than a slow one. It blocks good customers and misses coordinated ones. The engineering challenge of real-time detection is resolving rich, cross-institutional context in time to use it, not shaving milliseconds off a rule engine.




## Real Time Is a Direction, Not a Doctrine



            None of this makes batch retrospective monitoring obsolete, and it is not going away. It remains the right tool for long-horizon typologies, for patterns that only resolve over weeks, and for the deep investigations that produce freezes and referrals. There is no single mandated architecture, and anyone selling one as inevitable is overreaching.




            But the trajectory is not really in dispute. As the rails accelerate, more of the detection value moves toward the point where a response can still land. That means continuous, context-rich intelligence sitting alongside retrospective analysis, rather than [the batch cycle carrying the load alone](article-batch-processing.html).




            The batch era is not ending. Its monopoly on detection is.




## The Rails Are Not Waiting



            The money now moves in seconds, around the clock, and it does not wait for morning. AML does not have to block the payment to matter. But it does have to catch up to the rails, because its own instruments, the freeze, the referral, the closed account, only work on money and accounts that are still there.




            Speed, in the end, is not about the payment. It is about whether the response arrives while it can still do something.




## How ZQUAS Closes the Gap



            Resolving cross-institutional context in real time is the hard problem this article describes, and it is the one ZQUAS is built for. Doing it means computing across banks without any of them surrendering raw customer data, and without a central platform holding it. That avoids the centralised data-sharing models that have proven difficult to sustain under GDPR and under the narrow sharing gateway in AMLR Article 75.




            ZQUAS uses private set intersection over elliptic-curve Diffie-Hellman (ECDH-PSI) between two institutions, and secure multi-party computation across several, so only cryptographically protected values ever cross an institutional boundary. It is not central pooling, and it is not the overhead of fully homomorphic encryption. It runs peer to peer, with GPU acceleration used to reduce the computational cost of the cryptographic protocols and the detection itself.




            The binding constraint on the cross-institutional exchange is communication and protocol rounds rather than arithmetic. A bilateral federation round completes in under 10 seconds, measured at 7.8 seconds across 100,000 entities. That exchange runs on a longer timescale than the local decision it informs.




            Within a single institution, the alert-processing lifecycle completes in under 10 milliseconds, measured at 3.92ms. That figure covers the engine's own detection path in controlled testing, not the cross-institutional exchange. Speed there is not the boast.




            The point is that a local decision reached that quickly, enriched by network context a central database could not safely provide, arrives while a response can still land. That is what building for speed means on rails that no longer wait.




            See how the architecture works on the [architecture page](architecture.html), or the measured results, and exactly what each figure covers, on the [benchmark page](benchmark.html).



            Danny de Gier

                Founder, ZQUAS. 18+ years in financial crime compliance at Tier-1 banks and fintechs.
                Professional Postgraduate Diploma in Financial Crime Compliance (ICA / University of Manchester).

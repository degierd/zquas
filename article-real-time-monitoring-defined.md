# What Does Real-Time Actually Mean?

> Every transaction monitoring vendor claims real-time. The term has three distinct meanings with fundamentally different implications for detection capability. A framework for evaluating what real-time actually delivers.

Source: https://zquas.ai/article-real-time-monitoring-defined.html
Site: https://zquas.ai

---
[← Articles](articles.html)
        March 2026 · Technology · 8 min read


# What Does Real-Time Actually Mean?



Every transaction monitoring vendor claims real-time. The term appears on every product page, in every RFP response, in every sales deck. When every vendor checks the same box, the box becomes meaningless. The question is not whether a system is real-time. The question is: real-time at what scale, for what computation, and with what guarantees?






            Transaction monitoring has a vocabulary problem. "Real-time" is used to describe systems that differ by orders of magnitude in what they actually compute and how fast they compute it. A system that returns one API response in two seconds and a system that evaluates twelve million entities in parallel both call themselves real-time. The word has lost its meaning.




            The distinction matters because it determines detection capability. A system that responds quickly to individual transactions is not the same as a system that maintains current risk intelligence across the entire customer population. The first is fast plumbing. The second is fast intelligence. Both have the word "fast" in the description. They are fundamentally different things.




            There are three distinct levels of real-time processing in transaction monitoring. Each level represents a different architecture, a different capability, and a different cost structure. None of them is wrong. But they are not the same, and conflating them leads to poor vendor selection and gaps in detection coverage.




## Level 1: Per-Transaction API Response



            A transaction arrives via API. The system evaluates it against a set of rules or a scoring model. It returns accept, reject, or review within a defined time window. For instant payment schemes, that window is typically two to three seconds.




            The processing model is straightforward: one transaction in, one decision out. The system handles transactions sequentially or in small concurrent batches. The "real-time" claim refers to the response latency for an individual transaction, not the processing capacity of the system as a whole.




            Typical throughput sits at hundreds to low thousands of decisions per second. At peak volumes, transactions queue and response times degrade. Most systems handle this by horizontally scaling API workers, which preserves response time but does not change the fundamental processing model.




            The limitation is not speed. It is staleness. Each transaction is evaluated against a risk profile that was computed in a previous batch cycle. That batch may have run overnight. It may have run six hours ago. The system responds fast, but it responds based on yesterday's intelligence. A customer whose risk profile changed at 9:00 AM based on transactions at another institution will still show as low-risk until the next batch run, which might be midnight.




            Most SaaS transaction monitoring vendors, cloud-native rule engines, and API-first compliance platforms operate at this level. The architecture is well understood, relatively simple to deploy, and sufficient for many use cases. For banks processing moderate volumes with stable risk profiles, Level 1 meets the regulatory requirement for timely monitoring.




## Level 2: Streaming Analytics



            Transactions flow through a streaming pipeline built on infrastructure such as Kafka, Spark Streaming, or Flink. The system maintains running aggregates, statistical models, and behavioural profiles that update with each new event. Risk profiles are not computed in overnight batch cycles. They evolve continuously as new data arrives.




            The improvement over Level 1 is significant. Instead of evaluating each transaction against a static snapshot, the system evaluates against a risk profile that incorporates every prior transaction. Velocity checks, pattern detection, and anomaly scoring all operate on current data rather than data that is hours old.




            Throughput is substantially higher: tens of thousands to low hundreds of thousands of events per second, depending on infrastructure investment and pipeline complexity. The streaming architecture is designed for sustained high-volume processing, not just burst response.




            The limitation is computational depth. Simple operations run at streaming speed: aggregate calculations, threshold checks, statistical models. Complex operations do not. Graph analysis, entity resolution across millions of accounts, network topology detection: these computations are too expensive to run on every event. They get deferred to micro-batch windows that run every few minutes or every few hours. The system is fast for what it can compute in the stream, and slow for what it cannot.




            Enterprise transaction monitoring platforms with streaming capabilities operate here. Some newer vendors built their entire architecture on streaming-first principles. The trade-off is explicit: you get fresher risk intelligence for simple computations, at the cost of infrastructure complexity and higher operating expense.




## Level 3: Population-Scale Parallel Evaluation



            The system evaluates the entire entity population simultaneously. Every account, every risk score, every relationship, every policy. All computed in parallel on GPU hardware. Not one transaction at a time. Not one stream at a time. All entities at once.




            The processing model is inverted. Instead of waiting for a transaction to arrive and then evaluating it, the system continuously maintains the full governance state of every entity in the population. When a transaction arrives, the entity's state is already current. The decision is not computed on arrival. It was already computed.




            Throughput is measured in millions of governance decisions per second. The processing capacity exceeds the transaction arrival rate by orders of magnitude. There is no queue. There is no degradation at peak volume. The system runs faster than the data arrives, which means the bottleneck is never computation.




            The critical difference is what gets computed at full speed. Graph analysis, network detection, cross-entity pattern matching, relationship topology: these all run at the same speed as simple threshold checks. There is no deferred computation. There are no micro-batch windows. The entity resolution graph, the relationship network, and the risk scoring model all live in GPU memory and update in parallel.




            The limitation is infrastructure. GPU-native compliance requires GPU hardware. It cannot run on commodity cloud instances. The software architecture must be designed for parallel computation from the ground up. Existing CPU-based systems cannot be retrofitted. The data structures, memory layout, and execution model are fundamentally different.




            GPU-native compliance engines operate here. The category is new. The hardware requirements and architectural constraints mean this is not a feature that can be added to an existing product. It is a different class of system.




## Making It Concrete



            A mid-size European bank processes 2.5 million transactions per day. That is approximately 29 transactions per second on average, with peaks of 200 to 500 per second during business hours.




            A Level 1 system handles this load. Each transaction gets a response in two to three seconds. But each decision is based on a risk profile that was computed overnight. The system is fast at responding but slow at understanding. An entity whose risk changed this morning will not be flagged until tomorrow's batch updates the profile.




            A Level 2 system handles this load easily. Risk profiles update with each transaction. Velocity patterns and threshold breaches are detected in near-real-time. But complex graph analysis, such as identifying networks of related entities operating across multiple product lines, still runs in micro-batch windows. Those windows might be every fifteen minutes, every hour, or every six hours depending on the computation and the infrastructure budget.




            A Level 3 system evaluates the entire customer population, potentially millions of entities, multiple times per second. Every entity's risk is current at all times. When a transaction arrives, the governance decision has already been made. Graph relationships, network topology, and cross-entity patterns are continuously evaluated, not deferred. The 29 transactions per second arrive into a system that is processing 150 million+ policy evaluations per second. The transaction is not the trigger for computation. It is a data point absorbed into a computation that is already running.




## The Cross-Institutional Dimension



            Single-institution monitoring, regardless of level, has a fundamental blind spot. The criminal who maintains low-risk profiles at five separate banks is invisible to each bank individually. Detecting that pattern requires comparing data across institutions.




            AMLR Article 75, applicable from July 2027, permits cross-institutional information sharing for AML purposes. The question is how each level of real-time monitoring handles this new requirement.




            Level 1 systems cannot perform cross-institutional detection. Each API call evaluates one transaction at one institution. There is no mechanism for incorporating risk signals from other banks into the per-transaction decision, unless those signals are pre-loaded into the batch risk profile, which reintroduces the staleness problem.




            Level 2 systems can incorporate cross-institutional data, but doing so requires a shared data infrastructure: a common data lake, a messaging platform, or a centralised analytics environment. Each of these approaches involves sharing raw or minimally transformed data between institutions. GDPR and banking secrecy obligations create significant legal barriers. TMNL in the Netherlands demonstrated that centralising transaction data across banks, even with good intentions, runs directly into privacy law.




            Level 3 systems can perform cross-institutional detection through multi-party computation. Banks jointly evaluate shared entities without sharing underlying data. The MPC protocols run at GPU speed, matching the performance of local evaluation. Each bank's data remains within its own infrastructure. The computation produces correct risk assessments without revealing inputs. Privacy is mathematically guaranteed by the cryptographic protocol, not dependent on data sharing agreements or access controls.




## The Right Question to Ask Your Vendor



            When evaluating a transaction monitoring system, the standard question is: "What is your API response time?" That measures Level 1 performance. It tells you how fast the plumbing works.




            The better question is: "How many governance decisions can the system compute per second, across the full entity population, with current risk profiles?"




            The first question measures responsiveness. The second measures intelligence. Both matter. But only the second determines whether your compliance programme detects financial crime or simply processes transactions quickly.




            Ask your vendor which level they operate at. Ask them what computations run at streaming speed and what gets deferred to batch. Ask them how stale the risk profile is when a transaction decision is made. Ask them what happens to response times at peak volume. The answers will tell you more than any product page.




## Conclusion



            Real-time should mean that every entity in the system is evaluated continuously, not that each transaction gets a fast response based on yesterday's risk profile. The infrastructure to achieve this exists today. The question for compliance teams and technology leaders is whether their current monitoring operates at the level they assumed it did, or whether the "real-time" label has been masking a gap between capability and expectation.



            Danny de Gier

                Founder, ZQUAS. 18+ years in financial crime compliance at Tier-1 banks and fintechs.
                Professional Postgraduate Diploma in Financial Crime Compliance (ICA / University of Manchester).

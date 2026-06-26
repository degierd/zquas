# From Edge to Federation: A Unified Architecture for Real-Time Financial Crime Detection

> A ZQUAS position paper. A single detection engine that replaces overnight batch processing with continuous real-time monitoring. From the bank's data centre to a federated network spanning five banks. The same code, the same compliance policies, the same detection algorithms, processing every transaction the moment it occurs.

Source: https://zquas.ai/article-edge-to-federation.html
Site: https://zquas.ai

---
[← Articles](articles.html)
        March 2026 · Position Paper · 28 min read


# From Edge to Federation: A Unified Architecture for Real-Time Financial Crime Detection



A single detection engine that replaces overnight batch processing with continuous real-time monitoring. From the bank's data centre to a federated network spanning five banks. The same code, the same compliance policies, the same detection algorithms, processing every transaction the moment it occurs.



*Danny de Gier, Founder ZQUAS. 18 years financial crime compliance: Deutsche Bank, HSBC, RBS, ABN AMRO. PGDip Financial Crime Compliance, University of Manchester.*







## Executive Summary



The anti-money laundering industry has a structural problem that no amount of artificial intelligence can fix. Every major vendor sells the same architecture from 2005: collect transactions in a central database, run detection rules overnight, generate alerts the next morning. The only thing that has changed in twenty years is the label. What was "rules-based detection" is now "AI-powered monitoring." The pipeline is identical.



The Dutch Court of Audit (Algemene Rekenkamer) confirmed the result in the Netherlands: 13,000 full-time employees, 530,000 annual suspicious activity reports, and no measurable effectiveness in detecting or preventing financial crime. The pattern repeats globally. FinCEN processed over 4.7 million suspicious activity reports in fiscal year 2024 in the United States. The UK's FCA has fined multiple banks for monitoring systems it described as "inadequate and ineffective." The current approach is not underperforming. It is architecturally incapable of solving the problem it was designed for.



This paper presents a fundamentally different approach. A single detection engine that replaces overnight batch processing with continuous real-time monitoring. The same code, the same compliance policies, the same detection algorithms, processing every transaction the moment it occurs and sharing risk intelligence across institutions in seconds. Not faster batch processing. Continuous, real-time financial crime detection connected across the entire banking infrastructure.



The engine exists. It has been built. It runs on hardware ranging from a EUR 299 second-hand laptop to the most powerful GPU in the world. And the same architectural decisions that make it effective for detection also make it an ESG powerhouse: 60 to 80 percent lower energy consumption than CPU-based alternatives, reduced pressure to de-risk vulnerable customers, and cryptographic audit trails that satisfy the EU AI Act's explainability requirements. This is not a research proposal. It is a working system.



## 1. The Industry's AI Problem



Let us be direct about what is happening in the anti-money laundering vendor market.



A compliance officer at a major bank receives a visit from a technology vendor. The vendor presents a slide deck. The slides show the word "AI" on every page. The pitch explains that their transaction monitoring platform now uses machine learning to reduce false positives. The reduction is real. False positive rates drop from 95% to perhaps 85%. The compliance officer signs the contract. The vendor deploys the system. It takes six to twelve months.



What has actually changed? The transactions still flow into a central database. They are still processed in overnight batch cycles. The detection rules still fire against historical data. Alerts still arrive the next morning. The only difference is that a machine learning model now sits on top of the same pipeline, filtering out some of the noise.



This is not innovation. This is optimisation of a broken system.



The underlying architecture has not changed since the first transaction monitoring systems were deployed in the mid-2000s. The data flow is the same: transactions in, alerts out, 24 hours later. The institutional scope is the same: one bank, one database, one view. The computational model is the same: CPU-based batch processing in a data centre.



Placing a machine learning model on top of this pipeline is like installing a better spam filter on a fax machine. The filter might work. But the fax machine is still the problem.



The regulators are not just beginning to understand this. They are acting on it. The European Anti-Money Laundering Authority (AMLA) has been operational since July 2025, based in Frankfurt. In January 2026, all AML responsibilities were transferred from the European Banking Authority to AMLA. On 24 March 2026, AMLA holds its first public hearing. Direct supervision of 40 high-risk financial institutions begins in 2028. Article 75 of the Anti-Money Laundering Regulation (AMLR) mandates mechanisms for cross-institutional information sharing. This is not a request for better analytics within a single bank. It is a recognition that the single-institution model is fundamentally inadequate.



The Algemene Rekenkamer's findings are not an indictment of any particular vendor or bank. They are an indictment of the architecture itself. Thirteen thousand people processing half a million reports annually with no measurable result is not a staffing problem. It is not a technology problem. It is a structural problem. The industry is monitoring in the wrong place, at the wrong time, with the wrong scope.



Solving this requires architectural innovation, not analytical improvement.



## 2. Where Financial Crime Actually Happens



To understand why the current architecture fails, you need to understand how money laundering works in practice. Not in a textbook. In the real transaction flows of real banks.



Money laundering has three stages: placement (getting dirty money into the financial system), layering (moving it through multiple accounts and institutions to obscure its origin), and integration (using the cleaned money to purchase legitimate assets). These stages do not happen in one place. They happen everywhere. And they do not happen in one day. A well-run criminal network operates over weeks, spread across multiple banks.



The following scenario uses the Netherlands as an illustration. The same pattern operates in every jurisdiction with a multi-bank retail banking system.



Consider a mule network operating across Dutch banks. A criminal organisation recruits five individuals, often students or recent immigrants, to open bank accounts at multiple institutions. Cash from drug trafficking is deposited in modest amounts across these accounts. That is placement. The money then moves through a chain of transfers between mule accounts at different banks. Person X at Bank A sends EUR 2,000 to Person Y at Bank B. Person Y sends EUR 1,800 to Person Z at Bank C. Each transfer is below reporting thresholds. Each looks unremarkable in isolation. That is layering. Finally, the mules extract cash: EUR 500 from an ATM in Rotterdam on Monday, EUR 750 from two ATMs in Utrecht on Tuesday, EUR 500 in Amsterdam on Wednesday. Two or three small withdrawals per day, always below the daily limit, always at different machines. Each mule extracts EUR 18,000 over three weeks. Five mules, five banks, EUR 87,000 in cash. That is integration.



Where in this chain does the current monitoring infrastructure detect the crime?



At each individual bank, the transactions look ordinary. Bank A sees a customer receiving a small cash deposit and making a small transfer. Bank B sees a customer receiving a transfer and making another transfer. Bank C sees a customer receiving a transfer and making modest ATM withdrawals. Each transaction, viewed in isolation by one bank, is unremarkable.



The criminal network is only visible when you can see across all three banks simultaneously. The chain of transfers, the convergence of deposits from multiple mules, the timing patterns, the eventual extraction of consolidated funds. None of this is visible from inside a single institution.



But the more fundamental problem is time. Even if a bank could detect the suspicious pattern within its own transactions, the detection happens 24 hours after the transactions occurred. Every night, the batch system processes the day's transactions. Every morning, new alerts appear. By the time the analyst reviews the alert on Wednesday, the mule has been extracting cash since Monday. The alert is a historical record, not an intervention.



What if the bank's detection engine processed each transaction the moment it occurred? Not overnight. Not hourly. The moment the transaction entered the system.



Monday 14:00: Mule Y withdraws EUR 500 in Rotterdam. The institutional detection engine processes the transaction immediately. Risk score updated.



Monday 14:30: Y withdraws EUR 500 in Utrecht. Processed immediately. Pattern detected: same customer, different city, 30 minutes apart. Risk elevated.



Monday 15:00: Y withdraws EUR 400 in Amsterdam. Processed immediately. Structuring pattern confirmed across three cities in 90 minutes. Alert fires. The analyst sees it at 15:01.



Now add cross-bank intelligence. Bank A flagged this customer's network that same morning. With real-time processing, the federation signal is already in Y's risk profile when the first ATM withdrawal hits the system. The alert fires on the first withdrawal, not the third.



The analyst freezes the account Monday afternoon. Not Wednesday morning. Two days of extraction prevented.



This is not an incremental improvement. It is a structural change in when detection happens relative to when the crime happens.



## 3. A Different Architecture: Three Layers, One Engine



The ZQUAS F1 Engine is built on a simple premise: detection should happen the moment a transaction occurs, not 24 hours later. And it should be informed by intelligence from across the banking system, not limited to a single institution's view.



The architecture has three layers. Each layer runs the same engine. The same binary, compiled from the same source code, evaluating the same compliance policies. The difference between layers is not capability. It is scope.







### Layer 1: Institutional — Real-Time Full-Population Monitoring



The institutional installation is the primary detection engine, deployed in the bank's own data centre on enterprise GPU hardware. It is the replacement for the traditional batch transaction monitoring system. Where the current system processes yesterday's transactions tonight, the F1 Engine processes every transaction the moment it enters the system.



The institutional installation runs five detection layers, each analysing a different dimension of financial behaviour:



**Temporal detection** identifies time-based patterns. Is this customer suddenly active after months of dormancy? Are transfers happening at 3 AM with clockwork regularity? Is the frequency of transactions increasing in a way that deviates from this customer's normal behaviour? Are there three ATM withdrawals in three different cities within 90 minutes?



**Structural analysis** examines the shape of relationships between entities. Are twenty accounts all connected to the same counterparty? Does the network topology resemble a known mule structure, where funds flow inward from many sources and converge at a single extraction point?



**Behavioural anomaly detection** establishes a baseline for how each customer normally transacts and flags deviations. Not individual transactions that exceed a threshold, but sustained changes in behaviour: a retail customer who suddenly begins making large business-like transfers, or a dormant company that activates with a burst of cross-border payments.



**Corridor detection** identifies geographic flow patterns. Are funds moving through unusual jurisdictions? Is there a sudden shift in the geographic corridor of a customer's transactions, from domestic to a high-risk third country? Is the rate of change in geographic flow accelerating, suggesting a gradual ramp-up to a high-risk jurisdiction?



**Flow detection** traces end-to-end fund flows across entities. Where does money that enters the system at one point eventually end up? Can the system identify a chain of five transfers across four entities that ultimately moves EUR 50,000 from a cash deposit to a luxury goods purchase?



The institutional installation also collects and correlates signals in real-time as transactions arrive. An ATM withdrawal in Rotterdam at 14:00, combined with an ATM withdrawal in Utrecht at 14:30 by the same customer, combined with a federation warning from a partner bank that arrived at 13:45: the engine sees all three signals within seconds and fires the alert while the pattern is still forming.



At validated performance levels, the institutional installation processes 500,000 entities in under 2 seconds on a single GPU, with over 150 million policy evaluations per second. This is not batch processing measured in hours. It is continuous monitoring measured in seconds.



The difference this makes is concrete. In the mule network scenario from Section 2: the batch system generates an alert on Wednesday morning, two days after the first withdrawal. The real-time system generates an alert on Monday at 15:01, ninety minutes after the first withdrawal. Same crime. Same data. Same detection rules. The only difference is when the engine processes the transaction.







### Layer 2: Federation — Cross-Bank Detection Without Data Sharing



The federation layer is where the architecture addresses the most fundamental limitation of current AML systems: single-institution blindness.



Two banks cannot simply share their customer databases. Privacy regulation (GDPR in Europe, comparable frameworks elsewhere) prohibits it. And they should not want to. A bank's customer data is both commercially sensitive and legally protected.



The challenge is to detect criminal networks that span multiple banks without any bank revealing its customers to any other bank. No jurisdiction has achieved automated cross-institutional detection at scale. The Dutch TMNL initiative, backed by five major banks, was wound down in July 2024 after being found incompatible with the EU's AMLR. The Nordic KYC utility Invidem, founded by six banks in 2019, shut down in April 2023 after spending approximately EUR 60 million. The UK's Joint Money Laundering Intelligence Taskforce (JMLIT) operates under significant legal and operational constraints on data sharing. Australia's Fintel Alliance relies on voluntary participation. Singapore's COSMIC platform, launched in April 2024, is the most promising current attempt but remains limited to six banks and three specific risk areas.



These initiatives share a common architectural weakness. They relied on sending disguised customer data to a central organisation. This approach has two problems. First, the disguise (converting a national identifier to a scrambled code using a technique called hashing) can be reversed: any country's identifier space is finite. The Dutch social security number space contains approximately 20 million values. The UK's National Insurance number registry holds over 90 million. Scrambling all of them produces a reverse lookup table that breaks the disguise. Second, centralisation creates a single point of failure. If the central organisation's legal basis is challenged (as happened with TMNL), the entire system collapses.



The F1 Engine uses a different approach. Two banks discover which customers they share without either bank revealing its full customer list. Each bank takes its list of customer identifiers (like social security numbers or national insurance numbers) and transforms them into mathematical codes using advanced cryptography. These codes can be compared to find matches, but the original identifiers cannot be recovered from the codes. This is fundamentally different from the hashing approach used by previous initiatives. With hashing, an attacker who knows a country's finite identifier space can simply hash all values and build a reverse lookup table. With the cryptographic approach used by the F1 Engine, this attack does not work. There is no shortcut to reverse the transformation.



After shared customers are discovered, the banks exchange risk signals, not data. If Bank A's detection system determines that a customer's risk has increased, Bank A sends a simple message to Bank B: "This customer's risk went up. Reason: unusual incoming money." Bank B adds this information to its own assessment of that customer. Bank B never learns the details of the customer's transactions at Bank A, the identity of their counterparties, or which specific rule triggered the alert. Only the change in risk level and a general reason category.



This happens in pairs. In a network of five banks, each bank conducts a separate, private exchange with each of the other four banks. No bank sees the full picture. No central organisation holds all the data. The detection of a criminal network spanning three banks emerges from the combination of local decisions at each bank, informed by risk signals from direct partners. Each bank sees one piece. The picture forms without anyone holding the full image.



For regulators reviewing this architecture: the privacy guarantee is not a claim. It is a mathematical property of the protocol. Each exchange between two banks reveals only the customers they share and numerical risk scores. The European Data Protection Supervisor's test for whether data counts as truly anonymised is satisfied with stronger margins than any approach based on hashing identifiers.



Each risk signal carries a category label explaining why the score changed (for example: "unusual inbound flow pattern" or "structuring behaviour detected"). The receiving bank can verify, using the cryptographic audit trail, that the signal was computed according to mutually agreed policies. This is not a black-box score passing between banks. It is a verifiable, auditable, explainable signal.



The federation does not require every bank in the country to participate. It operates between pairs of banks. Two banks with a legal agreement can begin exchanging risk signals immediately. The detection improves with each additional bank that joins, but it produces results from the very first pair. The legal framework for this type of information sharing between banks is being developed under AMLR Article 75. The F1 Engine provides the technical mechanism that this legal framework requires.



### Layer 3: Regulatory Interface — Supervisory Access Without Data Exposure



The final layer provides the interface between the detection system and regulatory supervisors. Automated generation of Suspicious Activity Reports from detection results. A complete audit trail that allows supervisors to verify that a detection decision was computed correctly without accessing the underlying customer data. Cryptographic provenance that proves which policies were evaluated, on which data, at which time, without revealing the data itself.



This layer directly addresses AMLA Article 75's requirement for cross-institutional information sharing mechanisms while maintaining data protection obligations. The federation protocol described in Layer 2, combined with a policy-based access control system that governs who can see what at each institutional boundary, provides the technical infrastructure that Article 75 requires.



## 4. Three Use Cases for Real-Time Detection



The architectural shift from batch to real-time creates three distinct detection capabilities, each with different regulatory frameworks and deployment contexts.



### Use Case 1: Real-Time Institutional Transaction Monitoring (All Jurisdictions)



This is the core capability and the most immediate market opportunity. It applies in every jurisdiction where AML monitoring is mandated, which is effectively every jurisdiction.



The use case is straightforward: replace the overnight batch processing cycle with continuous real-time monitoring. Every transaction is analysed the moment it enters the bank's system. Alerts fire within seconds, not the next morning. The analyst sees patterns forming in real-time instead of reviewing historical records.



No legal barriers exist for this use case. Every bank is already required to monitor transactions. No regulation specifies that monitoring must happen overnight. The shift from batch to real-time is an operational improvement within existing legal frameworks. The bank is doing the same thing (monitoring transactions against detection rules) at a different speed (seconds instead of hours).



The practical impact: alerts that previously arrived 24 to 48 hours after the crime now arrive within minutes. The analyst can act while the pattern is still forming. Account freezes, enhanced monitoring, and investigative actions happen on the same day as the suspicious activity, not two days later.



This use case does not require edge devices, embedded hardware, or any deployment outside the bank's data centre. A single GPU in the bank's server room replaces the batch processing cluster. The ROI is immediate: faster detection, fewer missed patterns, and lower infrastructure cost.



### Use Case 2: Real-Time Sanctions Screening at GPU Speed (All Jurisdictions)



Sanctions screening is legally mandated in every major jurisdiction. OFAC in the United States, the EU Consolidated List, the UN Sanctions List, and HM Treasury in the UK all require financial institutions to screen transactions and block payments involving sanctioned entities before those payments are processed.



This is the one area where transaction blocking is not just permitted but required. If a payment is destined for a sanctioned individual, entity, or jurisdiction, the bank must block it. No tipping-off concerns apply because the legal basis is different: sanctions enforcement, not AML investigation.



The challenge is speed. With the rise of instant payment rails (SEPA Instant in Europe, Faster Payments in the UK, FedNow in the US), transactions settle in seconds. The sanctions screening must complete before the transaction settles. Legacy systems that screen in 200 to 500 milliseconds per transaction are under pressure. A GPU-native engine that screens the entire population against the full sanctions list in seconds provides a fundamentally different level of capability.



The F1 Engine's policy evaluation rate (over 150 million checks per second) means that a complete sanctions screen of the bank's entire customer base against all global sanctions lists can complete in the time it takes a legacy system to screen a single transaction. For banks processing millions of transactions daily through instant payment channels, this is not a performance luxury. It is a regulatory necessity.



### Use Case 3: Real-Time Payment Intervention (UK, and Emerging in EU)



In October 2024, the UK Payment Services (Amendment) Regulations 2024 came into force. This regulation explicitly permits Payment Service Providers to delay outbound payments when there are "reasonable grounds to suspect fraud or dishonesty." This is a legal framework that did not exist two years ago.



Combined with the UK's Authorised Push Payment (APP) fraud reimbursement rules (in force since October 2024), which impose a 50/50 liability split between sending and receiving PSPs, UK banks now have both the legal authority and the financial incentive to intervene in suspicious payments before they are processed.



The UK government's Fraud Strategy 2026-2029, published in March 2026, goes further: a new Online Crime Centre launches in April 2026, bringing together police, banks, mobile networks, and technology firms for real-time intelligence sharing. The FCA has stated that it expects banks to move toward automated, risk-based monitoring capable of identifying scam activity before payments are executed.



This creates a specific market for real-time payment intervention that does not yet exist in most EU jurisdictions. Across the EU, tipping-off provisions under AMLD Article 39 (implemented in the Netherlands as Wwft Article 23, and similarly in each Member State) prohibit banks from declining transactions based on AML suspicion. But the UK has carved out an exception for fraud and dishonesty. And the EU Instant Payments Regulation (2024/886), which entered into force in April 2024, is pushing EU jurisdictions toward similar real-time screening requirements for instant payments.



For this use case, the F1 Engine provides the real-time risk assessment that the bank needs to decide, within milliseconds, whether to delay a payment for further review. The federation layer adds cross-institutional intelligence: if a partner bank has flagged the recipient's network, that signal is available at the moment the sending bank processes the payment. The decision to hold the payment is made by the bank's existing compliance framework. The F1 Engine provides the intelligence that makes the decision possible in real-time.



This use case is currently UK-specific but the regulatory direction across Europe suggests it will expand. Banks that build the technical capability now will be prepared when the legal framework catches up.



## 5. Why This Requires a GPU



Everything described in the previous sections is theoretically possible on conventional computing infrastructure. The encrypted customer matching, the risk score sharing, the five-layer detection system, all of it could be implemented on standard servers.



It would take hours. Or days.



The customer matching process for a population of 1.5 million customers involves performing a complex mathematical operation for every customer at each bank. On a conventional server processor, which handles these operations one at a time, this takes hours per bank pair. For five banks conducting ten separate exchanges, the total processing time exceeds what is practical within a monitoring cycle.



The risk analysis algorithm must trace the connections between millions of customers and tens of millions of transactions. On a processor that handles these connections one at a time, this analysis alone consumes the available monitoring window.



The policy engine must check 123 compliance rules against every customer in the bank's population. On a processor checking one customer at a time, half a million customers multiplied by 123 rules is simply too much work to complete in a reasonable timeframe.



A Graphics Processing Unit, or GPU, solves this by doing thousands of these operations at the same time instead of one after another. The same work that takes hours on a conventional processor completes in seconds on a GPU, because the GPU performs tens of thousands of calculations simultaneously.



This is not a performance upgrade. It is an architectural requirement. Without GPU-native computation, real-time continuous monitoring is theoretically interesting but impossible to operate in practice. The cross-bank matching takes too long. The relationship analysis takes too long. The policy checks take too long.



The F1 Engine is built from the ground up for GPU execution. Not a conventional application with a GPU-accelerated add-on. Everything, from the cryptographic matching between banks through to the compliance policy checks and the risk analysis, runs natively on the GPU. This comprises 396,000 lines of C++ and CUDA code with 493 GPU kernels.



This is also why no existing AML vendor can replicate this approach by adding a GPU to their existing platform. Their architectures are fundamentally CPU-based. The data structures, the algorithms, the execution model are all designed for sequential processing. Adding a GPU to a CPU-based system is like adding a jet engine to a bicycle. The frame cannot support it.



Building a GPU-native AML engine from scratch requires simultaneous expertise in three domains: GPU systems engineering, cryptographic protocol design, and financial crime compliance. These skills rarely coexist in the same team. The F1 Engine was built over 18 months by a single engineer with 18 years of compliance experience at Tier 1 institutions and deep GPU systems knowledge.



## 6. Validation: How Do You Know the Detection Works?



Any detection system is only as good as the data it is tested against. A system that catches every criminal in a controlled test but fails against real criminal patterns provides false confidence.



The F1 Engine includes a simulation environment (Financial Crime Network Simulator) that generates synthetic banking populations with embedded criminal networks. The simulator produces ground truth: it knows exactly which entities are criminals, which network they belong to, and which typology they use. This enables closed-loop testing. Run a simulation, see the scorecard, verify that every criminal was detected.



But synthetic data has an obvious weakness: it might not reflect reality. If the synthetic transactions do not resemble real bank transactions, the detection thresholds calibrated against synthetic data will fail in production.



To address this, the simulator's transaction distributions are calibrated against publicly available banking statistics. The calibration framework is jurisdiction-agnostic: it works with any market where aggregate payment data is published. The current reference implementation uses Dutch data. The Dutch Central Bank (De Nederlandsche Bank, DNB) publishes aggregate payment data: 6.7 billion card payments totalling EUR 198 billion in 2024, with an average card transaction of approximately EUR 30. The Dutch statistics office (CBS) publishes household income and expenditure data. The Dutch Payments Association (Betaalvereniging Nederland) publishes transaction mix data by channel and type. Equivalent data is published by the Bank of England, the Federal Reserve, the ECB, and most central banks in FATF member jurisdictions.



The simulator's output is validated against these reference distributions. If the average retail transaction in the simulation deviates significantly from the published average for the target jurisdiction, the simulator is miscalibrated and the detection thresholds are unreliable. This validation runs automatically before any threshold calibration.



Eight criminal typologies are supported: trade-based laundering, mule networks, professional laundering, smurfing and structuring, correspondent banking abuse, dormant account exploitation, business front operations, and property market laundering. Each typology can be configured at difficulty levels 1 through 5, from amateur operations with obvious patterns to professional operations designed to evade detection.



The engine also includes an Adversarial Threshold Optimizer that automatically discovers optimal detection thresholds. Instead of a compliance officer manually deciding that "3 transactions per day is suspicious," the optimizer evaluates millions of threshold configurations against the simulated population and produces a mathematically verified set of optimal trade-offs between detection rate and false positive rate. The compliance officer does not guess. They choose a point on a curve that has been validated against adversarial criminal behaviour across multiple population seeds, difficulty levels, and economic conditions. No other AML system provides this capability.



At validated performance levels: in simulation testing, the engine finds every single criminal that was planted in the synthetic population. Zero missed criminals. In detection terminology, this is called "100% recall," meaning none of the known bad actors slipped through.



An important caveat: this result is measured against synthetic populations where the system knows exactly who the criminals are, because the simulator created them. In the real world, criminals are adaptive. They change their behaviour to avoid detection. Production detection rates will be lower than simulation results. This is true for every detection system ever built. The simulator's purpose is not to claim perfection. It is to provide a controlled environment for continuous calibration: run the simulation, measure what was missed, adjust the detection thresholds, run again. This feedback loop does not exist in systems that rely solely on production data, where you never know what you missed.



## 7. Regulatory Alignment



The architecture is not built in anticipation of regulation. It is built to implement regulation that is already in force.



**AMLR Article 75** mandates mechanisms for cross-institutional information sharing. The federation protocol (Layer 2) provides exactly this mechanism, with privacy protection that exceeds the requirements of traditional approaches.



**AMLA** has been operational since July 2025 in Frankfurt. In January 2026, all AML responsibilities transferred from the European Banking Authority to AMLA. AMLA's 2026-2028 work programme, published in February 2026, focuses on supervisory convergence and common approaches. The unified policy language in the F1 Engine enables identical policies to be written once and evaluated identically across all institutions, ensuring consistent detection regardless of which bank processes a transaction. This is precisely the convergence that AMLA is mandating.



**AMLD6** requires enhanced due diligence and beneficial ownership identification. The structural detection layer identifies shell company structures and complex ownership networks, and the federation layer reveals cross-institutional ownership patterns that no single bank can see alone.



**GDPR and European data protection guidance** require that data processing minimises exposure. The federation protocol exchanges only mathematical codes (not customer names or account numbers) and numerical risk scores (not transaction details). The access control system restricts what each operator can see based on their role. The raw mathematical outputs from the cross-bank matching process are never shown to human analysts.



**The EU AI Act** requires that AI systems used in high-impact decisions can be explained and overseen by humans. The Operator Console provides a human review step for every alert. Compliance policies are written in plain language that a compliance officer can read and understand, not hidden inside a machine learning model. Every detection decision carries a full audit trail showing exactly which rules fired and why.



**DORA** (Digital Operational Resilience Act) requires operational resilience for critical financial infrastructure. The system runs entirely on-premise, within the bank's own network. There is no cloud dependency.



**UK Payment Services (Amendment) Regulations 2024** permit payment delays for suspected fraud. The real-time detection capability (Use Case 3 in Section 4) provides the risk assessment required for banks to exercise this authority within the legally mandated timeframe.



**EU Instant Payments Regulation (2024/886)** requires sanctions screening for instant payments without delay. The GPU-native screening capability (Use Case 2 in Section 4) provides the processing speed required to screen transactions before settlement.



## 8. The Hidden Superpower: An ESG Architecture by Design



In 2026, a platform's ESG profile is often as important to a bank's board as its detection rate. Every major European bank publishes an annual ESG report. The environmental section covers carbon footprint. The social section covers financial inclusion. The governance section covers transparency and auditability. Most banks struggle to fill the governance section with anything more substantive than "we comply with applicable regulations."



The ZQUAS architecture is, almost by accident, an ESG powerhouse. Not because it was designed for ESG reporting, but because the engineering decisions that make it effective for detection also happen to produce exceptional ESG outcomes.



### Environmental: The Joule-Per-Transaction Metric



Traditional AML systems are energy-intensive. They require large data centres running 24 hours a day, seven days a week. Servers store years of historical transaction data. Batch jobs churn through millions of records every night. The CPU clusters that power these systems are optimised for flexibility, not efficiency. They can do anything, but they do everything at high energy cost.



A GPU is fundamentally different. It is designed for parallel computation. A useful analogy: a CPU is like a fleet of high-speed courier cars, each carrying one package at a time. A GPU is like a freight train, carrying ten thousand packages simultaneously. The energy cost per package is dramatically lower.



In terms of computational work per joule of energy consumed, a GPU-native engine processes the same volume of data with roughly 60 to 80 percent less energy than an equivalent CPU cluster. For a Tier 1 bank processing millions of transactions daily, this is not a rounding error. It is a measurable reduction in the IT carbon footprint of compliance operations.



The portability story reinforces this. This paper describes running the full detection stack on a 2017-era laptop purchased for EUR 299. This is a direct contribution to the circular economy. Instead of requiring banks to purchase new server-grade hardware every three years (generating electronic waste), the architecture allows institutions to repurpose existing or older GPU hardware for high-stakes compliance work. A Quadro P2000 that would otherwise be recycled or discarded becomes a functional AML installation.



When a bank's sustainability team asks "what is our compliance infrastructure's carbon footprint," an institution running ZQUAS has a concrete answer: fewer servers, lower energy consumption, repurposed hardware, continuous processing that eliminates the need for nightly batch compute spikes.



### Social: Financial Inclusion and Victim Protection



The social impact of AML is systematically overlooked. Traditional rule-based systems produce false positive rates of 95% or higher. For every 100 alerts generated, 95 are innocent customers flagged incorrectly.



The downstream consequence is de-risking. When a bank's monitoring system is inaccurate, the bank responds by closing the accounts of entire categories of customers deemed too expensive to monitor. Students, recent immigrants, small businesses in "high-risk" postcodes, money transfer operators serving diaspora communities. These groups lose access to the banking system not because they are criminals, but because the detection technology cannot distinguish them from criminals efficiently.



A system that finds every criminal in a test population and simultaneously reduces false alarms directly addresses this problem. By detecting actual criminals with precision, the system eliminates the pressure to de-risk entire populations. Innocent people stay in the financial system. The bank meets its compliance obligations without punishing its customers for the limitations of its technology.



There is a second social dimension. Money laundering networks exploit vulnerable people as mules, often students or recent immigrants recruited through social media with promises of easy money. These individuals face criminal prosecution when the network is eventually discovered. By detecting and disrupting mule networks in real-time, the system breaks the economic model that criminal organisations use to recruit vulnerable individuals. Faster detection means fewer people are recruited into criminal activity before the network is dismantled.



### Governance: Mathematical Transparency Instead of Black-Box AI



Current AI-based AML systems are, from a governance perspective, opaque. A machine learning model flags a customer. The compliance officer asks: why? The answer is a probability score derived from a neural network with millions of parameters. The model cannot explain its reasoning in terms that a regulator, a court, or an audit committee can verify.



This is a governance problem that is about to become a legal problem. The EU AI Act requires explainability for AI systems used in high-impact decisions. AML detection affects people's access to financial services. A system that cannot explain why it flagged an individual may not survive regulatory scrutiny under the AI Act.



The ZQUAS architecture takes a different approach. The federation protocol uses elliptic curve cryptography, not probabilistic AI, for its cross-institutional detection. The bank can prove to a regulator, mathematically, exactly why a risk score changed, which policies evaluated, which data was processed, at what time, without ever exposing private customer data. The audit trail is not a log file. It is a cryptographic proof.



The compliance policies themselves are written in a human-readable policy language (CPL). A compliance officer can read the policy that triggered an alert and understand, in plain language, what condition was met. This is not possible with a machine learning model. The same policy runs identically across the entire architecture, creating a single version of truth.







## 9. The Numbers



Claims of architectural innovation require evidence. The F1 Engine is a measured engineering artefact, not a design document.



**Codebase:** 396,000 lines of C++ and CUDA across 493 GPU kernels. 222,000 lines of test code. 618,000 lines total. One codebase, three deployment targets: the banking detection engine, the AI inference layer, and the cross-bank federation layer. Every kernel is a __global__ function in a .cu file. No CPU fallback. 12,342 automated tests.



**Performance:** 500,000 customers processed in under 2 seconds end-to-end. Over 150 million policy checks per second. A single cross-bank matching round for 100,000 customers: under 10 seconds. Time from detection to alert: under 10 milliseconds. All numbers measured on a single GPU.



**Portability:** The minimum GPU requirement is a 2017-era NVIDIA card with 4 gigabytes of memory. The engine has been validated on a Quadro P2000 purchased for EUR 299: 1,000 entities, 21 million transactions, 123 policies, every criminal found, on hardware that costs less than a restaurant dinner. The same binary, unmodified, runs on an RTX 5090 with 32 gigabytes of memory processing 100,000 entities.



**Security hardening:** Every binary is built with defence-grade protections against tampering, memory attacks, and reverse engineering. The same level of hardening applied to military and intelligence software.



## 10. From Data Centre to Laptop



On 22 March 2026, the F1 Engine was deployed to an HP ZBook 15 G5 purchased on a Dutch classifieds site for EUR 299. The laptop was manufactured in 2018. It has a six-core Xeon processor, 32 gigabytes of RAM, and an NVIDIA Quadro P2000 with 4 gigabytes of GPU memory.



From a bare Windows installation to a running detection platform with a full Operator Console accessible in the web browser: one day. One person. No external dependencies, no cloud services, no installation consultants.



The engine ran a simulation: 1,000 entities across five Dutch banks, with embedded criminal networks. Detection result: every criminal found. Zero missed. The Operator Console displayed the full scorecard, the criminal network structure, alert details, and the investigative workflow. On a laptop that costs less than a dinner at a Michelin-starred restaurant.



This portability demonstrates that the minimum hardware threshold for institutional-grade AML detection has dropped to commodity hardware. A regional bank, a credit union, a payment service provider, or a crypto exchange can deploy the same detection capability that a Tier 1 bank runs in its data centre. The barrier to entry is no longer technology. It is decision.



## 11. Future Vision: The Federated Financial Crime Network



The architecture described in this paper is designed for institutional deployment: a GPU in the bank's data centre, connected to partner banks through the federation protocol. This is what can be built and deployed today, within existing legal and regulatory frameworks.



But the architecture's portability points toward a future that extends beyond banks.



Consider a world in which every entity that touches money runs the same detection engine. Not just banks. Payment service providers. Electronic money institutions. Crypto asset service providers. Central securities depositories. Insurance companies. Real estate brokerages. Any entity required by regulation to monitor for financial crime.



The federation protocol operates between pairs of institutions. It does not care whether those institutions are banks. Two payment processors can run the same bilateral exchange. A bank and a crypto exchange can discover shared customers using the same cryptographic protocol. A real estate brokerage and a bank can exchange risk signals about a property buyer whose funds originated from a flagged network.



This is not science fiction. The EU's Anti-Money Laundering Regulation already extends AML obligations to crypto asset service providers (under MiCA), to payment institutions, to electronic money institutions. AMLA's direct supervision mandate covers not just banks but any financial institution deemed high-risk. The regulatory scope is expanding. The technical infrastructure should match it.



In this future, the federated network becomes a detection fabric that spans the entire financial system. A drug trafficking organisation deposits cash at a payment processor. The cash moves through a crypto exchange. The crypto is converted to fiat at a second exchange. The fiat is used to purchase a property through a real estate broker. At every step, the entity processing the transaction runs the same detection engine. At every step, risk signals propagate through the federation. The chain is visible not because any single institution sees the full picture, but because the federation protocol connects the dots across every institution the money touches.







The edge deployment capability makes this feasible. The engine runs on a EUR 299 laptop. It runs on embedded hardware. It can run at a payment terminal manufacturer's gateway, at a crypto exchange's processing node, at a property registration office's server. The hardware threshold is low enough that every obliged entity, not just the largest banks, can participate.



And at the physical edge: ATMs, merchant terminals, and payment gateways could eventually run detection intelligence directly. Today, legal frameworks in most jurisdictions prevent ATMs from declining cash withdrawals based on AML risk (tipping-off provisions under AMLD Article 39 and its national implementations, such as Wwft Article 23 in the Netherlands, prohibit this). But the UK's Payment Services (Amendment) Regulations 2024 show that legal frameworks can evolve. As real-time intervention becomes legally permissible in more jurisdictions, the hardware and software to support it already exist. When the law catches up, the technology will be ready.



The question is not whether this future is technically possible. The architecture already supports it. The question is whether the regulatory framework and institutional willingness will follow.



## 12. Regulatory Alignment Map



The following table maps the ZQUAS architecture to the specific regulatory requirements it implements.






| 
                    Regulation and Requirement | 
                    ZQUAS Capability 
| 
                    **AMLR Article 75:** Cross-institutional sharing | 
                    Federation protocol with bilateral ECDH-PSI and scalar risk deltas 
| 
                    **AMLA Direct Supervision (2028):** Common detection standards | 
                    Unified CPL policy language evaluated identically across institutions 
| 
                    **AMLD6:** Enhanced due diligence and beneficial ownership | 
                    Structural detection layer and cross-institutional ownership discovery 
| 
                    **GDPR:** Data minimisation and pseudonymisation | 
                    Cryptographic protocol exchanges only intersection membership and numerical scores 
| 
                    **EU AI Act:** Explainability for high-impact AI | 
                    Human-readable CPL policies with cryptographic audit trail, no black-box models 
| 
                    **DORA:** Operational resilience | 
                    Fully on-premise, no cloud dependency, continuous operation 
| 
                    **UK PSA 2024:** Payment delay for suspected fraud | 
                    Real-time risk assessment for payment intervention decisions 
| 
                    **EU Instant Payments Reg (2024/886):** Real-time sanctions screening | 
                    GPU-native screening at 150M+ checks per second 
| 
                    **MiCA:** AML obligations for crypto asset service providers | 
                    Same engine deployable to crypto exchanges, federation-compatible 
## 13. Conclusion



Financial crime does not operate at the institutional core on a 24-hour cycle. It operates continuously, across institutional boundaries, wherever money moves. An effective detection architecture must operate at the same speed, with the same scope, informed by intelligence from across the financial system.



The anti-money laundering industry has spent two decades optimising batch processing. The result is 13,000 full-time employees, 530,000 annual reports, and no measurable effectiveness. We propose a different approach: detect the moment each transaction occurs, informed by cross-institutional intelligence, across every institution the crime touches. With lower energy consumption, greater fairness, and mathematical transparency that no black-box AI system can match.



The technology exists. The regulatory mandate is not arriving. It is here. AMLA is operational. The 2026-2028 work programme is published. Direct supervision begins in 2028. The only question is which institutions will be ready.



*ZQUAS. Because monitoring yesterday's transactions tomorrow is not compliance. It is record-keeping.*



**Contact:** Danny de Gier | danny@zquas.ai | zquas.ai



*© June 2026 ZQUAS. All rights reserved. Implementation details and protocol specifications are proprietary.*

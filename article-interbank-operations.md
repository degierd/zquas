# What Running a Multi-Bank Monitoring Network Actually Looks Like

> The architecture papers write themselves. The hard part is operations. How do banks join? Who sets the rules? What happens when one bank's policy change affects another bank's alerts?

Source: https://zquas.ai/article-interbank-operations.html
Site: https://zquas.ai

---
[← Articles](articles.html)
        January 2026 · Banks · 9 min read


# What Running a Multi-Bank Monitoring Network Actually Looks Like



The architecture papers write themselves. The hard part is operations. How do banks join? Who sets the rules? What happens when one bank's policy change affects another bank's alerts? These are the questions that determine whether a network works or collapses.






Cross-institutional monitoring is easy to describe on a whitepaper. Multiple banks share data. Analytics detect patterns invisible to individual institutions. Criminal networks are exposed. Everyone benefits.



*A note on scope: the operational model described in this article reflects the designed architecture. The MPC protocol and GPU-accelerated cryptographic components have been implemented and validated in controlled testing. The architecture supports multi-installation deployment across separate institutional infrastructure, with each bank operating an independent installation connected via bilateral MPC sessions.*



The reality is messier. Several European initiatives have demonstrated both the detection value and the operational complexity of multi-bank monitoring. The detection works. The operations are where things break down.



Having spent 18 years inside the compliance functions of banks that participate in these kinds of initiatives, I can tell you that the technical architecture is maybe 30% of the challenge. The other 70% is governance, operations, and the uncomfortable questions that emerge when independent institutions try to collaborate without giving up autonomy.



This article addresses those questions directly, because any serious multi-bank monitoring architecture has to answer them.



## How Banks Join the Network



In a centralised model, joining is straightforward. The bank signs a data-sharing agreement, connects its data feeds to the central platform, and starts sending transactions. The central operator handles the analytics.



In a privacy-preserving model, joining looks different. The bank deploys a node on its own infrastructure. The node runs the compliance engine locally, processing the bank's own data against its own policy set. No data leaves the bank.



The cross-institutional capability activates when the bank's node establishes an MPC connection with another bank's node. This connection doesn't transmit transaction data. It enables cryptographic comparison: the two nodes can jointly evaluate whether shared counterparties exhibit suspicious cross-bank patterns, without either node revealing its underlying transactions.



The onboarding process for a new bank involves: deploying the node (on-premise or private cloud), configuring the local policy set, running a validation period against historical data to baseline detection quality, and then activating MPC connections to existing network members.



Each step is under the bank's control. The bank decides when to go live. The bank decides which other institutions to connect with. The bank can disconnect at any time without affecting its local monitoring capability.



This matters because the biggest operational blocker in multi-bank initiatives isn't technology. It's autonomy. Banks don't want to be locked into a consortium where another bank's decisions affect their compliance programme. A privacy-preserving architecture preserves autonomy by design.



## Who Sets the Rules



This is the question that creates the most friction in any multi-bank initiative. If five banks share a monitoring platform, whose rules apply?



In a centralised model, there are limited options. Either the consortium develops a shared rule set (which means compromise and lowest-common-denominator detection), or each bank's rules are applied centrally (which means the central operator needs access to proprietary compliance configurations). Both options have problems.



A shared rule set dilutes detection. Bank A has sophisticated correspondent banking rules developed over years. Bank B has minimal correspondent banking exposure and doesn't maintain those rules. The shared set either excludes Bank A's advanced rules (reducing detection) or includes them (creating noise for Bank B).



Per-bank rules in a central platform create confidentiality issues. A bank's monitoring configuration reveals its risk appetite, its business strategy, and the specific threats it's focused on. Most banks consider this information competitive and confidential. Sharing it with a central operator, even under NDA, is uncomfortable.



In a privacy-preserving model, each bank runs its own rules locally. There is no shared rule set. There is no central operator seeing anyone's configuration. The MPC layer computes cross-institutional risk indicators without knowing what rules either bank is running.



The result is that Bank A keeps its sophisticated correspondent banking rules. Bank B keeps its simpler configuration. Both benefit from cross-institutional detection without either bank compromising its proprietary monitoring approach.



## What Happens When Banks Disagree



In any collaborative monitoring arrangement, banks will occasionally disagree about risk assessments. Bank A's node identifies a counterparty as high-risk. Bank B's node doesn't. The MPC computation flags the shared counterparty as warranting further investigation. Now what?



In a centralised model, this disagreement is visible to the central operator, which creates complications. Does the operator tell Bank B that Bank A considers the counterparty high-risk? That could constitute tipping off. Does the operator suppress the signal? That could undermine detection.



In a privacy-preserving model, the disagreement is handled cleanly. The MPC output is a risk indicator, not an explanation. Bank A receives a signal that the shared counterparty shows elevated cross-institutional risk. Bank B receives the same signal. Neither bank knows the other's risk assessment. Neither bank knows which specific rules triggered at the other institution.



Each bank independently decides what to do with the signal. Bank A might escalate the case. Bank B might conduct enhanced due diligence. They make these decisions independently, based on their own policies and their own information, supplemented by the cross-institutional risk indicator.



This preserves the regulatory principle that each bank is independently responsible for its own compliance decisions. The network provides intelligence. The bank makes decisions. The two are clearly separated.



## The Policy Change Problem



Here's a scenario that breaks centralised monitoring architectures. Bank A changes its monitoring rules on Tuesday. The change adjusts thresholds for cross-border wire transfers. On Wednesday, the centralised platform generates a spike in alerts involving Bank A's customers.



What happened? Did the new rules detect genuine suspicious activity that the old rules missed? Or did the new rules inadvertently create false positives that cascade through the shared analytics?



In a centralised model, answering this question requires understanding Bank A's rule change, which the other banks and the central operator may not have visibility into. The operational response involves calls between compliance teams, analysis of the alert spike, and usually a temporary suppression of the affected alerts until the cause is understood. This can take days.



In a privacy-preserving model, Bank A's rule change only affects Bank A's local monitoring. The MPC computation is between nodes, not within them. Bank A's local alerts change because of the rule change. But the cross-institutional risk indicators are based on the MPC output, which depends on both banks' data, not on either bank's rules.



If Bank A's rule change causes Bank A to reclassify a counterparty's risk, that might affect the inputs to the next MPC computation. But the effect is bounded. It appears as a change in Bank A's risk assessment of the shared counterparty, not as a cascade through the entire network's alert pipeline.



The practical result: one bank can update its rules without destabilising the entire network. Policy changes are local. Cross-institutional effects are contained.



## Governance Without a Central Authority



Multi-bank monitoring initiatives typically establish a governance body: a steering committee of representatives from each participating bank, supported by a programme management office. This body makes decisions about shared rules, data standards, privacy controls, and dispute resolution.



These governance bodies are necessary in centralised models because someone has to manage the shared infrastructure. They're also expensive, slow, and politically fraught. Every decision requires consensus among competitors. Minor technical changes become multi-month negotiations.



A privacy-preserving network requires less central governance because there's less to govern. There's no shared rule set to negotiate. There's no central data platform to manage. There's no single operator with visibility into everyone's data.



What does need governance is: the MPC protocol version (all nodes must run compatible versions), the network membership (who can join and under what conditions), and the risk indicator format (what the MPC output looks like and how it's interpreted).



These are narrower, more technical decisions than "what rules should we all run." They can be managed with lighter governance structures. A technical standards body rather than a strategic steering committee.



## Regulatory Reporting in a Multi-Bank Network



When the cross-institutional monitoring identifies a potentially suspicious pattern, who files the SAR?



In a centralised model, this question is complicated. The central operator identifies the pattern. Multiple banks are involved. Each bank has its own regulatory reporting obligations. The central operator typically sends the signal back to each bank, and each bank independently decides whether to file. But the banks don't know what the other banks filed, creating potential inconsistency in the regulatory reporting.



In a privacy-preserving model, the process is similar in outcome but cleaner in execution. Each bank receives the same cross-institutional risk indicator. Each bank investigates independently using its own data and its own local monitoring results. Each bank makes its own filing decision independently.



The key difference is that the risk indicator is the same for all banks, so they're all working from the same intelligence. But they're investigating independently with their own data, which preserves the principle that each bank is responsible for its own compliance decisions.



If regulators want to understand the cross-institutional picture, the proof bundles from each bank's local monitoring can be verified independently. The MPC computation itself produces a separate attestation that can be verified without accessing either bank's data.



## Scaling the Network



The operational complexity of a multi-bank network depends heavily on how complexity scales with network size.



In a centralised model, complexity grows with every member. Each new bank adds data feeds, integration points, rule interactions, and governance stakeholders. Networks with five members are manageable. Networks with twenty become unwieldy. Networks with fifty are impractical.



In a privacy-preserving model, the MPC computation scales differently. Each node connects to other nodes through bilateral MPC sessions. The complexity per node grows linearly with the number of connections, not exponentially with network size. And each bank can choose which other banks to connect with, so a bank joining the network doesn't automatically create connections to every existing member.



This means the network can grow incrementally. Two banks start. A third joins and connects to both. A fourth joins and connects to two of the three. The network topology evolves organically based on bilateral decisions, not top-down consortium architecture.



For practical deployment, this is important. Getting five banks to agree to anything simultaneously is a multi-year project. Getting two banks to agree to a bilateral MPC connection is a quarterly conversation. The network grows through bilateral adoption, not consortium consensus.



## The Operational Bottom Line



The history of multi-bank monitoring in Europe shows that the detection value is real but the operational model determines whether the initiative survives.



Centralised models concentrate governance burden, create privacy exposure, and scale poorly. Privacy-preserving models distribute governance, eliminate privacy exposure, and scale incrementally.



The question isn't whether banks should collaborate on detection. The question is whether the collaboration architecture can survive contact with operational reality. That means: autonomous rule management, contained policy change effects, lightweight governance, independent regulatory reporting, and bilateral network growth.



The technology to support this operational model exists. The remaining challenge is getting the first two banks to start.


            Danny de Gier

                Founder, ZQUAS. 18+ years in financial crime compliance at Tier-1 banks and fintechs.
                Professional Postgraduate Diploma in Financial Crime Compliance (ICA / University of Manchester).

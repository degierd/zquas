# Privacy-Preserving Detection Under AMLR

> The EU AMLR creates a catch-22 for cross-institutional detection. Privacy-preserving computation offers a way through it.

Source: https://zquas.ai/article-privacy-preserving-amlr.html
Site: https://zquas.ai

---
[← Articles](articles.html)
        January 2026 · Regulators · 8 min read


# Privacy-Preserving Detection Under AMLR



The EU Anti-Money Laundering Regulation creates a catch-22. You can only share data about customers you've already identified as high-risk. But you need shared data to identify them in the first place. There is a way through this.






            The AMLR, effective mid-2027, does something that previous AML directives didn't. It explicitly provides a legal basis for inter-bank cooperation in detecting financial crime. That's the good news.




            The constraint is in the detail. Data sharing between institutions is restricted to customers who are already classified as high-risk, or where additional information is needed to determine if they should be. You can't pool transaction data across banks to go fishing for suspicious patterns. You need a reason first.




            This makes sense from a rights perspective. Mass financial surveillance, even with good intentions, is incompatible with the privacy protections that EU citizens are entitled to. The AMLR reflects that judgment clearly.




            But it creates a real operational problem for detection.




## The Detection Paradox



            Money laundering networks work precisely because they spread activity across multiple institutions. A criminal doesn't use one bank. They use four or five. Each bank sees a fragment that looks unremarkable in isolation. The suspicious pattern only becomes visible when you look across the network.




            Under AMLR, Bank A can share data about a customer with Bank B if the customer is already flagged as high-risk. But how does Bank A know the customer is high-risk if the evidence only exists in the combination of Bank A's data with Bank B's data?




            This isn't a hypothetical edge case. It's the central challenge in cross-institutional AML detection. Joint monitoring initiatives across Europe have run into exactly this problem. The detection value comes from combining data, but the legal framework restricts combination to cases where you already have evidence. The logic is circular.




## Previous Approaches and Why They Stalled



            The most ambitious attempt to solve this was in the Netherlands, where five major banks created a joint transaction monitoring utility. The concept was straightforward: pool transaction data from all five banks, run analytics across the combined dataset, identify patterns invisible to individual institutions.




            It worked technically. The combined data revealed previously unknown criminal networks. But it also triggered serious privacy objections. A civil rights organisation representing thousands of banking customers demanded the operation stop and all collected data be destroyed. The Dutch Data Protection Authority raised concerns. And when the AMLR was finalised, the legal basis for broad-based data pooling effectively disappeared.




            The initiative wasn't shut down because it failed at detection. It was shut down because the architecture, centralising raw data from multiple institutions, couldn't be reconciled with privacy requirements.




## Computation Without Disclosure



            There is a branch of cryptography that solves exactly this problem. Secure multi-party computation, or MPC, allows multiple parties to jointly compute a result from their combined data without any party revealing its data to the others.




            In practical terms: Bank A and Bank B can determine whether a shared counterparty exhibits suspicious cross-bank patterns. They get the answer. But Bank A never sees Bank B's transactions, and Bank B never sees Bank A's. The computation happens on encrypted inputs, and only the agreed-upon output is revealed.




            This isn't new research. MPC has been studied since the 1980s. What's new is that GPU-accelerated implementations have made it fast enough for real-time transaction monitoring. The computational overhead that previously made MPC impractical for high-volume financial applications has been largely eliminated by running the cryptographic protocols on GPU hardware designed for massively parallel workloads.




## How This Works Under AMLR



            The AMLR compliance argument for MPC-based detection is straightforward.




            No raw data is shared between institutions. Each bank's transaction data stays within its own infrastructure. There is no central database. There is no data processor holding information from multiple banks. The GDPR exposure that killed centralised approaches simply doesn't exist.




            What is shared is a cryptographic computation output: a risk indicator. This output doesn't contain customer data. It contains a yes/no signal about whether further investigation is warranted. If the signal indicates elevated risk, the relevant banks can then use the AMLR's legitimate data-sharing provisions for high-risk customers. The MPC computation provides the reasonable basis for sharing, without requiring a data pool to generate that basis.




            In other words, MPC turns the AMLR catch-22 into a two-step process. Step one: cryptographic computation identifies potential risk across institutions, without data disclosure. Step two: once risk is indicated, AMLR-compliant data sharing kicks in for the specific customers flagged.




## Supervisory Verification



            For regulators, there's a separate benefit. If the compliance system produces cryptographic proof bundles for every decision, supervisory verification changes character entirely.




            Today, when an examiner reviews a bank's transaction monitoring, they're looking at log files, case management records, and policy documentation. They're trusting that the bank's description of how the system works matches how it actually works. This is a trust-based model.




            With cryptographic attestation, the examiner doesn't need to trust. Each batch of compliance decisions carries a proof: these specific policies were applied to these specific inputs and produced these specific verdicts. A standalone verification tool can confirm the proof independently. No access to the bank's systems needed. No reliance on the vendor's software.




            This doesn't replace supervisory judgment. It provides a foundation of verifiable facts on top of which judgment can be exercised. The examiner can focus on whether the policies are adequate rather than spending time confirming whether the policies were actually applied.




## What This Means for Supervisory Strategy



            The AMLR's data-sharing restrictions are sometimes characterised as a barrier to effective AML. That framing misses the opportunity. The restrictions create demand for a better architecture, one that achieves detection without mass data collection.




            MPC-based detection, combined with cryptographic verification, offers supervisors something that centralised monitoring never could: a system that is simultaneously more effective at detecting cross-institutional crime and more protective of individual privacy. These two goals stop being in tension when the architecture is designed correctly.




            For supervisory and SupTech teams evaluating new approaches, the key questions are practical. Can the system demonstrate detection efficacy on realistic data? Can it operate within AMLR constraints without legislative carve-outs? Can the proof bundles be verified independently? And can the whole thing run at the speed and scale that real-time payment rails demand?




            These are testable questions. Regulatory sandbox programmes exist to answer them.



            Danny de Gier

                Founder, ZQUAS. 18+ years in financial crime compliance at Tier-1 banks and fintechs.
                Professional Postgraduate Diploma in Financial Crime Compliance (ICA / University of Manchester).

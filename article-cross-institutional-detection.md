# Why Cross-Institutional AML Detection Requires a New Architecture

> Joint transaction monitoring initiatives have stalled across Europe. Privacy-preserving computation offers a fundamentally different approach.

Source: https://zquas.ai/article-cross-institutional-detection.html
Site: https://zquas.ai

---
[← Articles](articles.html)
        February 2026 · Analysis · 8 min read


# Why Cross-Institutional AML Detection Requires a New Architecture



Joint transaction monitoring initiatives across Europe have demonstrated both the necessity and the impossibility of centralised data pooling. The problem isn't willingness — it's architecture.






## The Detection Gap Is Real



            An estimated €16 billion in criminal money moves through the Netherlands every year. The EU-wide figure is in the hundreds of billions. Banks spend over €200 billion a year on compliance globally. And less than 1% of illicit funds actually get caught.




            The reason comes down to how the system is built. Laundering networks don't stay inside one bank. A criminal deposits cash at Bank A, moves it to a shell company at Bank B, buys property through Bank C, and brings the clean money home via Bank D. Each bank sees one unremarkable transaction. Nobody sees the chain.




            The people are good. The technology within each bank is often good too. But the architecture makes it impossible. If every institution can only monitor its own customers, cross-bank networks stay invisible. That's not a bug in the system. It is the system.




## Why Data Centralisation Failed



            The obvious answer is to pool transaction data across banks and analyse it together. Several European jurisdictions have tried this. The results tell you everything you need to know.




            The problem wasn't technical. It was legal and political. When you centralise raw transaction data from multiple banks into one place, you've built a mass surveillance tool. The Dutch Data Protection Authority said as much. The Council of State agreed. Privacy advocates and civil liberties groups objected, and they were right to. The EU's new Anti-Money Laundering Regulation (AMLR), effective mid-2027, now explicitly restricts inter-bank data sharing to pre-identified high-risk customers. That effectively kills the centralised pooling model for broad-based detection.





Here's the problem we keep running into: you need cross-bank visibility to catch the networks, but the moment you centralise the data to get that visibility, you've broken the privacy rules. And those rules exist for good reason. So the question isn't whether to centralise. It's whether there's a way to get the detection without the centralisation.





            AMLR isn't a mistake. It reflects a real democratic judgement that mass financial surveillance needs limits, even when the goal is catching criminals. Any solution that tries to get around that constraint instead of working within it is going to hit the same wall.




## A Different Architectural Premise



            Centralised monitoring assumes you need to see the data to analyse it. But that's not actually true anymore. Secure multi-party computation (MPC) and zero-knowledge proofs let you run meaningful analysis across datasets that never leave their home institutions.




            In practice, this means each bank keeps full control of its own data. No transaction records cross the perimeter. The system runs risk comparisons cryptographically. Bank A and Bank B can determine whether a shared counterparty shows suspicious patterns across both institutions, without either bank seeing the other's transactions.






| 
                    Dimension | 
                    Centralised Model | 
                    MPC-Based Model 
| 
                    **Data location** | 
                    Central pooling entity | 
                    Remains at each institution 
| 
                    **Privacy exposure** | 
                    Full transaction visibility | 
                    Zero raw data disclosure 
| 
                    **GDPR/AMLR compatibility** | 
                    Requires legislative carve-out | 
                    Compatible by construction 
| 
                    **Single point of breach** | 
                    Yes, central database | 
                    No, distributed by design 
| 
                    **Regulatory verifiability** | 
                    Trust-based audit trails | 
                    Cryptographic proof verification 
## Performance Is No Longer the Barrier



            The standard objection to MPC is that it's too slow for real-time financial applications. Five years ago, that was true. It's not anymore.




            GPU-accelerated MPC runs cryptographic comparison, oblivious sorting, and secure aggregation on modern hardware at throughput levels that work for real-time transaction monitoring. The same GPU parallelism behind AI training and high-frequency trading turns out to be well suited for privacy-preserving financial crime detection.




            Combined with GPU-native policy evaluation, a single node can process millions of compliance events per second, running the full policy set against every transaction. You don't have to choose between detection coverage and computational performance anymore.




## Verifiability Changes the Regulatory Relationship



            The part that matters most for regulators is auditability. Today, supervisors rely on log files, case management exports, and institutional self-reporting to assess whether monitoring systems actually work. That entire model runs on trust.




            A cryptographically attested architecture changes that. Every batch of compliance decisions produces a sealed evidence bundle, a proof that specific policies were applied to specific data and produced specific verdicts. A regulator can verify that proof with a standalone tool. No need to access the bank's systems. No need to trust the vendor's software. No need to see the underlying data.




            That changes how supervision works in practice. Instead of asking "show me your monitoring reports" and spending weeks reviewing them, the regulator asks for the proof bundle and gets a clear answer: valid or invalid. The guesswork goes away.




## What Comes Next



            The AMLR creates a strange situation. It restricts centralised data pooling, which pushes the industry toward privacy-preserving alternatives. But it also establishes a pan-European legal framework for inter-institutional cooperation. That combination is exactly what an MPC-based detection network needs to operate.




            The architecture has been implemented and validated in controlled testing. The regulatory framework is taking shape. And the institutional willingness is clearly there, given the years of investment in joint monitoring initiatives that ultimately couldn't clear the legal bar. What's been missing is an architecture that delivers the detection without requiring the data centralisation.




            We've built one. If you're dealing with these problems, we should talk.



            Danny de Gier

                Founder, ZQUAS. 18+ years in financial crime compliance at Tier-1 banks and fintechs.
                Professional Postgraduate Diploma in Financial Crime Compliance (ICA / University of Manchester).

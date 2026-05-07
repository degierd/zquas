# Transaction Monitoring Netherlands: What Went Wrong, What Comes Next

> Analysis of the TMNL cross-institutional AML initiative. Why it was shut down, what the architectural problem was, and how privacy-preserving MPC provides the alternative.

Source: https://zquas.ai/tmnl.html
Site: https://zquas.ai

---
Case Analysis


# Transaction Monitoring Netherlands: What Went Wrong, What Comes Next



            Five Dutch banks spent four years and tens of millions of euros building the world's most ambitious cross-institutional AML monitoring initiative. It was shut down in 2024. Not because it failed at detection. Because its architecture couldn't survive contact with privacy law. Here's the full story, and the architectural alternative that resolves the conflict.


        Last updated: March 2026






## What TMNL Was



Transaction Monitoring Netherlands was founded in July 2020 by the five largest Dutch banks: ABN AMRO, ING, Rabobank, Triodos Bank, and de Volksbank. The initiative was coordinated by the Dutch Banking Association (NVB) and supported by the Dutch government's Money Laundering Action Plan.



The premise was simple and compelling. An estimated €16 billion in criminal money is laundered through the Netherlands every year. Criminals spread their activity across multiple banks. Each bank monitors its own customers but can't see the cross-bank patterns. By pooling transaction data from all five banks and analysing it jointly, TMNL could detect money laundering networks that were invisible to any individual institution.



TMNL was staffed with over 70 professionals from more than 20 nationalities. It built a cloud-based analytics platform, developed AI-driven detection models, and tested scenarios covering human trafficking, VAT fraud, and drug-related money flows. The combined data revealed previously unknown criminal schemes, including cocaine smuggling operations using fruit and vegetable import companies as fronts.



The Wall Street Journal called it a 'cutting edge example' of innovation in the fight against money laundering. FATF referenced it as a key success factor in the Netherlands' AML efforts. The model was studied internationally, particularly in the UK.








## Why It Was Shut Down



TMNL's architecture centralised raw transaction data from five banks into a single platform. This was the most intuitive approach to joint analysis, and it worked technically. But it created a fundamental conflict with privacy rights.



In April 2024, the human rights organisation HRIF.EU, together with other organisations representing investors' rights, submitted a petition to the Dutch Parliament on behalf of nearly 15,000 banking customers. The petition demanded that TMNL stop processing data, cease its entrusted transaction monitoring from the five banks, and destroy all collected data. HRIF.EU argued that TMNL infringed on GDPR protections around automated decision-making and lacked transparency about how it handled large volumes of transaction information.



The Dutch Data Protection Authority raised concerns. The Council of State questioned the legal basis. Political support, once strong, became uncertain as the privacy implications became clearer.



Then the EU Anti-Money Laundering Regulation (AMLR) was finalised in May 2024. AMLR provides a legal framework for inter-bank cooperation, but it restricts data sharing to customers who are already identified as high-risk or where additional information is needed to assess their risk level. Broad-based pooling of transaction data across banks, which was TMNL's entire operational model, was no longer legally viable under the incoming EU framework.



In July 2024, TMNL announced it would wind down its existing activities and restructure. By January 2025, most staff had departed. The CEO, Norbert Siegers, described the initiative as 'unique, special and educational' and expressed hope that 'politicians, supervisors, public and private parties will find each other in a new route to collaboration.'



TMNL, in its current form, ceased to exist.








## The Architecture Was the Problem



TMNL didn't fail because of bad intentions, inadequate technology, or insufficient investment. It failed because its architecture required centralising data, and centralising data from multiple banks into a single platform is fundamentally incompatible with EU privacy law at scale.



This isn't a criticism of the TMNL team. When the initiative was conceived in 2018, centralised pooling was the most obvious approach. Privacy-preserving alternatives like secure multi-party computation were either too slow for financial transaction volumes or too immature for production deployment.



But the architectural choice had consequences that became clear over time:




The core paradox: effective cross-institutional detection requires visibility across banks. Data centralisation provides that visibility but violates privacy rights. As long as detection and centralisation are architecturally coupled, the paradox is unsolvable.





Every initiative that follows the same architectural pattern will face the same problem. The UK has explored similar models. Singapore has its COSMIC platform. The US has information sharing under Section 314(b) of the Patriot Act. Each operates under different legal frameworks, but the tension between detection value and privacy exposure is universal.



The question isn't whether cross-institutional detection is valuable. TMNL proved that it is. The question is whether you can achieve the detection without the centralisation.








## Privacy-Preserving Cross-Institutional Detection



Secure multi-party computation allows multiple parties to jointly compute a result from their combined data without any party revealing its data to the others. The mathematics for this have existed since the 1980s. What's changed is performance.



GPU-accelerated MPC implementations now achieve throughput levels compatible with real-time financial transaction monitoring. The cryptographic protocols (secret sharing, oblivious sorting, secure comparison) run on GPU hardware designed for massively parallel workloads. The computational overhead that made MPC impractical five years ago has been largely eliminated.



### How It Works Operationally



Each bank deploys a compliance engine on its own infrastructure. The bank's transaction data never leaves its premises. The engine processes the bank's transactions against its own policy set locally, providing the same single-bank monitoring capability as any conventional system.



When two or more banks run compatible engines, cross-institutional detection activates via MPC. The engines jointly compute risk indicators for shared counterparties. Bank A and Bank B can determine whether a counterparty exhibits suspicious cross-bank patterns. They get the answer. But Bank A never sees Bank B's transactions, and Bank B never sees Bank A's.



The MPC output is a risk indicator, not customer data. If the indicator flags elevated risk, the banks can use AMLR's legitimate data-sharing provisions for high-risk customers to share specific information. The MPC computation provides the reasonable basis for sharing, without requiring a data pool to generate that basis.



### What This Solves





| 
                        Dimension | 
                        TMNL Model | 
                        MPC-Based Model 
| 
                        **Data location** | 
                        Central platform | 
                        Stays at each bank 
| 
                        **Privacy exposure** | 
                        Full transaction visibility | 
                        Zero raw data disclosure 
| 
                        **GDPR/AMLR compatibility** | 
                        Required legislative carve-out | 
                        Compatible by construction 
| 
                        **Single point of breach** | 
                        Central database | 
                        No central target 
| 
                        **Bank autonomy** | 
                        Shared rule set negotiations | 
                        Each bank runs own rules 
| 
                        **Policy change impact** | 
                        Network-wide cascading | 
                        Contained to local installation 
| 
                        **Governance overhead** | 
                        Steering committee, PMO, consensus | 
                        Technical standards only 
| 
                        **Network scaling** | 
                        Consortium agreement | 
                        Bilateral connections 
| 
                        **Regulatory verification** | 
                        Trust-based audit | 
                        Cryptographic proof bundles 
## The Window Is Open



AMLR takes effect mid-2027. The five banks that founded TMNL still need cross-institutional detection capability. The regulatory expectation hasn't changed. The detection value has been proven. What failed was the architecture, not the mission.



The TMNL team demonstrated, over four years, that cross-bank analysis reveals criminal networks invisible to individual institutions. That finding doesn't expire. It means the next initiative needs a different architecture, not a different goal.



Privacy-preserving multi-party computation provides that different architecture. Each bank retains full data sovereignty. No central platform exists to attract privacy challenges. AMLR compliance is built in, not bolted on. And the network can grow through bilateral connections between banks, without requiring consortium-level consensus.



The core architecture is proven. The regulatory framework supports it. The institutional will, demonstrated by years of investment in TMNL, is clearly present. What's needed is the first two banks to start.



[See the complete operational flow — how cross-institutional detection works, step by step, from transaction to SAR.](use-case.html)





        Related


## Related Articles


            [
                March 2026 · Use Case


### How Cross-Institutional Detection Works



The complete operational flow from transaction to SAR. Six steps, three banks, zero data shared.

            ](use-case.html)
            [
                March 2026 · Analysis


### Why Cross-Institutional AML Detection Requires a New Architecture



Joint transaction monitoring initiatives have stalled across Europe. Privacy-preserving computation offers a fundamentally different approach.

            ](article-cross-institutional-detection.html)
            [
                February 2026 · Regulators


### Privacy-Preserving Detection Under AMLR



The EU AMLR creates a catch-22 for cross-institutional detection. There is a way through this.

            ](article-privacy-preserving-amlr.html)
            [
                February 2026 · Banks


### What Running a Multi-Bank Monitoring Network Actually Looks Like



The hard part is operations. How do banks join? Who sets the rules? What happens when one bank's policy change affects another bank's alerts?

            ](article-interbank-operations.html)




        Contact


## Let's talk



            If you're working on cross-institutional compliance challenges, I'd like to hear from you.



            [danny@zquas.ai](mailto:danny@zquas.ai?subject=TMNL%20Analysis%20/%20ZQUAS%20Inquiry)
            [LinkedIn](https://www.linkedin.com/in/danny-de-gier-prof-pgdip-fcc/)

        Zwolle, Netherlands

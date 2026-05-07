# What AMLR Article 75 Means for Dutch Banks

> The Netherlands tried collaborative AML detection. It failed because the law was not ready. AMLR Article 75 changes that. Here is what Dutch banks need to understand.

Source: https://zquas.ai/article-amlr-article-75-dutch-banks.html
Site: https://zquas.ai

---
[← Articles](articles.html)
        February 2026 · Regulation · 9 min read


# What AMLR Article 75 Means for Dutch Banks



The Netherlands tried collaborative AML detection. It failed. Not because the technology was wrong, but because the law was not ready. AMLR Article 75 resolves the legal deadlock. Dutch banks now have 16 months to build the infrastructure.







## What TMNL Was, and Why It Failed



            In 2019, ING, Rabobank, ABN AMRO, de Volksbank, and Triodos established Transaction Monitoring Netherlands. The premise was correct. Criminals spread activity across multiple banks because each bank can only see its own transactions. Pooling transaction data would expose patterns that individual banks miss.




            By 2025, TMNL was being wound down. Two legal barriers proved fatal. First, the Dutch Wwft requires that transaction monitoring remain an obligation of the individual bank. TMNL was structured as a central entity processing data on behalf of multiple banks, which the Wwft did not accommodate. Second, the Dutch Data Protection Authority advised that mass monitoring of transactions without a specific statutory basis violated GDPR Article 9.2. No EU-level legal basis existed for bank-to-bank AML data sharing of this kind.




            The technology concept was valid. The legal framework was not ready.




## What Article 75 Changes



            AMLR Article 75 (Regulation 2024/1624) creates an explicit legal basis for what it terms "partnerships for information sharing" between obliged entities. For the first time, EU law directly permits banks to exchange information that is strictly necessary for AML/CFT obligations. The regulation removes the legal ambiguity that ended TMNL.




            Article 75(3) specifies what data may be shared within a partnership: customer identification data, beneficial ownership information, transactional information, risk analysis outputs, and information about suspicious transactions. Sharing of suspicious transaction data requires the consent of the relevant Financial Intelligence Unit.




            Article 75(4)(f) mandates pseudonymisation as a required technical safeguard. The data exchanged must be pseudonymised before sharing. Article 75(5) requires that each institution retain independent decision-making. No bank may outsource its compliance judgment to a central body. Each bank must evaluate alerts independently and file its own SARs. Article 75 applies from July 10, 2027.




## The DNB Position



            De Nederlandsche Bank has stated publicly that initiatives like TMNL are "essential" for detecting financial crime but require the "correct legal basis." DNB has consistently supported the principle of collaborative monitoring while acknowledging the legal barrier that TMNL encountered.




            DNB expects AMLR Article 75 to resolve the legal deadlock. The supervisor is actively preparing for the new framework through its Innovation Hub, which has engaged with technology providers working on privacy-preserving approaches to cross-institutional detection. DNB's position aligns with the FATF guidance that cross-institutional data sharing, where legally permitted, materially improves detection outcomes.




## The TMNL Barrier Revisited



            Each of TMNL's two legal barriers is directly addressed by Article 75. The Wwft outsourcing problem is resolved because Article 75(5) explicitly requires that each bank maintain independent compliance responsibility. Banks share intelligence. They do not outsource decisions. The Wwft concern about centralised monitoring does not apply when each institution retains its own monitoring function.




            The GDPR Article 9.2 problem is resolved because Article 75 itself provides the specific statutory basis that the Dutch DPA found missing. The processing of special category data for AML/CFT purposes within an Article 75 partnership now has an explicit EU-level legal foundation. Combined with Article 6(1)(c) GDPR, which permits processing necessary for compliance with a legal obligation, the legal basis is clear.




## What Banks Must Build Before July 2027



            Article 75 creates the permission. Banks must build the infrastructure. Cross-institutional monitoring under Article 75 requires capabilities that most banks do not currently have.




            Entity matching across institutions is the first requirement. Banks must be able to identify that a customer at one bank is the same legal entity as a customer at another bank, without sharing customer databases. This requires standardised entity identifiers, KvK numbers for Dutch entities, LEI codes for legal entities with international operations, and resolution logic that handles name variations and corporate structures.




            Risk comparison protocols must satisfy GDPR data minimisation under Article 5(1)(c). The technical design must ensure that only the minimum necessary information crosses institutional boundaries. Pseudonymisation under Article 75(4)(f) is the floor, not the ceiling. Banks that share more than pseudonymised risk scores face GDPR exposure regardless of the Article 75 legal basis.




            Cryptographic audit trails are required for supervisory verification. DNB and AMLA will expect to verify that the monitoring system operated as documented, that the correct policies were applied, and that no raw personal data crossed institutional boundaries. An audit trail that relies on bank self-reporting does not satisfy this requirement. The trail must be independently verifiable.




            Integration with existing transaction monitoring systems must be non-disruptive. Banks cannot replace their core monitoring infrastructure in the time available. The Article 75 capability must sit alongside existing systems, receiving risk scores and generating cross-institutional alerts without requiring a platform replacement.




            Building this infrastructure from scoping to production takes 12 to 18 months. Banks that begin in Q1 2026 can be ready. Banks that wait until 2027 cannot meet the July 10 application date.




## Privacy-Preserving Computation as the Technical Answer



            Article 75(4)(f) mandates pseudonymisation. Banks that interpret this narrowly, replacing customer names with pseudonyms before sharing transaction records, remain exposed. Pseudonymised transaction data is still personal data under GDPR. Re-identification risk exists wherever raw records are shared, even in pseudonymised form.




            Multi-party computation offers a technically stronger solution. Under MPC, each bank computes a risk score within its own environment. The computation then compares scores across banks without any raw data, pseudonymised or otherwise, leaving the originating institution. The output is a cross-institutional risk signal. The input remains within each bank's data perimeter.




            The European Data Protection Board has identified MPC as an accountability tool for cross-border data processing, noting that MPC "transforms personal data into random auxiliary numbers which are deleted after the computation, rendering them virtually impossible to intercept." MPC satisfies the Article 75 pseudonymisation requirement and goes beyond it. The EDPB analysis provides the legal grounding that DPOs and legal teams need when drafting Data Protection Impact Assessments for Article 75 partnerships.




## The Timeline



            July 10, 2027 is the Article 75 application date. The 40 institutions selected for direct AMLA supervision in the second half of 2027 will be evaluated partly on their cross-border AML capabilities. Dutch banks, given their direct experience with TMNL, understand the need for collaborative detection better than most institutions in Europe. They also have 16 months to build what TMNL could not.




            The legal question is answered. Article 75 permits collaborative AML detection. The technical question is which architecture satisfies both the legal mandate and the privacy requirements. An architecture that shares pseudonymised raw data may satisfy the letter of Article 75(4)(f) while remaining vulnerable to GDPR challenge. An architecture that generates intelligence without sharing raw data satisfies both.



            Danny de Gier

                Founder, ZQUAS. 18+ years in financial crime compliance at Tier-1 banks and fintechs.
                Professional Postgraduate Diploma in Financial Crime Compliance (ICA / University of Manchester).

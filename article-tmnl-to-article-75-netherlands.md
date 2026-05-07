# From TMNL to Article 75: The Netherlands' Path to Collaborative AML

> In 2019, five Dutch banks created the most ambitious collaborative AML project in Europe. By 2025, it was being wound down. This is what happened, why it mattered, and what comes next.

Source: https://zquas.ai/article-tmnl-to-article-75-netherlands.html
Site: https://zquas.ai

---
[← Articles](articles.html)
        February 2026 · Industry · 11 min read


# From TMNL to Article 75: The Netherlands' Path to Collaborative AML



In 2019, five of the largest Dutch banks created Transaction Monitoring Netherlands. It was the most ambitious collaborative AML project in Europe. By 2025, it was being wound down. This is the story of what happened, why it mattered, and what comes next.







## What TMNL Was



            Transaction Monitoring Netherlands was a joint venture established by ING, Rabobank, ABN AMRO, de Volksbank, and Triodos. The five banks together hold the majority of Dutch retail and SME banking relationships. Their combined transaction monitoring coverage is, in practical terms, a significant portion of Dutch financial activity.




            The premise behind TMNL was straightforward. Criminals spread their activity across multiple banks deliberately. A money laundering operation that moves funds through three different institutions leaves each bank with a fragment of the pattern. No single bank sees enough to trigger an alert. TMNL was designed to pool transaction data so that analysts could observe the full pattern across institutions.




            The premise was correct. Cross-institutional detection does expose patterns that individual banks miss. The five participating banks understood this from their own experience. Each had investigated cases where, after the fact, it emerged that the subject had concurrent relationships at two or more other participating institutions. The intelligence gap was real.




## Why TMNL Failed



            TMNL encountered two distinct legal barriers. Neither was a technicality. Both reflected genuine structural problems with the centralised data pooling approach.




            The first barrier was the Wet ter voorkoming van witwassen en financieren van terrorisme, the Wwft. Dutch AML law requires that transaction monitoring be conducted by the obliged entity itself. It is not an obligation that can be fully outsourced to a third party. TMNL was structured as a separate legal entity processing transaction data received from five banks. The Wwft did not accommodate this structure. Each bank remained legally responsible for its own monitoring, but TMNL was performing that monitoring centrally, creating a compliance gap that the Wwft framework could not resolve.




            The second barrier was GDPR. The Dutch Data Protection Authority, the AP, advised that mass monitoring of transactions across institutions, without a specific statutory basis for that sharing, lacked a lawful basis under GDPR Article 6. Transaction data relating to natural persons constitutes personal data. Sharing it with a joint entity for monitoring purposes requires a legal basis. Additionally, the AP found that transaction data can reveal special category data under GDPR Article 9 (for example, donations to religious organisations), creating a secondary compliance risk. In the absence of a specific EU or Dutch statutory provision authorising bank-to-bank AML data sharing of this kind, no adequate legal basis existed.




            The technology concept was valid. The legal framework was not ready. These are separate conclusions and it is important to keep them separate.




## What the Industry Learned



            TMNL generated insights that will shape every subsequent cross-institutional AML initiative in Europe. Four lessons are directly applicable to Article 75 design.




            Centralised data pooling creates GDPR problems by design. Any architecture in which multiple banks' customer data flows to a central repository inherits the legal exposure that ended TMNL. The central repository holds combined personal data from multiple controllers. The GDPR framework was not designed for this and does not accommodate it cleanly.




            A legal basis must exist before the sharing begins. TMNL operated in a legal gap and eventually the regulators closed it. Any future initiative must establish its legal basis before processing personal data across institutional boundaries, not after launch.




            The technology must satisfy data minimisation, not just data security. TMNL's approach addressed security, data was held within a controlled environment, but not minimisation. The underlying transaction records, far more data than necessary to generate a risk signal, were shared. GDPR Article 5(1)(c) requires that sharing be limited to what is necessary. Sharing full transaction records is not necessary to generate a cross-institutional risk score.




            Each bank must retain independent compliance responsibility. The Wwft barrier at TMNL was partly a consequence of the structure centralising the compliance function. Any workable cross-institutional model must preserve each bank's independent monitoring and independent decision-making. Collaborative detection supplements individual monitoring. It does not replace it.




## Article 75: The Legal Fix



            AMLR Article 75 (Regulation 2024/1624) directly addresses each of TMNL's legal barriers. The regulation creates an explicit statutory basis for "partnerships for information sharing" between obliged entities. For the first time, EU law provides the specific provision that the Dutch DPA found missing in the TMNL structure.




            The Wwft outsourcing problem is resolved by Article 75(5), which requires that each institution within a partnership retain independent compliance responsibility. No institution may delegate its monitoring obligation to the partnership. The partnership generates shared intelligence. Each bank evaluates that intelligence independently and files its own SARs with its national FIU.




            The GDPR lawful basis problem is resolved because Article 75 itself provides the statutory compatibility. Article 6(1)(c) GDPR permits processing necessary for compliance with a legal obligation. AMLR Article 75 is that legal obligation for participating banks. The processing that TMNL lacked a legal basis for now has one. The Article 9 special category risk is mitigated by the pseudonymisation requirements in Article 75(4)(f).




            Article 75(4)(f) mandates pseudonymisation as a required technical safeguard. The data minimisation lesson from TMNL is reflected directly in the regulatory text. Sharing must be limited to pseudonymised information. Banks cannot pool raw transaction records and expect Article 75 to cover them.




            Article 75(3) specifies the permissible scope: customer identification data, beneficial ownership information, transactional information, risk analysis outputs, and suspicious transaction information with FIU consent. The scope is defined and limited.




## The Technology Question



            Article 75 creates the permission. It also creates the requirement. Pseudonymisation is mandated. Each bank's independent decision-making must be preserved. The sharing must be limited to what is strictly necessary for AML/CFT purposes.




            The TMNL architecture, centralised pooling of transaction data, would still fail the Article 75 technical requirements. Pseudonymised raw transaction records are still personal data. Sharing them with a central entity still creates the data minimisation exposure that the AP identified. Article 75 does not rescue centralised pooling from GDPR.




            Privacy-preserving computation offers an architecture that satisfies both the legal basis and the technical safeguard requirements simultaneously. Under multi-party computation, each bank computes a risk score from its own transaction data, within its own environment. The computation then compares risk scores across institutions without any raw data, pseudonymised or otherwise, leaving the originating bank. The output is a cross-institutional risk signal. Each bank evaluates that signal independently and decides whether to file a SAR.




            The European Data Protection Board has described MPC as transforming personal data into "random auxiliary numbers which are deleted after the computation, rendering them virtually impossible to intercept." MPC satisfies the Article 75(4)(f) pseudonymisation requirement and goes beyond it. The intelligence is generated. The raw data stays within the originating institution.




## Timeline and Urgency



            Article 75 applies from July 10, 2027. DNB is preparing through its Innovation Hub. The 40 institutions selected for AMLA direct supervision in the second half of 2027 will be evaluated on their cross-border AML capabilities. Dutch banks that participated in TMNL already understand, more concretely than any other banks in Europe, why collaborative detection is essential. They understand the legal constraints. They understand the operational requirements. They have 16 months to build what TMNL could not.




            Building cross-institutional monitoring infrastructure from scoping to production takes 12 to 18 months. Vendor evaluation, DPIA completion, integration with existing monitoring systems, staff training, and regulatory engagement all take time. Banks that begin in Q1 2026 can be ready. Banks that begin in Q1 2027 cannot.




## TMNL as Proof of Demand



            TMNL was not a failure of ambition or of analysis. The five banks that created it were correct about the problem. Criminal networks do exploit institutional blind spots. Cross-institutional detection does produce results that individual monitoring cannot. The fact that five of the largest Dutch banks invested substantially in a joint venture to address this problem demonstrates the seriousness with which the Dutch banking sector approaches financial crime compliance.




            TMNL was a proof of demand. Article 75 removes the legal barrier. The next step is deploying technology that satisfies both the legal mandate and the privacy requirements embedded in that mandate. The technology exists. The legal basis exists. The demand has been proven. Dutch banks are positioned to lead the first wave of Article 75 partnerships in Europe.



            Danny de Gier

                Founder, ZQUAS. 18+ years in financial crime compliance at Tier-1 banks and fintechs.
                Professional Postgraduate Diploma in Financial Crime Compliance (ICA / University of Manchester).

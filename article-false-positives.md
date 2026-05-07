# The Real Cost of 95% False Positives

> Everyone in compliance knows the number. But the real damage isn't in the alerts themselves. It's in everything that happens around them.

Source: https://zquas.ai/article-false-positives.html
Site: https://zquas.ai

---
[← Articles](articles.html)
        January 2026 · Banks · 7 min read


# The Real Cost of 95% False Positives



Everyone in compliance knows the number. Ninety-five percent of AML alerts are false positives. But the real damage isn't in the alerts themselves. It's in everything that happens around them.






            I've spent 18 years in financial crime compliance at banks like Deutsche Bank, HSBC, and RBS. In every single one, the alert backlog was the dominant fact of life. Not the risk models. Not the regulatory exams. The backlog.




            Let me walk through what that 95% number actually costs, because the headline figure hides where the money really goes.




## Analyst Hours Are Just the Start



            A typical Tier-1 bank employs 3,000 to 6,000 people in AML operations. In the Netherlands alone, the banking sector had roughly 6,000 full-time AML staff as of 2019. That number has grown since.




            Most of those people spend their days reviewing alerts that turn out to be nothing. Open the case. Pull the customer profile. Check transaction history. Cross-reference against sanctions lists. Write a disposition note. Close the case. Repeat.




            At an average fully-loaded cost of €80,000 per analyst per year, a 3,000-person team costs €240 million annually. If 95% of their work is wasted on false alerts, that's roughly €228 million spent investigating legitimate business activity. Every year. At one bank.




            But the analyst cost is the part everyone already knows. The hidden costs are worse.




## Customer Damage



            When a monitoring system flags a transaction, many banks freeze the account pending review. For a business customer, that can mean missed payroll, failed supplier payments, or a collapsed deal. I've seen legitimate import-export companies locked out of their accounts for weeks because a wire to a correspondent bank in a higher-risk jurisdiction triggered an alert.




            Those customers don't come back. And they tell other businesses. The reputational cost doesn't show up in the compliance budget, but the commercial banking teams feel it.




            Worse, when alert volumes are overwhelming, analysts rush through reviews. They develop shortcuts. They start pattern-matching against the last hundred cases they cleared rather than genuinely investigating. This means the rare true positive buried in the pile gets the same cursory treatment as the false ones. The system designed to catch criminals ends up giving criminals cover through sheer noise.




## The Regulatory Trap



            Here's the part that keeps compliance officers up at night. Regulators don't just want you to catch money laundering. They want you to demonstrate that your monitoring system works effectively. When 95% of your alerts are false positives, what does that tell the examiner?




            It tells them your rules are too broad. But if you tighten the rules to reduce false positives, you risk missing real suspicious activity. And the fine for missing a SAR filing is existential. ING paid €775 million. ABN AMRO paid €480 million. Nobody gets fired for filing too many SARs. People absolutely get fired for missing one.




            So the system stays miscalibrated. Banks accept the waste because the alternative, being accused of insufficient monitoring, is worse. This is rational behavior by individual institutions, but it's collectively insane.




## Why Rules-Based Monitoring Creates This Problem



            Traditional transaction monitoring works by setting thresholds. Transactions above €10,000 to certain jurisdictions. Cash deposits above a certain frequency. Wire transfers that match known typologies.




            The problem is that these rules have no context. They don't know that the customer is a flower importer who has been sending €15,000 to Kenya every month for eight years. They don't know that the sudden spike in transaction volume coincides with Valentine's Day. They just see: amount exceeds threshold, jurisdiction matches risk list, generate alert.




            Every compliance professional knows this. The fix seems obvious: add context. But adding context in a rules-based system means adding more rules, more exceptions, more complexity. And every new rule interacts with every existing rule in ways that are hard to predict and impossible to test exhaustively.




## What Changes With Full Graph Context



            The alternative is to evaluate every transaction with full knowledge of the entity's network. Not just this transaction in isolation, but this customer's entire relationship map. Who they transact with. Who those counterparties transact with. What the normal pattern looks like across the network. Where the deviations are.




            When you can propagate risk scores across the entire entity graph in real time, the threshold problem disappears. You're not asking "does this transaction exceed a number?" You're asking "does this pattern look anomalous given everything we know about this network?" That's a different question entirely, and it produces different alert quality.




            GPU-accelerated graph analysis makes this practical at scale. Running full network context evaluation on millions of transactions per second isn't theoretical anymore. It's measurable. And when you combine it with deterministic policy enforcement, where the same data and same policies always produce the same verdict, you get something compliance officers have never had: a system they can actually explain to the regulator with confidence.




## The Bottom Line



            The 95% false positive rate isn't a technology problem. It's an architecture problem. Rules without context produce noise. Context at scale requires compute power that wasn't available when most monitoring systems were designed.




            The cost isn't just €200 million a year in wasted analyst time. It's damaged customer relationships, weakened detection of actual criminals, and a regulatory dynamic that punishes precision. Banks know this. Regulators know this. The architecture just hasn't caught up.




            It's catching up now.



            Danny de Gier

                Founder, ZQUAS. 18+ years in financial crime compliance at Tier-1 banks and fintechs.
                Professional Postgraduate Diploma in Financial Crime Compliance (ICA / University of Manchester).

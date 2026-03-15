const fs = require("fs");
const { Document, Packer, Paragraph, TextRun, Header, Footer, AlignmentType,
        HeadingLevel, BorderStyle, PageBreak, PageNumber, TabStopType } = require("docx");

const NAVY = "1B3A5C";
const ACCENT = "2E75B6";

const h1 = (text) => new Paragraph({ heading: HeadingLevel.HEADING_1, spacing: { before: 400, after: 240 }, children: [new TextRun({ text, bold: true, size: 34, font: "Georgia", color: NAVY })] });
const h2 = (text) => new Paragraph({ heading: HeadingLevel.HEADING_2, spacing: { before: 320, after: 180 }, children: [new TextRun({ text, bold: true, size: 26, font: "Georgia", color: NAVY })] });
const p = (text) => new Paragraph({ spacing: { after: 180, line: 312 }, children: [new TextRun({ text, size: 23, font: "Georgia" })] });
const pBold = (text) => new Paragraph({ spacing: { after: 180, line: 312 }, children: [new TextRun({ text, bold: true, size: 23, font: "Georgia" })] });

const pQuote = (text, source) => new Paragraph({
  spacing: { before: 280, after: 280, line: 312 },
  indent: { left: 600, right: 600 },
  border: { left: { style: BorderStyle.SINGLE, size: 14, color: ACCENT, space: 14 } },
  children: [
    new TextRun({ text: "\u201C" + text + "\u201D", italics: true, size: 24, font: "Georgia", color: "333333" }),
    new TextRun({ text: " \u2014 ", size: 20, font: "Georgia", color: "888888" }),
    new TextRun({ text: source, size: 20, font: "Georgia", color: "888888" })
  ]
});

const children = [];

// ═══ TITLE ═══
children.push(new Paragraph({ spacing: { before: 600, after: 100 }, children: [
  new TextRun({ text: "What Article 75 Was Afraid to Permit", size: 48, font: "Georgia", color: NAVY, bold: true })
]}));
children.push(new Paragraph({ spacing: { after: 400 }, children: [
  new TextRun({ text: "And why Multi-Party Computation makes the restriction irrelevant.", size: 24, font: "Georgia", color: "666666", italics: true })
]}));

// ═══ THE HOOK ═══
children.push(pQuote(
  "Article 75 doesn\u2019t appear to go as far as many financial crime fighters would have hoped, and focuses essentially on higher risk customers and/or post-suspicion sharing and is less permissive on sharing information on lower risk customers.",
  "Financial Crime News, June 2024"
));

children.push(p("This is the most important sentence in EU financial crime regulation right now. Read it again."));

children.push(p("The EU\u2019s new Anti-Money Laundering Regulation, effective July 2027, finally creates a legal framework for banks to share AML information. Article 75 establishes supervised partnerships where obliged entities can exchange customer data, transaction information, and risk factors."));

children.push(p("But it pulls the punch. Sharing is restricted to higher-risk customers and post-suspicion cases. Low-risk customers are excluded."));

children.push(pBold("The criminals who are most dangerous are the ones who maintain a low-risk profile at every bank they touch. Article 75 cannot reach them."));

// ═══ WHY THE RESTRICTION EXISTS ═══
children.push(h2("Why the restriction exists"));

children.push(p("The answer is GDPR. Sharing customer data across institutions is personal data processing. Under data minimisation principles, blanket-sharing your entire customer base with other banks would be disproportionate. Article 75 draws a line: share data on suspicious customers, not on everyone."));

children.push(p("This is legally correct. It is also operationally useless against sophisticated criminals."));

children.push(p("A criminal who spreads \u20AC12 million across six banks at \u20AC2 million each, with clean KYC, legitimate business fronts, and unremarkable transaction patterns at every institution, will never appear on any bank\u2019s high-risk list. The risk is invisible until you add it up. And Article 75 says you\u2019re not allowed to add it up."));

// ═══ THE RESOLUTION ═══
children.push(h2("What if you could add it up without sharing anything?"));

children.push(p("Multi-Party Computation (MPC) is a cryptographic technique that allows two parties to jointly compute a function over their combined data without either party revealing its input to the other."));

children.push(p("In practical terms: Bank A and Bank B each have a risk score for the same customer. Using MPC, they can determine whether the combined risk exceeds a threshold. Bank A does not learn Bank B\u2019s score. Bank B does not learn Bank A\u2019s score. Neither bank learns anything about the other\u2019s non-shared customers. The only output is a binary signal: above threshold, or not."));

children.push(p("What crosses between the banks during this computation? Elliptic curve points. Garbled circuit ciphertexts. Oblivious transfer labels. None of this is personal data. It is cryptographic material, computationally indistinguishable from random bytes."));

children.push(pBold("If no personal data is shared, the GDPR restriction that Article 75 was forced to accept has no object. The entire customer base can be federated."));

// ═══ THE NUMBERS ═══
children.push(h2("This is not theoretical"));

children.push(p("We built it. The ZQUAS platform runs GPU-accelerated MPC federation with 29 real compliance policies (100 rules across 9 regulatory domains, audited line-by-line against a 38-page policy manual grounded in FATF 40, EU AMLD5, Wwft, BSA, and FCA Handbook). Zero critical discrepancies. Every rule matches the spec."));

children.push(p("Measured results on production hardware, with AES-256-GCM encryption active on every round:"));

children.push(pBold("5,000 entities per bank, full pipeline: 344 milliseconds."));
children.push(pBold("500,000 entities per bank, full pipeline: 7.5 seconds."));
children.push(pBold("97 banks federated (entire Dutch banking sector): 72.7 seconds."));

children.push(p("If you work in AML, you just re-read those numbers. They are not a typo."));

children.push(p("Traditional cross-bank AML comparison requires overnight batch processing: extract data, pseudonymise, transfer, load, query. That takes 4\u201324 hours. ZQUAS replaces the entire pipeline with real-time cryptographic computation on GPU. The 5,764\u00d7 speedup at 1 million daily volume is not because we cut corners on the policies. It\u2019s because we eliminated the architecture that made cross-bank comparison slow: there is no data extraction, no transfer, no central database. Each bank runs a local edge node. The cryptographic protocol handles the rest."));

children.push(p("The 29 policies are real. Sanctions screening (OFAC, UN, EU, HMT), PEP/EDD with 8-factor composite scoring, transaction monitoring (structuring, layering, TBML, smurfing, round-trip detection, correspondent banking risk), fraud prevention (APP, synthetic ID, account takeover, deepfake detection, insider threat), KYC/KYB, crypto/VASP compliance, and SAR quality gating. Five cross-domain chains. Every policy maps to specific regulatory articles. Every policy was audited against the manual and corrected until the implementation matches the specification exactly."));

// ═══ THE TMNL CONNECTION ═══
children.push(h2("The TMNL lesson"));

children.push(p("The Netherlands learned this the hard way. TMNL (Transaction Monitoring Netherlands) proved that cross-bank detection works. Then the Dutch DPA stopped it, because centralising pseudonymised data is still processing personal data under GDPR."));

children.push(p("They were right. Pseudonymised data is personal data. That\u2019s settled law."));

children.push(p("But MPC doesn\u2019t pseudonymise. It computes on secret shares that are mathematically random without the other party\u2019s cooperation. That\u2019s not pseudonymisation. It\u2019s a fundamentally different operation. The distinction matters: pseudonymised data can be re-identified given auxiliary information. MPC secret shares cannot be de-anonymised even with unlimited computational resources."));

children.push(pBold("TMNL proved the detection works. Article 75 provides the legal framework. MPC makes it privacy-safe. The three pieces are finally available at the same time."));

// ═══ THE ASK ═══
children.push(h2("What we\u2019re asking for"));

children.push(p("Not trust. Evidence."));

children.push(p("We are seeking regulatory sandbox engagement (DNB InnovationHub, FCA Digital Sandbox) to demonstrate, under supervision, that MPC federation detects cross-institutional laundering patterns without any institution accessing any other institution\u2019s customer data. We are also seeking to establish, with the relevant Data Protection Authority, whether MPC protocol messages constitute personal data under GDPR."));

children.push(p("If they do: Article 75 scope limits apply, and we operate within them. That is still better than the status quo. If they don\u2019t: full customer base federation is legally permissible. The most dangerous criminals, the ones who exploit institutional silos, lose their best hiding place."));

// ═══ CLOSE ═══
children.push(new Paragraph({ spacing: { before: 400 }, border: { top: { style: BorderStyle.SINGLE, size: 4, color: "CCCCCC", space: 8 } }, children: [] }));

children.push(new Paragraph({ spacing: { before: 200, after: 120 }, children: [
  new TextRun({ text: "The full position paper ", size: 22, font: "Georgia" }),
  new TextRun({ text: "\u201CWhat Article 75 Was Afraid to Permit\u201D", italics: true, size: 22, font: "Georgia", color: ACCENT }),
  new TextRun({ text: " (including scaling benchmarks, a detailed legal analysis of MPC under GDPR, and responses to seven anticipated challenges) is available at ", size: 22, font: "Georgia" }),
  new TextRun({ text: "zquas.ai", size: 22, font: "Georgia", color: ACCENT, bold: true }),
  new TextRun({ text: ".", size: 22, font: "Georgia" })
]}));

children.push(new Paragraph({ spacing: { before: 200, after: 80 }, children: [
  new TextRun({ text: "ZQUAS", bold: true, size: 22, font: "Georgia", color: ACCENT }),
  new TextRun({ text: " \u2014 Bounded Compliance on an Unbounded Platform", size: 22, font: "Georgia", color: NAVY })
]}));

children.push(new Paragraph({ spacing: { after: 80 }, children: [
  new TextRun({ text: "info@zquas.ai", size: 20, font: "Georgia", color: ACCENT })
]}));

children.push(new Paragraph({ spacing: { before: 300, after: 100 }, children: [
  new TextRun({ text: "This article does not constitute legal advice. The legal position regarding MPC and GDPR should be validated through formal engagement with the relevant Data Protection Authority.", italics: true, size: 17, font: "Georgia", color: "999999" })
]}));

children.push(new Paragraph({ children: [
  new TextRun({ text: "\u00A9 2026 ZQUAS. All rights reserved.", italics: true, size: 17, font: "Georgia", color: "999999" })
]}));

// ═══ GENERATE ═══
const doc = new Document({
  styles: {
    default: { document: { run: { font: "Georgia", size: 23 } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 34, bold: true, font: "Georgia", color: NAVY },
        paragraph: { spacing: { before: 400, after: 240 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 26, bold: true, font: "Georgia", color: NAVY },
        paragraph: { spacing: { before: 320, after: 180 }, outlineLevel: 1 } }
    ]
  },
  sections: [{
    properties: {
      page: { size: { width: 11906, height: 16838 }, margin: { top: 1800, right: 1800, bottom: 1800, left: 1800 } }
    },
    children
  }]
});

Packer.toBuffer(doc).then(buffer => {
  const outPath = require("path").join(__dirname, "ZQUAS_LinkedIn_Article_75.docx");
  fs.writeFileSync(outPath, buffer);
  console.log("Generated: " + outPath);
});

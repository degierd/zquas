const fs = require("fs");
const { Document, Packer, Paragraph, TextRun, HeadingLevel, BorderStyle } = require("docx");

const NAVY = "1B3A5C";
const ACCENT = "2E75B6";

const h2 = (text) => new Paragraph({ heading: HeadingLevel.HEADING_2, spacing: { before: 300, after: 180 }, children: [new TextRun({ text, bold: true, size: 26, font: "Georgia", color: NAVY })] });
const p = (text) => new Paragraph({ spacing: { after: 180, line: 312 }, children: [new TextRun({ text, size: 23, font: "Georgia" })] });
const pBold = (text) => new Paragraph({ spacing: { after: 180, line: 312 }, children: [new TextRun({ text, bold: true, size: 23, font: "Georgia" })] });
const spacer = (h) => new Paragraph({ spacing: { before: h || 100 }, children: [] });

const children = [];

children.push(new Paragraph({ spacing: { before: 400, after: 200 }, children: [
  new TextRun({ text: "LinkedIn Post \u2014 Founding Partner Programme", size: 16, font: "Georgia", color: "999999", italics: true })
]}));

children.push(new Paragraph({ spacing: { after: 100 }, children: [
  new TextRun({ text: "Post this 2\u20133 days after the Article 75 piece. Let the first article get traction before announcing the programme.", italics: true, size: 19, font: "Georgia", color: "888888" })
]}));

children.push(new Paragraph({
  spacing: { before: 200 },
  border: { top: { style: BorderStyle.SINGLE, size: 4, color: ACCENT, space: 8 } },
  children: []
}));

children.push(spacer(200));

// ═══ THE POST ═══

children.push(p("The response to our Article 75 position paper surprised us."));

children.push(p("Compliance leaders from across Europe reached out. The message was consistent: \u201CWe\u2019ve been waiting for someone to say this.\u201D"));

children.push(p("The problem they described is the same everywhere. Their transaction monitoring systems are blind to cross-institutional patterns. They know criminals exploit the gaps between banks. They know Article 75 opens the door to information sharing. They also know that sharing actual customer data, even under Article 75\u2019s supervised framework, creates GDPR risk that their legal teams won\u2019t accept."));

children.push(pBold("So we\u2019re opening our Founding Partner Programme."));

children.push(p("Three institutions. Three pilot slots. Twelve weeks from signature to results."));

children.push(p("What Founding Partners get:"));

children.push(p("\u2022 24-month preferential licensing (50% of standard rate)"));
children.push(p("\u2022 Permanent seat on our Policy Advisory Board"));
children.push(p("\u2022 Joint regulatory sandbox engagement (DNB, FCA, or relevant national FSA)"));
children.push(p("\u2022 Co-authored case study published at industry conferences"));
children.push(p("\u2022 Dedicated integration engineer for the pilot duration"));
children.push(p("\u2022 Contractual data sovereignty guarantee. No customer data leaves your infrastructure, ever."));

children.push(p("What we\u2019ve already proven:"));

children.push(p("\u2022 500,000 entities per bank: 7.5 seconds, full pipeline, AES-256-GCM encrypted"));
children.push(p("\u2022 97 banks federated (entire Dutch banking sector): 72.7 seconds"));
children.push(p("\u2022 29 compliance policies, 100 rules, 9 domains. Audited line-by-line, zero discrepancies."));
children.push(p("\u2022 4/4 real-world laundering typologies detected, per-entity verified at every scale"));
children.push(p("\u2022 0.00% false positive rate on realistic moderate-risk population"));
children.push(p("\u2022 Zero data shared between institutions. Mathematically guaranteed."));

children.push(p("What you need to provide: entity risk scores (synthetic or representative), one server, one IT contact, one compliance contact, and the willingness to engage your regulator."));

children.push(p("No 18-month procurement process. No committee of committees. Twelve weeks."));

children.push(pBold("Three slots. When they\u2019re committed, the programme closes."));

children.push(p("If your institution is ready to move from overnight batch monitoring to real-time cross-institutional detection, without sharing a single byte of customer data, let\u2019s talk."));

children.push(p("info@zquas.ai"));

children.push(spacer(100));

children.push(p("\u2014"));
children.push(p("Danny de Gier"));
children.push(p("ZQUAS \u2014 Bounded Compliance on an Unbounded Platform"));

children.push(spacer(200));

children.push(new Paragraph({
  spacing: { before: 200 },
  border: { top: { style: BorderStyle.SINGLE, size: 4, color: ACCENT, space: 8 } },
  children: []
}));

children.push(spacer());

children.push(new Paragraph({ children: [
  new TextRun({ text: "Suggested hashtags: ", italics: true, size: 19, font: "Georgia", color: "888888" }),
  new TextRun({ text: "#AML #FinancialCrime #AMLR #Article75 #PrivacyPreservingTechnology #MPC #RegTech #Compliance #GDPR #Banking #FinCrime #TMNL", size: 19, font: "Georgia", color: ACCENT })
]}));

children.push(spacer());

children.push(new Paragraph({ children: [
  new TextRun({ text: "Suggested image: ", italics: true, size: 19, font: "Georgia", color: "888888" }),
  new TextRun({ text: "A clean graphic showing \u201C3 slots \u2022 3 regulators \u2022 12 weeks\u201D with the ZQUAS logo. Dark background, minimal, not a stock photo.", size: 19, font: "Georgia", color: "666666" })
]}));

children.push(spacer());

children.push(new Paragraph({ children: [
  new TextRun({ text: "Post timing: ", italics: true, size: 19, font: "Georgia", color: "888888" }),
  new TextRun({ text: "Tuesday or Wednesday morning, 8:00\u20139:00 CET. LinkedIn engagement peaks early-week mornings in European financial services.", size: 19, font: "Georgia", color: "666666" })
]}));

const doc = new Document({
  styles: { default: { document: { run: { font: "Georgia", size: 23 } } } },
  sections: [{ properties: { page: { margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 } } }, children }]
});

Packer.toBuffer(doc).then(buffer => {
  const outPath = require("path").join(__dirname, "ZQUAS_LinkedIn_Founding_Partner_Post.docx");
  fs.writeFileSync(outPath, buffer);
  console.log("Generated: " + outPath);
});

const fs = require("fs");
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
        Header, Footer, AlignmentType, LevelFormat, HeadingLevel, BorderStyle,
        WidthType, ShadingType, PageBreak, PageNumber, TabStopType } = require("docx");

const NAVY = "1B3A5C";
const ACCENT = "2E75B6";
const LIGHT_BG = "EDF3F8";
const HEADER_BG = "1B3A5C";
const HEADER_FG = "FFFFFF";
const GOLD = "B8860B";
const BORDER = { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" };
const BORDERS = { top: BORDER, bottom: BORDER, left: BORDER, right: BORDER };
const CELL_MARGINS = { top: 60, bottom: 60, left: 120, right: 120 };

const h1 = (text) => new Paragraph({ heading: HeadingLevel.HEADING_1, spacing: { before: 400, after: 240 }, children: [new TextRun({ text, bold: true, size: 34, font: "Georgia", color: NAVY })] });
const h2 = (text) => new Paragraph({ heading: HeadingLevel.HEADING_2, spacing: { before: 320, after: 180 }, children: [new TextRun({ text, bold: true, size: 26, font: "Georgia", color: NAVY })] });
const h3 = (text) => new Paragraph({ heading: HeadingLevel.HEADING_3, spacing: { before: 240, after: 140 }, children: [new TextRun({ text, bold: true, size: 22, font: "Georgia", color: ACCENT })] });
const p = (text) => new Paragraph({ spacing: { after: 160, line: 300 }, children: [new TextRun({ text, size: 22, font: "Georgia" })] });
const pBold = (label, text) => new Paragraph({ spacing: { after: 120, line: 300 }, children: [new TextRun({ text: label, bold: true, size: 22, font: "Georgia" }), new TextRun({ text, size: 22, font: "Georgia" })] });
const pBoldOnly = (text) => new Paragraph({ spacing: { after: 160, line: 300 }, children: [new TextRun({ text, bold: true, size: 22, font: "Georgia" })] });
const pItalic = (text) => new Paragraph({ spacing: { after: 120 }, children: [new TextRun({ text, italics: true, size: 19, font: "Georgia", color: "666666" })] });
const spacer = (h) => new Paragraph({ spacing: { before: h || 100 }, children: [] });
const pageBreak = () => new Paragraph({ children: [new PageBreak()] });

function headerCell(text, width) {
  return new TableCell({
    borders: BORDERS, width: { size: width, type: WidthType.DXA },
    shading: { fill: HEADER_BG, type: ShadingType.CLEAR },
    margins: CELL_MARGINS,
    children: [new Paragraph({ children: [new TextRun({ text, bold: true, size: 19, font: "Georgia", color: HEADER_FG })] })]
  });
}
function cell(text, width, shade) {
  return new TableCell({
    borders: BORDERS, width: { size: width, type: WidthType.DXA },
    shading: shade ? { fill: LIGHT_BG, type: ShadingType.CLEAR } : undefined,
    margins: CELL_MARGINS,
    children: [new Paragraph({ spacing: { line: 276 }, children: [new TextRun({ text, size: 19, font: "Georgia" })] })]
  });
}

const children = [];

// ═══════════════════════════════════════════════════════════
// COVER
// ═══════════════════════════════════════════════════════════

children.push(new Paragraph({ spacing: { before: 2400 }, alignment: AlignmentType.LEFT, children: [
  new TextRun({ text: "ZQUAS", size: 28, font: "Georgia", color: ACCENT, bold: true })
]}));
children.push(spacer(200));
children.push(new Paragraph({ alignment: AlignmentType.LEFT, children: [
  new TextRun({ text: "Founding Partner\nProgramme", size: 52, font: "Georgia", color: NAVY, bold: true })
]}));
children.push(spacer(300));
children.push(new Paragraph({ children: [
  new TextRun({ text: "Three institutions. Three pilot slots.\nOne question answered.", size: 26, font: "Georgia", color: "666666", italics: true })
]}));
children.push(spacer(800));
children.push(new Paragraph({ children: [
  new TextRun({ text: "March 2026  \u2022  Confidential", size: 20, font: "Georgia", color: "999999" })
]}));
children.push(new Paragraph({ spacing: { before: 100 }, children: [
  new TextRun({ text: "Contact: info@zquas.ai", size: 20, font: "Georgia", color: ACCENT })
]}));

children.push(pageBreak());

// ═══════════════════════════════════════════════════════════
// THE OPPORTUNITY
// ═══════════════════════════════════════════════════════════

children.push(h1("The Opportunity"));

children.push(p("The EU Anti-Money Laundering Regulation (AMLR) takes effect on 10 July 2027. For the first time, Article 75 creates a legal framework for cross-institutional AML information sharing. Every bank in Europe is evaluating how to comply."));

children.push(p("ZQUAS has built the only platform that enables cross-institutional AML detection without sharing any customer data. Using Multi-Party Computation (MPC), banks can jointly identify cross-bank laundering patterns while each institution\u2019s data remains entirely within its own infrastructure. No data extraction. No central database. No GDPR conflict."));

children.push(p("The platform is built, tested, and stress-tested. 29 compliance policies across 9 regulatory domains. GPU-accelerated. Real-time. Cryptographically attestable."));

children.push(pBoldOnly("We are opening three Founding Partner slots for institutions ready to be first."));

children.push(pageBreak());

// ═══════════════════════════════════════════════════════════
// WHAT FOUNDING PARTNERS GET
// ═══════════════════════════════════════════════════════════

children.push(h1("What Founding Partners Receive"));

children.push(h2("1. Founding Partner Pricing"));

children.push(p("50% reduction on all ZQUAS licence fees for 24 months from production go-live. This is not a trial discount. It is a two-year commercial agreement at half the standard rate, in recognition of the early commitment and the value of the partnership."));

children.push(pItalic("Standard licensing is per-institution, per-year. Founding Partner pricing applies to the full platform: edge node, federation, policy engine, and reporting."));

children.push(h2("2. Policy Advisory Board Seat"));

children.push(p("Each Founding Partner receives a permanent seat on the ZQUAS Policy Advisory Board. The Board meets quarterly and provides input on:"));

children.push(pBold("Policy development: ", "which new compliance policies should be added to the standard library. If your institution has a regulatory requirement not covered by the current 29-policy set, it moves to the front of the development queue."));
children.push(pBold("Threshold calibration: ", "review of detection thresholds, false positive rates, and policy effectiveness based on real-world data from the pilot and subsequent deployment."));
children.push(pBold("Product roadmap: ", "influence on platform development priorities: which integrations, which reporting formats, which regulatory jurisdictions are addressed next."));

children.push(pItalic("Advisory Board membership is exclusive to Founding Partners and persists beyond the 24-month pricing period."));

children.push(h2("3. Joint Regulatory Sandbox Engagement"));

children.push(p("ZQUAS co-presents with the Founding Partner at the relevant regulatory sandbox:"));

children.push(new Table({
  width: { size: 8706, type: WidthType.DXA },
  columnWidths: [2200, 2800, 3706],
  rows: [
    new TableRow({ children: [headerCell("Jurisdiction", 2200), headerCell("Sandbox", 2800), headerCell("Benefit to the Bank", 3706)] }),
    new TableRow({ children: [
      cell("Netherlands", 2200), cell("DNB InnovationHub", 2800, true),
      cell("Demonstrates innovation leadership to DNB. Positions the bank as a responsible early adopter of privacy-preserving technology.", 3706)
    ]}),
    new TableRow({ children: [
      cell("United Kingdom", 2200, true), cell("FCA Digital Sandbox", 2800),
      cell("Access to FCA sandbox benefits: regulatory feedback, temporary permissions, and a structured path to production.", 3706, true)
    ]}),
    new TableRow({ children: [
      cell("Nordics / EU", 2200), cell("National FSA sandbox or AMLA engagement", 2800, true),
      cell("Early engagement with AMLA (operational from 2025) on Article 75 partnership compliance.", 3706)
    ]})
  ]
}));

children.push(spacer());

children.push(p("The sandbox engagement is jointly funded. ZQUAS provides the technology, documentation, and regulatory submissions. The bank provides the use case, the data (synthetic or representative), and the regulatory relationship."));

children.push(pItalic("Joint sandbox participation gives the bank innovation credit with their regulator. This is valuable during supervisory assessments."));

children.push(h2("4. Co-Authored Case Study"));

children.push(p("After the pilot, ZQUAS and the Founding Partner jointly publish a case study documenting the results: detection effectiveness, false positive rates, performance metrics, integration experience, and regulatory feedback. The case study is published on both parties\u2019 websites and submitted to industry conferences (ACAMS, CAMS, BAFT, Sibos)."));

children.push(pBold("For the bank\u2019s compliance team: ", "this is a published credential. The MLRO and Head of FCC can present it at industry events, include it in regulatory submissions, and reference it in board reports."));
children.push(pBold("For the bank\u2019s innovation team: ", "this is a proof point for their technology investment thesis."));

children.push(h2("5. Dedicated Integration Support"));

children.push(p("Each Founding Partner is assigned a dedicated integration engineer for the duration of the pilot (typically 8\u201312 weeks). The engineer works with the bank\u2019s IT and compliance teams to:"));

children.push(pBold("Deploy the ZQUAS edge node: ", "on-premises or in the bank\u2019s private cloud. The edge node runs alongside the existing TM system (Actimize, Oracle, SAS, or other). No replacement required."));
children.push(pBold("Configure the data feed: ", "a single integration point (entity identifier + risk score) from the bank\u2019s existing monitoring system to the ZQUAS edge node."));
children.push(pBold("Run the federation: ", "connect to other Founding Partners via the ZQUAS relay infrastructure. Execute bilateral MPC rounds. Validate detection results."));
children.push(pBold("Produce the results: ", "generate the benchmark report, the case study data, and the regulatory submission documentation."));

children.push(pItalic("Integration complexity is deliberately minimal. The edge node consumes risk scores. It does not require access to the bank\u2019s transaction database, core banking system, or customer records."));

children.push(h2("6. Data Sovereignty Guarantee"));

children.push(p("Contractually guaranteed: no customer data leaves the bank\u2019s infrastructure at any point. The ZQUAS edge node processes data locally. The only information transmitted to peer institutions is cryptographic protocol material (elliptic curve points, garbled circuit ciphertexts, oblivious transfer labels) that is computationally indistinguishable from random bytes."));

children.push(p("This guarantee is not a policy. It is a property of the cryptographic protocol. A technical audit can verify it independently."));

children.push(pageBreak());

// ═══════════════════════════════════════════════════════════
// THE PILOT
// ═══════════════════════════════════════════════════════════

children.push(h1("The Pilot"));

children.push(h2("Scope"));

children.push(p("The pilot validates one capability: cross-institutional AML detection using MPC federation, with real compliance policies, against realistic data, under regulatory observation."));

children.push(p("Specifically:"));

children.push(pBold("Entities: ", "minimum 5,000 per institution, up to 500,000 (configurable). Synthetic data with planted typologies or representative data from the bank\u2019s existing monitoring system."));
children.push(pBold("Policies: ", "the full 29-policy ZQUAS Bank Compliance Policy Manual, adapted to each institution\u2019s regulatory perimeter if needed."));
children.push(pBold("Federation: ", "bilateral MPC rounds between all Founding Partners via the ZQUAS relay. End-to-end encrypted, authenticated, with ZAPB attestation."));
children.push(pBold("Detection: ", "four planted laundering typologies (trade-based ML, wire stripping, shell company layering, funnel account structuring) plus legitimate controls. Measured: detection rate, false positive rate, federation time."));

children.push(h2("Timeline"));

children.push(new Table({
  width: { size: 8706, type: WidthType.DXA },
  columnWidths: [1600, 2200, 4906],
  rows: [
    new TableRow({ children: [headerCell("Week", 1600), headerCell("Phase", 2200), headerCell("Activities", 4906)] }),
    new TableRow({ children: [
      cell("1\u20132", 1600), cell("Onboarding", 2200, true),
      cell("Legal agreements signed. Edge node deployed. Data feed configured. Integration engineer on-site or remote.", 4906)
    ]}),
    new TableRow({ children: [
      cell("3\u20134", 1600, true), cell("Validation", 2200),
      cell("Single-institution policy evaluation. Verify 29 policies produce correct results against the bank\u2019s entity data. Calibrate thresholds to the bank\u2019s risk appetite.", 4906, true)
    ]}),
    new TableRow({ children: [
      cell("5\u20138", 1600), cell("Federation", 2200, true),
      cell("Cross-institutional MPC rounds between Founding Partners. Bilateral detection. Measure results. Iterate on any integration issues.", 4906)
    ]}),
    new TableRow({ children: [
      cell("9\u201310", 1600, true), cell("Results", 2200),
      cell("Compile detection results. Benchmark report. Case study draft. Regulatory sandbox submission.", 4906, true)
    ]}),
    new TableRow({ children: [
      cell("11\u201312", 1600), cell("Sandbox", 2200, true),
      cell("Joint presentation to regulator. Demonstrate detection. Discuss GDPR/MPC legal position. Obtain regulatory feedback.", 4906)
    ]})
  ]
}));

children.push(spacer());
children.push(pItalic("Total pilot duration: 12 weeks. No multi-year implementation programme. No committee of committees. Twelve weeks from signature to results."));

children.push(h2("What the bank needs to provide"));

children.push(new Table({
  width: { size: 8706, type: WidthType.DXA },
  columnWidths: [3000, 5706],
  rows: [
    new TableRow({ children: [headerCell("Requirement", 3000), headerCell("Detail", 5706)] }),
    new TableRow({ children: [
      cell("Entity risk data", 3000), cell("Entity identifier + risk score per entity. Synthetic or representative. No raw transaction data required.", 5706, true)
    ]}),
    new TableRow({ children: [
      cell("Infrastructure", 3000, true), cell("One server or VM for the ZQUAS edge node. Minimum: 16 GB RAM, 4 cores, GPU optional (CPU fallback available). Network access to the ZQUAS relay (one outbound TCP connection).", 5706)
    ]}),
    new TableRow({ children: [
      cell("People", 3000), cell("One IT contact (for deployment). One compliance contact (for policy calibration and results review). Part-time commitment, not full-time.", 5706, true)
    ]}),
    new TableRow({ children: [
      cell("Regulatory relationship", 3000, true), cell("Willingness to participate in a joint sandbox submission to the relevant regulator (DNB, FCA, or national FSA).", 5706)
    ]}),
    new TableRow({ children: [
      cell("Legal", 3000), cell("Standard NDA + pilot agreement. ZQUAS provides templates. Typical legal review: 2\u20134 weeks.", 5706, true)
    ]})
  ]
}));

children.push(pageBreak());

// ═══════════════════════════════════════════════════════════
// WHY NOW
// ═══════════════════════════════════════════════════════════

children.push(h1("Why Now"));

children.push(h2("The July 2027 deadline is real"));

children.push(p("AMLR applies directly from 10 July 2027. Unlike previous directives, there is no national transposition period. The regulation is directly applicable in all EU member states from that date. AMLA begins direct supervision of high-risk cross-border institutions in 2028."));

children.push(p("Banks that can demonstrate cross-institutional detection capability before July 2027 are ahead of the compliance curve. Banks that cannot will be responding to regulatory requests after the deadline."));

children.push(h2("First-mover advantage is structural"));

children.push(p("Cross-institutional detection is a network. It becomes more valuable with each institution that joins. The first three banks to deploy MPC federation establish the network. Every subsequent bank that joins benefits from the detection capability the founders built."));

children.push(p("Founding Partners are not just early customers. They are the initial nodes in a network that will ultimately span the entire banking sector. Their influence on policy development, threshold calibration, and governance sets the standard for everyone who follows."));

children.push(h2("The competitive window is narrow"));

children.push(p("ZQUAS is the first platform to combine GPU-native compliance execution with privacy-preserving MPC federation. This will not remain unique indefinitely. Large compliance technology vendors (NICE Actimize, Oracle Financial Crime, SAS) are investing in privacy-enhancing technologies. Academic MPC-AML projects are maturing. The window in which Founding Partners can shape the platform and the market is measured in months, not years."));

children.push(pageBreak());

// ═══════════════════════════════════════════════════════════
// ABOUT ZQUAS
// ═══════════════════════════════════════════════════════════

children.push(h1("About ZQUAS"));

children.push(p("ZQUAS is a GPU-native governance and financial crime compliance platform. The core engine executes deterministic compliance policies in real time on GPU, producing cryptographically attestable decisions for every verdict. Each decision produces a ZAPB (Zero-Trust Adjudication Proof Bundle)."));

children.push(p("The federation layer enables privacy-preserving cross-institutional detection using Multi-Party Computation: ECDH-PSI for entity matching, Yao\u2019s Garbled Circuits for risk comparison, and Oblivious Transfer for secure key exchange. Banks detect cross-bank laundering patterns without any institution accessing any other institution\u2019s data."));

children.push(pBoldOnly("Bounded Compliance on an Unbounded Platform."));

children.push(p("The compliance layer is intentionally restricted: deterministic, sandboxed, bounded execution, cryptographically attestable. The platform underneath is general-purpose GPU compute: real-time, massively parallel, limited only by the hardware."));

children.push(h2("Key metrics (measured, not projected)"));

children.push(new Table({
  width: { size: 8706, type: WidthType.DXA },
  columnWidths: [4400, 4306],
  rows: [
    new TableRow({ children: [headerCell("Capability", 4400), headerCell("Result", 4306)] }),
    new TableRow({ children: [cell("Full pipeline (5K entities/bank, 3 banks)", 4400), cell("344 ms", 4306, true)] }),
    new TableRow({ children: [cell("Full pipeline (500K entities/bank, 3 banks)", 4400, true), cell("7.5 seconds", 4306)] }),
    new TableRow({ children: [cell("97-bank federation (entire Dutch banking sector)", 4400), cell("72.7 seconds", 4306, true)] }),
    new TableRow({ children: [cell("Policy framework", 4400, true), cell("29 policies, 100 rules, 9 domains, 0 discrepancies", 4306)] }),
    new TableRow({ children: [cell("Detection accuracy (4 real-world typologies)", 4400), cell("4/4 detected, per-entity verified at every scale", 4306, true)] }),
    new TableRow({ children: [cell("Transport security", 4400, true), cell("AES-256-GCM + Ed25519 (active on every round, verified)", 4306)] }),
    new TableRow({ children: [cell("False positive rate", 4400), cell("0.00% on realistic moderate-risk population", 4306, true)] }),
    new TableRow({ children: [cell("Endurance (50 epochs)", 4400, true), cell("0 MB memory leak", 4306)] })
  ]
}));

children.push(spacer(200));

children.push(h2("Leadership"));

children.push(p("Founded by Danny de Gier. 18+ years of financial crime compliance across Deutsche Bank, HSBC, RBS, and ABN AMRO. ICA Postgraduate Diploma in Financial Crime (University of Manchester). Former CRO at Vivid Money. Deep regulatory experience across FCA, DNB, BaFin, and ECB supervised institutions."));

children.push(pageBreak());

// ═══════════════════════════════════════════════════════════
// NEXT STEPS
// ═══════════════════════════════════════════════════════════

children.push(h1("Next Steps"));

children.push(p("Three slots. When they are committed, the programme closes."));

children.push(spacer());

children.push(new Table({
  width: { size: 8706, type: WidthType.DXA },
  columnWidths: [800, 2400, 5506],
  rows: [
    new TableRow({ children: [headerCell("Step", 800), headerCell("Action", 2400), headerCell("Detail", 5506)] }),
    new TableRow({ children: [
      cell("1", 800), cell("Expression of Interest", 2400, true),
      cell("Email info@zquas.ai with your institution name, jurisdiction, and primary contact. No commitment required at this stage.", 5506)
    ]}),
    new TableRow({ children: [
      cell("2", 800, true), cell("Technical Briefing", 2400),
      cell("90-minute session (remote or in-person) with ZQUAS engineering and your compliance + IT teams. Live demonstration of the platform. Q&A.", 5506, true)
    ]}),
    new TableRow({ children: [
      cell("3", 800), cell("NDA + Pilot Agreement", 2400, true),
      cell("ZQUAS provides template agreements. Typical legal review: 2\u20134 weeks. No procurement RFP required. This is a pilot, not a full deployment.", 5506)
    ]}),
    new TableRow({ children: [
      cell("4", 800, true), cell("Kick-off", 2400),
      cell("Edge node deployment. Data feed configuration. Integration engineer assigned. The 12-week clock starts.", 5506, true)
    ]})
  ]
}));

children.push(spacer(400));

children.push(new Paragraph({
  spacing: { before: 200, after: 200 },
  border: { top: { style: BorderStyle.SINGLE, size: 4, color: ACCENT, space: 8 }, bottom: { style: BorderStyle.SINGLE, size: 4, color: ACCENT, space: 8 } },
  alignment: AlignmentType.CENTER,
  children: [
    new TextRun({ text: "info@zquas.ai", size: 28, font: "Georgia", color: ACCENT, bold: true }),
    new TextRun({ text: "  \u2022  ", size: 28, font: "Georgia", color: "CCCCCC" }),
    new TextRun({ text: "zquas.ai", size: 28, font: "Georgia", color: ACCENT, bold: true })
  ]
}));

children.push(spacer(400));

children.push(new Paragraph({ children: [
  new TextRun({ text: "This document is confidential and intended for the recipient institution only. The Founding Partner Programme is limited to three institutions. Terms are subject to formal agreement. ZQUAS Bank N.V. referenced in the Policy Manual is a fictitious demonstration institution. The ZQUAS platform and the Founding Partner Programme are offered by ZQUAS (zquas.ai).", italics: true, size: 17, font: "Georgia", color: "999999" })
]}));
children.push(new Paragraph({ spacing: { before: 100 }, children: [
  new TextRun({ text: "\u00A9 2026 ZQUAS. All rights reserved.", italics: true, size: 17, font: "Georgia", color: "999999" })
]}));

// ═══════════════════════════════════════════════════════════
// GENERATE
// ═══════════════════════════════════════════════════════════

const doc = new Document({
  styles: {
    default: { document: { run: { font: "Georgia", size: 22 } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 34, bold: true, font: "Georgia", color: NAVY },
        paragraph: { spacing: { before: 400, after: 240 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 26, bold: true, font: "Georgia", color: NAVY },
        paragraph: { spacing: { before: 320, after: 180 }, outlineLevel: 1 } },
      { id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 22, bold: true, font: "Georgia", color: ACCENT },
        paragraph: { spacing: { before: 240, after: 140 }, outlineLevel: 2 } }
    ]
  },
  sections: [{
    properties: {
      page: { size: { width: 11906, height: 16838 }, margin: { top: 1800, right: 1600, bottom: 1800, left: 1600 } }
    },
    headers: {
      default: new Header({
        children: [new Paragraph({
          tabStops: [{ type: TabStopType.RIGHT, position: 8706 }],
          children: [
            new TextRun({ text: "ZQUAS Founding Partner Programme", size: 16, font: "Georgia", color: "AAAAAA" }),
            new TextRun({ text: "\t" }),
            new TextRun({ text: "Confidential", size: 16, font: "Georgia", color: "CC0000", bold: true })
          ]
        })]
      })
    },
    footers: {
      default: new Footer({
        children: [new Paragraph({
          tabStops: [{ type: TabStopType.CENTER, position: 4353 }, { type: TabStopType.RIGHT, position: 8706 }],
          border: { top: { style: BorderStyle.SINGLE, size: 2, color: "CCCCCC", space: 4 } },
          children: [
            new TextRun({ text: "info@zquas.ai", size: 15, font: "Georgia", color: "AAAAAA" }),
            new TextRun({ text: "\t" }),
            new TextRun({ text: "Page ", size: 15, font: "Georgia", color: "AAAAAA" }),
            new TextRun({ children: [PageNumber.CURRENT], size: 15, font: "Georgia", color: "AAAAAA" }),
            new TextRun({ text: "\t" }),
            new TextRun({ text: "\u00A9 2026 ZQUAS", size: 15, font: "Georgia", color: "AAAAAA" })
          ]
        })]
      })
    },
    children
  }]
});

Packer.toBuffer(doc).then(buffer => {
  const outPath = require("path").join(__dirname, "ZQUAS_Founding_Partner_Programme.docx");
  fs.writeFileSync(outPath, buffer);
  console.log("Generated: " + outPath);
});

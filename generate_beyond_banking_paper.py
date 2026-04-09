"""Generate ZQUAS 'Beyond Banking' cross-sector vision paper PDF -- dark theme.

Generates a professional multi-page PDF of the position paper published at
zquas.ai/article-beyond-banking.html, styled to match the ZQUAS dark-theme
PDF aesthetic.
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
import os

OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      "zquas-beyond-banking-paper.pdf")

# Colors
BG = HexColor("#0a0b0f")
BG_CARD = HexColor("#161722")
BG_TABLE_HEADER = HexColor("#1a1b2e")
BG_TABLE_ALT = HexColor("#0f1015")
TEXT_PRIMARY = HexColor("#e2e4ed")
TEXT_SECONDARY = HexColor("#8890a6")
TEXT_MUTED = HexColor("#565c72")
ACCENT = HexColor("#4a7dff")
ACCENT_DIM = HexColor("#2a4a8f")
GREEN = HexColor("#3FB950")
RED = HexColor("#F85149")
PURPLE = HexColor("#BC8CFF")
ORANGE = HexColor("#D29922")
TEAL = HexColor("#34d399")

W, H = A4
MARGIN = 50
CW = W - 2 * MARGIN
BODY_TOP = H - MARGIN - 40
BODY_BOTTOM = MARGIN + 35

page_num = [0]


# ---------- low-level helpers ---------- #

def draw_bg(c):
    c.setFillColor(BG)
    c.rect(0, 0, W, H, fill=1, stroke=0)


def draw_line(c, y, color=ACCENT_DIM, width=0.5):
    c.setStrokeColor(color)
    c.setLineWidth(width)
    c.line(MARGIN, y, W - MARGIN, y)


def draw_header_footer(c, page_title):
    page_num[0] += 1
    y = H - MARGIN
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(TEXT_PRIMARY)
    c.drawString(MARGIN, y, "ZQUAS")
    c.setFont("Helvetica", 7.5)
    c.setFillColor(TEXT_MUTED)
    c.drawRightString(W - MARGIN, y + 2, page_title)
    draw_line(c, y - 8, ACCENT, 1.5)

    fy = MARGIN + 14
    draw_line(c, fy, ACCENT, 0.75)
    fy -= 12
    c.setFont("Helvetica", 7)
    c.setFillColor(TEXT_MUTED)
    c.drawString(MARGIN, fy,
                 "zquas.ai  |  danny@zquas.ai  |  "
                 "linkedin.com/in/danny-de-gier-prof-pgdip-fcc/")
    c.drawRightString(W - MARGIN, fy, str(page_num[0]))


def new_page(c, title="Position Paper"):
    if page_num[0] > 0:
        c.showPage()
    draw_bg(c)
    draw_header_footer(c, title)
    return BODY_TOP


def wrap_lines(text, font, size, max_width):
    words = text.split()
    lines, current = [], ""
    for word in words:
        test = current + (" " if current else "") + word
        if pdfmetrics.stringWidth(test, font, size) > max_width:
            if current:
                lines.append(current)
            current = word
        else:
            current = test
    if current:
        lines.append(current)
    return lines


# ---------- Writer ---------- #

class Writer:
    def __init__(self, c, page_title="Position Paper"):
        self.c = c
        self.page_title = page_title
        self.y = new_page(c, page_title)

    def _ensure(self, needed):
        if self.y - needed < BODY_BOTTOM:
            self.y = new_page(self.c, self.page_title)

    def para(self, text, font="Helvetica", size=9.2, color=TEXT_SECONDARY,
             max_width=None, indent=0, spacing=8):
        if max_width is None:
            max_width = CW - indent
        leading = size + 4
        lines = wrap_lines(text, font, size, max_width)
        for line in lines:
            self._ensure(leading)
            self.c.setFont(font, size)
            self.c.setFillColor(color)
            self.c.drawString(MARGIN + indent, self.y, line)
            self.y -= leading
        self.y -= spacing

    def bold_para(self, text, **kw):
        kw.setdefault("font", "Helvetica-Bold")
        kw.setdefault("color", TEXT_PRIMARY)
        self.para(text, **kw)

    def italic_para(self, text, **kw):
        kw.setdefault("font", "Helvetica-Oblique")
        kw.setdefault("color", TEXT_MUTED)
        self.para(text, **kw)

    def section(self, title, size=13):
        self._ensure(size + 20)
        self.y -= 6
        self.c.setFont("Helvetica-Bold", size)
        self.c.setFillColor(ACCENT)
        self.c.drawString(MARGIN, self.y, title)
        self.y -= size + 8

    def subsection(self, title, size=10.5):
        self._ensure(size + 16)
        self.y -= 3
        self.c.setFont("Helvetica-Bold", size)
        self.c.setFillColor(TEXT_PRIMARY)
        self.c.drawString(MARGIN, self.y, title)
        self.y -= size + 6

    def bullet(self, label, text, indent=12):
        self._ensure(13 * 2)
        self.c.setFont("Helvetica-Bold", 9.2)
        self.c.setFillColor(ACCENT)
        self.c.drawString(MARGIN + indent, self.y, label)
        lw = pdfmetrics.stringWidth(label, "Helvetica-Bold", 9.2) + 6
        lines = wrap_lines(text, "Helvetica", 9, CW - indent - lw)
        self.c.setFont("Helvetica", 9)
        self.c.setFillColor(TEXT_SECONDARY)
        for i, line in enumerate(lines):
            if i == 0:
                self.c.drawString(MARGIN + indent + lw, self.y, line)
            else:
                self._ensure(13)
                self.c.drawString(MARGIN + indent + lw, self.y, line)
            self.y -= 13
        self.y -= 3

    def spacer(self, pts=8):
        self.y -= pts

    def accent_line(self, color=ACCENT_DIM, width=0.5):
        self._ensure(6)
        draw_line(self.c, self.y, color, width)
        self.y -= 8

    def card(self, title, lines_text, color=ACCENT, width=CW, indent=0):
        line_h = 13
        card_h = 24 + len(lines_text) * line_h + 6
        self._ensure(card_h + 4)
        x = MARGIN + indent
        self.c.setFillColor(BG_CARD)
        self.c.roundRect(x, self.y - card_h + 10, width, card_h, 6,
                         fill=1, stroke=0)
        self.c.setStrokeColor(color)
        self.c.setLineWidth(1.5)
        self.c.line(x, self.y - card_h + 10, x, self.y + 10)
        iy = self.y + 2
        self.c.setFont("Helvetica-Bold", 9.5)
        self.c.setFillColor(color)
        self.c.drawString(x + 10, iy, title)
        iy -= 16
        self.c.setFont("Helvetica", 8.5)
        self.c.setFillColor(TEXT_SECONDARY)
        for lt in lines_text:
            self.c.drawString(x + 10, iy, lt)
            iy -= line_h
        self.y -= card_h + 2

    def callout(self, text):
        leading = 12.5
        lines = wrap_lines(text, "Helvetica-Oblique", 9, CW - 24)
        box_h = len(lines) * leading + 16
        self._ensure(box_h + 4)
        self.c.setFillColor(BG_CARD)
        self.c.roundRect(MARGIN, self.y - box_h + 8, CW, box_h, 6,
                         fill=1, stroke=0)
        self.c.setStrokeColor(GREEN)
        self.c.setLineWidth(2)
        self.c.line(MARGIN, self.y - box_h + 8, MARGIN, self.y + 8)
        iy = self.y
        self.c.setFont("Helvetica-Oblique", 9)
        self.c.setFillColor(TEXT_PRIMARY)
        for line in lines:
            self.c.drawString(MARGIN + 12, iy, line)
            iy -= leading
        self.y -= box_h + 4

    def table(self, headers, rows, col_widths, font_size=8):
        row_h = 16
        header_h = 18
        total_h = header_h + row_h * len(rows) + 4
        self._ensure(min(total_h, 200))
        y = self.y
        # header
        self.c.setFillColor(BG_TABLE_HEADER)
        self.c.rect(MARGIN, y - header_h + 4, CW, header_h, fill=1, stroke=0)
        tx = MARGIN
        for i, h in enumerate(headers):
            self.c.setFont("Helvetica-Bold", 7)
            self.c.setFillColor(ACCENT)
            self.c.drawString(tx + 5, y - 8, h.upper())
            tx += col_widths[i]
        y -= header_h + 1
        # rows
        for ri, row in enumerate(rows):
            if y - row_h < BODY_BOTTOM:
                self.y = y
                y = new_page(self.c, self.page_title)
            if ri % 2 == 0:
                self.c.setFillColor(BG_TABLE_ALT)
                self.c.rect(MARGIN, y - row_h + 4, CW, row_h, fill=1,
                            stroke=0)
            tx = MARGIN
            for ci, cell in enumerate(row):
                if ci == 0:
                    self.c.setFont("Helvetica-Bold", font_size)
                    self.c.setFillColor(TEXT_PRIMARY)
                else:
                    self.c.setFont("Helvetica", font_size)
                    self.c.setFillColor(TEXT_SECONDARY)
                self.c.drawString(tx + 5, y - 8, cell)
                tx += col_widths[ci]
            y -= row_h
        self.y = y - 4


# ================================================================== #
#                          CONTENT                                     #
# ================================================================== #

def build_pdf():
    c = canvas.Canvas(OUTPUT, pagesize=A4)
    c.setTitle("Beyond Banking: Cross-Sector Federated Detection for "
               "Financial Crime, Telecommunications Fraud, and Digital "
               "Asset Compliance")
    c.setAuthor("Danny de Gier")
    c.setSubject("ZQUAS Position Paper - April 2026")

    w = Writer(c)

    # ===== COVER / TITLE ===== #
    w.spacer(40)
    w.c.setFont("Helvetica", 9)
    w.c.setFillColor(TEXT_MUTED)
    w.c.drawString(MARGIN, w.y, "ZQUAS POSITION PAPER  \u00b7  APRIL 2026")
    w.y -= 24

    title = ("Beyond Banking: Cross-Sector Federated Detection for Financial "
             "Crime, Telecommunications Fraud, and Digital Asset Compliance")
    w.c.setFont("Helvetica-Bold", 20)
    w.c.setFillColor(TEXT_PRIMARY)
    lines = wrap_lines(title, "Helvetica-Bold", 20, CW)
    for line in lines:
        w.c.drawString(MARGIN, w.y, line)
        w.y -= 26
    w.y -= 4

    w.accent_line(ACCENT, 2)

    w.para(
        "A single detection engine that correlates risk signals across "
        "banks, telecommunications operators, and digital asset platforms "
        "without sharing raw data between institutions. The same code, the "
        "same cryptographic protocols, the same GPU-native detection "
        "pipeline, applied to every regulated sector where financial crime "
        "operates.",
        size=10.5, color=TEXT_PRIMARY, spacing=14)

    w.c.setFont("Helvetica-Oblique", 9)
    w.c.setFillColor(TEXT_MUTED)
    w.c.drawString(MARGIN, w.y,
                   "Danny de Gier, Founder ZQUAS. 18 years financial crime "
                   "compliance:")
    w.y -= 13
    w.c.drawString(MARGIN, w.y,
                   "Deutsche Bank, HSBC, RBS, ABN AMRO, ClearBank, Vivid "
                   "Money. PGDip FCC, University of Manchester.")
    w.y -= 20

    w.accent_line()

    # ===== 1. THE CROSS-SECTOR PROBLEM ===== #
    w.section("1. The Cross-Sector Problem")

    w.para(
        "Financial crime does not respect institutional boundaries. It does "
        "not respect sectoral boundaries either.")

    w.para(
        "An Authorised Push Payment fraud starts with a phone call. The "
        "fraudster calls the victim, impersonating their bank. The call is "
        "routed through a telecommunications network. The victim transfers "
        "funds to a \"safe account\" controlled by the fraudster. The money "
        "moves through two or three bank accounts within minutes. Within "
        "hours, it exits through a cryptocurrency exchange into a "
        "stablecoin, crosses a blockchain bridge, and arrives in a "
        "jurisdiction with no bilateral cooperation agreement.")

    w.para(
        "The telecommunications operator saw the call. It came from a number "
        "that contacted 47 different people in the past week. The telco did "
        "not share this information with the bank.")

    w.para(
        "The bank saw the payment. A high-value transfer to a first-time "
        "payee, initiated within two hours of an inbound call. The bank did "
        "not know about the call because it has no access to "
        "telecommunications data.")

    w.para(
        "The cryptocurrency exchange saw the deposit. Funds arriving from a "
        "bank account opened three weeks ago, immediately converted to "
        "stablecoin and bridged to another chain. The exchange did not know "
        "the funds originated from an impersonation fraud.")

    w.bold_para(
        "Three institutions. Three data domains. Three independent compliance "
        "systems. Each one sees a fragment. None of them sees the crime.")

    w.para(
        "According to the UK Finance Annual Fraud Report 2025, criminals "
        "stole GBP 1.17 billion through payment fraud in 2024, of which "
        "GBP 450.7 million was lost to APP fraud alone. 70 per cent of APP "
        "fraud cases started online. 16 per cent originated through "
        "telecommunications networks.")

    w.bold_para(
        "The criminals have cross-sector visibility. The compliance "
        "infrastructure does not.")

    # ===== 2. WHAT EXISTS TODAY ===== #
    w.section("2. What Exists Today")

    w.para(
        "The ZQUAS F1 Engine is a GPU-native financial crime detection "
        "engine comprising approximately 253,000 lines of C++ and CUDA code. "
        "It is not a prototype, a proof of concept, or a roadmap. The "
        "banking detection pipeline is production-ready.")

    w.subsection("2.1 Banking Detection: Production-Ready")
    w.para(
        "The engine processes 500,000 entities in under 2 seconds with an "
        "alert lifecycle under 10 milliseconds. Total VRAM consumption is "
        "under 1 gigabyte. It runs on hardware ranging from a consumer-grade "
        "laptop GPU to data centre GPUs (A100, H100). The detection pipeline "
        "evaluates five layers covering temporal analysis, structural graph "
        "analysis, behavioural profiling, corridor analysis, and flow path "
        "reconstruction. All five layers execute on GPU with over 100 "
        "compiled compliance policies.")

    w.subsection("2.2 Bank-to-Bank Federation: Production-Ready")
    w.para(
        "The federation protocol implements Elliptic Curve Diffie-Hellman "
        "Private Set Intersection (ECDH-PSI) for entity matching, bilateral "
        "escalation signal propagation, and cryptographic evidence "
        "attestation. Federation rounds complete in under 10 seconds per "
        "bilateral pair.")

    w.subsection("2.3 Financial Crime Network Simulator: Production-Ready")
    w.para(
        "The F1 Engine includes a GPU-native simulation environment that "
        "generates synthetic banking populations with embedded criminal "
        "networks. 15 criminal typologies (8 AML, 7 APP fraud) generate "
        "realistic transaction data on GPU. The simulator is calibrated "
        "against published national statistics for three jurisdictions "
        "(Netherlands, United Kingdom, Germany). Over 300 tests pass.")

    w.subsection("2.4 Maturity Summary")
    w.table(
        ["Capability", "Status"],
        [
            ["Banking transaction ingestion", "Production-ready. Deployed."],
            ["Bank-to-bank federation (ECDH-PSI)", "Production-ready. Tested."],
            ["Five-layer detection pipeline (GPU)", "Production-ready. 100+ policies."],
            ["FCNS (15 typologies)", "Production-ready. 300+ tests."],
            ["Evidence system + blind assessment", "Production-ready. Implemented."],
            ["Deterministic entity hashing", "Production-ready. Implemented."],
            ["Cryptographic erasure (per-entity keys)", "Production-ready. Implemented."],
            ["Differential privacy on federation", "Architecture designed. Phase 2."],
            ["Signal velocity circuit breaker", "Architecture designed. Phase 2."],
            ["Cross-sector score calibration", "Architecture designed. Phase 2."],
            ["Telco ingestion (CDR/TMDR)", "Planned. Phase 2 (Q3 2026)."],
            ["Blockchain ingestion (EVM/UTXO)", "Planned. Phase 3 (Q4 2026)."],
        ],
        [250, CW - 250],
    )

    w.callout(
        "Everything in this paper that is described as \"architecture\" or "
        "\"planned\" is clearly labelled as such. Everything described "
        "without qualification is built, tested, and operational.")

    # ===== 3. THE REGULATORY DIRECTION ===== #
    w.section("3. The Regulatory Direction")

    w.para(
        "Regulators are converging on cross-sector responsibility. The "
        "evidence is unambiguous.")

    w.subsection("3.1 Singapore: Shared Responsibility Framework")
    w.para(
        "Singapore's MAS and IMDA implemented the Shared Responsibility "
        "Framework on 16 December 2024. It is the first regulatory framework "
        "to hold both financial institutions and telecommunications operators "
        "jointly liable for fraud losses. The framework operates on a "
        "waterfall principle. MAS added a fraud surveillance duty effective "
        "16 June 2025, requiring banks to detect and block suspicious "
        "transactions in real time.")

    w.subsection("3.2 United Kingdom: Converging Frameworks")
    w.para(
        "The PSR's APP fraud reimbursement regime (7 October 2024) requires "
        "PSPs to reimburse victims up to GBP 85,000 within five business "
        "days. The UK Telecommunications Fraud Sector Charter (5 November "
        "2025) commits telcos to cross-industry intelligence sharing. "
        "Ofcom's consultation on combatting mobile messaging scams (29 "
        "October 2025) proposes mandatory KYC for business message senders. "
        "The Data (Use and Access) Act 2025 establishes crime and fraud "
        "prevention as a lawful basis for data sharing. The UK Fraud "
        "Strategy 2026-2029 calls for cross-sector collaboration, supported "
        "by the new Operational Crime Centre launching April 2026.")

    w.subsection("3.3 European Union: AMLR Article 75 and MiCA")
    w.para(
        "AMLR Article 75 mandates mechanisms for cross-institutional "
        "information sharing. AMLA assumes oversight from 2027. MiCA became "
        "fully applicable in December 2024. CASPs now have the same "
        "compliance obligations as banks. When a stablecoin payment "
        "originates at a bank, transits a blockchain, and settles at an "
        "exchange, every entity in the chain is regulated. The technology "
        "to correlate signals across those steps does not exist.")

    w.subsection("3.4 SWIFT: The Institutional Blockchain Transition")
    w.para(
        "SWIFT announced on 29 September 2025 that it will add a "
        "blockchain-based shared ledger to its infrastructure, developed "
        "with over 30 financial institutions. When institutional settlement "
        "moves onto permissioned chains, the public transparency that "
        "Chainalysis and Elliptic rely on disappears. Consensus is not "
        "detection. Detection requires behavioural analysis across the "
        "entity graph over time. The cross-sector gap remains even when "
        "the intra-sector gap narrows.")

    # ===== 4. THE ARCHITECTURE ===== #
    w.section("4. The Architecture")

    w.subsection("4.1 Design Principle")
    w.para(
        "The F1 Engine operates on entities and relationships. A bank "
        "customer who is also a mobile subscriber who is also a crypto "
        "exchange user is one entity with three institutional views. At the "
        "federation layer, the engine treats all data sources uniformly: a "
        "sender, a receiver, a value, and a timestamp.")

    w.subsection("4.2 The Four-Installation Federation")

    w.card("BANKING INSTITUTION", [
        "F1 Edge Installation in bank's data centre.",
        "Transaction monitoring, entity risk assessment.",
        "Status: Production-ready.",
    ], ACCENT)

    w.card("TELECOMMUNICATIONS OPERATOR", [
        "F1 Edge Installation in telco's data centre.",
        "CDR/TMDR analysis, scam pattern detection.",
        "Status: Planned, Phase 2 (Q3 2026).",
    ], ORANGE)

    w.card("DIGITAL ASSET PLATFORM", [
        "F1 Edge Installation at exchange.",
        "On-chain/off-chain analysis, bridge and mixer detection.",
        "Status: Planned, Phase 3 (Q4 2026).",
    ], PURPLE)

    w.card("REGULATORY OBSERVER", [
        "Read-only interface for regulators.",
        "Aggregated metrics, detection rates, false positive rates.",
        "No entity-level data. Measures quality, not just quantity.",
    ], TEAL)

    w.subsection("4.3 Cross-Sector Entity Matching")
    w.para(
        "The critical technical challenge is linking the same person across "
        "institutional boundaries without sharing personal data. In the "
        "target launch jurisdictions, a single government identifier serves "
        "as the natural join key. In the Netherlands, the BSN is mandatory "
        "at banks (Wwft), telcos (SIM registration), and crypto exchanges "
        "(Wwft). The UK uses the National Insurance number and passport.")

    w.para(
        "The F1 Engine uses ECDH-PSI to discover common entities without "
        "revealing identity data. The protocol is GPU-accelerated and "
        "provably secure under standard cryptographic assumptions.")

    w.bold_para("Two-Tier Entity Matching:")
    w.bullet("\u2022 Tier 1: ",
             "Government ID hash. Primary mechanism for AML detection. "
             "Same person laundering across institutions using the same "
             "identity.")
    w.bullet("\u2022 Tier 2: ",
             "Phone number hash (E.164). Primary mechanism for APP fraud. "
             "Links the victim across telco and bank. The fraudster and "
             "mule are different people. The victim is the join key.")

    w.subsection("4.4 The Normalisation Pipeline")
    w.para(
        "PSI operates on exact hash matches. Deterministic normalisation "
        "before hashing (case, punctuation, whitespace, abbreviation, ISO "
        "formatting) ensures consistent matching. The pipeline runs locally "
        "at each institution before any data enters the cryptographic "
        "protocol.")

    w.subsection("4.5 Signal Propagation and Privacy Protection")
    w.para(
        "Each installation computes local risk assessments. When an entity "
        "warrants cross-institutional attention, an escalation signal "
        "propagates to matched peers. No raw transactions, CDRs, blockchain "
        "addresses, or customer names cross institutional boundaries.")

    w.callout(
        "In the current production architecture, federation signals are "
        "binary escalations: escalated or not escalated. Binary signals are "
        "mathematically immune to threshold drift. There is no intermediate "
        "value that noise, rounding, or miscalibration can degrade.")

    w.para(
        "Escalation signals are batched into federation rounds that "
        "aggregate multiple events. The receiving institution cannot "
        "determine which specific event triggered the escalation or when it "
        "occurred. This defeats inference attacks based on timing "
        "correlations.")

    w.subsection("4.6 Intersection Privacy and Anti-Leakage Controls")
    w.para(
        "Three controls mitigate commercial sensitivity of intersection "
        "metadata: (1) Risk-filtered PSI: only entities exceeding a local "
        "risk threshold enter the PSI set. (2) Ephemeral intersection: "
        "matched identifiers are discarded after the federation round. "
        "(3) PSI query budgets: limits on rounds per bilateral pair per "
        "period prevent incremental customer-base mapping.")

    w.subsection("4.7 Cross-Sector Score Calibration (Planned)")
    w.para(
        "The simulator generates synthetic populations with cross-sector "
        "activity. Calibration is computed bilaterally. Both institutions "
        "verify the mapping against the same ground truth. Bilateral "
        "calibration floors ensure poorly calibrated installations improve "
        "before influencing the federation. The signal velocity circuit "
        "breaker catches aggressive installations. The calibration floor "
        "catches negligent ones. Together they bound signal quality from "
        "both directions.")

    w.subsection("4.8 The APP Fraud Detection Example: Victim-Centric Linkage")
    w.para(
        "In professional APP fraud, the fraudster and the mule are different "
        "people. The architecture centres linkage on the victim.")

    w.bold_para("Step 1: Telco detects scam pattern.")
    w.para(
        "Burner SIM calls 200 potential victims. Burst calling pattern "
        "detected. Each targeted subscriber flagged locally. No data "
        "leaves the telco.", indent=12)

    w.bold_para("Step 2: Federation round: PSI match on phone number.")
    w.para(
        "Victim's phone number appears in both the telco's risk set and "
        "the bank's customer set. Match identifies the victim, not the "
        "fraudster.", indent=12)

    w.bold_para("Step 3: Escalation signal propagates to bank.")
    w.para(
        "\"This customer is being targeted by a telecommunications scam "
        "pattern.\" No call details, no timing, no number shared.", indent=12)

    w.bold_para("Step 4: Victim initiates payment to mule account.")
    w.para(
        "Bank's detection pipeline combines cross-sector signal + first-time "
        "payee + high-value transfer. Alert in under 10ms.", indent=12)

    w.bold_para("Step 5: Payment held. Fraud lifecycle broken.")
    w.para(
        "Only the specific high-risk payment is held. Salary, direct debits, "
        "routine transactions continue uninterrupted.", indent=12)

    w.callout(
        "The architecture does not need to unmask the fraudster to protect "
        "the victim. By correlating the targeting signal at the telco with "
        "the transfer signal at the bank, the fraud lifecycle is broken "
        "before the first payment settles.")

    w.subsection("4.9 The Private Blockchain Detection Example")
    w.para(
        "A bank customer initiates a GBP payment through SWIFT's "
        "blockchain-based ledger. The recipient converts the stablecoin "
        "to a different token via a regulated bridge. The tokens are sent "
        "to a mixer. On the permissioned chain: only participating banks "
        "see the transaction. On the public chain: no link back to the "
        "originating bank payment.")

    w.para(
        "With cross-sector federation: the bank's F1 installation assesses "
        "the originating entity. The CASP's F1 installation assesses the "
        "bridge user. PSI matches the entity across both (same government "
        "ID at KYC). The CASP's escalation signal propagates to the bank. "
        "Without federation: neither connects the dots.")

    w.subsection("4.10 Evidence Attestation")
    w.para(
        "The regulatory observer receives aggregated metrics. When a case "
        "requires law enforcement action, the F1 Engine generates an "
        "evidence package: investigation items from the detecting "
        "institution's own data, a cryptographic attestation transcript "
        "signed by each participating installation, and sector attribution "
        "indicating which sectors contributed signals. The prosecutor can "
        "demonstrate cross-sector criminal activity without the "
        "institutions ever having seen each other's files.")

    w.subsection("4.11 Protocol Governance")
    w.para(
        "Nobody decides what to detect. Everybody decides how to share. "
        "Each institution compiles its own detection policies. They only "
        "agree on how to share the output: entity-level escalation signals. "
        "Protocol governance is limited to: data format versioning, "
        "federation round timing, PSI parameters, privacy budgets, query "
        "limits, and signal quality floors.")

    # ===== 5. GDPR COMPLIANCE ===== #
    w.section("5. GDPR Compliance Architecture")

    w.bullet("\u2022 No raw data sharing: ",
             "No customer data, transaction records, CDRs, or blockchain "
             "addresses cross boundaries. Only binary escalation signals.")
    w.bullet("\u2022 Cryptographic matching: ",
             "ECDH-PSI blinds all identity data before comparison. Provably "
             "secure under standard assumptions.")
    w.bullet("\u2022 Lawful basis: ",
             "Data (Use and Access) Act 2025 and AMLR Article 75 provide "
             "the foundation for crime prevention data sharing.")
    w.bullet("\u2022 Cryptographic erasure: ",
             "GDPR Article 17 right to erasure via hierarchical per-entity "
             "key deletion. Signed destruction receipts.")
    w.bullet("\u2022 Purpose limitation: ",
             "Escalation signals do not reveal the underlying reason. "
             "Bank learns \"elevated risk from telecommunications\" but "
             "not the specific activity.")
    w.bullet("\u2022 No mass surveillance: ",
             "PSI operates on risk-filtered entity sets, not full customer "
             "bases. No central database. Each institution retains full "
             "sovereignty.")

    # ===== 6. TELCO VALUE PROPOSITION ===== #
    w.section("6. The Telco Value Proposition")

    w.para(
        "Singapore has implemented shared liability. The UK Fraud Sector "
        "Charter commits telcos to cross-industry intelligence sharing. "
        "Australia's Scam Prevention Framework imposes penalties up to "
        "AUD 50 million for non-compliance. The direction is global and "
        "irreversible.")

    w.para(
        "Under shared liability frameworks, not participating is more "
        "damaging than participating. A telco that could have flagged risk "
        "but did not faces financial liability and regulatory enforcement. "
        "The federation protocol shares an escalation signal, not an "
        "admission. The telco is demonstrating vigilance, not confessing "
        "failure.")

    w.para(
        "According to the CFCA's 2023 Global Fraud Loss Survey, "
        "telecommunications fraud losses reached USD 38.95 billion globally "
        "in 2023, representing 2.5 per cent of industry revenues. The "
        "F1 Edge Installation runs inside the telco's data centre, on the "
        "telco's hardware, under the telco's operational control.")

    # ===== 7. CRYPTO EXCHANGE VALUE PROPOSITION ===== #
    w.section("7. The Crypto Exchange Value Proposition")

    w.para(
        "MiCA requires CASPs to implement transaction monitoring equivalent "
        "to traditional financial institutions. Most exchanges check wallet "
        "blacklists. They cannot detect novel laundering patterns or the "
        "intersection of on-chain and off-chain activity.")

    w.para(
        "As institutional adoption moves settlement onto permissioned "
        "blockchains, public transparency diminishes. Exchanges that "
        "correlate risk signals across both public and private chains have "
        "a structural advantage. The FATF Travel Rule requires originator "
        "and beneficiary information to be transmitted with virtual asset "
        "transfers. The federation protocol can facilitate compliance by "
        "confirming entity identity matches without revealing underlying "
        "data.")

    # ===== 8. THE MARKET GAP ===== #
    w.section("8. The Market Gap")

    w.bold_para(
        "No company in the world offers a cross-sector federated detection "
        "platform.")

    w.para(
        "Telecommunications fraud vendors (Subex, SEON, Vonage) protect "
        "telcos from fraud on their own networks. They do not share "
        "detection signals with banks.")

    w.para(
        "Banking AML vendors (NICE Actimize, Feedzai, Tookitaki, Oracle "
        "Financial Crime) monitor transactions within a single bank. Some "
        "offer consortium models but none include telecommunications or "
        "blockchain data.")

    w.para(
        "Blockchain analytics firms (Chainalysis, Elliptic, Merkle Science) "
        "analyse public chain data. Their model depends on public blockchain "
        "transparency, which will diminish.")

    w.para(
        "ZQUAS is the only platform architected to process banking, "
        "telecommunications, and blockchain data in a single GPU-native "
        "detection pipeline, connected by a privacy-preserving federation "
        "protocol across all three sectors.")

    # ===== 9. HONEST LIMITATIONS ===== #
    w.section("9. Honest Limitations")

    w.bullet("\u2022 Federation speed: ",
             "Local detection under 10ms. Federation enrichment under 10s "
             "per bilateral round. A window of seconds to minutes exists "
             "for newly identified signals, vs. hours/days in batch.")
    w.bullet("\u2022 Adoption: ",
             "Network effect requires a minimum viable consortium. Initial "
             "deployment targets regulated groups rather than individual "
             "institutions.")
    w.bullet("\u2022 Jurisdiction-specific legal work: ",
             "Lawful basis established in principle. Operational boundaries "
             "still being defined per jurisdiction.")
    w.bullet("\u2022 Cross-sector calibration: ",
             "No cross-sector detection calibration methodology exists "
             "today. Simulation-based approach requires validation through "
             "pilot deployments.")
    w.bullet("\u2022 Multi-hop attenuation: ",
             "Bilateral federation propagates one hop. Hub-spoke topology "
             "designed but not yet deployed.")
    w.bullet("\u2022 ID fragmentation: ",
             "In jurisdictions without a universal identifier, multi-ID "
             "hashing mitigates but does not eliminate false negatives.")

    # ===== 10. TIMELINE ===== #
    w.section("10. Timeline")

    w.card("PHASE 1: Current", [
        "Banking federation. Pilot validation.",
        "Status: Production-ready.",
    ], GREEN)
    w.card("PHASE 2: Q3 2026", [
        "Telecommunications integration. CDR/TMDR ingestion.",
        "Cross-sector PSI on phone number and government ID.",
        "Differential privacy, signal velocity circuit breaker.",
    ], ORANGE)
    w.card("PHASE 3: Q4 2026", [
        "Digital asset integration. Blockchain event ingestion.",
        "Wallet-to-identity linking via exchange KYC.",
    ], PURPLE)
    w.card("PHASE 4: 2027", [
        "Regulatory interface. AMLA Article 75 reporting.",
        "Hub-spoke topology for multi-hop propagation.",
    ], ACCENT)

    w.spacer(6)
    w.bold_para("AMLR Article 75 applies: July 10, 2027. Cross-institutional "
                "information sharing mandated.", color=RED)

    # ===== 11. CONCLUSION ===== #
    w.section("11. Conclusion")

    w.para(
        "The financial crime industry has spent twenty years optimising "
        "detection within institutional silos. The criminals have spent "
        "twenty years exploiting the gaps between those silos. The gaps are "
        "now wider than ever: spanning banking, telecommunications, "
        "cryptocurrency, and private institutional blockchains.")

    w.para(
        "The regulatory response is converging. Singapore has implemented "
        "cross-sector liability. The UK is building the framework. The EU "
        "mandates cross-institutional sharing under AMLR. MiCA brings "
        "crypto exchanges into the regulated perimeter.")

    w.para(
        "The technology to match this regulatory direction did not exist. A "
        "detection engine that operates across banking, telecommunications, "
        "and blockchain data, connected by a federation protocol that shares "
        "escalation signals without sharing raw data, running at the speed "
        "required for real-time intervention, governed by the institutions "
        "that use it rather than a central authority.")

    w.bold_para(
        "We do not need to unmask the fraudster to protect the victim. By "
        "correlating the targeting signal at the telco with the transfer "
        "signal at the bank, we break the fraud lifecycle before the first "
        "payment settles.")

    w.para(
        "The banking detection engine is built. The federation protocol is "
        "built. The simulation environment is built. The cross-sector "
        "extensions are engineering milestones on an operational foundation.")

    w.bold_para("It exists now.")

    w.spacer(10)
    w.accent_line(ACCENT, 1.5)
    w.spacer(4)

    w.c.setFont("Helvetica-Oblique", 10)
    w.c.setFillColor(TEXT_PRIMARY)
    w.c.drawString(MARGIN, w.y,
                   "ZQUAS. The criminals have cross-sector visibility.")
    w.y -= 14
    w.c.drawString(MARGIN, w.y,
                   "Now the compliance infrastructure does too.")
    w.y -= 20

    w.c.setFont("Helvetica-Bold", 9)
    w.c.setFillColor(TEXT_SECONDARY)
    w.c.drawString(MARGIN, w.y,
                   "Contact: Danny de Gier  |  danny@zquas.ai  |  zquas.ai")
    w.y -= 18
    w.c.setFont("Helvetica", 8)
    w.c.setFillColor(TEXT_MUTED)
    w.c.drawString(MARGIN, w.y,
                   "\u00a9 2026 ZQUAS. All rights reserved. Implementation "
                   "details and protocol specifications are proprietary.")

    c.save()
    print(f"PDF generated: {OUTPUT}  ({page_num[0]} pages)")


if __name__ == "__main__":
    build_pdf()

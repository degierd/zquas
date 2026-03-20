"""Generate ZQUAS F1 Engine Capability Overview PDF -- dark theme house style."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
import os

OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      "zquas-f1-engine-capability-overview.pdf")

# Colors (matching zquas.ai)
BG = HexColor("#0a0b0f")
BG_CARD = HexColor("#161722")
BG_TABLE_HEADER = HexColor("#1a1b2e")
BG_TABLE_ALT = HexColor("#0f1015")
TEXT_PRIMARY = HexColor("#e2e4ed")
TEXT_SECONDARY = HexColor("#8890a6")
TEXT_MUTED = HexColor("#565c72")
ACCENT = HexColor("#4a7dff")
ACCENT_DIM = HexColor("#2a4a8f")

W, H = A4
MARGIN = 40
CW = W - 2 * MARGIN


def draw_bg(c):
    c.setFillColor(BG)
    c.rect(0, 0, W, H, fill=1, stroke=0)


def draw_line(c, y, color=ACCENT_DIM, width=0.5):
    c.setStrokeColor(color)
    c.setLineWidth(width)
    c.line(MARGIN, y, W - MARGIN, y)


def draw_header_footer(c, page_title, page_num, total_pages):
    y = H - MARGIN
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(TEXT_PRIMARY)
    c.drawString(MARGIN, y, "ZQUAS")
    c.setFont("Helvetica", 8)
    c.setFillColor(TEXT_MUTED)
    c.drawRightString(W - MARGIN, y + 2, page_title)
    y -= 8
    draw_line(c, y, ACCENT, 1.5)
    fy = MARGIN + 14
    draw_line(c, fy, ACCENT, 0.75)
    fy -= 12
    c.setFont("Helvetica", 7)
    c.setFillColor(TEXT_MUTED)
    c.drawString(MARGIN, fy,
                 "zquas.ai  |  danny@zquas.ai  |  linkedin.com/in/danny-de-gier-prof-pgdip-fcc/")
    c.drawRightString(W - MARGIN, fy, f"{page_num} / {total_pages}")


def wrap_text(c, x, y, text, size=9, color=TEXT_SECONDARY, font="Helvetica",
              max_width=None, leading=None):
    if max_width is None:
        max_width = CW
    if leading is None:
        leading = size + 3.5
    c.setFont(font, size)
    c.setFillColor(color)
    words = text.split()
    lines = []
    current = ""
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
    for i, line in enumerate(lines):
        c.drawString(x, y - i * leading, line)
    return y - len(lines) * leading


def section_header(c, y, label, size=12):
    c.setFont("Helvetica-Bold", size)
    c.setFillColor(TEXT_PRIMARY)
    c.drawString(MARGIN, y, label)
    return y - (size + 6)


def draw_dot(c, x, y):
    c.setFillColor(ACCENT)
    c.circle(x, y + 3, 1.8, fill=1, stroke=0)


def draw_table(c, y, headers, rows, col_widths, font_size=7.5, row_h=None, header_h=17,
               wrap_cols=None):
    """Draw a table with optional text wrapping in specified columns."""
    if wrap_cols is None:
        wrap_cols = set()

    # Header
    c.setFillColor(BG_TABLE_HEADER)
    c.rect(MARGIN, y - header_h + 4, CW, header_h, fill=1, stroke=0)
    tx = MARGIN
    for i, h in enumerate(headers):
        c.setFont("Helvetica-Bold", 7)
        c.setFillColor(ACCENT)
        c.drawString(tx + 5, y - 8, h.upper())
        tx += col_widths[i]
    y -= header_h + 1

    for ri, row in enumerate(rows):
        # Calculate row height based on wrapped text
        max_lines = 1
        for ci, cell in enumerate(row):
            if ci in wrap_cols:
                cw = col_widths[ci] - 10
                words = cell.split()
                lines = []
                current = ""
                for word in words:
                    test = current + (" " if current else "") + word
                    if pdfmetrics.stringWidth(test, "Helvetica-Bold" if ci == len(row) - 1 else "Helvetica", font_size) > cw:
                        if current:
                            lines.append(current)
                        current = word
                    else:
                        current = test
                if current:
                    lines.append(current)
                max_lines = max(max_lines, len(lines))
        actual_row_h = max(max_lines * (font_size + 3) + 6, 14)

        if ri % 2 == 0:
            c.setFillColor(BG_TABLE_ALT)
            c.rect(MARGIN, y - actual_row_h + 4, CW, actual_row_h, fill=1, stroke=0)

        tx = MARGIN
        for ci, cell in enumerate(row):
            is_last_col = ci == len(row) - 1
            if ci == 0:
                c.setFont("Helvetica", font_size)
                c.setFillColor(TEXT_SECONDARY)
            elif is_last_col:
                c.setFont("Helvetica-Bold", font_size)
                c.setFillColor(ACCENT)
            else:
                c.setFont("Helvetica", font_size)
                c.setFillColor(TEXT_MUTED)

            if ci in wrap_cols:
                cw = col_widths[ci] - 10
                font_name = "Helvetica-Bold" if is_last_col else "Helvetica"
                col_color = ACCENT if is_last_col else (TEXT_MUTED if ci > 0 else TEXT_SECONDARY)
                wrap_text(c, tx + 5, y - 8, cell, size=font_size, color=col_color,
                          font=font_name, max_width=cw, leading=font_size + 3)
            else:
                c.drawString(tx + 5, y - 8, cell)
            tx += col_widths[ci]
        y -= actual_row_h
    return y


TOTAL = 5


# ═══════════════════════════════════════
# PAGE 1: Title + What It Replaces
# ═══════════════════════════════════════
def page1(c):
    draw_bg(c)
    draw_header_footer(c, "F1 Engine Capability Overview", 1, TOTAL)

    y = H - MARGIN - 28

    # Hero
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(ACCENT)
    c.drawString(MARGIN, y, "ZQUAS F1 ENGINE")
    y -= 22

    y = wrap_text(c, MARGIN, y,
                  "One Engine. Everything AML. Nothing Shared.",
                  size=22, color=TEXT_PRIMARY, font="Helvetica-Bold", leading=28)
    y -= 8

    y = wrap_text(c, MARGIN, y,
                  "A single GPU-native platform that replaces the entire AML technology stack, "
                  "from sanctions screening to cross-institutional federation, running locally "
                  "at each bank with zero data leaving the institution.",
                  size=9, color=TEXT_SECONDARY, leading=13)
    y -= 14
    draw_line(c, y, ACCENT, 1)
    y -= 18

    # What It Replaces
    y = section_header(c, y, "What It Replaces")

    headers = ["Current Stack", "Vendor(s)", "ZQUAS Replacement"]
    widths = [120, 130, CW - 250]
    rows = [
        ["Sanctions screening", "Fircosoft, Dow Jones, Refinitiv",
         "GPU policy evaluation (29 AML policies, under 2 seconds)"],
        ["PEP / adverse media", "World-Check, LexisNexis",
         "Integrated in policy engine (CPL rules, 0.5% PEP threshold)"],
        ["Transaction monitoring", "Actimize, Norkom, SAS, Sentinels",
         "Real-time GPU evaluation (not batch, under 10ms alert lifecycle)"],
        ["Name / entity matching", "Fircosoft, Quantexa",
         "GPU identity resolution (canonical IDs, diacritic-aware)"],
        ["Case management", "Actimize, custom",
         "Operator Console (6 roles, investigation workspace, SAR filing)"],
        ["Suspicious Activity Reporting", "Manual / custom",
         "Constitutional governance (agents recommend, MLRO approves)"],
        ["Network analytics", "Quantexa, SynapseGrid",
         "GPU graph propagation (cross-bank contagion detection)"],
        ["Cross-bank detection", "TMNL (shut down)",
         "Privacy-preserving federation (ECDH-PSI + Garbled Circuits)"],
        ["Regulatory reporting", "Custom / Excel",
         "Cryptographic proof per decision (Ed25519-signed, regulator verifies offline)"],
    ]
    y = draw_table(c, y, headers, rows, widths, font_size=7, row_h=24, wrap_cols={1, 2})

    y -= 10
    y = wrap_text(c, MARGIN, y,
                  "All of the above runs on a single GPU at each bank. One deployment. "
                  "One codebase. One team to maintain. Total VRAM: under 1 GB.",
                  size=8.5, color=TEXT_PRIMARY, font="Helvetica-Bold", leading=12)


# ═══════════════════════════════════════
# PAGE 2: The Pipeline + Key Differentiators
# ═══════════════════════════════════════
def page2(c):
    draw_bg(c)
    draw_header_footer(c, "Pipeline & Differentiators", 2, TOTAL)

    y = H - MARGIN - 28

    y = section_header(c, y, "The Pipeline")
    y = wrap_text(c, MARGIN, y,
                  "Every entity at the bank passes through six stages. The full pipeline "
                  "executes in under 2 seconds for 500,000 entities.",
                  size=8.5, leading=12)
    y -= 6

    headers = ["Stage", "What Happens", "Output"]
    widths = [80, 250, CW - 330]
    rows = [
        ["1. Ingestion",
         "CSV, API, or real-time feed. Multilingual column mapping (Dutch, German, French, English).",
         "Entities in semantic knowledge graph"],
        ["2. Evaluation",
         "Every entity evaluated against 100 AML policies on GPU. 150 million+ evaluations/second.",
         "Risk score + verdict per entity per policy"],
        ["3. Proof",
         "Every evaluation produces an Ed25519-signed cryptographic proof. Independently verifiable.",
         "Proof bundle (Merkle root + signature)"],
        ["4. Triage",
         "50,000 GPU-resident agents assess every entity in under 10ms. Constitutional gate: no autonomous SARs.",
         "Clear / Monitor / Investigate / Escalate"],
        ["5. Federation",
         "All entities enter bilateral PSI with partner banks. Under 10 seconds per round. No raw data shared.",
         "Shared entity matches + risk escalations"],
        ["6. Network Detection",
         "Risk propagates across transaction + identity edges in unified GPU pass. Cross-bank patterns emerge.",
         "Mule networks, layering chains, circular flows"],
    ]
    y = draw_table(c, y, headers, rows, widths, font_size=7, wrap_cols={1, 2})

    y -= 10
    draw_line(c, y)
    y -= 16

    # Key Differentiators
    y = section_header(c, y, "Key Differentiators")

    diffs = [
        ("Compliance Policy Language (CPL): ",
         "Domain-specific language for AML policy definition. Compiled to GPU bytecode with guaranteed "
         "termination. 29 AML policies across sanctions, PEP screening, transaction monitoring, fraud "
         "detection, KYC/KYB, crypto/VASP, proliferation financing, and AI agent governance. Identical "
         "results on CPU and GPU. Hot-reloadable: policy amendments take effect immediately without restart."),
        ("Semantic Knowledge Graph: ",
         "Multi-domain entity model with per-field provenance tracking. GPU-optimised entity storage. "
         "Every fact about every entity has a tracked origin, confidence score, and timestamp."),
        ("Constitutional Agent Governance: ",
         "50,000 autonomous AML agents on GPU, each with per-agent resource budgets, Ed25519-signed "
         "warrants, and a constitutional gate. Agents recommend actions but cannot file SARs. A human "
         "MLRO must approve every SAR. Multiple independent defence layers prevent autonomous SAR filing."),
    ]
    for label, text in diffs:
        draw_dot(c, MARGIN + 4, y)
        full = label + text
        y = wrap_text(c, MARGIN + 14, y, full, size=7.5, max_width=CW - 14, leading=10.5)
        y -= 6


# ═══════════════════════════════════════
# PAGE 3: Federation + Graph Propagation
# ═══════════════════════════════════════
def page3(c):
    draw_bg(c)
    draw_header_footer(c, "Federation & Detection", 3, TOTAL)

    y = H - MARGIN - 28

    # Privacy-Preserving Federation
    y = section_header(c, y, "Privacy-Preserving Federation")

    y = wrap_text(c, MARGIN, y,
                  "Real multi-party computation using established cryptographic protocols: Private Set "
                  "Intersection for entity matching, Garbled Circuits for secure comparison, Oblivious "
                  "Transfer for key exchange. Semi-honest security model (appropriate for regulated "
                  "consortiums). AES-256-GCM transport encryption mandatory. Entity count padding hides "
                  "set sizes. Dual Ed25519 attestation: both parties sign, regulator verifies. "
                  "GPU-accelerated. Scales from 5 banks to 500+ without code changes.",
                  size=8.5, leading=12)

    y -= 14
    draw_line(c, y)
    y -= 16

    # Cross-Institutional Graph Propagation
    y = section_header(c, y, "Cross-Institutional Graph Propagation")

    y = wrap_text(c, MARGIN, y,
                  "When federation identifies shared entities, the engine creates cross-bank identity "
                  "edges. Risk propagation traverses both transaction and identity edges in a single GPU "
                  "pass. Risk flows from one bank's transaction network, across the identity bridge, into "
                  "the other bank's network. Detects layering chains, mule networks, and circular flows "
                  "that are invisible to any individual bank.",
                  size=8.5, leading=12)

    y -= 14
    draw_line(c, y)
    y -= 16

    # Measured Performance
    y = section_header(c, y, "Measured Performance")

    y = wrap_text(c, MARGIN, y,
                  "Conservative thresholds. All figures measured on NVIDIA RTX 5090. Actual measurements "
                  "consistently exceed published figures.",
                  size=8, color=TEXT_MUTED, leading=11)
    y -= 6

    headers = ["Metric", "Performance"]
    widths = [220, CW - 220]
    rows = [
        ["500,000 entities x 100 policies", "Under 2 seconds"],
        ["Policy throughput", "150 million+ evaluations/second"],
        ["Alert lifecycle (ingestion to triage)", "Under 10 milliseconds"],
        ["Federation per bilateral round", "Under 10 seconds"],
        ["Agent triage (50,000 entities)", "Under 10 milliseconds"],
        ["Total GPU memory", "Under 1 GB"],
        ["Automated tests", "7,200+"],
        ["Scaling", "Linear (2x entities = 2x time)"],
    ]
    y = draw_table(c, y, headers, rows, widths, font_size=7.5, row_h=14)

    y -= 14
    draw_line(c, y)
    y -= 16

    # Verification & Auditability
    y = section_header(c, y, "Verification & Auditability")

    headers = ["Capability", "Detail"]
    widths = [160, CW - 160]
    rows = [
        ["Cryptographic proof per decision",
         "Ed25519-signed proof bundle with Merkle root. Regulator verifies offline with public key only."],
        ["Every primitive RFC/NIST verified",
         "Ed25519: RFC 8032. SHA-256: FIPS 180-4. Blake3: official reference vectors."],
        ["Continuous safety verification",
         "Static analysis across entire codebase. Pre-commit gate enforces invariants on every change."],
        ["Semi-honest MPC security",
         "Based on ECDLP. Transport: AES-256-GCM. Mutual authentication on every federation round."],
        ["Regulatory submissions",
         "DNB InnovationHub: under review. FCA Digital Sandbox: submitted."],
    ]
    y = draw_table(c, y, headers, rows, widths, font_size=7, wrap_cols={1}, row_h=24)


# ═══════════════════════════════════════
# PAGE 4: Operator Console
# ═══════════════════════════════════════
def page4(c):
    draw_bg(c)
    draw_header_footer(c, "Operator Console", 4, TOTAL)

    y = H - MARGIN - 28

    y = section_header(c, y, "Operator Console")

    y = wrap_text(c, MARGIN, y,
                  "Web-based investigation workspace. Six roles: Analyst, Investigator, MLRO, "
                  "Compliance Officer, Administrator, Regulator. Each role sees only what CPL "
                  "access policies permit. Bloomberg/Linear dark-theme aesthetic.",
                  size=9, leading=13)
    y -= 10

    headers = ["Feature", "What It Does"]
    widths = [140, CW - 140]
    rows = [
        ["Intelligence Surface", "Real-time KPIs, risk distribution, alert feed"],
        ["Alert Queue", "Keyboard navigable (J/K/Enter), ranked by composite risk"],
        ["Investigation Workspace",
         "Entity profile, counterparty graph, risk timeline, AI-generated narrative, "
         "proof panel, provenance badges"],
        ["SAR Filing",
         "Viewport attestation, typology selection, proof hash. Constitutional gate: MLRO-only."],
        ["Federation Demo", "Configure peers, run MPC round, view escalations"],
        ["Regulator Portal",
         "Aggregate view only. No individual entity data. Proof verification with governance public key."],
        ["Policy Management",
         "View/branch/amend CPL policies. Dual-approve for constitutional amendments."],
        ["Internationalisation", "en-GB + nl-NL (188 translation keys, 1:1 parity)"],
    ]
    y = draw_table(c, y, headers, rows, widths, font_size=7.5, wrap_cols={1}, row_h=20)

    y -= 18
    draw_line(c, y)
    y -= 22

    # Stats summary
    y = section_header(c, y, "At a Glance")

    stats = [
        ("150M+", "policy evaluations/sec"),
        ("<2s", "500K entities, 100 policies"),
        ("<10ms", "alert lifecycle"),
        ("<10s", "federation per round"),
        ("<1 GB", "total VRAM"),
        ("7,200+", "automated tests"),
    ]

    col_w = CW / 3
    for i, (val, label) in enumerate(stats):
        col = i % 3
        row = i // 3
        sx = MARGIN + col * col_w
        sy = y - row * 50

        c.setFont("Helvetica-Bold", 18)
        c.setFillColor(ACCENT)
        c.drawString(sx, sy, val)
        c.setFont("Helvetica", 8)
        c.setFillColor(TEXT_SECONDARY)
        c.drawString(sx, sy - 15, label)

    y -= 120
    draw_line(c, y)
    y -= 16

    y = wrap_text(c, MARGIN, y,
                  "All numbers measured on NVIDIA RTX 5090. Medians of 3 runs, 10 warmup iterations. "
                  "Every result signed.",
                  size=7.5, color=TEXT_MUTED, leading=10.5)


# ═══════════════════════════════════════
# PAGE 5: Founder + Contact
# ═══════════════════════════════════════
def page5(c):
    draw_bg(c)
    draw_header_footer(c, "Confidential", 5, TOTAL)

    y = H - MARGIN - 28

    # Founder
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(TEXT_PRIMARY)
    c.drawString(MARGIN, y, "Danny de Gier")
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(ACCENT)
    c.drawString(MARGIN + pdfmetrics.stringWidth("Danny de Gier  ", "Helvetica-Bold", 12), y + 1,
                 "Founder & Engineer")
    y -= 20

    y = wrap_text(c, MARGIN, y,
                  "18 years in financial crime compliance at Tier-1 banks and fintechs. Senior roles at "
                  "Deutsche Bank, HSBC, RBS, ABN AMRO, ClearBank, Vivid Money. Board Member, Statutory "
                  "Director, Group CRCO, Group DPO. Professional Postgraduate Diploma in Financial Crime "
                  "Compliance (International Compliance Association / University of Manchester). Direct "
                  "regulatory engagement: FCA, FED, DNB, independent monitors.",
                  size=8.5, leading=12)

    y -= 8

    y = wrap_text(c, MARGIN, y,
                  "Self-taught GPU systems programmer. C++23, CUDA (sm_86/89/100/120), Vulkan. Built the "
                  "entire ZQUAS engine as a solo developer: policy language compiler, GPU adjudication "
                  "kernel, MPC protocol implementation, cryptographic attestation pipeline, adversarial "
                  "testing framework, entity resolution graph, rendering engine.",
                  size=8.5, leading=12)

    y -= 14
    draw_line(c, y)
    y -= 18

    # Contact
    y = section_header(c, y, "Contact")

    contact = [
        "danny@zquas.ai",
        "zquas.ai",
        "linkedin.com/in/danny-de-gier-prof-pgdip-fcc/",
        "Zwolle, Netherlands",
    ]
    for line in contact:
        c.setFont("Helvetica", 9)
        c.setFillColor(TEXT_SECONDARY)
        c.drawCentredString(W / 2, y, line)
        y -= 14

    y -= 16

    # Confidential notice
    c.setFont("Helvetica", 8)
    c.setFillColor(TEXT_MUTED)
    c.drawCentredString(W / 2, y, "CONFIDENTIAL  ---  March 2026")

    y -= 30

    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(ACCENT)
    c.drawCentredString(W / 2, y,
                        "The architecture is ready. The regulatory window is open. Let's talk.")


# ═══════════════════════════════════════
def main():
    c = canvas.Canvas(OUTPUT, pagesize=A4)
    c.setTitle("ZQUAS F1 Engine - Capability Overview")
    c.setAuthor("Danny de Gier")
    c.setSubject("GPU-Native Compliance Engine for Regulated Finance")

    page1(c)
    c.showPage()
    page2(c)
    c.showPage()
    page3(c)
    c.showPage()
    page4(c)
    c.showPage()
    page5(c)
    c.showPage()
    c.save()
    print(f"PDF generated: {OUTPUT}")


if __name__ == "__main__":
    main()

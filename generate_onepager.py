"""Generate ZQUAS 4-page executive briefing PDF -- dark theme."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
import os

OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "zquas-onepager.pdf")

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


def draw_header_footer(c, page_title, page_num):
    # Header
    y = H - MARGIN
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(TEXT_PRIMARY)
    c.drawString(MARGIN, y, "ZQUAS")
    c.setFont("Helvetica", 8)
    c.setFillColor(TEXT_MUTED)
    c.drawRightString(W - MARGIN, y + 2, page_title)
    y -= 8
    draw_line(c, y, ACCENT, 1.5)

    # Footer
    fy = MARGIN + 14
    draw_line(c, fy, ACCENT, 0.75)
    fy -= 12
    c.setFont("Helvetica", 7)
    c.setFillColor(TEXT_MUTED)
    c.drawString(MARGIN, fy,
                 "zquas.ai  |  danny@zquas.ai  |  linkedin.com/in/danny-de-gier-prof-pgdip-fcc/")
    c.drawRightString(W - MARGIN, fy, str(page_num))


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


def sub_header(c, x, y, label, size=10):
    c.setFont("Helvetica-Bold", size)
    c.setFillColor(TEXT_PRIMARY)
    c.drawString(x, y, label)
    return y - (size + 4)


def draw_bullet(c, x, y, label, text, max_width, label_size=10, text_size=9):
    c.setFont("Helvetica-Bold", label_size)
    c.setFillColor(TEXT_PRIMARY)
    c.drawString(x, y, label)
    y -= label_size + 3
    y = wrap_text(c, x, y, text, size=text_size, max_width=max_width, leading=12)
    return y - 5


def draw_card_rect(c, x, y, w, h):
    c.setFillColor(BG_CARD)
    c.roundRect(x, y, w, h, 6, fill=1, stroke=0)


def draw_dot(c, x, y):
    c.setFillColor(ACCENT)
    c.circle(x, y + 3, 1.8, fill=1, stroke=0)


def draw_table(c, y, headers, rows, col_widths, font_size=8, row_h=15, header_h=17):
    """Draw a table. Returns y after table."""
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

    # Rows
    for ri, row in enumerate(rows):
        if ri % 2 == 0:
            c.setFillColor(BG_TABLE_ALT)
            c.rect(MARGIN, y - row_h + 4, CW, row_h, fill=1, stroke=0)
        tx = MARGIN
        for ci, cell in enumerate(row):
            is_last_col = ci == len(row) - 1
            if ci == 0:
                c.setFont("Helvetica", font_size)
                c.setFillColor(TEXT_SECONDARY)
            elif is_last_col:
                if cell.startswith("No"):
                    c.setFont("Helvetica", font_size)
                    c.setFillColor(TEXT_MUTED)
                elif cell.startswith("Yes") or cell == "Continuous (GPU)":
                    c.setFont("Helvetica-Bold", font_size)
                    c.setFillColor(ACCENT)
                else:
                    c.setFont("Helvetica-Bold", font_size)
                    c.setFillColor(ACCENT)
            else:
                if cell.startswith("No"):
                    c.setFont("Helvetica", font_size)
                    c.setFillColor(TEXT_MUTED)
                else:
                    c.setFont("Helvetica", font_size)
                    c.setFillColor(TEXT_MUTED)
            c.drawString(tx + 5, y - 8, cell)
            tx += col_widths[ci]
        y -= row_h
    return y


# ========== PAGE 1: Problem & Solution ==========

def page1(c):
    draw_bg(c)
    draw_header_footer(c, "Executive Briefing", 1)

    y = H - MARGIN - 28

    # Hero title
    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(TEXT_PRIMARY)
    y = wrap_text(c, MARGIN, y,
                  "Sovereign Compliance Infrastructure for Regulated Finance",
                  size=20, color=TEXT_PRIMARY, font="Helvetica-Bold", leading=25)
    y -= 4

    y = wrap_text(c, MARGIN, y,
                  "GPU-native compliance engine enabling cross-institutional financial crime "
                  "detection without central data pooling. Every decision cryptographically "
                  "attested. Every verdict independently verifiable.",
                  size=9, color=TEXT_SECONDARY, leading=13)
    y -= 14

    # Stats row
    stat_w = CW / 3
    stats = [
        ("2.58M", "COMPLIANCE EVENTS / SEC"),
        ("29", "POLICIES IN PARALLEL"),
        ("8", "REGULATORY STANDARDS"),
    ]
    for i, (val, label) in enumerate(stats):
        sx = MARGIN + i * stat_w
        c.setFont("Helvetica-Bold", 16)
        c.setFillColor(ACCENT)
        c.drawString(sx, y, val)
        c.setFont("Helvetica", 7)
        c.setFillColor(TEXT_MUTED)
        c.drawString(sx, y - 13, label)

    y -= 32
    draw_line(c, y)
    y -= 18

    # The Problem
    y = section_header(c, y, "The Problem")

    problems = [
        ("Siloed Detection: ",
         "Money laundering networks operate across banks. Individual institutions see "
         "fragments. An estimated 16 billion euros is laundered through the Netherlands "
         "alone each year. Less than 1% of illicit funds are intercepted."),
        ("Privacy vs. Detection: ",
         "Joint monitoring initiatives have stalled. Centralising transaction data triggers "
         "GDPR objections. The EU AMLR (effective mid-2027) restricts data sharing to "
         "pre-identified high-risk customers only."),
        ("Legacy Architecture: ",
         "95% false positive rates. Overnight batch processing on CPU rule engines. "
         "50-100M+ euros annual compliance operations cost per Tier-1 bank. 5,500+ AML "
         "staff in the Netherlands alone."),
    ]

    for label, text in problems:
        draw_dot(c, MARGIN + 4, y)
        c.setFont("Helvetica-Bold", 9)
        c.setFillColor(TEXT_PRIMARY)
        c.drawString(MARGIN + 14, y, label.rstrip())
        y -= 13
        y = wrap_text(c, MARGIN + 14, y, text, size=9, max_width=CW - 14, leading=12)
        y -= 4

    y -= 6
    draw_line(c, y)
    y -= 18

    # The Solution
    y = section_header(c, y, "The Solution")

    col_w = (CW - 18) / 2
    left_x = MARGIN
    right_x = MARGIN + col_w + 18

    left_items = [
        ("GPU-Native Processing",
         "Full policy sets evaluated against every transaction simultaneously on GPU. "
         "Real-time, not batch. 2.58M compliance events per second on a single node."),
        ("Privacy-Preserving MPC",
         "Cross-institutional detection via GPU-accelerated secure multi-party computation. "
         "No central data pool. No GDPR exposure. Each bank retains full data sovereignty."),
        ("Cryptographic Attestation",
         "Every compliance decision produces an Ed25519-signed proof bundle with Merkle "
         "roots. Regulators verify independently with a standalone CLI tool."),
    ]
    right_items = [
        ("Constitutional Governance",
         "Zero-bypass enforcement. Every automated action requires a cryptographic warrant. "
         "Metered execution prevents runaway processes. Policy inclusion verifiable via "
         "Sparse Merkle Tree."),
        ("Deterministic Evaluation",
         "Policy language compiled to GPU bytecode. Same input + same policy = same verdict. "
         "Always. Reproducible by any party at any time."),
        ("Entity Resolution at GPU Speed",
         "GPU-resident identity graph with GNN-based risk propagation. Full network context "
         "for every decision in real time."),
    ]

    ly = y
    ry = y
    for label, text in left_items:
        ly = draw_bullet(c, left_x, ly, label, text, col_w)
    for label, text in right_items:
        ry = draw_bullet(c, right_x, ry, label, text, col_w)


# ========== PAGE 2: Full Capability Overview ==========

def page2(c):
    draw_bg(c)
    draw_header_footer(c, "Platform Capabilities", 2)

    y = H - MARGIN - 28

    # Core Engine
    y = section_header(c, y, "Core Engine")

    engine_headers = ["Capability", "Detail"]
    engine_widths = [140, CW - 140]
    engine_rows = [
        ["Processing speed", "2.58M CEPS (29 policies, 8 domains, single RTX 5090)"],
        ["Policy language", "CPL: lexer, parser, semantic analyser, compiler to GPU bytecode"],
        ["Adjudication pipeline", "Triple-stream GPU: Load (H2D), Adjudicate (kernel), Commit (D2H + sign)"],
        ["Determinism", "Byte-identical replay guaranteed. Fixed-point arithmetic where applicable"],
        ["Entity resolution", "GPU-resident double-buffered hash table (~1.34GB VRAM), GNN risk scoring"],
        ["Proof generation", "ZAPB: verdict hash (SipHash-128), Merkle proof, Ed25519 signature (912 bytes)"],
        ["ZK governance proofs", "GPU-accelerated PLONK + IPA with BabyJubJub/Poseidon primitives"],
    ]
    y = draw_table(c, y, engine_headers, engine_rows, engine_widths, font_size=7.5, row_h=14)

    y -= 10
    draw_line(c, y)
    y -= 16

    # Governance & Safety
    y = section_header(c, y, "Governance & Safety")

    gov_items = [
        ("ExecutionGate: ", "Zero-bypass enforcement point. No code path circumvents governance."),
        ("WarrantAuthority: ", "Ephemeral Ed25519 keypairs. Scoped, time-limited, non-reusable action warrants."),
        ("GasMeter: ", "Monotonic per-agent gas ledger. 16 sharded mutexes. Prevents resource exhaustion."),
        ("Janus Prediction: ", "Forward simulation of compliance state. Predicts budget depletion, warrant "
         "expiry, and coverage gaps before they occur. Q32.32 fixed-point deterministic projection."),
    ]
    for label, text in gov_items:
        draw_dot(c, MARGIN + 4, y)
        full = label + text
        y = wrap_text(c, MARGIN + 14, y, full, size=8.5, max_width=CW - 14, leading=11.5)
        y -= 4

    y -= 6
    draw_line(c, y)
    y -= 16

    # Detection Intelligence
    y = section_header(c, y, "Detection Intelligence")

    det_items = [
        ("Semantic Knowledge Graph: ", "7-domain ontology (Ontology, Topology, Dynamics, Epistemics, "
         "Salience, Affordance, Projection). Contextual reasoning beyond raw transaction patterns."),
        ("Multi-Timeline Evaluation: ", "Same entity evaluated under multiple policy versions simultaneously "
         "on GPU. Scenario analysis, impact assessment, and counterfactual replay at compliance speed."),
        ("Cross-Institutional MPC: ", "ABY3 replicated secret sharing. GPU-accelerated Kogge-Stone prefix "
         "adder, oblivious bitonic sort, Catrina-Saxena truncation. Federation protocol with ECDH-PSI "
         "and garbled circuits."),
    ]
    for label, text in det_items:
        draw_dot(c, MARGIN + 4, y)
        full = label + text
        y = wrap_text(c, MARGIN + 14, y, full, size=8.5, max_width=CW - 14, leading=11.5)
        y -= 4

    y -= 6
    draw_line(c, y)
    y -= 16

    # Continuous Verification
    y = section_header(c, y, "Continuous Verification")

    ver_items = [
        ("Sentinel Adversarial Framework: ", "13+ subsystems. GPU-accelerated fuzzing, decision surface "
         "cartography, adversarial oracle. Two-gate deployment pipeline (pre-commit + CI/CD)."),
        ("GapDetector: ", "Real-time policy coverage mapping against registered regulatory frameworks. "
         "Gaps identified automatically, continuously."),
        ("Build Attestation: ", "BLAKE3 + SHA-256 + Ed25519 embedded in binary. Runtime self-verification. "
         "Compiler version and git commit recorded. Reproducible builds."),
    ]
    for label, text in ver_items:
        draw_dot(c, MARGIN + 4, y)
        full = label + text
        y = wrap_text(c, MARGIN + 14, y, full, size=8.5, max_width=CW - 14, leading=11.5)
        y -= 4

    y -= 6
    draw_line(c, y)
    y -= 16

    # Integration
    y = section_header(c, y, "Integration")

    int_items = [
        ("Ingest: ", "256MB shared memory ring buffer. Lock-free atomic indices. JSON/REST, raw binary, "
         "GPU-Direct bypass. Configurable backpressure (drop newest, drop oldest, block)."),
        ("Export: ", "RAW and CEF formats for SIEM (Splunk, QRadar, Sentinel). Zero-copy flat encoding. "
         "Domain-tagged BLAKE3 integrity. Every exported verdict traceable to its proof bundle."),
    ]
    for label, text in int_items:
        draw_dot(c, MARGIN + 4, y)
        full = label + text
        y = wrap_text(c, MARGIN + 14, y, full, size=8.5, max_width=CW - 14, leading=11.5)
        y -= 4


# ========== PAGE 3: Market, Competition & Traction ==========

def page3(c):
    draw_bg(c)
    draw_header_footer(c, "Market & Positioning", 3)

    y = H - MARGIN - 28

    # Market Opportunity
    y = section_header(c, y, "Market Opportunity")

    market = [
        "200B+ euros annual global compliance spending. Growing 15-20% per year. Banks "
        "allocate 10-20% of operating budgets to compliance.",
        "AMLR mid-2027 creates a hard regulatory deadline. Every European bank must "
        "re-architect. EU AI Act classifies AML as high-risk with mandatory technical "
        "standards from August 2026.",
        "Cross-institutional detection proven valuable (TMNL demonstrated this over 4 years) "
        "but centralised architecture failed on privacy. MPC-based alternative has no "
        "competitors.",
    ]
    for text in market:
        draw_dot(c, MARGIN + 4, y)
        y = wrap_text(c, MARGIN + 14, y, text, size=9, max_width=CW - 14, leading=12)
        y -= 5

    y -= 8
    draw_line(c, y)
    y -= 18

    # Competitive Landscape
    y = section_header(c, y, "Competitive Landscape")

    comp_headers = ["", "Legacy Incumbents", "AI-Native Challengers", "ZQUAS"]
    comp_widths = [120, 130, 130, CW - 380]
    comp_rows = [
        ["Examples", "NICE Actimize, Oracle, SAS", "Sardine ($145M), Hawk ($56M)", "---"],
        ["Architecture", "CPU batch, rules-based", "CPU cloud, ML-based", "GPU-native, MPC + ZK"],
        ["Cross-bank detection", "No", "No", "Yes (privacy-preserving)"],
        ["Cryptographic proof", "No", "No", "Yes (Ed25519, Merkle)"],
        ["Deterministic eval", "No", "No", "Yes (byte-identical)"],
        ["Real-time at scale", "Limited", "Partial", "2.58M events/sec"],
        ["Adversarial self-testing", "No", "No", "Continuous (GPU)"],
        ["Regulator verification", "Trust-based", "Trust-based", "Independent CLI"],
        ["Replication timeline", "N/A", "N/A", "3-5 years minimum"],
    ]
    y = draw_table(c, y, comp_headers, comp_rows, comp_widths, font_size=7.5, row_h=14)

    y -= 10
    draw_line(c, y)
    y -= 18

    # Traction
    y = section_header(c, y, "Traction")

    traction = [
        "DNB InnovationHub: Submission under review",
        "FCA Sandbox: Regulatory sandbox programme engaged",
        "Benchmark: 2.58M CEPS on RTX 5090 with 29-policy Tier-1 bank set",
        "Detection fidelity: 1.25M transaction simulation (HSBC-modelled patterns)",
        "Test coverage: ~3,869 unit tests across engine subsystems",
        "Regulatory frameworks: EU AI Act, AMLR, FATF R15, NIST AI RMF, ISO 42001, MAS TRM, GDPR, DORA",
    ]
    for text in traction:
        draw_dot(c, MARGIN + 4, y)
        y = wrap_text(c, MARGIN + 14, y, text, size=8.5, max_width=CW - 14, leading=11.5)
        y -= 3

    y -= 8
    draw_line(c, y)
    y -= 18

    # Business Model
    y = section_header(c, y, "Business Model")

    phases = [
        ("Land: ", "Single-bank on-premise deployment. Annual licensing by transaction volume "
         "and policy complexity. Bank's data never leaves its infrastructure."),
        ("Expand: ", "Additional business lines, policy domains, jurisdictions within existing "
         "banks. Net revenue retention above 100%."),
        ("Network: ", "Cross-institutional MPC activates as network grows. Each new node "
         "increases detection for all participants. Network effects compound. Switching costs "
         "deepen with cryptographic audit chain."),
    ]
    for label, text in phases:
        c.setFont("Helvetica-Bold", 9)
        c.setFillColor(ACCENT)
        c.drawString(MARGIN, y, label.rstrip())
        y -= 13
        y = wrap_text(c, MARGIN, y, text, size=9, max_width=CW, leading=12)
        y -= 5


# ========== PAGE 4: Founder, Engineering & Contact ==========

def page4(c):
    draw_bg(c)
    draw_header_footer(c, "Founder & Engineering", 4)

    y = H - MARGIN - 28

    # Founder
    y = section_header(c, y, "Founder")

    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(TEXT_PRIMARY)
    c.drawString(MARGIN, y, "Danny de Gier")
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(ACCENT)
    c.drawString(MARGIN + pdfmetrics.stringWidth("Danny de Gier  ", "Helvetica-Bold", 12), y + 1,
                 "Founder & Engineer")
    y -= 18

    col_w = (CW - 18) / 2
    left_x = MARGIN
    right_x = MARGIN + col_w + 18

    # Left column: Compliance Career
    ly = y
    ly = sub_header(c, left_x, ly, "Compliance Career")
    ly = wrap_text(c, left_x, ly,
                   "18+ years in financial crime compliance at Tier-1 banks and fintechs. "
                   "Senior roles at RBS, Deutsche Bank, HSBC, and Commerzbank. Fintech "
                   "compliance leadership at ClearBank, Vivid Money, and CoinMetro. "
                   "Professional Postgraduate Diploma in Financial Crime Compliance "
                   "(International Compliance Association / University of Manchester). "
                   "Has personally built monitoring frameworks, written SARs, sat through "
                   "regulatory examinations, and managed compliance teams across multiple "
                   "jurisdictions.",
                   size=8.5, max_width=col_w, leading=11.5)

    # Right column: Engineering
    ry = y
    ry = sub_header(c, right_x, ry, "Engineering")
    ry = wrap_text(c, right_x, ry,
                   "Self-taught GPU systems programmer. C++23, CUDA (sm_86/89/100/120), "
                   "Vulkan. Built the entire ZQUAS engine as a solo developer: policy "
                   "language compiler, GPU adjudication kernel, MPC protocol implementation, "
                   "cryptographic attestation pipeline, adversarial testing framework, entity "
                   "resolution graph, rendering engine. This dual expertise, compliance domain "
                   "knowledge combined with GPU systems programming, shapes every architectural "
                   "decision and is extremely rare in the talent market.",
                   size=8.5, max_width=col_w, leading=11.5)

    y = min(ly, ry) - 10
    draw_line(c, y)
    y -= 18

    # Engineering Standards
    y = section_header(c, y, "Engineering Standards")

    eng_headers = ["Standard", "Detail"]
    eng_widths = [130, CW - 130]
    eng_rows = [
        ["Language", "C++23 with CUDA"],
        ["GPU targets", "sm_86, sm_89, sm_100, sm_120"],
        ["Build hardening", "/sdl, /guard:cf, /GS, /Qspectre, /CETCOMPAT, /HIGHENTROPYVA"],
        ["Testing", "~3,869 GTest units + standalone benchmark harnesses"],
        ["Cryptography", "BLAKE3, SHA-256, Ed25519, Poseidon, SipHash-128"],
        ["ECS framework", "entt-backed entity component system"],
        ["Serialisation", "Hologram v4 binary format (64B-aligned, std140)"],
        ["Build attestation", "BLAKE3 + SHA-256 + Ed25519 embedded, reproducible builds"],
    ]
    y = draw_table(c, y, eng_headers, eng_rows, eng_widths, font_size=7.5, row_h=14)

    y -= 10
    draw_line(c, y)
    y -= 18

    # Regulatory Framework Coverage
    y = section_header(c, y, "Regulatory Framework Coverage")

    frameworks = ["EU AI Act", "AMLR / 6AMLD", "FATF R15", "NIST AI RMF",
                  "ISO 42001", "MAS TRM", "GDPR", "DORA"]
    tag_x = MARGIN
    tag_h = 16
    tag_pad = 8
    tag_gap = 6
    tag_y = y - 2

    for fw in frameworks:
        tw = pdfmetrics.stringWidth(fw, "Helvetica", 7.5) + tag_pad * 2
        # Draw rounded tag
        c.setStrokeColor(ACCENT_DIM)
        c.setLineWidth(0.75)
        c.setFillColor(BG_CARD)
        c.roundRect(tag_x, tag_y - tag_h + 5, tw, tag_h, 4, fill=1, stroke=1)
        c.setFont("Helvetica", 7.5)
        c.setFillColor(TEXT_MUTED)
        c.drawString(tag_x + tag_pad, tag_y - 5, fw)
        tag_x += tw + tag_gap

    y = tag_y - tag_h - 12
    draw_line(c, y)
    y -= 22

    # Contact
    y = section_header(c, y, "Contact")

    contact_lines = [
        "danny@zquas.ai",
        "zquas.ai",
        "linkedin.com/in/danny-de-gier-prof-pgdip-fcc/",
        "Zwolle, Netherlands",
    ]
    for line in contact_lines:
        c.setFont("Helvetica", 9)
        c.setFillColor(TEXT_SECONDARY)
        c.drawCentredString(W / 2, y, line)
        y -= 14

    y -= 10

    # Closing line
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(ACCENT)
    c.drawCentredString(W / 2, y,
                        "The architecture is ready. The regulatory window is open. Let's talk.")


# ========== GENERATE ==========

def main():
    c = canvas.Canvas(OUTPUT, pagesize=A4)
    c.setTitle("ZQUAS - Sovereign Compliance Infrastructure")
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
    c.save()
    print(f"PDF generated: {OUTPUT}")


if __name__ == "__main__":
    main()

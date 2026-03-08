"""Generate ZQUAS one-pager PDF — dark theme, 2-page executive briefing."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "zquas-onepager.pdf")

# Colors
BG = HexColor("#0a0b0f")
BG_CARD = HexColor("#161722")
BG_TABLE_HEADER = HexColor("#1a1b2e")
BG_TABLE_ALT = HexColor("#10111a")
TEXT_PRIMARY = HexColor("#e2e4ed")
TEXT_SECONDARY = HexColor("#8890a6")
TEXT_MUTED = HexColor("#565c72")
ACCENT = HexColor("#4a7dff")
ACCENT_DIM = HexColor("#2a4a8f")
SUCCESS = HexColor("#34d399")
WHITE = HexColor("#ffffff")

W, H = A4  # 595.27 x 841.89 pts
MARGIN = 40
CW = W - 2 * MARGIN  # content width


def draw_bg(c):
    c.setFillColor(BG)
    c.rect(0, 0, W, H, fill=1, stroke=0)


def draw_line(c, y, color=ACCENT_DIM, width=0.5):
    c.setStrokeColor(color)
    c.setLineWidth(width)
    c.line(MARGIN, y, W - MARGIN, y)


def draw_text(c, x, y, text, size=9.5, color=TEXT_SECONDARY, font="Helvetica", max_width=None):
    c.setFont(font, size)
    c.setFillColor(color)
    if max_width:
        # Word wrap
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
            c.drawString(x, y - i * (size + 3), line)
        return y - len(lines) * (size + 3)
    else:
        c.drawString(x, y, text)
        return y - (size + 3)


def draw_wrapped_text(c, x, y, text, size=9.5, color=TEXT_SECONDARY, font="Helvetica",
                      max_width=CW, leading=None):
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


def draw_section_header(c, y, label):
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(TEXT_PRIMARY)
    c.drawString(MARGIN, y, label)
    return y - 22


def draw_bullet(c, x, y, label, text, max_width, label_size=9.5, text_size=9):
    c.setFont("Helvetica-Bold", label_size)
    c.setFillColor(TEXT_PRIMARY)
    c.drawString(x, y, label)
    y -= 13
    y = draw_wrapped_text(c, x, y, text, size=text_size, color=TEXT_SECONDARY, max_width=max_width)
    return y - 6


# ─── PAGE 1 ───

def page1(c):
    draw_bg(c)

    # Header bar
    y = H - MARGIN
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(TEXT_PRIMARY)
    c.drawString(MARGIN, y, "ZQUAS")

    c.setFont("Helvetica", 9)
    c.setFillColor(TEXT_MUTED)
    c.drawRightString(W - MARGIN, y, "Sovereign Compliance Infrastructure")

    y -= 10
    draw_line(c, y, ACCENT, 1.5)
    y -= 28

    # Hero
    c.setFont("Helvetica-Bold", 22)
    c.setFillColor(TEXT_PRIMARY)
    y = draw_wrapped_text(c, MARGIN, y, "GPU-Native Compliance Engine for Regulated Finance",
                          size=22, color=TEXT_PRIMARY, font="Helvetica-Bold", max_width=CW, leading=27)
    y -= 6

    y = draw_wrapped_text(c, MARGIN, y,
        "Cross-institutional financial crime detection without central data pooling. "
        "Every decision cryptographically attested. Every verdict independently verifiable.",
        size=10, color=TEXT_SECONDARY, max_width=CW, leading=15)
    y -= 16

    # Stats row
    stat_w = CW / 3
    stats = [
        ("2.58M", "Compliance events / sec"),
        ("29", "Policies evaluated in parallel"),
        ("8", "Regulatory standards covered"),
    ]
    for i, (val, label) in enumerate(stats):
        sx = MARGIN + i * stat_w
        c.setFont("Helvetica-Bold", 20)
        c.setFillColor(ACCENT)
        c.drawString(sx, y, val)
        c.setFont("Helvetica", 7)
        c.setFillColor(TEXT_MUTED)
        c.drawString(sx, y - 14, label.upper())

    y -= 36
    draw_line(c, y)
    y -= 22

    # The Problem
    y = draw_section_header(c, y, "The Problem")

    problems = [
        "Money laundering networks operate across banks. Individual institutions only see fragments. "
        "An estimated EUR 16 billion is laundered through the Netherlands alone each year.",

        "Joint monitoring initiatives have stalled. Centralising transaction data triggers GDPR objections. "
        "The EU AMLR (effective mid-2027) restricts data sharing to pre-identified high-risk customers.",

        "Legacy monitoring systems generate 95% false positive rates, process in overnight batches, "
        "and cost Tier-1 banks EUR 50-100M+ annually in compliance operations.",
    ]

    for text in problems:
        # Bullet marker
        c.setFillColor(ACCENT)
        c.circle(MARGIN + 4, y + 3, 2, fill=1, stroke=0)
        y = draw_wrapped_text(c, MARGIN + 14, y, text, size=9, color=TEXT_SECONDARY,
                              max_width=CW - 14, leading=12.5)
        y -= 5

    y -= 8
    draw_line(c, y)
    y -= 22

    # The Solution
    y = draw_section_header(c, y, "The Solution")

    col_w = (CW - 20) / 2
    left_x = MARGIN
    right_x = MARGIN + col_w + 20

    left_items = [
        ("GPU-Native Processing",
         "Full policy sets evaluated against every transaction simultaneously. Real-time, not batch."),
        ("Privacy-Preserving MPC",
         "Cross-institutional detection via GPU-accelerated secure multi-party computation. No central data pool."),
        ("Cryptographic Attestation",
         "Every decision produces a proof bundle. Regulators verify independently with a standalone CLI tool."),
    ]
    right_items = [
        ("Policy-as-Code",
         "Compliance policies compiled to bytecode. Same policy, same data, same verdict. Deterministic and reproducible."),
        ("Entity Resolution at GPU Speed",
         "GPU-resident identity graph with neural network risk propagation. Full network context for every decision."),
        ("Multi-Framework Coverage",
         "EU AI Act, AMLR, FATF R15, NIST AI RMF, ISO 42001, MAS TRM, GDPR, DORA."),
    ]

    ly = y
    ry = y
    for item in left_items:
        ly = draw_bullet(c, left_x, ly, item[0], item[1], col_w)
    for item in right_items:
        ry = draw_bullet(c, right_x, ry, item[0], item[1], col_w)


# ─── PAGE 2 ───

def page2(c):
    draw_bg(c)

    # Header bar (repeat)
    y = H - MARGIN
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(TEXT_PRIMARY)
    c.drawString(MARGIN, y, "ZQUAS")
    c.setFont("Helvetica", 9)
    c.setFillColor(TEXT_MUTED)
    c.drawRightString(W - MARGIN, y, "Sovereign Compliance Infrastructure")
    y -= 10
    draw_line(c, y, ACCENT, 1.5)
    y -= 24

    # Competitive Positioning
    y = draw_section_header(c, y, "Competitive Positioning")

    headers = ["", "Legacy Incumbents", "AI-Native Challengers", "ZQUAS"]
    rows = [
        ["Examples", "NICE Actimize, Oracle, SAS", "Sardine ($145M), Hawk AI ($56M)", "—"],
        ["Architecture", "CPU batch, rules-based", "CPU cloud, ML-based", "GPU-native, MPC + ZK"],
        ["Cross-bank detection", "No", "No", "Yes (privacy-preserving)"],
        ["Cryptographic proof", "No", "No", "Yes"],
        ["Real-time at scale", "Limited", "Partial", "2.58M events/sec"],
        ["Regulator verification", "Trust-based", "Trust-based", "Independent CLI tool"],
    ]

    col_widths = [110, 135, 135, 135]
    row_h = 16
    header_h = 18
    font_size = 7.5

    # Table header
    tx = MARGIN
    c.setFillColor(BG_TABLE_HEADER)
    c.rect(MARGIN, y - header_h + 4, CW, header_h, fill=1, stroke=0)
    for i, h in enumerate(headers):
        c.setFont("Helvetica-Bold", 7)
        c.setFillColor(ACCENT)
        c.drawString(tx + 6, y - 8, h.upper())
        tx += col_widths[i]
    y -= header_h + 2

    # Table rows
    for ri, row in enumerate(rows):
        if ri % 2 == 0:
            c.setFillColor(BG_TABLE_ALT)
            c.rect(MARGIN, y - row_h + 4, CW, row_h, fill=1, stroke=0)
        tx = MARGIN
        for ci, cell in enumerate(row):
            if ci == 0:
                c.setFont("Helvetica-Bold", font_size)
                c.setFillColor(TEXT_SECONDARY)
            elif ci == 3:
                c.setFont("Helvetica-Bold", font_size)
                c.setFillColor(ACCENT)
            else:
                c.setFont("Helvetica", font_size)
                c.setFillColor(TEXT_MUTED)
            c.drawString(tx + 6, y - 8, cell)
            tx += col_widths[i]
        y -= row_h

    y -= 14
    draw_line(c, y)
    y -= 22

    # Market & Timing
    y = draw_section_header(c, y, "Market & Timing")

    market_points = [
        "EUR 200B+ annual global compliance spending. Growing 15-20% per year.",
        "AMLR mid-2027 creates a hard regulatory deadline. Every European bank must re-architect.",
        "EU AI Act classifies AML systems as high-risk with mandatory technical standards from August 2026.",
    ]
    for text in market_points:
        c.setFillColor(ACCENT)
        c.circle(MARGIN + 4, y + 3, 2, fill=1, stroke=0)
        y = draw_wrapped_text(c, MARGIN + 14, y, text, size=9, color=TEXT_SECONDARY,
                              max_width=CW - 14, leading=12.5)
        y -= 5

    y -= 8
    draw_line(c, y)
    y -= 22

    # Traction
    y = draw_section_header(c, y, "Traction")
    traction = [
        "DNB InnovationHub submission under review",
        "FCA regulatory sandbox programme engaged",
        "2.58M CEPS benchmarked on RTX 5090 with 29-policy Tier-1 bank policy set",
        "~3,869 unit tests across engine subsystems",
    ]
    for text in traction:
        c.setFillColor(ACCENT)
        c.circle(MARGIN + 4, y + 3, 2, fill=1, stroke=0)
        c.setFont("Helvetica", 9)
        c.setFillColor(TEXT_SECONDARY)
        c.drawString(MARGIN + 14, y, text)
        y -= 15

    y -= 10
    draw_line(c, y)
    y -= 22

    # Founder
    y = draw_section_header(c, y, "Founder")
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(TEXT_PRIMARY)
    c.drawString(MARGIN, y, "Danny de Gier")
    y -= 16

    founder_points = [
        "18+ years financial crime compliance: RBS, Deutsche Bank, HSBC, Commerzbank, ClearBank, Vivid Money, CoinMetro",
        "GPU systems programming: C++23, CUDA, Vulkan",
        "Prof. Postgraduate Diploma in Financial Crime Compliance (ICA / University of Manchester)",
        "Based in Zwolle, Netherlands",
    ]
    for text in founder_points:
        c.setFillColor(ACCENT_DIM)
        c.circle(MARGIN + 4, y + 3, 2, fill=1, stroke=0)
        y = draw_wrapped_text(c, MARGIN + 14, y, text, size=8.5, color=TEXT_SECONDARY,
                              max_width=CW - 14, leading=12)
        y -= 4

    y -= 10
    draw_line(c, y)
    y -= 22

    # Business Model
    y = draw_section_header(c, y, "Business Model")

    phases = [
        ("Land:", "Single-bank on-premise deployment. Annual licensing by transaction volume."),
        ("Expand:", "Additional business lines, policy domains, and jurisdictions within existing banks."),
        ("Network:", "Cross-institutional MPC detection activates as network grows. Network effects compound."),
    ]
    for label, text in phases:
        c.setFont("Helvetica-Bold", 9.5)
        c.setFillColor(ACCENT)
        lw = pdfmetrics.stringWidth(label, "Helvetica-Bold", 9.5)
        c.drawString(MARGIN, y, label)
        c.setFont("Helvetica", 9)
        c.setFillColor(TEXT_SECONDARY)
        c.drawString(MARGIN + lw + 5, y, text)
        y -= 16

    # Footer
    y = MARGIN + 20
    draw_line(c, y, ACCENT, 1)
    y -= 16
    c.setFont("Helvetica", 8)
    c.setFillColor(TEXT_MUTED)
    c.drawString(MARGIN, y, "danny@zquas.ai")
    c.drawCentredString(W / 2, y, "zquas.ai")
    c.drawRightString(W - MARGIN, y, "linkedin.com/in/danny-de-gier-prof-pgdip-fcc")


# ─── GENERATE ───

def main():
    c = canvas.Canvas(OUTPUT, pagesize=A4)
    c.setTitle("ZQUAS — Sovereign Compliance Infrastructure")
    c.setAuthor("Danny de Gier")
    c.setSubject("GPU-Native Compliance Engine for Regulated Finance")

    page1(c)
    c.showPage()
    page2(c)
    c.showPage()
    c.save()
    print(f"PDF generated: {OUTPUT}")


if __name__ == "__main__":
    main()

"""Generate favicon.png, favicon-32.png, and og-image.png for ZQUAS."""

from PIL import Image, ImageDraw, ImageFont
import math
import os

DIR = os.path.dirname(os.path.abspath(__file__))

# Colors
BG = (10, 11, 15)
BG_CARD = (22, 23, 34)
ACCENT = (74, 125, 255)
ACCENT_DIM = (42, 74, 143)
TEXT_PRIMARY = (226, 228, 237)
TEXT_SECONDARY = (136, 144, 166)
TEXT_MUTED = (86, 92, 114)
BORDER = (30, 32, 48)

FONT_BOLD = "C:/Windows/Fonts/DejaVuSans-Bold.ttf"
FONT_REG = "C:/Windows/Fonts/DejaVuSans.ttf"


def generate_favicon(size, output_name):
    img = Image.new("RGBA", (size, size), BG + (255,))
    draw = ImageDraw.Draw(img)

    # "Z" character, roughly 70% of canvas height
    font_size = int(size * 0.68)
    font = ImageFont.truetype(FONT_BOLD, font_size)

    bbox = draw.textbbox((0, 0), "Z", font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    x = (size - tw) / 2 - bbox[0]
    y = (size - th) / 2 - bbox[1]

    draw.text((x, y), "Z", fill=ACCENT, font=font)

    path = os.path.join(DIR, output_name)
    img.save(path, "PNG")
    return path


def generate_og_image():
    W, H = 1200, 630
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    # Subtle radial gradient glow from center-top
    # Apply as additive blend on a separate layer
    glow = Image.new("RGB", (W, H), (0, 0, 0))
    glow_draw = ImageDraw.Draw(glow)
    cx, cy = W // 2, 80
    max_r = 500
    for r in range(max_r, 0, -2):
        alpha = 0.06 * (1 - (r / max_r) ** 2)
        c = (int(74 * alpha), int(125 * alpha), int(255 * alpha))
        glow_draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=c)

    # Composite glow onto background additively
    from PIL import ImageChops
    img = ImageChops.add(img, glow)
    draw = ImageDraw.Draw(img)

    # "ZQUAS" title
    title_font = ImageFont.truetype(FONT_BOLD, 72)
    dot_font = ImageFont.truetype(FONT_BOLD, 72)

    title_text = "ZQUAS"
    title_bbox = draw.textbbox((0, 0), title_text, font=title_font)
    title_w = title_bbox[2] - title_bbox[0]
    dot_bbox = draw.textbbox((0, 0), ".", font=dot_font)
    dot_w = dot_bbox[2] - dot_bbox[0]
    total_w = title_w + dot_w

    title_x = (W - total_w) / 2
    title_y = 175

    draw.text((title_x, title_y), title_text, fill=TEXT_PRIMARY, font=title_font)
    draw.text((title_x + title_w, title_y), ".", fill=ACCENT, font=dot_font)

    # Subtitle
    sub_font = ImageFont.truetype(FONT_REG, 24)
    sub_text = "Sovereign Compliance Infrastructure"
    sub_bbox = draw.textbbox((0, 0), sub_text, font=sub_font)
    sub_w = sub_bbox[2] - sub_bbox[0]
    sub_x = (W - sub_w) / 2
    sub_y = title_y + 95

    draw.text((sub_x, sub_y), sub_text, fill=TEXT_SECONDARY, font=sub_font)

    # Horizontal line (60% width, centered)
    line_w = int(W * 0.6)
    line_x = (W - line_w) // 2
    line_y = sub_y + 55
    draw.line([(line_x, line_y), (line_x + line_w, line_y)], fill=BORDER, width=1)

    # Tagline below line
    tag_font = ImageFont.truetype(FONT_REG, 16)
    tag_text = "GPU-Native  \u00b7  Privacy-Preserving  \u00b7  Cryptographically Verifiable"
    tag_bbox = draw.textbbox((0, 0), tag_text, font=tag_font)
    tag_w = tag_bbox[2] - tag_bbox[0]
    tag_x = (W - tag_w) / 2
    tag_y = line_y + 25

    draw.text((tag_x, tag_y), tag_text, fill=TEXT_MUTED, font=tag_font)

    # Bottom left: zquas.ai
    url_font = ImageFont.truetype(FONT_REG, 14)
    draw.text((40, H - 45), "zquas.ai", fill=TEXT_MUTED, font=url_font)

    path = os.path.join(DIR, "og-image.png")
    img.save(path, "PNG")
    return path


def main():
    f64 = generate_favicon(64, "favicon.png")
    f32 = generate_favicon(32, "favicon-32.png")
    og = generate_og_image()

    # Verify
    for path, expected in [(f64, (64, 64)), (f32, (32, 32)), (og, (1200, 630))]:
        img = Image.open(path)
        size_kb = os.path.getsize(path) / 1024
        name = os.path.basename(path)
        assert img.size == expected, f"{name}: expected {expected}, got {img.size}"
        print(f"  {name}: {img.size[0]}x{img.size[1]}, {size_kb:.1f} KB")

    print("All images generated and verified.")


if __name__ == "__main__":
    main()

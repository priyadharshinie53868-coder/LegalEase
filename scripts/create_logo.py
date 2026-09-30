import os
from PIL import Image, ImageDraw, ImageFont

def create_high_res_logo():
    os.makedirs("assets", exist_ok=True)
    # High resolution 800x200 canvas
    width, height = 800, 200
    image = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)

    # Balance scale badge (Left side)
    badge_x, badge_y, badge_size = 40, 25, 150
    draw.rounded_rectangle(
        [badge_x, badge_y, badge_x + badge_size, badge_y + badge_size],
        radius=28,
        fill=(30, 58, 138, 255)  # Navy Blue #1e3a8a
    )

    # Scale icon geometry
    cx = badge_x + badge_size // 2
    cy = badge_y + badge_size // 2
    # Center pillar
    draw.line([cx, cy - 40, cx, cy + 42], fill=(255, 255, 255, 255), width=6)
    # Base pedestal
    draw.line([cx - 30, cy + 42, cx + 30, cy + 42], fill=(255, 255, 255, 255), width=6)
    # Fulcrum point
    draw.ellipse([cx - 8, cy - 40, cx + 8, cy - 24], fill=(255, 255, 255, 255))
    # Crossbeam
    draw.line([cx - 45, cy - 26, cx + 45, cy - 26], fill=(255, 255, 255, 255), width=6)
    # Left pan
    draw.line([cx - 38, cy - 26, cx - 38, cy - 2], fill=(255, 255, 255, 255), width=4)
    draw.polygon([(cx - 50, cy - 2), (cx - 26, cy - 2), (cx - 38, cy + 12)], fill=(255, 255, 255, 255))
    # Right pan
    draw.line([cx + 38, cy - 26, cx + 38, cy - 2], fill=(255, 255, 255, 255), width=4)
    draw.polygon([(cx + 26, cy - 2), (cx + 50, cy - 2), (cx + 38, cy + 12)], fill=(255, 255, 255, 255))

    # Text rendering
    text_x = 220
    text_y = 45

    # Try loading a clean system font or fallback
    try:
        font_main = ImageFont.truetype("arial.ttf", 68)
        font_sub = ImageFont.truetype("arial.ttf", 24)
    except Exception:
        font_main = ImageFont.load_default()
        font_sub = ImageFont.load_default()

    draw.text((text_x, text_y), "LegalEase", fill=(15, 23, 42, 255), font=font_main)
    draw.text((text_x + 4, text_y + 75), "AI LEGAL DOCUMENT GENERATOR", fill=(100, 116, 139, 255), font=font_sub)

    image.save("assets/logo.png", "PNG")
    print("High-res logo created at assets/logo.png")

if __name__ == "__main__":
    create_high_res_logo()

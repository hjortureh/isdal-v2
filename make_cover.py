#!/usr/bin/env python3
"""Generate the social share cover image (assets/img/og-cover.png, 1200x630).

Needs Pillow. Downloads the Archivo font into .fonts-cache/ on first run.
Run:  python3 make_cover.py
"""

import os
import urllib.request

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(ROOT, ".fonts-cache")
OUT = os.path.join(ROOT, "assets", "img", "og-cover.png")

# Google Fonts serves static TTFs to clients without a modern UA string.
FONT_CSS = "https://fonts.googleapis.com/css2?family=Archivo:wght@600;800"

PAPER = (241, 239, 234)
INK = (19, 19, 17)
LINE = (19, 19, 17, 30)

W, H = 1200, 630


def get_fonts():
    os.makedirs(FONT_DIR, exist_ok=True)
    paths = {}
    req = urllib.request.Request(FONT_CSS, headers={"User-Agent": "curl/8"})
    css = urllib.request.urlopen(req).read().decode()
    import re

    urls = re.findall(r"url\((https://[^)]+\.ttf)\)", css)
    weights = re.findall(r"font-weight:\s*(\d+)", css)
    for weight, url in zip(weights, urls):
        p = os.path.join(FONT_DIR, f"archivo-{weight}.ttf")
        if not os.path.exists(p):
            urllib.request.urlretrieve(url, p)
        paths[weight] = p
    return paths


def main():
    fonts = get_fonts()
    f_word = ImageFont.truetype(fonts["800"], 148)
    f_tag = ImageFont.truetype(fonts["600"], 26)
    f_foot = ImageFont.truetype(fonts["600"], 20)

    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img, "RGBA")

    # right panel: Geysir night render
    panel_x = 760
    photo = Image.open(os.path.join(ROOT, "assets", "img", "geysir-1.webp")).convert("RGB")
    pw, ph = W - panel_x, H
    scale = max(pw / photo.width, ph / photo.height)
    photo = photo.resize((round(photo.width * scale), round(photo.height * scale)))
    left = (photo.width - pw) // 2
    top = (photo.height - ph) // 2
    img.paste(photo.crop((left, top, left + pw, top + ph)), (panel_x, 0))

    # faint vertical hairlines over the paper area
    for x in (250, 500):
        draw.line([(x, 0), (x, H)], fill=LINE, width=1)
    draw.line([(panel_x, 0), (panel_x, H)], fill=INK, width=2)

    m = 80  # left margin

    # wedge mark + wordmark, bottom-aligned like the site logo
    word_y = 208
    asc, desc = f_word.getmetrics()
    cap_bottom = word_y + asc  # baseline of the wordmark
    ws = 96  # wedge size
    wx, wy = m, cap_bottom - ws + 6
    draw.polygon(
        [(wx, wy + ws * 9 / 24), (wx + ws, wy), (wx + ws, wy + ws), (wx, wy + ws)],
        fill=INK,
    )
    word_x = wx + ws + 36
    draw.text((word_x, word_y), "ÍSDAL", font=f_word, fill=INK)

    # tag below the wordmark
    draw.text((word_x + 6, cap_bottom + 34), "A R C H I T E C T U R E   &   I N T E R I O R", font=f_tag, fill=INK)

    # footer line
    fy = H - 96
    draw.line([(m, fy), (panel_x - 60, fy)], fill=(19, 19, 17, 102), width=2)
    draw.text((m, fy + 22), "ARKITEKTÚR & INNANHÚSSHÖNNUN — REYKJAVÍK", font=f_foot, fill=INK)

    img.save(OUT, "PNG")
    print("wrote", os.path.relpath(OUT, ROOT), f"({os.path.getsize(OUT) // 1024} KB)")


if __name__ == "__main__":
    main()

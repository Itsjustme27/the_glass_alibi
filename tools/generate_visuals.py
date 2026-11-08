#!/usr/bin/env python3
"""Generate original placeholder visuals for The Glass Alibi.

Everything produced here is temporary, procedurally generated art (no external
assets). Final artwork can replace files in game/images/ and game/gui/ without
any story-code changes. Run from anywhere: paths are resolved relative to this
file's project root.
"""

import math
import os
import random

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GAME = os.path.join(ROOT, "game")
W, H = 1920, 1080
FONT_BOLD = "/home/swapnil69/Downloads/renpy-8.5.3-sdk/renpy/common/DejaVuSans-Bold.ttf"

random.seed(42)


def out(path):
    full = os.path.join(GAME, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    return full


def gradient(w, h, top, bottom):
    im = Image.new("RGB", (w, h))
    d = ImageDraw.Draw(im)
    for y in range(h):
        t = y / max(1, h - 1)
        c = tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3))
        d.line([(0, y), (w, y)], fill=c)
    return im


def add_glow(im, cx, cy, radius, color, strength=1.0):
    glow = Image.new("RGB", im.size, (0, 0, 0))
    d = ImageDraw.Draw(glow)
    steps = 24
    for i in range(steps, 0, -1):
        r = radius * i / steps
        f = (1 - i / steps) ** 2 * strength
        c = tuple(int(v * f) for v in color)
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=c)
    glow = glow.filter(ImageFilter.GaussianBlur(radius / 5))
    return _screen(im, glow)


def _screen(base, layer):
    from PIL import ImageChops
    return ImageChops.screen(base, layer)


def rain(im, count=420, alpha=46):
    overlay = Image.new("RGBA", im.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    for _ in range(count):
        x = random.randint(-40, W)
        y = random.randint(-60, H)
        ln = random.randint(18, 46)
        d.line([(x, y), (x - 6, y + ln)], fill=(170, 200, 225, alpha), width=1)
    return Image.alpha_composite(im.convert("RGBA"), overlay).convert("RGB")


def grain(im, amount=7):
    noise = Image.new("L", im.size)
    noise.putdata([random.randint(0, amount) for _ in range(W * H)])
    noise_rgb = Image.merge("RGB", (noise, noise, noise))
    return _screen(im, noise_rgb)


def vignette(im, strength=0.55):
    mask = Image.new("L", im.size, 0)
    d = ImageDraw.Draw(mask)
    d.ellipse([-W * 0.25, -H * 0.35, W * 1.25, H * 1.35], fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(220))
    black = Image.new("RGB", im.size, (0, 0, 0))
    return Image.composite(im, black, mask.point(lambda v: int(255 - (255 - v) * strength)))


def neon_text(im, text, pos, size, color, vertical=False):
    font = ImageFont.truetype(FONT_BOLD, size)
    glow = Image.new("RGB", im.size, (0, 0, 0))
    d = ImageDraw.Draw(glow)
    d.text(pos, text, font=font, fill=color)
    glow = glow.filter(ImageFilter.GaussianBlur(14))
    im = _screen(im, glow)
    d = ImageDraw.Draw(im)
    d.text(pos, text, font=font, fill=tuple(min(255, c + 70) for c in color))
    return im


def windows(d, x0, y0, x1, y1, cols, rows, p=0.18):
    cw = (x1 - x0) / cols
    ch = (y1 - y0) / rows
    for i in range(cols):
        for j in range(rows):
            if random.random() < p:
                c = random.choice([(64, 170, 160), (200, 150, 70), (90, 110, 160)])
                c = tuple(int(v * 0.55) for v in c)
                d.rectangle(
                    [x0 + i * cw + cw * 0.25, y0 + j * ch + ch * 0.25,
                     x0 + i * cw + cw * 0.72, y0 + j * ch + ch * 0.7],
                    fill=c,
                )


# ----------------------------------------------------------------------------
# Backgrounds
# ----------------------------------------------------------------------------

def bg_alley(darker=False):
    im = gradient(W, H, (4, 6, 12), (10, 16, 26))
    d = ImageDraw.Draw(im)

    # buildings left and right
    d.polygon([(0, 60), (560, 140), (560, 1080), (0, 1080)], fill=(6, 9, 15))
    d.polygon([(1360, 100), (1920, 40), (1920, 1080), (1360, 1080)], fill=(7, 10, 17))
    d.polygon([(560, 250), (820, 330), (820, 1080), (560, 1080)], fill=(5, 7, 12))
    d.polygon([(1100, 300), (1360, 220), (1360, 1080), (1100, 1080)], fill=(5, 8, 13))
    windows(d, 40, 120, 520, 700, 8, 10)
    windows(d, 1400, 100, 1880, 680, 8, 10)
    windows(d, 590, 320, 790, 760, 3, 8, 0.12)

    # wet street
    d.polygon([(560, 760), (1360, 760), (1920, 1080), (0, 1080)], fill=(8, 12, 18))
    # neon reflections
    for cx, col in [(430, (255, 45, 120)), (1490, (45, 225, 194)), (760, (255, 160, 60))]:
        for i in range(26):
            y = 790 + i * 11
            ww = 30 + i * 3
            a = max(0, 90 - i * 3)
            d.rectangle([cx - ww, y, cx + ww, y + 5], fill=tuple(int(v * a / 255) for v in col))

    # distant end of alley
    d.rectangle([820, 400, 1100, 760], fill=(3, 5, 9))
    im = add_glow(im, 960, 620, 240, (30, 70, 90), 0.5)

    im = neon_text(im, "KOTHA 420", (150, 300), 64, (255, 45, 120))
    im = neon_text(im, "MOMO", (1440, 340), 58, (45, 225, 194))
    im = neon_text(im, "BAR", (640, 430), 40, (255, 160, 60))

    # police strobes bleeding in
    im = add_glow(im, 60, 900, 320, (160, 30, 40), 0.35)
    im = add_glow(im, 1880, 940, 300, (30, 60, 160), 0.3)

    im = rain(im)
    if darker:
        im = Image.blend(im, Image.new("RGB", im.size, (2, 3, 6)), 0.45)
    im = vignette(im, 0.6)
    return grain(im)


def bg_gallery():
    im = gradient(W, H, (16, 11, 9), (24, 16, 12))
    d = ImageDraw.Draw(im)
    # floor
    d.polygon([(0, 780), (1920, 780), (1920, 1080), (0, 1080)], fill=(14, 10, 8))
    for x in range(0, W, 160):
        d.line([(x, 780), (x - 120, 1080)], fill=(20, 14, 10), width=2)

    # UV lamp cones
    for lx in (480, 1080, 1620):
        d.rectangle([lx - 60, 60, lx + 60, 84], fill=(20, 20, 28))
        im = add_glow(im, lx, 120, 260, (90, 60, 200), 0.5)
        d = ImageDraw.Draw(im)
        d.polygon([(lx - 40, 90), (lx + 40, 90), (lx + 240, 770), (lx - 240, 770)], fill=(26, 20, 40))

    # restoration tables
    for tx in (300, 900, 1450):
        d.rectangle([tx, 700, tx + 420, 760], fill=(30, 22, 16))
        d.rectangle([tx + 20, 760, tx + 50, 950], fill=(20, 15, 11))
        d.rectangle([tx + 350, 760, tx + 380, 950], fill=(20, 15, 11))

    # paubha paintings on tables/walls: gold frame, mandala
    def paubha(x, y, w, h):
        d.rectangle([x, y, x + w, y + h], fill=(60, 42, 18))
        d.rectangle([x + 10, y + 10, x + w - 10, y + h - 10], fill=(24, 30, 60))
        cx, cy = x + w // 2, y + h // 2
        rr = min(w, h) // 3
        d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], outline=(180, 140, 60), width=4)
        d.ellipse([cx - rr // 2, cy - rr // 2, cx + rr // 2, cy + rr // 2], outline=(160, 60, 50), width=3)

    paubha(340, 480, 300, 210)
    paubha(960, 470, 280, 220)
    paubha(120, 220, 240, 320)
    # the great Bhairav paubha over the false wall
    paubha(1380, 200, 330, 440)
    d.ellipse([1470, 300, 1620, 430], fill=(12, 12, 18))
    d.ellipse([1500, 340, 1528, 362], fill=(200, 60, 40))
    d.ellipse([1560, 340, 1588, 362], fill=(200, 60, 40))

    # Bhairav masks on the wall
    for mx in (700, 820):
        d.ellipse([mx, 250, mx + 90, 350], fill=(40, 26, 16))
        d.ellipse([mx + 18, 280, mx + 36, 296], fill=(8, 6, 6))
        d.ellipse([mx + 54, 280, mx + 72, 296], fill=(8, 6, 6))

    # velvet curtain, left edge
    for i in range(8):
        x = i * 26
        d.rectangle([x, 0, x + 18, 820], fill=(46 + (i % 2) * 12, 12, 18))

    im = vignette(im, 0.55)
    return grain(im)


def bg_vault():
    im = gradient(W, H, (8, 10, 12), (12, 14, 16))
    d = ImageDraw.Draw(im)
    d.polygon([(0, 820), (1920, 820), (1920, 1080), (0, 1080)], fill=(9, 11, 13))

    # single hanging bulb
    d.line([(960, 0), (960, 180)], fill=(30, 30, 30), width=3)
    d.ellipse([944, 180, 976, 214], fill=(220, 220, 180))
    im = add_glow(im, 960, 240, 460, (120, 130, 90), 0.5)
    d = ImageDraw.Draw(im)

    # corkboard with seven vials
    d.rectangle([180, 240, 760, 640], fill=(58, 42, 28))
    d.rectangle([196, 256, 744, 624], fill=(74, 54, 36))
    for i in range(7):
        vx = 240 + i * 72
        d.rectangle([vx, 320, vx + 34, 430], fill=(150, 190, 200))
        d.rectangle([vx + 6, 350, vx + 28, 424], fill=(90, 110, 120))
        d.rectangle([vx + 10, 366, vx + 24, 404], fill=(120, 70, 66))
        d.rectangle([vx - 2, 310, vx + 36, 324], fill=(40, 40, 44))
    # red silk connections
    for i in range(6):
        vx = 257 + i * 72
        d.line([(vx, 440), (vx + 72, 452)], fill=(150, 30, 40), width=2)
    d.text((220, 560), "VII", fill=(160, 40, 46), font=ImageFont.truetype(FONT_BOLD, 44))

    # center table with drive case and folder
    d.rectangle([860, 640, 1240, 700], fill=(26, 28, 30))
    d.rectangle([880, 700, 910, 930], fill=(18, 20, 22))
    d.rectangle([1190, 700, 1220, 930], fill=(18, 20, 22))
    d.rectangle([920, 592, 1060, 640], fill=(36, 26, 20))   # leather case
    d.rectangle([1080, 600, 1190, 640], fill=(140, 120, 80)) # folder
    d.rectangle([1080, 600, 1190, 612], fill=(120, 100, 64))

    # butcher apron hanging
    d.polygon([(1480, 300), (1600, 300), (1630, 660), (1450, 660)], fill=(46, 42, 40))
    d.polygon([(1500, 420), (1560, 430), (1570, 560), (1490, 550)], fill=(70, 22, 24))
    d.line([(1480, 300), (1540, 240)], fill=(40, 38, 36), width=4)
    d.line([(1600, 300), (1540, 240)], fill=(40, 38, 36), width=4)

    im = vignette(im, 0.65)
    return grain(im)


def bg_clinic():
    im = gradient(W, H, (6, 12, 14), (10, 20, 24))
    d = ImageDraw.Draw(im)

    # tiled walls
    for x in range(0, W, 120):
        d.line([(x, 0), (x, 760)], fill=(14, 28, 32), width=2)
    for y in range(0, 760, 90):
        d.line([(0, y), (W, y)], fill=(14, 28, 32), width=2)
    # floor
    d.polygon([(0, 760), (1920, 760), (1920, 1080), (0, 1080)], fill=(8, 16, 18))
    for x in range(0, W, 160):
        d.line([(x, 760), (x - 140, 1080)], fill=(12, 24, 26), width=2)

    # copper pipes
    for py in (60, 110):
        d.rectangle([0, py, W, py + 16], fill=(64, 40, 26))
        for x in range(100, W, 340):
            d.rectangle([x, py - 4, x + 26, py + 20], fill=(80, 52, 32))

    # cryo-pod center
    d.rectangle([860, 220, 1060, 860], fill=(16, 34, 44))
    d.rectangle([876, 236, 1044, 844], fill=(24, 60, 80))
    d.rectangle([876, 236, 1044, 844], outline=(90, 180, 200), width=3)
    d.ellipse([860, 190, 1060, 250], fill=(20, 40, 50))
    d.rectangle([840, 860, 1080, 920], fill=(14, 24, 28))
    im = add_glow(im, 960, 540, 420, (30, 110, 140), 0.5)
    d = ImageDraw.Draw(im)

    # autopsy tables
    for tx in (260, 1420):
        d.rectangle([tx, 660, tx + 340, 710], fill=(40, 52, 56))
        d.rectangle([tx + 30, 710, tx + 60, 920], fill=(24, 32, 36))
        d.rectangle([tx + 280, 710, tx + 310, 920], fill=(24, 32, 36))
        d.rectangle([tx + 20, 630, tx + 320, 662], fill=(52, 64, 68))

    # surgical lamp
    d.line([(480, 0), (480, 200)], fill=(30, 40, 44), width=6)
    d.ellipse([400, 200, 560, 250], fill=(60, 76, 80))
    im = add_glow(im, 480, 280, 300, (120, 160, 170), 0.35)

    im = vignette(im, 0.6)
    return grain(im)


def bg_cryo():
    im = gradient(W, H, (4, 10, 18), (8, 24, 44))
    d = ImageDraw.Draw(im)

    # big pod close-up
    d.rounded_rectangle([560, 60, 1360, 1080], radius=90, fill=(14, 40, 62))
    d.rounded_rectangle([596, 96, 1324, 1080], radius=72, fill=(20, 62, 96))
    # fluid gradient inside
    fluid = gradient(728, 984, (26, 80, 120), (10, 34, 60))
    im.paste(fluid, (596, 96))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([596, 96, 1324, 1080], radius=72, outline=(120, 210, 235), width=4)

    # the preserved body: vague silhouette
    d.ellipse([865, 240, 1055, 440], fill=(8, 18, 30))          # head
    d.polygon([(820, 440), (1100, 440), (1140, 900), (780, 900)], fill=(8, 18, 30))
    d.polygon([(820, 460), (700, 760), (740, 790), (850, 520)], fill=(8, 18, 30))  # arm
    # overcoat hint
    d.polygon([(820, 440), (1100, 440), (1120, 620), (800, 620)], fill=(6, 12, 22))
    # gold wedding band glint on the hand
    d.ellipse([712, 756, 736, 780], fill=(230, 190, 90))
    im = add_glow(im, 724, 768, 60, (230, 190, 90), 0.6)
    d = ImageDraw.Draw(im)

    # frost and condensation
    for _ in range(90):
        x = random.randint(610, 1300)
        y = random.randint(110, 1040)
        r = random.randint(2, 7)
        d.ellipse([x, y, x + r, y + r], fill=(190, 230, 245, 30))
    for _ in range(24):
        x = random.randint(620, 1290)
        y = random.randint(120, 900)
        d.line([(x, y), (x + random.randint(-8, 8), y + random.randint(30, 90))], fill=(150, 200, 220), width=1)

    # glass highlight
    d.polygon([(640, 120), (700, 120), (660, 1040), (620, 1040)], fill=(60, 120, 150))

    im = add_glow(im, 960, 540, 700, (20, 90, 140), 0.4)
    im = vignette(im, 0.55)
    return grain(im)


# ----------------------------------------------------------------------------
# Character silhouette sprites
# ----------------------------------------------------------------------------

SPRITE_W, SPRITE_H = 720, 1080
FILL = (10, 13, 19)


def figure_parts(kneeling=False, coat=True, broad=False):
    """Return (shape, args) lists for a parametric noir figure."""
    parts = []
    sw = 150 if not broad else 195  # half shoulder width
    if kneeling:
        head = (310, 330, 410, 445)
        parts.append(("ellipse", head))
        parts.append(("poly", [(330, 445), (390, 445), (395, 480), (325, 480)]))  # neck
        parts.append(("poly", [(360 - sw, 480), (360 + sw, 480), (400, 780), (320, 780)]))
        # folded legs
        parts.append(("poly", [(320, 760), (520, 780), (540, 850), (330, 840)]))
        parts.append(("poly", [(330, 820), (250, 900), (300, 950), (420, 860)]))
        parts.append(("poly", [(250, 900), (560, 930), (560, 985), (240, 960)]))
        # arms
        parts.append(("poly", [(360 - sw, 500), (360 - sw - 40, 520), (330, 740), (370, 750)]))
        parts.append(("poly", [(360 + sw, 500), (360 + sw + 40, 520), (430, 740), (390, 750)]))
    else:
        parts.append(("ellipse", (305, 120, 415, 245)))  # head
        parts.append(("poly", [(330, 240), (390, 240), (395, 285), (325, 285)]))  # neck
        hem = 800 if coat else 640
        parts.append(("poly", [(360 - sw, 285), (360 + sw, 285), (360 + sw + 55, hem), (360 - sw - 55, hem)]))
        # legs
        parts.append(("poly", [(300, 780 if coat else 640), (350, 780 if coat else 640), (340, 1035), (290, 1035)]))
        parts.append(("poly", [(370, 780 if coat else 640), (420, 780 if coat else 640), (430, 1035), (380, 1035)]))
        # arms
        parts.append(("poly", [(360 - sw, 300), (360 - sw - 45, 320), (360 - sw - 30, 640), (360 - sw + 10, 645)]))
        parts.append(("poly", [(360 + sw, 300), (360 + sw + 45, 320), (360 + sw + 30, 640), (360 + sw - 10, 645)]))
    return parts


def draw_parts(d, parts, color, dx=0, dy=0):
    for kind, a in parts:
        if kind == "ellipse":
            x0, y0, x1, y1 = a
            d.ellipse([x0 + dx, y0 + dy, x1 + dx, y1 + dy], fill=color)
        else:
            d.polygon([(x + dx, y + dy) for x, y in a], fill=color)


def sprite(name, rim, kneeling=False, coat=True, broad=False, props=(), eyes=False):
    im = Image.new("RGBA", (SPRITE_W, SPRITE_H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.ellipse([150, 1020, 570, 1068], fill=(0, 0, 0, 110))
    parts = figure_parts(kneeling, coat, broad)
    draw_parts(d, parts, rim + (255,), dx=-7)
    draw_parts(d, parts, FILL + (255,))

    hy = 330 if kneeling else 120  # head top
    for prop in props:
        if prop == "topi":
            d.polygon([(295, hy + 18), (425, hy + 6), (440, hy + 44), (300, hy + 52)], fill=(24, 28, 38))
            d.polygon([(295, hy + 18), (425, hy + 6), (428, hy + 22), (298, hy + 32)], fill=rim + (255,))
            for i in range(5):
                d.ellipse([310 + i * 24, hy + 34, 316 + i * 24, hy + 40], fill=(180, 160, 90, 255))
        elif prop == "fedora":
            d.ellipse([270, hy + 26, 450, hy + 58], fill=(16, 18, 24))
            d.polygon([(310, hy + 34), (330, hy - 16), (400, hy - 16), (415, hy + 34)], fill=(16, 18, 24))
            d.rectangle([312, hy + 14, 413, hy + 26], fill=rim + (255,))
        elif prop == "umbrella":
            d.line([(545, 300), (545, 1000)], fill=(30, 34, 42), width=8)
            d.polygon([(533, 300), (557, 300), (545, 240)], fill=(30, 34, 42))
            d.line([(545, 1000), (570, 1020)], fill=(30, 34, 42), width=8)
            d.ellipse([536, 610, 554, 628], fill=(220, 190, 90))  # thumb ring glint
        elif prop == "glasses":
            d.ellipse([322, hy + 66, 352, hy + 92], outline=(140, 230, 220), width=3)
            d.ellipse([368, hy + 66, 398, hy + 92], outline=(140, 230, 220), width=3)
            d.line([(352, hy + 78), (368, hy + 78)], fill=(140, 230, 220), width=3)
        elif prop == "tie":
            d.polygon([(352, 300), (368, 300), (374, 470), (360, 500), (346, 470)], fill=(190, 130, 60))
        elif prop == "blood":
            for bx, by, rr in [(330, 420, 26), (400, 520, 32), (350, 640, 22), (420, 380, 18)]:
                d.ellipse([bx - rr, by - rr, bx + rr, by + rr], fill=(96, 18, 24))
        elif prop == "tears":
            d.line([(338, hy + 96), (334, hy + 140)], fill=(150, 210, 230), width=3)
            d.line([(384, hy + 96), (388, hy + 140)], fill=(150, 210, 230), width=3)
        elif prop == "laser":
            d.ellipse([348, 430, 372, 454], fill=(255, 40, 60))
            im = _screen_rgba(im, (360, 442), 40, (255, 40, 60))
            d = ImageDraw.Draw(im)
        elif prop == "cigar":
            d.rectangle([408, hy + 108, 448, hy + 118], fill=(60, 44, 30))
            d.ellipse([444, hy + 106, 454, hy + 120], fill=(255, 120, 40))
        elif prop == "clipboard":
            d.rectangle([430, 560, 520, 680], fill=(70, 78, 86))
            d.rectangle([440, 575, 510, 585], fill=(140, 150, 158))
            d.rectangle([440, 595, 510, 603], fill=(120, 130, 138))
        elif prop == "cords":
            d.rectangle([330, 700, 430, 716], fill=(150, 30, 40))
            d.rectangle([330, 722, 430, 734], fill=(150, 30, 40))
        elif prop == "vest":
            d.polygon([(300, 320), (420, 320), (430, 560), (290, 560)], fill=(22, 28, 34))
            d.rectangle([310, 360, 410, 380], fill=(36, 44, 52))
            d.rectangle([310, 420, 410, 440], fill=(36, 44, 52))
        elif prop == "rolled_sleeves":
            d.rectangle([170, 560, 215, 640], fill=(58, 62, 72))
            d.rectangle([505, 560, 550, 640], fill=(58, 62, 72))

    if eyes:
        ey = hy + 78
        d.rectangle([326, ey, 350, ey + 6], fill=rim + (255,))
        d.rectangle([372, ey, 396, ey + 6], fill=rim + (255,))

    im.save(out(f"images/sprites/{name}.png"))


def _screen_rgba(im, center, radius, color):
    glow = Image.new("RGBA", im.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(glow)
    cx, cy = center
    for i in range(12, 0, -1):
        r = radius * i / 12
        a = int(90 * (1 - i / 12))
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color + (a,))
    return Image.alpha_composite(im, glow)


# ----------------------------------------------------------------------------
# GUI
# ----------------------------------------------------------------------------

TEAL = (45, 225, 194)
PANEL = (10, 15, 21)
BORDER = (42, 58, 68)


def panel(w, h, fill=PANEL, alpha=235, border=BORDER, accent=None, radius=10):
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=radius, fill=fill + (alpha,), outline=border + (255,), width=2)
    if accent:
        d.rounded_rectangle([0, 0, w - 1, h - 1], radius=radius, outline=accent + (255,), width=2)
    return im


def gui_images():
    g = "gui"
    # textbox: dark bar with a teal hairline on top
    tb = panel(1920, 277, fill=(7, 11, 16), alpha=228, border=(26, 38, 46), radius=0)
    d = ImageDraw.Draw(tb)
    d.line([(0, 1), (1920, 1)], fill=TEAL + (140,), width=2)
    tb.save(out(f"{g}/textbox.png"))

    panel(450, 54, fill=(9, 14, 20), alpha=240, accent=TEAL, radius=8).save(out(f"{g}/namebox.png"))
    panel(900, 375, fill=(9, 13, 19), alpha=245, border=TEAL, radius=12).save(out(f"{g}/frame.png"))

    nvl = Image.new("RGBA", (1920, 1080), (5, 8, 12, 210))
    nvl.save(out(f"{g}/nvl.png"))

    panel(360, 64, alpha=200, radius=8).save(out(f"{g}/skip.png"))
    panel(1383, 64, alpha=200, radius=8).save(out(f"{g}/notify.png"))

    # speech bubbles
    for fname, hh in (("bubble.png", 155), ("thoughtbubble.png", 133)):
        b = Image.new("RGBA", (200, hh), (0, 0, 0, 0))
        d = ImageDraw.Draw(b)
        d.rounded_rectangle([2, 2, 197, hh - 26], radius=16, fill=(12, 18, 24, 235), outline=TEAL + (200,), width=2)
        if fname == "bubble.png":
            d.polygon([(60, hh - 28), (90, hh - 28), (70, hh - 4)], fill=(12, 18, 24, 235))
        else:
            d.ellipse([66, hh - 24, 82, hh - 8], fill=(12, 18, 24, 235), outline=TEAL + (200,))
            d.ellipse([52, hh - 10, 62, hh], fill=(12, 18, 24, 235), outline=TEAL + (200,))
        b.save(out(f"{g}/{fname}"))

    # buttons
    panel(450, 49, fill=(13, 19, 26), alpha=235, radius=8).save(out(f"{g}/button/idle_background.png"))
    panel(450, 49, fill=(18, 30, 38), alpha=245, accent=TEAL, radius=8).save(out(f"{g}/button/hover_background.png"))
    panel(1185, 52, fill=(10, 16, 22), alpha=225, border=(36, 50, 60), radius=8).save(out(f"{g}/button/choice_idle_background.png"))
    panel(1185, 52, fill=(16, 30, 36), alpha=245, accent=TEAL, radius=8).save(out(f"{g}/button/choice_hover_background.png"))
    panel(150, 45, fill=(10, 15, 21), alpha=180, radius=8).save(out(f"{g}/button/quick_idle_background.png"))
    panel(150, 45, fill=(18, 30, 38), alpha=220, accent=TEAL, radius=8).save(out(f"{g}/button/quick_hover_background.png"))
    panel(414, 309, fill=(10, 15, 21), alpha=235, radius=10).save(out(f"{g}/button/slot_idle_background.png"))
    panel(414, 309, fill=(16, 26, 34), alpha=245, accent=TEAL, radius=10).save(out(f"{g}/button/slot_hover_background.png"))

    # check / radio marks: tint template luminance to teal
    for fname in ("check_foreground.png", "check_selected_foreground.png", "radio_foreground.png", "radio_selected_foreground.png"):
        p = os.path.join(GAME, g, "button", fname)
        src = Image.open(p).convert("RGBA")
        lum = src.convert("L")
        sel = "selected" in fname
        col = TEAL if sel else (150, 170, 180)
        tinted = Image.new("RGBA", src.size, col + (0,))
        tinted.putalpha(lum)
        tinted.save(p)

    # bars / scrollbars / sliders: regenerate flat dark grooves + teal thumbs
    def groove(w, h):
        im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        d = ImageDraw.Draw(im)
        d.rounded_rectangle([0, 0, w - 1, h - 1], radius=min(w, h) // 2, fill=(16, 24, 30, 220), outline=(36, 50, 60, 255))
        return im

    def thumb(w, h, hover):
        im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        d = ImageDraw.Draw(im)
        c = TEAL + (255,) if hover else (90, 120, 130, 255)
        d.rounded_rectangle([0, 0, w - 1, h - 1], radius=min(w, h) // 2, fill=c)
        return im

    for kind in ("idle", "hover"):
        hv = kind == "hover"
        groove(1050, 18).save(out(f"{g}/scrollbar/horizontal_{kind}_bar.png"))
        thumb(1050, 18, hv).save(out(f"{g}/scrollbar/horizontal_{kind}_thumb.png"))
        groove(18, 1050).save(out(f"{g}/scrollbar/vertical_{kind}_bar.png"))
        thumb(18, 1050, hv).save(out(f"{g}/scrollbar/vertical_{kind}_thumb.png"))
        groove(525, 38).save(out(f"{g}/slider/horizontal_{kind}_bar.png"))
        thumb(15, 38, hv).save(out(f"{g}/slider/horizontal_{kind}_thumb.png"))
        groove(38, 525).save(out(f"{g}/slider/vertical_{kind}_bar.png"))
        thumb(38, 15, hv).save(out(f"{g}/slider/vertical_{kind}_thumb.png"))
        groove(525, 38).save(out(f"{g}/bar/left.png"))
        groove(525, 38).save(out(f"{g}/bar/right.png"))
        groove(38, 525).save(out(f"{g}/bar/top.png"))
        groove(38, 525).save(out(f"{g}/bar/bottom.png"))

    # overlays
    Image.new("RGBA", (1920, 1080), (3, 5, 8, 150)).save(out(f"{g}/overlay/main_menu.png"))
    Image.new("RGBA", (1920, 1080), (3, 5, 8, 170)).save(out(f"{g}/overlay/game_menu.png"))
    Image.new("RGBA", (1920, 1080), (2, 3, 6, 200)).save(out(f"{g}/overlay/confirm.png"))

    # window icon: neon glass shard
    icon = Image.new("RGBA", (250, 250), (6, 10, 14, 255))
    d = ImageDraw.Draw(icon)
    d.rounded_rectangle([4, 4, 246, 246], radius=36, outline=TEAL + (255,), width=6)
    d.polygon([(70, 190), (125, 45), (150, 120), (185, 90), (160, 195)], fill=(18, 30, 38, 255), outline=TEAL + (255,))
    d.line([(125, 45), (135, 130), (100, 190)], fill=(230, 57, 70, 255), width=4)
    icon.save(out(f"{g}/window_icon.png"))

    # phone variants: scale desktop counterparts into existing phone sizes
    phone_root = os.path.join(GAME, g, "phone")
    for root, _, files in os.walk(phone_root):
        for f in files:
            if not f.endswith(".png"):
                continue
            rel = os.path.relpath(os.path.join(root, f), phone_root)
            desktop = os.path.join(GAME, g, rel)
            if os.path.exists(desktop):
                ph = Image.open(os.path.join(root, f))
                size = ph.size
                Image.open(desktop).resize(size, Image.LANCZOS).save(os.path.join(root, f))


def scanlines():
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    for y in range(0, H, 4):
        d.line([(0, y), (W, y)], fill=(0, 0, 0, 255), width=2)
    im.save(out("images/fx/scanlines.png"))


def main():
    bg_alley().save(out("images/bg/neon_alley_rain.png"))
    bg_gallery().save(out("images/bg/ritesh_gallery_night.png"))
    bg_vault().save(out("images/bg/secret_vault.png"))
    bg_clinic().save(out("images/bg/cyber_clinic_morgue.png"))
    bg_cryo().save(out("images/bg/cryo_reveal.png"))
    bg_alley(darker=True).save(out("gui/main_menu.png"))
    menu = Image.open(out("gui/main_menu.png")).convert("RGB")
    Image.blend(menu, Image.new("RGB", menu.size, (4, 6, 10)), 0.35).save(out("gui/game_menu.png"))

    sprite("ritesh_coat_neutral", (230, 57, 70), props=("umbrella",))
    sprite("ritesh_coat_serious", (230, 57, 70), props=("umbrella",), eyes=True)
    sprite("ritesh_shirt_sleeves", (230, 57, 70), coat=False, props=("rolled_sleeves",))
    sprite("ritesh_dark_silhouette", (255, 30, 60), eyes=True)
    sprite("ritesh_kneeling", (230, 57, 70), kneeling=True)
    sprite("ritesh_bloodied", (230, 57, 70), props=("blood",))
    sprite("ritesh_crying", (230, 57, 70), kneeling=True, props=("tears",))
    sprite("detective_raincoat", (69, 123, 157), props=("topi",))
    sprite("detective_tactical", (69, 123, 157), props=("topi", "vest", "laser"))
    sprite("prosecutor_suit", (244, 162, 97), coat=False, props=("tie",))
    sprite("prosecutor_bloodied", (244, 162, 97), kneeling=True, coat=False, props=("blood", "cords"))
    sprite("boss_overcoat", (109, 89, 122), broad=True, props=("fedora", "cigar"))
    sprite("doctor_labcoat", (42, 157, 143), coat=False, props=("glasses", "clipboard"))

    scanlines()
    gui_images()
    print("Visual placeholders generated.")


if __name__ == "__main__":
    main()
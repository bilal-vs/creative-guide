"""Builds the Verdant Soft colour guidelines (v8): PNG pages + one PDF. Colour only; layouts and visuals live in brand/theme/.

    python3 brand/guidelines/build.py      (from the repo root)
"""
import os
import sys
sys.path.insert(0, 'brand/theme')
from PIL import Image, ImageDraw, ImageFilter
from kit import C, font, grad, rmask, glow, text_w, gtext, rgb
from colours import PALETTE, NEW_IN_V8, BRAND, MOODS, WEEK, GATES

W, H = 1600, 1000
M = 96
OUT = 'brand/guidelines'
PAGES = []
LIGHT_BG, DARK_BG = '#F2F7FB', '#050816'
RED = '#E5486F'
POS = {'top-left': (.05, .05), 'top-right': (.85, .1), 'centre-right': (.75, .55), 'centre': (.5, .5), 'top edge sheen': (.5, 0)}


# ---------------------------------------------------------------- helpers
def lum(h):
    c = lambda v: v / 12.92 if v <= .03928 else ((v + .055) / 1.055) ** 2.4
    r, g, b = [c(v / 255) for v in rgb(h)]
    return .2126 * r + .7152 * g + .0722 * b


def ratio(a, b):
    x, y = sorted([lum(a), lum(b)], reverse=True)
    return (x + .05) / (y + .05)


def worst(fg, grounds):
    return min(ratio(fg, g) for g in grounds)


def is_light(h):
    return lum(h) > .35


def wrap(text, fnt, width):
    words, lines, cur = text.split(), [], ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if text_w(t, fnt) <= width:
            cur = t
        else:
            lines.append(cur); cur = w
    return lines + ([cur] if cur else [])


def para(d, x, y, text, size, colour, width, weight=400, lead=1.45):
    f = font(size, weight)
    for line in wrap(text, f, width):
        d.text((x, y), line, fill=colour, font=f); y += int(size * lead)
    return y


def bullets(d, x, y, items, size, colour, width, dot, weight=400, gap=14):
    f = font(size, weight)
    for it in items:
        d.ellipse((x, y + size * .45, x + 10, y + size * .45 + 10), fill=dot)
        for line in wrap(it, f, width - 28):
            d.text((x + 28, y), line, fill=colour, font=f); y += int(size * 1.4)
        y += gap
    return y


def page(section, title, dark=False, kicker=None):
    im = Image.new('RGB', (W, H), DARK_BG if dark else LIGHT_BG)
    if dark:
        glow(im, (W - 700, -400, W + 300, 400), C['cobalt'], 220, 160)
    else:
        glow(im, (-300, -300, 500, 300), C['polar'], 255, 120)
    d = ImageDraw.Draw(im)
    fg = C['white'] if dark else C['abyss']; mute = C['sky'] if dark else C['steel']
    d.text((M, 54), section.upper(), fill=mute, font=font(18, 700))
    d.text((M, 92), title, fill=fg, font=font(56, 800))
    if kicker:
        d.text((M, 172), kicker, fill=mute, font=font(24, 400))
    return im, d, fg, mute


def finish(im, dark=False):
    n = len(PAGES) + 1
    d = ImageDraw.Draw(im); mute = C['sky'] if dark else C['steel']
    lg = Image.open('brand/brand-guide/png/verdant-logo-white.png' if dark else 'brand/brand-guide/png/verdant-logo-gradient.png').convert('RGBA')
    h = 26; lg = lg.resize((int(lg.width * h / lg.height), h), Image.LANCZOS); im.paste(lg, (M, H - 62), lg)
    d.text((W - M - text_w(f'{n:02d}', font(18, 700)), H - 58), f'{n:02d}', fill=mute, font=font(18, 700))
    PAGES.append(im)


def chip(im, d, x, y, w, h, col, r=16, dark=False):
    if isinstance(col, list) and len(col) > 1:
        im.paste(grad(w, h, col), (x, y), rmask(w, h, r))
    else:
        c = col[0] if isinstance(col, list) else col
        d.rounded_rectangle((x, y, x + w, y + h), radius=r, fill=c, outline=('#2A3B5C' if dark else '#C9D8E4'), width=2)


def swatch(d, x, y, w, h, name, hx, outline=False, new=False):
    tc = C['abyss'] if is_light(hx) else C['white']
    d.rounded_rectangle((x, y, x + w, y + h), radius=20, fill=hx, outline='#C9D8E4' if is_light(hx) else None, width=2)
    if outline:
        d.rounded_rectangle((x - 5, y - 5, x + w + 5, y + h + 5), radius=24, outline=C['abyss'], width=3)
    d.text((x + 16, y + h - 84), name, fill=tc, font=font(20, 800))
    r, g, b = rgb(hx)
    d.text((x + 16, y + h - 52), hx, fill=tc, font=font(17, 600))
    d.text((x + 16, y + h - 28), f'RGB {r} {g} {b}', fill=tc, font=font(13, 500))
    if new:
        d.rounded_rectangle((x + w - 60, y + 10, x + w - 10, y + 34), radius=12, fill=C['white'] if not is_light(hx) else C['abyss'])
        d.text((x + w - 52, y + 13), 'NEW', fill=C['abyss'] if not is_light(hx) else C['white'], font=font(13, 800))


def gbar(im, d, x, y, w, h, stops, label, mute, r=18):
    im.paste(grad(w, h, stops), (x, y), rmask(w, h, r))
    d.text((x, y + h + 10), label, fill=mute, font=font(18, 700))
    d.text((x, y + h + 36), ' · '.join(stops), fill=mute, font=font(16, 500))


def pair_rows(d, x, y, rows, fg, mute, width=680, step=66):
    """rows: (label, text colour, [grounds], min ratio). Reports the worst case across the grounds."""
    for label, tc, grounds, need in rows:
        r = worst(tc, grounds); ok = r >= need; gshow = min(grounds, key=lambda g: ratio(tc, g))
        d.rounded_rectangle((x, y, x + 130, y + 50), radius=14, fill=gshow, outline='#C9D8E4' if is_light(gshow) else '#2A3B5C', width=2)
        d.text((x + 20, y + 8), 'Aa', fill=tc, font=font(26, 800))
        d.text((x + 150, y + 4), label, fill=fg, font=font(19, 700))
        d.text((x + 150, y + 29), f'{tc} on {gshow} (worst case)', fill=mute, font=font(14, 500))
        d.text((x + width - 150, y + 11), f'{r:.1f}:1', fill=fg, font=font(21, 800))
        d.rounded_rectangle((x + width - 58, y + 12, x + width, y + 40), radius=14, fill=C['mint'] if ok else RED)
        d.text((x + width - 46, y + 15), 'OK' if ok else 'NO', fill=C['abyss'], font=font(15, 800))
        y += step
    return y


def mood_tile(mood, w=420, h=525):
    """Abstract colour tile: ground, one colour mass, ink bars, highlight bar, pill, accent. Shows colour and proportion, not a layout."""
    s = w / 1080
    im = grad(w, h, mood['ground'], 'a')
    gc, ga, gp = mood['ground_glow']; px, py = POS[gp]
    glow(im, (int(w * px - w * .45), int(h * py - h * .35), int(w * px + w * .45), int(h * py + h * .35)), gc, int(255 * ga / 100), int(90 * s * 2))
    dark = mood['theme'] == 'dark'
    mx0, my0, mx1, my1 = int(w * .42), int(h * .55), w + 30, h + 30
    if mood['mass_shadow']:
        col, a, oy, bl = mood['mass_shadow']; sh = Image.new('L', (w, h), 0)
        ImageDraw.Draw(sh).rounded_rectangle((mx0 + 6, my0 + int(oy * s * 2), mx1, my1), radius=int(44 * s * 2), fill=int(255 * a / 100 * 1.6))
        im.paste(Image.new('RGB', (w, h), rgb(col)), (0, 0), sh.filter(ImageFilter.GaussianBlur(bl * s * 2)))
    mass = grad(mx1 - mx0, my1 - my0, mood['mass'], 'd')
    for col, a, where in mood['mass_glows']:
        qx, qy = POS[where]; mw, mh = mass.size
        glow(mass, (int(mw * qx - mw * .45), int(mh * qy - mh * .45), int(mw * qx + mw * .45), int(mh * qy + mh * .45)), col, int(255 * a / 100 * 1.5), 30)
    im.paste(mass, (mx0, my0), rmask(mx1 - mx0, my1 - my0, int(44 * s * 2)))
    d = ImageDraw.Draw(im)
    if mood['mass_edge']:
        ov = Image.new('RGBA', (w, h), (0, 0, 0, 0)); ec, ea = mood['mass_edge']
        ImageDraw.Draw(ov).rounded_rectangle((mx0, my0, mx1, my1), radius=int(44 * s * 2), outline=rgb(ec) + (int(255 * ea / 100),), width=2)
        im.paste(ov, (0, 0), ov)
    x0 = int(w * .08)
    pw_ = int(w * .30); im.paste(grad(pw_, 18, mood['pill'] if len(mood['pill']) > 1 else mood['pill'] * 2), (x0, int(h * .14)), rmask(pw_, 18, 9))
    for i, (frac, hl) in enumerate([(.72, 0), (.55, 1), (.62, 0)]):
        yy = int(h * .22) + i * int(h * .075); bw = int(w * frac)
        if hl:
            im.paste(grad(bw, int(h * .05), mood['highlight']), (x0, yy), rmask(bw, int(h * .05), 6))
        else:
            d.rounded_rectangle((x0, yy, x0 + bw, yy + int(h * .05)), radius=6, fill=mood['headline'])
    im.paste(grad(int(w * .12), 6, BRAND), (x0, int(h * .47)), rmask(int(w * .12), 6, 3))
    d.rounded_rectangle((x0, int(h * .5), x0 + int(w * .45), int(h * .5) + 8), radius=4, fill=mood['supporting'])
    return im


def place(im, tile, x, y, dark=False, r=16):
    w, h = tile.size; sh = Image.new('L', im.size, 0)
    ImageDraw.Draw(sh).rounded_rectangle((x + 4, y + 12, x + w + 4, y + h + 12), radius=r + 4, fill=120 if dark else 80)
    im.paste(Image.new('RGB', im.size, rgb('#000000' if dark else '#9DB4CC')), (0, 0), sh.filter(ImageFilter.GaussianBlur(14)))
    im.paste(tile, (x, y), rmask(w, h, r))


# ---------------------------------------------------------------- 01 overall
def p_cover():
    im = Image.new('RGB', (W, H), DARK_BG)
    for box, col, a, b in [((700, -300, 1900, 700), C['cobalt'], 255, 170), ((1000, 300, 1800, 1200), C['ocean'], 200, 160),
                           ((850, 500, 1350, 1000), C['cyan'], 130, 140), ((1300, -100, 1800, 350), '#2457D6', 200, 120)]:
        glow(im, box, col, a, b)
    lg = Image.open('brand/brand-guide/png/verdant-logo-white.png').convert('RGBA'); h = 64
    lg = lg.resize((int(lg.width * h / lg.height), h), Image.LANCZOS); im.paste(lg, (M, 96), lg)
    d = ImageDraw.Draw(im)
    d.text((M, 420), 'Colour', fill=C['white'], font=font(132, 800))
    gtext(im, (M, 560), 'Guidelines', font(132, 800), [C['cyan'], C['mint']])
    d.text((M, 760), 'Social media · colour system v8 · two themes, four moods · October 2026', fill=C['sky'], font=font(26, 500))
    PAGES.append(im)


def p_contents():
    im, d, fg, mute = page('Contents', 'What’s inside')
    sections = [('01', 'Overall colour', 'Principles · core · palette · gradients · themes and moods · proportions · contrast · logo', '03'),
                ('02', 'Dark theme', 'Overview · Dark Royal · Dark Lagoon · surfaces · text and contrast · glows and checks · rules', '11'),
                ('03', 'Light theme', 'Overview · Light Royal · Light Lagoon · surfaces · text and contrast · glows and checks · rules', '18')]
    y = 270
    for num, name, desc, pg in sections:
        gtext(im, (M, y - 10), num, font(96, 800), ['#2457D6', '#007A9E'])
        d.text((M + 190, y), name, fill=fg, font=font(44, 800))
        d.text((M + 190, y + 62), desc, fill=mute, font=font(22, 400))
        d.text((W - M - 120, y + 10), f'p. {pg}', fill=mute, font=font(26, 700))
        d.line((M, y + 128, W - M, y + 128), fill='#D3E1EC', width=2)
        y += 190
    finish(im)


def p_principles():
    im, d, fg, mute = page('01 · Overall colour', 'Principles', kicker='Six rules behind every colour decision.')
    items = [('Two colours never change.', 'Slate Blue #416D95 and Sage Teal #74AFAD are the logo’s colours. Exactly as they are, in every theme, and as the accent bar on every post.'),
             ('Two themes, four moods.', 'Light and dark, each in a Royal (blue) and a Lagoon (teal) mood. The pillar picks the mood, so the feed has rhythm.'),
             ('Punch from saturation, not darkness.', 'Light posts stay light: their colour mass is a bright mid-tone, never a dark block. Dark posts glow from within.'),
             ('One colour mass per post.', 'One saturated shape carries the eye. Highlight colour goes on 1–3 words only.'),
             ('Tinted, never grey.', 'Shadows, borders and glows are tinted navy, royal or lagoon. No neutral grey and no pure white ground.'),
             ('Readable first.', 'Every text colour is listed with the grounds it passes on, measured at the worst point of each gradient.')]
    y = 236
    for i, (t, body) in enumerate(items):
        gtext(im, (M, y - 6), f'0{i + 1}', font(42, 800), ['#2457D6', '#007A9E'])
        d.text((M + 96, y), t, fill=fg, font=font(28, 800))
        para(d, M + 96, y + 40, body, 21, C['steel'], 1300, 400, 1.35)
        y += 112
    finish(im)


def p_core():
    im, d, fg, mute = page('01 · Overall colour', 'Core colours', kicker='Fixed. Taken from the logo and the website. Never tinted, shaded or substituted.')
    swatch(d, M, 240, 680, 400, 'Slate Blue', '#416D95', outline=True)
    swatch(d, M + 720, 240, 680, 400, 'Sage Teal', '#74AFAD', outline=True)
    im.paste(grad(1400, 64, BRAND), (M, 700), rmask(1400, 64, 20))
    d.text((M, 780), 'Brand gradient · #416D95 to #74AFAD · the logo, and the accent bar on every post', fill=mute, font=font(20, 600))
    bullets(d, M, 830, [f'Slate Blue: decorative on light (logo, accent bar); as text only on white ({ratio("#416D95", "#FFFFFF"):.1f}:1).',
                        f'Sage Teal: supporting text on Dark Lagoon ({worst("#74AFAD", MOODS["dark-lagoon"]["ground"]):.1f}:1); never text on light.'],
            19, C['steel'], 1400, '#2457D6', 500, 4)
    finish(im)


def p_palette():
    im, d, fg, mute = page('01 · Overall colour', 'Full palette', kicker='Twenty colours in five families. NEW marks the five added in v8.')
    y = 236
    for gname, sw in PALETTE:
        d.text((M, y + 40), gname.upper(), fill=mute, font=font(16, 700))
        x = M + 200
        for name, hx in sw:
            swatch(d, x, y, 196, 108, name, hx, outline=name in ('Slate Blue', 'Sage Teal'), new=name in NEW_IN_V8); x += 208
        y += 124
    d.text((M, H - 104), 'Retired: Royal Deep #2F62C8 (replaced by Electric Royal). Never: yellow, lime, orange, coral, green as the brand colour.', fill=RED, font=font(18, 700))
    finish(im)


def p_gradients():
    im, d, fg, mute = page('01 · Overall colour', 'Gradients', kicker='Fixed stops. Grounds, colour masses and highlights for each mood.')
    G = [('Brand · logo + accent bar', BRAND), ('Royal Tide · light mass', MOODS['light-royal']['mass']),
         ('Lagoon Tide · light mass', MOODS['light-lagoon']['mass']), ('Royal Aurora · dark mass', MOODS['dark-royal']['mass']),
         ('Lagoon Aurora · dark mass', MOODS['dark-lagoon']['mass']), ('Highlight · Light Royal', MOODS['light-royal']['highlight']),
         ('Highlight · Light Lagoon', MOODS['light-lagoon']['highlight']), ('Highlight · Dark Royal', MOODS['dark-royal']['highlight']),
         ('Highlight · Dark Lagoon', MOODS['dark-lagoon']['highlight']), ('Mist ground · Light Royal', MOODS['light-royal']['ground']),
         ('Polar ground · Light Lagoon', MOODS['light-lagoon']['ground']), ('Abyss ground · Dark Royal', MOODS['dark-royal']['ground']),
         ('Teal Night ground · Dark Lagoon', MOODS['dark-lagoon']['ground'])]
    for i, (n, st) in enumerate(G):
        col, row = i % 3, i // 3; x = M + col * 476; y = 226 + row * 136
        gbar(im, d, x, y, 450, 56, st, n, mute, 16)
    finish(im)


def p_moods():
    im, d, fg, mute = page('01 · Overall colour', 'Themes and moods', kicker='The pillar picks the mood. No two posts in a row share a theme and mood.')
    keys = ['light-royal', 'light-lagoon', 'dark-royal', 'dark-lagoon']
    for i, k in enumerate(keys):
        m = MOODS[k]; x = M + i * 352; tile = mood_tile(m, 320, 400)
        place(im, tile, x, 236, dark=m['theme'] == 'dark')
        d.text((x, 656), m['name'], fill=fg, font=font(26, 800))
        para(d, x, 694, m['pillars'], 17, mute, 320, 600, 1.35)
    y = 790; d.text((M, y), 'THE WEEK', fill=mute, font=font(16, 700))
    cw = (W - 2 * M - 6 * 12) // 7
    for i, (day, k, pil) in enumerate(WEEK):
        m = MOODS[k]; x = M + i * (cw + 12)
        im.paste(grad(cw, 74, m['mass']), (x, y + 30), rmask(cw, 74, 16))
        ImageDraw.Draw(im).text((x + 14, y + 38), day, fill=C['white'], font=font(20, 800))
        ImageDraw.Draw(im).text((x + 14, y + 68), m['name'], fill=C['white'], font=font(13, 600))
        d.text((x, y + 114), pil, fill=mute, font=font(15, 600))
    finish(im)


def p_proportions():
    im, d, fg, mute = page('01 · Overall colour', 'Proportions', kicker='How much of each colour a post uses. The ground dominates; highlight stays small.')
    rows = [('LIGHT THEME', [(.60, MOODS['light-royal']['ground'], 'Ground'), (.30, MOODS['light-royal']['mass'], 'Colour mass'),
                             (.06, '#050816', 'Ink text'), (.04, MOODS['light-royal']['highlight'], 'Highlight + accent')]),
            ('DARK THEME', [(.60, MOODS['dark-royal']['ground'], 'Ground'), (.30, MOODS['dark-royal']['mass'], 'Aurora mass'),
                            (.06, '#FFFFFF', 'White text'), (.04, MOODS['dark-royal']['highlight'], 'Highlight + accent')])]
    y = 250
    for title, parts in rows:
        d.text((M, y), title, fill=mute, font=font(18, 700)); cx = M
        for frac, col, label in parts:
            pw = int(1400 * frac)
            if isinstance(col, list):
                im.paste(grad(pw, 90, col), (cx, y + 36))
            else:
                d.rectangle((cx, y + 36, cx + pw, y + 126), fill=col, outline='#C9D8E4')
            d.text((cx + 6, y + 140), f'{int(frac * 100)}%', fill=fg, font=font(18, 800))
            d.text((cx + 6, y + 166), label, fill=mute, font=font(14, 500)); cx += pw
        y += 260
    bullets(d, M, 790, ['Colour mass: 25–40% of the frame. Ground: at least 50%.', 'Highlight colour on 1–3 words; the accent bar is the only other accent.'],
            21, C['steel'], 1400, '#2457D6', 500, 6)
    finish(im)


def p_contrast():
    im, d, fg, mute = page('01 · Overall colour', 'Contrast at a glance', kicker='Worst case across each mood’s ground. 4.5:1 for small text, 3:1 for headlines.')
    col = [('light-royal', 'light-lagoon'), ('dark-royal', 'dark-lagoon')]
    for ci, ks in enumerate(col):
        x = M + ci * 720; y = 236
        for k in ks:
            m = MOODS[k]; g = m['ground']
            d.text((x, y), m['name'].upper(), fill=mute, font=font(16, 700)); y += 28
            y = pair_rows(d, x, y, [('Headline', m['headline'], g, 4.5), ('Supporting', m['supporting'], g, 4.5),
                                     ('Highlight start', m['highlight'][0], g, 3), ('Highlight end', m['highlight'][-1], g, 3)], fg, mute, 680, 58) + 12
    finish(im)


def p_logo():
    im, d, fg, mute = page('01 · Overall colour', 'Logo colours', kicker='The logo keeps its own colours. Choose the lockup by the ground behind it.')
    boxes = [(MOODS['light-royal']['ground'], 'brand/brand-guide/png/verdant-logo-gradient.png', 'Gradient lockup · Light Royal'),
             (MOODS['light-lagoon']['ground'], 'brand/brand-guide/png/verdant-logo-gradient.png', 'Gradient lockup · Light Lagoon'),
             (MOODS['dark-royal']['ground'], 'brand/brand-guide/png/verdant-logo-white.png', 'White lockup · Dark Royal'),
             (MOODS['dark-lagoon']['ground'], 'brand/brand-guide/png/verdant-logo-white.png', 'White lockup · Dark Lagoon')]
    for i, (g, path, cap) in enumerate(boxes):
        x = M + i * 352
        im.paste(grad(330, 300, g, 'a'), (x, 240), rmask(330, 300, 24))
        lg = Image.open(path).convert('RGBA'); h = 46; lg = lg.resize((int(lg.width * h / lg.height), h), Image.LANCZOS)
        im.paste(lg, (x + (330 - lg.width) // 2, 240 + 127), lg)
        d.text((x, 556), cap, fill=mute, font=font(18, 600))
    bullets(d, M, 660, ['Never recolour the logo to match a post, never place it on the colour mass or a busy area, never add glow or outline.',
                        'The logo gradient is Slate Blue to Sage Teal and is never edited.'], 21, C['steel'], 1400, '#2457D6', 500, 8)
    finish(im)


# ---------------------------------------------------------------- 02/03 themes
def sec(theme):
    return '02 · Dark theme' if theme == 'dark' else '03 · Light theme'


def p_theme_overview(theme):
    dark = theme == 'dark'
    im, d, fg, mute = page(sec(theme), 'Dark theme' if dark else 'Light theme', dark,
                           'Glowing from within, never neon.' if dark else 'Light and luminous. Punch from saturated colour and strong ink, never from a dark block.')
    keys = ['dark-royal', 'dark-lagoon'] if dark else ['light-royal', 'light-lagoon']
    for i, k in enumerate(keys):
        m = MOODS[k]; x = M + i * 360
        place(im, mood_tile(m, 330, 412), x, 236, dark)
        d.text((x, 666), m['name'], fill=fg, font=font(26, 800))
        para(d, x, 704, m['idea'], 17, mute, 330, 500, 1.35)
    x = M + 760
    d.text((x, 240), 'WHAT STAYS THE SAME IN BOTH MOODS', fill=mute, font=font(16, 700))
    same = (['Headline in White, Inter 800', 'One aurora mass with a fine Polar edge; no drop shadows on dark',
             'Accent bar: brand gradient Slate Blue to Sage Teal', 'Pill: solid bright fill, Abyss text', 'White logo lockup']
            if dark else
            ['Headline in Abyss #050816, Inter 800', 'One bright colour mass with a tinted shadow; Cobalt never used as a fill',
             'Accent bar: brand gradient Slate Blue to Sage Teal', 'Pill: gradient fill, white text', 'Supporting text in Steel Navy #42658A', 'Gradient logo lockup'])
    y = bullets(d, x, 280, same, 21, fg, 640, C['cyan'] if dark else '#2457D6', 500, 8)
    d.text((x, y + 20), 'WHAT CHANGES WITH THE MOOD', fill=mute, font=font(16, 700))
    bullets(d, x, y + 60, ['Ground tint, colour mass, highlight gradient, pill colour, line colour' + (', supporting text' if dark else '')],
            21, fg, 640, C['cyan'] if dark else '#2457D6', 500, 8)
    finish(im, dark)


def role_row(im, d, x, y, label, col, desc, fg, mute, dark, w=640):
    chip(im, d, x, y, 120, 64, col, 14, dark)
    d.text((x + 140, y + 2), label, fill=fg, font=font(20, 800))
    hexes = col if isinstance(col, list) else [col]
    para(d, x + 140, y + 30, (desc + ' · ' if desc else '') + ' · '.join(h for h in hexes if h.startswith('#')), 15, mute, w - 140, 500, 1.35)


def p_mood(k):
    m = MOODS[k]; dark = m['theme'] == 'dark'
    im, d, fg, mute = page(sec(m['theme']), m['name'], dark, f'{m["idea"]}  For: {m["pillars"]}.')
    place(im, mood_tile(m, 400, 500), M, 236, dark)
    glows = ', '.join(f'{c} at {a}% ({w})' for c, a, w in m['mass_glows'])
    rows = [('Ground', m['ground'], f'Gradient, glow {m["ground_glow"][0]} at {m["ground_glow"][1]}% {m["ground_glow"][2]}'),
            ('Colour mass · ' + m['mass_name'], m['mass'], 'Glows: ' + glows),
            ('Headline', m['headline'], 'Inter 800'), ('Highlight words', m['highlight'], '1–3 words'),
            ('Supporting text', m['supporting'], 'Sublines, captions, footer'), ('Meta text', m['meta'], 'Counters, small labels'),
            ('Pill', m['pill'], f'Text {m["pill_text"]}'), ('Accent bar', BRAND, 'Brand gradient'),
            ('Lines and borders', m['lines'], 'Hairlines, card borders'), ('Logo', BRAND if not dark else '#FFFFFF', m['logo'])]
    for i, (label, col, desc) in enumerate(rows):
        x = M + 460 + (i % 2) * 520; y = 236 + (i // 2) * 120
        role_row(im, d, x, y, label, col, desc, fg, mute, dark, 500)
    finish(im, dark)


def p_surfaces(theme):
    dark = theme == 'dark'
    im, d, fg, mute = page(sec(theme), 'Surfaces and depth', dark,
                           'Depth from edges and glow, never drop shadows.' if dark else 'Four levels. Shadows are tinted with the mood colour, never grey.')
    for i, k in enumerate(['dark-royal', 'dark-lagoon'] if dark else ['light-royal', 'light-lagoon']):
        m = MOODS[k]; x = M + i * 720; y = 236
        g = grad(680, 560, m['ground'], 'a'); im.paste(g, (x, y), rmask(680, 560, 28))
        dd = ImageDraw.Draw(im)
        levels = [('L0 Ground', None), ('L1 Surface', m['surface']), ('L2 Raised', m['raised']), ('L3 Colour mass', 'mass')]
        for j, (name, spec) in enumerate(levels):
            bx, by, bw, bh = x + 40 + j * 40, y + 50 + j * 120, 420, 96
            if spec is None:
                dd.text((bx, by + 30), 'L0 Ground · ' + ' · '.join(m['ground']), fill=fg, font=font(16, 700)); continue
            if spec == 'mass':
                if m['mass_shadow']:
                    col, a, oy, bl = m['mass_shadow']; sh = Image.new('L', im.size, 0)
                    ImageDraw.Draw(sh).rounded_rectangle((bx + 6, by + oy // 2, bx + bw, by + bh + oy // 2), radius=24, fill=int(255 * a / 100 * 1.4))
                    im.paste(Image.new('RGB', im.size, rgb(col)), (0, 0), sh.filter(ImageFilter.GaussianBlur(bl // 3)))
                im.paste(grad(bw, bh, m['mass']), (bx, by), rmask(bw, bh, 24))
                if m['mass_edge']:
                    ov = Image.new('RGBA', im.size, (0, 0, 0, 0)); ec, ea = m['mass_edge']
                    ImageDraw.Draw(ov).rounded_rectangle((bx, by, bx + bw, by + bh), radius=24, outline=rgb(ec) + (int(255 * ea / 100),), width=2)
                    im.paste(ov, (0, 0), ov)
                label = f'L3 {m["mass_name"]}' + (f' · shadow {m["mass_shadow"][0]} at {m["mass_shadow"][1]}%' if m['mass_shadow'] else f' · edge Polar at {m["mass_edge"][1]}%')
                ImageDraw.Draw(im).text((bx + 20, by + 34), label, fill=C['white'], font=font(16, 700)); continue
            if spec.get('shadow'):
                col, a, oy, bl = spec['shadow']; sh = Image.new('L', im.size, 0)
                ImageDraw.Draw(sh).rounded_rectangle((bx + 4, by + oy // 2, bx + bw, by + bh + oy // 2), radius=22, fill=int(255 * a / 100 * 1.8))
                im.paste(Image.new('RGB', im.size, rgb(col)), (0, 0), sh.filter(ImageFilter.GaussianBlur(max(6, bl // 3))))
            if spec['fill'].startswith('#'):
                ImageDraw.Draw(im).rounded_rectangle((bx, by, bx + bw, by + bh), radius=22, fill=spec['fill'], outline=spec['border'] if spec['border'].startswith('#') else None, width=2)
            else:
                a = .88 if not dark else .08
                base = im.crop((bx, by, bx + bw, by + bh)).filter(ImageFilter.GaussianBlur(10))
                im.paste(Image.blend(base, Image.new('RGB', (bw, bh), (255, 255, 255)), a), (bx, by), rmask(bw, bh, 22))
                ov = Image.new('RGBA', im.size, (0, 0, 0, 0))
                ImageDraw.Draw(ov).rounded_rectangle((bx, by, bx + bw, by + bh), radius=22, outline=(255, 255, 255, 255 if not dark else 40), width=2)
                im.paste(ov, (0, 0), ov)
            sh_txt = f' · shadow {spec["shadow"][0]} at {spec["shadow"][1]}%' if spec.get('shadow') else ''
            ImageDraw.Draw(im).text((bx + 20, by + 22), f'{name} · {spec["fill"]}', fill=m['headline'], font=font(16, 700))
            ImageDraw.Draw(im).text((bx + 20, by + 50), f'border {spec["border"]}{sh_txt}', fill=m['supporting'], font=font(14, 500))
        d.text((x, y + 576), m['name'], fill=fg, font=font(22, 800))
    finish(im, dark)


def p_text(theme):
    dark = theme == 'dark'
    im, d, fg, mute = page(sec(theme), 'Text colour and contrast', dark, 'Measured at the worst point of each ground gradient, and on surfaces and the mass.')
    for i, k in enumerate(['dark-royal', 'dark-lagoon'] if dark else ['light-royal', 'light-lagoon']):
        m = MOODS[k]; x = M + i * 720; g = m['ground']
        surf = [m['surface']['fill']] if m['surface']['fill'].startswith('#') else []
        d.text((x, 230), m['name'].upper(), fill=mute, font=font(16, 700))
        pair_rows(d, x, 260, [('Headline', m['headline'], g + surf, 4.5), ('Highlight start', m['highlight'][0], g, 3), ('Highlight end', m['highlight'][-1], g, 3),
                              ('Supporting', m['supporting'], g + surf, 4.5), ('Meta', m['meta'], g + surf, 4.5),
                              ('Pill text', m['pill_text'], m['pill'], 4.5), ('Text on the mass', m['text_on_mass'], m['mass'][:2], 4.5 if dark else 3)],
                  fg, mute, 680, 62)
    para(d, M, 720, 'Text on the mass: White only, headline size, at the mass’s darkest end. Body text never sits on the mass.'
         + ('' if dark else ' Slate Blue is never small text on light (4.3:1 worst case); Cyan, Mint Jade, Sage Teal and Polar are never text on light.'),
         20, C['steel'] if not dark else C['sky'], 1400, 500)
    finish(im, dark)


def p_glows(theme):
    dark = theme == 'dark'
    im, d, fg, mute = page(sec(theme), 'Glows and automatic checks', dark, 'Exact glow recipes, and the checks the pipeline runs on every image.')
    y = 236
    for k in (['dark-royal', 'dark-lagoon'] if dark else ['light-royal', 'light-lagoon']):
        m = MOODS[k]
        d.text((M, y), m['name'].upper(), fill=mute, font=font(16, 700)); y += 34
        gc, ga, gp = m['ground_glow']
        recipe = [f'Ground glow: {gc} at {ga}%, {gp}, very soft (blur about a third of the frame)'] + \
                 [f'Mass glow: {c} at {a}%, {w}' for c, a, w in m['mass_glows']] + \
                 ([f'Mass shadow: {m["mass_shadow"][0]} at {m["mass_shadow"][1]}%, offset {m["mass_shadow"][2]} px down, blur {m["mass_shadow"][3]} px'] if m['mass_shadow']
                  else [f'Mass edge: Polar #E9FFFC at {m["mass_edge"][1]}%, 1–2 px; no drop shadow'])
        for j, r in enumerate(recipe):
            col = r.split(': ')[1].split(' ')[0]
            if col.startswith('#'):
                glow_sw = Image.new('RGB', (64, 40), rgb(DARK_BG if dark else '#FFFFFF')); glow(glow_sw, (-10, -20, 74, 60), col, 255, 10)
                im.paste(glow_sw, (M, y), rmask(64, 40, 12))
            d.text((M + 84, y + 8), r, fill=fg, font=font(18, 500)); y += 50
        y += 18
    x = M + 860
    d.rounded_rectangle((x, 236, W - M, 760), radius=26, fill='#0B1530' if dark else '#FFFFFF')
    d.text((x + 30, 262), 'AUTOMATIC CHECK · ' + theme.upper(), fill=C['cyan'] if dark else '#2457D6', font=font(18, 800))
    bullets(d, x + 30, 310, GATES[theme] + ['Fail any check: regenerate. Never publish a light post that reads half-dark, or a dark post with no glow.'],
            20, fg, 560, C['cyan'] if dark else '#2457D6', 500, 14)
    finish(im, dark)


def p_rules(theme):
    dark = theme == 'dark'
    im, d, fg, mute = page(sec(theme), 'Do and don’t', dark)
    if dark:
        do = ['Pick the mood by pillar: Royal for Insight, Lagoon for Brand world', 'One aurora mass, glowing from within, with a fine Polar edge',
              'White headlines; Sky (Royal) or Sage Teal (Lagoon) supporting text', 'Highlight 1–3 words: Sky to Cyan, or Cyan to Mint Jade',
              'Pill: solid Cyan or Mint Jade with Abyss text', 'Brand-gradient accent bar on every post']
        dont = ['Royal navy (#194493-style) or pure black grounds', 'Drop shadows on dark; use edges and glow instead',
                'Every element glowing; more than one glow source competing', 'White text on Cyan or Mint Jade (2.0:1)',
                'Mint Jade as a large fill (it starts to read as green)', 'Yellow, lime, orange, coral']
    else:
        do = ['Pick the mood by pillar: Royal for How we work and Proof, Lagoon for Grow with us', 'One bright colour mass, 25–40% of the frame, tinted shadow',
              'Abyss headlines; Steel Navy supporting text', 'Highlight 1–3 words: Electric Royal to Deep Ocean, or Deep Ocean to Deep Lagoon',
              'White cards and glass with tinted borders', 'Brand-gradient accent bar on every post']
        dont = ['Cobalt Night, Navy or Abyss as a fill (light posts stay light)', 'Pure white ground; grey shadows',
                'Cyan, Mint Jade, Sage Teal or Polar as text', 'Body text on the colour mass', 'Pastel-only, washed-out posts', 'Yellow, lime, orange, coral']
    card = '#0B1530' if dark else '#FFFFFF'
    for col, (t, items, c) in enumerate([('Do', do, C['cyan'] if dark else '#2457D6'), ('Don’t', dont, RED)]):
        x = M + col * 720
        d.rounded_rectangle((x, 200, x + 690, 880), radius=28, fill=card)
        d.text((x + 36, 228), t, fill=c, font=font(36, 800))
        bullets(d, x + 36, 304, items, 22, fg, 610, c, 500, 18)
    finish(im, dark)


def p_back():
    im = Image.new('RGB', (W, H), DARK_BG)
    for box, col, a, b in [((-200, 400, 900, 1300), C['cobalt'], 255, 170), ((200, 600, 900, 1200), C['ocean'], 170, 150), ((300, 700, 700, 1100), C['cyan'], 110, 120)]:
        glow(im, box, col, a, b)
    d = ImageDraw.Draw(im)
    d.text((M, 360), 'Let’s build it', fill=C['white'], font=font(110, 800))
    gtext(im, (M + text_w('Let’s build it ', font(110, 800)), 360), 'right.', font(110, 800), [C['cyan'], C['mint']])
    d.text((M, 520), 'verdant-soft.com · info@verdant-soft.com · Lahore, Pakistan', fill=C['sky'], font=font(26, 500))
    lg = Image.open('brand/brand-guide/png/verdant-logo-white.png').convert('RGBA'); h = 48
    lg = lg.resize((int(lg.width * h / lg.height), h), Image.LANCZOS); im.paste(lg, (M, H - 130), lg)
    PAGES.append(im)


if __name__ == '__main__':
    p_cover(); p_contents(); p_principles(); p_core(); p_palette(); p_gradients(); p_moods(); p_proportions(); p_contrast(); p_logo()
    for theme in ('dark', 'light'):
        p_theme_overview(theme)
        for k in [k for k in MOODS if MOODS[k]['theme'] == theme]:
            p_mood(k)
        p_surfaces(theme); p_text(theme); p_glows(theme); p_rules(theme)
    p_back()
    os.makedirs(f'{OUT}/pages', exist_ok=True)
    for f in os.listdir(f'{OUT}/pages'):
        os.remove(f'{OUT}/pages/{f}')
    for i, p in enumerate(PAGES, 1):
        p.save(f'{OUT}/pages/{i:02d}.png', optimize=True)
    for f in os.listdir(OUT):
        if f.endswith('.pdf'):
            os.remove(f'{OUT}/{f}')
    PAGES[0].save(f'{OUT}/verdant-soft-colour-guidelines.pdf', save_all=True, append_images=PAGES[1:], resolution=120, quality=92)
    print(len(PAGES), 'pages')

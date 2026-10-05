"""Builds the Verdant Soft colour guidelines: PNG pages + one PDF. Colour only; layouts and visuals live in brand/theme/.

    python3 brand/guidelines/build.py      (from the repo root)
"""
import os
import sys
sys.path.insert(0, 'brand/theme')
from PIL import Image, ImageDraw
from kit import C, font, grad, rmask, glow, text_w, gtext, rgb

W, H = 1600, 1000
M = 96
OUT = 'brand/guidelines'
PAGES = []
LIGHT_BG, DARK_BG = '#F2F7FB', '#050816'
RED = '#E5486F'


def lum(h):
    c = lambda v: v / 12.92 if v <= .03928 else ((v + .055) / 1.055) ** 2.4
    r, g, b = [c(v / 255) for v in rgb(h)]
    return .2126 * r + .7152 * g + .0722 * b


def ratio(a, b):
    x, y = sorted([lum(a), lum(b)], reverse=True)
    return (x + .05) / (y + .05)


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


def swatch(d, x, y, w, h, name, hx, outline=False, sub=None):
    tc = C['abyss'] if is_light(hx) else C['white']
    d.rounded_rectangle((x, y, x + w, y + h), radius=22, fill=hx, outline='#C9D8E4' if is_light(hx) else None, width=2)
    if outline:
        d.rounded_rectangle((x - 5, y - 5, x + w + 5, y + h + 5), radius=26, outline=C['abyss'], width=3)
    d.text((x + 20, y + h - 96), name, fill=tc, font=font(24, 800))
    r, g, b = rgb(hx)
    d.text((x + 20, y + h - 58), hx, fill=tc, font=font(19, 600))
    d.text((x + 20, y + h - 32), f'RGB {r} {g} {b}', fill=tc, font=font(15, 500))
    if sub:
        d.text((x, y + h + 12), sub, fill=C['steel'], font=font(16, 500))


def gbar(im, d, x, y, w, h, stops, label, mute, r=20):
    im.paste(grad(w, h, stops), (x, y), rmask(w, h, r))
    d.text((x, y + h + 10), label, fill=mute, font=font(18, 700))
    d.text((x, y + h + 36), ' · '.join(stops), fill=mute, font=font(16, 500))


def pair_rows(d, x, y, rows, ground, fg, mute, width=660):
    """rows: (label, text colour, ground colour or None, min ratio)."""
    for label, tc, gc, need in rows:
        gc = gc or ground; r = ratio(tc, gc); ok = r >= need
        d.rounded_rectangle((x, y, x + 150, y + 54), radius=14, fill=gc, outline='#C9D8E4' if is_light(gc) else '#2A3B5C', width=2)
        d.text((x + 22, y + 9), 'Aa', fill=tc, font=font(28, 800))
        d.text((x + 175, y + 6), label, fill=fg, font=font(20, 700))
        d.text((x + 175, y + 32), f'{tc} on {gc}', fill=mute, font=font(15, 500))
        tag = f'{r:.1f}:1'
        d.text((x + width - 150, y + 14), tag, fill=fg, font=font(22, 800))
        d.rounded_rectangle((x + width - 60, y + 14, x + width, y + 42), radius=14, fill=C['mint'] if ok else RED)
        d.text((x + width - 48, y + 17), 'OK' if ok else 'NO', fill=C['abyss'], font=font(16, 800))
        y += 72
    return y


def proportion(im, d, x, y, w, parts, mute):
    cx = x
    for frac, hx, label in parts:
        pw = int(w * frac)
        if isinstance(hx, list):
            im.paste(grad(pw, 90, hx), (cx, y))
        else:
            d.rectangle((cx, y, cx + pw, y + 90), fill=hx)
        d.text((cx + 6, y + 104), f'{int(frac * 100)}%', fill=mute, font=font(18, 800))
        d.text((cx + 6, y + 130), label, fill=mute, font=font(15, 500))
        cx += pw
    ov = Image.new('L', im.size, 0)


# ------------------------------------------------------------------ pages
def p_cover():
    im = Image.new('RGB', (W, H), DARK_BG)
    for box, col, a, b in [((700, -300, 1900, 700), C['cobalt'], 255, 170), ((1000, 300, 1800, 1200), C['ocean'], 200, 160),
                           ((850, 500, 1350, 1000), C['cyan'], 130, 140), ((1300, -100, 1800, 350), C['royal'], 200, 120)]:
        glow(im, box, col, a, b)
    lg = Image.open('brand/brand-guide/png/verdant-logo-white.png').convert('RGBA'); h = 64
    lg = lg.resize((int(lg.width * h / lg.height), h), Image.LANCZOS); im.paste(lg, (M, 96), lg)
    d = ImageDraw.Draw(im)
    d.text((M, 420), 'Colour', fill=C['white'], font=font(132, 800))
    gtext(im, (M, 560), 'Guidelines', font(132, 800), [C['cyan'], C['mint']])
    d.text((M, 760), 'Social media · palette v6 · dark and light themes · October 2026', fill=C['sky'], font=font(26, 500))
    PAGES.append(im)


def p_contents():
    im, d, fg, mute = page('Contents', 'What’s inside')
    sections = [('01', 'Overall colour', 'Principles · core colours · full palette · gradients · proportions · contrast · logo colours', '03'),
                ('02', 'Dark theme colours', 'Roles · grounds and gradients · text and contrast · do and don’t', '10'),
                ('03', 'Light theme colours', 'Roles · grounds and gradients · text and contrast · do and don’t', '13')]
    y = 270
    for num, name, desc, pg in sections:
        gtext(im, (M, y - 10), num, font(96, 800), [C['royal_deep'], C['ocean']])
        d.text((M + 190, y), name, fill=fg, font=font(44, 800))
        d.text((M + 190, y + 62), desc, fill=mute, font=font(24, 400))
        d.text((W - M - 120, y + 10), f'p. {pg}', fill=mute, font=font(26, 700))
        d.line((M, y + 128, W - M, y + 128), fill='#D3E1EC', width=2)
        y += 190
    finish(im)


def p_principles():
    im, d, fg, mute = page('01 · Overall colour', 'Principles', kicker='How the palette works, in five rules.')
    items = [('Two colours never change.', 'Slate Blue #416D95 and Sage Teal #74AFAD are the logo’s colours. They appear exactly as they are, in every theme.'),
             ('Deep grounds, bright light.', 'Navy and cobalt give depth; ocean teals and cyans bring the energy; ice and polar keep it airy.'),
             ('One accent family per post.', 'A post uses its ground, the core colours, and either the teals or the blues as accent, plus at most one light tone.'),
             ('Colour has a job.', 'One mass of colour per post carries the eye. Highlight colour goes on 1–3 words, never on whole paragraphs.'),
             ('Readable first.', 'Every text colour is paired only with grounds where it passes contrast (page 08).')]
    y = 250
    for i, (t, body) in enumerate(items):
        gtext(im, (M, y - 6), f'0{i + 1}', font(44, 800), [C['royal_deep'], C['ocean']])
        d.text((M + 100, y), t, fill=fg, font=font(30, 800))
        para(d, M + 100, y + 44, body, 22, C['steel'], 1250, 400, 1.35)
        y += 132
    finish(im)


def p_core():
    im, d, fg, mute = page('01 · Overall colour', 'Core colours', kicker='Fixed. Taken from the logo and the website. Never tinted, shaded or substituted.')
    swatch(d, M, 240, 680, 420, 'Slate Blue', '#416D95', outline=True)
    swatch(d, M + 720, 240, 680, 420, 'Sage Teal', '#74AFAD', outline=True)
    im.paste(grad(1400, 70, ['#416D95', '#74AFAD']), (M, 720), rmask(1400, 70, 20))
    d.text((M, 805), 'Brand gradient · 102° · #416D95 to #74AFAD · the logo, and nothing else changes it', fill=mute, font=font(20, 600))
    bullets(d, M, 850, [f'Slate Blue: text on white {ratio("#416D95", "#FFFFFF"):.1f}:1 · Sage Teal: text on Abyss {ratio("#74AFAD", "#050816"):.1f}:1, never text on light grounds.'],
            20, C['steel'], 1400, C['royal'], 500)
    finish(im)


def p_palette():
    im, d, fg, mute = page('01 · Overall colour', 'Full palette', kicker='Five families. Names and hex codes are the reference for every post and prompt.')
    groups = [('Core · fixed', [('Slate Blue', '#416D95'), ('Sage Teal', '#74AFAD')]),
              ('Deep grounds', [('Abyss', '#050816'), ('Navy', '#1E3058'), ('Cobalt Night', '#151754')]),
              ('Ocean teals', [('Mint Jade', '#34CCA4'), ('Jade', '#00A598'), ('Lagoon', '#00ACB3'), ('Cyan', '#09CACC'), ('Ocean', '#0088AA')]),
              ('Blues', [('Royal Blue', '#3C6EB7'), ('Royal Deep', '#2F62C8'), ('Steel Navy', '#42658A')]),
              ('Lights', [('Sky', '#A6CAEC'), ('Ice', '#EBF5F7'), ('Polar', '#E9FFFC'), ('White', '#FFFFFF')])]
    y = 236
    for gname, sw in groups:
        d.text((M, y + 46), gname.upper(), fill=mute, font=font(17, 700))
        x = M + 230
        for name, hx in sw:
            swatch(d, x, y, 226, 112, name, hx, outline=name in ('Slate Blue', 'Sage Teal')); x += 242
        y += 127
    d.text((M, H - 104), 'Never: yellow, lime, orange, coral, or green as the brand colour.', fill=RED, font=font(20, 700))
    finish(im)


def p_gradients():
    im, d, fg, mute = page('01 · Overall colour', 'Gradients', kicker='Built from the core outward. Stops are fixed; angles may vary.')
    G = [('Brand · logo only', ['#416D95', '#74AFAD']), ('Lagoon · hero colour', ['#74AFAD', '#09CACC', '#3C6EB7']),
         ('Highlight · words on light', ['#2F62C8', '#0088AA']), ('Highlight · words on dark', ['#09CACC', '#34CCA4']),
         ('Cobalt · colour block on light', ['#151754', '#21387B', '#3C6EB7']), ('Aurora panel · colour mass on dark', ['#0B1A3A', '#21387B', '#1D4A8A']),
         ('Ice ground · light theme', ['#F4F9FC', '#E6F1F8', '#D6E7F4']), ('Abyss ground · dark theme', ['#050816', '#070C20', '#0B1530']),
         ('Ocean · teal objects', ['#34CCA4', '#00ACB3', '#0088AA']), ('Daybreak · light accents', ['#EBF5F7', '#A6CAEC', '#3C6EB7'])]
    for i, (n, st) in enumerate(G):
        col, row = i % 2, i // 2; x = M + col * 720; y = 226 + row * 136
        gbar(im, d, x, y, 680, 62, st, n, mute)
    finish(im)


def p_proportions():
    im, d, fg, mute = page('01 · Overall colour', 'Proportions', kicker='How much of each colour a post uses. Ground dominates; highlight colour stays small.')
    d.text((M, 250), 'LIGHT THEME', fill=mute, font=font(18, 700))
    proportion(im, d, M, 285, 1400, [(.60, ['#F4F9FC', '#D6E7F4'], 'Ice ground'), (.25, ['#151754', '#3C6EB7'], 'Cobalt colour block'),
                                     (.10, '#050816', 'Abyss text'), (.05, ['#2F62C8', '#0088AA'], 'Highlight')], mute)
    d.text((M, 520), 'DARK THEME', fill=mute, font=font(18, 700))
    proportion(im, d, M, 555, 1400, [(.65, ['#050816', '#0B1530'], 'Abyss ground'), (.20, ['#0B1A3A', '#1D4A8A'], 'Aurora panel'),
                                     (.10, '#FFFFFF', 'White text'), (.05, ['#09CACC', '#34CCA4'], 'Highlight')], mute)
    bullets(d, M, 800, ['Highlight colour covers 1–3 words and small accents (pill, bar), about 5% of the post.',
                        'One colour mass only: a block on light, an aurora panel on dark.'], 22, C['steel'], 1400, C['royal'], 500, 6)
    finish(im)


def p_contrast():
    im, d, fg, mute = page('01 · Overall colour', 'Contrast', kicker='Text colours and the grounds they may sit on. 4.5:1 for small text, 3:1 for headlines.')
    d.text((M, 236), 'ON LIGHT GROUNDS', fill=mute, font=font(18, 700))
    pair_rows(d, M, 270, [('Headline · Abyss', '#050816', '#E6F1F8', 4.5), ('Highlight · Royal Deep', '#2F62C8', '#E6F1F8', 3),
                          ('Highlight · Ocean', '#0088AA', '#E6F1F8', 3), ('Supporting · Steel Navy', '#42658A', '#E6F1F8', 4.5),
                          ('Core · Slate Blue', '#416D95', '#FFFFFF', 4.5), ('Never · Cyan as text', '#09CACC', '#E6F1F8', 3),
                          ('Never · Sage Teal as text', '#74AFAD', '#FFFFFF', 3)], '#E6F1F8', fg, mute)
    d.text((M + 740, 236), 'ON DARK GROUNDS', fill=mute, font=font(18, 700))
    pair_rows(d, M + 740, 270, [('Headline · White', '#FFFFFF', '#050816', 4.5), ('Highlight · Cyan', '#09CACC', '#050816', 4.5),
                                ('Highlight · Mint Jade', '#34CCA4', '#050816', 4.5), ('Supporting · Sky', '#A6CAEC', '#050816', 4.5),
                                ('Core · Sage Teal', '#74AFAD', '#050816', 4.5), ('Text on block · White', '#FFFFFF', '#21387B', 4.5),
                                ('Never · Slate Blue small text', '#416D95', '#050816', 4.5)], '#050816', fg, mute)
    finish(im)


def p_logo():
    im, d, fg, mute = page('01 · Overall colour', 'Logo colours', kicker='The logo keeps its own colours. Choose the lockup by the ground behind it.')
    boxes = [((M, 240, M + 440, 560), '#FFFFFF', 'brand/brand-guide/png/verdant-logo-gradient.png', 'Gradient lockup · white, ice, polar grounds'),
             ((M + 480, 240, M + 920, 560), '#E6F1F8', 'brand/brand-guide/png/verdant-logo-gradient.png', 'Gradient lockup · ice ground'),
             ((M + 960, 240, W - M, 560), DARK_BG, 'brand/brand-guide/png/verdant-logo-white.png', 'White lockup · abyss, navy, cobalt, any block')]
    for (x0, y0, x1, y1), bg, path, cap in boxes:
        d.rounded_rectangle((x0, y0, x1, y1), radius=26, fill=bg, outline='#C9D8E4', width=2)
        lg = Image.open(path).convert('RGBA'); h = 64; lg = lg.resize((int(lg.width * h / lg.height), h), Image.LANCZOS)
        im.paste(lg, ((x0 + x1 - lg.width) // 2, (y0 + y1 - h) // 2), lg)
        d.text((x0, y1 + 16), cap, fill=mute, font=font(19, 600))
    bullets(d, M, 680, ['Never recolour the logo to match a post, never put it on a busy or mid-tone area, never add glow or outline.',
                        'The gradient in the logo is Slate Blue to Sage Teal and is not edited.'], 22, C['steel'], 1400, C['royal'], 500, 8)
    finish(im)


def p_theme_roles(dark):
    sec = '02 · Dark theme colours' if dark else '03 · Light theme colours'
    im, d, fg, mute = page(sec, 'Colour roles', dark, 'Every colour on a ' + ('dark' if dark else 'light') + ' post, and its job.')
    roles = ([('Ground', ['#050816', '#0B1530'], 'Abyss gradient, with a soft Cobalt Night glow top-left'),
              ('Colour mass', ['#0B1A3A', '#1D4A8A'], 'One aurora panel; Cyan and Royal Blue glow inside; fine Polar edge at 35%'),
              ('Headline', '#FFFFFF', 'White'), ('Highlight words', ['#09CACC', '#34CCA4'], 'Cyan to Mint Jade'),
              ('Supporting text', '#A6CAEC', 'Sky: sublines, captions, footer'), ('Label pill', ['#09CACC', '#34CCA4'], 'Cyan to Mint Jade fill, Abyss text'),
              ('Accent bar', ['#09CACC', '#34CCA4'], 'Cyan to Mint Jade'), ('Lines, dots', '#2A3B5C', 'Quiet navy'), ('Logo', '#FFFFFF', 'White lockup')]
             if dark else
             [('Ground', ['#F4F9FC', '#D6E7F4'], 'Ice gradient, with a Polar glow top-left; never flat white'),
              ('Colour mass', ['#151754', '#3C6EB7'], 'One block, Cobalt Night to Royal Blue, Cyan glow inside'),
              ('Headline', '#050816', 'Abyss'), ('Highlight words', ['#2F62C8', '#0088AA'], 'Royal Deep to Ocean'),
              ('Supporting text', '#42658A', 'Steel Navy: sublines, captions, footer'), ('Label pill', ['#2F62C8', '#0088AA'], 'Royal Deep to Ocean fill, white text'),
              ('Accent bar', ['#2F62C8', '#09CACC'], 'Royal Deep to Cyan'), ('Lines, dots', '#B9CDE0', 'Soft blue-grey'), ('Logo', ['#416D95', '#74AFAD'], 'Gradient lockup')])
    y = 230
    for i, (role, col, desc) in enumerate(roles):
        x = M + (i % 2) * 720; yy = y + (i // 2) * 128
        if isinstance(col, list):
            im.paste(grad(150, 90, col), (x, yy), rmask(150, 90, 18))
        else:
            d.rounded_rectangle((x, yy, x + 150, yy + 90), radius=18, fill=col, outline='#C9D8E4' if is_light(col) else '#2A3B5C', width=2)
        d.text((x + 175, yy + 6), role, fill=fg, font=font(24, 800))
        para(d, x + 175, yy + 42, desc + ('' if isinstance(col, list) else f' · {col}'), 18, mute, 500, 500, 1.35)
    finish(im, dark)


def p_theme_grounds(dark):
    sec = '02 · Dark theme colours' if dark else '03 · Light theme colours'
    im, d, fg, mute = page(sec, 'Grounds and gradients', dark, 'The backdrop and the one colour mass. Exact stops and glow colours.')
    if dark:
        g = grad(660, 520, ['#050816', '#070C20', '#0B1530'], 'a'); glow(g, (-200, -200, 300, 250), C['cobalt'], 200, 110)
        im.paste(g, (M, 230), rmask(660, 520, 30))
        p = grad(660, 520, ['#0B1A3A', '#21387B', '#1D4A8A'], 'd'); glow(p, (230, 180, 760, 600), C['cyan'], 170, 90); glow(p, (400, -150, 860, 200), C['royal'], 160, 80)
        im.paste(p, (M + 740, 230), rmask(660, 520, 30))
        ImageDraw.Draw(im).rounded_rectangle((M + 740, 230, M + 1400, 750), radius=30, outline=(150, 220, 240), width=2)
        caps = [('Abyss ground', '#050816 · #070C20 · #0B1530, diagonal; glow Cobalt Night #151754, top-left'),
                ('Aurora panel', '#0B1A3A · #21387B · #1D4A8A; glows Cyan #09CACC (centre-right) and Royal Blue #3C6EB7 (top-right); edge Polar at 35%')]
    else:
        g = grad(660, 520, ['#F4F9FC', '#E6F1F8', '#D6E7F4'], 'a'); glow(g, (-200, -200, 300, 250), C['polar'], 255, 110)
        im.paste(g, (M, 230), rmask(660, 520, 30)); ImageDraw.Draw(im).rounded_rectangle((M, 230, M + 660, 750), radius=30, outline='#C9D8E4', width=2)
        p = grad(660, 520, ['#151754', '#21387B', '#3C6EB7'], 'd'); glow(p, (230, 180, 760, 600), C['cyan'], 150, 90)
        im.paste(p, (M + 740, 230), rmask(660, 520, 30))
        caps = [('Ice ground', '#F4F9FC · #E6F1F8 · #D6E7F4, diagonal; glow Polar #E9FFFC, top-left'),
                ('Colour block', '#151754 · #21387B · #3C6EB7; glow Cyan #09CACC, centre-right; soft Royal Blue shadow')]
    d = ImageDraw.Draw(im)
    for i, (t, c) in enumerate(caps):
        x = M + i * 740
        d.text((x, 772), t, fill=fg, font=font(26, 800)); para(d, x, 812, c, 19, mute, 640, 500, 1.4)
    finish(im, dark)


def p_theme_text(dark):
    sec = '02 · Dark theme colours' if dark else '03 · Light theme colours'
    im, d, fg, mute = page(sec, 'Text colour and rules', dark)
    ground = '#050816' if dark else '#E6F1F8'
    rows = ([('Headline · White', '#FFFFFF', None, 4.5), ('Highlight · Cyan', '#09CACC', None, 4.5), ('Highlight · Mint Jade', '#34CCA4', None, 4.5),
             ('Supporting · Sky', '#A6CAEC', None, 4.5), ('Pill text · Abyss on Cyan', '#050816', '#09CACC', 4.5), ('On panel · White', '#FFFFFF', '#21387B', 4.5)]
            if dark else
            [('Headline · Abyss', '#050816', None, 4.5), ('Highlight · Royal Deep', '#2F62C8', None, 3), ('Highlight · Ocean', '#0088AA', None, 3),
             ('Supporting · Steel Navy', '#42658A', None, 4.5), ('Pill text · White on Royal Deep', '#FFFFFF', '#2F62C8', 4.5), ('On block · White', '#FFFFFF', '#21387B', 4.5)])
    pair_rows(d, M, 220, rows, ground, fg, mute)
    do = (['Abyss ground with one aurora panel', 'White headlines, Sky supporting text', 'Cyan to Mint Jade on 1–3 words', 'Glows in Cyan and Royal Blue only']
          if dark else
          ['Ice ground, never flat white', 'Abyss headlines, Steel Navy supporting text', 'Royal Deep to Ocean on 1–3 words', 'One Cobalt block per post'])
    dont = (['Royal navy (#194493-style) or pure black grounds', 'Slate Blue as small text (3.6:1)', 'Every element glowing', 'Yellow, lime, orange, coral']
            if dark else
            ['Cyan, Mint Jade, Sage Teal or Polar as text', 'Gradient text in body copy', 'Pastel-only, washed-out posts', 'Yellow, lime, orange, coral'])
    x = M + 760; card = '#0B1530' if dark else '#FFFFFF'
    for i, (t, items, c) in enumerate([('Do', do, C['cyan'] if dark else C['royal_deep']), ('Don’t', dont, RED)]):
        yy = 220 + i * 330
        d.rounded_rectangle((x, yy, W - M, yy + 300), radius=26, fill=card)
        d.text((x + 30, yy + 22), t, fill=c, font=font(30, 800))
        bullets(d, x + 30, yy + 80, items, 21, fg, 560, c, 500, 8)
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
    p_cover(); p_contents(); p_principles(); p_core(); p_palette(); p_gradients(); p_proportions(); p_contrast(); p_logo()
    for dark in (True, False):
        p_theme_roles(dark); p_theme_grounds(dark); p_theme_text(dark)
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

"""Verdant Soft post kit: the shared components and the seven templates, in a light and a dark theme.

Draws mockups at full post size (1080 x 1350) with the real brand typeface (Inter, brand/fonts/).
Used by brand/guidelines/build.py. Run from the repo root.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

PW, PH = 1080, 1350                      # post canvas (4:5)
SX, SY = 84, 110                         # safe margins: sides, top/bottom
FONTS = 'brand/fonts'
C = dict(abyss='#050816', navy='#1E3058', cobalt='#151754', navy2='#21387B', royal='#3C6EB7', royal_deep='#2F62C8',
         steel='#42658A', slate='#416D95', sage='#74AFAD', ocean='#0088AA', cyan='#09CACC', mint='#34CCA4',
         lagoon='#00ACB3', jade='#00A598', polar='#E9FFFC', ice='#EBF5F7', sky='#A6CAEC', white='#FFFFFF')


def font(sz, weight=700, family='Inter'):
    return ImageFont.truetype(f'{FONTS}/{family}-{weight}.ttf', sz)


def rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def grad(w, h, stops, mode='h'):
    g = Image.new('RGB', (w, h)); px = g.load(); cols = [rgb(c) for c in stops]; n = len(cols) - 1
    for x in range(w):
        for y in range(h):
            t = {'h': x / w, 'v': y / h, 'd': x / w * .5 + y / h * .5, 'a': x / w * .35 + y / h * .65}[mode]
            t = max(0, min(.9999, t)); i = min(int(t * n), n - 1); f = t * n - i; a, b = cols[i], cols[i + 1]
            px[x, y] = tuple(int(a[k] + (b[k] - a[k]) * f) for k in range(3))
    return g


def rmask(w, h, r):
    m = Image.new('L', (w, h), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, w - 1, h - 1), radius=r, fill=255)
    return m


def glow(img, box, col, alpha, blur):
    w, h = img.size; m = Image.new('L', (w, h), 0)
    ImageDraw.Draw(m).ellipse(box, fill=alpha); m = m.filter(ImageFilter.GaussianBlur(blur))
    img.paste(Image.new('RGB', (w, h), rgb(col)), (0, 0), m)


def text_w(text, fnt):
    return ImageDraw.Draw(Image.new('L', (1, 1))).textbbox((0, 0), text, font=fnt)[2]


def gtext(im, xy, text, fnt, stops):
    x, y = xy; bb = ImageDraw.Draw(im).textbbox((0, 0), text, font=fnt); w, h = bb[2] + 4, bb[3] + 16
    m = Image.new('L', (w, h), 0); ImageDraw.Draw(m).text((0, 0), text, fill=255, font=fnt)
    im.paste(grad(w, h, stops), (x, y), m)
    return bb[2]


# ---------- themes ----------
def _light_ground():
    im = grad(PW, PH, ['#F4F9FC', '#E6F1F8', '#D6E7F4'], 'a')
    glow(im, (-250, -250, 450, 350), C['polar'], 255, 110)
    return im


def _dark_ground():
    im = grad(PW, PH, ['#050816', '#070C20', '#0B1530'], 'a')
    glow(im, (-300, -300, 500, 380), C['cobalt'], 200, 140)
    return im


LIGHT = dict(name='light', ground=_light_ground, ink=C['abyss'], hl=[C['royal_deep'], C['ocean']], sub=C['steel'],
             footer=C['steel'], pill=[C['royal_deep'], C['ocean']], pill_fg=C['white'], accent=[C['royal_deep'], C['cyan']],
             logo='brand/brand-guide/png/verdant-logo-gradient.png', block=[C['cobalt'], C['navy2'], C['royal']],
             block_glow=C['cyan'], shadow=C['royal'], shadow_a=110, row_glass=.55, row_ink=C['abyss'],
             dot='#B9CDE0', quote=[C['polar'], C['cyan']], edge=None)
DARK = dict(name='dark', ground=_dark_ground, ink=C['white'], hl=[C['cyan'], C['mint']], sub=C['sky'],
            footer=C['sky'], pill=[C['cyan'], C['mint']], pill_fg=C['abyss'], accent=[C['cyan'], C['mint']],
            logo='brand/brand-guide/png/verdant-logo-white.png', block=['#0B1A3A', C['navy2'], '#1D4A8A'],
            block_glow=C['cyan'], shadow=C['cyan'], shadow_a=70, row_glass=.10, row_ink=C['white'],
            dot='#2A3B5C', quote=[C['cyan'], C['mint']], edge=(150, 220, 240))


# ---------- components ----------
def logo(im, th, x=SX, y=SY, h=52):
    lg = Image.open(th['logo']).convert('RGBA'); w = int(lg.width * h / lg.height)
    lg = lg.resize((w, h), Image.LANCZOS); im.paste(lg, (x, y), lg)


def pill(im, th, x, y, text, size=26):
    w = text_w(text, font(size, 700)) + 52
    im.paste(grad(w, 58, th['pill']), (x, y), rmask(w, 58, 29))
    ImageDraw.Draw(im).text((x + 26, y + 13), text, fill=th['pill_fg'], font=font(size, 700))
    return w


def headline(im, th, x, y, lines, size=100, lead=1.06, weight=800):
    f = font(size, weight)
    for runs in lines:
        cx = x
        for text, hl in runs:
            if hl:
                cx += gtext(im, (cx, y), text, f, th['hl'])
            else:
                ImageDraw.Draw(im).text((cx, y), text, fill=th['ink'], font=f); cx += text_w(text, f)
        y += int(size * lead)
    return y


def accent(im, th, x, y, w=110):
    im.paste(grad(w, 10, th['accent']), (x, y), rmask(w, 10, 5))


def sub(im, th, x, y, text, size=32):
    ImageDraw.Draw(im).text((x, y), text, fill=th['sub'], font=font(size, 400))


def footer(im, th, text='verdant-soft.com', colour=None):
    ImageDraw.Draw(im).text((SX, PH - SY - 2), text, fill=colour or th['footer'], font=font(24, 600))


def block(im, th, box, radius=44, glow_at=(.35, .35, 1.15, 1.2)):
    """Light: the one saturated colour block. Dark: the one aurora panel (glowing, with a fine light edge)."""
    x0, y0, x1, y1 = box; w, h = x1 - x0, y1 - y0
    blk = grad(w, h, th['block'], 'd')
    gx0, gy0, gx1, gy1 = glow_at
    glow(blk, (int(w * gx0), int(h * gy0), int(w * gx1), int(h * gy1)), th['block_glow'], 150 if th['name'] == 'light' else 170, 90)
    if th['name'] == 'dark':
        glow(blk, (int(w * .6), int(h * -.3), int(w * 1.3), int(h * .4)), C['royal'], 160, 80)
    sh = Image.new('L', im.size, 0)
    ImageDraw.Draw(sh).rounded_rectangle((x0 + 10, y0 + 30, x1 + 10, y1 + 30), radius=radius, fill=th['shadow_a'])
    im.paste(Image.new('RGB', im.size, rgb(th['shadow'])), (0, 0), sh.filter(ImageFilter.GaussianBlur(44)))
    im.paste(blk, (x0, y0), rmask(w, h, radius))
    if th['edge']:
        ov = Image.new('RGBA', im.size, (0, 0, 0, 0))
        ImageDraw.Draw(ov).rounded_rectangle(box, radius=radius, outline=th['edge'] + (90,), width=2)
        im.paste(ov, (0, 0), ov)


def glass(im, box, r=26, a=.35, edge_a=255):
    x0, y0, x1, y1 = box; w, h = x1 - x0, y1 - y0
    base = im.crop(box).filter(ImageFilter.GaussianBlur(16))
    im.paste(Image.blend(base, Image.new('RGB', (w, h), (255, 255, 255)), a), (x0, y0), rmask(w, h, r))
    ov = Image.new('RGBA', im.size, (0, 0, 0, 0))
    ImageDraw.Draw(ov).rounded_rectangle(box, radius=r, outline=(255, 255, 255, edge_a), width=3)
    im.paste(ov, (0, 0), ov)


def bars(im, bx, by):
    spec = [(150, 300, 90, 150, [C['mint'], C['cyan']]), (270, 200, 90, 250, [C['cyan'], C['lagoon']]),
            (390, 90, 90, 360, [C['polar'], C['cyan']])]
    for x, y, w, h, st in spec:
        glow(im, (bx + x - 30, by + y + h - 40, bx + x + w + 30, by + y + h + 50), C['cyan'], 140, 35)
    for x, y, w, h, st in spec:
        im.paste(grad(w, h, st, 'v'), (bx + x, by + y), rmask(w, h, 24))
        hl = Image.new('L', (w, h), 0); ImageDraw.Draw(hl).rounded_rectangle((7, 7, w // 3, h - 7), radius=18, fill=70)
        im.paste(Image.new('RGB', (w, h), (255, 255, 255)), (bx + x, by + y), hl)


def glass_stack(im, th, bx, by):
    for i, (x, y) in enumerate([(70, 80), (140, 180), (210, 280)]):
        glass(im, (bx + x, by + y, bx + x + 380, by + y + 200), a=.20 + .1 * i, edge_a=230)
        st = [[C['mint'], C['cyan']], [C['cyan'], C['polar']], [C['polar'], C['cyan']]][i]
        im.paste(grad(170 + 40 * i, 14, st), (bx + x + 36, by + y + 50), rmask(170 + 40 * i, 14, 7))
        d = ImageDraw.Draw(im)
        d.rounded_rectangle((bx + x + 36, by + y + 90, bx + x + 260, by + y + 100), radius=5, fill='#C9DCEC')
        d.ellipse((bx + x + 320, by + y + 42, bx + x + 350, by + y + 72), fill=C['cyan'] if i < 2 else C['white'])


def network(im, cx, cy):
    pts = [(-150, -110, 16, C['polar']), (140, -140, 16, C['sky']), (150, 120, 16, C['mint']), (-130, 130, 16, C['sage']), (40, -230, 10, C['polar'])]
    glow(im, (cx - 140, cy - 140, cx + 140, cy + 140), C['cyan'], 160, 50)
    d = ImageDraw.Draw(im)
    for dx, dy, r, c in pts:
        d.line((cx, cy, cx + dx, cy + dy), fill='#9FE3E8', width=4)
    d.ellipse((cx - 38, cy - 38, cx + 38, cy + 38), fill=C['cyan'])
    for dx, dy, r, c in pts:
        d.ellipse((cx + dx - r, cy + dy - r, cx + dx + r, cy + dy + r), fill=c)


def quote_mark(im, th, x, y, size=380):
    f = font(size, 800); q = Image.new('L', (int(size * .9), int(size * .8)), 0)
    ImageDraw.Draw(q).text((0, -int(size * .12)), '“', fill=255, font=f)
    im.paste(grad(q.width, q.height, th['quote'], 'd'), (x, y), q)


def list_rows(im, th, x, y, items, w=912):
    for i, t in enumerate(items):
        top = y + i * 150
        glass(im, (x, top, x + w, top + 124), r=30, a=th['row_glass'], edge_a=200 if th['name'] == 'light' else 70)
        im.paste(grad(76, 76, th['hl'], 'd'), (x + 26, top + 24), rmask(76, 76, 38))
        d = ImageDraw.Draw(im)
        n = str(i + 1); d.text((x + 64 - text_w(n, font(36, 800)) // 2, top + 37), n, fill=th['pill_fg'], font=font(36, 800))
        d.text((x + 130, top + 38), t, fill=th['row_ink'], font=font(40, 700))


def page_counter(im, th, n, total):
    txt = f'{n:02d} / {total:02d}'; f = font(26, 700)
    ImageDraw.Draw(im).text((PW - SX - text_w(txt, f), SY + 10), txt, fill=th['sub'], font=f)


def dots(im, th, n, total, y=PH - SY + 6):
    d = ImageDraw.Draw(im); x = PW - SX - total * 26 - 14
    for i in range(total):
        if i == n - 1:
            im.paste(grad(40, 12, th['accent']), (x, y), rmask(40, 12, 6)); x += 52
        else:
            d.ellipse((x, y, x + 12, y + 12), fill=th['dot']); x += 26


def photo_frame(im, box):
    x0, y0, x1, y1 = box; w, h = x1 - x0, y1 - y0
    ph = grad(w, h, ['#C9D9E8', '#AFC6DB'], 'd'); d = ImageDraw.Draw(ph)
    d.ellipse((w // 2 - 90, h // 2 - 170, w // 2 + 90, h // 2 + 10), fill='#93AFC9')
    d.rounded_rectangle((w // 2 - 180, h // 2 + 40, w // 2 + 180, h + 60), radius=120, fill='#93AFC9')
    d.text((24, h - 50), 'real photo · news inbox', fill='#F4F9FC', font=font(22, 500))
    im.paste(ph, (x0, y0), rmask(w, h, 36))
    ImageDraw.Draw(im).rounded_rectangle(box, radius=36, outline=(255, 255, 255), width=8)


# ---------- templates ----------
def t_hero(th):
    im = th['ground'](); logo(im, th); pill(im, th, SX, 206, 'Built to scale')
    y = headline(im, th, 80, 290, [[('Built for the', 0)], [('next stage', 1)], [('of growth', 0)]])
    accent(im, th, SX + 4, y + 26); sub(im, th, SX, y + 56, 'Software that scales with your business.')
    block(im, th, (500, 760, 1140, 1410)); bars(im, 500, 760); footer(im, th); return im


def t_glass(th):
    im = th['ground'](); logo(im, th); pill(im, th, SX, 206, 'Outsourcing, Decoded')
    y = headline(im, th, 80, 290, [[('You pay at', 0)], [('milestones', 1)], [('you can see', 0)]])
    accent(im, th, SX + 4, y + 26); sub(im, th, SX, y + 56, 'At kickoff, at key phases, at final delivery.')
    block(im, th, (430, 770, 1130, 1410)); glass_stack(im, th, 430, 770); footer(im, th); return im


def t_quote(th):
    im = th['ground'](); block(im, th, (600, -60, 1200, 420), glow_at=(.33, .33, 1.17, 1.17)); quote_mark(im, th, 760, 70)
    logo(im, th); pill(im, th, SX, 206, 'Client words')
    f = font(62, 800); y = 500
    ImageDraw.Draw(im).text((SX, y), 'They', fill=th['ink'], font=f)
    gtext(im, (SX + text_w('They ', f), y), 'quickly', f, th['hl'])
    for i, l in enumerate(['understood our problem,', 'collaborated effectively', 'with our team, and', 'delivered a solid', 'solution.']):
        ImageDraw.Draw(im).text((SX, y + 78 * (i + 1)), l, fill=th['ink'], font=f)
    accent(im, th, SX + 4, y + 78 * 6 + 26, 90)
    ImageDraw.Draw(im).text((SX, y + 78 * 6 + 56), 'Isana Sebastian', fill=th['sub'], font=font(34, 700))
    footer(im, th); return im


def t_list(th):
    im = th['ground'](); block(im, th, (-60, 1120, 1140, 1420), radius=56, glow_at=(.45, .1, 1.2, 1.6))
    logo(im, th); pill(im, th, SX, 206, 'Wireframe to Production')
    y = headline(im, th, 80, 290, [[('Before the first', 0)], [('line of code', 1)]], size=92)
    accent(im, th, SX + 4, y + 26); sub(im, th, SX, y + 56, 'Our UI/UX process starts here.')
    list_rows(im, th, SX, 640, ['Research & discovery', 'User personas', 'Architecture & wireframing'])
    footer(im, th, colour=C['white']); return im


def t_cover(th):
    im = th['ground'](); logo(im, th); pill(im, th, SX, 206, 'Outsourcing, Decoded · 03')
    y = headline(im, th, 80, 290, [[('Can I hire you', 0)], [('for just one', 0)], [('service?', 1)]], size=96)
    accent(im, th, SX + 4, y + 26); sub(im, th, SX, y + 56, 'Swipe for the short answer.')
    block(im, th, (560, 820, 1140, 1410)); network(im, 860, 1060)
    footer(im, th); dots(im, th, 1, 5); return im


def t_slide(th):
    im = th['ground'](); logo(im, th); page_counter(im, th, 2, 5)
    y = headline(im, th, 80, 250, [[('Yes. ', 0), ('Pick one.', 1)]], size=88)
    sub(im, th, SX, y + 12, 'Each service works on its own or together.')
    block(im, th, (SX, 520, PW - SX, 1130), radius=40, glow_at=(.5, .4, 1.3, 1.4))
    for i, s in enumerate(['Custom Software Development', 'Cloud & DevOps', 'IT Team Outsourcing', 'UI/UX Design']):
        top = 580 + i * 130; glass(im, (SX + 50, top, PW - SX - 50, top + 100), r=50, a=.16, edge_a=170)
        d = ImageDraw.Draw(im); d.ellipse((SX + 80, top + 36, SX + 108, top + 64), fill=C['cyan'])
        d.text((SX + 136, top + 27), s, fill=C['white'], font=font(38, 700))
    footer(im, th); dots(im, th, 2, 5); return im


def t_people(th):
    im = th['ground'](); block(im, th, (480, 560, 1140, 1410), glow_at=(.2, .5, 1.1, 1.3)); photo_frame(im, (560, 640, 1000, 1180))
    logo(im, th); pill(im, th, SX, 206, 'Grow with us')
    y = headline(im, th, 80, 290, [[('Welcome', 0)], [('to the team', 1)]], size=100)
    accent(im, th, SX + 4, y + 26)
    d = ImageDraw.Draw(im); d.text((SX, y + 60), '[Name]', fill=th['ink'], font=font(40, 800))
    d.text((SX, y + 112), '[Role]', fill=th['sub'], font=font(30, 400))
    footer(im, th); return im


TEMPLATES = [('HERO', 'Hero in block', 'How we work · Brand world', t_hero),
             ('GLASS', 'Glass in block', 'How we work', t_glass),
             ('QUOTE', 'Client words', 'Proof', t_quote),
             ('LIST', 'Steps list', 'How we work · Insight', t_list),
             ('COVER', 'Carousel cover', 'Series · carousels', t_cover),
             ('SLIDE', 'Carousel slide', 'Series · carousels', t_slide),
             ('PEOPLE', 'People', 'Grow with us (inbox photo)', t_people)]


def render_all(th):
    return [(('L-' if th['name'] == 'light' else 'D-') + tid, name, use, fn(th)) for tid, name, use, fn in TEMPLATES]

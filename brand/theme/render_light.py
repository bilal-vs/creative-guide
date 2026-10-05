"""Light theme v2 for Verdant Soft posts: components, templates and reference sheets.

Renders mockups only (DejaVu stands in for the brand typeface). Run from the repo root:
    python3 brand/theme/render_light.py
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUT = 'brand/theme'
PW, PH = 1080, 1350                      # post canvas (4:5)
SX, SY = 84, 110                         # safe margins: sides, top/bottom
C = dict(abyss='#050816', royal='#3C6EB7', royal_deep='#2F62C8', steel='#42658A', slate='#416D95',
         sage='#74AFAD', ocean='#0088AA', cyan='#09CACC', mint='#34CCA4', lagoon='#00ACB3',
         polar='#E9FFFC', ice='#EBF5F7', sky='#A6CAEC', cobalt='#151754', navy2='#21387B', white='#FFFFFF')
HL = [C['royal_deep'], C['ocean']]       # highlight-word gradient (passes 4:1 on the ice ground)
LOGO = 'brand/brand-guide/png/verdant-logo-gradient.png'


def font(sz, bold=True, serif=False):
    if serif:
        return ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf', sz)
    name = 'DejaVuSans-Bold.ttf' if bold else 'DejaVuSans.ttf'
    return ImageFont.truetype('/usr/share/fonts/truetype/dejavu/' + name, sz)


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


# ---------- components ----------
def ground():
    """Tinted ice ground with a polar glow top-left. Never pure white."""
    im = grad(PW, PH, ['#F4F9FC', '#E6F1F8', '#D6E7F4'], 'a')
    glow(im, (-250, -250, 450, 350), C['polar'], 255, 110)
    return im


def logo(im, x=SX, y=SY, h=52):
    lg = Image.open(LOGO).convert('RGBA'); w = int(lg.width * h / lg.height)
    lg = lg.resize((w, h), Image.LANCZOS); im.paste(lg, (x, y), lg)


def pill(im, x, y, text, size=26):
    d = ImageDraw.Draw(im); w = d.textbbox((0, 0), text, font=font(size))[2] + 52
    im.paste(grad(w, 58, HL), (x, y), rmask(w, 58, 29))
    ImageDraw.Draw(im).text((x + 26, y + 13), text, fill=C['white'], font=font(size))
    return w


def gtext(im, xy, text, fnt, stops=HL):
    x, y = xy; bb = ImageDraw.Draw(im).textbbox((0, 0), text, font=fnt); w, h = bb[2] + 4, bb[3] + 14
    m = Image.new('L', (w, h), 0); ImageDraw.Draw(m).text((0, 0), text, fill=255, font=fnt)
    im.paste(grad(w, h, stops), (x, y), m)
    return bb[2]


def headline(im, x, y, lines, size=100, lead=1.08):
    """lines: list of lists of (text, highlighted) runs. Returns the y below the block."""
    f = font(size)
    for runs in lines:
        cx = x
        for text, hl in runs:
            if hl:
                cx += gtext(im, (cx, y), text, f)
            else:
                d = ImageDraw.Draw(im); d.text((cx, y), text, fill=C['abyss'], font=f)
                cx += d.textbbox((0, 0), text, font=f)[2]
        y += int(size * lead)
    return y


def accent(im, x, y, w=110):
    im.paste(grad(w, 10, [C['royal_deep'], C['cyan']]), (x, y), rmask(w, 10, 5))


def sub(im, x, y, text, size=32):
    ImageDraw.Draw(im).text((x, y), text, fill=C['steel'], font=font(size, bold=False))


def footer(im, text='verdant-soft.com', arrow=False):
    d = ImageDraw.Draw(im); d.text((SX, PH - SY - 4), text, fill=C['steel'], font=font(24))
    if arrow:
        d.text((PW - SX - 40, PH - SY - 10), '→', fill=C['royal_deep'], font=font(34))


def block(im, box, radius=44, glow_at=(.35, .35, 1.15, 1.2)):
    """The one saturated colour block per post: cobalt → royal, cyan glow inside, soft royal shadow."""
    x0, y0, x1, y1 = box; w, h = x1 - x0, y1 - y0
    blk = grad(w, h, [C['cobalt'], C['navy2'], C['royal']], 'd')
    gx0, gy0, gx1, gy1 = glow_at
    glow(blk, (int(w * gx0), int(h * gy0), int(w * gx1), int(h * gy1)), C['cyan'], 150, 90)
    sh = Image.new('L', im.size, 0)
    ImageDraw.Draw(sh).rounded_rectangle((x0 + 10, y0 + 30, x1 + 10, y1 + 30), radius=radius, fill=110)
    im.paste(Image.new('RGB', im.size, rgb(C['royal'])), (0, 0), sh.filter(ImageFilter.GaussianBlur(40)))
    im.paste(blk, (x0, y0), rmask(w, h, radius))


def glass(im, box, r=26, a=.35):
    x0, y0, x1, y1 = box; w, h = x1 - x0, y1 - y0
    base = im.crop(box).filter(ImageFilter.GaussianBlur(16))
    im.paste(Image.blend(base, Image.new('RGB', (w, h), (255, 255, 255)), a), (x0, y0), rmask(w, h, r))
    ImageDraw.Draw(im).rounded_rectangle(box, radius=r, outline=(255, 255, 255), width=3)


def bars(im, bx, by):
    spec = [(150, 300, 90, 150, [C['mint'], C['cyan']]), (270, 200, 90, 250, [C['cyan'], C['lagoon']]),
            (390, 90, 90, 360, [C['polar'], C['cyan']])]
    for x, y, w, h, st in spec:
        glow(im, (bx + x - 30, by + y + h - 40, bx + x + w + 30, by + y + h + 50), C['cyan'], 140, 35)
    for x, y, w, h, st in spec:
        im.paste(grad(w, h, st, 'v'), (bx + x, by + y), rmask(w, h, 24))
        hl = Image.new('L', (w, h), 0); ImageDraw.Draw(hl).rounded_rectangle((7, 7, w // 3, h - 7), radius=18, fill=70)
        im.paste(Image.new('RGB', (w, h), (255, 255, 255)), (bx + x, by + y), hl)


def glass_stack(im, bx, by):
    for i, (x, y) in enumerate([(70, 80), (140, 180), (210, 280)]):
        glass(im, (bx + x, by + y, bx + x + 380, by + y + 200), a=.30 + .1 * i)
        st = [[C['mint'], C['cyan']], [C['cyan'], C['polar']], [C['polar'], C['cyan']]][i]
        im.paste(grad(170 + 40 * i, 14, st), (bx + x + 36, by + y + 50), rmask(170 + 40 * i, 14, 7))
        d = ImageDraw.Draw(im)
        d.rounded_rectangle((bx + x + 36, by + y + 90, bx + x + 260, by + y + 100), radius=5, fill='#D6E7F4')
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


def quote_mark(im, x, y, size=380, stops=(C['polar'], C['cyan'])):
    q = Image.new('L', (int(size * .8), int(size * .7)), 0)
    ImageDraw.Draw(q).text((0, -int(size * .13)), '“', fill=255, font=font(size, serif=True))
    im.paste(grad(q.width, q.height, list(stops), 'd'), (x, y), q)


def list_rows(im, x, y, items, w=912):
    for i, t in enumerate(items):
        top = y + i * 150
        glass(im, (x, top, x + w, top + 124), r=30, a=.55)
        im.paste(grad(76, 76, HL, 'd'), (x + 26, top + 24), rmask(76, 76, 38))
        d = ImageDraw.Draw(im)
        d.text((x + 50, top + 38), str(i + 1), fill=C['white'], font=font(36))
        d.text((x + 130, top + 40), t, fill=C['abyss'], font=font(40))


def page_counter(im, n, total):
    d = ImageDraw.Draw(im); txt = f'{n:02d} / {total:02d}'
    d.text((PW - SX - d.textbbox((0, 0), txt, font=font(26))[2], SY + 8), txt, fill=C['steel'], font=font(26))


def dots(im, n, total, y=PH - SY + 4):
    d = ImageDraw.Draw(im); x = PW - SX - total * 26
    for i in range(total):
        if i == n - 1:
            im.paste(grad(40, 12, HL), (x - 14, y), rmask(40, 12, 6)); x += 30
        else:
            d.ellipse((x, y, x + 12, y + 12), fill='#B9CDE0'); x += 26


def photo_frame(im, box):
    x0, y0, x1, y1 = box; w, h = x1 - x0, y1 - y0
    ph = grad(w, h, ['#C9D9E8', '#AFC6DB'], 'd'); d = ImageDraw.Draw(ph)
    d.ellipse((w // 2 - 90, h // 2 - 170, w // 2 + 90, h // 2 + 10), fill='#93AFC9')
    d.rounded_rectangle((w // 2 - 180, h // 2 + 40, w // 2 + 180, h + 60), radius=120, fill='#93AFC9')
    d.text((24, h - 50), 'real photo · news inbox', fill='#F4F9FC', font=font(22, bold=False))
    im.paste(ph, (x0, y0), rmask(w, h, 36))
    ImageDraw.Draw(im).rounded_rectangle(box, radius=36, outline=(255, 255, 255), width=8)


# ---------- templates ----------
def t_hero():
    im = ground(); logo(im); pill(im, SX, 206, 'Built to scale')
    y = headline(im, 80, 292, [[('Built for the', 0)], [('next stage', 1)], [('of growth', 0)]])
    accent(im, SX + 4, y + 8); sub(im, SX, y + 36, 'Software that scales with your business.')
    block(im, (500, 760, 1140, 1410)); bars(im, 500, 760); footer(im); return im


def t_glass():
    im = ground(); logo(im); pill(im, SX, 206, 'Outsourcing, Decoded')
    y = headline(im, 80, 292, [[('You pay at', 0)], [('milestones', 1)], [('you can see', 0)]])
    accent(im, SX + 4, y + 8); sub(im, SX, y + 36, 'At kickoff, at key phases, at final delivery.')
    block(im, (430, 770, 1130, 1410)); glass_stack(im, 430, 770); footer(im); return im


def t_quote():
    im = ground(); block(im, (600, -60, 1200, 420), glow_at=(.33, .33, 1.17, 1.17)); quote_mark(im, 770, 90)
    logo(im); pill(im, SX, 206, 'Client words')
    f = font(64); y = 500; d = ImageDraw.Draw(im); d.text((SX, y), 'They', fill=C['abyss'], font=f)
    gtext(im, (SX + d.textbbox((0, 0), 'They ', font=f)[2], y), 'quickly', f)
    for i, l in enumerate(['understood our problem,', 'collaborated effectively', 'with our team, and', 'delivered a solid', 'solution.']):
        ImageDraw.Draw(im).text((SX, y + 80 * (i + 1)), l, fill=C['abyss'], font=f)
    accent(im, SX + 4, y + 80 * 6 + 24, 90)
    ImageDraw.Draw(im).text((SX, y + 80 * 6 + 54), 'Isana Sebastian', fill=C['steel'], font=font(34))
    footer(im); return im


def t_list():
    im = ground(); block(im, (-60, 1120, 1140, 1420), radius=56, glow_at=(.45, .1, 1.2, 1.6))
    logo(im); pill(im, SX, 206, 'Wireframe → Production')
    y = headline(im, 80, 292, [[('Before the first', 0)], [('line of code', 1)]], size=92)
    accent(im, SX + 4, y + 8); sub(im, SX, y + 36, 'Our UI/UX process starts here.')
    list_rows(im, SX, 640, ['Research & discovery', 'User personas', 'Architecture & wireframing'])
    d = ImageDraw.Draw(im); d.text((SX, PH - SY - 4), 'verdant-soft.com', fill=C['white'], font=font(24)); return im


def t_cover():
    im = ground(); logo(im); pill(im, SX, 206, 'Outsourcing, Decoded · 03')
    y = headline(im, 80, 292, [[('Can I hire you', 0)], [('for just one', 0)], [('service?', 1)]], size=96)
    accent(im, SX + 4, y + 8); sub(im, SX, y + 36, 'Swipe for the short answer.')
    block(im, (560, 820, 1140, 1410)); network(im, 860, 1060)
    footer(im); dots(im, 1, 5); return im


def t_slide():
    im = ground(); logo(im); page_counter(im, 2, 5)
    y = headline(im, 80, 250, [[('Yes. ', 0), ('Pick one.', 1)]], size=88)
    sub(im, SX, y + 10, 'Each service works on its own or together.')
    block(im, (SX, 520, PW - SX, 1130), radius=40, glow_at=(.5, .4, 1.3, 1.4))
    for i, s in enumerate(['Custom Software Development', 'Cloud & DevOps', 'IT Team Outsourcing', 'UI/UX Design']):
        top = 580 + i * 130; glass(im, (SX + 50, top, PW - SX - 50, top + 100), r=50, a=.18)
        d = ImageDraw.Draw(im); d.ellipse((SX + 80, top + 36, SX + 108, top + 64), fill=C['cyan'])
        d.text((SX + 136, top + 26), s, fill=C['white'], font=font(38))
    footer(im); dots(im, 2, 5); return im


def t_people():
    im = ground(); block(im, (480, 560, 1140, 1410), glow_at=(.2, .5, 1.1, 1.3)); photo_frame(im, (560, 640, 1000, 1180))
    logo(im); pill(im, SX, 206, 'Grow with us')
    y = headline(im, 80, 292, [[('Welcome', 0)], [('to the team', 1)]], size=100)
    accent(im, SX + 4, y + 8)
    d = ImageDraw.Draw(im); d.text((SX, y + 40), '[Name]', fill=C['abyss'], font=font(40))
    d.text((SX, y + 92), '[Role]', fill=C['steel'], font=font(30, bold=False))
    footer(im); return im


TEMPLATES = [('L-HERO', 'Hero in block', 'How we work · Brand world', t_hero),
             ('L-GLASS', 'Glass in block', 'How we work', t_glass),
             ('L-QUOTE', 'Client words', 'Proof', t_quote),
             ('L-LIST', 'Steps list', 'How we work · Insight', t_list),
             ('L-COVER', 'Carousel cover', 'Series, v2 carousels', t_cover),
             ('L-SLIDE', 'Carousel slide', 'Series, v2 carousels', t_slide),
             ('L-PEOPLE', 'People', 'Grow with us (inbox photo)', t_people)]


def sheet_templates():
    renders = [(tid, name, use, fn()) for tid, name, use, fn in TEMPLATES]
    W = 1600; s = .30; pw, ph = int(PW * s), int(PH * s); gap = (W - 160 - 4 * pw) // 3
    page = Image.new('RGB', (W, 170 + 2 * (ph + 120) + 40), '#EEF4F9'); d = ImageDraw.Draw(page)
    d.text((80, 40), 'Verdant Soft · light theme v2 · templates', fill=C['abyss'], font=font(34))
    d.text((80, 92), 'One grid, one component kit, seven layouts. Every post uses exactly one colour block.', fill=C['steel'], font=font(20, bold=False))
    cells = renders + [None]
    for i, cell in enumerate(cells):
        col, row = i % 4, i // 4; x = 80 + col * (pw + gap); y = 150 + row * (ph + 120)
        if cell is None:
            for j, (k, c) in enumerate([('Abyss', 'abyss'), ('Royal', 'royal'), ('Ocean', 'ocean'), ('Cyan', 'cyan'), ('Mint', 'mint'), ('Polar', 'polar')]):
                yy = y + j * (ph // 6)
                d.rounded_rectangle((x, yy, x + pw, yy + ph // 6 - 8), radius=12, fill=C[c], outline='#C9D6E2')
                d.text((x + 16, yy + 14), f'{k} {C[c]}', fill=C['white'] if c in ('abyss', 'royal', 'ocean') else C['abyss'], font=font(18))
            d.text((x, y + ph + 16), 'Theme colours', fill=C['steel'], font=font(20)); continue
        tid, name, use, im = cell
        sh = Image.new('L', page.size, 0)
        ImageDraw.Draw(sh).rounded_rectangle((x + 5, y + 12, x + pw + 5, y + ph + 12), radius=18, fill=80)
        page.paste(Image.new('RGB', page.size, rgb('#9DB4CC')), (0, 0), sh.filter(ImageFilter.GaussianBlur(12)))
        page.paste(im.resize((pw, ph), Image.LANCZOS), (x, y), rmask(pw, ph, 16))
        d = ImageDraw.Draw(page)
        d.text((x, y + ph + 14), f'{tid} · {name}', fill=C['abyss'], font=font(19))
        d.text((x, y + ph + 42), use, fill=C['steel'], font=font(17, bold=False))
    page.save(f'{OUT}/light-2-templates.png', optimize=True)
    return renders


def sheet_anatomy(hero):
    W = 1600; s = .56; pw, ph = int(PW * s), int(PH * s)
    page = Image.new('RGB', (W, ph + 220), '#EEF4F9'); d = ImageDraw.Draw(page)
    d.text((80, 40), 'Verdant Soft · light theme v2 · anatomy', fill=C['abyss'], font=font(34))
    d.text((80, 92), 'Grid at 1080 × 1350. Sides 84 px, top and bottom 110 px. Text block top-left, colour block lower-right.', fill=C['steel'], font=font(20, bold=False))
    x0, y0 = 80, 150
    page.paste(hero.resize((pw, ph), Image.LANCZOS), (x0, y0), rmask(pw, ph, 16))
    ov = Image.new('RGBA', page.size, (0, 0, 0, 0)); od = ImageDraw.Draw(ov)
    m = lambda v: int(v * s)
    od.rectangle((x0 + m(SX), y0 + m(SY), x0 + m(PW - SX), y0 + m(PH - SY)), outline=(232, 62, 140, 200), width=2)
    page.paste(ov, (0, 0), ov); d = ImageDraw.Draw(page)
    notes = [(SY + 26, '1  Logo · real file, 52 px tall'), (235, '2  Label pill · gradient royal → ocean, white 26 px'),
             (350, '3  Headline · 100 px bold, abyss #050816'), (440, '    highlight words · gradient #2F62C8 → #0088AA'),
             (640, '4  Accent bar · 110 × 10, royal → cyan'), (690, '5  Subline · 32 px regular, steel #42658A'),
             (1000, '6  Colour block · cobalt → royal + cyan glow, r 44'),
             (PH - SY + 8, '7  Footer · verdant-soft.com, 24 px, steel')]
    tx = x0 + pw + 50
    for yy, txt in notes:
        py = y0 + m(yy)
        d.line((x0 + pw - 6, py, tx - 10, py), fill='#E83E8C', width=2); d.ellipse((x0 + pw - 12, py - 6, x0 + pw, py + 6), fill='#E83E8C')
        d.text((tx, py - 13), txt, fill=C['abyss'], font=font(21))
    d.text((tx, y0 + ph - 10), 'Pink frame = safe area: logo and text never cross it.', fill=C['steel'], font=font(18, bold=False))
    page.save(f'{OUT}/light-1-anatomy.png', optimize=True)


def sheet_rules():
    W = 1600; page = Image.new('RGB', (W, 1060), '#EEF4F9'); d = ImageDraw.Draw(page)
    d.text((80, 40), 'Verdant Soft · light theme v2 · rules', fill=C['abyss'], font=font(34))
    do = ['Tinted ice ground, never flat white', 'Exactly one saturated colour block per post',
          'One hero object, inside the block', '1–3 highlight words, gradient royal → ocean',
          'Headline 88–100 px, max 3 lines, sentence case', 'Label pill names the series or topic',
          'Glass only on or near the block, never stacked > 3', 'Real people only from real photos (inbox)']
    dont = ['Cyan, mint, sage or polar as text on light', 'Two colour blocks, or a block with no job',
            'Gradient text in body copy or subline', 'Centred headline over the hero',
            'Stock people, robots, generic tech icons', 'Yellow, lime, orange, coral, or green as brand',
            'Text inside the block smaller than 36 px', 'Busy effects: bokeh, sparkles, lens flares']
    for col, (title, items, c) in enumerate([('Do', do, C['royal_deep']), ("Don't", dont, '#B4234A')]):
        x = 80 + col * 740
        d.rounded_rectangle((x, 120, x + 700, 1000), radius=28, fill='#FFFFFF', outline='#D6E2EC', width=2)
        d.text((x + 36, 150), title, fill=c, font=font(34))
        for i, t in enumerate(items):
            yy = 230 + i * 92
            d.ellipse((x + 36, yy + 6, x + 60, yy + 30), fill=c)
            d.text((x + 80, yy), t, fill=C['abyss'], font=font(23, bold=False))
    page.save(f'{OUT}/light-3-rules.png', optimize=True)


if __name__ == '__main__':
    renders = sheet_templates()
    sheet_anatomy(renders[0][3])
    sheet_rules()
    print('rendered', [r[0] for r in renders])

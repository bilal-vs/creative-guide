"""Check writing packs against STYLE_GUIDE.md caption rules.

Usage: python3 tools/check_packs.py writing/round-02-lane-packs.md
Reads every ```yaml block preceded by <!-- pack: ID --> and checks lengths, emoji, hashtags,
banned words, numbers and headline limits. Rules are read from STYLE_GUIDE.md where they are
machine-readable (HASHTAGS-v1, BANNED-WORDS-v1, CAROUSEL-v2).
"""
import re, sys, yaml, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
GUIDE = (ROOT / 'STYLE_GUIDE.md').read_text()


def block(block_id):
    m = re.search(r'<!-- id: %s -->\n```yaml\n(.*?)```' % re.escape(block_id), GUIDE, re.S)
    return yaml.safe_load(m.group(1))


def block_or_none(block_id):
    try:
        return block(block_id)
    except AttributeError:
        return None


ON_IMAGE = block_or_none('ON-IMAGE-v1') or {}
OI_LIMITS = ON_IMAGE.get('hard_limits', {})
VS = block_or_none('VISUAL-SYSTEM-v1') or {}
FAMILY_LAYOUT_OVERRIDE = {'grow-with-us': 'STACK'}


def layout_for(p):
    """Layout of a single post from the VISUAL-SYSTEM-v1 day map (STACK labels are checked per line)."""
    if p.get('lane') in FAMILY_LAYOUT_OVERRIDE:
        return FAMILY_LAYOUT_OVERRIDE[p['lane']]
    day = str(p.get('day', '')).split('-')[0]
    return (VS.get('day_map', {}).get(day) or {}).get('layout')


HASHTAGS = block('HASHTAGS-v1')
BANNED = block('BANNED-WORDS-v1')
CAROUSEL = block('CAROUSEL-v2')
LIMITS = {s['role']: s for s in CAROUSEL['slides']}
EMOJI = re.compile('[\U0001F300-\U0001FAFF☀-➿\U0001F000-\U0001F2FF]')


def words(text):
    return [w for w in re.split(r'\s+', text.strip()) if w and not w.startswith('#') and re.search(r'\w', w)]


def caption_body(text):
    return '\n'.join(l for l in text.splitlines() if not l.strip().startswith('#'))


def tags(text):
    return re.findall(r'#\w+', text)


def strip_hl(s):
    return s.replace('[', '').replace(']', '')


def check_banned(label, text, errs):
    low = text.lower()
    for w in BANNED['words']:
        if re.search(r'\b%s\w*' % re.escape(w.lower()), low):
            errs.append(f'{label}: banned word "{w}"')
    for p in BANNED['phrases']:
        if p.lower() in low:
            errs.append(f'{label}: banned phrase "{p}"')
    if text.count('!') > BANNED['punctuation']['exclamation_marks_max']:
        errs.append(f'{label}: too many exclamation marks')


def numbers_in(text):
    return re.findall(r'\$?\d[\d,.]*%?', text)


def check_headline(label, hl, errs, max_words=8, quote=False):
    n = len(words(strip_hl(hl)))
    if not quote and n > max_words:
        errs.append(f'{label}: headline {n} words > {max_words}')
    hls = re.findall(r'\[([^\]]+)\]', hl)
    if len(hls) != 1:
        errs.append(f'{label}: needs exactly one [highlight], found {len(hls)}')
    elif not 1 <= len(hls[0].split()) <= 3:
        errs.append(f'{label}: highlight must be 1-3 words')


def check_pack(p):
    errs, warns = [], []
    pid, lane = p['id'], p['lane']
    li, ig = p['linkedin'], p['instagram']
    nli, nig = len(words(caption_body(li))), len(words(caption_body(ig)))
    if not 120 <= nli <= 220: errs.append(f'LinkedIn {nli} words (120-220)')
    if not 40 <= nig <= 100: errs.append(f'Instagram {nig} words (40-100)')
    if EMOJI.search(li): errs.append('LinkedIn has emoji')
    ig_emoji = EMOJI.findall(ig)
    if len(ig_emoji) > 2: errs.append('Instagram > 2 emoji')
    if ig.strip() and EMOJI.match(ig.strip()): errs.append('Instagram starts with emoji')
    for l in ig.splitlines():
        if EMOJI.match(l.strip()): errs.append('Instagram emoji used as a bullet/line start')
    want = HASHTAGS[lane]
    if tags(li) != want['linkedin']: errs.append(f'LinkedIn hashtags {tags(li)} != {want["linkedin"]}')
    igt = tags(ig)
    if len(igt) != 5 or igt[:4] != want['instagram'][:4]: errs.append(f'Instagram hashtags {igt} != {want["instagram"]}')
    for lab, t in (('LinkedIn', li), ('Instagram', ig)):
        check_banned(lab, t, errs)
        if re.search(r'\bI\b', t.replace('"I don', '').replace("'I don", '')): errs.append(f'{lab}: uses "I"')
    external = lane in ('trends', 'ai', 'startup', 'numbers', 'concepts')
    if external and 'Our take:' not in li: errs.append('LinkedIn missing "Our take:"')
    if external and 'Our take' not in ig: errs.append('Instagram missing "Our take"')
    direct = 'Book a call' in li or 'Book a call' in ig
    if direct and lane not in ('how-we-work', 'proof'): errs.append('direct CTA outside how-we-work/proof')
    if p['cta'] == 'direct' and not direct: errs.append('cta: direct but no "Book a call"')
    endq = '?' in caption_body(li).strip().splitlines()[-1] if caption_body(li).strip() else False
    # numbers must trace to sources
    allnums = numbers_in(li + ' ' + ig + ' ' + yaml.safe_dump(p.get('on_image', '')) + yaml.safe_dump(p.get('slides', '')))
    allnums = [n for n in allnums if not re.fullmatch(r'0?\d', n.rstrip('.,'))]  # step counters 1-9 allowed
    if allnums and not p.get('sources'):
        errs.append(f'numbers {sorted(set(allnums))} with no sources')
    elif allnums:
        warns.append(f'numbers to trace by hand against {p["sources"]}: {sorted(set(allnums))}')
    # on-image
    if p['format'] == 'single':
        oi = p['on_image']
        check_headline('headline', oi['headline'], errs, quote=(p['headline_formula'] == 'quote'))
        smax = OI_LIMITS.get('subline_words_max', 12)
        if oi.get('subline') and len(words(oi['subline'])) > smax and p['headline_formula'] != 'quote':
            errs.append(f'subline > {smax} words')
        if lane == 'numbers' and not oi.get('source_line'): errs.append('numbers post without source line')
        info = oi.get('info') or {}
        items = [x for x in (info.get('items') or []) if str(x).strip()]
        if OI_LIMITS:
            exempt = lane in ('proof', 'numbers')
            if not exempt:
                lo, hi = OI_LIMITS.get('info_items_min', 2), OI_LIMITS.get('info_items_max', 4)
                if not lo <= len(items) <= hi:
                    errs.append(f'needs {lo}-{hi} diagram labels (ON-IMAGE-v1), has {len(items)}')
            wmax = OI_LIMITS.get('words_per_item_max')
            layout = layout_for(p)
            caps = OI_LIMITS.get('label_characters_max', {})
            for it in items:
                if wmax and len(words(it)) > wmax: errs.append(f'label over {wmax} words: "{it}"')
                if layout == 'STACK':
                    head, _, tail = str(it).partition(':')
                    for part in ([head + ':', tail.strip()] if tail else [head]):
                        if len(part) > caps.get('STACK_per_line', 20):
                            errs.append(f'STACK label line over {caps.get("STACK_per_line", 20)} characters: "{part}"')
                elif layout in caps and len(str(it)) > caps[layout]:
                    errs.append(f'label over {caps[layout]} characters for {layout}: "{it}"')
            strings = 2 + bool((oi.get('subline') or '').strip()) + len(items) + bool((oi.get('source_line') or '').strip()) + 1
            smax = OI_LIMITS.get('strings_max', 8)
            if strings > smax: errs.append(f'{strings} on-image strings > {smax}')
            total = sum(len(words(strip_hl(str(oi.get(k) or '')))) for k in ('pill', 'headline', 'subline', 'source_line'))
            total += sum(len(words(str(x))) for x in items) + 1  # + the URL
            tw = OI_LIMITS.get('image_total_words_max')
            if tw and total > tw and lane != 'proof': errs.append(f'image text {total} words > {tw}')
            if lane == 'proof' and len(words(strip_hl(oi.get('headline', '')))) > 25: errs.append('proof quote over 25 words')
            for v in [oi.get('pill'), oi.get('headline'), oi.get('subline'), oi.get('source_line')] + items:
                if v and re.search('[\u00b7\u2192\u2013\u2014\u2026\u201c\u201d\u2018\u2019]', str(v)):
                    errs.append(f'non-keyboard character on the image: "{v}"')
            warns.append(f'image: {strings} strings, {total} words')
    else:
        slides = p['slides']
        if not 6 <= len(slides) <= 8: errs.append(f'{len(slides)} slides (6-8)')
        order = [s['role'] for s in slides]
        if order[0] != 'cover' or order[-1] != 'receipt': errs.append(f'bad order {order}')
        for s in slides:
            lab = f'slide {s["n"]} ({s["role"]})'
            lim = LIMITS.get(s['role'], {})
            if s.get('headline'):
                check_headline(lab, s['headline'], errs, lim.get('headline_max_words', 8))
            if s.get('body') and lim.get('body_max_words') and len(words(s['body'])) > lim['body_max_words']:
                errs.append(f'{lab}: body {len(words(s["body"]))} words > {lim["body_max_words"]}')
            if s['role'] == 'step' and not s.get('bridge'): errs.append(f'{lab}: missing bridge')
            if s.get('bridge') and len(words(s['bridge'])) > lim.get('bridge_max_words', 8): errs.append(f'{lab}: bridge too long')
            if s['role'] == 'item' and not s.get('source_line'): errs.append(f'{lab}: item without source line')
            if s['role'] == 'receipt' and len(s.get('list', [])) > 6: errs.append(f'{lab}: receipt > 6 items')
            check_banned(lab, yaml.safe_dump(s), errs)
        if len(p['alt_text']) != len(slides): errs.append('alt text count != slide count')
    if 'PENDING' in yaml.safe_dump(p): warns.append('contains PENDING-CHECK items: practice only, not publishable')
    return nli, nig, errs, warns


def main(path):
    text = pathlib.Path(path).read_text()
    packs = [yaml.safe_load(b) for b in re.findall(r'<!-- pack: \w+ -->\n```yaml\n(.*?)```', text, re.S)]
    fails = 0
    qs = 0
    for p in packs:
        nli, nig, errs, warns = check_pack(p)
        qs += bool(p.get('question'))
        status = 'PASS' if not errs else 'FAIL'
        fails += bool(errs)
        print(f"{p['id']:3} {p['lane']:13} LI {nli:3} IG {nig:3}  {status}")
        for e in errs: print('     x', e)
        for w in warns: print('     !', w)
    print(f'{len(packs)} packs, {fails} failing, questions {qs}/{len(packs)}')
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))

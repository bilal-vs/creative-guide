"""Lint a Flow / Nano Banana 2 prompt against STYLE_GUIDE.md §6 text-rendering rules.

Usage: python3 tools/lint_prompt.py <file-with-prompt> [--kind single|proof|numbers|inner|receipt]
The prompt is the content of the first ```text block in the file, or the whole file.
"""
import re, sys, pathlib

WORDS = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10}
CAPS = {'single': 8, 'proof': 8, 'numbers': 8, 'inner': 6, 'receipt': 10}
BAD_CHARS = '→·–—…“”‘’'
BANNED = ['pixel-perfect', 'exact replica', 'recreate', 'green', 'lime']


def main(path, kind='single'):
    text = pathlib.Path(path).read_text()
    m = re.search(r'```text\n(.*?)```', text, re.S)
    prompt = (m.group(1) if m else text).strip()
    errs, info = [], []
    quoted = re.findall(r'"([^"]*)"', prompt)
    if prompt.count('"') % 2: errs.append('odd number of double quotes')
    n = len(quoted)
    cm = re.search(r'exactly (\w+) pieces of text', prompt)
    if not cm: errs.append('missing count sentence ("exactly N pieces of text")')
    else:
        want = WORDS.get(cm.group(1).lower())
        if want != n: errs.append(f'count sentence says {cm.group(1)} but {n} strings are quoted')
    if n > CAPS[kind]: errs.append(f'{n} quoted strings > cap {CAPS[kind]} for {kind}')
    if len(set(quoted)) != n: errs.append('a string is quoted twice')
    total = sum(len(q.split()) for q in quoted)
    info.append(f'{n} strings, {total} words in quotes')
    if kind == 'single' and total > 35: errs.append(f'{total} words on image > 35')
    for q in quoted:
        if any(c in q for c in BAD_CHARS): errs.append(f'non-keyboard character in "{q}"')
        if re.search(r'#[0-9A-Fa-f]{3,6}\b', q): errs.append(f'hex code inside quotes: "{q}"')
        if 'Verdant Soft' in q: errs.append('"Verdant Soft" must never be a quoted string')
        if re.search(r'[\U0001F300-\U0001FAFF]', q): errs.append(f'emoji in "{q}"')
    low = prompt.lower()
    for b in BANNED:
        if re.search(r'\b%s\b' % re.escape(b), low): errs.append(f'banned prompt word "{b}"')
    if not prompt.endswith('Portrait image, 3:4 aspect ratio.'): errs.append('must end with "Portrait image, 3:4 aspect ratio."')
    if 'attached image' not in low: errs.append('no logo reference instruction')
    print(f'{path}: {"PASS" if not errs else "FAIL"} · ' + '; '.join(info))
    for e in errs: print('  x', e)
    for q in quoted: print('   ·', q)
    return 1 if errs else 0


if __name__ == '__main__':
    kind = 'single'
    if '--kind' in sys.argv: kind = sys.argv[sys.argv.index('--kind') + 1]
    sys.exit(main(sys.argv[1], kind))

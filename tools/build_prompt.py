"""Assemble a Flow / Nano Banana 2 prompt for one post from STYLE_GUIDE.md blocks.

Usage:
  python3 tools/build_prompt.py <packs-file.md> <pack-id> [--cover N]

Reads VISUAL-SYSTEM-v1 (day map, moods, layouts, diagram families, text lines),
PROMPT-RULES-v1 (series purposes) and STYLE-BLOCK-v1 from STYLE_GUIDE.md, and the pack
(YAML after <!-- pack: ID -->) from the packs file. The pack supplies the strings:
day, lane, series, on_image {pill, headline, subline, info.items, source_line}, and
visual {post_job, config}. Carousel packs use their first slide plus visual.cover_labels.
--cover N writes the prompt as the cover of an N-slide carousel (adds the cover suffix);
without it the post is a single image post.
Prints the prompt. The pipeline never picks a mood, layout or family freely (§6).
"""
import re
import sys
import pathlib
import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
GUIDE = (ROOT / 'STYLE_GUIDE.md').read_text()

WORD = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}
ORD = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth',
       'eleventh', 'twelfth', 'thirteenth', 'fourteenth', 'fifteenth', 'sixteenth', 'seventeenth',
       'eighteenth', 'nineteenth', 'twentieth', 'twenty-first', 'twenty-second', 'twenty-third',
       'twenty-fourth', 'twenty-fifth']
MAX_LINES = {'BAND': 'three', 'WINDOW': 'three', 'COLUMN': 'four', 'SLIDE': 'two', 'CORNER': 'two'}
FAMILY_BY_LANE = {'how-we-work': 'RAIL', 'build-notes': 'MATRIX', 'proof': 'QUOTE-MARK', 'grow-with-us': 'STACK',
                  'startup': 'TREE', 'numbers': 'FIGURE-BAR', 'concepts': 'CUTAWAY', 'ai': 'FAN', 'trends': 'SIGNAL-BOARD'}
OPENER = ('Create an image: a finished, ready-to-publish social media post for Instagram and LinkedIn, designed by a '
          'senior brand design team for Verdant Soft, a B2B software company that designs and builds custom software '
          'for international clients. It is {format_phrase} in a recurring series that {series_purpose}, and this '
          '{post_noun} {post_job}.')


def yaml_block(block_id):
    m = re.search(r'<!-- id: %s -->\n```yaml\n(.*?)```' % re.escape(block_id), GUIDE, re.S)
    return yaml.safe_load(m.group(1))


def text_block(block_id):
    m = re.search(r'<!-- id: %s -->\n```text\n(.*?)```' % re.escape(block_id), GUIDE, re.S)
    return m.group(1).strip()


VS = yaml_block('VISUAL-SYSTEM-v1')
RULES = yaml_block('PROMPT-RULES-v1')
STYLE = text_block('STYLE-BLOCK-v1')


def series_purposes():
    entry = next(s for s in RULES['slot_rules'] if s.startswith('{series_purpose}'))
    return dict(re.findall(r"- (.+?): '(.+?)'", entry))


def load_pack(path, pack_id):
    text = pathlib.Path(path).read_text()
    m = re.search(r'<!-- pack: %s -->\n```yaml\n(.*?)```' % re.escape(pack_id), text, re.S)
    if not m:
        sys.exit(f'pack {pack_id} not found in {path}')
    return yaml.safe_load(m.group(1))


def highlight_phrase(headline):
    """Name the [highlight] span by position, e.g. 'final three words' or 'third, fourth and fifth words'."""
    words = headline.split()
    start = next(i for i, w in enumerate(words) if w.startswith('['))
    end = next(i for i, w in enumerate(words) if ']' in w)
    k = end - start + 1
    if end == len(words) - 1:
        return 'final word' if k == 1 else f'final {WORD[k]} words'
    names = ORD[start:end + 1]
    if k == 1:
        return f'{names[0]} word'
    return (', '.join(names[:-1]) + ' and ' + names[-1]) + ' words'


def strip_hl(s):
    return s.replace('[', '').replace(']', '')


def build(pack, cover_slides=None):
    day = pack['day'].split('-')[0]
    lane = pack['lane']
    entry = VS['day_map'][day]
    mood_key, layout_key = entry['mood'], entry['layout']
    visual = pack.get('visual') or {}
    config = visual.get('config') or {}
    family_key = config.get('family') or FAMILY_BY_LANE[lane]
    if lane == 'proof' and pack.get('series') == 'Project Spotlight':
        family_key = config.get('family', 'MODULE-MAP')

    mood = VS['moods'][mood_key]
    slots = mood['slots']
    layout = VS['layouts'][layout_key]
    family = VS['diagram']['families'][family_key]
    text_lines = VS['text_lines']

    if pack['format'] == 'carousel':
        first = pack['slides'][0]
        oi = {'pill': first.get('pill'), 'headline': first['headline'], 'subline': first.get('body'),
              'info': {'items': visual.get('cover_labels') or []}, 'source_line': first.get('source_line') or ''}
    else:
        oi = pack['on_image']
    labels = list((oi.get('info') or {}).get('items') or [])
    source_line = (oi.get('source_line') or '').strip()

    # roles
    is_quote = family_key == 'QUOTE-MARK'
    is_figure = family_key.startswith('FIGURE')
    lead_role = "client's quote" if is_quote else ('figure' if is_figure else 'headline')
    second_role = 'attribution' if is_quote else ('name and role' if family_key == 'FRAME' else 'subline')
    visual_noun = 'quotation mark' if is_quote else ('picture frame' if family_key == 'FRAME' else 'diagram')

    # layout block
    block = layout['prompt_block']
    if '{footer_clause}' in block:
        clause = layout['footer_clause']['with_source' if source_line and 'with_source' in layout['footer_clause'] else 'plain']
        if cover_slides:
            clause = clause + ' ' + layout['footer_clause']['cover_suffix']
        block = block.replace('{footer_clause}', clause)
    block = (block.replace('{visual_noun}', visual_noun).replace('{lead_role}', lead_role)
             .replace('{second_role}', second_role).replace('{support}', slots['support']))

    # diagram block
    diagram = family['prompt_block'].replace('{n_word}', WORD.get(len(labels), ''))
    if family_key == 'RAIL':
        diagram = diagram.replace('{middle_phrase}', family['middle_phrase'][str(len(labels))])
    if family_key == 'MATRIX':
        diagram = diagram.replace('{ordinal}', config.get('ordinal', 'second'))
    if family_key == 'FIGURE-BAR':
        figure = strip_hl(oi['headline']).rstrip('%')
        diagram = diagram.replace('{fill_words}', config.get('fill_words') or family['fill_words_examples'][figure])
    if family_key == 'FAN':
        diagram = diagram.replace('{modifier_sentence}', family['modifiers'][config.get('modifier', 'none')])
        diagram = re.sub(r'  +', ' ', diagram)

    # text lines
    lines = []
    pill = text_lines['PILL'].replace('{pill_position}', text_lines['pill_position'][layout_key])
    pill = pill.replace('{pill_fill}', slots['pill_fill']).replace('{pill}', oi['pill']).replace('{pill_text}', slots['pill_text'])
    lines.append(pill)
    if is_figure:
        lines.append(text_lines['LEAD_figure'].replace('{figure}', strip_hl(oi['headline'])).replace('{highlight}', slots['highlight']))
    else:
        hp = highlight_phrase(oi['headline'])
        key = 'LEAD_quote' if is_quote else 'LEAD_headline'
        lead = text_lines[key].replace('{quote}', strip_hl(oi['headline'])).replace('{headline}', strip_hl(oi['headline']))
        lead = lead.replace('{ink}', slots['ink']).replace('{max_lines}', MAX_LINES[layout_key]).replace('{highlight}', slots['highlight'])
        if hp == 'final word':
            lead = lead.replace('the {highlight_position} stay together on one line and are filled with',
                                'the final word stays on its line and is filled with')
        lead = lead.replace('{highlight_position}', hp)
        lines.append(lead)
    lines.append(text_lines['ACCENT'].replace('{lead_role}', lead_role))
    second = (oi.get('subline') or '').strip()
    if second:
        if is_quote:
            lines.append(text_lines['ATTRIBUTION'].replace('{attribution}', second).replace('{support}', slots['support']))
        elif is_figure:
            lines.append(text_lines['CONTEXT'].replace('{context}', second).replace('{ink}', slots['ink']))
        else:
            lines.append(text_lines['SUBLINE'].replace('{subline}', second).replace('{support}', slots['support']))
    anchors = text_lines['label_anchors'].get(family_key, [])
    for i, label in enumerate(labels):
        lines.append(f'{anchors[i]}: "{label}"')
    if source_line:
        src = text_lines['SOURCE'].replace('"Source: {source_name}, {YYYY}"', f'"{source_line}"').replace('{support}', slots['support'])
        lines.append(src)
    lines.append(text_lines['URL'].replace('{support}', slots['support']))
    n = sum(line.count('"') // 2 for line in lines)
    count = text_lines['COUNT'].replace('{n_strings_word}', WORD[n])
    logo = text_lines['LOGO'].replace('{logo_colours}', slots['logo_colours'])

    purposes = series_purposes()
    if cover_slides:
        format_phrase, post_noun = f'the cover of a {WORD.get(cover_slides, str(cover_slides))}-slide carousel', 'cover'
    else:
        format_phrase, post_noun = 'a single image post', 'post'
    opener = OPENER.format(format_phrase=format_phrase, series_purpose=purposes[pack['series']],
                           post_noun=post_noun, post_job=visual['post_job'])
    prompt = (f'{opener}\n\nLayout: {block}\n\n{mood["prompt_block"]}\n\n'
              f'On the plate, {diagram} The plate, the drawing and the glass piece carry no other words.\n\n'
              'Text, each piece exactly as written between the double quotes:\n'
              + '\n'.join('- ' + line for line in lines) + '\n' + count + '\n\n' + logo + '\n\n' + STYLE
              + '\n\nPortrait image, 3:4 aspect ratio.')
    return prompt, {'mood': mood_key, 'layout': layout_key, 'family': family_key, 'ref_pack': slots['ref_pack'], 'strings': n}


if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    cover = int(sys.argv[sys.argv.index('--cover') + 1]) if '--cover' in sys.argv else None
    prompt, info = build(load_pack(sys.argv[1], sys.argv[2]), cover)
    print(prompt)
    print(f'\n# {info}', file=sys.stderr)

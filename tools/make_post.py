"""Create a post file (posts/<date>-<slug>.md) and its ledger row from a pack.

Usage:
  python3 tools/make_post.py <packs-file.md> <pack-id> <date> <slug> [--cover N] [--training]

The prompt is assembled by tools/build_prompt.py from STYLE_GUIDE.md blocks, so the file
always matches the guide. --training marks the post as a visual-training run (no D-1
research, never published). Refuses to overwrite an existing post file: prompts that have
been sent are never edited (CLAUDE.md conventions); write a new version instead.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build_prompt import build, load_pack  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
REF = {'REF-PACK-v2-light': 'brand/ref-pack/ref-pack-v2-light.png', 'REF-PACK-v2-dark': 'brand/ref-pack/ref-pack-v2-dark.png'}


def main(packs_file, pack_id, date, slug, cover=None, training=False):
    pack = load_pack(packs_file, pack_id)
    prompt, info = build(pack, cover)
    out = ROOT / 'posts' / f'{date}-{slug}.md'
    if out.exists():
        sys.exit(f'{out} exists: never edit a sent prompt; add a new prompt version to that file instead')
    tpl = f"TPL-{pack['lane']}-v1"
    sources = ', '.join(pack.get('sources') or []) or 'none'
    config = f"{info['mood']} · {info['layout']} · {info['family']}"
    timely = next((x for x in (pack.get('sources') or []) if str(x).startswith('T-')), 'evergreen')
    fmt = f'cover of a {cover}-slide carousel, run as a single' if cover else pack['format']
    research = ('Not applicable: training post, never published.' if training else
                '_To do on the day before the post date (STYLE_GUIDE.md §1 step 0). Use the check table in posts/_template.md._')
    alt = pack.get('alt_text') or []
    alt_md = '\n'.join(f'- {a}' for a in alt)
    body = f"""---
date: {date}
pillar: {pack['lane']}
lane: {pack['lane']}
series: {pack['series']}
format: {fmt}
topic: {pack.get('topic', '')}
sources: [{sources}]
template: {tpl}
status: iterating
---

# {'Visual training' if training else 'Post'} · {pack_id} · {pack['series']}

## Brief
- **Configuration:** {config} ({info['strings']} on-image strings), from `VISUAL-SYSTEM-v1` → `day_map`.
- **Copy:** `{packs_file}` pack {pack_id}.
- **What the image must say in 3 seconds:** {pack.get('visual', {}).get('post_job', '')}.
- **Sources:** {sources}.

## Research (day before, D−1)
{research}

## Prompt v1
**Settings:** Google Flow · Images · Nano Banana 2 · aspect ratio `3:4` (crop to 4:5) · outputs `4` · one ingredient: `{REF[info['ref_pack']]}` · download the largest size · paste exactly as written.

```text
{prompt}
```

### Review v1
_Waiting for outputs._

## Captions
**LinkedIn**
```text
{pack['linkedin'].rstrip()}
```

**Instagram**
```text
{pack['instagram'].rstrip()}
```

**Alt text**
{alt_md}
"""
    out.write_text(body)
    row = (f"| {date} | [{date}-{slug}]({date}-{slug}.md) | {pack['lane']}{' (training)' if training else ''} | "
           f"{pack['lane']} · {pack['series']} | {fmt} | {timely} | {sources} | {pack_id} {pack.get('topic', '')} | "
           f"{config} | per {tpl} | — | {sources} | {tpl} | v1 | — | waiting |")
    ledger = ROOT / 'posts' / 'index.md'
    ledger.write_text(ledger.read_text().rstrip('\n') + '\n' + row + '\n')
    print(out.relative_to(ROOT), info)


if __name__ == '__main__':
    a = sys.argv
    if len(a) < 5:
        sys.exit(__doc__)
    cover = int(a[a.index('--cover') + 1]) if '--cover' in a else None
    main(a[1], a[2], a[3], a[4], cover, '--training' in a)

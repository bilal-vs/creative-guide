"""Verdant Soft colour system v8: one source of truth for the guidelines book and the post kit.

Two themes x two moods, chosen by content pillar. Every text pair here is contrast-checked in build.py.
"""

PALETTE = [
    ('Core · fixed', [('Slate Blue', '#416D95'), ('Sage Teal', '#74AFAD')]),
    ('Deep', [('Abyss', '#050816'), ('Navy', '#1E3058'), ('Cobalt Night', '#151754'), ('Teal Night', '#061A22')]),
    ('Blues', [('Electric Royal', '#2457D6'), ('Royal Blue', '#3C6EB7'), ('Steel Navy', '#42658A'), ('Sky', '#A6CAEC')]),
    ('Teals', [('Deep Lagoon', '#00727F'), ('Deep Ocean', '#007A9E'), ('Ocean', '#0088AA'), ('Lagoon', '#00ACB3'), ('Cyan', '#09CACC'), ('Mint Jade', '#34CCA4')]),
    ('Lights', [('Mist', '#F5F9FD'), ('Ice', '#EBF5F7'), ('Polar', '#E9FFFC'), ('White', '#FFFFFF')]),
]
NEW_IN_V8 = {'Electric Royal', 'Deep Lagoon', 'Deep Ocean', 'Teal Night', 'Mist'}

BRAND = ['#416D95', '#74AFAD']          # logo gradient; also the accent bar on every post

MOODS = {
    'light-royal': dict(
        name='Light Royal', theme='light', pillars='How we work (Tue, Sun) · Proof (Thu)',
        idea='Bright and confident. A luminous royal-blue mass on misty white.',
        ground=['#F5F9FD', '#E8F0F8', '#DAE6F2'], ground_glow=('#E9FFFC', 70, 'top-left'),
        surface=dict(fill='#FFFFFF', border='#C9DCEC', shadow=('#1E3058', 8, 8, 24)),
        raised=dict(fill='white 88% glass', border='#FFFFFF', shadow=('#1E3058', 16, 24, 60)),
        mass=['#2457D6', '#3C6EB7'], mass_name='Royal Tide', mass_glows=[('#09CACC', 40, 'centre-right'), ('#A6CAEC', 30, 'top edge sheen')],
        mass_shadow=('#2457D6', 28, 30, 70), mass_edge=None,
        headline='#050816', supporting='#42658A', meta='#42658A',
        highlight=['#2457D6', '#007A9E'], pill=['#2457D6', '#007A9E'], pill_text='#FFFFFF',
        lines='#C9DCEC', logo='gradient lockup', text_on_mass='#FFFFFF'),
    'light-lagoon': dict(
        name='Light Lagoon', theme='light', pillars='Grow with us (Fri)',
        idea='Fresh and human. A deep-lagoon mass on polar white.',
        ground=['#F2FAFA', '#E3F3F3', '#D2EBEC'], ground_glow=('#E9FFFC', 70, 'top-left'),
        surface=dict(fill='#FFFFFF', border='#BFDDE0', shadow=('#062A33', 8, 8, 24)),
        raised=dict(fill='white 88% glass', border='#FFFFFF', shadow=('#062A33', 14, 24, 60)),
        mass=['#00727F', '#0088AA', '#00ACB3'], mass_name='Lagoon Tide', mass_glows=[('#34CCA4', 35, 'centre'), ('#E9FFFC', 30, 'top edge sheen')],
        mass_shadow=('#00727F', 26, 30, 70), mass_edge=None,
        headline='#050816', supporting='#42658A', meta='#42658A',
        highlight=['#007A9E', '#00727F'], pill=['#00727F', '#007A9E'], pill_text='#FFFFFF',
        lines='#BFDDE0', logo='gradient lockup', text_on_mass='#FFFFFF'),
    'dark-royal': dict(
        name='Dark Royal', theme='dark', pillars='Engineering insight (Mon, Wed)',
        idea='Focused and technical. A royal aurora glowing out of the abyss.',
        ground=['#050816', '#0A1030', '#12164A'], ground_glow=('#21387B', 60, 'top-left'),
        surface=dict(fill='#0B1530', border='#1C2B4E', shadow=None),
        raised=dict(fill='white 8% glass', border='Polar 12% inner top edge', shadow=None),
        mass=['#0B1A3A', '#21387B', '#2457D6'], mass_name='Royal Aurora', mass_glows=[('#09CACC', 35, 'centre-right'), ('#3C6EB7', 40, 'top-right')],
        mass_shadow=None, mass_edge=('#E9FFFC', 25),
        headline='#FFFFFF', supporting='#A6CAEC', meta='#74AFAD',
        highlight=['#A6CAEC', '#09CACC'], pill=['#09CACC'], pill_text='#050816',
        lines='#1C2B4E', logo='white lockup', text_on_mass='#FFFFFF'),
    'dark-lagoon': dict(
        name='Dark Lagoon', theme='dark', pillars='Brand world (Sat)',
        idea='Deep and atmospheric. A lagoon aurora in teal night.',
        ground=['#040C12', '#061A22', '#08262F'], ground_glow=('#0088AA', 35, 'top-left'),
        surface=dict(fill='#0A2028', border='#163A42', shadow=None),
        raised=dict(fill='white 8% glass', border='Polar 12% inner top edge', shadow=None),
        mass=['#062A33', '#00727F', '#0088AA'], mass_name='Lagoon Aurora', mass_glows=[('#34CCA4', 35, 'centre'), ('#09CACC', 30, 'top-right')],
        mass_shadow=None, mass_edge=('#E9FFFC', 25),
        headline='#FFFFFF', supporting='#74AFAD', meta='#A6CAEC',
        highlight=['#09CACC', '#34CCA4'], pill=['#34CCA4'], pill_text='#050816',
        lines='#163A42', logo='white lockup', text_on_mass='#FFFFFF'),
}

WEEK = [('Mon', 'dark-royal', 'Insight'), ('Tue', 'light-royal', 'How we work'), ('Wed', 'dark-royal', 'Insight'),
        ('Thu', 'light-royal', 'Proof'), ('Fri', 'light-lagoon', 'Grow with us'), ('Sat', 'dark-lagoon', 'Brand world'),
        ('Sun', 'light-royal', 'How we work')]

GATES = {
    'light': ['Mean luminance of the image at least 0.55', 'At most 6% of pixels darker than luminance 0.10',
              'No fill darker than the mood’s darkest mass stop, except text'],
    'dark': ['Mean luminance of the image at most 0.15', 'At least 2% of pixels brighter than luminance 0.50 (the glow)',
             'Glow and highlight together cover at most 25% of the frame'],
}

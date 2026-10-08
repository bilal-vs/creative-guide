---
date: 2026-10-07
pillar: how-we-work
type: taste-probe
round: L1
status: waiting for outputs
---

# Taste probe L1 · light · P3 "Your payments follow the project"

**Why:** the user asked to train the visuals by rating 4 different looks for the same post, from 1 to 10.
- **Order:** single posts first, carousels later; light first, then dark.
- **Same copy:** every version has the same 7 pieces of text, the same logo reference and the same settings, so only the visual direction changes.

**How:**
1. Run each prompt in Google Flow: Images · Nano Banana 2 · 3:4 · 4 outputs · one ingredient, `brand/ref-pack/ref-pack-v2-light.png`. Paste exactly as written.
2. Upload the outputs to the Taste Lab page: https://claude.ai/artifact/Rbi98WmtVZB12QcBn7edrT (source `writing/taste/taste-lab.html`, built by `tools/build_taste_lab.py` from `writing/taste/rounds.json`).
3. Rate every image 1–10, tap tags, and pick a favourite direction.
4. Claude reads the ratings back and records what they teach in `learnings/taste.md`.

| Variant | Look | What it tests |
|---|---|---|
| A · Report | Calm engineering-report page: misty white page, a full-bleed lagoon colour band, a flat white milestone diagram and one frosted-glass piece. | Baseline: the current VISUAL-SYSTEM-v1 look. Flat and calm, with the least colour. |
| B · Luminous | Colour-led: one silky aqua-to-lagoon gradient fills the background, with three floating frosted-glass discs on a white line. | More colour and softness: does a gradient field beat a calm page with one band? |
| C · Studio 3D | Product-photography still life: porcelain and frosted-glass plinths rising like steps on a pale aqua tabletop. | Dimensional, tactile objects versus flat graphics. |
| D · Swiss type | Type-led poster: a huge headline on off-white paper, one vertical brand-gradient bar and a thin minimal timeline. | Typography as the hero, with the least imagery. |

Prompt A is identical to `posts/2026-10-06-vis-p3-milestone-payments.md` Prompt v1, so outputs already made from it count here.

## Prompt A · Report
**Settings:** Google Flow · Images · Nano Banana 2 · aspect ratio `3:4` · outputs `4` · ingredient `brand/ref-pack/ref-pack-v2-light.png`.

```text
Create an image: a finished, ready-to-publish social media post for Instagram and LinkedIn, designed by a senior brand design team for Verdant Soft, a B2B software company that designs and builds custom software for international clients. It is a single image post in a recurring series that explains plainly how working with an outsourcing partner works, and this post shows startup founders the three points in a project at which they pay.

Layout: a strict editorial grid read from top to bottom, with margins of about 8% of the width at the sides and 11% of the height at the top and bottom that only the page and the plate reach into. The logo sits at the top left with its top edge about 11% down and the series pill on the same line at the top right, with a thin hairline rule across the content width just below them. The headline starts at about 20% of the height, followed by the accent bar and the subline, all left-aligned and ending by about 51%. The colour plate is a full-bleed horizontal band from about 55% to about 81% of the height, running off the left and right edges and covering about 28% of the image; the diagram sits on it inside the side margins. Below the band, on the plain page, the website address sits at the bottom left at about 87% of the height.

Colour: the page is a calm polar white with a cool sea tint, a soft vertical gradient from pale polar white (#F2FAFA) to pale misty aqua (#D2EBEC), with a faint polar-white glow at the top left. The plate is a smooth gradient from deep lagoon teal (#00727F) to ocean teal (#0088AA), with a soft deep-teal-tinted shadow on the page along its inner edge. The drawing and labels on it are white. The glass piece is pale sky-blue frosted glass (#A6CAEC) with a faint mint-jade (#34CCA4) light directly behind it, never behind a label. Hairline rules are pale sea-grey (#BFDDE0).

On the plate, a horizontal milestone rail: one straight white line across the plate at about two fifths of its height, from the left margin to about four fifths of the image width, carrying exactly three evenly spaced nodes, the first at its left end and the last at its right end. The nodes go from unfinished to finished: the first is a thin white ring, the middle one a white ring with a solid centre, and the last is the glass piece, a small rounded puck of frosted glass. Under each node, left-aligned with it, is its label in white bold sans-serif, about the subline's size, on one or two lines. The plate, the drawing and the glass piece carry no other words.

Text, each piece exactly as written between the double quotes:
- At the top right, on the same line as the logo, a small, fully rounded pill label filled with a smooth gradient from deep lagoon teal (#00727F) to deep ocean teal (#007A9E): "Outsourcing, Decoded", in white semi-bold.
- The headline: "Your payments follow the project", in extra-bold near-black navy (#050816), left-aligned on up to three lines; the final two words stay together on one line and are filled with a smooth gradient from deep ocean teal (#007A9E) to deep lagoon teal (#00727F). It is by far the largest text.
- Directly under the headline, a short accent bar about a tenth of the image width, in a gradient from muted slate blue (#416D95) to soft sage teal (#74AFAD).
- The subline: "Milestone-based, from kickoff to delivery.", in regular steel navy (#42658A), about two fifths of the headline's height.
- Under the first node: "Project initiation"
- Under the second node: "Key development phases"
- Under the third node: "Final delivery"
- The website address: "verdant-soft.com", in semi-bold steel navy (#42658A), small but sharp.
Apart from the logo, the image contains exactly seven pieces of text, the ones quoted above, each appearing once and spelled exactly as given. Every other area is clean page, plate, lines and shapes.

Logo: use the attached image as the Verdant Soft logo. Place it unchanged at the top left on the plain page, inside the margins, about a quarter of the image width, keeping its shape, letters and slate-blue to sage-teal gradient colours exactly as in the attached image.

Design finish: a premium, minimal editorial page by a senior brand design team, calm and exact like a beautifully designed engineering report: a strict grid, generous empty space, asymmetric and uncluttered. Type is a crisp neo-grotesque sans-serif in the style of Inter, with extra-bold, tightly spaced sentence-case headlines and a neat monospace for small reference text; every letter is sharp and easy to read on a phone. The plate is a crisp-edged, full-bleed printed panel that keeps any glow inside itself. The drawing on it is flat and white, with even rounded strokes, only horizontal and vertical lines meeting at right angles, and a faint grid of tiny dots. The frosted glass piece is the only dimensional object, softly lit and matte. Everything is matte, with a very fine print grain over the whole image. Pure graphic design in cool blues and teals with near-black navy and white.

Portrait image, 3:4 aspect ratio.
```

## Prompt B · Luminous
**Settings:** Google Flow · Images · Nano Banana 2 · aspect ratio `3:4` · outputs `4` · ingredient `brand/ref-pack/ref-pack-v2-light.png`.

```text
Create an image: a finished, ready-to-publish social media post for Instagram and LinkedIn, designed by a senior brand design team for Verdant Soft, a B2B software company that designs and builds custom software for international clients. It is a single image post in a recurring series that explains plainly how working with an outsourcing partner works, and this post shows startup founders the three points in a project at which they pay.

Layout: a calm, airy portrait composition with margins of about 8% of the width at the sides and 11% of the height at the top and bottom. The logo sits at the top left with its top edge about 11% down, and the series pill on the same line at the top right. The headline starts at about 20% of the height, followed by the accent bar and the subline, all left-aligned and ending by about 50%. The milestone diagram floats across the lower half, from about 58% to about 80% of the height, inside the side margins. The website address sits at the bottom left at about 88% of the height.

Colour: the whole background is one luminous, silky gradient field that stays light and bright. Pale polar white (#F2FAFA) fills the top left behind all the text, then the colour flows diagonally down to the right through soft aqua (#D2EBEC), bright aqua (#09CACC) and mint jade (#34CCA4) into a glowing lagoon teal (#00ACB3) and ocean teal (#0088AA) in the bottom right corner, with a faint touch of sky blue (#A6CAEC) along the right edge. The blend is smooth, like light through tinted glass, with a very fine print grain, and the top half stays almost white.

The diagram: a thin white line runs straight across the lower half at about 66% of the height, from the left margin to the right margin, carrying exactly three evenly spaced frosted-glass discs. Each disc is a softly rounded, translucent puck of sandblasted glass with a bright white rim, picking up the colours of the gradient behind it; the discs grow slightly larger from left to right, and the last one glows softly from within. Directly under each disc sits a small white rounded tag holding its label in near-black navy bold sans-serif. The discs, the line and the tags carry no other words.

Text, each piece exactly as written between the double quotes:
- At the top right, on the same line as the logo, a small, fully rounded white pill label with a hairline deep lagoon teal (#00727F) outline: "Outsourcing, Decoded", in deep lagoon teal (#00727F) semi-bold.
- The headline: "Your payments follow the project", in extra-bold near-black navy (#050816), left-aligned on up to three lines; the final two words stay together on one line and are filled with a smooth gradient from deep ocean teal (#007A9E) to deep lagoon teal (#00727F). It is by far the largest text.
- Directly under the headline, a short accent bar about a tenth of the image width, in a gradient from muted slate blue (#416D95) to soft sage teal (#74AFAD).
- The subline: "Milestone-based, from kickoff to delivery.", in regular steel navy (#42658A), about two fifths of the headline's height.
- On the tag under the first disc: "Project initiation"
- On the tag under the second disc: "Key development phases"
- On the tag under the third disc: "Final delivery"
- The website address: "verdant-soft.com", in semi-bold steel navy (#42658A), small but sharp.
Apart from the logo, the image contains exactly seven pieces of text, the ones quoted above, each appearing once and spelled exactly as given. Every other area is clean gradient, glass and line.

Logo: use the attached image as the Verdant Soft logo. Place it unchanged at the top left on the plain page, inside the margins, about a quarter of the image width, keeping its shape, letters and slate-blue to sage-teal gradient colours exactly as in the attached image.

Design finish: a premium, modern brand graphic by a senior design team: luminous and colour-led, with one silky gradient, a few pieces of soft frosted glass and crisp editorial typography. Type is a crisp neo-grotesque sans-serif in the style of Inter, with extra-bold, tightly spaced sentence-case headlines; every letter is sharp and easy to read on a phone. Generous empty space, nothing cluttered, a matte finish with a very fine grain, in fresh aquas and teals with near-black navy and white.

Portrait image, 3:4 aspect ratio.
```

## Prompt C · Studio 3D
**Settings:** Google Flow · Images · Nano Banana 2 · aspect ratio `3:4` · outputs `4` · ingredient `brand/ref-pack/ref-pack-v2-light.png`.

```text
Create an image: a finished, ready-to-publish social media post for Instagram and LinkedIn, designed by a senior brand design team for Verdant Soft, a B2B software company that designs and builds custom software for international clients. It is a single image post in a recurring series that explains plainly how working with an outsourcing partner works, and this post shows startup founders the three points in a project at which they pay.

Layout: a premium editorial portrait layout with margins of about 8% of the width at the sides and 11% of the height at the top and bottom. The logo sits at the top left with its top edge about 11% down and the series pill on the same line at the top right, with a thin hairline rule across the content width just below them. The headline starts at about 18% of the height, followed by the accent bar and the subline, all left-aligned and ending by about 44%. The lower half is a calm still-life scene that runs off the left, right and bottom edges, and the website address sits at the bottom left at about 88% of the height, on the pale tabletop.

Scene: the whole image is one seamless pale studio set, photographed like premium product photography. The upper part is a smooth misty white backdrop (#F5F9FD) that curves softly into a pale aqua tabletop (#E3F3F3) across the lower half, lit by soft, diffuse daylight from the upper left that casts gentle, soft-edged shadows to the right. On the tabletop stand exactly three rounded plinths in a row from left to right, each one taller than the one before, like steps rising: the first is matte pale porcelain, the second is matte pale porcelain with a deep lagoon teal (#00727F) top, and the third and tallest is made of frosted lagoon-teal glass (#00ACB3) that glows softly from within. A slim white line runs along the tabletop in front of the three plinths, linking them. In front of each plinth stands a small upright white card facing the camera, holding its label in near-black navy bold sans-serif. The camera looks straight on from plinth height with a 50mm lens, and everything is in crisp focus. The plinths, the line and the cards carry no other words.

Text, each piece exactly as written between the double quotes:
- At the top right, on the same line as the logo, a small, fully rounded pill label filled with a smooth gradient from deep lagoon teal (#00727F) to deep ocean teal (#007A9E): "Outsourcing, Decoded", in white semi-bold.
- The headline: "Your payments follow the project", in extra-bold near-black navy (#050816), left-aligned on up to three lines; the final two words stay together on one line and are filled with a smooth gradient from deep ocean teal (#007A9E) to deep lagoon teal (#00727F). It is by far the largest text.
- Directly under the headline, a short accent bar about a tenth of the image width, in a gradient from muted slate blue (#416D95) to soft sage teal (#74AFAD).
- The subline: "Milestone-based, from kickoff to delivery.", in regular steel navy (#42658A), about two fifths of the headline's height.
- On the card in front of the first plinth: "Project initiation"
- On the card in front of the second plinth: "Key development phases"
- On the card in front of the third plinth: "Final delivery"
- The website address: "verdant-soft.com", in semi-bold steel navy (#42658A), small but sharp.
Apart from the logo, the image contains exactly seven pieces of text, the ones quoted above, each appearing once and spelled exactly as given. Every other area is clean backdrop, tabletop and objects.

Logo: use the attached image as the Verdant Soft logo. Place it unchanged at the top left on the plain page, inside the margins, about a quarter of the image width, keeping its shape, letters and slate-blue to sage-teal gradient colours exactly as in the attached image.

Design finish: premium product photography meets editorial graphic design: tactile, calm and precise, like a launch image from a top product company. Matte porcelain and sandblasted frosted glass, soft daylight and gentle shadows, in a restrained palette of misty whites, pale aquas and lagoon teal with near-black navy type. Type is a crisp neo-grotesque sans-serif in the style of Inter, with extra-bold, tightly spaced sentence-case headlines; every letter is sharp and easy to read on a phone. Generous empty space above the objects, nothing cluttered, a very fine grain.

Portrait image, 3:4 aspect ratio.
```

## Prompt D · Swiss type
**Settings:** Google Flow · Images · Nano Banana 2 · aspect ratio `3:4` · outputs `4` · ingredient `brand/ref-pack/ref-pack-v2-light.png`.

```text
Create an image: a finished, ready-to-publish social media post for Instagram and LinkedIn, designed by a senior brand design team for Verdant Soft, a B2B software company that designs and builds custom software for international clients. It is a single image post in a recurring series that explains plainly how working with an outsourcing partner works, and this post shows startup founders the three points in a project at which they pay.

Layout: a bold Swiss typographic poster on a strict grid, with margins of about 8% of the width at the sides and 11% of the height at the top and bottom. A slim vertical colour bar, about 3% of the image width, runs the full height of the image along the left edge. The logo sits at the top left inside the margin with its top edge about 11% down, and the series pill on the same line at the top right. The headline is set very large, starting at about 22% of the height and filling most of the content width, followed by the accent bar and the subline, all left-aligned and ending by about 60%. Below it, from about 66% to about 80% of the height, sits a minimal timeline, and the website address sits at the bottom left at about 88% of the height.

Colour: the page is clean off-white paper (#F9F9F9) with a very fine print grain. The vertical bar is a smooth gradient from electric royal blue (#2457D6) at the top through deep ocean teal (#007A9E) to soft sage teal (#74AFAD) at the bottom. Almost everything else is near-black navy (#050816) on the paper; the only other colour is in the highlighted headline words, the accent bar and the last timeline marker.

The timeline: one thin near-black navy line runs straight across the content width, carrying exactly three evenly spaced small circles. The first two are thin near-black navy outlines, and the third is solid, filled with a smooth gradient from electric royal blue (#2457D6) to deep ocean teal (#007A9E). Under each circle, left-aligned with it, sits its label in near-black navy bold sans-serif. The line and the circles carry no other words.

Text, each piece exactly as written between the double quotes:
- At the top right, on the same line as the logo, a small, fully rounded pill label drawn as a thin near-black navy (#050816) outline on the paper: "Outsourcing, Decoded", in near-black navy semi-bold.
- The headline: "Your payments follow the project", in extra-bold near-black navy (#050816), very large and very tightly spaced, left-aligned on up to three lines; the final two words stay together on one line and are filled with a smooth gradient from electric royal blue (#2457D6) to deep ocean teal (#007A9E). It is by far the largest text, filling most of the width.
- Directly under the headline, a short accent bar about a tenth of the image width, in a gradient from muted slate blue (#416D95) to soft sage teal (#74AFAD).
- The subline: "Milestone-based, from kickoff to delivery.", in regular steel navy (#42658A), about two fifths of the headline's height.
- Under the first circle: "Project initiation"
- Under the second circle: "Key development phases"
- Under the third circle: "Final delivery"
- The website address: "verdant-soft.com", in semi-bold steel navy (#42658A), small but sharp.
Apart from the logo, the image contains exactly seven pieces of text, the ones quoted above, each appearing once and spelled exactly as given. Every other area is clean paper.

Logo: use the attached image as the Verdant Soft logo. Place it unchanged at the top left on the plain page, inside the margins, about a quarter of the image width, keeping its shape, letters and slate-blue to sage-teal gradient colours exactly as in the attached image.

Design finish: a bold, minimal Swiss editorial poster by a senior typographer: type-led, with a huge confident headline, a strict grid, vast calm white space and precise thin lines, nothing decorative. Type is a crisp neo-grotesque sans-serif in the style of Inter, with extra-bold, very tightly spaced sentence-case headlines; every letter is sharp and easy to read on a phone. Flat print design on matte paper with a very fine grain.

Portrait image, 3:4 aspect ratio.
```

## Results (2026-10-08)
| Variant | Score | Note |
|---|---|---|
| D Swiss type | **7/10** | "looks good but text needs improvement too flat also" (Modern, Premium, Clear to read) |
| C Studio 3D | 4/10 | "serves no purpose font too basic" |
| A Report | 2/10 | "Nothing useful font too basic" (Looks AI, Old-fashioned) |
| B Luminous | 1/10 | "font too basic" (Looks AI, Too dull, Old-fashioned) |

- **Round note:** "font too basic use some attractive but visually good font".
- **Text:** all 7 strings rendered exactly in every variant.
- **Analysis:** in `learnings/taste.md`.
- **Decision:** D wins. VISUAL-SYSTEM-v1 (A) is paused. Round L2 explores typefaces and depth on D's layout.

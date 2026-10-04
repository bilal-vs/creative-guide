Verdant Soft is a software house in Lahore building web, mobile, cloud and AI products for founders abroad. This guide sets the look of its daily Instagram and LinkedIn posts in two themes, **light** and **dark**. Posts are 4:5 (1080 × 1350). An image model makes the picture; the logo, headline and every word are overlaid afterwards in these tokens.

## The two fixed colours
- `slate-blue` **#416D95** and `sage-teal` **#74AFAD** are the brand. They are the logo's own colours and never change, in any theme, on any post.
- `brand-gradient` runs slate blue to sage teal at 102.32°. It is the logo, the mark, graphic bars and shapes.
- Everything else (backgrounds, text, lines, washes) is a theme token. Use the token, never a raw hex.
- It is **not green**. Never describe or render the brand as green, and never use yellow or royal navy (#194493-style) on a post. Those belonged to the old social templates.

## Light theme
Calm, airy, like the website.
- Ground: `bg` (Mist #F4F7F8), with `surface` (white) for cards and panels.
- Text: `ink` for headlines, `body` for copy, `muted` for the caption line.
- Highlight 1–3 words of the headline in `highlight`, which is `slate-blue` here (5.1:1).
- Use `sage-teal` only as fills, shapes, lines and icons. It is never text on light (2.3:1).
- Never set gradient text on light. Use the gradient as a bar or shape beside the words.
- Logo: the gradient lockup (`verdant-logo-gradient.png`).

## Dark theme
Focused and technical, the website's footer brought forward.
- Ground: `bg` (Deep Slate #0E1A23), with `surface` (#162632) for panels.
- Text: `ink` (near-white) for headlines, `body` for copy, `muted` for the caption line.
- Highlight words in `highlight`, which is `sage-teal` here (7.1:1), or in `brand-gradient` text at 24px and up (its blue end is 3.2:1).
- Use `slate-blue` for fills, shapes and large text only.
- Logo: the white lockup (`verdant-logo-white.png`).

## Which theme, when
Alternate so the grid reads as a rhythm, about 4 light and 3 dark each week.

| Pillar | Theme | Why |
|---|---|---|
| Engineering insight (Mon, Wed) | **Dark** | Technical, focused, code-adjacent |
| How we work (Tue, Sun) | Light | Clear, open, reassuring |
| Proof: client words or project spotlight (Thu) | Light | Clean ground for quotes and screens |
| Grow with us (Fri) | Light | Warm, human, real photos |
| Brand world (Sat) | **Dark** | The most visual, atmospheric post |

National and religious days use their own pre-approved templates, not these themes.

## Colour pairings that pass
- **Light:**
  - `ink` on `bg` 15.2:1, `body` on `bg` 8.2:1, `muted` on `bg` 4.5:1, `slate-blue` on `bg` 5.1:1
  - `on-blue` (white) on a `slate-blue` fill 5.5:1
  - `on-teal` (ink) on a `sage-teal` fill 6.6:1
- **Dark:**
  - `ink` on `bg` 16.1:1, `body` on `bg` 9.8:1, `muted` on `bg` 5.6:1, `sage-teal` on `bg` 7.1:1
  - `slate-blue` on `bg` 3.2:1, for 24px+ text only
- **Never:** white on `sage-teal`, `sage-teal` text on light grounds, or small `slate-blue` text on dark grounds.

## Typography
- **Inter only.** Headlines 700 with slight negative tracking, quotes 500, captions 500. Styles: `display`, `headline`, `quote`, `subhead`, `body`, `label`, `caption`; sizes are at full post size.
- **Sentence case** everywhere. No all-caps headlines, no Unicode "bold" letters.
- **One headline per post**, up to 8 words. Optionally one `subhead` line.
- The series `label` (for example "Build Notes · 04") sits above the headline in `highlight`.
- The image model never renders words. All text is overlaid.

## Logo
- **Placement:** full lockup top-left at `safe-x` / `safe-y`, at `logo-height` (44px, about 184px wide).
  - Light theme: `verdant-logo-gradient.png`.
  - Dark theme: `verdant-logo-white.png`.
- **The mark** (`vs-mark-gradient.png`, `vs-mark-white.svg`) is for avatars and for the oversized background motif.
- **Never** recolour, outline, add effects to, or place the logo over a busy image area.
- **Clear space:** at least the height of the "V" on every side.

## Post layout (1080 × 1350)
- **Margins:** `safe-x` 72px left and right, `safe-y` 144px top and bottom. Logo, text and caption stay inside, so the post survives a 1:1 crop and Instagram's 3:4 grid. Image and motif shapes may bleed to the edges.
- **Top band:** logo left, optional series `label` right or below.
- **Text block:** headline (+ subhead) in one zone, top-left or bottom-left. Never centred over the image's subject.
- **Image zone:** the generated picture fills the rest. The prompt asks for calm, empty space where the text block sits.
- **Bottom line:** `caption` in `muted`: verdant-soft.com, or the handle.
- **Motif (optional):** an oversized, cropped VS mark or a fine line-and-node mesh in `motif`, bleeding off one edge.
- **Panels and quote boxes:** `surface` or a `wash-*` token, `radius-md`.

## Imagery
Starting descriptions for the image prompt. These are hypotheses to test, not final wording.
- **Light:** bright, airy, soft daylight; off-white and pale grey surfaces; small accents in muted slate blue (#416D95) and soft sage teal (#74AFAD); clean architectural or modular forms; lots of empty negative space.
- **Dark:** deep slate night tones (#0E1A23); soft sage-teal and slate-blue light glowing from within forms; calm low-key lighting; generous dark negative space.
- **Subjects (both themes):** growth shown through structure. Modular blocks assembling, layered translucent panels, branching node networks, light moving through architecture.
- **Never:**
  - robots, glowing brains, holographic icon clouds, lightbulbs, coins, handshakes
  - plants sprouting from laptops
  - stock smiling teams, or AI people shown as staff
  - third-party logos
  - any text inside the image

## Voice on the post
Engineer-to-founder: plain, specific, warm. One idea per post. The site's own line is the north star: "Let's build it right." Captions are written per platform, with 3–5 hashtags including #VerdantSoft.

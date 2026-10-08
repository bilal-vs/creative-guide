# Taste profile (the user's visual preferences)

**What it's for:** the evidence for what the user likes and dislikes visually. A rule moves into `STYLE_GUIDE.md` §5 only after it has held on 2 or more posts; each rule cites its round and images.

**Method** (agreed 2026-10-07):
- **Probes:** same post, same text, 4 visual directions per round. Light first, then dark; single posts first, carousels later.
- **Ratings:** the user rates every output 1–10 with tap-tags on the Taste Lab page (https://claude.ai/artifact/Rbi98WmtVZB12QcBn7edrT). Ratings are stored in the page's `images` collection and favourites in `rounds/<id>`.
- **Claude predicts blind:** before reading the user's ratings, Claude records a prediction (direction ranking, then per-image picks once the images are visible). The agreement rate is how we know Claude has learned the taste; the target is about 9 in 10.
- **Disagreements are the lesson:** each gets a written reason here.

## Round L1 (light · P3): Claude's blind prediction, recorded before any images or ratings
**Predicted ranking:**
1. **B Luminous.** The user asked for "full level of creativity colors graidents visuals", called the earlier palette "dull boring", and picked an aqua/teal gradient reference (#34CCA4, #00ACB3, #0088AA, #09CACC).
2. **C Studio 3D.** It reads as "premium" and "attractive" from the post rules, and it's visual-led.
3. **A Report.** Clean and readable, but it may read as too calm.
4. **D Swiss type.** Probably "too plain / not enough visual" for this user, though it's the most minimal.

**Risks to the prediction:**
- B may look generic-AI with too much gradient.
- C's 3D may garble the label cards.
- The user's "minimal" rule could favour A or D.

## Results
### Round L1 (light · P3), rated 2026-10-08
Ratings come from the Taste Lab db; Claude viewed all 4 uploads. The user uploaded 1 output per direction. Nano Banana 2 rendered all 7 strings exactly in all 4, with the logo correct.

| Dir | Score | User note | Tags | What the image actually showed |
|---|---|---|---|---|
| D Swiss type | **7** | "looks good but text needs improvement too flat also" | Modern, Premium, Clear to read | Off-white paper; slim royal-to-teal vertical bar at the left edge; huge 4-line headline with "the project" in a royal-to-sage gradient; accent bar; subline; thin navy timeline with 2 outline circles and a gradient-filled third; labels in regular weight (the prompt asked for bold); URL. Strong hierarchy, very plain. |
| C Studio 3D | 4 | "serves no purpose font too basic" | — | Misty page and 2-line headline; the still life sits in an inset rounded card (not full-bleed): porcelain cylinder, porcelain with a lagoon top, a frosted teal glass cylinder, and tent cards with labels. Polished render, but the objects mean nothing. |
| A Report | 2 | "Nothing useful font too basic" | Looks AI, Old-fashioned | The current VISUAL-SYSTEM-v1 look: aqua page, full-bleed lagoon band, white rail with ring, dot and glass puck, white labels. Reads as a stock SaaS infographic. |
| B Luminous | 1 | "font too basic" | Looks AI, Too dull, Old-fashioned | A pale page washing into a mint/teal glow at the bottom right (reads greenish); three big frosted discs; white tags. Generic glassmorphism. |

**Round note (user):** "font too basic use some attractive but visually good font". No favourite was tapped; D wins by score.

**Prediction vs actual:**
- **Predicted** B > C > A > D; **actual** D > C > A > B.
- **Top pick:** wrong. The middle two were right, and the extremes were swapped.
- **Agreement:** 0/1 on the top pick and 2/4 on positions.
- **Why I was wrong:** I took "full creativity with colours and gradients" (2026-10-04) to mean soft gradient fields. In images, the user reads soft glows, pastel gradients and frosted glass as **AI-looking and old-fashioned**.

**Candidate rules** (one round only; promote after a second round confirms):
1. **Typography is the biggest lever.** "Font too basic" appeared in 3 image notes and the round note. A plain neo-grotesque (Inter style) everywhere reads as basic. Headlines need a typeface with character.
2. **Type-led beats illustration-led.** Big confident type with strict hierarchy (D) wins on modern, premium and clear.
3. **Visuals must mean something.** Decorative objects or diagrams that don't add meaning score low ("serves no purpose", "nothing useful").
4. **No soft-glow gradients, no glassmorphism, no pastel haze.** These are the "AI look".
5. **Flat is a weakness.** The winner was called "too flat", so the user wants depth, but depth with a purpose (not C's random objects).

**Next:** round L2 tests rules 1 and 5 on D's layout: display font, editorial serif, dimensional type, bold colour block.

## Round L2 (light · "What your dev brief is missing"): Claude's blind prediction, recorded 2026-10-08 before any images or ratings
**Predicted ranking:**
1. **C Embossed paper.** It answers both complaints at once: a characterful font and depth with a purpose (the depth is the print itself, not random objects).
2. **A Display font.** It fixes "font too basic" but stays flat.
3. **D Colour block.** Bold and modern, but more blue/teal mass, and the user disliked colour-led B in L1.
4. **B Editorial serif.** Elegant, but may read as "old-fashioned", the user's own tag on L1's losers.

**Risk:** the embossing may soften the text, or read as "mockup / AI".

**Withdrawn, never generated (2026-10-08).** The user called the four L2 prompts "completely useless" and, in the same messages, set the main rule (70% Verdant, 30% other, other = carousels only) and the design bar ("a group of graphic designers on a high budget… visually attractive with some functionality, not useless"). Lesson for me: a taste round must use a post the feed will really run. L2 trained single posts on generic advice, which is now carousel-only, and its four versions only swapped the font or the depth instead of offering four real design ideas. The prediction above is void.

## Round L3 (light · Verdant single, Project Spotlight F30): Claude's blind prediction, recorded 2026-10-08 before any images or ratings
**What changed from L2:** a real Verdant single (four modules we built for a clinic, plus the stack), and four different agency-grade ideas in which the visual carries the information. Each uses a different characterful typeface.

**Predicted ranking:**
1. **B Interface.** The most literal "functionality" (it shows the software) and the most "high-budget launch" look. Risk: wordless UI may sprout fake text (variance).
2. **A Module cards.** It is L1's 7/10 winner with both complaints fixed (a sharper display font; raised cards for depth). Risk: still reads as "a poster", not agency-grade.
3. **C Patient file.** Premium and tactile, with a clear metaphor. Risk: the tabs' text may be small or garbled, and a folder may feel ordinary.
4. **D System map.** It explains the system best, but isometric infographics often read as "looks AI / generic".

**What I'll learn:** whether "functionality" means showing the product (B), structured information (A, D) or a physical metaphor (C), and which typeface family wins (Clash, Instrument Serif, Syne, Unbounded styles).


# Verdant Soft carousel playbook

**Version:** v1, 2026-10-06.
**Sources:** the user's 10-point carousel checklist, and *The Carousel Playbook* by @adarshxdesign (25 hook formulas, cover checklist, slide framework, 3-second test).
**How it was adapted:** for a B2B engineering brand whose posts are made automatically.
- **Kept:** everything that holds up.
- **Changed:** anything that would need invented numbers, a human replying in DMs, or creator-style bait.
- **Added:** proof, fact-checking, and our theme system.

The machine-readable version is `STYLE_GUIDE.md` §4.1 `CAROUSEL-v2` (v2 adds the external and roundup variants for Tech, Explained).

---

## 1. What we kept, what we changed, and why
| From the sources | Our version | Why |
|---|---|---|
| Hook → Problem → Value → Proof/Examples → CTA | Cover → Payoff → Steps → **Proof** → CTA → **Receipt** | Combines both sources. B2B buyers need proof before they act. The receipt is what gets saved. |
| CTA on the second-last slide (people leave on the last) | **Main CTA on the second-last slide, plus a soft CTA line on the receipt** | Meets both: the CTA comes before people drop off, and the last slide still says what to do next (checklist #10). |
| "Comment PDF" keyword CTAs | **Not used** | They need a person sending DMs, which the pipeline can't do. They also read as cheap to founders and CTOs. |
| Proof and number hooks ("I analyzed 100…", "__% fail…") | **Proof and fact hooks**, built only from `FACTS` and `PUBLIC-PROOF` | We never invent numbers. |
| "Dark background + bright type never fails" | **Contrast is measured, not assumed** | Both themes pass: light posts get contrast from Abyss ink at 15:1+, dark posts from white at 16:1+. |
| Under 10 words on the cover | **8 words maximum** | Matches our headline rule. |
| 3-second test, 5/5 or don't post | **Kept**, plus a sixth question: "Is every word true for us to say?" | Truth is a gate for an automated brand. |

## 2. The framework: every slide has one job
Length: **6–8 slides**. That's enough to teach something and short enough to finish.

| Slide | Name | Job | Copy limits | What it drives |
|---|---|---|---|---|
| 1 | **Cover** | Open a loop: a claim plus tension, never the answer | Headline ≤ 8 words; optional subline ≤ 8 words; "Swipe" cue | Swipe rate |
| 2 | **Payoff** | Why it matters to the reader, then the first real answer, fast. Treat it as a second cover. | Headline ≤ 6 words; body ≤ 35 words | Dwell time |
| 3 to N−3 | **Steps** | One idea per slide. End on a bridge line into the next slide. | Headline ≤ 6 words; body ≤ 30 words; bridge ≤ 8 words | Completion |
| N−2 | **Proof** | A fact, a case study, or a client's exact words | Verbatim quote or a fact from `FACTS`; attribution | Trust |
| N−1 | **CTA** | One clear action: book a call, follow the series, or save | Headline ≤ 6 words; one action line | Action |
| N | **Receipt** | The whole carousel compressed into one savable frame, plus a soft CTA line | List of ≤ 6 short items; "Save this" line; logo | Saves and shares |

**Bridge lines** stop a reader leaving mid-carousel. Examples:
- "But that's only half of it."
- "Then comes the part most teams skip."
- "Here's where it gets expensive."

## 3. Hook formulas (25, adapted)
A hook is a **claim, not a topic**. Add a tension word (*costing, breaks, quietly, before, nobody, stop, wrong*). It has to be something we can stand behind.

**Curiosity**
1. Nobody tells founders about ___ until it's too late.
2. The ___ question to ask before you build.
3. What ___ looks like when it's built to scale.
4. ___, explained in one carousel.
5. Where ___ quietly breaks first.

**Contrarian**
6. Stop ___. Start ___ instead.
7. ___ won't save your launch. ___ will.
8. ___ is a design decision, not a dev task.
9. Most ___ advice ignores ___.
10. ___ isn't the problem. ___ is.

**Proof and facts** (only from `FACTS` and `PUBLIC-PROOF`)
11. How we built ___ for ___. (a case study, F30–F39, no client named)
12. What a client said after ___. (verbatim only)
13. Inside a ___ build: the decisions that mattered.
14. Our stack for ___, and why. (F05, F06)
15. From brief to ___: how a project actually runs. (F04, F12, F13)

**Fear and mistakes**
16. Your ___ isn't slow. Your ___ is.
17. This ___ is quietly costing you ___.
18. ___ mistakes founders make when outsourcing. (the number counts the slides, never a statistic)
19. Before you hire a dev team, read this.
20. The ___ that breaks products at scale.

**Aspiration**
21. ___ without ___: how it's done.
22. Steal our ___ checklist.
23. What we'd tell a first-time founder about ___.
24. The ___ that makes a product easy to grow.
25. Get ___ right before you write a line of code.

**Hook tests:**
- Would a CTO repeat it to their cofounder?
- Is it true for Verdant Soft to say?
- Does it leave a gap the next slide fills?

## 4. Cover rules
1. **Say one thing.** One cover, one message.
2. **Make it big.** Headline at 88–100 px on a 1080 px canvas. It has to be readable on a phone at arm's length.
3. **Contrast is measured.** Use the theme's ink and highlight pairs only (`THEMES-v1`).
4. **A claim, not a topic.** "UI/UX process" describes. "The costliest bugs are written before the code" provokes.
5. **Leave a gap.** Tease the answer, never give it away.
6. **One focal point.** The mood's colour mass holds the only visual.

**Formula:** bold claim + tension word + one focal point + big type + measured contrast.

## 5. Copy rules for every slide
- One idea per slide, and every slide must teach, explain, prove or move the reader forward.
- No more than 3 text levels: headline, body, meta (counter).
- One highlight per slide (1–3 words).
- Body text at least 32 px at 1080 wide, and at most 30 words.
- Numbers appear only as step counters ("01", "02 / 08"), or when they're in `FACTS` with `status: confirmed`.
- Voice follows `brand/strategy.md` §5: engineer to founder, plain and specific, no buzzwords.
- **Alt text:** one plain sentence per slide for Instagram. LinkedIn documents get the cover headline as the title.

## 6. Design rules (colour and type come from the themes)
- **Mood:** the whole carousel uses one theme and mood, picked by pillar (`THEMES-v1`).
- **Visuals:** the cover carries the colour mass and the hero visual. Inner slides are text-led, with a small motif.
- **Fixed positions on every slide:**
  - logo top-left
  - counter "02 / 08" top-right
  - progress dots bottom-right
  - footer bottom-left
- **Receipt slide:** list rows with step numbers. It has to work as a standalone image.
- **Format:** 4:5 at 1080 × 1350.
  - **LinkedIn:** upload as a PDF document.
  - **Instagram:** upload as an image carousel. Same slides, separate captions.

## 7. The Verdant carousel checklist (14 points)
Run it before any carousel is published. Every item is pass or fail.

**Hook and story**
1. **Hook:** slide 1 is a claim plus tension, ≤ 8 words, and makes you want to swipe.
2. **One clear idea:** a stranger gets the topic within 3 seconds.
3. **Structure:** Cover → Payoff → Steps → Proof → CTA → Receipt, in 6–8 slides.
4. **Value:** every slide teaches, explains, proves or moves the reader forward. Nothing is filler.
5. **Bridges:** every step slide ends with a line that pulls the reader to the next.

**Design**
6. **Readable:** body text ≥ 32 px and ≤ 30 words; no zooming needed.
7. **Hierarchy:** it's obvious what to read first, second and third; one highlight per slide.
8. **Minimal:** no graphic, icon or decoration without a job; at most one visual per slide.
9. **Consistent:** one mood, one type scale, and the same positions for logo, counter and dots.

**Value and action**
10. **Save and share factor:** the receipt slide is worth saving on its own.
11. **CTA:** one clear action on the second-last slide, repeated softly on the last.

**Brand and truth** (our addition)
12. **True:** every claim is in `FACTS` or `PUBLIC-PROOF`; no invented numbers; quotes are verbatim.
13. **Voice:** no buzzwords; it sounds like an engineer talking to a founder.
14. **Theme:** the mood matches the pillar, and all text pairs pass contrast and the automatic image checks.

**3-second test (cover):**
- readable without trying
- one focal point
- a claim, not decoration
- ≤ 8 words
- you'd stop scrolling
- it's true for us to say

Six out of six, or regenerate the cover.

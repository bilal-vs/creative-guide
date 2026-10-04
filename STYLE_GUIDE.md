# Social Media Style Guide

> **Status: DRAFT, not production-ready.** Sections marked **TBD** are not yet proven. The pipeline must not run until every TBD is gone and the blind test (see `README.md`, phase 4) has passed.
>
> **Audience:** an automated agent that creates and publishes one post per day to Instagram and LinkedIn with no human editing. Every rule here must be followable as written. If an agent has to guess, the guide has a gap.
>
> **Verbatim blocks** are fenced code blocks preceded by `<!-- id: NAME-vN -->`. The pipeline copies them exactly.

---

## 1. How the pipeline uses this guide
**TBD.** The daily procedure, in order:

1. Pick today's pillar (§3 rotation)
2. Pick a topic (§3 topic bank, respecting no-repeat rules against the post history)
3. Fill the pillar's template (§4, §6)
4. Generate N images (§6 settings)
5. Judge every output (§8)
6. Select the best passing output, or retry, or use the fallback (§8)
7. Apply overlays (§5)
8. Write captions (§7)
9. Publish
10. Log the post to the history

## 2. Brand foundation
**TBD.**
- Company and offering
- Audience per platform (Instagram vs LinkedIn)
- Goals of the account
- Brand voice: traits, with do/don't examples

## 3. Content pillars, rotation, and topic bank
**TBD.**
- Pillar definitions: purpose and what qualifies
- Weekly rotation (day → pillar)
- Topic bank per pillar, and how to generate new topics
- No-repeat rules (window, and what counts as a repeat)

## 4. Post formats
**TBD.** One recipe per pillar: the concept pattern, template ID, slot rules, and caption template.

## 5. Visual identity
**TBD.**
- **Fixed elements** (never vary): palette, lighting, medium/style, mood
- **Variable elements** (vary daily within limits): subject, setting, composition, metaphor
- Palette: hex values plus the exact wording to use in prompts
- Composition and negative-space zones reserved for overlays
- Text-in-image policy (what the model may render vs. what is overlaid)
- Overlay spec: logo, headline, positions, sizes, fonts

## 6. Image prompt system
**TBD.**
- Master prompt template with `{slots}`
- Fixed style block (verbatim)
- Slot-filling rules
- Generation settings: model, aspect ratio, number of outputs, resolution
- Reference pack (if adopted)
- Known model quirks and their workarounds

## 7. Caption system
**TBD.**
- Instagram template: hook (first line, before the "more" cut-off), length, structure, CTA, hashtags, emoji policy
- LinkedIn template: hook (before "see more"), length, structure, CTA, link handling, hashtags
- Alt text rules
- Banned words and AI clichés (verbatim list)
- Approved few-shot examples

## 8. QA rubric and selection policy
**TBD.**
- Binary checks a vision model applies to every output
- Scoring and the pass threshold
- Number of candidates generated, selection rule, retry limit
- Fallback when no output passes
- Caption checks

## 9. Guardrails
**TBD.**
- AI disclosure policy. Note: Nano Banana outputs carry SynthID and C2PA metadata, so Meta platforms may auto-label them as AI.
- No likenesses of real people, no third-party trademarks or logos
- Claims and compliance rules for the industry

## 10. Approved examples
**TBD.** Each example records the post file, template ID, exact prompt and settings, a written description of the approved image, and both captions.

---

## Changelog
| Date | Change | Evidence |
|---|---|---|
| 2026-10-04 | Skeleton created | — |

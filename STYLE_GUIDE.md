# Social Media Style Guide

> **Status: DRAFT, not production-ready.** Sections marked **TBD** are not yet proven. The pipeline must not run until every TBD is gone and the blind test (see `README.md`, phase 4) has passed.
>
> **Audience:** an automated agent that creates and publishes one post per day to Instagram and LinkedIn with no human editing. Every rule here must be followable as written. If an agent has to guess, the guide has a gap.
>
> **Verbatim blocks** are fenced code blocks preceded by `<!-- id: NAME-vN -->`. The pipeline copies them exactly.

---

## 1. How the pipeline uses this guide
**TBD.** The daily procedure, in order:

1. **Read memory:** the post history (`posts/index.md` schema, §11), the news inbox, and today's calendar moments
2. **Decide today's post** using the priority from §3 (inbox > calendar > series episode > evergreen rotation), while respecting caps and no-repeat windows (§3, §9, §11)
3. Pick the topic and its facts (only from §2 `FACTS` and `PUBLIC-PROOF`)
4. Fill the pillar's template (§4, §6)
5. Generate N images (§6 settings)
6. Judge every output (§8)
7. Select the best passing output, or retry, or use the fallback (§8)
8. Apply overlays (§5)
9. Write captions, one per platform (§7)
10. Publish
11. Log the post to the history, with every field §11 requires

## 2. Brand foundation
> **DRAFT: researched from public sources on 2026-10-04 and not yet confirmed by the user.** Full sources: `brand/research.md`. The handler's proposal for positioning, audiences and voice is in `brand/strategy.md`. It moves here once approved.

**Company:** Verdant Soft (verdant-soft.com), a software company in Lahore, Pakistan, serving international clients.
**Service lines:** Custom Software Development · Cloud & DevOps · IT Team Outsourcing (dedicated teams) · UI/UX Design. Builds web and mobile applications.
**Goals of the accounts (user decision):** both Instagram and LinkedIn serve **brand, clients and talent**.
**Audiences, positioning, voice:** TBD, pending approval of `brand/strategy.md` §3–5.

### Fact bank
The pipeline may state a company fact **only if it appears below with `status: confirmed`**. Anything else, including facts that are true but not listed, must not be stated.

<!-- id: FACTS-v1 -->
```yaml
- id: F01
  fact: "Verdant Soft is a software company based in Lahore, Pakistan."
  status: confirmed
  source: verdant-soft.com; clutch.co/profile/verdant-soft
- id: F02
  fact: "Verdant Soft offers custom software development, cloud & DevOps, IT team outsourcing (dedicated teams), and UI/UX design."
  status: confirmed
  source: verdant-soft.com
- id: F03
  fact: "Verdant Soft builds web and mobile applications."
  status: confirmed
  source: verdant-soft.com
- id: F04
  fact: "Verdant Soft's UI/UX process: research & discovery, personas & journey maps, information architecture & wireframes, design & prototyping, usability testing, developer collaboration, post-launch iteration."
  status: confirmed
  source: verdant-soft.com/services/ui-ux-design
- id: F05
  fact: "Verdant Soft works with the MERN stack and React."
  status: confirmed
  source: client testimonial on verdant-soft.com
- id: F06
  fact: "Verdant Soft's cloud & DevOps work uses AWS, Docker, Kubernetes, Terraform, Ansible and CI/CD pipelines."
  status: confirmed
  source: Verdant Soft DevOps job posts
- id: F07
  fact: "Verdant Soft has delivered features for an AI SaaS platform."
  status: confirmed
  source: client testimonial on verdant-soft.com
- id: F08
  fact: "Verdant Soft was founded in 2019."
  status: pending        # single source (Clutch); user to confirm
  source: clutch.co/profile/verdant-soft
- id: F09
  fact: "Tagline: Engineering tomorrow's tech today!"
  status: pending        # unverified; confirm on live site
  source: search summary only
# Never state: team size, rates, minimum project size, employee reviews.
```

### Public proof
User decision: clients and testimonials that are **publicly available** may be used, **sparingly** (caps in §9). The pipeline may quote **only** `quote_verbatim` text from entries with `status: quotable`. Every entry below is still waiting for its exact wording to be captured.

<!-- id: PUBLIC-PROOF-v1 -->
```yaml
- id: P01
  who: "E-commerce management company (unnamed on Clutch)"
  gist: "Built a communication system with real-time chat and UI customisation; MVP delivered on time; 5.0 for quality, schedule, cost and willingness to refer."
  quote_verbatim: null
  source: https://clutch.co/profile/verdant-soft
  status: pending-verbatim
- id: P02
  who: "Elia Essen"
  gist: "Took full ownership of an AI SaaS platform; MERN/React; scalable, visually strong features."
  quote_verbatim: null
  source: https://www.verdant-soft.com/
  status: pending-verbatim
- id: P03
  who: "Nick Kuijpers, CEO, WEMASY"
  gist: "Supportive, reliable partner; dependable full-stack team."
  quote_verbatim: null
  source: https://www.verdant-soft.com/
  status: pending-verbatim
- id: P04
  who: "Shervin Khanzadi, CEO, Alogirft (spelling unverified)"
  gist: "Highly professional front-end team with a diverse skill set."
  quote_verbatim: null
  source: https://www.verdant-soft.com/
  status: pending-verbatim
```

## 3. Content strategy: pillars, rotation, series, inputs, calendar
**TBD.** Pending approval of `brand/strategy.md` §6–9.
- Pillar definitions: purpose and what qualifies
- Weekly rotation (day → pillar)
- Recurring series and episode order
- Input priority: news inbox > calendar > series > evergreen
- Topic bank per pillar, and how to generate new topics
- No-repeat rules (window, and what counts as a repeat)
- Calendar of moments, with the yearly table of movable dates

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
`[decided]` means the user agreed it. `[proposed]` means it's waiting for the user's approval in `brand/strategy.md` §10.

- `[decided]` **Facts:** state company facts only from §2 `FACTS` with `status: confirmed`. Never invent metrics, client names, awards, years or team size.
- `[decided]` **Public proof, used sparingly:** quote only `quote_verbatim` text from §2 `PUBLIC-PROOF` with `status: quotable`. `[proposed]` caps: at most **1 proof post per week**, and the **same client not again within 30 days**.
- `[proposed]` **No AI-generated people presented as Verdant Soft staff, clients or events.** Talent and culture visuals are conceptual, or show people who can't be identified (hands, silhouettes, shot from behind, out of focus). Real photos come only from the news inbox.
- `[proposed]` **National and religious days:** use only the pre-approved templates. Never generate Arabic or Urdu script, religious figures, or sacred sites.
- `[proposed]` **No third-party logos or trademarks** in images. Tech names in captions are fine.
- `[proposed]` **Identity:** never confuse the company with other "Verdant" companies (Verdant YC, Verdant DevCore, Verdant TCS, Verdant Web Tech, …).
- **TBD:** AI disclosure policy. Nano Banana outputs carry SynthID and C2PA metadata, so Meta platforms may label them as AI automatically.

## 10. Approved examples
**TBD.** Each example records the post file, template ID, exact prompt and settings, a written description of the approved image, and both captions.

## 11. Memory and adaptation
**TBD.** This is how the pipeline behaves like a handler: it keeps track of the past and decides the future.
- **Post history schema:** the fields logged for every post (see the `posts/index.md` columns): pillar, series and episode, topic, visual subject, composition, client named, fact IDs used, template, outcome
- **News inbox:** where the team drops real events and photos, and its format
- **No-repeat windows and caps,** checked against the history before choosing
- **Series continuity:** next episode, and when a series ends or gets refreshed
- **After launch:** metrics loop, with pillar weights adjusted only within bounds; brand fundamentals never change automatically; monthly human summary

---

## Changelog
| Date | Change | Evidence |
|---|---|---|
| 2026-10-04 | Skeleton created | — |
| 2026-10-04 | §2 draft with FACTS-v1 and PUBLIC-PROOF-v1; §3 widened to content strategy; §9 guardrails; §11 added | `brand/research.md` |

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
> **Audited 2026-10-04.** Website, LinkedIn About and Clutch were read in Chrome; raw evidence is in `brand/audit-raw.md` and the summary in `brand/research.md` → "Audit results". The handler's proposal for positioning, audiences and voice is `brand/strategy.md` (v1). It moves here once the user approves it.

**Company:** Verdant Soft (verdant-soft.com), a software company in Lahore, Pakistan, serving international clients. Client evidence so far: Australia, the Netherlands and Algeria.
**Service lines:** Custom Software Development · Cloud & DevOps · IT Team Outsourcing (dedicated teams) · UI/UX Design. Builds web and mobile applications.
**Goals of the accounts (user decision):** both Instagram and LinkedIn serve **brand, clients and talent**.
**Audiences, positioning, voice:** TBD, pending approval of `brand/strategy.md` §3–5.

### Fact bank
The pipeline may state a company fact **only if it appears below with `status: confirmed`**. Anything else, including facts that are true but not listed, must not be stated.
- `confirmed`: usable. The fact may be reworded, but names, numbers and scope words ("built", "contributed to", "modules") must stay as written.
- `pending`: waiting on the user. Don't state it.
- Case-study facts (F30–F39) never name a client. The case-study pages don't name one either.

<!-- id: FACTS-v2 -->
```yaml
- id: F01
  fact: "Verdant Soft is a software company based in Lahore, Pakistan."
  status: confirmed
  source: verdant-soft.com; clutch.co/profile/verdant-soft; linkedin.com/company/verdant-soft
- id: F02
  fact: "Verdant Soft offers custom software development, cloud & DevOps, IT team outsourcing (dedicated teams), and UI/UX design."
  status: confirmed
  source: verdant-soft.com (Services menu and service pages)
- id: F03
  fact: "Verdant Soft builds web and mobile applications."
  status: confirmed
  source: verdant-soft.com (site description)
- id: F04
  fact: "Verdant Soft's UI/UX process has six steps: research & discovery, user personas, architecture & wireframing, design & prototyping, testing & validation, implementation & iteration."
  status: confirmed
  source: verdant-soft.com/services/ui-ux-design
  note: "v2 corrects v1, which listed seven steps taken from search snippets."
- id: F05
  fact: "Verdant Soft works with the MERN stack and React, and lists Next.js, Vue, NestJS, Express, Django, Node.js, Python and PHP among its technologies, with MySQL, PostgreSQL, MongoDB, Amazon Aurora and SQLite databases."
  status: confirmed
  source: verdant-soft.com/services/custom-software; case-study pages; client testimonial on verdant-soft.com
- id: F06
  fact: "Verdant Soft's cloud & DevOps work covers AWS, Azure, Google Cloud, DigitalOcean and Alibaba Cloud; CI/CD with GitHub, GitLab, Bitbucket, Jenkins and CircleCI; Docker, Kubernetes and OpenShift; Terraform, CloudFormation and Ansible; and monitoring with Datadog, Prometheus, Grafana, Elasticsearch and Dynatrace."
  status: confirmed
  source: verdant-soft.com/services/cloud-devops
- id: F07
  fact: "Verdant Soft has delivered features for an AI SaaS platform."
  status: confirmed
  source: client testimonial on verdant-soft.com (P02)
- id: F08
  fact: "Verdant Soft was founded in 2019."
  status: pending        # stated only on Clutch (a field the company fills in); the site says "5+ Years of expertise"; user to confirm
  source: clutch.co/profile/verdant-soft
- id: F09
  fact: "Verdant Soft's tagline is: Engineering Tomorrow’s Tech Today!"
  exact_text: "Engineering Tomorrow’s Tech Today!"   # use this exact string (title case, curly apostrophe) wherever the tagline appears
  status: confirmed
  source: LinkedIn tagline and banner; Instagram bio; Clutch (sentence case). Not on the website.
- id: F10
  fact: "Verdant Soft's website is verdant-soft.com and its public email is info@verdant-soft.com."
  status: confirmed
  source: verdant-soft.com (footer, /hire-us, /contact-us)
- id: F11
  fact: "Prospective clients can book a meeting from the verdant-soft.com homepage, or start a project at verdant-soft.com/hire-us."
  status: confirmed
  source: verdant-soft.com ("Book a Meeting" opens a Calendly booking; "Hire an Expert" → /hire-us)
- id: F12
  fact: "Verdant Soft works on a milestone-based payment schedule, with payments at project initiation, key development phases, and final delivery."
  status: confirmed
  source: verdant-soft.com FAQ ("How do payments work?")
- id: F13
  fact: "Verdant Soft's IT team outsourcing comes as dedicated teams, project-based outsourcing, managed IT services, or offshore development, with full-time, part-time or project-based engagement."
  status: confirmed
  source: verdant-soft.com/services/it-team-outsourcing
- id: F14
  fact: "Verdant Soft describes its work as full-cycle: strategy, design, development and deployment."
  status: confirmed
  source: verdant-soft.com/blogs/design-to-deployment
- id: F15
  fact: "Clients can request a single service (for example DevOps, web development, UI/UX design or IT team outsourcing) rather than a full package."
  status: confirmed
  source: verdant-soft.com FAQ ("Can I request just one service?")
- id: F16
  fact: "Verdant Soft has 5+ years of expertise."
  status: confirmed
  source: verdant-soft.com homepage counter
- id: F17
  fact: "Verdant Soft has a verified client review on Clutch, rated 4.5 overall with 5.0 for quality, schedule, cost and willingness to refer."
  status: confirmed
  source: clutch.co/profile/verdant-soft (review dated 2024-10-26)
- id: F18
  fact: "Verdant Soft's social accounts: LinkedIn linkedin.com/company/verdant-soft, Instagram @verdant_soft."
  status: confirmed
  source: verdant-soft.com footer links

# Case studies (from verdant-soft.com/case-study/web/<slug>; no client names)
- id: F30
  fact: "Verdant Soft built the medications, allergies, visits and lab-orders modules of a healthcare management system for a psychiatrist and therapist clinic (Next.js, Node.js, Express, PostgreSQL)."
  status: confirmed
  source: /case-study/web/psychiatric-clinic
- id: F31
  fact: "Verdant Soft developed a role-based e-commerce CMS platform for managing the backend operations of online stores (Next.js, Node.js, NestJS, PostgreSQL)."
  status: confirmed
  source: /case-study/web/e-commerce
- id: F32
  fact: "Verdant Soft developed a real estate platform that simplifies the property transaction experience (React, Python, Django, MongoDB)."
  status: confirmed
  source: /case-study/web/real-estate
- id: F33
  fact: "Verdant Soft developed a zone-based parking application for managing parking sessions (React, Node.js, Express, PostgreSQL)."
  status: confirmed
  source: /case-study/web/parking-app
- id: F34
  fact: "Verdant Soft developed a VPN browser extension with subscription management (React, TypeScript)."
  status: confirmed
  source: /case-study/web/vpn-extension
- id: F35
  fact: "Verdant Soft built a digital platform for the dental industry that brings together patient services, professional education and digital consent management (Next.js, TypeScript, PostgreSQL)."
  status: confirmed
  source: /case-study/web/dental-care
- id: F36
  fact: "Verdant Soft built a real-time sync of products, collections and orders between a Shopify store and a Vue.js application."
  status: confirmed
  source: /case-study/web/shopify
- id: F37
  fact: "Verdant Soft developed a clinic management platform that streamlines clinic operations and patient booking (React, Node.js, NestJS, PostgreSQL)."
  status: confirmed
  source: /case-study/web/clinic-management
- id: F38
  fact: "Verdant Soft developed a browser-based design canvas inspired by tools like Figma, using Vue.js and Konva.js."
  status: confirmed
  source: /case-study/web/canvas
- id: F39
  fact: "Verdant Soft contributed to a scalable, multi-tenant integration platform for data synchronization and ETL workflows (Python)."
  status: confirmed
  source: /case-study/web/etl-management-system

# Self-reported numbers: NOT usable until the user confirms them (they disagree with each other across channels).
- id: F50
  fact: "500+ successful projects; 36+ active clients; 95% client satisfaction rate."
  status: pending        # homepage counters; conflicts with F51
  source: verdant-soft.com homepage
- id: F51
  fact: "50+ scalable & secure solutions; 1M+ global users reached; 69+ websites launched."
  status: pending        # LinkedIn post 2026-01-20; conflicts with F50
  source: linkedin.com/company/verdant-soft (post)
- id: F52
  fact: "Clients reduced monthly cloud costs by up to 40%."
  status: pending        # blog claim, no client or context named
  source: verdant-soft.com/blogs/cloud-optimization

# Never state: team size or headcount (a past LinkedIn post's figure contradicts Clutch's range), rates, minimum project size, employee reviews.
# Never quote: the case-study "The Process" text (identical boilerplate on every case study; mentions teams that aren't Verdant Soft's).
```

### Public proof
User decision: clients and testimonials that are **publicly available** may be used, **sparingly** (caps in §9). Rules for the pipeline:
- Quote **only** text that appears in an entry's `quote_verbatim` or `alt_quotes`, **character for character**. Never correct, trim inside or merge quotes. Each one is an exact substring of `full_text`, which is the testimonial as displayed.
- Use only entries with `status: quotable`. `reference-only` entries inform positioning but are never quoted. `pending-confirmation` and `pending-transcript` entries are never quoted.
- Print the `attribution` exactly. Never print star ratings.
- Proof caps (§9) count per **`client_key`**, not per entry. P01 and P04 are the same person.

<!-- id: PUBLIC-PROOF-v2 -->
```yaml
- id: P01
  client_key: shervin-khanzadi
  attribution: "Shervin Khanzadi, Director, Sweet Round Pty Ltd"
  context: "Chat system for AlgoRift, a platform for Amazon sellers (MVP, Aug–Oct 2024). Verified Clutch review."
  quote_verbatim: "Their dedication to maximizing value while managing costs truly set them apart."
  alt_quotes:
    - "Their project management was efficient and responsive, consistently delivering milestones on time."
    - "They quickly adapted to our needs, incorporating feedback seamlessly to ensure the final product aligned perfectly with our expectations."
  full_text: "see brand/audit-raw.md §11.1 (full review; long)"
  source: https://clutch.co/profile/verdant-soft
  status: quotable
- id: P02
  client_key: elia-essen
  attribution: "Elia Essen"
  context: "AI SaaS platform; MERN / React."
  quote_verbatim: "They took full ownership of our AI SaaS platform, delivering high-quality, scalable, and visually stunning features that exceeded our expectations."
  alt_quotes:
    - "Working with Verdant Soft has been an absolute pleasure."
  full_text: "Working with Verdant Soft has been an absolute pleasure. Their expertise in the MERN stack, especially React. js, is truly impressive. They took full ownership of our AI SaaS platform, delivering high-quality, scalable, and visually stunning features that exceeded our expectations."
  note: "Never quote the sentence containing 'React. js' (typo in the source)."
  source: https://www.verdant-soft.com/
  status: pending-confirmation   # no public link found between this name and an AI SaaS company; user to confirm client and company before it's quoted
- id: P03
  client_key: nick-kuijpers
  attribution: "Nick Kuijpers, CEO, Wemasy"
  context: "Wemasy: Dutch website-builder SaaS."
  quote_verbatim: "Verdant Soft has proven to be a highly supportive and reliable partner in the development of our company. Their team takes a thoughtful approach to analyzing issues and delivering effective solutions."
  alt_quotes:
    - "Verdant Soft has proven to be a highly supportive and reliable partner in the development of our company."
    - "Their team takes a thoughtful approach to analyzing issues and delivering effective solutions."
  full_text: "Verdant Soft has proven to be a highly supportive and reliable partner in the development of our company. Their team takes a thoughtful approach to analyzing issues and delivering effective solutions."
  source: https://www.verdant-soft.com/   # displayed as "CEO Wemasy"
  status: quotable
- id: P04
  client_key: shervin-khanzadi      # same person as P01
  attribution: "Shervin Khanzadi"   # name only: the site shows "CEO Alogirft" (typo for AlgoRift); Clutch shows "Director, Sweet Round Pty Ltd"; public profiles say founder of AlgoRift. User to confirm.
  context: "Front-end development."
  quote_verbatim: "Verdant Soft is a team of highly professional front-end developers with a strong and diverse skill set."
  alt_quotes:
    - "Their commitment to delivering high-quality results was evident throughout our collaboration."
  full_text: "Verdant Soft is a team of highly professional front-end developers with a strong and diverse skill set. Their commitment to delivering high-quality results was evident throughout our collaboration."
  source: https://www.verdant-soft.com/
  status: quotable
- id: P05
  client_key: hesham-elkouha
  attribution: "Hesham Elkouha"
  quote_verbatim: null
  alt_quotes: []
  full_text: "It was a pleasure working with Verdant Soft very professional and delivered the work as expected. Their response time was also amazing."
  note: "Run-on first sentence; the only clean sentence is weak on its own."
  source: https://www.verdant-soft.com/
  status: reference-only
- id: P06
  client_key: waqas-zahoor-pal
  attribution: "Waqas Zahoor Pal"
  context: "Emergency task."
  quote_verbatim: "The job was completed perfectly with full cooperation and professional conduct."
  alt_quotes: []
  full_text: "The job was completed perfectly with full cooperation and professional conduct. I never expected an emergency task to be handled this efficiently, but Verdant Soft demonstrated that with hard work and dedication, anything is possible."
  note: "The second sentence is not quoted (its ending reads as hype)."
  source: https://www.verdant-soft.com/
  status: quotable
- id: P07
  client_key: isana-sebastian
  attribution: "Isana Sebastian"
  quote_verbatim: "They quickly understood our problem, collaborated effectively with our team, and delivered a solid solution."
  alt_quotes:
    - "Their proactive communication, thoughtful suggestions, and flexibility made the process smooth."
    - "Working with Verdant Soft was a great experience."
  full_text: "Working with Verdant Soft was a great experience. They quickly understood our problem, collaborated effectively with our team, and delivered a solid solution. Their proactive communication, thoughtful suggestions, and flexibility made the process smooth."
  source: https://www.verdant-soft.com/
  status: quotable
- id: P08
  client_key: ben-kemboi
  attribution: "Ben Kemboi"
  quote_verbatim: "The team sought a clear understanding before starting the work."
  alt_quotes:
    - "Verdant Soft completed the work in a timely manner."
    - "They maintained positive communication and were ready to edit the work when asked to do so."
  full_text: "Verdant Soft completed the work in a timely manner. The team sought a clear understanding before starting the work. They maintained positive communication and were ready to edit the work when asked to do so."
  source: https://www.verdant-soft.com/
  status: quotable
- id: P09
  client_key: ilyes-abderrezak
  attribution: "Ilyes Abderrezak, Product Owner"   # from the video poster; LinkedIn post tags Nedjmati
  quote_verbatim: null
  alt_quotes: []
  full_text: null
  source: https://www.verdant-soft.com/ (video /videos/nedjimeti.mp4)
  status: pending-transcript
- id: P10
  client_key: unknown-video-1
  attribution: null
  quote_verbatim: null
  alt_quotes: []
  full_text: null
  source: https://www.verdant-soft.com/ (video /videos/alex-video-3.mp4)
  status: pending-transcript
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
> **Measured 2026-10-04** from verdant-soft.com (computed styles and logo files; `brand/audit-raw.md` §2–4).
> - **Brand source of truth:** the palette, type and logo below. Every overlay and template uses only these.
> - **Proposed, not yet approved:** moving social onto the website system and dropping the past royal-navy and yellow social templates (`brand/strategy.md` v1 §3).
> - **Not decided yet:** how the colours are worded in prompts. That waits for the Phase 1 tests.

### 5.1 Palette: two fixed colours, two themes
`[decided]` (user, 2026-10-04): **slate blue and sage teal stay exactly as they are.** Everything else is a theme colour and may change.
- Posts come in a **light** theme and a **dark** theme.
- The dark ground is a deep slate in the brand blue's own hue (H206), not the old royal navy (H219, very saturated).
- Every text pair below passes WCAG contrast. Machine-readable copy: `brand/brand-guide/project/tokens.json`.

<!-- id: PALETTE-v2 -->
```yaml
fixed:                       # identical in both themes; never altered
  slate-blue: "#416D95"
  sage-teal:  "#74AFAD"
  brand-gradient: "linear-gradient(102.32deg, #416D95, #74AFAD)"
light:                       # calm, airy, like the website
  bg:      "#F4F7F8"         # Mist
  surface: "#FFFFFF"         # cards, panels
  ink:     "#13212C"         # headlines, 15.2:1 on bg
  body:    "#3E4C58"         # copy, 8.2:1
  muted:   "#66737E"         # caption line, 4.5:1
  line:    "#DDE5E9"
  highlight: slate-blue      # 5.1:1; sage-teal is never text on light (2.3:1)
  logo: verdant-logo-gradient
dark:                        # focused, technical
  bg:      "#0E1A23"         # Deep Slate
  surface: "#162632"
  ink:     "#F1F5F7"         # 16.1:1 on bg
  body:    "#B6C3CC"         # 9.8:1
  muted:   "#8494A0"         # 5.6:1
  line:    "#26394A"
  highlight: sage-teal       # 7.1:1; slate-blue text only at 24px+ (3.2:1); gradient text allowed at 24px+
  logo: verdant-logo-white
on-fills: { on-slate-blue: "#FFFFFF", on-sage-teal: "#13212C" }   # never white on sage teal (2.5:1)
never: [green as the brand colour, yellow, royal navy, pure black grounds]
```

`[proposed]` **Theme by pillar** (about 4 light and 3 dark a week):
- **Dark:** Engineering insight (Mon, Wed) and Brand world (Sat).
- **Light:** How we work (Tue, Sun), Proof (Thu) and Grow with us (Fri).

**Prompt wording:** TBD, being tested in `posts/2026-10-04-direction-test-built-to-scale.md`. Hypothesis: name the colours with their hex codes ("muted slate blue (#416D95)", "soft sage teal (#74AFAD)") and never say "green".

### 5.2 Typography (overlays only; the model never renders brand text)
<!-- id: TYPE-v1 -->
```yaml
family: "Inter"            # the site self-hosts it; open-source (SIL OFL), so the pipeline can bundle it
headline: { weight: 700, colour: ink, highlight: gradient }
subhead:  { weight: 600, colour: ink }
body:     { weight: 500, colour: body }
small:    { weight: 400, colour: muted }
letter_spacing: normal
case: "sentence case, as on the site; never all caps"   # [proposed]: past social used all-caps templates
signature: "set 1–3 key words of a headline in `highlight` (light: slate-blue; dark: sage-teal or gradient text); the rest in ink"
```

### 5.3 Logo files (`brand/assets/`)
| Use | File | Notes |
|---|---|---|
| Light background, full lockup | `verdant-green-logo.8bcaebdb.svg` | Gradient VS mark + "Verdant Soft". Embedded PNG, 852×204. Keep it ≤ ~400 px wide on a 1080 px post |
| Dark background, full lockup | `verdant-white-logo.e0d6cd95.svg` | All white. Embedded PNG, 4096×981 |
| Mark only, white | `VS.05a1a937.svg` | The only true vector file |
| Mark only, gradient | `VS-Green.770a6db3.svg`, `VerdantLogoLeft.ee8822eb.png` | PNG 2160×2160 (the Left file has the mark offset in a transparent square) |
| Small icon | `apple-touch-icon.png` (180×180), `favicon.png`, `favicon.ico` | Gradient mark |

Gap: there are no vector lockup files. Ask the team for source files (SVG, AI or Figma) before the overlay spec is final.

### 5.4 Brand motifs from the website (candidates for templates; untested)
- Headline words highlighted in the gradient (§5.2 signature).
- An oversized, cropped, faint VS mark as a background shape (site footer). It's an overlay asset, not generated.
- A fine grey-blue line-and-node mesh (site hero).
- Generous open space with rounded `surface` panels, in the light (Mist) or dark (Deep Slate) theme (§5.1).

### 5.5 Still TBD
- **Fixed elements** (never vary): lighting, medium/style, mood
- **Variable elements** (vary daily within limits): subject, setting, composition, metaphor
- Composition and negative-space zones reserved for overlays
- Text-in-image policy (what the model may render vs. what is overlaid)
- Overlay spec: logo position and size, headline position, safe margins

## 6. Image prompt system
**TBD.**
- `[decided]` **Aspect ratio:** Google Flow offers Nano Banana 2 only 1:1, 16:9, 9:16, 4:3 and 3:4 (no 4:5). Generate at **3:4**, end every prompt with "Portrait image, 3:4 aspect ratio.", and crop deterministically to the 4:5 post (1080×1440 → 1080×1350, 45px off the top and bottom). The API pipeline uses the same 3:4 + crop, for parity. Evidence: Flow error, 2026-10-04.
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
- `[decided]` **Public proof, used sparingly:** quote only `quote_verbatim` or `alt_quotes` text from §2 `PUBLIC-PROOF` with `status: quotable`, character for character. `[proposed]` caps: at most **1 proof post per week**, and the **same `client_key` not again within 30 days**.
- `[proposed]` **No self-reported numbers:** project counts, client counts, satisfaction rates, user reach or savings percentages are stated only once they appear in §2 `FACTS` as `confirmed`. Today none do (F50–F52 are pending).
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
| 2026-10-04 | §6: generate at 3:4 and crop to 4:5 (Flow has no 4:5) | Flow error message |
| 2026-10-04 | §5 → PALETTE-v2: slate blue and sage teal fixed (user decision); light and dark themes with new neutrals; theme-by-pillar proposed | User decision; contrast computed |
| 2026-10-04 | Audit: §2 → FACTS-v2 (tagline confirmed, UI/UX process corrected to 6 steps, contact/CTA/payment/engagement facts, 10 case studies, self-reported numbers held as pending) and PUBLIC-PROOF-v2 (verbatim quotes; 6 quotable entries from 5 clients; `client_key` so caps count per person; P01 and P04 are one client; P02 held until the client is confirmed). §5 palette, type and logo files measured from the website. §9 proof cap per `client_key`; no self-reported numbers | `brand/audit-raw.md`, `brand/research.md` → Audit results |

# Social Media Style Guide

> **Status: DRAFT, not production-ready.** Sections marked **TBD** are not yet proven. The pipeline must not run until every TBD is gone and the blind test (see `README.md`, phase 4) has passed.
>
> **Audience:** an automated agent that creates and publishes one post per day to Instagram and LinkedIn with no human editing. Every rule here must be followable as written. If an agent has to guess, the guide has a gap.
>
> **Verbatim blocks** are fenced code blocks preceded by `<!-- id: NAME-vN -->`. The pipeline copies them exactly.

---

## 1. How the pipeline uses this guide
**TBD.** The daily procedure, in order. Steps 0–4 run **the day before** the post (D−1); steps 5–11 run on the day.

0. **Research the post the day before** `[decided]` (user, 2026-10-06). On D−1:
   - Decide tomorrow's slot and topic (steps 1–3).
   - Re-open every source the post will cite, and confirm the claim and numbers are unchanged and the page is live.
   - Search primary sources for newer developments on the topic. Add 1–3 new trend items to the bank.
   - Run a sensitivity check: is there any news, outage, tragedy or national moment that would make tomorrow's post wrong?
   - Record the results in the post file's **Research** section (`posts/_template.md`).
   - Decide: go / update / swap to evergreen / hold. A post with no D−1 research is not published.
1. **Read memory:** the post history (`posts/index.md` schema, §11), the news inbox (`inbox/`), the source banks (`banks/`), and today's calendar moments
2. **Decide today's post** using `CONTENT-MIX-v1` (§3): today's slot, then the priority inbox > calendar > timely trend item > series episode > evergreen, while respecting the Verdant band, caps and no-repeat windows (§3, §9, §11)
3. Pick the topic and its facts (Verdant facts only from §2 `FACTS` and `PUBLIC-PROOF`; external facts only from checked, unexpired bank items under §2.3 `EXTERNAL-SOURCES-v1`)
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
**Audiences and voice:** `[decided]` (user, 2026-10-06): `brand/strategy.md` v2 §4–5. External content (Tech, Explained) is written for founders and decision-makers; Grow with us is for talent. Caption-level rules are in §7. **Positioning** (strategy §3) is still a proposal.

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

### 2.3 External sources (Tech, Explained) `[decided]` (user, 2026-10-06)
70% of posts are about the wider tech world, so the pipeline needs a second fact bank with its own rules. External facts come **only** from checked, unexpired items in `banks/trends.md` (timely) or `banks/topics.md` (evergreen). An item is `checked` only once its primary source page was opened and the claim was found on it. Items tagged `[decided · CD]` are calls the user delegated to the creative director.

<!-- id: EXTERNAL-SOURCES-v1 -->
```yaml
scope: "every fact, number, quote or claim in a post that is not about Verdant Soft"
allowed_sources:                     # primary only
  - "the official blog, docs, changelog or press release of the organisation that made or measured the thing"
  - "a research paper, read at the authors' own page or arXiv"
  - "the original survey or report, on the publisher's own results page"
  - "standards bodies and official statistics offices"
not_allowed:
  - "an article, newsletter or social post reporting someone else's number (second-hand)"
  - "statistics roundup or aggregator sites"
  - "AI-generated summaries, including search-result snippets"
  - "any page the researcher could not open and read in full"
stats_max_age_years: 2               # from the source's publication date
checked_means: "the primary page was fetched and the claim appears on it, in substance; numbers exactly"
claims:
  - "say only what the source says; no extrapolation, no rounding up, no 'up to' unless the source says it"
  - "attribute every number in the same sentence or on the same slide"
citation:
  image: "Source: {source_name}, {YYYY}"                     # meta line on any post or slide that states a sourced fact
  linkedin_caption: "Source: {source_name} · {source_url}"   # last line before the hashtags  [decided · CD]
  instagram_caption: "Source: {source_name}"                 # links aren't clickable on Instagram  [decided · CD]
  roundup: "one source line on each item slide; every source listed in the LinkedIn caption"
naming:
  allowed: "name companies, products and models in text when they are the subject; neutral and factual"
  banned:
    - "third-party logos, trademarks or product UI in images"
    - "verdicts or comparisons (X is better than Y)"
    - "implying a partnership, endorsement or client relationship"
    - "speculation about unreleased products or rumours"
verdant_boundary:
  - "never present a trend, a third-party result or a public case as Verdant Soft's experience"
  - "'In our builds…' only when a FACTS entry with status: confirmed backs it; record the F-id in the post file"
  - "the Verdant take is advice or opinion by default ('What we'd tell a founder: …')"
expiry:
  trend_item: "published + 14 days"
  evergreen_number: "re-check the source every 12 months; retire it once older than stats_max_age_years"
banks: { trends: banks/trends.md, evergreen: banks/topics.md, inbox: inbox/ }
item_schema:                          # trend items; evergreen numbers use the same source fields
  id: "T-YYYY-MM-DD-NN (date of the drop)"
  lane: "trends | ai | concepts | numbers | startup"
  claim: "one sentence, exactly what the source supports"
  why_it_matters_to_founders: "one sentence"
  source_name: "publisher as it should appear on the image"
  source_url: "the primary page"
  source_type: "official | paper | report | standards"
  published: "YYYY-MM-DD"
  retrieved: "YYYY-MM-DD"
  expires: "YYYY-MM-DD"
  status: "pending-check | checked | used | expired | rejected"   # only checked items may be used in posts
  take_hint: "the founder-facing angle for our take"
```

## 3. Content strategy: pillars, rotation, series, inputs, calendar
`[decided]` (user, 2026-10-06). The reasoning is in `brand/strategy.md` v2 §6–9. Items tagged `[decided · CD]` were delegated to the creative director. The calendar of moments (strategy §9) still needs the user's pick of which moments get posts.

<!-- id: CONTENT-MIX-v1 -->
```yaml
mix:
  verdant_share: { target: 0.30, band: [0.25, 0.40], period: calendar-month }
  external_pillar: "Tech, Explained"             # 5 lanes, ~70%
  carousels: "7 of every 21 posts, fixed 3-week cycle; the rest are single posts"
calendar:
  anchor_monday: "2026-10-12"                    # practice anchor; reset to the launch Monday
  week_index: "n = floor((date - anchor_monday) / 7 days)"
  week_type: "A if n is even, else B"
  cycle_week: "(n mod 3) + 1"
  days:
    Mon: { lane: trends,   series: "This Week in Tech", format: carousel, timely: always }
    Tue: { A: how-we-work, B: build-notes,  format: "carousel in cycle week 2, else single" }
    Wed: { lane: ai,       series: "AI, Explained",     format: "carousel in cycle week 1, else single" }
    Thu: { A: proof,       B: grow-with-us, format: single }
    Fri: { lane: startup,  series: "Founder Notes",     format: "carousel in cycle week 3, else single" }
    Sat: { lane: numbers,  series: "By the Numbers",    format: single }
    Sun: { lane: concepts, series: "Under the Hood",    format: "carousel in cycle week 3, else single" }
  carousel_days: { 1: [Mon, Wed], 2: [Mon, Tue], 3: [Mon, Fri, Sun] }
lanes:
  trends:   { name: "Trends & news",            audience: founders, series: "This Week in Tech" }
  ai:       { name: "AI & LLMs",                audience: founders, series: "AI, Explained" }
  startup:  { name: "Startup & product advice", audience: founders, series: "Founder Notes" }
  numbers:  { name: "Facts & numbers",          audience: founders, series: "By the Numbers" }
  concepts: { name: "Software concepts",        audience: founders, series: "Under the Hood" }
verdant_pillars:
  how-we-work:  { series: ["Outsourcing, Decoded", "Wireframe → Production"], rule: "alternate by episode; on a carousel day use Wireframe → Production" }
  build-notes:  { series: ["Build Notes"], source: "F05–F06, F30–F39 only" }
  proof:        { series: ["Client words", "Project Spotlight"], rule: "alternate; same client_key not within 30 days" }
  grow-with-us: { series: ["Grow at Verdant"], rule: "inbox first; otherwise conceptual, no AI-generated people" }
  brand-world:  { slot: none, rule: "calendar moments and milestones only" }
timely:
  target: "about half of external posts: 2–3 a week"
  rule: "Mon always uses trend items. Wed, Fri, Sat and Sun use a checked, unexpired trend item for their lane when one exists, at most 2 of them a week; otherwise evergreen"
priority: [inbox, calendar_moment, timely_trend_item, series_episode, evergreen]
overrides:
  inbox_or_moment: "replaces that day's external post, never a Verdant slot"
  bumped_evergreen: "moves to the next free external slot"
  bumped_trend: "expires, unless the next Monday roundup can still use it"
  verdant_band_guard: "if an inbox item would push the month's Verdant share above 0.40, it queues"
  inbox_max_per_day: 1
ctas:
  direct: { text: "Book a call at verdant-soft.com", allowed_on: [how-we-work, proof], max_per_week: 2 }
  soft:   { external: ["save this", "follow the series"], grow-with-us: ["follow", "see open roles (inbox roles only)"], build-notes: ["save this", "follow the series"] }
endings:
  question_share: "about 1 in 3 posts; a specific question a founder can answer from experience; never 'Thoughts?'"
no_repeat:                                       # [decided · CD]
  lane_topic_days: 90
  trend_item: "never twice; one follow-up explainer in another lane is allowed"
  company_as_main_subject_per_week: 2
  headline_formula: "never the same formula three days running; never the same opening word two days running"   # revised 2026-10-06: the stricter version capped problem/curiosity below the user's 60%
  proof_client_key_days: 30
research:
  saturday_run: "every Saturday 09:59 PKT: 3–5 checked trend items into banks/trends.md; marks expired items"
  daily_run: "from launch: 1–3 items a day plus major breaking news; the Saturday run then picks the week's best 3–5 for Monday"
  evergreen_refresh: monthly
  pre_post: "D-1 [decided, user 2026-10-06]: the day before every post, re-open its sources, check for newer developments and sensitivity, log it in the post file's Research section, then go / update / swap / hold. No D-1 research, no publish. Monday's roundup is researched on Sunday, from the Saturday drop."
```

## 4. Post formats
Copy recipes per lane, `[decided]` where the Decisions table in `learnings/log.md` (2026-10-06) says so. Structures are **draft v0** under test in writing round 2 (`writing/round-02-lane-packs.md`). Templates, moods and visuals are **TBD at the visuals stage**.

| Lane / pillar | Series | Format | Headline default | On-image text | Take | CTA |
|---|---|---|---|---|---|---|
| trends | This Week in Tech | carousel (roundup variant) | curiosity ("What changed for founders this week") | pill, headline, one item per slide with its source line | "Our take" slide | soft: follow for next Monday |
| ai | AI, Explained | carousel in cycle week 1, else single | problem/curiosity ("Why AI [makes things up]") | pill, headline, subline; one term defined | caption "Our take:" (single) or slide (carousel) | soft |
| startup | Founder Notes | carousel in cycle week 3, else single | problem/curiosity or imperative | pill, headline, subline | as above | soft |
| numbers | By the Numbers | single | plain fact: the number is the hero ("[N%] of {who} {do what}", number from a checked bank item) | pill, the number, one line of context, **source line** | caption "Our take:" | soft |
| concepts | Under the Hood | carousel in cycle week 3, else single | problem/curiosity ("What an API [actually is]") | pill, headline, subline; one term defined | as above | soft |
| how-we-work | Outsourcing, Decoded / Wireframe → Production | carousel in cycle week 2, else single | rhythm or plain benefit | pill, headline, subline | — | **direct** |
| build-notes | Build Notes | carousel in cycle week 2, else single | imperative lesson or problem | pill, headline, subline | — | soft |
| proof | Client words / Project Spotlight | single | the client's words are the headline (verbatim) | quote, attribution | — | **direct** |
| grow-with-us | Grow at Verdant | single | warm opinion or imperative | pill, headline, subline | — | soft |

**Single-post anatomy (copy):**
- series pill (2–4 words)
- headline: ≤ 8 words, sentence case, one highlight of 1–3 words
- optional subline: ≤ 12 words
- source line if a sourced fact appears
- the logo

Nothing else goes on the image.

### 4.1 Carousels (v2, 2026-10-06)
Adapted from the user's carousel checklist and *The Carousel Playbook* (@adarshxdesign). The full reasoning is in `writing/carousel-playbook.md`. The worked example `writing/carousel-01-before-the-code.md` is **approved by the user as the model** for Verdant carousels.

v2 adds two variants, **external** and **roundup**, for Tech, Explained. v1 is in git history (commit 740ca9f).

<!-- id: CAROUSEL-v2 -->
```yaml
length: { min: 6, max: 8 }
variants:
  verdant:   # how-we-work, build-notes, proof material
    order: [cover, payoff, step x1-4, proof, cta, receipt]
  external:  # ai, startup, concepts
    order: [cover, payoff, step x1-3, our-take, action, receipt]
  roundup:   # trends, every Monday ("This Week in Tech")
    order: [cover, item x3-5, our-take, receipt]   # the our-take slide carries the soft action line
slides:
  - { role: cover,    job: "open a loop: claim + tension, never the answer", headline_max_words: 8, subline_max_words: 8, extras: [swipe-cue, series-pill], drives: swipe-rate }
  - { role: payoff,   job: "why it matters to the reader + first real answer; a second cover", headline_max_words: 6, body_max_words: 35, drives: dwell }
  - { role: step,     job: "one idea per slide; end with a bridge line", headline_max_words: 6, body_max_words: 30, bridge_max_words: 8, drives: completion }
  - { role: item,     job: "one trend item: what happened + why it matters to founders + source line", headline_max_words: 8, body_max_words: 30, extras: [source-line], drives: completion }
  - { role: proof,    job: "a fact (FACTS), case study (F30–F39) or verbatim client quote (PUBLIC-PROOF)", drives: trust }
  - { role: our-take, job: "the Verdant take: what we'd tell a founder; experience only if FACTS backs it", headline_max_words: 6, body_max_words: 30, drives: trust }
  - { role: cta,      job: "one direct action (verdant variant only)", headline_max_words: 6, drives: action }
  - { role: action,   job: "one soft action: save this | follow the series", headline_max_words: 6, drives: follows-and-saves }
  - { role: receipt,  job: "the carousel in one savable frame + soft CTA line + logo", list_max_items: 6, drives: saves-and-shares }
copy:
  highlight: "1–3 words per slide"
  text_levels_max: 3
  body_min_px_at_1080: 32
  numbers: "only as step counters, from FACTS with status confirmed, or from a checked unexpired bank item with its source line on the same slide"
  terms: "external variants define one technical term in one line, plain language"
  alt_text: "one plain sentence per slide (Instagram); LinkedIn document title = cover headline"
cta:
  allowed: ["book a call at verdant-soft.com (how-we-work and proof material only)", "follow the series", "save this"]
  banned: ["comment KEYWORD for a DM (needs a human responder)", "engagement bait", "more than one action per slide", "a direct sales CTA on Tech, Explained carousels"]
hooks:
  default: "problem/curiosity, about 60% of covers; other formulas fill the rest"
  rule: "a claim, not a topic; one tension word (costing, breaks, quietly, before, nobody, stop, wrong); must be true for us to say"
  banned: ["invented statistics or percentages", "fake experiments (I tested X for 30 days)", "creator bragging"]
  formulas: see writing/carousel-playbook.md §3 (25 formulas in 5 families)
design:
  mood: "one theme + mood for the whole carousel; lane → mood mapping TBD at the visuals stage (THEMES-v1 maps the old pillars)"
  cover: "carries the colour mass and hero visual"
  inner: "text-led, small motif"
  fixed_positions: { logo: top-left, counter: top-right "02 / 08", dots: bottom-right, footer: bottom-left, source_line: "above the footer" }
  format: "4:5, 1080x1350; LinkedIn = PDF document, Instagram = image carousel"
checklist:   # all must pass; any fail = revise
  - "hook: slide 1 is a claim + tension, ≤8 words, makes you swipe"
  - "one clear idea, graspable in 3 seconds"
  - "structure: the variant's order, 6–8 slides"
  - "every slide teaches, explains, proves or moves forward"
  - "every step slide ends with a bridge"
  - "readable: body ≥32 px, ≤30 words"
  - "hierarchy: obvious read order; one highlight per slide"
  - "minimal: nothing without a job; ≤1 visual per slide"
  - "consistent: one mood, one type scale, fixed positions"
  - "receipt slide worth saving on its own"
  - "one clear action on the second-last slide (roundup: on the our-take slide), soft repeat on the last"
  - "true: every claim in FACTS, PUBLIC-PROOF or a checked unexpired bank item; quotes verbatim; sources on the slide; no invented numbers"
  - "voice: no buzzwords; engineer talking to a founder"
  - "theme: mood matches the lane; contrast and automatic image checks pass"
three_second_test: [readable without trying, one focal point, a claim not decoration, "≤8 words", you would stop scrolling, true for us to say]
```

## 5. Visual identity
> **Measured 2026-10-04** from verdant-soft.com (computed styles and logo files; `brand/audit-raw.md` §2–4).
> - **Brand source of truth:** the palette, type and logo below. Every overlay and template uses only these.
> - **Proposed, not yet approved:** moving social onto the website system and dropping the past royal-navy and yellow social templates (`brand/strategy.md` v1 §3).
> - **Not decided yet:** how the colours are worded in prompts. That waits for the Phase 1 tests.

### 5.0 Post rules (user, 2026-10-04) `[decided]`
Every post is:
1. **Minimal.** One strong visual, lots of clean space, no clutter or busy effects.
2. **Professional.**
3. **Premium.**
4. **Visually attractive.** Full use of colour and the brand gradient.
5. **Built around a visual.** Never text alone on a flat background, except Proof quote cards.
6. **Readable.** High-contrast text on a clean area, legible on a phone.
7. **Designer-made.** Every post and every carousel slide looks like a professional graphic design team made it: a deliberate grid, consistent margins, a clear type hierarchy, nothing that looks template-generated or AI-generic.

These are binary checks in the QA rubric (§8).

### 5.1 Colour system v8: palette + two themes × four moods
- `[decided]` (user): **slate blue and sage teal stay exactly as they are**; the palette grew from the user's references (v6), then became a full theme system.
- **v8 (2026-10-05) came from three independent designer proposals and Claude's synthesis.** Light posts stay light: their colour mass is a bright mid-tone (Royal Tide / Lagoon Tide), never a dark cobalt block.
- **The highlight and pill colours were fixed** after the old Ocean end failed contrast: Ocean was 3.3:1 on the darkest light ground, and white text on it was 4.1:1.
- **The pillar picks the mood.** Note (2026-10-06): the pillar → mood mapping in THEMES-v1, `colours.py WEEK` and the colour book predates the 30/70 content mix and its five external lanes (§3). The lane → mood mapping is decided at the visuals stage; no colours change now.
- **Source of truth:** `brand/theme/colours.py`. Book: `brand/guidelines/verdant-soft-colour-guidelines.pdf` (25 pages).

<!-- id: PALETTE-v8 -->
```yaml
palette:
  core:
    slate-blue: "#416D95"
    sage-teal: "#74AFAD"
  deep:
    abyss: "#050816"
    navy: "#1E3058"
    cobalt-night: "#151754"
    teal-night: "#061A22"
  blues:
    electric-royal: "#2457D6"
    royal-blue: "#3C6EB7"
    steel-navy: "#42658A"
    sky: "#A6CAEC"
  teals:
    deep-lagoon: "#00727F"
    deep-ocean: "#007A9E"
    ocean: "#0088AA"
    lagoon: "#00ACB3"
    cyan: "#09CACC"
    mint-jade: "#34CCA4"
  lights:
    mist: "#F5F9FD"
    ice: "#EBF5F7"
    polar: "#E9FFFC"
    white: "#FFFFFF"
  brand-gradient: ["#416D95", "#74AFAD"]   # logo + accent bar on every post
  retired: { royal-deep: "#2F62C8" }
```

<!-- id: THEMES-v1 -->
```yaml
moods:
  light-royal:
    name: Light Royal
    theme: light
    pillars: How we work (Tue, Sun) · Proof (Thu)
    ground: ['#F5F9FD', '#E8F0F8', '#DAE6F2']
    ground_glow: ['#E9FFFC', 70, top-left]
    surface:
      fill: '#FFFFFF'
      border: '#C9DCEC'
      shadow: ['#1E3058', 8, 8, 24]
    raised:
      fill: white 88% glass
      border: '#FFFFFF'
      shadow: ['#1E3058', 16, 24, 60]
    mass: ['#2457D6', '#3C6EB7']
    mass_name: Royal Tide
    mass_glows:
    - ['#09CACC', 40, centre-right]
    - ['#A6CAEC', 30, top edge sheen]
    mass_shadow: ['#2457D6', 28, 30, 70]
    mass_edge: null
    headline: '#050816'
    supporting: '#42658A'
    meta: '#42658A'
    highlight: ['#2457D6', '#007A9E']
    pill: ['#2457D6', '#007A9E']
    pill_text: '#FFFFFF'
    lines: '#C9DCEC'
    logo: gradient lockup
    text_on_mass: '#FFFFFF'
  light-lagoon:
    name: Light Lagoon
    theme: light
    pillars: Grow with us (Fri)
    ground: ['#F2FAFA', '#E3F3F3', '#D2EBEC']
    ground_glow: ['#E9FFFC', 70, top-left]
    surface:
      fill: '#FFFFFF'
      border: '#BFDDE0'
      shadow: ['#062A33', 8, 8, 24]
    raised:
      fill: white 88% glass
      border: '#FFFFFF'
      shadow: ['#062A33', 14, 24, 60]
    mass: ['#00727F', '#0088AA', '#00ACB3']
    mass_name: Lagoon Tide
    mass_glows:
    - ['#34CCA4', 35, centre]
    - ['#E9FFFC', 30, top edge sheen]
    mass_shadow: ['#00727F', 26, 30, 70]
    mass_edge: null
    headline: '#050816'
    supporting: '#42658A'
    meta: '#42658A'
    highlight: ['#007A9E', '#00727F']
    pill: ['#00727F', '#007A9E']
    pill_text: '#FFFFFF'
    lines: '#BFDDE0'
    logo: gradient lockup
    text_on_mass: '#FFFFFF'
  dark-royal:
    name: Dark Royal
    theme: dark
    pillars: Engineering insight (Mon, Wed)
    ground: ['#050816', '#0A1030', '#12164A']
    ground_glow: ['#21387B', 60, top-left]
    surface: {fill: '#0B1530', border: '#1C2B4E', shadow: null}
    raised: {fill: white 8% glass, border: Polar 12% inner top edge, shadow: null}
    mass: ['#0B1A3A', '#21387B', '#2457D6']
    mass_name: Royal Aurora
    mass_glows:
    - ['#09CACC', 35, centre-right]
    - ['#3C6EB7', 40, top-right]
    mass_shadow: null
    mass_edge: ['#E9FFFC', 25]
    headline: '#FFFFFF'
    supporting: '#A6CAEC'
    meta: '#74AFAD'
    highlight: ['#A6CAEC', '#09CACC']
    pill: ['#09CACC']
    pill_text: '#050816'
    lines: '#1C2B4E'
    logo: white lockup
    text_on_mass: '#FFFFFF'
  dark-lagoon:
    name: Dark Lagoon
    theme: dark
    pillars: Brand world (Sat)
    ground: ['#040C12', '#061A22', '#08262F']
    ground_glow: ['#0088AA', 35, top-left]
    surface: {fill: '#0A2028', border: '#163A42', shadow: null}
    raised: {fill: white 8% glass, border: Polar 12% inner top edge, shadow: null}
    mass: ['#062A33', '#00727F', '#0088AA']
    mass_name: Lagoon Aurora
    mass_glows:
    - ['#34CCA4', 35, centre]
    - ['#09CACC', 30, top-right]
    mass_shadow: null
    mass_edge: ['#E9FFFC', 25]
    headline: '#FFFFFF'
    supporting: '#74AFAD'
    meta: '#A6CAEC'
    highlight: ['#09CACC', '#34CCA4']
    pill: ['#34CCA4']
    pill_text: '#050816'
    lines: '#163A42'
    logo: white lockup
    text_on_mass: '#FFFFFF'
week:
- {day: Mon, mood: dark-royal, pillar: Insight}
- {day: Tue, mood: light-royal, pillar: How we work}
- {day: Wed, mood: dark-royal, pillar: Insight}
- {day: Thu, mood: light-royal, pillar: Proof}
- {day: Fri, mood: light-lagoon, pillar: Grow with us}
- {day: Sat, mood: dark-lagoon, pillar: Brand world}
- {day: Sun, mood: light-royal, pillar: How we work}
gates:
  light: [Mean luminance of the image at least 0.55, At most 6% of pixels darker than luminance 0.10, 'No fill darker than the mood’s darkest
      mass stop, except text']
  dark: [Mean luminance of the image at most 0.15, At least 2% of pixels brighter than luminance 0.50 (the glow), Glow and highlight together
      cover at most 25% of the frame]
rules: ['exactly one colour mass per post, 25–40% of the frame', highlight on 1–3 words, 'accent bar = brand gradient #416D95 → #74AFAD', 'light
    posts: no Cobalt Night, Navy or Abyss fills', 'dark posts: no drop shadows; edges and glow', 'shadows and borders tinted, never grey', no
    two consecutive posts share theme + mood]
```

### 5.1a Light theme v2: the system (user: "build the overall theme")
- One grid, one component kit and seven templates. Every light post is built from these, never designed from scratch.
- Reference sheets: `brand/theme/light-1-anatomy.png`, `light-2-templates.png`, `light-3-rules.png`. Regenerate them with `python3 brand/theme/render_light.py`.
- The mockups use a stand-in font. The real headline face is Inter (Syne for headlines is still an open question).

> **Colours superseded by THEMES-v1 (§5.1):** the light colour mass is now the mood's Tide (Royal or Lagoon), not Cobalt, and the highlight and pill use the v8 gradients. The layout and components below still apply.

<!-- id: LIGHT-THEME-v2 -->
```yaml
canvas: { size: "1080x1350 (4:5)", generate_at: "3:4, crop to 4:5", safe_x: 84, safe_y: 110 }
ground: "tinted ice gradient #F4F9FC → #E6F1F8 → #D6E7F4 with a polar #E9FFFC glow top-left; never flat white"
components:
  logo:      "real gradient lockup (REF-PACK-v1), top-left at safe_x/safe_y, 52 px tall"
  pill:      "label pill: gradient #2F62C8 → #0088AA, white bold 26 px, names the series or topic"
  headline:  "bold 88–100 px, abyss #050816, max 3 lines, sentence case, left-aligned"
  highlight: "1–3 words in gradient #2F62C8 → #0088AA (≥4:1 on the ground)"
  accent:    "bar 110×10, gradient royal → cyan, under the headline"
  subline:   "one line, 32 px regular, steel #42658A"
  block:     "EXACTLY ONE saturated colour block per post: cobalt #151754 → #21387B → royal #3C6EB7, cyan #09CACC glow inside, radius 44, soft royal shadow, bleeds off an edge"
  hero:      "one object inside the block: glossy gradient bars | node network | glass stack | quote mark | real photo frame"
  glass:     "frosted panels (white 20–55%, thin white edge); on or near the block only; max 3"
  list_row:  "glass row, gradient number disc, bold 40 px text; max 4 rows"
  counter:   "carousel '02 / 05' top-right in steel; progress dots bottom-right (active = gradient bar)"
  footer:    "verdant-soft.com, bold 24 px, steel (white when it sits on the block)"
templates:
  L-HERO:   { use: [how-we-work, brand-world], layout: "text top-left; block lower-right with hero object" }
  L-GLASS:  { use: [how-we-work], layout: "text top-left; block lower-right with a stack of up to 3 glass cards" }
  L-QUOTE:  { use: [proof], layout: "block top-right holding the quote mark; verbatim quote 60–64 px below; 1–3 words highlighted; attribution in steel" }
  L-LIST:   { use: [how-we-work, insight], layout: "text top-left; 3–4 glass list rows; block as a bottom band carrying the footer" }
  L-COVER:  { use: [series, carousel-cover], layout: "pill with series + episode; question headline; block lower-right; progress dots" }
  L-SLIDE:  { use: [carousel-inner], layout: "counter top-right; short headline; block as the content panel with glass rows; dots" }
  L-PEOPLE: { use: [grow-with-us], layout: "text top-left; block lower-right holding a REAL inbox photo in a white-edged frame; name + role" }
rules:
  do: ["one colour block with a job", "one hero object", "gradient highlight on 1–3 words", "pill names the series or topic", "real people only from real photos"]
  dont: ["cyan/mint/sage/polar as text on light", "two blocks", "gradient text in body or subline", "centred headline over the hero", "stock people, robots, generic tech icons", "yellow, lime, orange, coral, green-as-brand", "text inside the block under 36 px", "bokeh, sparkles, lens flares"]
```

`[proposed]` **Theme and mood by pillar:** see `THEMES-v1` → `week` (Mon/Wed Dark Royal · Tue/Thu/Sun Light Royal · Fri Light Lagoon · Sat Dark Lagoon).

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

### 5.5 Text and logo policy
- `[decided]` (user, 2026-10-04): **posts are generated complete.** The model renders the headline, subline and URL (exact quoted text) and places the logo from a fixed reference image (**REF-PACK-v1**: `brand/brand-guide/png/verdant-logo-gradient.png` for light posts).
- Every output is checked for exact spelling and logo fidelity.
- If text or logo accuracy fails repeatedly, fall back to generating the background and overlaying the text and logo (principle 5).

### 5.6 Still TBD
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
`[decided]` rules come from the user (2026-10-06); `[decided · CD]` were delegated to the creative director. **Templates and few-shot examples stay TBD** until writing practice passes two consecutive rounds at ≥ 80% keep, with no truth or voice failures. Round 2 is `writing/round-02-lane-packs.md`.

**Decided rules:**
- `[decided]` **Captions per platform:** the same visual on both platforms, separate captions. **English only.**
- `[decided]` **Length:** LinkedIn 120–220 words, Instagram 40–100 words (hashtags excluded from the count).
- `[decided]` **Emoji:** LinkedIn none. Instagram ≤ 2, never the first character, never as bullets.
- `[decided]` **Hashtags:** LinkedIn 3, Instagram 5, at the very end, from `HASHTAGS-v1`. Both always include #VerdantSoft.
- `[decided]` **Pronouns:** "we" for our experience, "you" for the advice. Never "I".
- `[decided]` **The Verdant take** ends every external post.
  - **Single posts:** the last body paragraph starts "Our take:" `[decided · CD]`.
  - **Carousels:** the take is its own slide.
  - **Content:** advice by default. "In our builds…" only with a confirmed FACTS id.
- `[decided]` **CTA:**
  - "Book a call at verdant-soft.com" only on How we work and Proof.
  - External, Build Notes and Grow with us posts end with a soft action (save, follow the series).
- `[decided]` **Questions:** about 1 in 3 posts end with a specific question. Never "Thoughts?" or "Agree?".
- `[decided]` **Explainers:** plain language, with one technical term defined in one line.
- `[decided]` **Sources:**
  - LinkedIn ends with "Source: Name · URL" before the hashtags.
  - Instagram gives "Source: Name" with no URL `[decided · CD]`.
  - The URLs allowed in captions are source URLs and verdant-soft.com.
- `[decided]` **Headlines:** problem/curiosity about 60%. Never the same formula three days running, never the same opening word two days running `[decided · CD]`. One highlight.
- **Alt text** `[decided · CD]`:
  - **Single posts:** one or two plain sentences. Say what the image is, and quote the on-image headline exactly.
  - **Carousels:** one sentence per slide.

**Draft structure v0 (under test):**
- **LinkedIn:**
  1. a hook line before "see more" (≤ 15 words; it extends the headline, never repeats it word for word)
  2. 2–4 short paragraphs of 1–3 sentences each, with line breaks
  3. "Our take:" (external) or the direct CTA line (How we work, Proof)
  4. an optional question
  5. the source line
  6. hashtags
- **Instagram:**
  1. a hook line (≤ 10 words)
  2. 1–2 short paragraphs
  3. "Our take:" in one sentence (external)
  4. an optional question
  5. "Source: Name" plus the soft action
  6. a blank line, then hashtags

<!-- id: HASHTAGS-v1 -->
```yaml
# [decided] counts: linkedin 3, instagram 5, #VerdantSoft always included.
# [decided · CD] sets below; the LAST Instagram tag may be swapped for one topic tag (e.g. #RAG) when the topic has an established tag.
trends:       { linkedin: ["#VerdantSoft", "#TechNews", "#ArtificialIntelligence"], instagram: ["#VerdantSoft", "#TechNews", "#ArtificialIntelligence", "#StartupFounder", "#SoftwareDevelopment"] }
ai:           { linkedin: ["#VerdantSoft", "#ArtificialIntelligence", "#LLM"], instagram: ["#VerdantSoft", "#ArtificialIntelligence", "#LLM", "#MachineLearning", "#AIExplained"] }
startup:      { linkedin: ["#VerdantSoft", "#Startups", "#ProductDevelopment"], instagram: ["#VerdantSoft", "#Startups", "#ProductDevelopment", "#StartupFounder", "#MVP"] }
numbers:      { linkedin: ["#VerdantSoft", "#TechTrends", "#Startups"], instagram: ["#VerdantSoft", "#TechTrends", "#Startups", "#SoftwareDevelopment", "#StartupFounder"] }
concepts:     { linkedin: ["#VerdantSoft", "#SoftwareEngineering", "#TechExplained"], instagram: ["#VerdantSoft", "#SoftwareEngineering", "#TechExplained", "#WebDevelopment", "#StartupFounder"] }
how-we-work:  { linkedin: ["#VerdantSoft", "#SoftwareOutsourcing", "#ProductDevelopment"], instagram: ["#VerdantSoft", "#SoftwareOutsourcing", "#DedicatedTeam", "#ProductDevelopment", "#SoftwareHouse"] }
build-notes:  { linkedin: ["#VerdantSoft", "#SoftwareEngineering", "#SystemDesign"], instagram: ["#VerdantSoft", "#SoftwareEngineering", "#SystemDesign", "#BackendDevelopment", "#CloudComputing"] }
proof:        { linkedin: ["#VerdantSoft", "#ClientStories", "#SoftwareDevelopment"], instagram: ["#VerdantSoft", "#ClientStories", "#SoftwareDevelopment", "#SoftwareOutsourcing", "#ProductDevelopment"] }
grow-with-us: { linkedin: ["#VerdantSoft", "#CareersInTech", "#LahoreTech"], instagram: ["#VerdantSoft", "#CareersInTech", "#LahoreTech", "#PakistanTech", "#SoftwareEngineer"] }
```

<!-- id: BANNED-WORDS-v1 -->
```yaml
# Case-insensitive; also blocks inflections (empowers, leveraging, unlocked …).
# From brand/strategy.md §5 [decided]; AI clichés and recruiting clichés added [decided · CD].
words: [innovative, cutting-edge, seamless, seamlessly, leverage, synergy, game-changer, game changer, unlock, revolutionise, revolutionize, delve, empower, top-tier, world-class, state-of-the-art, next-level, transformative, paradigm, supercharge, elevate, harness, ever-evolving, tapestry, rockstar, ninja, guru]
phrases: ["in today's fast-paced world", "in the ever-evolving landscape", "navigate the complexities", "deep dive", "dive in", "buckle up", "let that sink in", "here's the kicker", "the future is here", "exciting news", "we are pleased to announce", "thoughts?", "agree?"]
punctuation: { exclamation_marks_max: 1, unicode_bold: banned }
```

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
- `[decided]` **No self-reported numbers** (user, 2026-10-06): project counts, client counts, satisfaction rates, user reach or savings percentages are stated only once they appear in §2 `FACTS` as `confirmed`, and that needs the user's written confirmation. Today none do (F50–F52 are pending).
- `[proposed]` **No AI-generated people presented as Verdant Soft staff, clients or events.** Talent and culture visuals are conceptual, or show people who can't be identified (hands, silhouettes, shot from behind, out of focus). Real photos come only from the news inbox.
- `[proposed]` **National and religious days:** use only the pre-approved templates. Never generate Arabic or Urdu script, religious figures, or sacred sites.
- `[proposed]` **No third-party logos or trademarks** in images. Tech names in captions are fine.
- `[proposed]` **Identity:** never confuse the company with other "Verdant" companies (Verdant YC, Verdant DevCore, Verdant TCS, Verdant Web Tech, …).
- `[decided]` **External facts** (user, 2026-10-06):
  - Primary sources only, stats ≤ 2 years old, never second-hand.
  - The source goes on the image and in the caption.
  - Only checked, unexpired bank items may be used (§2.3 `EXTERNAL-SOURCES-v1`).
- `[decided]` **Other companies:** named in text only. Neutral and factual; no logos or product UI in images, no verdicts or comparisons, no implied partnership.
- `[decided]` **Verdant boundary:** never present a trend or a third-party result as Verdant experience. "In our builds…" only with a confirmed FACTS id.
- `[decided]` **Stance:** practical and balanced on AI and tech. No hype, no doom, no predictions presented as fact.
- **TBD:** AI disclosure policy. Nano Banana outputs carry SynthID and C2PA metadata, so Meta platforms may label them as AI automatically.

## 10. Approved examples
**TBD.** Each example records the post file, template ID, exact prompt and settings, a written description of the approved image, and both captions.

## 11. Memory and adaptation
This is how the pipeline behaves like a handler: it keeps track of the past and decides the future. **Partly decided (2026-10-06); the rest is TBD.**
- **Post history schema:** one row per post in `posts/index.md`. The fields:
  - date, file, pillar, lane/series and episode, format (single/carousel), timely (trend id or "evergreen"), sources (bank ids)
  - topic, visual subject, composition, client named, fact IDs used, template, final prompt
  - passed/total, verdict
- **Source banks** (`[decided]`):
  - `banks/trends.md`: timely items, 14-day expiry
  - `banks/topics.md`: evergreen topics per lane

  Both follow §2.3. When the pipeline uses an item, it sets `status: used` and records the post file.
- **Research runs:**
  - `[decided]` A **Saturday run** at 09:59 PKT, starting now: 3–5 checked trend items, and expired items get marked.
  - `[decided]` A **daily run from launch:** 1–3 items plus major breaking news. The Saturday run then picks the week's best 3–5 for Monday's roundup.
  - `[decided]` **D−1 research for every post** (user, 2026-10-06): the day before each post, the run re-checks that post's sources, looks for newer developments and runs a sensitivity check. It records the result in the post file. At launch, this is the daily run's first job; Monday's roundup is researched on Sunday, from the Saturday drop.
  - Runs commit to the repo, so the history is the audit trail.
- **News inbox** (`[decided]`): optional, at `inbox/` (format in `inbox/README.md`).
  - Items replace that day's external post.
  - Max one per day; the rest queue.
  - Real photos come only from here.
- **No-repeat windows and caps:** `CONTENT-MIX-v1` → `no_repeat`, checked against the history before choosing.
- **Series continuity:** next episode, and when a series ends or gets refreshed. **TBD.**
- **After launch:** a metrics loop adjusts **lane** weights within bounds.
  - Each lane stays at 5–20% of the month; the Verdant share at 25–40%.
  - Weights move by at most ±5 percentage points a month.
  - Brand fundamentals never change automatically.
  - A monthly human summary, plus an **8-week review of the 30/70 split** `[decided · CD]`.

---

## Changelog
| Date | Change | Evidence |
|---|---|---|
| 2026-10-04 | Skeleton created | — |
| 2026-10-06 | Content mix reset (user): §2.3 EXTERNAL-SOURCES-v1; §3 CONTENT-MIX-v1 (30% Verdant / 70% Tech, Explained, five lanes as named series, Tue/Thu Verdant, 2-2-3 carousel cycle, overrides, no-repeat); §4 lane recipes; §4.1 CAROUSEL-v1 → v2 (external and roundup variants); §7 decided caption rules, HASHTAGS-v1, BANNED-WORDS-v1; §9 external-content guardrails and no company numbers decided; §11 banks, research runs, inbox | User answers in plan mode, `learnings/log.md` 2026-10-06; `brand/strategy.md` v2 |
| 2026-10-04 | §2 draft with FACTS-v1 and PUBLIC-PROOF-v1; §3 widened to content strategy; §9 guardrails; §11 added | `brand/research.md` |
| 2026-10-06 | §4.1 CAROUSEL-v1: slide roles and limits, hook rules, CTA rules, 14-point checklist, 3-second test (adapted from the user's checklist + Carousel Playbook) | User-supplied playbook; `writing/carousel-playbook.md` |
| 2026-10-05 | §5.1 → PALETTE-v8 + THEMES-v1: Electric Royal, Deep Ocean, Deep Lagoon, Teal Night, Mist added; Royal Deep retired; two themes × four moods by pillar; elevation; tinted shadows; automatic light/dark checks. Light colour mass is now bright (no cobalt) | Three-designer panel + synthesis; contrast computed; 25-page book |
| 2026-10-05 | §5.1 → PALETTE-v7: Royal Deep added; named theme gradients (highlight-light/dark, ice-ground, abyss-ground, aurora-panel); per-theme colour roles and proportions. Colour guidelines book: `brand/guidelines/verdant-soft-colour-guidelines.pdf` | User: multi-page guidelines, colour only |
| 2026-10-05 | §5.1a → LIGHT-THEME-v2: grid, component kit, 7 templates (hero, glass, quote, list, carousel cover/slide, people), do/don't rules. Text pops via gradient highlights; one saturated colour block per post | User: "text doesn't pop", "build the overall theme"; `brand/theme/` |
| 2026-10-05 | §5.1 → PALETTE-v6 "deep ocean" from the user's reference boards and hex picks: deep navy/cobalt grounds, ocean teals, royal blue, polar lights, six gradients + aurora mesh; no yellow or lime | User references; contrast computed; `brand/palette/` |
| 2026-10-04 | §5.0 post rules: minimal, professional, premium, attractive, visual, readable, designer-made (posts and carousels) | User decision |
| 2026-10-04 | §5.5: complete posts generated in-model (text + logo via REF-PACK-v1); overlay is the fallback | User decision |
| 2026-10-04 | §6: generate at 3:4 and crop to 4:5 (Flow has no 4:5) | Flow error message |
| 2026-10-04 | §5 → PALETTE-v2: slate blue and sage teal fixed (user decision); light and dark themes with new neutrals; theme-by-pillar proposed | User decision; contrast computed |
| 2026-10-04 | Audit: §2 → FACTS-v2 (tagline confirmed, UI/UX process corrected to 6 steps, contact/CTA/payment/engagement facts, 10 case studies, self-reported numbers held as pending) and PUBLIC-PROOF-v2 (verbatim quotes; 6 quotable entries from 5 clients; `client_key` so caps count per person; P01 and P04 are one client; P02 held until the client is confirmed). §5 palette, type and logo files measured from the website. §9 proof cap per `client_key`; no self-reported numbers | `brand/audit-raw.md`, `brand/research.md` → Audit results |

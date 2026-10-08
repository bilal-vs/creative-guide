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

**Single posts carry information on the image** (`ON-IMAGE-v1`, user 2026-10-06). The old copy-only anatomy is superseded. In the lane table above, read "On-image text" for single posts as "plus the lane's labelled diagram".

<!-- id: ON-IMAGE-v1 -->
```yaml
id: ON-IMAGE-v1
status: 'decided 2026-10-07. User: ''the post must have some info rather than all info in captions'' (P6 note: ''too less details''). Limits come from VISUAL-SYSTEM-v1 text_budget and stay hypotheses until the first Flow calibration runs.'
applies_to: single posts and carousel covers; inner slides follow CAROUSEL-v2
supersedes: §4 'Single-post anatomy' and its line 'Nothing else goes on the image'
principle: 'The image carries the WHAT: a claim headline plus one structured payload, the labelled diagram on the colour plate. The caption carries the WHY, the SO WHAT and the NOW WHAT. Someone who never opens the caption still leaves with one concrete, savable thing. The headline is the claim; the labels are the facts or the method, never a restatement of the headline.'
anatomy:
- logo (REF-PACK-v2), top left, on the plain page
- series pill, 2-4 words
- 'headline: the claim, one [highlight] of 1-3 words'
- accent bar in the brand gradient
- subline or context line (optional)
- the plate with the lane's diagram; its 2-4 labels are the info block
- source line when a sourced fact appears (plain page, monospace)
- verdant-soft.com
hard_limits:
  image_total_words_max: 35
  strings_max: 8
  info_items_min: 2
  info_items_max: 4
  words_per_item_max: 5
  info_title_words_max: 0
  subline_words_max: 12
  label_characters_max:
    BAND: 24
    WINDOW: 18
    COLUMN: 12
    STACK_per_line: 20
exempt_from_labels:
- 'proof (Client words: the quote is the information)'
- numbers (figure, context line and source line are the information)
lane_defaults:
  how-we-work: 'RAIL: milestones or process steps, verbatim from FACTS'
  build-notes: 'MATRIX: what the lesson isolates or separates'
  proof: QUOTE-MARK for Client words; MODULE-MAP for Project Spotlight, tiles named verbatim from one FACTS entry
  grow-with-us: 'STACK: the real tools by layer; FRAME when a real inbox photo exists'
  startup: 'TREE: the kept path and the parked items'
  numbers: 'FIGURE: the number, its context line and the source line'
  concepts: 'CUTAWAY: the parts of the system, in plain words'
  ai: 'FAN: tokens, core and branches (single variant)'
  trends: 'SIGNAL-BOARD: one labelled track per story (cover)'
characters: 'plain keyboard characters only: no middle dot, arrows, en or em dashes, ellipses, curly quotes or emoji; a middle dot means two separate strings'
caption_complement:
- 'C1 no shingle: no 5-word run is shared between either caption and any on-image string. Exempt: the verbatim proof quote, Source lines, and the one sentence that states and attributes an on-image number'
- 'C2 no re-list: no caption paragraph covers 3 or more labels (or every label when there are 2)'
- 'C3 hook: each caption''s first line shares less than 60% of its content words with the headline'
- 'C4 take: ''Our take:'' goes one step past the image and never appears on it'
- 'C5 pointer: a caption may point at the image at most once (''Save the three checks above''); it never re-types the labels'
- 'C6 numbers: every on-image number reappears in the caption in the same sentence as its source name, with hedges kept'
- 'C7 caption-only: ''Our take:'', ''Book a call at verdant-soft.com'', the closing question, URLs other than the footer, hashtags and emoji'
caption_order:
  linkedin: 'hook (15 words or fewer, extends the headline) -> why it matters -> one worked example or failure -> ''Our take:'' or the direct CTA -> optional question -> ''Source: Name · URL'' -> 3 hashtags'
  instagram: 'hook (10 words or fewer, not the headline) -> the single most useful idea not on the image -> ''Our take:'' in one sentence (external) -> optional question -> ''Source: Name'' plus the soft action -> blank line -> 5 hashtags'
alt_text: 'singles: one string of 2-3 plain sentences, ''Post reading: {headline}. {subline}. {labels in reading order joined with semicolons}.'' plus the source line; carousels: one sentence per slide'
```

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
- **The day picks the mood** (2026-10-07). `VISUAL-SYSTEM-v1` → `day_map` (§5.7) supersedes the THEMES-v1 pillar → mood week map. `colours.py WEEK` and the colour book are updated in roadmap step 3 (colour revision). The colours themselves don't change.
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

### 5.7 Visual system v1: "SCHEMATIC, editorial finish" (**PAUSED 2026-10-08, under revision**)
> **Paused by user taste data.** In round L1 the SCHEMATIC look scored 2/10 ("nothing useful, font too basic"), and the type-led Swiss poster scored 7/10 ("modern, premium, clear to read", but "font too basic" and "too flat").
> - **Kept:** its mechanics (day map, text budget, quote-once prompting, the prompt tools).
> - **Being replaced:** its look, via taste rounds L2 (fonts, depth) and D1 (dark), then VISUAL-SYSTEM-v2.

- **Source:** the visual workflow (3 art directors; judges for clients, a student, a designer and the pipeline engineer).
- **The idea:** every post is one page of a calm engineering report: a misty light page, a strict grid and a near-black headline with one gradient highlight. One saturated plate bleeds off the edges and carries a flat white diagram, whose labels are the info block. One small frosted-glass piece in the other hue family is the only dimensional object.
- **Week:** six light days and one dark Saturday. Royal and lagoon alternate, and no two consecutive days share a mood or layout.
- **This supersedes** the THEMES-v1 pillar → mood week map. The colours stay PALETTE-v8.
- **Templates are proven by calibration:** a template is accepted at ≥ 50% of outputs passing over 8 outputs, on 2 topics (§8).
- **Prompt assembly:** `tools/build_prompt.py` (§6).

<!-- id: VISUAL-SYSTEM-v1 -->
```yaml
id: VISUAL-SYSTEM-v1
status: 'PAUSED 2026-10-08: under revision. In taste round L1 this look (direction A, Report) scored 2/10 and the type-led Swiss poster (D) won at 7/10. See learnings/taste.md. Do not generate posts with it.'
date: 2026-10-06
name: SCHEMATIC, editorial finish
lineage: 'Base: SCHEMATIC-v1 (art director C), weighted panel score 7.25/10 (clients 40%, designer+engineer 35%, student 25%). Finish, plate geometry, counter-accent, dark-day choice and slot-library structure grafted from Luminous Report (A, 6.93). Progression object, carousel reference, copy hygiene and sameness controls grafted from Built Objects (B, 6.15).'
big_idea: 'Every post is one page of a calm engineering report, set as premium Swiss editorial design. The information is the visual: one precise white diagram (a milestone rail, an isolation matrix, a decision tree, a system cutaway, a proportion bar) drawn on one saturated colour plate that bleeds off the edge of the page. Its labels are the post''s info block, so one element informs and decorates at once. Exactly one element of the diagram (the active node, the kept path, the interface) is a small tactile piece of sandblasted frosted glass in the other hue family: the one physical, premium moment on an otherwise flat, exact page. Near-black sentence-case headlines with one gradient highlight, a misty light page, monospace reference text and fine grain finish it. Royal days carry ideas, lagoon days carry practice and evidence, and one dark Saturday carries the week''s key figure. Each lane owns one diagram family, so the series is recognisable at thumbnail size and the pipeline only fills
  slots (family, node count, active node, labels).'
canvas:
  generate: 3:4 portrait in Flow and the API; every position below is a % of the 3:4 frame (reference grid 1080x1440)
  publish_linkedin: '4:5, 1080x1350: keep the full width, trim 3.125% of the height from the top and 3.125% from the bottom, Lanczos to 1080 wide'
  publish_instagram: 4:5 crop by default; native 3:4 (1080x1440) is an open user decision; every layout is safe in both
  safe_zone:
    sides_pct_of_width: 8
    top_and_bottom_pct_of_height: 11
  plate_coverage_pct_of_4x5_crop:
    singles_and_covers:
    - 25
    - 40
    inner_slides: exempt (CAROUSEL-v2 inner = text-led, small motif)
  final_sizes_at_1080_wide:
    headline: 84-100 px, extra bold (800), the largest text
    quote: 56-62 px bold (Client words only)
    figure: digit height about 14% of the image height, about two thirds of the content width (numbers only)
    subline_and_context: 34-40 px
    plate_labels: '>= 36 px, white, bold'
    body: '>= 32 px (34 target)'
    meta: '>= 28 px: URL, source line, slide counter'
  logo: REF-PACK-v2 lockup, top-left on the plain page, about a quarter of the image width; never on the plate
fixed_on_every_post:
- misty light page (or teal night on Saturday) with a strict grid, 8%/11% margins, left-aligned text
- logo top-left from the reference image
- series pill (covers and singles) or slide counter (inner slides)
- extra-bold sentence-case headline in near-black navy (white on dark), exactly one highlight span of 1-3 words in the mood's gradient
- 'accent bar under the headline in the brand gradient #416D95 -> #74AFAD (both core colours on every post)'
- exactly one saturated colour plate, crisp edges, bleeding off at least two image edges
- one flat white diagram in the line language, plus exactly one frosted-glass piece in the counter-accent hue
- verdant-soft.com bottom-left on the plain page
- matte surfaces, fine print grain, glow only inside the plate
variable_daily:
- 'diagram family (fixed per lane) and its configuration: node count, active index, modifier'
- labels, headline, subline, figure, source line
- mood and layout come from the day map, never chosen freely
day_map:
  Mon:
    lane: trends
    mood: light-royal
    layout: WINDOW
    family: SIGNAL-BOARD
  Tue:
    lane: how-we-work (A) | build-notes (B)
    mood: light-lagoon
    layout: BAND
    family: RAIL | MATRIX
  Wed:
    lane: ai
    mood: light-royal
    layout: COLUMN
    family: FAN
  Thu:
    lane: proof (A) | grow-with-us (B)
    mood: light-lagoon
    layout: WINDOW
    family: QUOTE-MARK or MODULE-MAP | STACK or FRAME
  Fri:
    lane: startup
    mood: light-royal
    layout: BAND
    family: TREE
  Sat:
    lane: numbers
    mood: dark-lagoon
    layout: CORNER
    family: FIGURE-BAR | FIGURE-RATIO | FIGURE-SIGNATURE
  Sun:
    lane: concepts
    mood: light-lagoon
    layout: COLUMN
    family: CUTAWAY
day_map_properties:
- no two consecutive days share mood or layout, Sun -> Mon included
- every day has a unique mood x layout pair, so each day is recognisable in the grid
- 6 of 7 days light; the one dark day is a single-only lane, so the dark theme needs one template and no dark carousel
- 'royal 3 days, lagoon 3 days + dark lagoon 1: teal-led 4 of 7, the fix for ''too much blue'''
- Verdant's own days (Tue, Thu) are lagoon, the hue family nearest the logo's sage teal
- Dark Royal has no weekly slot in v1; it stays in PALETTE-v8 unused
moods:
  light-royal:
    from: THEMES-v1 light-royal; plate glow now sits only behind the glass piece
    ground:
    - '#F5F9FD'
    - '#E8F0F8'
    - '#DAE6F2'
    plate:
    - '#2457D6'
    - '#3C6EB7'
    plate_light: '#09CACC'
    glass_piece: '#00ACB3'
    shadow: '#2457D6 tinted, soft'
    rule: '#C9DCEC'
    prompt_block: 'Colour: the page is a calm misty white with a hint of blue, a soft vertical gradient from mist white (#F5F9FD) to pale ice blue (#DAE6F2), with a faint polar-white glow at the top left. The plate is a smooth gradient from vivid electric royal blue (#2457D6) to softer royal blue (#3C6EB7), with a soft blue-tinted shadow on the page along its inner edge. The drawing and labels on it are white. The glass piece is lagoon-teal frosted glass (#00ACB3) with a faint cyan (#09CACC) light directly behind it, never behind a label. Hairline rules are pale blue-grey (#C9DCEC).'
    slots:
      pill_fill: a smooth gradient from electric royal blue (#2457D6) to deep ocean teal (#007A9E)
      pill_text: white
      ink: near-black navy (#050816)
      ink_short: near-black navy
      support: steel navy (#42658A)
      highlight: a smooth gradient from electric royal blue (#2457D6) to deep ocean teal (#007A9E)
      rail_ink: electric royal blue (#2457D6)
      logo_colours: slate-blue to sage-teal gradient colours
      ref_pack: REF-PACK-v2-light
  light-lagoon:
    from: 'THEMES-v1 light-lagoon; plate uses the text-safe stops only (the #00ACB3 stop under white text is 2.78:1)'
    ground:
    - '#F2FAFA'
    - '#E3F3F3'
    - '#D2EBEC'
    plate:
    - '#00727F'
    - '#0088AA'
    plate_light: '#34CCA4'
    glass_piece: '#A6CAEC'
    shadow: '#062A33 tinted, soft'
    rule: '#BFDDE0'
    prompt_block: 'Colour: the page is a calm polar white with a cool sea tint, a soft vertical gradient from pale polar white (#F2FAFA) to pale misty aqua (#D2EBEC), with a faint polar-white glow at the top left. The plate is a smooth gradient from deep lagoon teal (#00727F) to ocean teal (#0088AA), with a soft deep-teal-tinted shadow on the page along its inner edge. The drawing and labels on it are white. The glass piece is pale sky-blue frosted glass (#A6CAEC) with a faint mint-jade (#34CCA4) light directly behind it, never behind a label. Hairline rules are pale sea-grey (#BFDDE0).'
    slots:
      pill_fill: a smooth gradient from deep lagoon teal (#00727F) to deep ocean teal (#007A9E)
      pill_text: white
      ink: near-black navy (#050816)
      ink_short: near-black navy
      support: steel navy (#42658A)
      highlight: a smooth gradient from deep ocean teal (#007A9E) to deep lagoon teal (#00727F)
      rail_ink: deep lagoon teal (#00727F)
      logo_colours: slate-blue to sage-teal gradient colours
      ref_pack: REF-PACK-v2-light
  dark-lagoon:
    from: THEMES-v1 dark-lagoon, unchanged; Saturday only; tested last
    ground:
    - '#040C12'
    - '#061A22'
    - '#08262F'
    plate:
    - '#062A33'
    - '#00727F'
    - '#0088AA'
    plate_edge: '#E9FFFC'
    glass_piece: '#A6CAEC'
    glass_light: '#09CACC'
    rule: '#163A42'
    prompt_block: 'Colour: this is the dark version. The page is a deep teal night, a soft vertical gradient from almost-black teal (#040C12) to dark teal (#08262F), with a faint ocean-teal (#0088AA) haze at the top left. The plate is a smooth gradient from dark teal (#062A33) through deep lagoon teal (#00727F) to ocean teal (#0088AA), outlined by a thin pale polar (#E9FFFC) edge light; nothing casts a drop shadow. The drawing on it is white. The glass piece is pale sky-blue frosted glass (#A6CAEC) that glows faintly from within with cyan (#09CACC) light and catches a thin pale rim light. Hairline rules are dark sea-grey (#163A42).'
    slots:
      pill_fill: solid mint jade (#34CCA4)
      pill_text: near-black navy (#050816)
      ink: white
      ink_short: white
      support: soft sage teal (#74AFAD)
      highlight: a smooth gradient from cyan (#09CACC) to mint jade (#34CCA4)
      rail_ink: cyan (#09CACC)
      logo_colours: all-white colours
      ref_pack: REF-PACK-v2-dark
  counter_accent_rule: 'Every post shows both hue families: royal plates carry lagoon glass, lagoon plates (light and dark) carry sky-blue glass, and every highlight gradient ends in a teal (#007A9E, #00727F or #34CCA4). No post is ever single-hue blue or single-hue teal.'
  reserve_mood_blocks:
    light-royal-tide-b: 'if royal days still read too blue after the counter-accent: plate #007A9E (top) -> #2457D6 (bottom); new version MOOD-light-royal-v2'
    light-mist: 'only if the user vetoes any dark day: Saturday on the Mist page with a brand-gradient plate #416D95 -> #74AFAD; FIGURE layouts carry no white text on that plate (white on #74AFAD fails); needs its own test against the v4 ''dull'' risk'
layouts:
  BAND:
    id: LAYOUT-BAND-v1
    used_by:
    - how-we-work
    - build-notes
    - startup
    zones:
      logo_and_pill_row: 11-15%
      hairline: 16%
      headline: 20-41%
      accent_bar_and_subline: to 51%
      plate: 55-81% full width, bleeds left and right
      source_line: 84%
      url: 87%
    plate_coverage_4x5: about 28%
    prompt_block: a strict editorial grid read from top to bottom, with margins of about 8% of the width at the sides and 11% of the height at the top and bottom that only the page and the plate reach into. The logo sits at the top left with its top edge about 11% down and the series pill on the same line at the top right, with a thin hairline rule across the content width just below them. The headline starts at about 20% of the height, followed by the accent bar and the subline, all left-aligned and ending by about 51%. The colour plate is a full-bleed horizontal band from about 55% to about 81% of the height, running off the left and right edges and covering about 28% of the image; the diagram sits on it inside the side margins. {footer_clause}
    footer_clause:
      plain: Below the band, on the plain page, the website address sits at the bottom left at about 87% of the height.
      with_source: Below the band, on the plain page, the source line sits at the left at about 84% of the height and the website address at the bottom left at about 87%.
      cover_suffix: Small progress dots and a short arrow line sit at the bottom right at about 87% of the height, in {support}.
  WINDOW:
    id: LAYOUT-WINDOW-v1
    used_by:
    - trends-cover
    - proof
    - grow-with-us
    zones:
      logo: 11%
      plate: x 46-100%, y 0-51%, bleeds top and right
      pill: left column at 45%
      lead_text: 55-83% full width
      url: 87%
    plate_coverage_4x5: about 27%
    prompt_block: a strict editorial grid with a large colour window, with margins of about 8% of the width at the sides and 11% of the height at the top and bottom that only the page and the plate reach into. The colour plate is a window in the top-right corner, from about 46% of the width to the right edge and from the top edge down to about 51% of the height, running off the top and right edges with one generously rounded lower-left corner and covering about 27% of the image; it holds the {visual_noun} inside the margins. The logo sits at the top left with its top edge about 11% down, and the series pill sits in the same left column at about 45% of the height, level with the bottom of the window; the space between them stays calm and empty. Below the window, the {lead_role} runs across the full content width from about 55% of the height, followed by the accent bar and the {second_role}, all left-aligned and ending by about 83%. {footer_clause}
    footer_clause:
      plain: The website address sits at the bottom left at about 87% of the height.
      cover_suffix: Small progress dots and a short arrow line sit at the bottom right at about 87% of the height, in {support}.
  COLUMN:
    id: LAYOUT-COLUMN-v1
    used_by:
    - ai
    - concepts
    zones:
      plate: x 65-100%, full height, bleeds top, right and bottom
      text_column: x 8-59%
      logo: 11%
      pill: 30%
      headline: 34%
      text_ends: 72%
      url: 87%
    plate_coverage_4x5: about 35% (kept under 36% so the light gate's mean luminance stays >= 0.55)
    prompt_block: 'a strict editorial grid with a tall colour column, with margins of about 8% of the width at the sides and 11% of the height at the top and bottom that only the page and the plate reach into. The colour plate is a full-height column down the right side, from about 65% of the width to the right edge, running off the top, right and bottom edges and covering about 35% of the image; it holds the diagram, stacked from top to bottom, inside the margins. Everything else sits in the left column, from the left margin to about 59% of the width: the logo at the top left with its top edge about 11% down, a calm empty space, the series pill at about 30% of the height, then the headline from about 34%, the accent bar and the subline, all left-aligned and ending by about 72%. {footer_clause}'
    footer_clause:
      plain: The website address sits at the bottom left at about 87% of the height.
      with_source: The source line sits at the left at about 84% of the height and the website address at the bottom left at about 87%.
      cover_suffix: Small progress dots and a short arrow line sit at the bottom of the left column, at about 87% of the height, right-aligned to it, in {support}.
  CORNER:
    id: LAYOUT-CORNER-v1
    used_by:
    - numbers
    zones:
      logo_and_pill_row: 11-15%
      hairline: 16%
      figure: 20-36%
      context: 39-48%
      plate: x 46-100%, y 51-100%, bleeds right and bottom
      source_line: 84% left of the plate
      url: 87%
    plate_coverage_4x5: about 26%
    prompt_block: a strict editorial grid built around one huge figure, with margins of about 8% of the width at the sides and 11% of the height at the top and bottom that only the page and the plate reach into. The logo sits at the top left with its top edge about 11% down and the series pill on the same line at the top right, with a thin hairline rule across the content width just below them. The figure starts at about 20% of the height, flush left, about two thirds of the content width wide, its digits about 14% of the image height tall. The context line sits below it from about 39% of the height, left-aligned on one or two lines, ending by about 48%. The colour plate fills the lower-right corner, from about 46% of the width to the right edge and from about 51% of the height to the bottom edge, running off the right and bottom edges with one generously rounded upper-left corner and covering about 26% of the image. To the left of the plate, on the plain page, the source line sits at about
      84% of the height and the website address at the bottom left at about 87%.
  SLIDE:
    id: LAYOUT-SLIDE-v1
    used_by: every carousel slide after the cover (modes BODY, ITEM, RECEIPT)
    zones:
      logo_and_counter_row: 11%
      headline: 18-29%
      body: 31-58%
      band: 63-75% full width (receipt 74-84%)
      source_line: 84%
      url: 87%
    prompt_block_body: a calm, text-led reading page on a strict grid, with margins of about 8% of the width at the sides and 11% of the height at the top and bottom that only the page and the band reach into. The logo sits at the top left with its top edge about 11% down and the slide counter on the same line at the top right. The headline starts at about 18% of the height, left-aligned on one or two lines; the body text follows from about 31% and, with the {after_body} just below it, ends by about 58%. A slim full-bleed colour band runs across the image from about 63% to about 75% of the height, off the left and right edges, and holds the progress line inside the side margins. {footer_clause}
    prompt_block_receipt: a calm, text-led summary page on a strict grid, with margins of about 8% of the width at the sides and 11% of the height at the top and bottom that only the page and the band reach into. The logo sits at the top left with its top edge about 11% down and the slide counter on the same line at the top right. The headline starts at about 18% of the height, left-aligned on one or two lines; the checklist follows from about 29% and ends by about 70%. A slim full-bleed colour band runs across the image from about 74% to about 84% of the height, off the left and right edges, holding a short white line of text at its left and the completed progress line at its right. The website address sits at the bottom left at about 87% of the height.
    footer_clause:
      plain: Below the band, on the plain page, the website address sits at the bottom left at about 87% of the height.
      with_source: Below the band, on the plain page, the source line sits at the left at about 84% of the height and the website address at the bottom left at about 87%.
    band_fill: 'the day mood''s plate gradient (royal #2457D6 -> #3C6EB7; lagoon #00727F -> #0088AA)'
diagram:
  line_language: White, even strokes with rounded ends; lines only horizontal or vertical, turning at right angles with small rounded corners; nodes are small rings (hollow = not yet / parked), white dots (done / solid) or the glass piece (active); a faint grid of tiny dots on the plate only. Every node carries a label or is a counted progress marker. No diagonal connectors, no free-floating networks, no icons, no screens, no logos.
  glass_piece: 'Exactly one per post: a piece of sandblasted frosted glass in the mood''s counter-accent hue, matte and softly lit, the only dimensional object in the image. It marks the active element: the finished milestone, the isolated tenant, the chosen output, the kept path, the interface, the end of the fill. Lane variants: a small puck (default), a slab (MATRIX), a keycap (STACK, FRAME), a sculpted quotation mark (QUOTE-MARK), a block glowing from within (CUTAWAY, FIGURE-SIGNATURE). Never text on it.'
  families:
    SIGNAL-BOARD:
      id: DIAGRAM-SIGNAL-BOARD-v1
      lane: trends (cover)
      config: tracks = item count (3-5); one label per track, 1-2 words, <= 18 characters; the first track's ring is the glass piece
      prompt_block: a signal board. {n_word} parallel horizontal white tracks are stacked with even gaps across the plate. Each track starts with a small solid white dot at its left end and carries one outlined white ring at a different point along it, staggered from track to track. The ring on the first track is the glass piece, a small softly rounded puck of frosted glass. Just above the left end of each track sits its label in white bold sans-serif, about the subline's size.
    RAIL:
      id: DIAGRAM-RAIL-v1
      lane: how-we-work
      config: nodes = labels = 3 or 4, taken verbatim from FACTS; labels <= 4 words, <= 24 characters, 1-2 lines; progression unfinished -> finished (the Wireframe -> Production signature)
      prompt_block: 'a horizontal milestone rail: one straight white line across the plate at about two fifths of its height, from the left margin to about four fifths of the image width, carrying exactly {n_word} evenly spaced nodes, the first at its left end and the last at its right end. The nodes go from unfinished to finished: the first is a thin white ring, {middle_phrase}, and the last is the glass piece, a small rounded puck of frosted glass. Under each node, left-aligned with it, is its label in white bold sans-serif, about the subline''s size, on one or two lines.'
      middle_phrase:
        '3': the middle one a white ring with a solid centre
        '4': the two middle ones white rings with solid centres
    MATRIX:
      id: DIAGRAM-MATRIX-v1
      lane: build-notes
      config: 3 rows x 3 columns; 3 row labels (what is isolated), <= 2 words each; the isolated column (1st, 2nd or 3rd) is the glass slab
      prompt_block: 'an isolation matrix. A grid of three rows and three columns of rounded cells drawn in thin white outlines fills the right two thirds of the plate, with clear vertical gaps between the columns running the full height of the grid. The {ordinal} column is the glass piece: a slim slab of frosted glass standing behind its three cells, which are drawn in solid white outlines. At the left of the plate, level with each row, sits that row''s label in white bold sans-serif, about the subline''s size.'
      variant_BLOCKS: an architecture diagram of {n_word} rounded blocks drawn in thin white outlines, {arrangement}, joined only by right-angle white connector lines. The {focus} block is the glass piece, a rounded block of frosted glass. Under each block sits its label in white bold sans-serif, about the subline's size.
    FAN:
      id: DIAGRAM-FAN-v1
      lane: ai
      config: 3 end nodes = 3 labels, <= 12 characters each (COLUMN width); at most one modifier per post
      prompt_block: a prediction diagram that runs from top to bottom down the plate. Near the top, three small rounded chips drawn in white outlines sit side by side, like tokens. One vertical white line joins them to a plain rounded-square core in the middle of the plate. Below the core the line splits at right angles into three branches of different stroke weights, each turning right and ending in a node, the three nodes stacked one above another. The heaviest branch ends in the glass piece, a small softly rounded puck of frosted glass; the other two end in thin outlined rings. {modifier_sentence} To the right of each end node sits its label in white bold sans-serif, about the subline's size.
      modifiers:
        none: ''
        retrieval: A small outlined box beside the core, like a stack of index cards, feeds into it through one short right-angle line.
        agents: A thin white return line runs from the glass piece back up to the chips, turning at right angles.
        evals: A short horizontal gate bar crosses the three branches just above their end nodes.
        hallucination: The heaviest branch has a clear gap in it just below the core, so the most confident answer is connected to nothing.
    QUOTE-MARK:
      id: DIAGRAM-QUOTE-MARK-v1
      lane: proof (Client words)
      config: no labels on the plate; the verbatim quote is the lead text
      prompt_block: one large opening quotation mark sculpted from frosted glass, the glass piece, standing on the plate slightly left of its centre, about a third of the window's height tall, resting on a thin white baseline that runs off the plate's right edge, with a few faint dots of the plate grid around it.
    MODULE-MAP:
      id: DIAGRAM-MODULE-MAP-v1
      lane: proof (Project Spotlight)
      config: 3-4 tiles named verbatim from one FACTS entry (F30-F39), <= 16 characters each; the scope word (built / developed / contributed to) goes in the headline or subline
      prompt_block: a module map. One larger rounded core block of frosted glass, the glass piece, sits at the left of the plate. Thin white connector lines leave it at right angles and lead to {n_word} smaller rounded tiles drawn in white outlines, stacked one above another on the right. Inside each tile sits its label in white bold sans-serif, about the subline's size.
    STACK:
      id: DIAGRAM-STACK-v1
      lane: grow-with-us (conceptual)
      config: '3 bars; each label is one string ''Layer: tool, tool, tool'' set on two lines, <= 20 characters per line, names only, never logos'
      prompt_block: 'a layer stack. Three wide rounded bars drawn in thin white outlines are stacked one above another with even gaps. A vertical white connector runs down their left side and threads one small solid white node through each bar. At the top of the connector sits the glass piece: a single blank keycap of frosted glass. Inside each bar sits its label in white bold sans-serif, about the subline''s size, on two lines that break after the colon.'
    FRAME:
      id: DIAGRAM-FRAME-v1
      lane: grow-with-us (inbox photo)
      config: the real inbox photo is composited into the frame after generation; people are never generated and a staff photo is never sent to the model
      prompt_block: 'an empty picture frame: an upright rectangle with a thin white border, standing on the plate, filled with flat, plain pale polar white (#E9FFFC) and nothing else. A small blank keycap of frosted glass, the glass piece, rests against its lower-right corner.'
    TREE:
      id: DIAGRAM-TREE-v1
      lane: startup
      config: 3 end nodes = 3 labels (the kept one + 2 parked), <= 20 characters each; FORK variant = 2 branches for trade-offs
      prompt_block: a decision tree that reads from left to right. A root ring sits near the left edge of the plate at mid-height. From it one white line runs right and splits at right angles into {n_word} branches that end in {n_word} nodes stacked one above another on the right half of the plate. Exactly one branch, the kept path, is a thick solid white line ending in the glass piece, a small softly rounded puck of frosted glass; the other branches are thin dashed white lines ending in small hollow rings. To the right of each end node sits its label in white bold sans-serif, about the subline's size.
    CUTAWAY:
      id: DIAGRAM-CUTAWAY-v1
      lane: concepts
      config: '3 blocks = 3 labels, <= 12 characters each (COLUMN width); variants: cache (a small lit chamber beside a long channel), queue (single-file tokens), index (a column of thin shelves, one lit)'
      prompt_block: 'a system cutaway that runs from top to bottom down the plate. Three rounded blocks are stacked one above another with even gaps. The top block is a plain white outline. The middle block is the glass piece: a block of frosted glass glowing softly from within, with three short white lines of different lengths on its face, like lines on a menu card. The bottom block is a white outline with a thin dashed inner boundary, like a private inside. A request line with a small arrowhead runs down the left half from the top block into the middle block, and from the middle block into the bottom block; a response line with a small arrowhead runs back up the right half the same way, through the middle block. No line skips the middle block. Directly under each block sits its label in white bold sans-serif, about the subline''s size.'
    FIGURE-BAR:
      id: DIAGRAM-FIGURE-BAR-v1
      lane: numbers
      config: only when the figure is a share that is a multiple of 10%, or 25% or 75%; fill checked by pixels within +-3% of the track length
      prompt_block: a proportion bar. One long horizontal track with rounded ends, drawn as a thin white outline, lies across the middle of the plate inside the margins, with ten faint white tick marks evenly spaced along it. The track is filled with solid white from its left end to exactly {fill_words}, and the rest of the track is empty. A small softly rounded bead of frosted glass, the glass piece, sits at the end of the fill.
      fill_words_examples:
        '50': half its length, at the fifth tick mark
        '25': a quarter of its length, halfway between the second and third tick marks
        '70': seven tenths of its length, at the seventh tick mark
    FIGURE-RATIO:
      id: DIAGRAM-FIGURE-RATIO-v1
      lane: numbers
      config: only for 'N in M' with M <= 10
      prompt_block: a row of {m_word} small white rings evenly spaced across the plate inside the margins; the first {k_word} are filled solid white and the rest stay outlined, and the last filled ring is the glass piece, a small softly rounded bead of frosted glass.
    FIGURE-SIGNATURE:
      id: DIAGRAM-FIGURE-SIGNATURE-v1
      lane: numbers
      config: 'every other figure (amounts, counts, dates, shares that are not multiples of 10%): no proportion is drawn, so nothing can misstate the number'
      prompt_block: a single softly rounded block of frosted glass, the glass piece, standing on a thin white baseline in the middle of the plate and glowing faintly from within.
    PROGRESS-LINE:
      id: DIAGRAM-PROGRESS-LINE-v1
      lane: all carousel inner slides
      config: nodes = total slides; node n = this slide; earlier = solid, later = rings; receipt = all solid with the glass piece last
      prompt_block: 'a progress line: one thin white line runs across the band inside the side margins, carrying {N_word} small nodes evenly spaced. Node {n_word} is the glass piece, a small softly rounded puck of frosted glass; the nodes before it are solid white dots and the nodes after it are thin outlined white rings.'
lanes:
  trends:
    series: This Week in Tech
    day: Mon
    mood: light-royal
    template: TPL-trends-v1
    cover: LAYOUT-WINDOW-v1 + DIAGRAM-SIGNAL-BOARD-v1; track labels are the week's item topics (1-2 words); with 5 items the subline is dropped
    inner: LAYOUT-SLIDE-v1 ITEM mode (headline <= 8 words, body <= 30 words, source line) and BODY mode for our-take; receipt in RECEIPT mode on Nano Banana Pro
  how-we-work:
    series:
    - Outsourcing, Decoded
    - Wireframe → Production
    day: Tue (week A)
    mood: light-lagoon
    template: TPL-how-we-work-v1
    single: 'LAYOUT-BAND-v1 + DIAGRAM-RAIL-v1; labels = the stages, verbatim from FACTS (P3: F12)'
    carousel: 'cycle week 2: BAND cover with the rail''s first stages, SLIDE inner slides, receipt'
  build-notes:
    series: Build Notes
    day: Tue (week B)
    mood: light-lagoon
    template: TPL-build-notes-v1
    single: LAYOUT-BAND-v1 + DIAGRAM-MATRIX-v1 (or its BLOCKS variant); labels = what the lesson isolates or connects, from F05-F06, F30-F39
    carousel: 'cycle week 2 (when Build Notes takes the Tuesday carousel): BAND cover, SLIDE inner slides'
  ai:
    series: AI, Explained
    day: Wed
    mood: light-royal
    template: TPL-ai-v1
    single: LAYOUT-COLUMN-v1 + DIAGRAM-FAN-v1 with at most one modifier; labels = the three candidate outputs or roles
    carousel: 'cycle week 1: COLUMN cover, SLIDE inner slides, receipt'
  proof:
    series:
    - Client words
    - Project Spotlight
    day: Thu (week A)
    mood: light-lagoon
    template: TPL-proof-v1
    client_words: LAYOUT-WINDOW-v1 + DIAGRAM-QUOTE-MARK-v1; lead = the verbatim quote (<= 25 words); second line = the attribution exactly as in PUBLIC-PROOF; prefer entries whose attribution carries a role and company
    project_spotlight: LAYOUT-WINDOW-v1 + DIAGRAM-MODULE-MAP-v1; tiles verbatim from one FACTS entry
  grow-with-us:
    series: Grow at Verdant
    day: Thu (week B)
    mood: light-lagoon
    template: TPL-grow-with-us-v1 (conceptual) | TPL-grow-with-us-photo-v1 (default whenever an inbox photo exists)
    conceptual: LAYOUT-WINDOW-v1 + DIAGRAM-STACK-v1; tools named in text, never as logos
    photo: LAYOUT-WINDOW-v1 + DIAGRAM-FRAME-v1; second line = name, labels none, real photo composited after generation
  startup:
    series: Founder Notes
    day: Fri
    mood: light-royal
    template: TPL-startup-v1
    single: LAYOUT-BAND-v1 + DIAGRAM-TREE-v1 (FORK variant for two-way trade-offs); labels = the kept job and two parked items
    carousel: 'cycle week 3: BAND cover, SLIDE inner slides, receipt'
  numbers:
    series: By the Numbers
    day: Sat
    mood: dark-lagoon
    template: TPL-numbers-v1
    single: LAYOUT-CORNER-v1 + FIGURE-BAR | FIGURE-RATIO | FIGURE-SIGNATURE (chosen by the figure's type); lead = the figure, second line = context (<= 14 words), source line required
  concepts:
    series: Under the Hood
    day: Sun
    mood: light-lagoon
    template: TPL-concepts-v1
    single: LAYOUT-COLUMN-v1 + DIAGRAM-CUTAWAY-v1 (or its cache, queue, index variants); labels = the parts of the system, plain words
    carousel: 'cycle week 3: COLUMN cover, SLIDE inner slides, receipt'
  overrides: inbox items and calendar moments take the replaced day's mood and layout, and the family of their own lane
text_lines:
  PILL: '{pill_position}, a small, fully rounded pill label filled with {pill_fill}: "{pill}", in {pill_text} semi-bold.'
  pill_position:
    BAND: At the top right, on the same line as the logo
    CORNER: At the top right, on the same line as the logo
    WINDOW: In the left column, level with the bottom of the window
    COLUMN: In the left column, below the empty space
  COUNTER: 'At the top right, the slide counter: "{nn} / {NN}", in a neat monospace, {support}, small.'
  highlight_grammar: '{highlight_position} is a plural phrase such as ''final three words'' or ''second and third words''; for one word use ''final word, which stays on its line and is filled with'', keeping the sentence grammatical'
  LEAD_headline: 'The headline: "{headline}", in extra-bold {ink}, left-aligned on up to {max_lines} lines; the {highlight_position} stay together on one line and are filled with {highlight}. It is by far the largest text.'
  LEAD_quote: 'The client''s quote: "{quote}", in bold {ink}, left-aligned on up to six lines; the {highlight_position} are filled with {highlight}. It is the largest text.'
  LEAD_figure: 'The figure: "{figure}", in extra-bold sans-serif filled with {highlight}, by far the largest element in the image.'
  ACCENT: Directly under the {lead_role}, a short accent bar about a tenth of the image width, in a gradient from muted slate blue (#416D95) to soft sage teal (#74AFAD).
  SUBLINE: 'The subline: "{subline}", in regular {support}, about two fifths of the headline''s height.'
  ATTRIBUTION: 'Below the accent bar, the attribution: "{attribution}", in semi-bold {support}, about half the quote''s size.'
  CONTEXT: 'The context line: "{context}", in semi-bold {ink}, about two fifths of a normal headline''s size.'
  BODY: 'The body text: "{body}", in regular {ink}, about a third of the headline''s size, on up to six lines.'
  AFTER_BODY: 'Just below the body, the {after_body}: "{line}", in semi-bold {ink}, the same size as the body.'
  CHECKLIST_INTRO: 'The checklist: a thin vertical line in {rail_ink} runs down the left with one small solid dot per row, and beside each dot one row of text in semi-bold {ink}, about the body''s size:'
  CHECKLIST_ROW: '- Row {k_word}: "{item}"'
  SAVE: 'On the band, at its left: "Save this", in white bold, about the body''s size.'
  LABEL: '- {label_anchor}: "{label}"'
  label_anchors:
    SIGNAL-BOARD:
    - Above the first track
    - Above the second track
    - Above the third track
    - Above the fourth track
    - Above the fifth track
    RAIL:
    - Under the first node
    - Under the second node
    - Under the third node
    - Under the fourth node
    MATRIX:
    - Beside the top row
    - Beside the middle row
    - Beside the bottom row
    FAN:
    - Beside the top end node
    - Beside the middle end node
    - Beside the bottom end node
    TREE:
    - Beside the top end node, at the end of the kept path
    - Beside the middle end node
    - Beside the bottom end node
    CUTAWAY:
    - Under the top block
    - Under the middle block
    - Under the bottom block
    STACK:
    - Inside the top bar
    - Inside the middle bar
    - Inside the bottom bar
    MODULE-MAP:
    - Inside the top tile
    - Inside the second tile
    - Inside the third tile
    - Inside the fourth tile
  SOURCE: 'The source line: "Source: {source_name}, {YYYY}", in a neat regular monospace, {support}, the same small size as the website address.'
  URL: 'The website address: "verdant-soft.com", in semi-bold {support}, small but sharp.'
  COUNT: Apart from the logo, the image contains exactly {n_strings_word} pieces of text, the ones quoted above, each appearing once and spelled exactly as given. Every other area is clean page, plate, lines and shapes.
  LOGO: 'Logo: use the attached image as the Verdant Soft logo. Place it unchanged at the top left on the plain page, inside the margins, about a quarter of the image width, keeping its shape, letters and {logo_colours} exactly as in the attached image.'
carousels:
  mood: one mood for every slide, from the day map
  cover: the lane's single layout and diagram in its start state, at most 4 labelled nodes, every node labelled; pill = series; subline = the swipe line; progress dots and a short arrow line as graphics
  inner: 'LAYOUT-SLIDE-v1: counter top-right (monospace), headline, body (>= 32 px, <= 30 words), bridge or action line on the page, source line above the URL, a slim full-bleed band holding DIAGRAM-PROGRESS-LINE-v1'
  receipt: 'LAYOUT-SLIDE-v1 RECEIPT mode: up to 6 rows on a vertical checklist rail in {rail_ink} on the page, ''Save this'' in white bold on the band, verdant-soft.com as its own string; up to 10 strings, so Nano Banana Pro by default'
  fixed_positions:
    logo: top-left
    counter: top-right
    progress: the band (replaces CAROUSEL-v2 dots on inner slides)
    url: bottom-left
    source_line: above the URL, on the page
  consistency: same mood, type scale and positions on every slide; optional REF-CAROUSEL (the selected cover) as a second reference, only after the user approves a principle-4 amendment
text_budget:
  on_image_v1_hard_limits:
    subline_words_max: 12
    info_items_min: 2
    info_items_max: 4
    words_per_item_max: 5
    info_title_words_max: 1
    image_total_words_max: 35
  info_exempt:
  - numbers (figure + context + source line are the information)
  - proof Client words (the quote is the information)
  strings_per_single_max: 8
  strings_per_inner_slide_max: 6
  strings_receipt_max: 10
  headline_words_max: 8
  quote_words_max: 25
  context_words_max: 14
  label_characters_max:
    BAND: 24
    WINDOW: 18
    COLUMN: 12
    per_line_STACK: 20
  labels_add_information: labels never restate the headline; if half or more of a label's content words appear in the headline, rewrite the headline as the claim and keep the labels as the facts
gates:
  light_v2:
  - mean luminance of the 4:5 crop >= 0.55
  - <= 6% of pixels darker than luminance 0.10, counted outside OCR text boxes (a three-line near-black headline alone is about 3.5-5%)
  - no fill darker than the mood's darkest plate stop, except text
  dark_v2:
  - mean luminance <= 0.15
  - pixels brighter than luminance 0.50 (text, drawing, edge light, glass) cover 2-25% of the frame; the plate counts as mass, not glow
  - no drop shadows
  layout:
  - output ratio 3:4 within 1%
  - plate coverage 25-40% of the 4:5 crop on singles and covers (layouts target 26-35%, leaving room for drift)
  - no text or logo outside the safe zone
feed_rhythm:
  grid_example: 'Nine newest tiles, Mon to the following Tue, newest top-left. Row 1: Tue lagoon BAND (rail) | Mon royal WINDOW (signal board) | Sun lagoon COLUMN (cutaway). Row 2: Sat DARK CORNER (figure) | Fri royal BAND (tree) | Thu lagoon WINDOW (quote). Row 3: Wed royal COLUMN (fan) | Tue lagoon BAND (matrix) | Mon royal WINDOW (signal board).'
  reading: Royal and lagoon alternate into a loose checkerboard. Plates sit low (band), high (window), tall (column) and in the corner, so no shape repeats on neighbouring tiles. The one dark tile walks one column a week (7 mod 3 = 1), a planned anchor that makes the light tiles look brighter. The misty page, top-left logo and near-black headlines repeat on every tile, so the grid reads as one publication.
variety_rules:
- mood and layout come from the day map; never chosen freely
- no two consecutive posts share mood or layout (checked again when an override lands)
- any 9 consecutive tiles hold 1-2 dark tiles, never adjacent
- any 9 consecutive tiles hold at most 2 type-led heroes (Client words quote, numbers figure)
- within a lane, the same configuration (family + node count + active index + modifier) may not repeat within 28 days; the next post changes at least one of them
- exactly one glass piece and one highlight span per post; at most one plate light, behind the glass piece only
- a carousel keeps one mood, one family and one type scale from cover to receipt
- before selection, render the candidate with the last 8 published posts as a 3x3; reject if 3 tiles in any row or column share a mood
- 'thumbnail test at 360 px wide: the first headline line is legible and the day family is clear from colour alone'
ledger_fields:
- mood
- layout
- family
- node_count
- active_index
- modifier
- glass_variant
- visual_logic
- model
- ref_pack
- outputs
- download_px
- passed_of_total
- failure_classes
current_not_dated:
  current:
  - 'Swiss editorial grid: oversized, extra-bold, sentence-case headlines, wide margins, left-aligned type'
  - 'information as the visual: labelled diagrams in the dot-grid, right-angle, ringed-node language of current dev-tool docs and Figma/FigJam canvases'
  - 'report-grade detail: hairline rules, monospace reference text, source lines as footnotes'
  - 'proof-first, data-forward: real stages, real modules, real stacks, sourced numbers, no invented charts'
  - 'one restrained physical moment: a single frosted-glass piece, glass as a material rather than a UI panel (the post-Liquid-Glass reading)'
  - analogous blue-to-teal colour held inside one crisp, full-bleed plate
  - matte surfaces and fine grain against the glossy, symmetrical AI-render look
  - light-first with one dark page, like current product UI
  retired:
  - glossy rising bar charts (too close to growth arrows) and the kit's hard-coded teal heroes
  - glassmorphism card stacks and glass list rows (L-GLASS, L-LIST, L-SLIDE)
  - 'free-floating node networks and constellations: every node here is counted, labelled and on the grid'
  - 'aurora blobs and the coral-violet-cyan mesh ''SaaS aura'': glow lives only inside the plate, behind one piece'
  - isometric and Corporate Memphis illustration, neon on navy, all-caps navy-and-yellow templates
  - 'inset rounded slide cards: plates bleed off the page edge'
  - AI-generated people of any kind
  test: if a post would still look right with its diagram redrawn by hand in Figma, it is not dated
deliberate_changes:
- 'THEMES-v1 week map replaced by day_map: Mon and Wed Dark Royal -> Light Royal; Tue How we work and Thu Proof Light Royal -> Light Lagoon; Sun Light Royal -> Light Lagoon; Fri Light Lagoon (Grow) -> Light Royal (Founder Notes); Sat stays Dark Lagoon (Brand world -> By the Numbers); Grow stays Light Lagoon (now Thu B)'
- Dark Royal has no weekly slot
- 'Light Lagoon plate drops the #00ACB3 stop wherever white text sits on it (#00727F -> #0088AA)'
- plate glows move from fixed positions to 'behind the glass piece only'
- LIGHT-THEME-v2 templates and heroes superseded by 4 layouts + SLIDE and 14 diagram families; the colour mass now bleeds off at least two edges
- carousel inner slides exempt from the 25-40% mass rule; CAROUSEL-v2 dots on inner slides move into the band's progress line
- 'monospace becomes a brand element for reference text only (proposed: IBM Plex Mono or JetBrains Mono; fallback Inter tabular figures)'
- 'TYPE-v1 is stale: its heading says overlays only and weight 700; complete posts and weight 800 are current'
- single posts carry an info block as diagram labels (ON-IMAGE-v1), replacing §4's 'nothing else goes on the image'
- light gate v2 excludes OCR text boxes from the dark-pixel count; dark gate v2 counts the plate as mass, not glow
open_decisions:
- 'day map including one dark Saturday: approved [decided · CD]'
- 'Instagram: the 4:5 crop, the same file as LinkedIn [decided · CD]; native 3:4 stays possible because every layout keeps the 4:5 safe zone'
- 'monospace for reference text (source line, slide counter): yes [decided · CD]'
- '''Wireframe → Production'': calibration test T2 decides; if the arrow garbles, the series becomes ''Wireframe to Production'' [decided · CD]'
- 'REF-CAROUSEL second reference for inner slides: deferred until a cover passes and principle 4 is amended'
- 'AI disclosure (§9): deferred; the crop and re-encode probably strip C2PA while SynthID survives'
```

### 5.6 Still TBD
- **Fixed elements** (never vary): lighting, medium/style, mood
- **Variable elements** (vary daily within limits): subject, setting, composition, metaphor
- Composition and negative-space zones reserved for overlays
- Text-in-image policy (what the model may render vs. what is overlaid)
- Overlay spec: logo position and size, headline position, safe margins

## 6. Image prompt system
`[decided · CD]` (2026-10-07), from VISUAL-SYSTEM-v1. Prompts are assembled, never free-written: `python3 tools/build_prompt.py <pack-id> <packs-file>` fills `PROMPT-SKELETON-v1` from the day map, the mood, layout and diagram blocks in §5.7, and the pack's strings. `python3 tools/lint_prompt.py <post-file>` checks every prompt before it is sent.

- `[decided]` **Aspect ratio:** Google Flow offers Nano Banana 2 only 1:1, 16:9, 9:16, 4:3 and 3:4 (no 4:5). Generate at **3:4**, end every prompt with "Portrait image, 3:4 aspect ratio.", and crop deterministically to the 4:5 post (keep the full width, trim 3.125% of the height top and bottom). The API pipeline uses the same 3:4 + crop, for parity. Evidence: Flow error, 2026-10-04.
- **Reference pack REF-PACK-v2:** `brand/ref-pack/ref-pack-v2-light.png` (gradient lockup on a #F5F9FD 3:4 canvas) for light moods; `brand/ref-pack/ref-pack-v2-dark.png` (white lockup on #061A22) for Saturday. Exactly one reference per prompt.
- **Versioning:** TPL-<lane>-v<n> covers the layout, mood and diagram blocks, the text-line templates and the style block. Changing any of them bumps the version. A prompt is never edited once sent; a new version is written instead.

**Fixed style block** (appended to every prompt):

<!-- id: STYLE-BLOCK-v1 -->
```text
Design finish: a premium, minimal editorial page by a senior brand design team, calm and exact like a beautifully designed engineering report: a strict grid, generous empty space, asymmetric and uncluttered. Type is a crisp neo-grotesque sans-serif in the style of Inter, with extra-bold, tightly spaced sentence-case headlines and a neat monospace for small reference text; every letter is sharp and easy to read on a phone. The plate is a crisp-edged, full-bleed printed panel that keeps any glow inside itself. The drawing on it is flat and white, with even rounded strokes, only horizontal and vertical lines meeting at right angles, and a faint grid of tiny dots. The frosted glass piece is the only dimensional object, softly lit and matte. Everything is matte, with a very fine print grain over the whole image. Pure graphic design in cool blues and teals with near-black navy and white.
```

**Master prompt skeleton:**

<!-- id: PROMPT-SKELETON-v1 -->
```text
Create an image: a finished, ready-to-publish social media post for Instagram and LinkedIn, designed by a senior brand design team for Verdant Soft, a B2B software company that designs and builds custom software for international clients. It is {format_phrase} in a recurring series that {series_purpose}, and this {post_noun} {post_job}.

Layout: {LAYOUT_BLOCK}

{MOOD_BLOCK}

On the {plate_noun}, {DIAGRAM_BLOCK} The {plate_noun}, the drawing and the glass piece carry no other words.

Text, each piece exactly as written between the double quotes:
- {PILL | COUNTER}
- {LEAD_headline | LEAD_quote | LEAD_figure}
- {ACCENT}
- {SUBLINE | ATTRIBUTION | CONTEXT | BODY}
[- {AFTER_BODY}]
[{CHECKLIST_INTRO}
{CHECKLIST_ROW, one per row}]
[{LABEL, one per label, in diagram order}]
[- {SAVE}]
[- {SOURCE}]
- {URL}
{COUNT}

{LOGO}

{STYLE-BLOCK-v1}

Portrait image, 3:4 aspect ratio.
```

**Slot and text-rendering rules:**

<!-- id: PROMPT-RULES-v1 -->
```yaml
slot_rules:
- 'FILL ORDER: the date gives the day; VISUAL-SYSTEM-v1 day_map gives mood and layout; the lane gives template and diagram family; the post file gives the strings; FACTS or the checked bank item gives labels and numbers. The pipeline never picks a mood, layout or family freely.'
- '{format_phrase}: "a single image post" | "the cover of a {N}-slide carousel" | "slide {n} of a {N}-slide carousel" (numbers as words). {post_noun}: post | cover | slide.'
- '{series_purpose}: a fixed plain clause per series. It never contains the series name, which appears only inside the pill quote, or ''Verdant Soft''.

  - This Week in Tech: ''sums up the week''s technology news for startup founders''

  - Outsourcing, Decoded: ''explains plainly how working with an outsourcing partner works''

  - Wireframe → Production: ''walks through how a product goes from first sketch to live software''

  - Build Notes: ''shares engineering lessons from real software builds''

  - AI, Explained: ''explains how AI systems work in plain language''

  - Client words: ''shares what clients say about working with the company''

  - Project Spotlight: ''shows what the company built for a client''

  - Grow at Verdant: ''shows students and junior developers what working at the company is like''

  - Founder Notes: ''gives startup founders practical product advice''

  - By the Numbers: ''explains one sourced number about technology''

  - Under the Hood: ''explains one software concept for non-technical founders'''
- '{post_job}: one plain clause of 20 words or fewer, from the post file''s Brief. No quoted words, no numbers that aren''t on the image, no banned words.'
- '{LAYOUT_BLOCK}: layouts.<layout>.prompt_block, verbatim.

  - {footer_clause} = plain or with_source (with_source whenever a source line exists). Covers append cover_suffix with {support} filled.

  - WINDOW also fills {visual_noun} (diagram | quotation mark | picture frame), {lead_role} (headline | client''s quote) and {second_role} (subline | attribution | name and role).

  - SLIDE BODY fills {after_body} (bridge line | action line). If there is none, delete '' and, with the {after_body} just below it,'' and write '' and'' instead.

  - SLIDE RECEIPT uses prompt_block_receipt.'
- '{MOOD_BLOCK}: moods.<mood>.prompt_block, verbatim. Every {pill_fill}, {pill_text}, {ink}, {ink_short}, {support}, {highlight}, {rail_ink} and {logo_colours} slot in the text lines comes from the same mood''s slots. Never mix moods in a post or a carousel.'
- '{plate_noun}: ''plate'' on singles and covers, ''band'' on inner slides. {DIAGRAM_BLOCK}: the lane family''s prompt_block, verbatim.

  - Write counts as words ({n_word} = three).

  - {middle_phrase}, {ordinal}, {fill_words}, {m_word} and {k_word} come from the family entry.

  - FAN takes exactly one modifier sentence, or an empty string.

  - Inner slides use PROGRESS-LINE with {N_word} = total slides and {n_word} = this slide.'
- 'TEXT LINES: use text_lines.<NAME> verbatim, in the skeleton''s order. Omit any optional line whose element is absent, and its bullet with it.

  - Singles and covers use PILL; inner slides use COUNTER.

  - LEAD is LEAD_headline, LEAD_quote (Client words) or LEAD_figure (numbers).

  - {lead_role} in ACCENT = headline | client''s quote | figure.

  - The second line is SUBLINE, ATTRIBUTION (Client words), CONTEXT (numbers) or BODY (inner slides).

  - LABEL lines use the family''s label_anchors in diagram order.'
- 'QUOTING: every on-image string appears exactly once, inside straight double quotes. No other double quotes appear anywhere in the prompt. Hex codes, colour names, font names and role words never go inside quotes.'
- 'HIGHLIGHT: name it by position, never by re-quoting the words. Write a plural phrase (''final three words'', ''second and third words''). For a single word, use ''final word, which stays on its line and is filled with''. Exactly one span of 1–3 consecutive words, the same words marked [ ] in the pack.'
- '{max_lines}: BAND three, WINDOW three, COLUMN four, SLIDE two. If the headline can''t fit (more than about 22 characters a line in BAND or WINDOW, about 13 in COLUMN), the copy is shortened. The layout never changes.'
- 'LABELS:

  - 2–4 labels (singles: the family''s count), each 5 words or fewer.

  - Character caps: BAND 24, WINDOW 18, COLUMN 12, STACK 20 per line.

  - Taken verbatim from FACTS, PUBLIC-PROOF or the checked bank item.

  - Every node gets a label.

  - If half or more of a label''s content words appear in the headline, the headline is rewritten as the claim. The labels stay as the facts.'
- '{n_strings_word} in COUNT = the number of quoted strings in the text lines, written as a word (P3 = seven). The logo is not counted. Caps: singles 8, inner slides 6, receipt 10.'
- 'LOGO and reference:

  - {logo_colours} comes from the mood.

  - Attach exactly one reference: REF-PACK-v2-light on light moods, REF-PACK-v2-dark on Saturday.

  - Inner slides may add REF-CAROUSEL only after the principle-4 amendment is approved.'
- 'NEVER WRITE:

  - ''pixel-perfect'', ''exact replica'' or ''recreate'';

  - ''green'' or ''lime'' (write mint jade or sage teal);

  - lists of ''no X'' (say what is there instead);

  - the series name or ''Verdant Soft'' outside the pill quote, the opener and the logo line;

  - arrows, middle dots, dashes or ellipses inside quoted strings.'
- 'VERSIONING: TPL-<lane>-v<n> covers the fixed parts of the template: layout block, mood block, family block, text-line templates and style block. Change any of them and the version goes up. Inside a post, prompts go v1, v2 …, and a prompt is never edited once sent.'
text_rendering_rules:
- 'QUOTE ONCE (from C): every on-image string appears exactly once in the prompt, inside straight double quotes, in its own element line. Nothing else goes inside double quotes: hex codes, colour names, font names, role words (pill, headline, label) and the series and mood names all stay outside. A and B each quoted a string outside their own closing list; this rule removes that failure.'
- 'CLOSE WITH THE COUNT SENTENCE, not a re-quoted list: ''Apart from the logo, the image contains exactly N pieces of text, the ones quoted above, each appearing once and spelled exactly as given.'' Write N as a word. Calibration test T1 compares this on P3 with A''s explicit quoted lines plus closing list (8 outputs each). Whichever form wins on exact-text pass rate is locked.'
- 'HIGHLIGHT AND LINE BREAKS BY POSITION: describe them (''the final three words stay together on one line and are filled with …'') and never re-quote a fragment. Use exactly one highlight span of 1–3 consecutive words per post or slide. Give a maximum line count and let the model break the lines; OCR ignores line breaks.'
- 'TEXT BUDGET:

  - Singles: 8 quoted strings or fewer and 35 words or fewer. The URL counts; the logo doesn''t.

  - Headline: 8 words or fewer. Subline: 12 or fewer. Context line: 14 or fewer.

  - Labels: 2–4, each 5 words or fewer. Character caps: BAND 24, WINDOW 18, COLUMN 12, STACK 20 per line.

  - Client words quote: 25 words or fewer.

  - Inner slides: 6 strings or fewer, body 30 words or fewer.

  - Receipt: 10 strings or fewer, on Nano Banana Pro by default.'
- 'LABELS ARE THE INFO BLOCK AND MUST ADD INFORMATION. They come verbatim from FACTS, PUBLIC-PROOF or the checked bank item. If half or more of a label''s content words already appear in the headline, the headline is rewritten as the claim. Every node or tile gets a label: no decorative unlabelled nodes.'
- 'SIZE IN WORDS, CHECKED IN PIXELS: prompts state size relatively (''by far the largest text'', ''about two fifths of the headline''s height'', ''about a third'', ''small but sharp''). The floors are measured on the final 1080-wide post: headline 84–100 px, white plate labels 36 px or more in bold, body 32 px or more, meta (URL, source line, counter) 28 px or more. Any string below its floor fails.'
- 'WHERE TEXT MAY SIT:

  - Light pages: headline in near-black navy #050816 (18.9:1 on mist); subline, URL and source line in steel navy #42658A (4.8:1 or better). Cyan, mint, sage or polar text never appears on a light page.

  - White text appears only on the plate''s deep stops (royal #2457D6/#3C6EB7, lagoon #00727F/#0088AA, dark plate), only in bold at 36 px or more.

  - White text never sits over #00ACB3 (2.78:1) or over the cyan or mint light (about 2:1), and never on the glass piece.

  - The URL and source line always sit on the plain page.

  - Dark Saturday: figure in the cyan → mint gradient, context line in white, source line and URL in sage teal #74AFAD (6.4:1).'
- 'PLAIN KEYBOARD CHARACTERS ONLY (from B):

  - Quoted strings use straight apostrophes, periods, commas, colons, digits, % and $.

  - No arrows, middle dots, en or em dashes, ellipses, curly quotes or emoji.

  - A ''·'' in the copy becomes two separate strings.

  - ''Wireframe → Production'' gets one isolated test first. If the arrow garbles, the user chooses ''Wireframe to Production''. The repo''s Inter subset has no → glyph either.'
- 'NUMBERS: copy them exactly from the checked bank item or FACTS, with the symbol inside the same quoted string ("50%"). Never round, never spell out, and never repeat a number elsewhere on the image.'
- 'SOURCE LINE: always "Source: {Organisation}, {YYYY}" in a neat monospace on the plain page, above the URL. Required on every post or slide that states an external fact; never on the plate. In CORNER it stays at 24 characters or fewer so it fits left of the plate.'
- 'BRAND NAME: ''Verdant Soft'' is never a quoted string. It appears unquoted only in the opening sentence and the logo line, and the wordmark comes only from the reference image. If stray ''Verdant Soft'' text appears in 2 or more outputs of a run, classify it [prompt] and change the opener to ''a B2B software company''.'
- 'LOGO WORDING (calm): ''use the attached image as the Verdant Soft logo. Place it unchanged at the top left on the plain page, inside the margins, about a quarter of the image width, keeping its shape, letters and … colours exactly as in the attached image.'' Never write ''pixel-perfect'', ''exact replica'' or ''recreate''. The logo never sits on the plate. Light posts use the gradient-lockup reference; dark posts use the white-lockup reference.'
- 'COLOUR WORDING: give a plain colour name with the hex in parentheses, always outside quotes. Never write ''green'' or ''lime''. If a hex code, colour name or role word renders as visible text, classify it [prompt]: make a colour-names-only variant of that template and measure the colour drift by pixel sampling.'
- 'OCR QA: compare each quoted string exactly after normalising apostrophes, quote marks and whitespace; line breaks are ignored. Any missing, extra, duplicated or misspelled string fails the technical check. The first failure of a string is [variance]. The same string failing in 2 or more runs is [prompt]. The frosted quotation-mark sculpture on Client words is whitelisted from the ''extra text'' check.'
- 'ESCALATION:

  - A template is accepted when 50% or more of its outputs pass over 8 outputs (two runs of 4), on two different topics. That gives about a 94% chance of a usable post per batch of 4.

  - Below 50%, rerun it unchanged on Nano Banana Pro and log that.

  - An element that fails in more than 25% of outputs across 2 or more posts moves to deterministic overlay, in this order: logo, URL, source line, numbers bar fill, plate labels. Headline and pill go last.

  - When an element moves to overlay, the prompt then reserves its area as clean, empty page.'
```

**Generation settings** (Flow now, API parity later):

<!-- id: GENERATION-v1 -->
```text
FLOW (hand runs now)
- Model and tool:
  - Google Flow → Images, Nano Banana 2 (Gemini 3.1 Flash Image) for singles, covers and inner slides.
  - Nano Banana Pro for receipt slides, and for any template whose pass rate is below 50% (log the switch).
  - Never Nano Banana 2 Lite for anything that carries text.
- Aspect ratio 3:4 (Flow has no 4:5). The prompt also ends "Portrait image, 3:4 aspect ratio."
- Outputs: 4.
- Ingredients: exactly ONE reference image.
  - REF-PACK-v2-light: brand/brand-guide/png/verdant-logo-gradient.png (852×204), centred at about 60% of the width on a plain 3:4 canvas filled #F5F9FD (e.g. 1536×2048).
  - REF-PACK-v2-dark (Saturday only): brand/brand-guide/png/verdant-logo-white.png on a plain 3:4 #061A22 canvas.
  - Padding the wide (about 4:1) logo removes its pull toward a wide output.
  - REF-PACK-v2 still has to be built. Until it exists, use REF-PACK-v1 (the raw wide PNG) and log any ratio drift.
- Run rules:
  - Paste the prompt exactly as written.
  - Single shot: no lasso, no draw-to-edit, no follow-up turns.
  - Any wording change is a new prompt version.
- Download the largest size offered (2K if available). Record the real pixel size of the first file; 1K at 3:4 is probably about 896×1200, unverified.
- Check the corners for a visible watermark. A mark more than about 45 px from the edge survives the crop.
- Log every run:
  - date, post file, TPL id and version, prompt version;
  - mood, layout, family with node count, active index and modifier;
  - model, ratio, outputs, REF-PACK version, download px, watermark yes/no;
  - pass or fail per rubric item, failure class ([prompt] / [variance] / [concept]).

API PIPELINE (parity, later)
- Model and call:
  - Model gemini-3.1-flash-image; escalation gemini-3-pro-image. Both IDs are medium confidence: confirm before building.
  - image_config.aspect_ratio "3:4", image_size "2K", thinking_level "high".
  - response modalities IMAGE only (IMAGE+TEXT is reported to cap output at 1K).
- 4 candidates per post, the same REF-PACK files. Assert the output ratio is 3:4 within 1%, otherwise discard the image.
- Calibration before any blind test: P3, P7 and P8, 4 outputs each in Flow, in the API at thinking high and in the API at thinking minimal. Score all on the §8 rubric and keep the API setting whose pass rate matches Flow's.

POST-PROCESS (deterministic, identical for Flow and API)
- Crop by ratio: keep the full width and trim 3.125% of the height from the top and from the bottom → 4:5. Lanczos to 1080×1350, sRGB.
- Export PNG pages for the LinkedIn PDF carousel and JPEG at quality 92 for Instagram.
- Optional, user decision: post Instagram natively at 3:4 (1080×1440). Every layout keeps its content inside the 4:5 safe zone, so both work.
- Grow FRAME posts: composite the real inbox photo into the detected empty rectangle.
- Overlay only the elements the escalation ladder has moved.

SELECTION
1. Automatic gates (light v2 or dark v2, layout) and OCR.
2. §8 rubric, binary checks plus scroll-stop of 3 or more.
3. The highest scroll-stop among the passes wins.
4. If none pass, run a second batch of 4 (8 outputs at most). If still none, apply the escalation ladder. Never publish a failing output.

CALIBRATION TESTS (first runs)
- T1: P3 text form. Quote-once with the count sentence (default) vs explicit quoted lines with a closing list, 8 outputs each.
- T2: the 'Wireframe → Production' pill, tested alone.
- T3: does the Light Lagoon mint light read green? (hue check)
- T4: REF-CAROUSEL second reference, only after its approval.

TEST ORDER (light first)
1. P3 TPL-how-we-work-v1 (Light Lagoon, BAND, RAIL), plus T1.
2. P7 TPL-startup-v1 (Light Royal, BAND, TREE). Together with P3 this proves BAND on two topics.
3. P9 TPL-concepts-v1 (Light Lagoon, COLUMN, CUTAWAY).
4. P5 TPL-proof-v1 Client words and P6 TPL-grow-with-us-v1 (both WINDOW).
5. P4 TPL-build-notes-v1 (BAND, MATRIX).
6. AI COLUMN with FAN (P2's cover, run as a single).
7. P1 carousel: WINDOW cover, SLIDE inner slides, receipt on Pro.
8. P8 TPL-numbers-v1 (Dark Lagoon, CORNER, FIGURE-BAR at 50%), last; needs REF-PACK-v2-dark.

A layout or template is promoted to the guide only after it passes on two different topics.
```

**Known model quirks and research caveats** (from the visual research, 2026-10-06; most are from search summaries, so verify them on the first runs):
- Only four cloud.google.com blog posts were read in full: the Ultimate prompting guide, the enterprise launch, the GA notice and the Lite notice. Every other model claim below comes from search summaries or secondary sources.
- Model IDs (gemini-3.1-flash-image, gemini-3-pro-image) and the thinking_level parameter (minimal | high) come from search summaries (M). Confirm them against the live API before the pipeline is built. Flow does not expose thinking level, so Flow ↔ API parity must be measured, not assumed.
- Reference-image limits: '10 object + 4 character images for Nano Banana 2, 6 + 5 for Pro' and 'Pro accepts up to 3 style references' are summary-only or L. The system uses one reference (two only if REF-CAROUSEL is approved), so the impact is low.
- Flow specifics are all secondary or summary (M/L): 1–4 outputs per prompt, images free (0 credits), Nano Banana Pro selectable, Flow's own ingredient limit, 2K/4K upscale on download, watermark by tier, and a forced-watermark regression on Pro. Verify each one on the first run and log it.
- Reference images overriding the requested aspect ratio, and the open bug where 3.1 Flash ignores aspect_ratio, come from forum and third-party reports (M). This is why REF-PACK-v2 pads the logo to 3:4 and every output's ratio is checked.
- Text-accuracy figures are L and conflict: about 95% on 1–4-word strings, Pro about 94% vs about 92% for Nano Banana 2, and 'keep to 3–5 text elements'. The 25-character guidance is for Imagen, an older model. The 8-string cap is a hypothesis to be measured. The 81% vs 69% 'all strings correct' figures are judge arithmetic assuming 97% per string, not measurements.
- No source documents that hex codes in prompts are honoured, and the reports of instruction text rendering as visible text are L. Colour fidelity and leakage are handled by pixel sampling and OCR, not trusted.
- Two reports are forum-only: IMAGE+TEXT response modality capping output at 1K (L), and the June 2026 2K/4K washout incident, fixed on 19 June (M). Keep the R-SHARP check.
- The 1K 3:4 output size of about 896×1200 is arithmetic, not observed. Read the real size from the first download.
- Platform facts come from search summaries and secondary sources (M/L): Instagram's 3:4 grid tiles and native 1080×1440 uploads; LinkedIn's 4:5 tallest size; PDF carousels at about 1.4× reach (vendor data); LinkedIn's 'CR' badge for C2PA; the EU AI Act Art. 50 date of 2026-08-02. The §9 AI-disclosure decision should not rest on them without the user checking.
- The 'what feels current' and 'what looks dated' claims are L–M secondary or vendor sources and are used only as design direction, never as facts in posts. They include the serif-headline rise (one blog), the Liquid Glass revival, the mesh-gradient 'SaaS aura' label, Canva's 'Imperfect by Design' and the AI-trust survey figures (31%, 63%).
- The four judges (founder, CTO, student, designer+engineer) were AI agents simulating those perspectives, not real people. Treat their scores as structured hypotheses. If possible, show the first approved posts to two or three real founders and a student group.
- Contrast ratios and coverage percentages were computed here (H for the hex pairs). The model will not hit hex values or plate geometry exactly, so the light-gate margin on COLUMN layouts (mean luminance estimated at about 0.57) and all coverage targets must be measured on real outputs.
- The dark gate's floor of 2% of pixels above luminance 0.50 may be marginal on FIGURE posts. The cyan and mint figure gradient has luminance of about 0.47, below the threshold, so the bright pixels come mainly from the white text, bar and edge light. Measure it on the first Saturday outputs before relying on it.
- The missing → glyph in the Inter subset is first-hand evidence (H), but it concerns the overlay fonts, not the model. Whether Nano Banana 2 renders the arrow in 'Wireframe → Production' cleanly is untested (test T2).

## 7. Caption system
`[decided]` rules come from the user (2026-10-06); `[decided · CD]` were delegated to the creative director. **Templates and few-shot examples stay TBD** until writing practice passes two consecutive rounds at ≥ 80% keep, with no truth or voice failures.

`[decided · CD]` (user, 2026-10-06: "decide by yourself", "review the writing with 5 personas"): the keep/kill marks come from a **5-persona writing panel**, which reviews the words only, never the visuals. The panel is a bootstrapped AU founder, a sceptical US CTO, a Dutch PM, a Lahore CS student and a cynical LinkedIn tech peer. A part is killed when 3 or more of the 5 kill it. Truth or freshness flags are checked against the sources, not voted. The user keeps a veto. Round 2 is `writing/round-02-lane-packs.md`; the panel's rounds are in `writing/persona-reviews.md`.

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
**Partly decided** (2026-10-07). The visual checks below come from VISUAL-SYSTEM-v1. An output **passes** only if every binary check passes and its scroll-stop score is 3 or more. Selection, retries and escalation are in `GENERATION-v1` (§6): 4 outputs per run, a second run if none pass, at most 8 outputs, then the escalation ladder. A failing output is never published. Caption checks are `tools/check_packs.py` plus the ON-IMAGE-v1 caption-complement rules.

<!-- id: VISUAL-RUBRIC-v1 -->
```yaml
binary_checks:
- 'R-TEXT-EXACT: every quoted string appears exactly once, character for character, after normalising apostrophes, quote marks and whitespace. Headline line breaks are ignored.'
- 'R-TEXT-NONE-EXTRA: no other text anywhere. That includes hex codes, colour or role words, ''Verdant Soft'' outside the logo, letters on the plate or the glass, filler text, and watermarks inside the 4:5 crop. The Client-words quotation-mark sculpture is whitelisted.'
- 'R-TEXT-COUNT: the number of text elements OCR finds equals N in the count sentence. The logo is excluded.'
- 'R-LOGO: matches the REF-PACK lockup (V-mark shape, ''Verdant Soft'' letters, gradient or white colours). It is not redrawn, sits top-left on the plain page at about a quarter of the width, and is never on the plate.'
- 'R-SAFE-ZONE: no text or logo in the outer 8% of the width at either side, or the outer 11% of the 3:4 height at top and bottom. That makes the post safe for the 4:5 crop and for Instagram''s 3:4 grid.'
- 'R-ASPECT: the delivered file is 3:4 within 1%.'
- 'R-PLATE: exactly one saturated plate with crisp edges. It bleeds off the edges its layout names, and covers 25–40% of the 4:5 crop on singles and covers. Inner slides are exempt.'
- 'R-GLOW: glow appears only on the plate, directly behind the glass piece. Nothing blooms onto the page, there are no aura blobs, and no glow sits behind any label.'
- 'R-DIAGRAM-COUNT: nodes, tracks, tiles, blocks, branches, rows and rings match the numbers in the prompt exactly.'
- 'R-DIAGRAM-GEOMETRY: connectors are only horizontal or vertical, with right-angle turns. No diagonal or curved connectors, no free-floating network, no line crossing any text.'
- 'R-LABELS: each label sits at its correct node or block, in white bold, wholly over a deep plate stop. The sampled luminance behind each label is 0.21 or less, so it is not over #00ACB3, cyan or mint. Labels are complete, and every node is labelled or is a counted progress marker.'
- 'R-GLASS-ONE: exactly one frosted-glass piece, in the mood''s counter-accent hue (lagoon on royal plates, sky-blue on lagoon plates), at the active element. Nothing else is dimensional.'
- 'R-COUNTER-ACCENT: hue sampling finds both the royal-blue and the teal family. The post is not single-hue.'
- 'R-AI-GENERIC: none of the following: glossy chrome or plastic sheen, a saturated symmetrical 3D hero, extra floating cards or panels, bokeh, sparkles, lens flares or light trails. Fine grain is visible at 100% zoom.'
- 'R-NOT-GREEN: no region larger than 0.5% of the frame with hue between 70° and 150° and saturation above 40%. Mint must not read as green, and there is no lime.'
- 'R-BANNED-IMAGERY: no people, hands or faces; no robots, brains, lightbulbs, handshakes, coins, growth arrows, rockets or plants; no third-party logos, product UI or screenshots.'
- 'R-ACCENT-BAR: present directly under the lead text, in the brand gradient #416D95 → #74AFAD (ΔE of 10 or less at both ends).'
- 'R-HIGHLIGHT: exactly one highlight span, on the specified words, in the mood''s gradient. No other coloured text.'
- 'R-INK: the headline is near-black (light) or white (dark). No cyan, mint, sage or polar text on a light page. The URL and source line sit on the plain page.'
- 'R-GATE-LIGHT-v2: mean luminance of 0.55 or more; 6% or fewer of pixels below luminance 0.10, counted outside OCR text boxes; no fill darker than the mood''s darkest plate stop, except text.'
- 'R-GATE-DARK-v2: mean luminance of 0.15 or less; pixels above luminance 0.50 cover 2–25% of the frame (the plate counts as mass, not glow); no drop shadows.'
- 'R-NUMBERS-TRUTH: the bar fill is within ±3% of the stated share, measured to the centre of the glass bead. The ratio ring count matches. FIGURE-SIGNATURE posts draw no proportion. The figure string matches the bank item exactly.'
- 'R-INFO-ADDS: the plate labels add facts the headline does not state (less than 50% content-word overlap with the headline).'
- 'R-BRIEF-FIT-3S: a blind judge sees the image without its caption and states the post''s point in one sentence. It must match the post file''s visual_logic.'
- 'R-THUMBNAIL-360: at 360 px wide, the first headline line is legible and the day''s mood family is clear from colour alone.'
- 'R-GRID-FIT: rendered with the last 8 published posts as a 3×3, no row or column holds 3 tiles of the same mood, and no tile shares its layout with the previous day''s.'
- 'R-CAROUSEL-SET: every slide keeps one mood, the same type scale and the fixed positions (logo top-left, counter top-right, band progress line, URL bottom-left, source line above the URL). The progress-line node matches the slide number.'
- 'R-FRAME: on Grow photo posts, the frame rectangle is empty and flat before compositing. The composited image is the real inbox file, unaltered.'
- 'R-SHARP: Laplacian sharpness is above a calibrated floor and luminance is within the mood''s band. This catches blur and washed-out 2K/4K outputs.'
- 'R-WATERMARK: no visible watermark inside the 4:5 crop or the 3:4 Instagram frame.'
score: scroll-stop 1-5; pass needs 3 or more
template_acceptance: 50% or more of outputs pass over 8 outputs (two runs of 4), on two different topics
failure_classes:
- '[prompt]: fix the template'
- '[variance]: run-to-run randomness, handled by generate-4-and-select'
- '[concept]: change or drop the post type'
```

**Still TBD:** the vision-model judge prompt, and scripted versions of the OCR, pixel and gate checks.

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
- `[decided]` **No pricing-type content** (user, 2026-10-08): no prices, rates, payment terms or schedules, milestone payments, estimates, costs or engagement-model commercial terms in any post. F12 and F13 stay true facts but are never post topics.
- `[decided]` **The information on a single post must be useful on its own** (user, 2026-10-08: "the data should be more useful… this doesn't even serve purpose"). The payload is something a founder (or a student, on Grow posts) would save: a checklist, steps, a definition with a concrete example, a decision rule, or a sourced number with its meaning. Company-process trivia never qualifies.
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
| 2026-10-08 | §5.7 VISUAL-SYSTEM-v1 PAUSED: the taste round L1 user ratings put the SCHEMATIC look at 2/10 and the type-led Swiss poster at 7/10. §9: no pricing-type content; on-image information must be useful on its own (user) | Taste Lab ratings and notes; `learnings/taste.md`; user message 2026-10-08 |
| 2026-10-07 | §4 ON-IMAGE-v1 (single posts carry a labelled diagram; caption-complement rules C1–C7); §5.7 VISUAL-SYSTEM-v1 "SCHEMATIC, editorial finish" (day map with one dark Saturday, 4 layouts + slide, a diagram family per lane, counter-accent glass) supersedes the THEMES-v1 week map; §6 STYLE-BLOCK-v1, PROMPT-SKELETON-v1, PROMPT-RULES-v1, GENERATION-v1, REF-PACK-v2; §8 VISUAL-RUBRIC-v1; §7 done criterion via the 5-persona writing panel | User feedback on round 2; visual workflow (3 art directors, 4 judges); `brand/visual/visual-system-v1-draft.yaml` |
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

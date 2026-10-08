# Trend bank (timely items)

**What it's for:** timely facts for Tech, Explained. The Monday roundup ("This Week in Tech") draws from it, and the Thursday carousel uses it when a trend item fits its lane (`STYLE_GUIDE.md` §3 `CONTENT-MIX-v2` → `timely`).

**Rules:** `STYLE_GUIDE.md` §2.3 `EXTERNAL-SOURCES-v1`.
- **Primary sources only.** An item is `checked` only after its primary page was opened and the claim found on it.
- **Only `checked` items may be used in posts.** `pending-check` items are leads, not facts.
- **Expiry:** an item expires 14 days after the source's publication date.
- **When a post uses an item:** set `status: used` and add `used_in: posts/<file>.md`.

**Who writes here:**
- the Saturday research run (every Saturday, 09:59 PKT)
- from launch, a daily run
- a human, when an item comes from the inbox

Each drop is a dated section with one YAML block. Old drops stay, as the audit trail.

---

## Drop 2026-10-06 (manual, first drop)
**Network note:** this environment's egress proxy blocked every primary source tried except anthropic.com: stackoverflow.blog, github.blog, blog.cloudflare.com, blog.google, openai.com, arxiv.org, huggingface.co and survey.stackoverflow.co.

That's why this drop is lopsided:
- **checked:** only the items whose primary page could be read (both Anthropic announcements)
- **pending-check:** everything else

**Balance:** a real roundup should not lean on one company. `CONTENT-MIX-v2` → `no_repeat.one_company_per_week` caps one outside company at 2 items across the week's two external carousels. The Saturday run should rebalance once the user allows the source domains.

```yaml
- id: T-2026-10-06-01
  lane: trends
  claim: "Anthropic is committing $100 million to train 10,000 Frontier Deployed Engineers by the end of 2027, through a program called Claude Frontier Academy, with cohorts in San Francisco, New York and London."
  why_it_matters_to_founders: "The hard part of AI projects is shifting from the model to the people who can deploy it inside a real business."
  source_name: "Anthropic"
  source_url: "https://www.anthropic.com/news/claude-frontier-academy"
  source_type: official
  published: "2026-10-02"
  retrieved: "2026-10-06"
  expires: "2026-10-16"
  status: checked
  take_hint: "Before you buy an AI tool, decide who owns deploying it, measuring it and fixing it."
  verbatim_support:
    - "to train 10,000 Frontier Deployed Engineers (FDEs) by the end of 2027"
    - "Cohorts are running in San Francisco, New York and London."

- id: T-2026-10-06-02
  lane: numbers
  claim: "Barclays expects Claude Code adoption to reach 50% of its developer population by the end of 2026, rising to a majority of its software engineers in 2027."
  why_it_matters_to_founders: "Large, regulated companies are now planning AI coding tools into how their whole engineering workforce works, not trialling them on the side."
  source_name: "Anthropic"
  source_url: "https://www.anthropic.com/news/barclays-scales-claude"
  source_type: official
  published: "2026-10-01"
  retrieved: "2026-10-06"
  expires: "2026-10-15"
  status: checked
  take_hint: "AI makes code faster to write. Review, tests and clear ownership decide whether it ships safely."
  note: "A customer story published by the vendor. Write 'Barclays expects', never 'Barclays has'."
  verbatim_support:
    - "Claude Code adoption to reach 50% of its developer population by the end of 2026, rising to a majority of software engineers in 2027"

- id: T-2026-10-06-03
  lane: trends
  claim: "Cloudflare released two open-weight 'decision' models, Clef and Clef-flash, on Workers AI, built for fast structured calls such as classifying or routing a request."
  why_it_matters_to_founders: "Not every AI feature needs a frontier model. Small, cheap models for narrow decisions are becoming a standard building block."
  source_name: "Cloudflare"
  source_url: null            # exact blog post URL not yet read
  source_type: official
  published: "2026-10-01"     # per search summaries; confirm on the primary post
  retrieved: null
  expires: "2026-10-15"
  status: pending-check
  take_hint: "Match the model to the job: a narrow decision rarely needs the biggest model."
  note: "Found only through search summaries; blog.cloudflare.com was blocked. Parameter counts and prices in the summaries must not be used until the primary post is read."

- id: T-2026-10-06-04
  lane: numbers
  claim: "Stack Overflow published a look-back at its past Developer Survey findings ahead of the 2026 results."
  why_it_matters_to_founders: "The survey is the standard yardstick for how developers actually use AI tools."
  source_name: "Stack Overflow"
  source_url: "https://stackoverflow.blog/2026/09/30/getting-ready-for-2026-results-a-look-back-on-developer-survey-findings/"
  source_type: official
  published: "2026-09-30"
  retrieved: null
  expires: "2026-10-14"
  status: pending-check
  take_hint: "Adoption is high, trust is lower. Build review into how your team uses AI."
  note: "Search summaries quote AI-usage percentages from this post. None may be used until the page itself is read (stackoverflow.blog was blocked). When the 2026 survey results publish, they become a By the Numbers source in their own right."

- id: T-2026-10-06-05
  lane: trends
  claim: "OpenAI held DevDay 2026 on 29 September in San Francisco, and the announcements centred on agents that keep working on ongoing tasks rather than single prompt-and-response exchanges."
  why_it_matters_to_founders: "Products are moving from 'ask and answer' to 'delegate and check'. That changes what you design, test and pay for."
  source_name: "OpenAI"
  source_url: "https://openai.com/index/devday-2026-recap/"
  source_type: official
  published: "2026-09-29"
  retrieved: null
  expires: "2026-10-13"
  status: pending-check
  take_hint: "An agent is only as good as its limits: what it may touch, when it must ask, how you check its work."
  note: "Found via search results only; openai.com was blocked. Model names, user numbers and prices from the summaries must not be used until the recap page is read."

- id: T-2026-10-06-06
  lane: trends
  claim: "From 30 September, Google requires verified-developer registration for installing and updating apps from participating stores on certified Android devices in Brazil, Indonesia, Singapore and Thailand."
  why_it_matters_to_founders: "If you ship an Android app, developer identity is becoming part of distribution, starting in four countries."
  source_name: "Google (Android Developers)"
  source_url: null            # primary page not yet read
  source_type: official
  published: "2026-09-30"     # effective date per search summaries; confirm on the primary page
  retrieved: null
  expires: "2026-10-14"
  status: pending-check
  take_hint: "Put store accounts and signing keys in the company's name, not a freelancer's."
  note: "Found via a search summary only. Confirm the countries, the date and the scope on Google's own Android developer pages before use."

- id: T-2026-10-06-R1
  lane: ai
  claim: "Google announced a model called 'Gemini 4 Argon' on 30 September 2026."
  source_name: null
  source_url: null
  source_type: null
  published: null
  retrieved: null
  expires: null
  status: rejected
  note: "One search summary stated this. A second search found no official announcement; Google's own blog could not be read here. Kept as the example of why second-hand claims are banned."
```

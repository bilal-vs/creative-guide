# Trend bank (timely items)

**What it's for:** timely facts for Tech, Explained. The Monday roundup ("This Week in Tech") draws from it, and other lanes use it when a trend item fits (`STYLE_GUIDE.md` §3 `CONTENT-MIX-v1` → `timely`).

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

**Balance:** a real roundup should not lean on one company. `CONTENT-MIX-v1` caps one company as the main subject at 2 posts a week. The Saturday run should rebalance once the user allows the source domains.

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

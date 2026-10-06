# Writing practice · Round 2 · One full pack per lane

**Date:** 2026-10-06
**Goal:** test the copy system on all 9 lanes before any of it becomes `STYLE_GUIDE.md` §7 templates. Each pack is complete except for the visual: on-image text, LinkedIn caption, Instagram caption, hashtags, alt text and the Verdant take.

**Rules applied:**
- `STYLE_GUIDE.md` §3 `CONTENT-MIX-v1`, §4 recipes, §4.1 `CAROUSEL-v2`, §7 decided rules, `HASHTAGS-v1`, `BANNED-WORDS-v1`
- §2.3 `EXTERNAL-SOURCES-v1`
- `brand/strategy.md` v2 §5

**How to review:** on the review page, mark each part Keep or Kill, with an optional note.
- **Done** = two rounds in a row at ≥ 80% Keep, with no truth or voice failures. Then the rules move into §7.
- **Checks:** run `python3 tools/check_packs.py writing/round-02-lane-packs.md` for word counts, emoji, hashtags, banned words and numbers.

**The week these packs simulate:** cycle week 1 (week A), so Monday and Wednesday are carousels. Packs 4 and 6 are the week-B alternates for Tuesday and Thursday.

**Headline mix in week A:** problem/curiosity on Mon, Wed, Fri and Sun (4 of 7, 57%). The other days use rhythm (Tue), quote (Thu) and fact (Sat). No formula runs three days in a row, and no opening word repeats on consecutive days.

**Questions:** packs 1, 6 and 7 (3 of 9).
**Direct CTA:** packs 3 and 5 only.

> **Source caveat:** this environment blocked every primary source except anthropic.com.
> - **Checked:** only the two Anthropic items (`T-2026-10-06-01`, `-02`).
> - **Pack 1** uses three `pending-check` items to show the roundup format. Those items are **practice only and not publishable** until their primary pages are read.
> - **Pack 8** uses a checked item, but it is a vendor's customer story.
> - Once the source domains are allowed, the Saturday run will balance the companies covered.

---

## Pack 1 · Mon · This Week in Tech · carousel (roundup)
<!-- pack: P1 -->
```yaml
id: P1
day: Mon
lane: trends
series: "This Week in Tech"
format: carousel
variant: roundup
topic: "Week of 29 Sep to 5 Oct 2026"
sources: [T-2026-10-06-05, T-2026-10-06-01, T-2026-10-06-03, T-2026-10-06-06]
status_note: "PRACTICE ONLY: items from OpenAI, Cloudflare and Google are pending-check"
headline_formula: problem-curiosity
question: true
cta: soft
slides:
  - { n: 1, role: cover, pill: "This Week in Tech", headline: "The part of AI [nobody budgets for]", body: "Four updates from this week, and what they mean for you.", extra: "Swipe" }
  - { n: 2, role: item, headline: "Agents that [keep working]", body: "OpenAI's DevDay centred on agents that carry on with ongoing tasks, not one-off answers. For founders: design for delegating and checking, not just chatting.", source_line: "Source: OpenAI, 2026 [PENDING CHECK]" }
  - { n: 3, role: item, headline: "The new gap is [deployment]", body: "Anthropic is committing $100 million to train 10,000 engineers who deploy AI inside companies, by the end of 2027. The hard part is now the rollout.", source_line: "Source: Anthropic, 2026" }
  - { n: 4, role: item, headline: "Small models for [narrow decisions]", body: "Cloudflare released two open-weight 'decision' models built for quick, structured calls like routing or classifying a request. Not every feature needs the biggest model.", source_line: "Source: Cloudflare, 2026 [PENDING CHECK]" }
  - { n: 5, role: item, headline: "Android starts [verifying developers]", body: "Google now requires verified-developer registration for app installs and updates on certified Android devices in Brazil, Indonesia, Singapore and Thailand. Keep store accounts in your company's name.", source_line: "Source: Google, 2026 [PENDING CHECK]" }
  - { n: 6, role: our-take, headline: "Our take: [own the rollout]", body: "Models get cheaper and smarter every month. What decides success is who owns deployment, accounts and checks. Name that person before you buy the tool.", extra: "Follow for next Monday's roundup." }
  - { n: 7, role: receipt, headline: "This week in [four lines]", list: ["Agents that keep working on tasks (OpenAI)", "$100M for AI deployment skills (Anthropic)", "Small open models for quick decisions (Cloudflare)", "Android developer verification begins (Google)"], extra: "Save this · verdant-soft.com" }
linkedin: |
  The part of AI nobody budgets for isn't the model. It's the rollout.

  Four updates from this week, and what each one means if you're building a product:

  1. OpenAI's DevDay centred on agents that keep working on ongoing tasks. Expect to design for delegating and checking, not just chatting.
  2. Anthropic is committing $100 million to train 10,000 engineers who deploy AI inside companies, by the end of 2027. Deployment skill is now the scarce part.
  3. Cloudflare released two small open-weight models for quick, structured decisions. Not every feature needs the biggest model.
  4. Google now requires verified-developer registration for Android app installs and updates in Brazil, Indonesia, Singapore and Thailand.

  Our take: models will keep getting cheaper and better. What decides whether AI works in your business is who owns the rollout: the accounts, the limits and the checks. Name that person before you pick the tool.

  Who owns AI rollout in your company today?

  Sources: OpenAI · [URL pending check]
  Anthropic · https://www.anthropic.com/news/claude-frontier-academy
  Cloudflare · [URL pending check]
  Google · [URL pending check]
  #VerdantSoft #TechNews #ArtificialIntelligence
instagram: |
  The part of AI nobody budgets for: the rollout.

  This week brought agents that keep working, $100M for AI deployment skills, small models for quick decisions, and Android developer verification in four countries.

  Our take: name who owns the rollout before you pick the tool.

  Sources: OpenAI, Anthropic, Cloudflare, Google. Follow for next Monday's roundup.

  #VerdantSoft #TechNews #ArtificialIntelligence #StartupFounder #SoftwareDevelopment
alt_text:
  - "Cover reading: The part of AI nobody budgets for. Four updates from this week."
  - "OpenAI's DevDay focused on AI agents that keep working on ongoing tasks."
  - "Anthropic is committing 100 million dollars to train 10,000 engineers who deploy AI in companies."
  - "Cloudflare released two small open models for quick, structured decisions."
  - "Google now requires verified Android developers in Brazil, Indonesia, Singapore and Thailand."
  - "Our take: decide who owns the AI rollout before choosing a tool."
  - "A four-line summary of this week's updates, with verdant-soft.com."
```
**Notes:**
- **Why this cover:** it turns four unrelated news items into one founder problem, the rollout. Without it, the roundup reads like a news feed.
- **Company cap:** three of the four items name a different company, so the "same company at most twice a week" rule holds.

---

## Pack 2 · Wed · AI, Explained · carousel (external)
<!-- pack: P2 -->
```yaml
id: P2
day: Wed
lane: ai
series: "AI, Explained"
format: carousel
variant: external
topic: E-AI-01
sources: []
term: "hallucination"
headline_formula: problem-curiosity
question: false
cta: soft
slides:
  - { n: 1, role: cover, pill: "AI, Explained", headline: "Why AI [makes things up]", body: "And how good products stop it.", extra: "Swipe" }
  - { n: 2, role: payoff, headline: "It's predicting, [not looking up]", body: "A language model writes the most likely next words, based on patterns it learned. When it doesn't know, it can still sound sure. That's called a hallucination." }
  - { n: 3, role: step, headline: "Fix 1: [give it sources]", body: "Let the model look up your own documents first, then answer only from what it found.", bridge: "But sources alone aren't enough." }
  - { n: 4, role: step, headline: "Fix 2: allow [I don't know]", body: "Tell it to admit when the answer isn't in its sources. A clear 'not sure' serves your users better than a confident guess.", bridge: "Then prove it works." }
  - { n: 5, role: step, headline: "Fix 3: [test before launch]", body: "Keep a set of real questions with known answers. Run them on every change. If the score drops, the release waits.", bridge: "So where do you start?" }
  - { n: 6, role: our-take, headline: "Our take: [design for doubt]", body: "Don't only ask whether the AI is accurate. Ask what happens when it's wrong, and design that moment first: what the user sees, and who fixes it." }
  - { n: 7, role: action, headline: "Save this for [your AI build]", body: "Follow AI, Explained: a new one every Wednesday." }
  - { n: 8, role: receipt, headline: "Stop AI [making things up]", list: ["Know why: it predicts, it doesn't look up", "Give it sources to answer from", "Let it say 'I don't know'", "Test real questions on every change"], extra: "Save this · verdant-soft.com" }
linkedin: |
  AI doesn't lie. It predicts.

  A language model writes the most likely next words, based on patterns from its training. Most of the time that's useful. When it doesn't know something, it still produces likely-sounding words, and they can be wrong. That's a hallucination: a confident answer with nothing behind it.

  You can't switch it off, but you can design around it:
  - Give it sources. Let it look up your own documents before it answers, and answer only from them.
  - Let it say "I don't know." A clear "not sure" serves your users better than a confident guess.
  - Test before launch. Keep a set of real questions with known answers, and run them on every change.

  Our take: the useful question isn't only "is the AI accurate?" It's "what happens when it's wrong?" Design that moment first: what the user sees, who gets alerted, and how it gets fixed.

  Swipe through for the version you can save.
  #VerdantSoft #ArtificialIntelligence #LLM
instagram: |
  AI doesn't lie. It predicts.

  When a model doesn't know something, it still writes likely-sounding words. That's a hallucination.

  Three fixes: give it sources, let it say "I don't know", and test with real questions before every release.

  Our take: design for the moment it's wrong, before it happens.

  Save this for your next AI build.

  #VerdantSoft #ArtificialIntelligence #LLM #MachineLearning #AIExplained
alt_text:
  - "Cover reading: Why AI makes things up, and how good products stop it."
  - "AI predicts likely words instead of looking facts up, which causes hallucinations."
  - "Fix one: give the AI your own documents to answer from."
  - "Fix two: allow the AI to say it doesn't know."
  - "Fix three: test with real questions before every launch."
  - "Our take: design for the moment the AI is wrong."
  - "Save this and follow AI, Explained every Wednesday."
  - "A four-point checklist for stopping AI from making things up."
```
**Notes:**
- **One term:** "hallucination", defined on slide 2. "Retrieval" is described but deliberately not named, to keep to one term.
- **No numbers anywhere,** so there is nothing to source.

---

## Pack 3 · Tue (wk A) · How we work · Outsourcing, Decoded · single
<!-- pack: P3 -->
```yaml
id: P3
day: Tue
lane: how-we-work
series: "Outsourcing, Decoded"
format: single
topic: V-HWW-01
sources: [F12, F11]
headline_formula: rhythm
question: false
cta: direct
on_image:
  pill: "Outsourcing, Decoded"
  headline: "Kickoff. Key phases. Delivery. That's when [you pay]."
  subline: "How payments work with us."
  source_line: null
linkedin: |
  Paying a remote team for work you can't see yet is the biggest leap in outsourcing. So here is exactly how payments work with us.

  Verdant Soft works on a milestone-based payment schedule. You pay at three points:

  1. Project initiation.
  2. Key development phases.
  3. Final delivery.

  Each payment lines up with a stage of the work. Your budget moves as the product moves, and you always know what the next payment is for.

  It's one of the questions in our FAQ for a reason: a clear payment structure is part of a clear project. If a team can't tell you when and why you pay, ask how they plan the rest of the work.

  Planning a build? Book a call at verdant-soft.com and bring your questions about scope and payments.

  #VerdantSoft #SoftwareOutsourcing #ProductDevelopment
instagram: |
  Kickoff. Key phases. Delivery. That's when you pay.

  We work on a milestone-based schedule: payments at project initiation, at key development phases and at final delivery. Each one lines up with a stage of the build.

  Planning a product? Book a call at verdant-soft.com.

  #VerdantSoft #SoftwareOutsourcing #DedicatedTeam #ProductDevelopment #SoftwareHouse
alt_text:
  - "Post reading: Kickoff. Key phases. Delivery. That's when you pay. How payments work with us."
```
**Notes:**
- **Truth check:** F12 is stated plainly.
- **FAQ wording, checked:** the audit shows "How do payments work?" is the fourth FAQ question (`brand/audit-raw.md`, shared FAQ block). So the caption says "one of the questions in our FAQ", not "the first".

---

## Pack 4 · Tue (wk B) · Build Notes · single
<!-- pack: P4 -->
```yaml
id: P4
day: Tue-B
lane: build-notes
series: "Build Notes"
format: single
topic: V-BN-01
sources: [F39]
headline_formula: imperative
question: false
cta: soft
on_image:
  pill: "Build Notes"
  headline: "Isolate tenants [before you scale] them"
  subline: "A lesson from multi-tenant data platforms."
  source_line: null
linkedin: |
  In a multi-tenant platform, every customer shares the same system. The one thing they must never share is data.

  That sounds obvious until the platform grows. One missing filter in one query, and a customer sees a record that isn't theirs. One heavy sync job, and every other tenant waits.

  That's why isolation is a day-one decision, not a later fix:
  - Every record carries its tenant, and every query is scoped to it by default, not by memory.
  - Each tenant's sync and ETL jobs run in their own lane, so one big import can't stall everyone else.
  - Credentials and connections are stored per tenant, never shared.

  Verdant Soft contributed to a scalable, multi-tenant integration platform for data synchronization and ETL workflows, built in Python. On platforms like that, the boundaries you draw early decide how safely you can add customers later.

  Building a multi-tenant product? Save this for your architecture review.

  #VerdantSoft #SoftwareEngineering #SystemDesign
instagram: |
  Isolate tenants before you scale them.

  In a multi-tenant platform, customers share the system but must never share data. Scope every query to its tenant by default, give each tenant's jobs their own lane, and store credentials per tenant.

  We contributed to a scalable, multi-tenant platform for data sync and ETL workflows, built in Python.

  Save this for your next architecture review.

  #VerdantSoft #SoftwareEngineering #SystemDesign #BackendDevelopment #CloudComputing
alt_text:
  - "Post reading: Isolate tenants before you scale them. A lesson from multi-tenant data platforms."
```
**Notes:**
- **The three bullets are general engineering advice,** not claims about what that project did. The case-study page doesn't state its design decisions, so the post keeps "contributed to" exactly (F39).

---

## Pack 5 · Thu (wk A) · Proof · Client words · single
<!-- pack: P5 -->
```yaml
id: P5
day: Thu
lane: proof
series: "Client words"
format: single
topic: V-PR-01
sources: [P07]
headline_formula: quote
question: false
cta: direct
on_image:
  pill: "Client words"
  headline: "They quickly [understood our problem], collaborated effectively with our team, and delivered a solid solution."
  subline: "Isana Sebastian"
  source_line: null
linkedin: |
  Before we write code, we work to understand the problem behind the brief. Here's how one client described working with us:

  "They quickly understood our problem, collaborated effectively with our team, and delivered a solid solution."
  Isana Sebastian

  That sentence covers three of the things founders worry about most when they hire a remote team: being understood, being included, and getting something that works.

  Understanding comes first in how we run projects. Our UI/UX process starts with research and discovery, before anything is designed or built. We'd rather ask one more question at the start than rebuild a feature at the end.

  If that's the kind of partner you're looking for, book a call at verdant-soft.com. Bring the brief, or just the problem. We'll start with questions.

  #VerdantSoft #ClientStories #SoftwareDevelopment
instagram: |
  "They quickly understood our problem, collaborated effectively with our team, and delivered a solid solution."
  Isana Sebastian

  Understood, included, delivered: three of the things founders worry about when they hire a remote team.

  Planning a build? Book a call at verdant-soft.com.

  #VerdantSoft #ClientStories #SoftwareDevelopment #SoftwareOutsourcing #ProductDevelopment
alt_text:
  - "Client quote from Isana Sebastian: They quickly understood our problem, collaborated effectively with our team, and delivered a solid solution."
```
**Notes:**
- **Quote:** P07 `quote_verbatim`, character for character. The attribution is the name only, as in PUBLIC-PROOF.
- **Word cap:** a Proof quote is exempt from the 8-word headline cap (§4 recipe). The highlight is 3 words.
- **Facts used:** the research step is F04.

---

## Pack 6 · Thu (wk B) · Grow with us · Grow at Verdant · single
<!-- pack: P6 -->
```yaml
id: P6
day: Thu-B
lane: grow-with-us
series: "Grow at Verdant"
format: single
topic: V-GW-01
sources: [F05]
headline_formula: plain
question: true
cta: soft
on_image:
  pill: "Grow at Verdant"
  headline: "The stack [you'd work with] here"
  subline: "React, Next.js, Node.js, Python, PostgreSQL and more."
  source_line: null
linkedin: |
  If you're starting out in software, the useful question isn't which language is best. It's which tools real products are built with.

  Here's the stack we list across our services and case studies:
  - Front end: React, Next.js and Vue.
  - Back end: Node.js with Express or NestJS, Python with Django, and PHP.
  - Data: MySQL, PostgreSQL, MongoDB, Amazon Aurora and SQLite.

  You don't need all of it on day one. Pick one front end, one back end and one database, and build one thing end to end, from the first screen to the stored data. You'll learn more from that than from another tutorial.

  Studying computer science or just graduated? Follow Grow at Verdant for skills, tools and what software work actually looks like.

  Which part of the stack are you learning right now?

  #VerdantSoft #CareersInTech #LahoreTech
instagram: |
  The stack you'd work with here.

  Front end: React, Next.js, Vue. Back end: Node.js, NestJS, Express, Django, PHP. Data: PostgreSQL, MySQL, MongoDB and more.

  Starting out? Pick one of each and build something end to end. It beats another tutorial.

  Which part are you learning right now? 💻

  #VerdantSoft #CareersInTech #LahoreTech #PakistanTech #SoftwareEngineer
alt_text:
  - "Post reading: The stack you'd work with here. React, Next.js, Node.js, Python, PostgreSQL and more."
```
**Notes:**
- **Facts:** F05 only.
- **Promises:** no culture or career claims, since none are in FACTS. It's warmer through advice, not promises.

---

## Pack 7 · Fri · Founder Notes · single
<!-- pack: P7 -->
```yaml
id: P7
day: Fri
lane: startup
series: "Founder Notes"
format: single
topic: E-FN-01
sources: []
headline_formula: problem-curiosity
question: true
cta: soft
on_image:
  pill: "Founder Notes"
  headline: "When your MVP [stops being minimal]"
  subline: "Scope it around one job."
  source_line: null
linkedin: |
  An MVP has one purpose: to prove that people want the thing. Every extra feature delays that proof.

  It usually starts with reasonable requests. A dashboard, because investors like dashboards. Social login, because users expect it. An admin panel, just in case. Each one is small. Together they push your first real user further away.

  A simple test before anything goes in:
  - What is the one job a user hires this product to do?
  - Does this feature help that job get done, or measure whether it did?
  - If not, it waits for version two.

  Our take: write that one job on the first page of your brief. Every scope decision after it gets easier, for you and for whoever builds it.

  What's one feature you were glad you cut?

  #VerdantSoft #Startups #ProductDevelopment
instagram: |
  When your MVP stops being minimal.

  An MVP exists to prove people want the thing. Every extra feature delays that proof. Before adding one, ask: does it help the user's one job get done? If not, it waits for version two.

  Our take: write the one job on the first page of your brief.

  Save this for your next scoping call.

  #VerdantSoft #Startups #ProductDevelopment #StartupFounder #MVP
alt_text:
  - "Post reading: When your MVP stops being minimal. Scope it around one job."
```

---

## Pack 8 · Sat · By the Numbers · single
<!-- pack: P8 -->
```yaml
id: P8
day: Sat
lane: numbers
series: "By the Numbers"
format: single
topic: "Barclays' planned AI coding adoption"
sources: [T-2026-10-06-02]
headline_formula: fact
question: false
cta: soft
on_image:
  pill: "By the Numbers"
  headline: "[50%]"
  subline: "of Barclays' developers expected to use Claude Code by end-2026"
  source_line: "Source: Anthropic, 2026"
linkedin: |
  50%. That's the share of its developers Barclays expects to be using Claude Code by the end of 2026, rising to a majority of its software engineers in 2027.

  When a bank plans AI coding tools into its whole engineering workforce, they're no longer an experiment. They're part of how software gets made.

  For founders, the question has changed. It isn't "should our team use AI to write code?" It's "how do we keep quality and ownership when they do?"

  The tools change how fast code appears. They don't change who is responsible for it.

  Our take: AI makes code faster to write, not automatically safe to ship. Keep code review, automated tests and a clear owner for every change, however the code was written.

  Source: Anthropic · https://www.anthropic.com/news/barclays-scales-claude
  #VerdantSoft #TechTrends #Startups
instagram: |
  50% of Barclays' developers are expected to be using Claude Code by the end of 2026.

  When a bank plans AI coding into its whole engineering team, it's past the experiment stage.

  Our take: AI makes code faster to write, not safe to ship. Keep review, tests and a clear owner.

  Source: Anthropic

  #VerdantSoft #TechTrends #Startups #SoftwareDevelopment #StartupFounder
alt_text:
  - "Large figure 50 percent: the share of Barclays' developers expected to use Claude Code by the end of 2026. Source: Anthropic, 2026."
```
**Notes:**
- **Wording:** "expects" and "expected", as the item's note requires. The number and its timing are copied from the checked item.
- **Bias flag:** the source is the vendor. Once more domains are open, prefer an independent survey for By the Numbers (E-NUM bank).

---

## Pack 9 · Sun · Under the Hood · single
<!-- pack: P9 -->
```yaml
id: P9
day: Sun
lane: concepts
series: "Under the Hood"
format: single
topic: E-CON-01
sources: []
term: "API"
headline_formula: problem-curiosity
question: false
cta: soft
on_image:
  pill: "Under the Hood"
  headline: "What an API [actually is]"
  subline: "A menu for software, explained for founders."
  source_line: null
linkedin: |
  An API is a menu one piece of software offers another.

  The menu lists what you can ask for (create an order, fetch a customer, send a message) and exactly how to ask. The kitchen behind it stays private. That's an API, or application programming interface: a defined way for one system to request things from another.

  Why it matters when you plan a product:
  - An integration is only as good as the other side's menu. If a tool has no API for what you need, no developer can wish one into existence.
  - Your own product may need a menu too, for your mobile app, partners or future integrations.
  - Menus change. Good integrations plan for new versions and usage limits from the start.

  Our take: before you commit to a third-party tool, ask to see its API documentation. A short look now is cheaper than a workaround later.

  Save this for your next scoping session.
  #VerdantSoft #SoftwareEngineering #TechExplained
instagram: |
  What an API actually is: a menu for software.

  It lists what one system can ask another for, and exactly how to ask, while the kitchen stays private.

  Planning a product that connects to other tools? Check each tool's API documentation before you commit.

  Our take: a short look now is cheaper than a workaround later.

  Save this for your next scoping call. 🧩

  #VerdantSoft #SoftwareEngineering #TechExplained #WebDevelopment #StartupFounder
alt_text:
  - "Post reading: What an API actually is. A menu for software, explained for founders."
```

---

## Feedback
_Waiting for the user's marks on the review page. Results are copied here after the review._

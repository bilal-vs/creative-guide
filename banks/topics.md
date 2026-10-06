# Topic bank (evergreen)

**What it's for:** evergreen topics for every lane. The pipeline uses one when no inbox item, calendar moment, timely trend item or due series episode claims the slot (`STYLE_GUIDE.md` §3 `CONTENT-MIX-v1` → `priority`).

**Rules:**
- **No-repeat:** a lane topic is not reused within 90 days (`no_repeat`).
- **Numbers** must come from `FACTS` (confirmed) or from a source checked under `EXTERNAL-SOURCES-v1`, with that source on the image and in the caption.
- **The "term" field** is the one technical term the post defines in a single plain line.
- **Verdant topics** cite their FACTS ids.
- **Build Notes** may describe only what the case-study page states. When the page doesn't state the engineering decision, the post frames general engineering advice ("what this kind of build has to get right"), plus the fact of what we built (F-id, scope words exact).

**Status:**
- `ready`: usable
- `needs-source`: a numbers topic whose primary source has not been read yet; not usable
- `used`: add the post file

**Refresh:** monthly, plus the Saturday run's suggestions. Version: 2026-10-06.

---

## Tech, Explained (external, written for founders)

### AI, Explained (`ai`)
```yaml
- { id: E-AI-01, topic: "Why AI chatbots make things up", term: "hallucination", angle: "A model predicts likely words; it doesn't look facts up unless you make it", status: ready }
- { id: E-AI-02, topic: "Why long AI chats forget the beginning", term: "context window", angle: "The model only sees a fixed amount of text at once", status: ready }
- { id: E-AI-03, topic: "How AI answers from your own documents", term: "RAG (retrieval-augmented generation)", angle: "Look up first, then answer: the pattern behind most business chatbots", status: ready }
- { id: E-AI-04, topic: "What an AI agent actually does", term: "agent", angle: "A model in a loop with tools: plan, act, check, repeat", status: ready }
- { id: E-AI-05, topic: "Why AI is priced per token", term: "token", angle: "What you pay for, and why long prompts cost more", status: ready }
- { id: E-AI-06, topic: "How you know an AI feature works before launch", term: "eval", angle: "Test sets for AI behaviour, the way unit tests work for code", status: ready }
- { id: E-AI-07, topic: "Prompting, RAG or fine-tuning: which one you need", term: "fine-tuning", angle: "Start cheap; move up only when the cheaper option fails", status: ready }
- { id: E-AI-08, topic: "How AI finds 'similar' things", term: "embedding", angle: "Meaning turned into numbers, so search can match ideas rather than exact words", status: ready }
```

### Under the Hood (`concepts`)
```yaml
- { id: E-CON-01, topic: "What an API actually is", term: "API", angle: "A menu one piece of software offers another", status: ready }
- { id: E-CON-02, topic: "Why the second page load is faster", term: "cache", angle: "Keeping a copy close so you don't fetch it again", status: ready }
- { id: E-CON-03, topic: "One app, many customers' data", term: "multi-tenancy", angle: "Shared platform, separated data; isolation is a design choice made early", status: ready }
- { id: E-CON-04, topic: "How code gets from a laptop to live", term: "CI/CD", angle: "Automatic checks and releases instead of manual uploads", status: ready }
- { id: E-CON-05, topic: "The loan you didn't know you took", term: "technical debt", angle: "Shortcuts are fine when they're chosen on purpose and paid back", status: ready }
- { id: E-CON-06, topic: "Why you never test on the live site", term: "staging environment", angle: "A copy of production where mistakes are free", status: ready }
- { id: E-CON-07, topic: "Asking every minute vs being told", term: "webhook", angle: "Polling vs push, and why it matters for sync and cost", status: ready }
- { id: E-CON-08, topic: "Why one database query crawls", term: "index", angle: "The book index analogy; what to ask your team when pages slow down", status: ready }
```

### Founder Notes (`startup`)
```yaml
- { id: E-FN-01, topic: "Scope your MVP around one job, not ten features", term: null, angle: "The smallest product that proves one thing", status: ready }
- { id: E-FN-02, topic: "What to have ready before you brief a dev team", term: null, angle: "Users, the one job, must-haves, constraints, examples you like", status: ready }
- { id: E-FN-03, topic: "Buy, build or integrate", term: null, angle: "Build only what makes you different", status: ready }
- { id: E-FN-04, topic: "Fixed scope or a dedicated team", term: null, angle: "Which fits which stage; our take may cite F13", facts: [F13], status: ready }
- { id: E-FN-05, topic: "Why 'small changes' after launch aren't small", term: null, angle: "Every change touches data, tests and users", status: ready }
- { id: E-FN-06, topic: "How to read a development estimate", term: null, angle: "Ask what's included, what's assumed and what's excluded", status: ready }
- { id: E-FN-07, topic: "Who should own your code, domains and cloud accounts", term: null, angle: "An ownership checklist before you sign anything", status: ready }
- { id: E-FN-08, topic: "Rebuild or refactor", term: null, angle: "Signs you need a rewrite, and signs you don't", status: ready }
```

### By the Numbers (`numbers`)
Evergreen numbers need a primary source read in full, ≤ 2 years old. Until a source is read, the topic is `needs-source`.
```yaml
- { id: E-NUM-01, topic: "How many developers use AI tools", candidate_source: "Stack Overflow Developer Survey 2025 results (survey.stackoverflow.co/2025); replace with 2026 results when published", status: needs-source }
- { id: E-NUM-02, topic: "How AI-assisted development affects delivery", candidate_source: "DORA report on AI-assisted software development (dora.dev)", status: needs-source }
- { id: E-NUM-03, topic: "The growth of open source and AI repositories", candidate_source: "GitHub Octoverse (github.blog/news-insights/octoverse)", status: needs-source }
- { id: E-NUM-04, topic: "How developers feel about trusting AI output", candidate_source: "Stack Overflow Developer Survey, AI section", status: needs-source }
- { id: E-NUM-05, topic: "Most-used databases among developers", candidate_source: "Stack Overflow Developer Survey, technology section", status: needs-source }
- { id: E-NUM-06, topic: "Most-used cloud platforms among developers", candidate_source: "Stack Overflow Developer Survey, technology section", status: needs-source }
```

### This Week in Tech (`trends`)
Always timely; there is no evergreen bank. It draws from `banks/trends.md`.

---

## Verdant Soft

### How we work: Outsourcing, Decoded / Wireframe to Production (`how-we-work`)
```yaml
- { id: V-HWW-01, series: "Outsourcing, Decoded", topic: "How payments work: milestones you can see", facts: [F12], status: ready }
- { id: V-HWW-02, series: "Outsourcing, Decoded", topic: "Can I hire you for just one service?", facts: [F15, F02], status: ready }
- { id: V-HWW-03, series: "Outsourcing, Decoded", topic: "Four ways to work with an outsourced team", facts: [F13], status: ready }
- { id: V-HWW-04, series: "Outsourcing, Decoded", topic: "Strategy to deployment under one roof", facts: [F14, F02], status: ready }
- { id: V-HWW-05, series: "Outsourcing, Decoded", topic: "How to start: book a call or send a brief", facts: [F11], status: ready }
- { id: V-HWW-06, series: "Wireframe → Production", topic: "UI/UX steps 1–2: research and personas", facts: [F04], status: ready }
- { id: V-HWW-07, series: "Wireframe → Production", topic: "UI/UX steps 3–4: wireframes and prototypes", facts: [F04], status: ready }
- { id: V-HWW-08, series: "Wireframe → Production", topic: "UI/UX steps 5–6: testing and iteration", facts: [F04], status: ready }
```

### Build Notes (`build-notes`)
```yaml
- { id: V-BN-01, topic: "Isolate tenants before you scale them (multi-tenant ETL)", facts: [F39], scope_words: "contributed to", status: ready }
- { id: V-BN-02, topic: "Keeping a Shopify store and a Vue app in sync", facts: [F36], status: ready }
- { id: V-BN-03, topic: "Building a design canvas in the browser", facts: [F38], status: ready }
- { id: V-BN-04, topic: "Parking sessions by zone", facts: [F33], status: ready }
- { id: V-BN-05, topic: "Roles first: an e-commerce CMS", facts: [F31], status: ready }
- { id: V-BN-06, topic: "Subscriptions inside a browser extension", facts: [F34], status: ready }
- { id: V-BN-07, topic: "Healthcare modules that must never be wrong (medications, allergies)", facts: [F30], scope_words: "built the … modules", status: ready }
- { id: V-BN-08, topic: "Infrastructure as code: why we write servers down", facts: [F06], status: ready }
```

### Proof: Client words / Project Spotlight (`proof`)
Client words use only `quotable` entries, verbatim. The same `client_key` is not reused within 30 days.
```yaml
- { id: V-PR-01, type: client-words, proof: P07, client_key: isana-sebastian, status: ready }
- { id: V-PR-02, type: client-words, proof: P03, client_key: nick-kuijpers, status: ready }
- { id: V-PR-03, type: client-words, proof: P01, client_key: shervin-khanzadi, status: ready }
- { id: V-PR-04, type: client-words, proof: P08, client_key: ben-kemboi, status: ready }
- { id: V-PR-05, type: client-words, proof: P06, client_key: waqas-zahoor-pal, status: ready }
- { id: V-PR-06, type: project-spotlight, facts: [F35], status: ready }
- { id: V-PR-07, type: project-spotlight, facts: [F37], status: ready }
- { id: V-PR-08, type: project-spotlight, facts: [F32], status: ready }
```

### Grow with us: Grow at Verdant (`grow-with-us`)
Conceptual unless the inbox supplies something real. No invented culture claims, no AI-generated people.
```yaml
- { id: V-GW-01, topic: "The stack you'd learn here", facts: [F05], status: ready }
- { id: V-GW-02, topic: "What 'full-cycle' means for a junior engineer", facts: [F14], status: ready }
- { id: V-GW-03, topic: "Cloud skills worth learning early", facts: [F06], status: ready }
- { id: V-GW-04, topic: "For designers: the six steps before code", facts: [F04], status: ready }
- { id: V-GW-05, topic: "Working on products for clients abroad", facts: [F01], note: "name client countries only as PUBLIC-PROOF context shows them (Australia: P01; the Netherlands: P03)", status: ready }
- { id: V-GW-06, topic: "Read the brief before you write the code", facts: [], status: ready }
```

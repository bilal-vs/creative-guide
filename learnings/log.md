# Learnings & decision log

## Current status
- **Phase:** 1, Foundation → visual directions
- **Branch:** `claude/social-media-style-guide-665rja`
- **Done:**
  - audit and write-up
  - `FACTS-v2`, `PUBLIC-PROOF-v2`
  - `PALETTE-v2`: light and dark themes; slate blue and sage teal fixed
  - strategy v1
- **NOW: light-theme direction test, complete posts.** The user is running the 3 light prompts as **v3** in `posts/2026-10-04-direction-test-built-to-scale.md`: full post with headline, subline, URL, and the logo from REF-PACK-v1; 3:4. The dark prompts are deferred until a light direction wins.
  - Waiting on: the user runs each in Google Flow (Nano Banana 2, 4:5, 4 outputs) exactly as written and pastes **all** outputs, labelled by prompt.
- **Next:** review each output in the rubric table and classify failures. The best direction becomes the first `TPL-*` template, then gets tested across pillars and topics.
- **Still open** (in `brand/strategy.md` §14; not blocking the visual tests):
  - numbers allowed in posts
  - Shervin Khanzadi's attribution; Elia Essen's company
  - founding year
  - buyer markets
  - news-inbox owner
  - Instagram Reels
  - repo privacy
- **Flow:** no 4:5 option (1:1, 16:9, 9:16, 4:3, 3:4), so we generate at 3:4 and crop to 4:5. Still unknown: how many outputs per run.

---

## Log

### 2026-10-04 · Extended palette (v3)
- **User:** don't be bound to the two colours; choose others that match and improve the overall look.
- **Mine:**
  - **Midnight #142B40:** depth, in the brand-blue hue.
  - **Deep Teal #2C6A6C:** finally a teal that's legible as text on light.
  - **Glacier #BFE3DE:** luminous light and glows.
  - **One warm Coral spark #E8876A:** the complement of blue and teal. Limited to ≤5% so posts stay minimal and premium.
  - **Ice #EAF4F3:** a neutral.
  - **Four named gradients:** brand, daylight, depth, glow.
  - **Rule:** at most 2 extended colours per post.
- Recorded as `PALETTE-v3` in `STYLE_GUIDE.md` §5.1; sheet in `brand/palette-v3.png`.
- The v3 prompts (unsent) will take these colours when the user says go.

### 2026-10-04 · Complete posts, not backgrounds
- **User decision:** the model generates the whole post (headline, subline, URL, logo), not a background for overlay.
- **Mine:**
  - the logo comes from a fixed reference image (REF-PACK-v1, the gradient lockup PNG) so it isn't redrawn
  - text is kept to three short exact lines to limit spelling risk
  - new rubric checks for exact text and logo fidelity
  - overlay stays as the documented fallback
- **User:** "use full level of creativity: colours, gradients, visuals." v3 was rewritten before sending: luminous blue→teal gradient backgrounds, gradient glass, light trails and caustics, a low-angle hero view, with the headline kept on the bright top-left.
- **User rules:** posts must be minimal, professional, premium, visually attractive, built around a visual, and readable. v3 was revised again before sending: one hero object in the gradient on a luminous gradient ground, busy effects removed (bokeh, trails, glints), and high-contrast text on a clean area. The rules are now `STYLE_GUIDE.md` §5.0, plus "every post and carousel looks made by a professional graphic design team".
- The prompts went to v3. v2 was never run.

### 2026-10-04 · Flow aspect ratios
- Flow rejected 4:5. Nano Banana 2 in Flow offers only 1:1, 16:9, 9:16, 4:3 and 3:4.
- **Decision:** generate at 3:4, say "3:4 aspect ratio" in the prompt, and crop to 4:5 deterministically (45px off the top and bottom at 1080 wide). The pipeline does the same, for parity.
- The prompts went to v2 (aspect ratio only). v1 was never run. Rule followed: never edit a sent prompt.

### 2026-10-04 · Palette themes + first direction test
**Decisions (user)**
- **Keep slate blue #416D95 and sage teal #74AFAD exactly.** All other colours may change. Posts get a light theme and a dark theme.
- No formal brand-guide page is needed for now. Go straight to prompts.

**Decisions (mine)**
- **Light theme:** Mist #F4F7F8, ink #13212C, slate-blue highlights.
- **Dark theme:** Deep Slate #0E1A23 (the brand blue's hue, not royal navy), near-white ink, sage-teal highlights.
- All text pairs pass WCAG. Proposed theme by pillar: insight and brand world dark, the rest light.
- **First test:** 3 directions (architectural model, living network, layered glass) × 2 themes, on one shared topic, with an identical prompt spine. This isolates the direction as the variable.

**Guide changes**
- §5 → `PALETTE-v2`. `TYPE-v1` colour names aligned.
- A half-built design-system page is kept as source files in `brand/brand-guide/` (tokens, README, post mockups). It isn't published; the user said it isn't needed now.

### 2026-10-04 · Audit write-up (cloud)
**What happened**
- A local Claude Code session with Chrome captured the website, the LinkedIn About page and Clutch. It also captured 19 LinkedIn posts and the Instagram profile before the user narrowed the scope to business info. Upwork and Fiverr were skipped.
- The cloud session reviewed the screenshots and ran three independent checks: pixel sampling of the logos and past posts, web research on the named clients, and a separate business read. Then it wrote everything up.

**Findings that changed things**
- **The brand colour is a slate blue → sage teal gradient (#416D95 → #74AFAD), not green.** The CSS names it "green-gradient". The logo files match it exactly.
- **Past social posts use a different, more saturated royal navy** (about #194493) **with yellow.** Neither is a brand colour, and the font isn't Inter.
- The website is the cleanest expression of the brand: off-white and ink, Inter, gradient-highlighted words, a line-and-node mesh, and an oversized VS mark.
- **The tagline is confirmed** on LinkedIn, Instagram and Clutch, but it isn't on the website. **Founded 2019** appears only on Clutch.
- **"Alogirft" is a website typo for AlgoRift.** Shervin Khanzadi wrote both the website testimonial and the Clutch review, so P01 and P04 are one client.
- **Clients:** AlgoRift / Sweet Round (Australia), Wemasy (Netherlands), Nedjmati (Algeria). No public link was found between "Elia Essen" and an AI SaaS company, so P02 is held.
- **The numbers disagree across channels:** homepage counters, LinkedIn stats and Clutch's team range.
- **Engagement (19 posts):** real-people posts got about 36 reactions on average; generic insight posts got about 7.

**Decisions (mine, as proposals in `brand/strategy.md` v1)**
- Move social onto the website system and retire the navy and yellow templates, AI robots and stock "staff".
- Insight posts must come from their own projects. Proof alternates Client words and Project spotlight.
- Inbox items with real people take the day. Hiring roles come only from the inbox, because the careers job list is broken.
- No self-reported numbers. Caption reset: 3–5 hashtags, no Unicode bold, a hook first.
- The employee repost kit moves up to launch.

**Guide changes**
- §2 → `FACTS-v2`:
  - tagline confirmed; UI/UX process corrected from seven steps to six
  - new facts: CTAs, milestone payments, engagement models, ten case studies
  - F50–F52 numbers pending
- §2 → `PUBLIC-PROOF-v2`: verbatim text, `client_key`, six quotable entries.
- §5: `PALETTE-v1`, `TYPE-v1`, logo file table, candidate motifs.
- §9: the proof cap counts per `client_key`, and the no-numbers rule.

**Lessons**
- **Sample colours from opaque pixels only.** Semi-transparent PNG pixels read as false colours (#307080). Composite onto white, or mask the edges, before sampling.
- **Scope words matter.** Case studies say "contributed to" or "built the … modules". Past posts inflated that ("redefined…"). Facts must carry the scope word.
- **A testimonial on the site isn't the same as verifiable proof.** Check that the name maps to a real client before the pipeline quotes it.
- **Keep the local capture narrow.** The user only wanted business facts; the local session over-built tooling and drifted into social. Next time, give a short capture spec with a hard scope.

### 2026-10-04 · Audit attempt (cloud): blocked → split workflow
**What happened**
- A new cloud session tried to run the audit. It had **no Claude in Chrome tools** (none attached, and no connector or local session to reach).
- Egress was blocked for every target: the proxy returned `403` on `verdant-soft.com`, `clutch.co`, `linkedin.com`, `instagram.com`, `upwork.com` and `fiverr.com`, and WebFetch returned `EGRESS_BLOCKED`.
- WebSearch still works but only returns paraphrases. It found no LinkedIn company URL, no Upwork or Fiverr profile, and no Instagram account. These must come from the site's footer or from LinkedIn itself.

**Decisions (user)**
- **Research locally, then write up in the cloud.** The local Claude Code session with Chrome only captures raw facts into `brand/audit-raw.md`, plus logos and reference screenshots. The cloud session then does the analysis and all edits to the guide and strategy.

**Guide changes**
- None. `brand/research.md` gained the split note and a capture spec under "Audit TODO".

**Lessons**
- **Cloud sessions never get Claude in Chrome.** It only attaches to Claude Code running on the user's machine. Plan any browser work as a local step.
- **Fallback for public pages:** allow the domains in the environment's network settings, then use the headless Chromium that's pre-installed in the cloud container (Playwright, `/opt/pw-browsers`). It can read computed styles, fonts and the DOM. It won't get past LinkedIn, Instagram, Upwork or Fiverr login walls; those still need Chrome or screenshots.
- **Reference screenshots of past brand material may live in the repo** (`brand/audit/screens/`). The "no images in the repo" rule covers generated outputs.

### 2026-10-04 · Company research + handler strategy
**What happened**
- Researched Verdant Soft through web search. Direct fetches of their site, Clutch, Glassdoor, G2 and Rozee were blocked by the network policy.
- Findings, with sources and confidence tags, are in `brand/research.md`.
- No colours, logo, fonts or past posts could be retrieved.

**Decisions (user)**
- Both platforms serve **brand, clients and talent**.
- Publicly available clients and testimonials may be used, **but not too much**.
- Brand assets come from a browser pass over the live site.

**Decisions (mine, recorded as proposals in `brand/strategy.md`)**
- Positioning: *the engineering partner that owns the outcome*. Every public testimonial says on time, responsive, reliable, ownership.
- Creative platform: **"Growth, engineered."** The name means growth, and the idea covers clients (products that scale), brand (point of view) and talent (careers that grow).
- 5 pillars with a 7-day rotation. v1 = one cross-posted image per day with separate captions per platform.
- Input priority: news inbox > calendar > series > evergreen.
- New guardrails: no AI-generated "staff"; pre-approved templates for national and religious days; a fact bank as the only source of claims; proof capped at 1 per week, with no client repeated within 30 days.

**Guide changes**
- §2 drafted with `FACTS-v1` and `PUBLIC-PROOF-v1`.
- §3 widened to content strategy.
- §9 guardrails tagged `[decided]` or `[proposed]`.
- §11 Memory and adaptation added.
- Ledger columns widened.

**Lesson**
- Search snippets give paraphrases, not quotes. **Never quote a testimonial from a search result.** Capture the verbatim text from the source page.

### 2026-10-04 · Project setup
**Decisions**
1. **Tune templates, not images.** Success = pass rate of an unchanged template across topics.
2. **Classify every failure** as `[prompt]`, `[variance]`, or `[concept]`.
3. **Reviews use one fixed rubric and table format**, so they can later calibrate the automated judge.
4. **Flow ↔ API parity:** single-shot prompts, logged settings, aspect ratio stated in the prompt, and reference images only as a fixed versioned pack. Flow has no API, so the pipeline will call Gemini directly.
5. **Deterministic elements are overlaid, not generated** (logos, exact text, handles). This is the default and will be confirmed per brand.
6. **Variety by rule:** fixed vs variable elements, topic bank, no-repeat window, ledger as memory.
7. **Done = blind test:** a fresh agent with only `STYLE_GUIDE.md` produces a week of posts that pass unedited.
8. **The repo holds all state.** `CLAUDE.md` is the session entry point.

**User choices**
- Images are pasted in chat, not stored in the repo. Written reviews are the only record, so they must describe each output concretely.
- Nothing is published during the build phase. Reviews judge quality, brand fit, and scroll-stop, not engagement.
- `STYLE_GUIDE.md` (Markdown) is the single source of truth. A machine-readable YAML is exported only after the blind test passes.

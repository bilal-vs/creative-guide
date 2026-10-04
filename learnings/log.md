# Learnings & decision log

## Current status
- **Phase:** 1, Foundation
- **Done:** public-source research (`brand/research.md`) and the handler strategy proposal (`brand/strategy.md`)
- **Branch:** `claude/social-media-style-guide-665rja`
- **NEXT ACTION: the audit, in two steps** (user decision; details in `brand/research.md` → "Audit TODO" → "Split" and "Capture spec"):
  1. **Local capture (user's machine).** Run Claude Code with Chrome connected (`claude --chrome`), logged in to LinkedIn, on the branch above. Follow the capture spec: raw verbatim facts go into `brand/audit-raw.md`, logos into `brand/assets/`, reference screenshots into `brand/audit/screens/`. Commit and push. No analysis in this step.
  2. **Cloud write-up.** Read `brand/audit-raw.md` and the screenshots. Then write the audit results and the Keep / Fix / Drop / Gaps summary in `brand/research.md`; update `STYLE_GUIDE.md` §2 (`FACTS-v2`, `PUBLIC-PROOF-v2`) and §5 (palette, fonts, logo); revise `brand/strategy.md` to v1; update the log; push; summarise for the user.

  Cloud sessions can't do step 1: no Claude in Chrome, and the network policy blocks the sites (see the 2026-10-04 "Audit attempt (cloud)" entry).
- **Then:** the user reviews the strategy (questions in `brand/strategy.md` §14). Then Phase 1 visual directions: 2–3 directions inside "Growth, engineered", tested on one shared topic.
- **Open questions:**
  - Which aspect ratios does Flow offer for Nano Banana 2 images? (We want 4:5 for both platforms.)
  - How many outputs per generation? (We want 4, to measure pass rate.)
  - Should the repo be made private? It's public right now, so only public-safe info goes in.
  - Confirm: the tagline "Engineering tomorrow's tech today!", the founding year 2019, and the spelling of "Alogirft".

---

## Log

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

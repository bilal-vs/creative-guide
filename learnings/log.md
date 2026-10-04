# Learnings & decision log

## Current status
- **Phase:** 1, Foundation
- **Waiting on:** the user's description of the company and the types of posts they want
- **Next action:** record it in `brand/brief.md`, then propose content pillars and 2–3 distinct visual directions, tested on one shared topic
- **Open questions:**
  - Which aspect ratios does Flow offer for Nano Banana 2 images? (We want 4:5 for both platforms; if Flow lacks it, decide on a substitute and note the API difference.)
  - How many outputs per generation will the user run? (We want 4, so we can measure pass rate.)
  - Does the brand have a logo, hex palette, and fonts? (This decides the overlay spec.)

---

## Log

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

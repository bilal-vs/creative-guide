# Learnings & decision log

## Current status
- **Phase:** 1, Foundation
- **Branch:** `claude/social-media-style-guide-665rja`
- **ROADMAP (user, 2026-10-05), in this order:**
  1. **Writing practice** (now): headlines → captions (LinkedIn and Instagram) → carousel copy → alt text and hashtags. Codify the winners into `STYLE_GUIDE.md` §7. Files in `writing/`.
  2. **Visuals**: discuss and train. Templates and kit are in `brand/theme/` (7 templates × 4 moods). The prompts in `posts/2026-10-04-direction-test-built-to-scale.md` (v3, unsent) get rebuilt from the templates.
  3. **Revise the colour guide** from what the visuals teach (`brand/theme/colours.py` → `python3 brand/guidelines/build.py`).
- **NOW (2026-10-08):**
  - **Main rule (user):** 70% Verdant / 30% external. External is carousels only; Verdant is 3 singles + 2 carousels a week (`STYLE_GUIDE.md` §3 `CONTENT-MIX-v2`).
  - **Visual taste round L3 (light, Verdant single):** the user runs 4 prompts (Project Spotlight F30) and rates them on the Taste Lab, https://claude.ai/artifact/Rbi98WmtVZB12QcBn7edrT (tab L3). L1 is done (D won at 7/10). L2 was withdrawn.
  - **Design bar (user):** "a group of graphic designers on a high budget… visually attractive with some functionality, not useless."
  - **Persona writing loop:** running as a workflow. When it lands, integrate it into `writing/round-03-lane-packs.md` and recast the external packs as carousel covers.
  - **Next after L3:** dark round D1 from the L3 winner, then VISUAL-SYSTEM-v2 for Verdant singles, then carousels.
  - **Done criterion (writing):** 2 rounds in a row at ≥ 80% keep, with no truth or voice failures.
- **Content system (user, 2026-10-06):**
  - **Mix:** superseded on 2026-10-08 by the main rule above (`CONTENT-MIX-v2`, `brand/strategy.md` v3).
  - **Research:** every post is researched **the day before** (D−1).
  - **Routine "Weekly trend drop":** `trig_01Wrzh1wzUKNL3SFFVpNSNuf`, every Saturday at 09:59 PKT. It writes to `banks/trends.md`; daily runs start at launch.
- **Blocked:** the cloud network only reaches anthropic.com among the primary sources. The user said they'll allow the source domains (title bar → cloud environment → Edit → Network access → Custom). Until then, research items stay `pending-check`.
- **Done:**
  - audit
  - FACTS-v2 and PUBLIC-PROOF-v2
  - strategy v2
  - colour system v8 (PALETTE-v8 + THEMES-v1) and the 25-page colour book
  - LIGHT-THEME-v2 templates
  - post rules §5.0
  - CAROUSEL-v2 (example 01 approved)
  - headline style decided
  - caption rules, HASHTAGS-v1, BANNED-WORDS-v1
  - EXTERNAL-SOURCES-v1
  - banks and inbox
- **Still open:**
  - `brand/strategy.md` §14 (numbers, Shervin Khanzadi's attribution, Elia Essen, founding year, markets, Reels, calendar moments, repo privacy)
  - lane → mood mapping (visuals stage)
  - Syne for headlines?
  - Flow outputs per run

---

## Log

### 2026-10-08 · The main rule: 70% Verdant, external = carousels only; L2 withdrawn; round L3 (Verdant single)
**User:**
- "one main rule for overall posts 70% verdant soft 30% other the 30% other should be completely for carousel and out of the 70% 60% posts 40% carousel… the prompts you gave me are all completely useless"
- "the visuals should look like a group of graphic designers on a high budget designed a single post and it should be visually attractive with some functionality, not useless"

**Decided (user):** the mix flips back to Verdant-first. Every week now has 5 Verdant posts (3 singles + 2 carousels) and 2 external carousels, so it's 3 singles and 4 carousels overall. A single post is always Verdant. Written into `STYLE_GUIDE.md` §3 `CONTENT-MIX-v2`, §4 lane table, §9, §11; `brand/strategy.md` v3; `tools/sim_calendar.py` (8 weeks: 71.4% Verdant, 60% of Verdant singles, all external carousels: ALL OK).

**Decided · CD (days):**
- **Mon:** This Week in Tech (external carousel)
- **Tue:** How we work (wk A) or Build Notes (wk B), carousel
- **Wed:** Proof single: Project Spotlight (wk A) or Client words (wk B)
- **Thu:** external carousel, rotating AI, Explained → Under the Hood → Founder Notes → By the Numbers
- **Fri:** the carousel pillar Tuesday didn't run
- **Sat:** Grow at Verdant single
- **Sun:** new **Verdant Toolkit** single (one service or stack area; F02–F06, F14, F15)
- **Why:** carousels go on weekdays for LinkedIn buyers; singles spread to mid-week and the weekend for Instagram and talent.
- **Overrides:** inbox items and moments now take Verdant single slots, never external ones. The direct-CTA cap rises to 3 a week.

**Why L2 was useless (my reading):**
1. It trained single posts on a generic Founder Notes checklist. That's "other" content, which is now carousel-only, and it isn't about Verdant.
2. The four versions only swapped the font or the depth, not four real design ideas, and none had a visual that does a job.

L2 is withdrawn (never generated) and removed from the Taste Lab.

**Round L3** (`posts/2026-10-08-taste-light-l3-spotlight.md`, all 4 lint PASS, 8 strings / 27 words):
- **The post:** a real Verdant single, Project Spotlight F30, "Four modules a clinic can't get wrong", with the four modules and the stack.
- **Four agency-grade ideas** where the visual carries the information: A Module cards (Swiss, raised cards, Clash style), B Interface (a floating clinic app in perspective, Instrument Serif), C Patient file (a top-down photo with four coloured index tabs, Syne), D System map (isometric module blocks on a stack slab, Unbounded).
- **Blind prediction:** B > A > C > D (`learnings/taste.md`).
- **Taste Lab** republished (v4) with tabs L1 and L3. Checked at 390 and 1280 px: no script errors and no horizontal scroll.

**Open risk (told to the user):** five Verdant posts a week use up the confirmed Verdant facts in about 10–12 weeks. From launch the team must feed `inbox/` (projects, photos, reviews, process notes). The persona writing loop (round 3) was built on the old lane packs. Its writing lessons still apply, but its external singles become carousel covers.

### 2026-10-08 · Taste round L1 results → SCHEMATIC paused; no pricing content; round L2
- **L1 scores (user, Taste Lab):** D Swiss type 7, C Studio 3D 4, A Report 2 (the current VISUAL-SYSTEM-v1), B Luminous 1.
  - "Font too basic" appeared in 3 image notes and the round note.
  - Soft gradients and glass were tagged "Looks AI", "Old-fashioned".
  - D: "looks good but text needs improvement, too flat".
  - Nano Banana 2 rendered all 7 strings exactly in every image.
- **My blind prediction failed:** predicted B > C > A > D, actual D > C > A > B (extremes swapped). Lesson: in this user's eyes, "creativity with colour and gradients" does **not** mean soft gradient fields.
- **User:** "the data is not useful, don't include pricing type of thing in any… it's a single slide, this doesn't even serve purpose."
  - **Decided:** no pricing, payment-terms or engagement-terms content in any post; the on-image information must be useful on its own (`STYLE_GUIDE.md` §9).
  - **Dropped:** P3 (milestone payments).
  - **Excluded** in the topic bank: V-HWW-01, V-HWW-03, E-FN-04 and E-FN-06.
- **Paused:** VISUAL-SYSTEM-v1 (§5.7) and the 3 SCHEMATIC prompts already sent (P3, P7, P9), marked "don't generate".
- **Round L2** (`posts/2026-10-08-taste-light-l2-brief.md`; L2 tab on https://claude.ai/artifact/Rbi98WmtVZB12QcBn7edrT):
  - **Copy:** the useful checklist "What your dev brief is missing" (E-FN-02), the same 8 strings in every version.
  - **Versions:** A display font (Syne style), B editorial serif, C embossed paper (display font plus depth), D flat colour block.
  - **Blind prediction** recorded first: C > A > D > B.
- **Persona writing loop:** resumed after the session-limit failure (run wf_11be7077-103). Patched so a round with fewer than 3 personas returned is invalid; the failed run had reported "100% keep" from 0 personas.

### 2026-10-07 · Visual taste training starts (round L1, light)
- **User:** train single posts first and carousels later, light first and then dark. For each round: 4 prompts of the same post with different visuals; the user uploads the outputs to a page and rates each 1–10.
- **Built:**
  - `posts/2026-10-07-taste-light-p3.md`: P3 in 4 directions with identical text. A Report (the current VISUAL-SYSTEM-v1), B Luminous (aqua gradient field plus glass discs), C Studio 3D (porcelain and glass plinths), D Swiss type (huge type on off-white paper).
  - The Taste Lab page (https://claude.ai/artifact/Rbi98WmtVZB12QcBn7edrT): upload, rate 1–10, tap-tags, pick a favourite. It uses the assets and db capabilities.
  - `learnings/taste.md`: the method, plus my blind prediction recorded before any ratings (B > C > A > D).
- **Next:** read the ratings with ArtifactData and view the images (Artifact read, path = asset id). Score agreement, write the taste rules with evidence, then run round D1 (dark) the same way.

### 2026-10-06 · Content mix reset + writing system (plan mode, 11 rounds of questions)
- **User decisions:**
  - **Mix:** 30% Verdant / 70% external (per month, flexible; Verdant band 25–40%).
  - **Formats:** one third carousels (2-2-3 cycle).
  - **External pillar:** Tech, Explained, written for founders. Five lanes, each a named series: This Week in Tech (Mon roundup carousel), AI, Explained (Wed), Founder Notes (Fri), By the Numbers (Sat), Under the Hood (Sun).
  - **Verdant days:** Tue (How we work / Build Notes) and Thu (Proof / Grow with us), alternating weekly.
  - **Content:** half evergreen, half trending. Primary sources only, with the source on the image and in the caption. Companies named in text, neutral.
  - **Tone:** a practical stance. A Verdant take on every external post. Plain language with one term defined.
  - **No company numbers** until confirmed.
  - **Captions:** same visual, separate captions. LinkedIn 120–220 / Instagram 40–100 words. English only. Emoji: LinkedIn none, Instagram ≤ 2. Hashtags: LinkedIn 3 / Instagram 5. "We" plus "you".
  - **CTAs and endings:** direct CTA only on How we work and Proof. A question on about 1 in 3 posts.
  - **Headlines:** problem/curiosity about 60%; keep the highlight. Carousel example 01 approved as the model.
  - **Overrides:** inbox items and calendar moments replace the day's external post.
  - **Research:** Saturday trend drop from now, daily runs at launch, optional human inbox.
  - **Workflow:** practice uses one pack per lane on a keep/kill page; the done criterion is 2 rounds at ≥ 80% keep.
- **Mid-session additions:**
  - "decide what you think you can decide better": my calls are tagged `[decided · CD]` (no-repeat windows, link placement, take placement, hashtag sets, banned-word additions, run time).
  - "make sure to do research about the post the day before": the **D−1 research** rule. Every post's sources are re-opened, newer developments and sensitivity are checked, and the result is logged in the post file. No research, no publish.
- **Deliberate change, flagged:** v1 grounded insight in our own work, because generic posts did worst in the audit. Mitigation: the take line, the founder audience, the named series, and an 8-week review of the split after launch.
- **Lesson (research):**
  - **The search tool contradicted itself.** One search summary "confirmed" a Gemini 4 Argon launch on 30 Sep; a second found no official announcement. That's the case for primary-only sources. Logged as `T-2026-10-06-R1`, rejected.
  - **Most primary sites are unreachable here.** The cloud egress proxy blocks most primary sites (only anthropic.com worked), so the first drop has 2 checked items and 4 `pending-check`.
  - **Effect on practice:** pack 1 is practice-only. Being made by Anthropic, I flagged that the only checked items were Anthropic's, and capped the company at 2 a week.
- **Self-correction:** my first variety rule (no formula on consecutive days) capped problem/curiosity below the user's 60%. Revised to "never three days running, never the same opening word twice in a row".
- **Files:**
  - `brand/strategy.md` v2
  - `STYLE_GUIDE.md` §1, §2.3, §3, §4, §4.1 (v2), §7, §9, §11
  - `banks/`, `inbox/`, `posts/index.md` and `posts/_template.md`
  - `writing/round-02-lane-packs.md`, `writing/review/round-02.html`
  - `tools/` (check_packs, build_review, check_yaml, sim_calendar)

### 2026-10-06 · Carousel playbook
- **User:** shared *The Carousel Playbook* (@adarshxdesign: 25 hook formulas, cover checklist, slide jobs, 3-second test) and a 10-point checklist. Use it, or make it better.
- **Adapted for a B2B engineering brand with automated posting:**
  - structure Cover → Payoff → Steps → **Proof** → CTA → **Receipt** (6–8 slides)
  - main CTA on the second-last slide, with a soft repeat on the receipt (reconciles both sources)
  - hook formulas rewritten without invented numbers; proof hooks come only from FACTS and PUBLIC-PROOF
  - "comment PDF" CTAs dropped (the automation can't send DMs)
  - checklist grown to 14 points with a **brand and truth** group
  - a sixth question in the 3-second test: "true for us to say?"
- **Codified:** `STYLE_GUIDE.md` §4.1 `CAROUSEL-v1`.
- **Worked example:** "The costliest bugs are written before the code" (8 slides, F04 + P08 verbatim).

### 2026-10-05 · Colour system v8: two themes × four moods (detailed book)
- **User:**
  - improve the dark and light themes, mainly light, and make the guide detailed
  - think deeply first
- **Method:** three independent designer agents (moods by pillar; luminous light; editorial elevation), then my synthesis. Every pair is contrast-checked in code.
- **Key findings:**
  - Light posts got all their punch from a DARK cobalt block, so they felt half-dark and alike.
  - The old highlight end Ocean was only 3.3:1 on the darkest light ground.
  - White on the Ocean pill was 4.1:1, which fails for small text.
- **v8:**
  - **Light Royal** (How we work, Proof) and **Light Lagoon** (Grow with us): bright Royal Tide / Lagoon Tide masses with tinted shadows; mist and polar grounds; highlight Electric Royal → Deep Ocean, or Deep Ocean → Deep Lagoon.
  - **Dark Royal** (Insight) and **Dark Lagoon** (Brand world): aurora masses with a polar edge and no drop shadows; Sky → Cyan or Cyan → Mint highlights.
  - L0–L3 elevation; brand-gradient accent bar on every post (both core colours on every post).
  - Automatic image checks: light needs mean luminance ≥ 0.55 and ≤ 6% dark pixels; dark needs ≤ 0.15 plus a glow.
- **New colours:** Electric Royal #2457D6, Deep Ocean #007A9E, Deep Lagoon #00727F, Teal Night #061A22, Mist #F5F9FD. Royal Deep retired.
- **Source of truth:** `brand/theme/colours.py` (the book and kit read from it). Guide: PALETTE-v8 + THEMES-v1 (YAML generated from the source). Book: 25 pages.
- **Lesson:** compute contrast at the worst stop of every gradient, not the average; that's where the old highlight failed.

### 2026-10-05 · Colour guidelines book (16 pages)
- **User:** a multi-page guidelines book: overall, then dark theme, then light theme. Mid-build: **"colour guide only, not about visuals."** Writing and visuals get their own practice later.
- **Built** `brand/guidelines/verdant-soft-colour-guidelines.pdf` (pages in `brand/guidelines/pages/`; script `brand/guidelines/build.py`):
  - **Overall:** principles, core colours, full palette with HEX and RGB, 10 gradients, proportions, computed contrast pairs, logo colours.
  - **Dark and light themes:** colour roles, grounds and gradients, text colour and rules.
- **Fonts:** real Inter and Syne (OFL) were added in `brand/fonts/` from npm (@fontsource), converted from woff2. Inter's latin subset has no → or ≥, so the copy avoids them.
- **Palette → v7:** Royal Deep #2F62C8; named theme gradients; per-theme roles and proportions.
- **Kit:** the dark-theme templates now exist in `brand/theme/kit.py` (D-*), mirroring L-*, for the visuals stage.

### 2026-10-05 · Light theme v2 as a system
- **User:**
  - v1 was improved but not good enough: the heading doesn't pop, and it's too light overall
  - build the overall theme, not three posts
- **Diagnosis:**
  - the royal-blue highlight is mid-tone, so it's weak on white
  - mostly white with pale glows reads as washed out
  - there was no system, only one-offs
- **LIGHT-THEME-v2:**
  - tinted ice ground
  - **exactly one saturated colour block per post** (cobalt → royal with a cyan glow), which holds the hero
  - 100 px headline with **gradient highlight words** (#2F62C8 → #0088AA, ≥4:1)
  - gradient label pill, accent bar
  - component kit
  - **7 templates:** L-HERO, L-GLASS, L-QUOTE, L-LIST, L-COVER, L-SLIDE, L-PEOPLE
  - do/don't rules
- **Renderer:** `brand/theme/render_light.py`; sheets in `brand/theme/`.
- **Lesson:** "pop" on light grounds comes from one saturated mass plus a vivid gradient on the key words, not from more pale glows.
- **Next:** rebuild the test prompts from the templates (L-HERO, L-GLASS, L-QUOTE) when the user says go; the dark theme gets the same treatment.

### 2026-10-05 · Light theme improved
- **User:** loves palette v6; improve the light-theme posts.
- **Diagnosis:** the light sample was flat (plain white, flat bars, no depth).
- **Fix (LIGHT-THEME-v1):**
  - white with a pale aurora (polar, sky, faint cyan)
  - one glossy gradient hero in the teals → royal blue, with a soft cyan glow
  - optional frosted glass
  - text: polar pill label; deep navy-black headline with royal-blue highlight; a short gradient accent bar instead of an underline (the underline cut through descenders); steel-navy subline and URL
- **Mockups:** `brand/palette/v6-4-light-posts.png`.
- The unsent v3 light prompts were rewritten to this recipe and palette.

### 2026-10-05 · Palette v6 "deep ocean" (from user references)
- **User:**
  - shared 5 reference boards: Monestra greens, a navy/indigo/lime board, an aurora blur, a gradient board, Syne + Inter type
  - shared their own hexes: #34CCA4 #00ACB3 #0088AA #42658A #00A598 #09CACC
  - liked the 4th board's gradients; no yellow (from the 2nd)
- **Mine:**
  - sampled the reference colours
  - **deep grounds:** Abyss #050816, Navy #1E3058, Cobalt Night #151754
  - **the user's teals as the energy:** Mint Jade, Jade, Lagoon, Cyan, Ocean
  - **blues:** Royal #3C6EB7 (the reference's blue), Steel Navy #42658A
  - **lights:** Sky #A6CAEC, Ice #EBF5F7, Polar #E9FFFC
  - **gradients rebuilt from board 4:** abyss, cobalt, lagoon (starting from the core sage teal), daybreak, ocean, plus an aurora mesh
  - **rule:** one accent family per post
- The sheets are split into 3 pages in `brand/palette/` (user: "you can make multiple pages").
- **Open:** board 5 suggests Syne for headlines with Inter for body. Not adopted yet; ask the user.

### 2026-10-04 · Extended palette (v3 → v4)
- **User:** don't be bound to the two colours; add matching ones, minimal and similar.
- **v3 (mine):** Midnight, Deep Teal, Glacier, a Coral spark, the Ice neutral, four gradients.
- **User feedback:** no orange or coral; more minimal blues; the rest liked.
- **v4:**
  - **Blue family on the core's hue (209):** Midnight #142B40, Harbor #2A4D6E, Slate Blue (core), Ocean #5F88AE, Steel #8FA9BF, Sky #ADC6DD, Haze #DDE7F0, Frost #EEF3F8.
  - **Teal family:** Deep Teal #2C6A6C, Sage Teal (core), Glacier #BFE3DE, Ice #EAF4F3.
  - **Six gradients:** brand, daylight, frost, depth, ocean, glow.
  - **Rule:** at most 2 non-core family tones per post.
- **Lesson:** this brand wants a fully cool palette. Warm accents are out, even as a small spark.
- Recorded as `PALETTE-v4`, then replaced by v5 (below).
- **User on v4:** too much blue; overall dull and boring. Think about the best overall palette and range; the core stays.
- **v5:**
  - the muted core is the *material*
  - two luminous accents, Azure #3F8EE0 and Aqua #2EC4B4, are the *light*
  - soft tints: Sky, Mint and a little Lilac
  - a warm Linen #F7F3ED ground; a Midnight #0F2236 dark ground
  - gradients: brand, lagoon, aurora, dawn, deep-sea, signal
  - rule: one luminous accent per post
- **Lesson:** a palette of only muted, cool, mid-saturation colours reads as dull, however well it harmonises. It needs a luminous accent and a warm-white ground for life and contrast.
- Recorded as `PALETTE-v5` in `STYLE_GUIDE.md` §5.1; sheet in `brand/palette-v5.png`.

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

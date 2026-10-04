# creative-guide

This repo builds a style guide for daily Instagram + LinkedIn posts with AI-generated images (Nano Banana 2). The goal is a guide precise enough that an automated workflow can create and publish posts every day with **no human editing**.

## What's where
| Path | Purpose |
|---|---|
| `STYLE_GUIDE.md` | **The deliverable.** It holds only proven, agreed rules. |
| `brand/brief.md` | Company and post-type input, kept in the user's own words |
| `posts/` | One file per post: brief, every prompt version, reviews, captions |
| `posts/index.md` | Ledger of all posts (also the pipeline's memory for avoiding repeats) |
| `learnings/log.md` | Dated decisions and lessons, plus the **current status** block |
| `CLAUDE.md` | Operating manual for Claude sessions |

## The loop
1. **Brief → prompt → captions.** Claude writes them in a post file.
2. **Generate.** The user runs the prompt in Google Flow exactly as written, with the logged settings.
3. **Review.** The user shares all outputs in chat. Claude scores each one against the rubric and classifies failures (prompt, variance, or concept).
4. **Refine or approve.** A new prompt version, or an approved post.
5. **Codify.** Lessons go into the log. Once a lesson holds across posts, it's promoted into `STYLE_GUIDE.md`.

## Phases
| Phase | Exit when |
|---|---|
| 0. Setup | Repo structure pushed |
| 1. Foundation | Brand foundation written, pillars agreed, visual direction chosen |
| 2. Exploration | Every pillar has a template that produced an approved post |
| 3. Hardening | Templates hit the pass-rate target unchanged across new topics |
| 4. Blind test | A fresh agent using only `STYLE_GUIDE.md` produces a week of passing posts → export machine-readable config |

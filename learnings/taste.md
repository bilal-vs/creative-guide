# Taste profile (the user's visual preferences)

**What it's for:** the evidence for what the user likes and dislikes visually. A rule moves into `STYLE_GUIDE.md` §5 only after it has held on 2 or more posts; each rule cites its round and images.

**Method** (agreed 2026-10-07):
- **Probes:** same post, same text, 4 visual directions per round. Light first, then dark; single posts first, carousels later.
- **Ratings:** the user rates every output 1–10 with tap-tags on the Taste Lab page (https://claude.ai/artifact/Rbi98WmtVZB12QcBn7edrT). Ratings are stored in the page's `images` collection and favourites in `rounds/<id>`.
- **Claude predicts blind:** before reading the user's ratings, Claude records a prediction (direction ranking, then per-image picks once the images are visible). The agreement rate is how we know Claude has learned the taste; the target is about 9 in 10.
- **Disagreements are the lesson:** each gets a written reason here.

## Round L1 (light · P3): Claude's blind prediction, recorded before any images or ratings
**Predicted ranking:**
1. **B Luminous.** The user asked for "full level of creativity colors graidents visuals", called the earlier palette "dull boring", and picked an aqua/teal gradient reference (#34CCA4, #00ACB3, #0088AA, #09CACC).
2. **C Studio 3D.** It reads as "premium" and "attractive" from the post rules, and it's visual-led.
3. **A Report.** Clean and readable, but it may read as too calm.
4. **D Swiss type.** Probably "too plain / not enough visual" for this user, though it's the most minimal.

**Risks to the prediction:**
- B may look generic-AI with too much gradient.
- C's 3D may garble the label cards.
- The user's "minimal" rule could favour A or D.

## Results
_Waiting._

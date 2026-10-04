---
date: 2026-10-04
pillar: brand-world (direction test)
topic: Built to scale
template: DIR-A/B/C × light/dark, v1 (Phase 1 direction test; becomes TPL-* once a direction wins)
status: iterating
---

# Direction test: "Built to scale"

## Brief
- **Purpose:** Phase 1. Test 3 visual directions inside "Growth, engineered", each in the light and dark theme (`STYLE_GUIDE.md` §5.1 `PALETTE-v2`), on one shared topic. We want to see which direction the model renders on-brand most reliably.
- **Pillar:** Brand world (the topic suits both themes, so the directions compare fairly).
- **Topic:** software built to grow with the business.
- **Key message (one sentence):** Verdant Soft builds software that holds up at the next stage of growth.
- **What the viewer should take away:** this team thinks about scale from the first wireframe.
- **Overlay headline (added after generation, not in the prompt):** "Built for the next stage of growth", with "next stage" in `highlight`.
- **Why it stops the scroll:** a calm, premium, unusual object in the brand colours, instead of the stock tech imagery everyone else posts.

**Directions** (the fixed part of each template; only the theme changes between light and dark):
- **A · Architectural model:** a precise scale model of modular blocks rising in steps.
- **B · Living network:** a fine 3D network of threads and nodes, branching upward.
- **C · Layered glass:** blank frosted-glass panes fanning upward, with coloured light passing through.

**Fixed across all six (the shared spine):**
- commercial context sentence
- brand colours named with their hex codes
- subject placed lower-right
- the upper half and left side reserved as empty space for the headline and logo
- wordless surfaces
- ends with the aspect ratio

**Run order (user, 2026-10-04): light theme first.** Only v1-A-light, v1-B-light and v1-C-light are being run now. The dark prompts wait until a light direction is chosen.

**Settings (all six):** Google Flow · Nano Banana 2 · aspect ratio `4:5` (if Flow doesn't offer 4:5, use the closest portrait ratio and say which) · outputs `4` · resolution `default` · no reference images.

## Prompt v1-A-light
```text
An image for an Instagram and LinkedIn post by Verdant Soft, a B2B software engineering company. A precise architectural scale model made of modular blocks that rise in steps from left to right, as if the structure is growing while it is being built. The blocks are matte off-white and frosted glass, with a few blocks in muted slate blue (#416D95) and a few in soft sage teal (#74AFAD). The model stands in the lower right of the frame on a seamless pale grey-white studio surface (#F4F7F8) that curves smoothly up into the background. Soft, diffused daylight comes from the upper left and casts gentle, clean shadows; every edge is crisp. Shot with a 90mm lens from slightly above eye level, with a shallow depth of field. The upper half and the left side of the frame are open, smooth, evenly lit background with nothing in it, leaving clear room for a headline. All surfaces are clean and wordless. Calm, modern, premium, quietly confident. Portrait image, 4:5 aspect ratio.
```

## Prompt v1-A-dark
```text
An image for an Instagram and LinkedIn post by Verdant Soft, a B2B software engineering company. A precise architectural scale model made of modular blocks that rise in steps from left to right, as if the structure is growing while it is being built. The blocks are dark graphite and smoked glass, and several of them glow softly from within in soft sage teal (#74AFAD) and muted slate blue (#416D95). The model stands in the lower right of the frame on a seamless deep slate surface (#0E1A23) in a dark studio. Low-key lighting: the main light comes from inside the glowing blocks, with a faint cool rim light on the edges and soft reflections on the floor. Shot with a 90mm lens from slightly above eye level, with a shallow depth of field. The upper half and the left side of the frame are calm, even deep slate darkness with nothing in it, leaving clear room for a headline. All surfaces are clean and wordless. Focused, technical, premium, quietly confident. Portrait image, 4:5 aspect ratio.
```

## Prompt v1-B-light
```text
An image for an Instagram and LinkedIn post by Verdant Soft, a B2B software engineering company. A delicate three-dimensional network of fine, straight threads and small spherical nodes that branches upward and outward from the lower right corner, like a system that is growing as it scales. The nodes are small matte spheres in muted slate blue (#416D95), soft sage teal (#74AFAD) and white, joined by thin, precise lines. The network floats in front of a bright, seamless off-white background (#F4F7F8) under soft, even studio light. Shot with a 100mm macro lens with a shallow depth of field, so the nearest nodes are crisp and the ones behind fall into soft focus. The upper half and the left side of the frame are open, clean background with nothing in it, leaving clear room for a headline. All surfaces are clean and wordless. Airy, precise, optimistic. Portrait image, 4:5 aspect ratio.
```

## Prompt v1-B-dark
```text
An image for an Instagram and LinkedIn post by Verdant Soft, a B2B software engineering company. A delicate three-dimensional network of fine, straight threads and small spherical nodes that branches upward and outward from the lower right corner, like a system that is growing as it scales. The nodes glow softly from within in soft sage teal (#74AFAD) and muted slate blue (#416D95), and the thin threads between them catch a faint light. The network floats in calm deep slate darkness (#0E1A23), with a few distant nodes melting into soft bokeh. Shot with a 100mm macro lens with a shallow depth of field, so the nearest nodes are crisp and the ones behind fall into soft focus. The upper half and the left side of the frame are even deep slate darkness with nothing in it, leaving clear room for a headline. All surfaces are clean and wordless. Focused, precise, quietly futuristic. Portrait image, 4:5 aspect ratio.
```

## Prompt v1-C-light
```text
An image for an Instagram and LinkedIn post by Verdant Soft, a B2B software engineering company. An editorial still life of thin rectangular panes of frosted glass with softly rounded corners, standing in a gentle staircase that fans upward from the lower right of the frame, like the layers of a well-built digital product. Some panes are clear, some are tinted muted slate blue (#416D95) and some soft sage teal (#74AFAD); every pane is completely blank. Soft directional daylight passes through the glass and casts long, coloured, translucent shadows across a seamless off-white surface (#F4F7F8). Shot from a three-quarter high angle with a 70mm lens, with crisp focus on the front edges of the glass. The upper half and the left side of the frame are open, smooth, evenly lit background with nothing in it, leaving clear room for a headline. All surfaces are clean and wordless. Serene, refined, modern. Portrait image, 4:5 aspect ratio.
```

## Prompt v1-C-dark
```text
An image for an Instagram and LinkedIn post by Verdant Soft, a B2B software engineering company. An editorial still life of thin rectangular panes of smoked glass with softly rounded corners, standing in a gentle staircase that fans upward from the lower right of the frame, like the layers of a well-built digital product. Every pane is completely blank, and their edges catch a soft glow of soft sage teal (#74AFAD) and muted slate blue (#416D95) light rising from below. The panes stand on a seamless deep slate surface (#0E1A23) in a dark room, with faint coloured reflections beneath them. Shot from a three-quarter high angle with a 70mm lens, with crisp focus on the front edges of the glass. The upper half and the left side of the frame are calm, even deep slate darkness with nothing in it, leaving clear room for a headline. All surfaces are clean and wordless. Focused, refined, premium. Portrait image, 4:5 aspect ratio.
```

## Reviews
Paste all outputs per prompt. Each output is scored on:
- **Brief fit**
- **Brand fit:** colours read as slate blue and sage teal, not green; no yellow or royal navy.
- **No defects:** no text or letters, no artifacts.
- **Negative space:** the upper half and left side are clear for the headline and logo.
- **Crop-safe:** works at 4:5 and 1:1.
- **Scroll-stop:** scored 1–5.

An output passes only if every binary check passes and scroll-stop is ≥ 3.

**Decision rule:** the direction with the best pass rate across both themes moves forward as the first `TPL-*` template. A direction that fails in one theme only can be kept for the other theme.

### Review v1-A-light
_Waiting for outputs._

### Review v1-A-dark
_Deferred: light theme first._

### Review v1-B-light
_Waiting for outputs._

### Review v1-B-dark
_Deferred: light theme first._

### Review v1-C-light
_Waiting for outputs._

### Review v1-C-dark
_Deferred: light theme first._

## Captions (for the eventual post; facts F02, F04, F06, F11, F14)
**Instagram**
```text
Software should work for you, not the other way around.

We plan for growth from the first wireframe: architecture that can take more users, cloud that holds up under load, and code your team can keep building on.

Strategy, design, development and deployment, under one roof.

#VerdantSoft #SoftwareEngineering #CloudDevOps #ProductDevelopment
```

**LinkedIn**
```text
Most rewrites start the same way: the product worked, then the business grew.

Scaling problems are usually decisions made early, not traffic that arrived late. So we make those decisions at the start:

• Architecture that separates what changes often from what shouldn't
• Cloud and CI/CD set up so a release is routine, not an event
• Interfaces designed from real user research, so the next feature has a place to go

That is what full-cycle means to us: strategy, design, development and deployment, built to hold up at the next stage.

Planning a product that has to survive its own success? Book a call at verdant-soft.com.

#VerdantSoft #SoftwareArchitecture #CloudDevOps #ProductDevelopment
```

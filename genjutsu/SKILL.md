---
name: genjutsu
description: Genjutsu suite (AThevon/genjutsu) - anti-AI-slop creative coding. cast = motion/micro-interaction pipeline, paint = art direction + design system pipeline, plus 17 technique sub-skills (GSAP, Framer Motion, Three.js, CSS native, Canvas generative, SwiftUI, Compose, audits). Use when the user asks to animate a UI, add wow-factor, build a design system, or invoke genjutsu/cast/paint.
---

# Genjutsu — Suite Gateway

The `AThevon/genjutsu` repo, installed at `~/.zcode/skills/`. All 19 member skills are registry-hidden by design; this gateway is their single list entry and toggle.

## Loading protocol

1. For a full pipeline, `Read` **cast** (motion/micro-interactions) or **paint** (art direction/design system) first and follow it - they know how to pull in technique sub-skills.
2. For a targeted need, go straight to the technique table and `Read` the matching SKILL.md (paths are absolute); each sits next to its own `references/` when present.
3. cast/paint resolve the technique directory themselves (probe patched for `~/.zcode/skills/_jutsu`, which symlinks the siblings below), so their internal loading works unchanged.
4. Voice note from the repo: ninja flair during work, plain factual summaries in reports.

## Entry skills

| Skill | Path | Use when |
|---|---|---|
| cast | `/Users/boohee/.zcode/skills-repos/genjutsu/skills/cast/SKILL.md` | Animate an existing UI: motion, micro-interactions, wow-factor |
| paint | `/Users/boohee/.zcode/skills-repos/genjutsu/skills/paint/SKILL.md` | Full visual universe: art direction, design system, implementation, audit |

## Technique sub-skills

| Sub-skill | Path | Use when |
|---|---|---|
| motion-principles | `/Users/boohee/.zcode/skills-repos/genjutsu/skills/_jutsu/motion-principles/SKILL.md` | Foundation: timing, easing, enter/exit, accessibility, performance |
| desktop-principles | `/Users/boohee/.zcode/skills-repos/genjutsu/skills/_jutsu/desktop-principles/SKILL.md` | Hover states, pointer precision, keyboard, focus (macOS/Windows/Linux) |
| mobile-principles | `/Users/boohee/.zcode/skills-repos/genjutsu/skills/_jutsu/mobile-principles/SKILL.md` | Touch targets, thumb zones, safe areas, gestures, mobile budgets |
| css-native | `/Users/boohee/.zcode/skills-repos/genjutsu/skills/_jutsu/css-native/SKILL.md` | Zero-dependency: scroll-driven, View Transitions, @starting-style |
| gsap | `/Users/boohee/.zcode/skills-repos/genjutsu/skills/_jutsu/gsap/SKILL.md` | GSAP engine via genjutsu's lens (core/timeline/ScrollTrigger/plugins) |
| framer-motion | `/Users/boohee/.zcode/skills-repos/genjutsu/skills/_jutsu/framer-motion/SKILL.md` | AnimatePresence, layout animations, gestures, motion values |
| threejs-r3f | `/Users/boohee/.zcode/skills-repos/genjutsu/skills/_jutsu/threejs-r3f/SKILL.md` | 3D scenes, shaders, postprocessing (Three.js / React Three Fiber) |
| canvas-generative | `/Users/boohee/.zcode/skills-repos/genjutsu/skills/_jutsu/canvas-generative/SKILL.md` | Particles, flow fields, noise, fractals (Canvas 2D) |
| compose-graphics | `/Users/boohee/.zcode/skills-repos/genjutsu/skills/_jutsu/compose-graphics/SKILL.md` | Material 3 motion physics, AGSL shaders, DrawScope (Android) |
| compose-motion | `/Users/boohee/.zcode/skills-repos/genjutsu/skills/_jutsu/compose-motion/SKILL.md` | Jetpack Compose animation foundations |
| compose-multiplatform | `/Users/boohee/.zcode/skills-repos/genjutsu/skills/_jutsu/compose-multiplatform/SKILL.md` | KMP expect/actual, cross-target density/fonts |
| swiftui-motion | `/Users/boohee/.zcode/skills-repos/genjutsu/skills/_jutsu/swiftui-motion/SKILL.md` | withAnimation, matchedGeometryEffect, springs (SwiftUI) |
| swiftui-graphics | `/Users/boohee/.zcode/skills-repos/genjutsu/skills/_jutsu/swiftui-graphics/SKILL.md` | Metal shaders, visualEffect, Liquid Glass, Canvas (SwiftUI) |
| design-audit | `/Users/boohee/.zcode/skills-repos/genjutsu/skills/_jutsu/design-audit/SKILL.md` | Final checklist: motion gaps, a11y, color, responsive, performance |
| ui-ux-pro-max | `/Users/boohee/.zcode/skills-repos/genjutsu/skills/_jutsu/ui-ux-pro-max/SKILL.md` | Searchable dataset: 84 styles, 192 palettes, 74 font pairings, 99 UX rules |

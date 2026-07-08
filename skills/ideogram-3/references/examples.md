# Examples — prompts in practice

Worked Ideogram prompts showing the quotes rule, weak→strong, a brand-consistent set, and an edit —
plus honest scope. Brand context: a SaaS social scheduler (clean, design-led, mono + terminal-green
accent). Your output pulls the real palette/style from `brand-profile.md` (or a Style Reference).

---

## Weak → strong (the quotes rule)

**Weak:** "a poster about scheduling posts, with text"
**Strong:** "A clean design-style poster. The headline "Post less. Reach more." in a bold geometric
sans-serif, near-black, centred in the upper third. Beneath it, the line "Batch a week in 20 minutes."
in a lighter weight, smaller. Off-white background, a single terminal-green underline accent. Generous
negative space. Aspect ratio 4:5."
*(exact text in straight quotes, text-first, specific type + layout — render the final on Quality)*

## Logo-with-tagline (concept)

"A minimalist wordmark logo. The word "WOOP" in a bold geometric sans-serif, near-black, with a single
small terminal-green dot as an accent after the last letter. Beneath, the tagline "schedule, simply."
in a thin lowercase sans-serif. Centered, flat vector look, white background. 1:1."
*(concept/mockup — for a production logo, redraw as a true vector)*

## Brand-consistent carousel set (Style References)

Lock a **Style Reference** image (or the brand model) + palette, hold 4:5, then:
- Slide 1: "[same brand style], the text "Stop posting into the void." centred, bold sans-serif, one
  small motif. 4:5."
- Slide 2: "[same brand style], the text "Plan the week in one sitting.", same type and palette. 4:5."
*(reuse the same reference on every slide; review the set for drift; → `carousel-writer` owns structure)*

## Magic Fill edit (fix, don't regenerate)

On a finished graphic with a typo: mask just the text line, keep the surrounding context, prompt: "same
graphic; the line now reads "Reach more, post less." in the same bold sans-serif and colour." → fixes
the word without rebuilding the image.

---

## Honest scope (say this)

- **Verify spelling** — read every rendered word before publishing; use **Quality** for text-critical
  finals.
- **Disclosure is on you** — Ideogram does **not** force a SynthID-style watermark, so there's no
  embedded AI marker; **disclose AI imagery** per platform/region (Meta "Made with AI", EU AI Act).
  Don't pass it off as a non-AI photo.
- **No real people / no IP** — no real identifiable individuals, copyrighted characters, or trademarked
  logos (e.g. cloning a brand's mark); use original marks/figures.
- **No photoreal faces** — for realistic portraits, use another model.
- **Finish complex layouts in Canva/Figma**; Ideogram makes the typographic base.
- **Prompt craft only** — API/MCP/model IDs + the *generate → upload to WoopSocial Media → attach* flow
  live in `tools/integrations/ideogram.md`; WoopSocial doesn't generate images.

---

## What the examples share

- **Exact text in straight quotes, text-first**, with specific type + layout.
- **Style References / locked palette** for consistent sets; **Magic Fill** to fix, not rebuild.
- **Brand-grounded**, right aspect ratio, **Quality** for finals.
- **Verified, disclosed, IP-safe**, and finished in a design tool when the layout demands it.

---
name: ideogram-3
description: >-
  Use to write great prompts for Ideogram (the typography-first image model: Ideogram 4.0 / 3.0) to
  generate or edit design-led, text-heavy images for social media — the typography-image-prompt
  mini-skill, sibling to nano-banana. Run when the user wants an Ideogram prompt, a typographic
  graphic, a logo or wordmark, a poster, packaging or a text-heavy design, a brand-consistent set, or
  to edit with Canvas/Magic Fill. Reads brand-profile for brand style. Built on the verified 2026
  reality: Ideogram is the typography/design specialist (~90-95% text accuracy with layout control)
  with Style References (match a look from up to 3 images), Magic Prompt (auto-expands prompts), Canvas
  + Magic Fill (inpainting) + Extend (outpainting) + Layerize (editable text layers), custom brand
  models, and API + MCP (plus open weights). Teaches the core rule (put exact text in straight quotes,
  text-first), typography/layout prompting, Style-Reference consistency, and Magic-Prompt control.
  Honest: both Ideogram and Nano Banana are now excellent at in-image text — pick by tooling/ecosystem,
  not a fake win; Ideogram is weak at photoreal human faces (use Midjourney/Imagen); complex
  multi-element layouts are best finished in Canva/Figma; Ideogram does NOT force a SynthID-style
  watermark so AI disclosure is still required per platform/region and is on the user; never generate
  real identifiable people or copyrighted characters/brand logos; verify spelling. This is the
  prompt-craft layer — the API/MCP/connection (model IDs, the generate -> upload to WoopSocial Media ->
  attach flow) lives in tools/integrations/ideogram.md; the consuming pack is carousel-writer's
  image-prompt-pack.
metadata:
  version: 1.0.0
license: MIT
---

# Ideogram (typography image prompt craft)

Write prompts that get clean, typographic images out of **Ideogram** — the text-first image model
(**Ideogram 4.0**; open weights, API + MCP). This is the **prompt-craft** layer of a three-layer
setup, and the **typography sibling to `nano-banana`**:

- **Connection/API/MCP** (model IDs, auth, the *generate → upload to WoopSocial Media → attach* flow) →
  `tools/integrations/ideogram.md`.
- **Prompt craft** (this skill) → how to ask for the right typographic image well.
- **In-skill application** → `carousel-writer`'s image-prompt-pack.

> Fast-moving area — re-verify model names/specs quarterly.

## Reach for Ideogram when… (and which tool?)

Reach for it for **typography/design-led** work: posters, logos/wordmarks, packaging, text-heavy
graphics, brand-consistent sets — using **Style References**, **custom brand models**, **Canvas/Magic
Fill/Extend/Layerize**, and **MCP/open-weights**.

**Be honest about "which tool":** Ideogram and `nano-banana` are **both excellent at in-image text now**
— pick by **tooling/ecosystem**, not a fake "best text" claim. Ideogram's edge = dedicated **design
tooling**; Nano Banana's edge = **Gemini reasoning, multi-image consistency, conversational editing,
Search grounding.** **Skip Ideogram for photoreal faces** (→ Midjourney/Imagen), painterly art (→
Midjourney), or vector SVG (→ Recraft). (Details: `references/when-and-how-to-prompt.md`.)

## Step 0 — Read the brand + the job

Load `brand-profile.md` (colours, typographic feel, style). Identify the **job** (quote graphic / logo
/ poster / packaging / carousel set / header / edit) and the **aspect ratio**.

## Step 1 — Write the prompt (text-first, in quotes)

- **Put the exact text in straight quotes** — the #1 rule; quoted strings render reliably. One quoted
  string per text element, each with its own styling.
- **Lead with the text**, then scene/style. **Specify typography** (font character, weight, case,
  placement, layout) — not just "bold."
- Pick a **style mode** (realistic/design/anime/3D). **Magic Prompt** auto-expands (good for
  exploration) — **turn it off for exact control**. Set the **aspect ratio**. See
  `references/when-and-how-to-prompt.md`.

## Step 2 — Consistency & typography levers

- **Style References** (up to 3 images) or a **custom brand model** for a coherent set; lock palette +
  aspect ratio; review for drift.
- **Layerize** for editable text layers; keep critical text short; render finals on **Quality**. See
  `references/typography-and-style.md`.

## Step 3 — Edit & pick the recipe

Use **Canvas / Magic Fill / Extend / background removal** to fix rather than regenerate. Adapt a
**recipe** (quote graphic, logo, poster, carousel system, header, packaging) with the right ratio and
brand grounding. See `references/canvas-editing-and-recipes.md`.

## Step 4 — Verify, finish, disclose, ship

- **Verify the rendered spelling** (every word) before publishing.
- For **precise multi-element layouts**, finish the typographic base in **Canva/Figma**.
- **Disclose** AI imagery per platform/region — Ideogram does **not** force a watermark, so there's **no
  embedded AI marker**; disclosure is **on you**. Don't pass it off as a non-AI photo.
- **Ship:** generate per the integration guide → **upload to WoopSocial Media → attach** via
  `scheduling-and-queue`. WoopSocial doesn't generate images.

## Quality bar — self-check

- Did I **match the tool to the job** (and give an honest Ideogram-vs-Nano-Banana read; route photoreal
  faces elsewhere)?
- Is the **exact text in straight quotes, text-first**, with specific **typography + layout** and the
  right **aspect ratio**, **brand-grounded**?
- Did I use **Style References / brand model** for sets, and **Magic Prompt off** when exact control was
  needed?
- Did I cover **verify spelling**, **finish complex layouts in Canva**, **disclosure (no enforced
  watermark)**, and **refuse real people / IP / trademarked logos**?
- Did I point to **`tools/integrations/ideogram.md`** for the API/MCP + WoopSocial flow (no claim that
  WoopSocial generates images)?

## Edge cases & pushback

- **"Ideogram or Nano Banana?"** → honest tooling-based answer; both great at text.
- **Photoreal headshot** → route to Midjourney/Imagen; Ideogram is weak at real faces.
- **"It changed my wording"** → that's Magic Prompt; turn it off for exact control.
- **"No watermark, so post as a real photo"** → disclosure still required; don't disguise AI.
- **Trademarked logo / real person** → refuse; offer an original mark/figure.
- **Precise multi-block layout** → generate the base, finish in Canva/Figma.
- **"Generate it in WoopSocial"** → WoopSocial doesn't generate; this prompts Ideogram, then upload to
  Media and attach.

## Related

- `tools/integrations/ideogram.md` — API/model IDs, MCP/agent access, pricing, the upload-to-WoopSocial flow.
- `nano-banana` — the image sibling (honest which-tool); `carousel-writer` (image-prompt-pack) — consuming skill.
- `brand-profile` — the visual brand; `caption-writer`/`hook-writer` — the in-image copy.
- `scheduling-and-queue` — attach the image to a post and publish.

## References

- `references/when-and-how-to-prompt.md` — when to reach for Ideogram vs other tools, and the prompt craft.
- `references/typography-and-style.md` — the two levers: typography (the quotes rule, layout) and style consistency (Style References, brand models).
- `references/canvas-editing-and-recipes.md` — Canvas/Magic Fill/Extend/Layerize + social design recipes + the Ideogram→Canva finish.
- `references/examples.md` — weak→strong prompts, a logo, a consistent set, a Magic-Fill edit, and honest scope.

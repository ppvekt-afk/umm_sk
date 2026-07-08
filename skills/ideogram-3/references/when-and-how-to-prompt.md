# When & How to Prompt Ideogram

When to reach for Ideogram over Nano Banana or another model, and the prompt craft that gets clean
typographic results. (The API/MCP/connection layer is in `tools/integrations/ideogram.md` — this is
prompt craft.)

> Fast-moving model area — re-verify model names/specs quarterly. As of 2026: **Ideogram 4.0** is the
> current model (open weights; API + **MCP** for agents); **3.0** (Mar 2025) introduced Style
> References. Tiers/modes: **Turbo / Balanced / Quality** — iterate fast, finalize on **Quality** for
> text-critical work.

## Reach for Ideogram when the job is…

A typography- or design-led asset, where its dedicated tooling helps:

- **Text-heavy / typographic design** — posters, logos, wordmarks, packaging, book/album covers, event
  flyers, social headers, quote graphics. ~90–95% text accuracy with real **layout control**.
- **Brand-consistent series** — **Style References** (match a look from up to 3 images) and **custom
  brand models** (train on 15–100 images).
- **Post-generation design control** — **Canvas, Magic Fill (inpainting), Extend (outpainting),
  Layerize (editable text layers), background removal.**
- **Agent / open-weights workflows** — **MCP** access for agents; open weights you can run/tune.

## Honest "which tool?" (don't fake a win)

- **vs `nano-banana`:** **both are now excellent at in-image text.** Pick by **tooling/ecosystem**, not
  a clean "best text" claim. Ideogram's edge = dedicated **design tooling** (Style References, Layerize,
  Canvas/Magic Fill, custom brand models, MCP, open weights). Nano Banana's edge = **Gemini reasoning /
  world-knowledge, multi-image consistency (up to 14), conversational editing, Search-grounded
  infographics.** Use whichever fits the workflow you're in.
- **Skip Ideogram for photoreal human faces/portraits** → Midjourney / Imagen (Ideogram is great for
  illustrated/stylized figures, not photoreal faces).
- **Skip for painterly/editorial art** → Midjourney; **for vector SVG export** → Recraft.

## The prompt craft

- **Put the exact text in straight quotes** — the #1 rule. Ideogram renders quoted strings as literal
  tokens far more reliably. *…the words "Visit Iceland" in bold sans-serif…*.
- **Text-first.** Lead with the text requirement, then the scene/style.
- **Describe typography specifically** — font character, weight, case, placement, layout ("bold
  condensed sans-serif, centered, upper third"), not just "bold."
- **Style modes** — realistic / design / anime / 3D (the "design" default is clean and design-oriented).
- **Magic Prompt** — Ideogram's built-in LLM auto-expands a simple prompt (great for **exploration**).
  **Turn it OFF when you need exact control** over your specified text and layout.
- **Style References** instead of verbose style prose — upload images that carry the look/brand.
- **Iterate then finalize** — generate variations on Turbo/Balanced; re-run the keeper on **Quality**
  for crisp text. Set the **aspect ratio** for the platform.

## The honest finishing caveat

For **complex, pixel-precise multi-element layouts**, generate the typographic base in Ideogram and
**finish in Canva/Figma** — Canvas isn't as exact as design software, and the common pro workflow is
Ideogram → Canva composite. Always **verify the rendered spelling** before publishing.

## Brand-grounded

Read `brand-profile.md` — bake in **brand colours, fonts/typographic feel, style, do/don't** (or use a
Style Reference / custom brand model) so the output is on-brand.

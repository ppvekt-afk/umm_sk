# Typography & Style

Ideogram's two specialist levers for social: **typography** (text done right) and **style
consistency** (a coherent look across a set). Prompt both deliberately.

> Re-verify quarterly. Strong ≠ perfect — always review the output, especially spelling.

## 1. Typography (the core strength)

Ideogram was built for text. To get clean, legible type:

- **Exact text in straight quotes** — the single most important rule. Quoted strings render far more
  accurately. Put **each distinct text element in its own quotes** with its own styling.
- **Text-first** — lead with the text requirement before the scene.
- **Specify the type** — font character ("geometric sans-serif," "high-contrast serif," "condensed
  grotesque"), weight, case, alignment, and **placement/layout** ("headline centred upper third,
  small caption lower left").
- **Multi-line / hierarchy** — describe the hierarchy (headline vs subhead vs caption); Ideogram
  handles multi-line compositions, but keep it **clean** — fewer, well-specified lines render best.
- **Keep critical text short** — long paragraphs are riskier; **verify every word** before publishing.
- **Quality tier for final** — render text-critical finals (logos, posters) on **Quality**.

### Layerize & Magic Fill for type

- **Layerize (4.0)** turns generated text into **editable layers** you can restyle/reposition without
  regenerating — useful for getting the layout right.
- **Magic Fill** can fix a mis-rendered word or swap a line via a masked region (see
  `canvas-editing-and-recipes.md`).

### The honest typography caveat

For **precise multi-element layouts** (exact margins, multiple text blocks, logo lockups), generate the
typographic base in Ideogram and **finish in Canva/Figma**. Don't fight the model for pixel-perfect
placement.

## 2. Style consistency (a coherent set)

To make a series (carousel, campaign, brand feed) look like one family:

- **Style References** — upload up to **3 images** that carry the colours/typography/mood you want;
  reuse the **same reference across every image** in the set. Cleaner and more consistent than
  re-describing the style in prose each time.
- **Custom brand model** — for ongoing brand work, train a model on **15–100 reference images** for
  reliable on-brand output.
- **Color palette control** — lock the brand palette across the set.
- **Reuse the locked style + palette + aspect ratio** on every image; generate, then **review the set
  for drift** and regenerate the odd one out.
- **Character consistency** — a character reference keeps a recurring illustrated figure consistent
  across scenes (illustrated, not photoreal faces).

Pull the actual palette/style from `brand-profile.md` (or a Style Reference) so "on-brand" is concrete,
not guessed.

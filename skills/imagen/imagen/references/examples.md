# Examples — prompts in practice

Worked Imagen prompts showing weak→strong, photoreal product + portrait, and honest scope. Brand
context: a calm SaaS social scheduler (clean, off-white, terminal-green accent). Your output pulls the
real style from `brand-profile.md`.

---

## Weak → strong

**Weak:** "a product photo, 4k, amazing quality, professional"
**Strong:** "A matte-black smartphone on a raw concrete surface, screen showing a clean minimal
invoicing app, hard top light with crisp reflections, shot on a 50mm lens, shallow depth of field,
dry commercial product style. 4:5, 2K." (Ultra)
*(subject, setting, lighting, lens, depth of field, style, format — concrete photographic direction,
no quality spam)*

## Photoreal portrait (original, not a real person)

"Studio portrait of a fictional 30-something founder, warm confident half-smile, plain knit sweater,
85mm portrait lens, soft key light from the left, gentle falloff, shallow depth of field, natural skin
texture. 4:5, 2K." (Ultra for skin)
*(no real identifiable individual; Ultra tier for believable skin; review hands/eyes)*

## Scene/background for overlay

"A tidy wooden desk by a bright window, soft morning light, a coffee mug and closed laptop, calm
editorial mood, clean negative space top-left for text overlay, no on-image text. 9:16, 2K."
*(leave room for copy; add type later or via `ideogram`)*

---

## Honest scope (say this)

- **Review every image** — hands, faces, fine text, reflections can glitch; verify before publishing.
- **SynthID + disclosure** — every Imagen image is SynthID-watermarked; disclose AI images (EU AI Act
  Article 50; California AB 853) and sign with **C2PA**. Never pass an AI image off as a real photo.
- **No real people / no IP** — no real identifiable individuals (Imagen also restricts face gen in
  some regions), no copyrighted characters/logos, no brand styles you don't own.
- **Cost lever** — draft on **Fast**, finalize on **Ultra**; per-image pricing, clean commercial license.
- **Right tool** — photoreal → Imagen; typography/poster → `ideogram`; conversational edit →
  `nano-banana`; stylized art → Midjourney's lane (not the library's automated pick).
- **Prompt craft only** — API/model IDs/pricing + the *generate → upload to WoopSocial Media → attach*
  path live in `tools/integrations/imagen.md`; WoopSocial doesn't generate images.

---

## What the examples share
- **Direct the photograph** (subject/setting/camera/lighting/detail) — no quality spam.
- **Right tier + 2K + aspect** set up front; **brand-grounded.**
- **Reviewed, SynthID-disclosed, and IP-safe** before publishing.

# When & How to Prompt Imagen

When to reach for Imagen over its siblings, and the photographic prompt anatomy that gets believable
images. (The API/connection layer — model IDs, auth, per-image pricing — is in
`tools/integrations/imagen.md`; this is prompt craft.)

> Fast-moving area — re-verify model/specs quarterly. As of 2026: **Imagen 4** (Fast/Standard/Ultra)
> is current — photoreal leader, native 2K, clean commercial license, real API.

## Reach for Imagen when the job is…
- **Photorealism** — the standout: product shots, lifestyle/UGC-style photos, portraits/people,
  food, architecture, nature. If it must look like a real photograph, this is the tool.
- **Product / brand photography at volume** — consistent, license-clean, cheap per image.
- **Simple in-image text** in a photo (a label, a sign) — renders well (for *layout-led* type → ideogram).

## Reach for something else when…
- **Conversational / multi-turn editing** ("now change the background", iterative tweaks) or
  **web-grounded** generation → **nano-banana**.
- **Typography-led layout** (posters, logos, exact multi-line headlines, placement) → **ideogram**.
- **Stylized / painterly / editorial art** → Midjourney's lane (not the library's automated pick).
- Match the job; the **image-prompt** router picks the tool.

## The photographic prompt anatomy (shoot it like a photographer)
Describe a **photograph**, not a wish. Include:

- **Subject** — who/what, specifically (materials, state, expression).
- **Setting / context** — where, surface, background, time of day.
- **Camera** — shot type (close-up / medium / wide / macro / overhead), **lens** (e.g. 50mm, 85mm
  portrait, wide), **angle**, **depth of field** ("shallow DoF, soft bokeh").
- **Lighting** — direction/quality ("soft window light", "hard top light", "golden hour", "studio softbox").
- **Mood / style** — ("clean commercial product film", "warm editorial", "documentary").
- **Detail / realism** — textures, materials, skin, reflections (this is what reads as "real").
- **Format** — aspect ratio (4:5 / 9:16 / 1:1) and 2K; pick the tier (Fast draft / Ultra hero).

Avoid quality-spam ("4k, amazing, masterpiece") — Imagen rewards **concrete photographic direction.**

## Brand-grounded
Read `brand-profile.md` — bake the brand's palette, materials, and look into the prompt so the photo
matches the brand, not generic stock. **Review** the output (hands/faces/fine text) before publishing,
and handle **SynthID + disclosure** (see the SKILL and `tools/integrations/imagen.md`).

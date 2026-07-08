---
name: imagen
description: >-
  Use to write great prompts for Google Imagen (Imagen 4) to generate photoreal images for social
  media — the image-prompt-craft mini-skill for the PHOTOREAL branch, sibling to nano-banana and
  ideogram under the image-prompt router. Run when the user wants an Imagen / AI image prompt for a
  realistic photograph: product shots, lifestyle/UGC-style photos, portraits/people, food,
  architecture, nature, or a photoreal background/scene for a post. Reads brand-profile for style.
  Built on the verified 2026 reality: Imagen 4 (Fast/Standard/Ultra; model IDs imagen-4.0-*-generate-001;
  ~$0.02/$0.04/$0.06 per image) is the photorealism leader (skin, faces, product, nature) at native
  2K, with strong in-image text, a clean commercial license, and a real REST API (Gemini API / Vertex
  AI). Teaches the photographic prompt anatomy (subject, setting, camera/lens, lighting, mood, detail,
  format) and tier selection. Honest: every image carries a SynthID watermark and must be disclosed
  (EU AI Act Article 50, California AB 853, C2PA), Imagen restricts some face generation by region,
  never generate real identifiable people or copyrighted characters/IP/logos, and verify the output.
  Prompt-craft layer — the API/connection lives in tools/integrations/imagen.md.
metadata:
  version: 1.0.0
  license: MIT
---

# Imagen (image prompt craft)

Write prompts that get **believable photographs** out of **Google Imagen** (**Imagen 4**) — the
**photoreal** branch of the image cluster, sibling to **nano-banana** and **ideogram** under the
**image-prompt** router.

- **Connection/API** (model IDs, auth, per-image pricing, the *generate → upload to WoopSocial Media →
  attach* flow) → `tools/integrations/imagen.md`.
- **Prompt craft** (this skill) → how to direct a real-looking photo.
- **Router** → `image-prompt` picks the tool for the job.

> Fast-moving area — re-verify model names/specs quarterly.

## Reach for Imagen when… (match the job)
Its real strength: **photorealism** — product shots, lifestyle/UGC-style, portraits/people, food,
architecture, nature, and photoreal backgrounds — at **native 2K**, license-clean, cheap per image.
Reach **elsewhere** for **conversational/multi-turn editing or web-grounded** generation
(→ `nano-banana`), **typography-led layout / posters / exact text** (→ `ideogram`), or **stylized/
painterly art** (Midjourney's lane — not the library's automated pick). (Details:
`references/when-and-how-to-prompt.md`.)

## Step 0 — Read the brand + the job
Load `brand-profile.md` (palette, materials, look). Identify the **job** (product / lifestyle /
portrait / food / scene) and the **aspect ratio** (4:5, 9:16, 1:1).

## Step 1 — Direct the photograph (not quality spam)
Describe a shot like a photographer: **subject · setting · camera (shot type/lens/angle/depth of
field) · lighting · mood/style · detail/realism · format**. Ground in the brand. Avoid "4k, amazing,
masterpiece" — Imagen rewards concrete photographic direction. See `references/when-and-how-to-prompt.md`.

## Step 2 — Pick the tier (verify-quarterly)
**Fast** (~$0.02) for drafts/volume · **Standard** (~$0.04) the 2K workhorse · **Ultra** (~$0.06) for
hero shots, faces/skin, fine detail. Draft on Fast → finalize on Ultra. Full capabilities + how it
differs from siblings: `references/imagen-2026-capabilities.md`; recipes + worked shots:
`references/recipes-and-tiers.md`.

## Step 3 — Verify, disclose, ship
- **Verify** every image (hands, faces, fine text, reflections) before publishing.
- **Disclose** AI images — every Imagen image is **SynthID**-watermarked; EU AI Act **Article 50**,
  **California AB 853**; sign with **C2PA**. Never pass an AI image off as a real photo.
- **Ship:** generate per the integration guide → **upload to WoopSocial Media → attach** via
  `scheduling-and-queue`. WoopSocial doesn't generate images.

## Quality bar — self-check
- Did I **match the tool to the job** (route conversational → nano-banana, typography → ideogram)?
- Is the prompt a **directed photograph** (subject/setting/camera/lighting/detail), **brand-grounded**,
  with **tier + 2K + aspect** set — and **no quality spam**?
- Did I plan **draft-cheap → finalize-Ultra**, and **review** the output?
- Did I handle **SynthID + disclosure (Art. 50 / AB 853 / C2PA)** and **refuse real people / IP / logos**
  (incl. Imagen's regional face-gen limits)?
- Did I point to **`tools/integrations/imagen.md`** for the API + WoopSocial flow (no claim WoopSocial
  generates images)?

## Edge cases & pushback
- **Poster / exact multi-line headline / logo** → that's `ideogram` (layout); use Imagen for the
  photoreal background, ideogram for the type.
- **"Now change the background" / iterative edits** → route to `nano-banana`.
- **Real person / copyrighted IP or logo / "post as a real photo"** → refuse; SynthID + disclosure;
  offer an original/owned alternative.
- **"a product, photoreal, 4k, amazing"** → rewrite into a directed photograph (subject/lens/lighting/detail).
- **"Generate it in WoopSocial"** → WoopSocial doesn't generate; this prompts Imagen, then the image is
  uploaded to Media and attached.

## Related
- `tools/integrations/imagen.md` — API/model IDs (Gemini API / Vertex AI), per-image pricing, the WoopSocial flow.
- `image-prompt` — the router; `nano-banana` — conversational/web-grounded sibling; `ideogram` —
  typography/layout sibling.
- `brand-profile` — the visual brand; `caption-writer`/`hook-writer` — copy that pairs with the image;
  `veo-3` — animate a still into video (image-to-video).
- `scheduling-and-queue` — attach the image to a post and publish.

## References
- `references/when-and-how-to-prompt.md` — when to reach for Imagen vs siblings, and the photographic anatomy.
- `references/imagen-2026-capabilities.md` — tiers, model IDs, pricing, photoreal strengths, sibling differences.
- `references/recipes-and-tiers.md` — tier selection + photoreal social recipes + worked shots.
- `references/examples.md` — weak→strong, a product hero, a portrait, and honest scope.

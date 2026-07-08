# Imagen 2026 capabilities — verified

*Volatile. Re-verify quarterly against ai.google.dev / Vertex AI docs. Confirm model IDs/prices before
building.*

## What it is
Google's dedicated **photoreal** text-to-image model (**Imagen 4**, April 2026, S-tier). It targets
the realism others miss — **skin, faces, nature, product, architecture** — at **native 2K**, with
**first-class in-image text rendering**, a **clean commercial license**, and a **real REST API**
(Gemini API + Vertex AI). The photoreal branch of the image cluster.

## Tiers + API (verify-quarterly)
| Tier | Model ID | Price/img | Notes |
|---|---|---|---|
| Fast | `imagen-4.0-fast-generate-001` | ~$0.02 | ~2.7s; drafts/volume; up to ~1408×768 |
| Standard | `imagen-4.0-generate-001` | ~$0.04 | ~5–8s; the 2K workhorse |
| Ultra | `imagen-4.0-ultra-generate-001` | ~$0.06 | ~10–15s; native 2K; best skin/detail/fidelity |

REST via **Gemini API** (`ai.google.dev`) and **Vertex AI** (GCP-native). **Pay-per-image, no
subscription.** Every image carries an invisible **SynthID** watermark.

## Strengths
- **Photorealism leader** — natural skin, accurate lighting, zero waxy artifacts; product/portrait/
  architecture/food/nature. Reviewers rate it S-tier on photoreal benchmarks (April 2026).
- **Text rendering** — strong across all tiers (good for simple labels/signage in a photo).
- **License-clean** — safe for client/commercial work; cheap at volume ($0.02 Fast).

## Limits / honest caveats
- **Regional face-gen restrictions** — Google limits certain human-face generation in some regions
  (bias controversy). Don't assume a face prompt will run everywhere.
- **No real identifiable people, no copyrighted IP/logos/brand styles you don't own.**
- Artifacts still happen (hands, fine text, complex scenes) — **review every image.**
- Image-only output (text prompt → image); for multi-turn conversational editing use a different tool.

## How it differs from its siblings (route via image-prompt)
- **vs nano-banana (Gemini Flash Image):** Imagen is the **specialist** (text→image, photoreal,
  cheaper, better text, pay-per-image); **nano-banana is conversational/multimodal** (multi-turn
  edits, web-grounded). Different lanes — not redundant.
- **vs ideogram:** Imagen for **photoreal**; **ideogram** for **typography-led layout** (posters,
  logos, exact multi-line text via JSON). For a poster: Imagen background + ideogram type.
- **vs Midjourney:** Midjourney leads **artistic/stylized/painterly** work but its **API is limited
  release with restrictive commercial terms** (and an active Disney lawsuit) — so it's **not** the
  library's automated pick. Imagen is the **photoreal + API-clean** choice. (Add a manual `midjourney`
  skill later only if the stylized branch is needed.)

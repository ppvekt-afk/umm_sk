# Versions

Version numbers track the plugin/marketplace release (`.claude-plugin/plugin.json`). Bump the
version there and in `.claude-plugin/marketplace.json` on every release so plugin users receive
updates; attach freshly built `dist/` ZIPs to each GitHub release.

## v1.0.0 — July 2026

Initial public release.

- **106 skills across 14 topics** — strategy & foundation, ideas & content angles, copy &
  captions, video scripts, AI video, visual & design, voice & music, editing & clipping,
  platform growth (all 9 platforms), planning & publishing, hashtags & SEO, community,
  influencer & monetization, analytics & optimization.
- Every skill: `SKILL.md` + 3–5 reference files + evals. All facts editorially reviewed and
  web-verified July 2026.
- **19 tool integration guides** (`tools/integrations/`) + registry.
- **17 topic packs** (`scripts/packs.json`) with per-skill ZIPs for claude.ai web upload;
  referenced tool guides are embedded into each skill ZIP at build time.
- Installable via `npx skills add`, Claude Code plugin marketplace, direct copy, ZIP upload
  (claude.ai), OpenClaw, and Hermes.

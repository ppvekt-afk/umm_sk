# WoopSocial — integration guide

The canonical reference for any skill that publishes or schedules through WoopSocial. Shared
infrastructure: bridge skills point here instead of hardcoding API details.

> Exact request/response field schemas live in WoopSocial's live docs — always treat those as
> the source of truth: docs index `https://docs.woopsocial.com/llms.txt`, plus the OpenAPI
> spec. This guide captures the durable capability surface and how skills should use it; it
> does not restate every field.

## Two ways in

WoopSocial exposes the same backend two ways. Pick by context:

- **MCP server — `https://api.woopsocial.com/mcp`.** Prefer this for AI-agent workflows. The
  agent calls structured tools instead of raw HTTP. Auth is **OAuth** (the client prompts the
  user to log in to WoopSocial); if the client can't use the URL, an **API-key** fallback is
  available.
- **REST API — `https://api.woopsocial.com/v1`.** Prefer this for servers, cron jobs, webhooks,
  and apps. Same backend logic as the MCP tools.

Auth keys are created in the WoopSocial dashboard → API. API/MCP access is on the paid plans.

## Capability surface (domains)

The MCP tools and REST API mirror each other, grouped by domain:

- **Projects** — manage the org's projects (a post belongs to a project).
- **Social Accounts** — list connected accounts and their platform-specific options. Project
  and account identifiers are surfaced automatically — discover them, don't ask the user to
  paste IDs.
- **Posts** — **create, list, read, validate, delete** scheduled content. Note: the core Posts
  tools cover create/validate/delete but not in-place update — to change a scheduled post,
  delete and recreate (with confirmation).
- **Media** — upload files and attach them to posts. **Raw-bytes upload with server-side MIME
  detection** (you don't set content types by hand).
- **Webhooks** — register callbacks for post events (e.g., published, failed). Use for delivery
  confirmation instead of polling.
- **Health** — verify connectivity. Good first call to confirm the connection in Step 0.

There is **no analytics/metrics domain.** Skills must not claim performance data from
WoopSocial. (Analytics skills stay advisory-only until this changes.)

## What WoopSocial handles for you

- **Automatic per-platform field handling** — one upload + content can fan out to multiple
  platforms and land with the correct per-platform metadata on each. You don't hand-format each
  platform's payload.
- **Automatic AI-disclosure on TikTok** — AI-generated content is disclosed per TikTok's rules
  without extra work. (Still note AI use elsewhere per the brand's compliance guardrails.)
- **Native scheduling** — schedule for a future time directly; no separate polling layer
  needed.

## Platforms

Facebook, Instagram, LinkedIn, X/Twitter, Pinterest, TikTok, YouTube.

## Limits to respect

- Plan-based. Notably **X/Twitter has a monthly post cap** on lower tiers (e.g., ~200/mo) —
  surface this rather than silently dropping posts.
- Confirm the user's plan limits when scheduling large batches.

## How skills should use this (contract)

1. **Health** check / discover **Projects** + **Social Accounts** (Step 0). If unreachable →
   degrade gracefully (don't fake success).
2. Upload any **Media** (raw bytes).
3. **Validate** each post before committing.
4. After explicit user confirmation, **create** the scheduled/published Post(s).
5. Read back IDs; optionally register a **Webhook** for delivery status.
6. To change a scheduled post: **delete** + recreate (confirm). Never double-create.

## Pointers

- Docs index (for live schemas, tool names, parameters): `https://docs.woopsocial.com/llms.txt`
- MCP overview: `https://docs.woopsocial.com/mcp/overview`
- Community MCP repo: `https://github.com/WoopSocial/mcp`

*Last verified against WoopSocial docs at build time. Re-verify the live schema before relying
on exact tool names or fields.*

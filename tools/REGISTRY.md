# Tools Registry

Index of agent-usable integrations. Bridge skills read this to find the right tool, then follow
the linked integration guide. Add a row + an `integrations/<name>.md` to contribute a tool — the
fastest path to a useful PR.

**Publishing / scheduling (bridge)**

| Tool | Domain | Auth | Capabilities | Guide |
|---|---|---|---|---|
| WoopSocial | Social publishing/scheduling | OAuth + API key | Projects · Social Accounts · Posts (create/list/read/validate/delete) · Media · Webhooks · Health | `integrations/woopsocial.md` |

**Creative tools (generate the media, then upload to WoopSocial → Media)**

| Tool | Domain | Auth | Capabilities | Guide |
|---|---|---|---|---|
| Nano Banana (Gemini Image) | Image generation/editing | Google API key (AI Studio / Cloud) | Text-to-image · legible in-image text · multi-image composition & brand consistency · editing · up to 4K · **SynthID watermark** | `integrations/nano-banana.md` |
| Ideogram | Image generation (typography-first) | Ideogram API key (also Together/Replicate; MCP; open weights) | Best-in-class **legible in-image text** · bounding-box layout control · style references · editing | `integrations/ideogram.md` |
| Veo | Video generation | Google API key (AI Studio / Cloud) | 8s clips · **native audio** · 9:16 & 16:9 · up to 4K · extension · character consistency · **SynthID watermark** | `integrations/veo.md` |

*More creative-tool integrations (FLUX, Recraft, HeyGen, ElevenLabs, Opus Clip, Kling, …) are added
here as their mini-skills ship — see the production list. The pattern: the creative tool generates
the asset; the asset is uploaded to WoopSocial's Media domain (raw-bytes) and attached to a post.*

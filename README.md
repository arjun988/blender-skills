# AAA Blender Skills Pack

Professional Blender Agent Skills for Cursor and Claude Code. Transform your AI assistant into a Senior Technical Art team — not a tutorial bot.

Inspired by the [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) architecture.

## Quick Start

See **[QUICKSTART.md](QUICKSTART.md)** for the full setup guide.

### Claude Code Plugin

```bash
/plugin marketplace add your-username/blender-skills
/plugin install aaa-blender-skills@your-username
```

Update `your-username` in `.claude-plugin/marketplace.json` before publishing.

### Cursor

This repo includes preconfigured Blender MCP at [`.cursor/mcp.json`](.cursor/mcp.json).

Sync skills to Cursor:

```powershell
Copy-Item -Recurse -Force ".claude\skills\*" ".cursor\skills\"
```

Restart Cursor after setup.

### Claude Code (Manual)

```bash
cp -r .claude/skills /path/to/your/project/.claude/skills/
```

## Blender MCP

**This repo ships MCP config.** Connect Blender before asset work:

1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/)
2. Install [BlenderMCP addon](https://github.com/ahujasid/blender-mcp) in Blender
3. Blender sidebar (N) → **BlenderMCP** → **Connect to Claude**
4. Restart Cursor — verify `blender` MCP server is active

Full guide: **[docs/BLENDER_MCP_SETUP.md](docs/BLENDER_MCP_SETUP.md)**

| Config File | Client |
|-------------|--------|
| `.cursor/mcp.json` | Cursor (project) |
| `.mcp.json` | Claude Code (project) |

Skills reference:
- [.claude/skills/references/mcp-integration.md](.claude/skills/references/mcp-integration.md) — Agent protocol
- [.claude/skills/references/mcp-tools.md](.claude/skills/references/mcp-tools.md) — Tool catalog

## Philosophy

Every skill:

- **Thinks before acting** — Plans the full pipeline
- **Uses Blender MCP** — Executes via MCP when available, not UI walkthroughs
- **Matches reference images** — Analyze photo first, camera match, screenshot compare loop
- **Follows production standards** — Naming, validation, game-ready output
- **Coordinates via Blender Director** — Orchestrates multi-discipline workflows

## Reference Image Workflow

When you attach a photo or concept art:

1. Agent reads [reference-image-match.md](.claude/skills/references/reference-image-match.md)
2. Writes analysis using [reference-analysis-template.md](.claude/skills/references/reference-analysis-template.md)
3. Matches camera → geometry (silhouette → panels → detail) → materials → lighting → grading
4. Compares viewport screenshots to your image (up to 3 refinement passes)
5. Validates with [visual-match-checklist.md](.claude/skills/references/visual-match-checklist.md)

See [SKILLS_GUIDE.md](SKILLS_GUIDE.md) for the full workflow combination.

## Skills (23)

| Category | Skills |
|----------|--------|
| **Orchestration** | [blender-director](.claude/skills/blender-director/) |
| **Modeling** | [blender-modeler](.claude/skills/blender-modeler/), [hard-surface](.claude/skills/hard-surface/), [environment-artist](.claude/skills/environment-artist/), [character-artist](.claude/skills/character-artist/), [creature-artist](.claude/skills/creature-artist/) |
| **Workflow** | [sculpting](.claude/skills/sculpting/), [retopology](.claude/skills/retopology/), [uv-workflow](.claude/skills/uv-workflow/), [materials](.claude/skills/materials/), [texture-workflow](.claude/skills/texture-workflow/) |
| **Technical** | [geometry-nodes](.claude/skills/geometry-nodes/), [lighting](.claude/skills/lighting/), [rendering](.claude/skills/rendering/), [animation](.claude/skills/animation/), [rigging](.claude/skills/rigging/) |
| **Pipeline** | [procedural-modeling](.claude/skills/procedural-modeling/), [asset-optimization](.claude/skills/asset-optimization/), [export-pipeline](.claude/skills/export-pipeline/) |
| **Style** | [horror-style](.claude/skills/horror-style/), [lowpoly-style](.claude/skills/lowpoly-style/), [stylized-style](.claude/skills/stylized-style/), [realistic-style](.claude/skills/realistic-style/) |

## Universal Pipeline

Every asset follows: Reference → Planning → Scale → Modeling → Cleanup → UVs → Materials → Optimization → Export → Validation

See [.claude/skills/references/asset-pipeline.md](.claude/skills/references/asset-pipeline.md)

## Example Prompts

```
Match this reference photo — industrial spaceship, matte grey hull, analyze first then build in Blender
```

```
Create a modular sci-fi wall kit for Unreal Engine with 2m grid snapping
```

```
Block out a horror corridor inspired by Silent Hill — narrow, fluorescent lighting
```

```
Retopologize this creature sculpt for game animation, 15k triangle budget
```

```
Export this character with walk cycle to FBX for Unity
```

## Project Structure

```
.claude-plugin/          # Claude Code plugin manifest
.claude/skills/          # Skill source (23 skills + references)
.cursor/mcp.json         # Blender MCP config for Cursor
.mcp.json                # Blender MCP config for Claude Code
docs/BLENDER_MCP_SETUP.md
QUICKSTART.md
SKILLS_GUIDE.md
```

## Documentation

| Doc | Purpose |
|-----|---------|
| [QUICKSTART.md](QUICKSTART.md) | Installation and first steps |
| [SKILLS_GUIDE.md](SKILLS_GUIDE.md) | Decision trees and skill combinations |
| [docs/BLENDER_MCP_SETUP.md](docs/BLENDER_MCP_SETUP.md) | Blender MCP connection |
| [.claude/skills/references/](.claude/skills/references/) | Shared pipeline standards |

## License

MIT — See [LICENSE](LICENSE)

# Blender Skills Project

AAA Blender Agent Skills Pack for Cursor and Claude Code with Blender MCP integration.

## Project Structure

```
.claude-plugin/          # plugin.json + marketplace.json
.claude/skills/          # 23 specialist skills + shared references
.cursor/mcp.json         # Blender MCP (Cursor)
.mcp.json                # Blender MCP (Claude Code)
docs/BLENDER_MCP_SETUP.md
```

## Agent Instructions

1. For Blender asset tasks, read **blender-director** first for complex work
2. **Check Blender MCP** — if connected, execute via MCP; never narrate UI steps
3. Read MCP tool schemas before calling (see `references/mcp-tools.md`)
4. Follow universal pipeline in `references/asset-pipeline.md`
5. Validate before export using `references/validation-checklist.md`
6. Use naming conventions from `references/naming-conventions.md`

## MCP Setup

Blender must be running with the BlenderMCP addon connected. See `docs/BLENDER_MCP_SETUP.md`.

## Key Files

- `QUICKSTART.md` — Installation
- `SKILLS_GUIDE.md` — Decision trees and workflows
- `README.md` — Overview

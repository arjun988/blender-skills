# Blender MCP Integration Rules

When Blender MCP is available, **execute operations through MCP** instead of describing manual UI steps.

**Setup:** See repo `docs/BLENDER_MCP_SETUP.md`. Project config: `.cursor/mcp.json` (Cursor) or `.mcp.json` (Claude Code).

**Tool catalog:** See `mcp-tools.md` for BlenderMCP capabilities and bpy fallbacks.

## Priority Order

1. Check MCP tool descriptors before any Blender operation
2. Read tool schemas for required parameters
3. Execute via MCP tools
4. Validate results via MCP scene queries
5. Only fall back to UI instructions if MCP lacks the capability

## MCP-First Operations

| Task | MCP Approach |
|------|--------------|
| Create objects | Use MCP object creation tools |
| Modify geometry | Use MCP mesh/edit tools |
| Apply modifiers | Use MCP modifier tools |
| UV operations | Use MCP UV tools if supported |
| Materials | Create/assign materials via MCP |
| Collections | Organize scene hierarchy via MCP |
| Export | Use MCP export tools |
| Validation | Query scene stats via MCP |

## Execution Protocol

```
1. List available MCP tools for Blender server
2. Read schema for each tool before calling
3. Plan operation sequence (non-destructive first)
4. Execute step-by-step with validation between steps
5. Report object names, counts, and metrics after each phase
```

## Scene Organization via MCP

When creating assets, immediately establish:

```
Scene Root
├── COL_Reference
├── COL_Blockout
├── COL_HighPoly
├── COL_LowPoly
├── COL_Collision
├── COL_Lights
└── COL_Export
```

Naming prefixes: see `naming-conventions.md`

## Non-Destructive Defaults

- Create duplicates before destructive operations
- Keep backup collections hidden, not deleted
- Apply modifiers only at export phase unless required for downstream work
- Document modifier stack in planning output

## Validation Queries

After major phases, query via MCP:

- Object count and names
- Polygon/triangle counts per object
- Material count
- Collection membership
- Origin/pivot locations
- Transform application status

## Error Handling

If MCP call fails:
1. Read error message completely
2. Check if Blender is running and MCP connected
3. Verify object/mesh names match scene state
4. Retry with corrected parameters
5. Never silently skip failed operations

## Anti-Patterns

- ❌ "Press Tab to enter Edit Mode, then..."
- ❌ Long UI walkthroughs when MCP can execute
- ❌ Assuming scene state without querying
- ❌ Destructive apply without backup
- ❌ Export without validation pass

## Fallback Mode

When Blender MCP is unavailable:
- Provide concise planning and specifications
- Output Python `bpy` scripts the user can run
- Include validation checklist for manual verification
- Note which steps require MCP for full automation

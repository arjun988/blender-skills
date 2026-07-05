---
name: asset-optimization
description: Validates and optimizes Blender assets for polycount, topology, UV efficiency, material count, naming, collections, and game-ready performance. Use before export on all production assets via MCP.
license: MIT
metadata:
  author: blender-skills
  version: "1.0.0"
  domain: blender
  role: specialist
  triggers: optimize, optimization, polycount, LOD, cleanup, performance, game ready, validate, triangle count
  related-skills: export-pipeline, blender-director, uv-workflow
---

# Asset Optimization

Enforce budgets. Clean geometry. Game-ready validation gate before export.

## When to Use

- Before every export
- After modeling complete
- LOD generation
- Scene-wide performance audit
- Pre-delivery validation

## Workflow

```
Audit → Identify Issues → Fix → Re-Audit → LOD Generation → Validation Report
```

## Audit Checklist

Run via MCP scene queries where possible:

### Geometry
- [ ] Triangle count vs budget (`../references/polycount-budgets.md`)
- [ ] Duplicate vertices merged
- [ ] Loose geometry removed
- [ ] Non-manifold fixed
- [ ] Interior faces deleted
- [ ] Applied transforms (scale 1,1,1)

### UVs
- [ ] Pack efficiency > 75%
- [ ] Texel density consistent
- [ ] No unintended overlaps

### Materials
- [ ] Count within budget
- [ ] No unused slots
- [ ] Names follow `MAT_` convention

### Organization
- [ ] All objects named `SM_` prefix
- [ ] Collections organized per convention
- [ ] Collision meshes in `COL_Collision`

## Optimization Techniques

| Issue | Fix |
|-------|-----|
| Over budget | Remove unseen geo, decimate, bake detail |
| High triangle count on flat surfaces | Reduce subdiv/bevel segments |
| Many draw calls | Merge materials; atlas textures |
| Repeated geometry | Convert to instances |
| Heavy modifiers | Apply and merge strategically |

## LOD Generation

```
LOD0: Full detail (hero)
LOD1: 50% tris — remove micro-bevels, small greebles
LOD2: 25% tris — decimate modifier; preserve silhouette
LOD3: 10% tris — impostor/card or simple proxy
```

Naming: `SM_Asset_LOD0`, `SM_Asset_LOD1`, etc.

Use Decimate modifier:
- Planar mode for hard surface
- Collapse mode for organic
- Always verify silhouette after decimate

## Modifier Cleanup

Before export:
1. Apply stack OR export with modifiers per engine support
2. Remove unused modifiers
3. Collapse mirror/array if instances not needed
4. Document which modifiers remain live

## Scene Audit Report Template

```markdown
## Optimization Report: [Asset/Scene]

**Total Triangles:** [count] (budget: [target])
**Draw Calls (materials):** [count]
**Objects:** [count]
**Issues Fixed:** [list]

### Per-Object Breakdown
| Object | Tris | Materials | Status |
|--------|------|-----------|--------|
| SM_... | ... | ... | PASS/FAIL |
```

## MCP Integration

1. Query polycount per object via MCP
2. Query material count via MCP
3. Run cleanup operations via MCP
4. Generate LOD duplicates via MCP
5. Validate naming conventions via MCP scene tree

## Constraints

### MUST DO
- Run full validation before export
- Document polycount in production brief
- Create LODs for hero assets in games
- Fix all non-manifold before export
- Output validation report

### MUST NOT DO
- Export without budget check
- Decimate deforming meshes without testing
- Remove collision proxies
- Skip naming convention validation
- Optimize hero face/hands below animation needs

## Reference Guide

| Topic | Reference | Load When |
|-------|-----------|-----------|
| Full validation | `../references/validation-checklist.md` | Final gate |
| Polycount budgets | `../references/polycount-budgets.md` | Budget setting |
| LOD strategies | `references/lod-strategies.md` | LOD creation |

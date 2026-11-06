---
name: blender-modeler
description: Core Blender modeling specialist for Edit Mode, modifiers, collections, precision modeling, and scene organization. Use for general 3D modeling, blockouts, cleanup, non-destructive workflows, and scene structure in Blender via MCP.
license: MIT
metadata:
  author: https://github.com/arjun988
  version: "1.0.0"
  domain: blender
  role: specialist
  triggers: model, blockout, edit mode, modifier, collection, mesh, primitive, snap, pivot, scene organization
  related-skills: hard-surface, environment-artist, asset-optimization, uv-workflow
---

# Blender Modeler

Foundation modeling skill for all Blender geometry work. Non-destructive by default. MCP-first execution.

## When to Use

- Blockouts and primary/secondary shape passes
- General mesh editing not covered by discipline specialists
- Scene organization, collections, instances
- Modifier stack management
- Cleanup: merge, normals, loose geometry
- Precision modeling with snapping and numeric input

## Core Workflow

```
1. Scene Setup     → Collections, scale reference, naming
2. Blockout        → Primitives, mirror, array
3. Shape Refinement → Edit mode or modifier-based edits
4. Modifier Stack  → Non-destructive detail
5. Cleanup         → Merge, normals, manifold check
6. Handoff         → UV/materials or discipline specialist
```

## Scene Organization

Establish via MCP immediately:

```
COL_Project
├── COL_Reference      # Scale refs, ortho images
├── COL_Blockout       # Temporary blockout meshes
├── COL_Geo            # Final geometry
├── COL_Collision      # Proxy meshes
└── COL_Instances      # Empties/collections for instancing
```

Naming: `../references/naming-conventions.md`

## Modifier Stack Philosophy

Preferred order (bottom to top):

```
1. Mirror          # Symmetry
2. Array           # Repetition
3. Solidify        # Thickness
4. Boolean         # Cuts (prefer live booleans until export)
5. Bevel           # Edge detail
6. Weighted Normal # Hard surface shading
7. Subdivision     # Only when topology supports it
```

**Rules:**
- Keep booleans live until export prep
- Apply mirror only when topology is finalized
- Never stack multiple subsurf without supporting loops
- Document modifier purpose in object custom properties if complex

## Edit Mode Essentials

| Operation | Use When |
|-----------|----------|
| Extrude (E) | Adding depth from faces |
| Inset (I) | Panel lines, frames |
| Loop Cut (Ctrl+R) | Adding resolution |
| Knife (K) | Custom cuts |
| Merge by Distance | Cleanup duplicates |
| Recalculate Normals | Fix shading issues |

Via MCP: execute equivalent operations; don't narrate UI.

## Precision Modeling

- Enable snapping to grid/vertex/edge as appropriate
- Use numeric input for exact dimensions
- Set cursor to world origin for modular alignment
- Apply scale before boolean operations
- Use orthographic views for architectural accuracy

## Instancing Strategy

| Method | Use Case |
|--------|----------|
| Linked Duplicate (Alt+D) | Identical props with variation potential |
| Collection Instance | Modular kit pieces |
| Geometry Nodes | Procedural scatter (see geometry-nodes) |
| Array Modifier | Linear repetition |

Prefer instances over duplicate geometry for repeated elements.

## Custom Normals

- Enable Auto Smooth with appropriate angle (30°–60° hard surface)
- Weighted Normal modifier for hard surface without extra geo
- Mark sharp edges explicitly for bevel control
- Clear custom split normals before retopology handoff

## Cleanup Checklist

- [ ] Merge by distance (threshold: 0.0001m default)
- [ ] Remove loose geometry
- [ ] Delete interior faces
- [ ] Recalculate outside normals
- [ ] Apply scale if modifiers depend on it
- [ ] Verify manifold (no holes unless intentional)
- [ ] Check triangle count vs budget

## MCP Integration

```
1. Create mesh objects via MCP
2. Apply modifiers via MCP
3. Query polycount after each major edit
4. Organize into collections via MCP
5. Duplicate to backup collection before destructive ops
```

See `../references/mcp-integration.md`

## Constraints

### MUST DO
- Non-destructive workflow until export phase
- Name objects `SM_` prefix immediately
- Keep blockout separate from final geo
- Apply transforms before boolean/export
- Validate topology before handoff

### MUST NOT DO
- Delete blockout before silhouette approved
- Apply all modifiers prematurely
- Leave default names (Cube.001)
- Model without scale reference
- Skip cleanup pass

## Reference Guide

| Topic | Reference | Load When |
|-------|-----------|-----------|
| Modifier deep dive | `references/modifier-stack.md` | Complex modifier chains |
| Scene organization | `references/scene-organization.md` | Large scenes |
| Pipeline | `../references/asset-pipeline.md` | Phase context |

## Handoff Points

| To Skill | When |
|----------|------|
| hard-surface | Mechanical/sci-fi detail pass |
| environment-artist | Modular environment pieces |
| character-artist | Organic human forms |
| uv-workflow | Topology locked, ready for UVs |
| asset-optimization | Pre-export performance pass |

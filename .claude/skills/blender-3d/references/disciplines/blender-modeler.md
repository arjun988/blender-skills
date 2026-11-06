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

Naming: `naming-conventions.md` (shared)

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

See `mcp-integration.md` (shared)

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
| Pipeline | `asset-pipeline.md` (shared) | Phase context |

## Handoff Points

| To Skill | When |
|----------|------|
| hard-surface | Mechanical/sci-fi detail pass |
| environment-artist | Modular environment pieces |
| character-artist | Organic human forms |
| uv-workflow | Topology locked, ready for UVs |
| asset-optimization | Pre-export performance pass |
# Modifier Stack Reference

## Boolean Workflow

```
1. Ensure both operands have applied scale
2. Use exact/overlap solver for mechanical cuts
3. Keep boolean live; duplicate result for backup
4. Apply bevel AFTER boolean (bevel modifier below boolean in stack = wrong)
5. Correct order: Boolean → Bevel → Weighted Normal
```

## Bevel Settings

| Context | Width | Segments | Profile |
|---------|-------|----------|---------|
| Hard surface panel | 0.001–0.005m | 2–3 | 0.5 |
| Chamfer edge | 0.002–0.01m | 1–2 | 0.5 |
| Soft edge | 0.001m | 3–5 | 0.7 |

Limit bevel to marked edges or weight groups for control.

## Mirror Modifier

- Use bisect for half-model workflows
- Clip enabled to prevent center overlap
- Merge threshold: 0.001m default
- Apply only when center loop is clean

## Array Modifier

- Use constant offset for modular pieces
- Fit type: Fixed Count for known repetitions
- Merge vertices at array boundaries when seamless

## Subdivision Surface

- Only on quad-dominant topology
- Level 1 for preview, Level 2 max for hero assets
- Support loops required at hard edges
- Never subsurf boolean results without cleanup

## Common Stack Examples

**Modular wall panel:**
```
Mirror → Solidify → Bevel (weight) → Weighted Normal
```

**Repeated floor tile:**
```
Array → Bevel → Weighted Normal
```

**Blockout (temporary):**
```
Mirror → Array (no bevel yet)
```

# Scene Organization

## View Layers

| Layer | Contents |
|-------|----------|
| Default | Active modeling |
| Reference | Image planes, scale refs |
| Blockout | WIP blockout only |
| Final | Approved geometry |
| Export | Export-ready duplicates |

## Parenting Strategy

- Parent mechanical sub-parts to root empty: `SM_AssetName_Root`
- Keep pivot at functional point (hinge, grip, floor)
- Use constraints for mechanical relationships (see rigging skill)

## Asset Browser Integration

- Mark finished assets for reuse
- Tag by category: Prop, Env, Char, Weapon
- Include preview render in asset catalog

## Large Scene Management

- One collection per modular kit
- Instance collections, don't duplicate
- Hide blockout collections after approval
- Use collection colors for discipline identification

## Performance in Viewport

- Disable subdiv viewport levels during modeling
- Use wireframe overlay for topology review
- Hide high-poly sculpts when working on low-poly


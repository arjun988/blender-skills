---
name: geometry-nodes
description: Blender Geometry Nodes for procedural modeling, scatter systems, vegetation, buildings, pipes, cables, and reusable node groups. Use for procedural asset generation and instancing pipelines via MCP.
license: MIT
metadata:
  author: https://github.com/arjun988
  version: "1.0.0"
  domain: blender
  role: specialist
  triggers: geometry nodes, procedural, scatter, node group, GN_, instancing, parametric
  related-skills: procedural-modeling, environment-artist, blender-modeler
---

# Geometry Nodes

Reusable procedural systems. Parametric assets. Performance-aware instancing.

## When to Use

- Scatter systems (rocks, vegetation, debris)
- Parametric buildings, roads, pipes, cables
- Procedural variation without unique modeling
- Kit assembly with randomization
- Non-destructive iteration on large scenes

## Workflow

```
Define Parameters → Build Node Tree → Create Node Group (GN_)
    → Test Variations → Bake/Instance Decision → Export Integration
```

## Node Group Standards

- Prefix: `GN_[System]_[Descriptor]`
- Expose only necessary inputs (seed, density, scale range)
- Document input ranges in group name or custom properties
- Version node groups: `GN_Scatter_Rocks_v02`

## Core Patterns

### Scatter System
```
Mesh Surface → Distribute Points on Faces → Instance on Points
    → Randomize Rotation (Z) → Randomize Scale → Realize (optional)
```

### Building Generator
```
Floor Count (input) → Repeat Mesh → Stack Instances
    → Window Cut Pattern → Material Variation → Output
```

### Cable/Pipe Routing
```
Curve Input → Curve to Mesh (profile) → Subdivide → Set Material
    → Multiple curves from single path node
```

### Rock Formation
```
Ico Sphere → Displace (noise) → Decimate → Instance Scatter
```

## Randomization

| Parameter | Typical Range |
|-----------|---------------|
| Scale | 0.8–1.2 (uniform or per-axis) |
| Rotation Z | 0–360° |
| Density | 0.1–2.0 per m² |
| Seed | Integer for reproducibility |

Always expose seed as group input for art direction iteration.

## Performance Rules

| Scenario | Approach |
|----------|----------|
| Game export | Realize instances → decimate → export mesh |
| Background scatter | Keep instanced; limit count |
| Hero procedural | Bake to static mesh for engine |
| Viewport preview | Limit instance count attribute |

## Reusable Systems Library

| Group | Purpose |
|-------|---------|
| GN_Scatter_Objects | Generic surface scatter |
| GN_Array_Modular | Linear modular repetition |
| GN_Curve_Pipe | Pipe/cable along curve |
| GN_Wall_Variant | Parametric wall sections |
| GN_Vegetation_Cluster | Tree/bush clustering |

## MCP Integration

1. Create geometry nodes modifier via MCP
2. Configure group inputs via MCP
3. Query instance count and final polycount
4. Realize geometry for export via MCP
5. Organize GN objects in dedicated collection

## Integration with Export

Before export:
1. Apply geometry nodes modifier OR
2. Realize instances and merge OR
3. Export as instances if engine supports (Unreal HISM)

Document which approach per target engine.

## Constraints

### MUST DO
- Create reusable node groups, not one-off trees
- Expose seed and density as inputs
- Test at min/max parameter extremes
- Realize/bake before game export unless engine supports instances
- Name groups with `GN_` prefix

### MUST NOT DO
- Million-instance scatter without LOD/culling plan
- Nested realize operations (performance killer)
- Hardcode values that should be inputs
- Export procedural without polycount validation
- Skip variation testing at boundary values

## Reference Guide

| Topic | Reference | Load When |
|-------|-----------|-----------|
| Scatter recipes | `references/scatter-systems.md` | Environment scatter |
| Building generators | `references/building-generators.md` | Architectural procedural |

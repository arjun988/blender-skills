---
name: procedural-modeling
description: Procedural asset creation for rocks, buildings, vegetation, roads, terrain, pipes, cables, and sci-fi panels using Geometry Nodes and modifier-based workflows in Blender via MCP.
license: MIT
metadata:
  author: https://github.com/arjun988
  version: "1.0.0"
  domain: blender
  role: specialist
  triggers: procedural modeling, procedural rock, procedural building, terrain, road, pipe, cable, sci-fi panel, parametric
  related-skills: geometry-nodes, environment-artist, blender-modeler
---

# Procedural Modeling

Parametric assets with art-directable variation. Geometry Nodes priority. Bake for game export.

## When to Use

- Rocks, cliffs, terrain features
- Modular building generation
- Road and path systems
- Pipe/cable networks
- Sci-fi panel arrays
- Vegetation placement systems

## Workflow

```
Define Parameters → Build Procedural System → Validate Variations
    → Realize/Bake → Optimize → Export
```

## System Categories

| System | Primary Tool | Output |
|--------|--------------|--------|
| Rocks | Geo Nodes + noise | Static mesh |
| Buildings | Geo Nodes stack | Modular pieces |
| Roads | Curve + Geo Nodes | Mesh strip |
| Pipes | Curve to mesh | Network |
| Vegetation | Scatter GN | Instanced/baked |
| Sci-fi panels | Array + random | Trim sheet geo |

## Rock Generation

```
Base shape (ico sphere) → Displace (multi-scale noise)
    → Decimate → Subdivide (selective) → Weighted Normal
    → Variation: seed input controls all noise
```

Expose: `seed`, `scale`, `roughness`, `density`

## Building Generation

```
Footprint curve → Extrude floors → Window boolean pattern
    → Balcony probability → Roof type switch → Material ID
```

Output separate meshes per floor module for game kits.

## Road Systems

```
Centerline curve → Resample → Cross-section profile
    → Bridge blend at intersections → UV follow curve
```

## Pipe/Cable Networks

```
Node graph points → Connect minimum spanning → Curve segments
    → Profile sweep → Collision offset → Clamp size range
```

## Sci-Fi Panels

```
Grid subdivide → Random inset/extrude → Bevel
    → Panel index → Material variation
    → Bake to trim sheet layout
```

## Variation Testing

Test at parameter extremes:
- Minimum scale/density
- Maximum scale/density
- Seed 0, 42, 9999 (reproducibility check)

## Game Export Decision

| Approach | When |
|----------|------|
| Keep procedural in Blender only | Iteration phase |
| Realize single variant | Standard game prop |
| Bake multiple seeds as LOD variants | Background variety |
| Export node group to engine | Only if engine supports |

## MCP Integration

1. Build procedural systems via MCP
2. Set seed/density parameters via MCP
3. Realize geometry via MCP
4. Query output polycount per variation
5. Export realized meshes

## Constraints

### MUST DO
- Expose seed for reproducibility
- Test min/max parameter bounds
- Realize before game engine export
- Optimize after realize (asset-optimization)
- Document parameter ranges in production brief

### MUST NOT DO
- Export unrealsized geometry nodes to game without validation
- Infinite variation without performance testing
- Procedural where manual hero quality required
- Skip UV planning on procedural output
- Hardcode random without seed control

## Reference Guide

| Topic | Reference | Load When |
|-------|-----------|-----------|
| Geo nodes patterns | `../geometry-nodes/SKILL.md` | Node setup |
| Environment integration | `../environment-artist/SKILL.md` | Scene placement |

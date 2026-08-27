
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


## Appendix: building-generators

# Building Generators

## Parametric Inputs

| Input | Type | Example |
|-------|------|---------|
| floor_count | Integer | 3–20 |
| floor_height | Float | 3.0m |
| width | Float | 8.0m |
| depth | Float | 12.0m |
| window_rows | Integer | 2–4 |
| seed | Integer | Reproducible variation |

## Node Stack Pattern

```
Footprint (mesh plane) → Extrude Mesh (floors)
    → Set Position (window cuts via index selection)
    → Instance Window Module on selected faces
    → Set Material Index
    → Realize Instances (for export)
```

## Window Cut Pattern

```
Subdivide face grid → Delete random faces (seed-driven)
    → Inset remaining → Extrude inward
```

## Roof Variants

Switch node group input:
- `flat` — extrude top face
- `pitched` — edge split + rotate
- `parapet` — extrude low wall perimeter

## Output Structure

Separate objects per module for game kits:
- `SM_Env_Building_Wall_Module`
- `SM_Env_Building_Window_Module`
- `SM_Env_Building_Roof_Module`

## Performance

Realize and decimate before export. Cap floor_count for background buildings.

## Appendix: scatter-systems

# Scatter Systems

## Rock Scatter

```
Input: Cliff surface mesh
Density: 0.3–1.0 per m²
Scale: 0.5–2.0 (non-uniform 0.8–1.2)
Rotation: Random Z; align normal optional
Cull: Slope > 45° exclude
```

## Grass Scatter

```
Density: 5–20 per m² (adjust for target polycount)
Scale: 0.8–1.2
Only on upward-facing normals (Normal dot Z > 0.7)
```

## Debris Scatter

```
Clustered: Poisson disk minimum distance 0.3m
Seed-exposed for art iteration
Realize before export; cap instance count
```

## Performance Cap

Set maximum instance count input. Background: 500. Hero zone: 2000 max.

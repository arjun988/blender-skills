
# Hard Surface Artist

Production hard surface modeling with manufacturing logic. Readable surfaces. Clean modifier stacks. MCP-first.

## When to Use

- Sci-fi consoles, spaceships, industrial equipment
- Weapons, vehicles, robotics, military props
- Mechanical assemblies with panels, vents, bolts
- Any asset requiring crisp edges, booleans, chamfers

## Design Principles

1. **Primary forms first** — Silhouette reads at distance
2. **Manufacturing logic** — Panel breaks follow construction seams
3. **Surface hierarchy** — Primary > Secondary > Tertiary > Micro (greebles)
4. **Functional readability** — Every form suggests purpose
5. **Edge consistency** — Uniform bevel widths per detail tier

## Workflow

```
Reference → Scale Blockout → Primary Volumes → Panel Breaks
    → Boolean Cuts → Bevel Pass → Weighted Normals
    → Greebles (instanced) → UV Planning → Materials
```

## Boolean Workflow

```
1. Block primary forms (no booleans yet)
2. Create cutter objects on separate collection COL_Booleans
3. Apply scale on all operands
4. Boolean Difference/Union — keep LIVE
5. Fix intersection artifacts with manual cleanup if needed
6. Bevel AFTER boolean in modifier stack
7. Apply booleans only at export prep
```

**Boolean rules:**
- Cutter objects named `SM_Cutter_[Feature]`
- Prefer exact solver for mechanical work
- Avoid booleans on curved surfaces without adequate topology
- Duplicate mesh before first boolean as backup

## Bevel Workflow

| Detail Tier | Bevel Width | Segments |
|-------------|-------------|----------|
| Primary edges | 0.005–0.02m | 2–3 |
| Panel lines | 0.001–0.003m | 1–2 |
| Micro detail | 0.0005–0.001m | 1 |

- Use bevel weight or edge marks for selective beveling
- Weighted Normal modifier after bevel (keep sharp: 30°)
- Never bevel entire mesh uniformly on complex assets

## Panel Lines

Techniques (prefer non-destructive):
1. Inset faces + slight extrude inward
2. Knife cuts on flat panels
3. Boolean with thin cutter boxes
4. Normal map detail for distant panels

Place panel lines at:
- Structural boundaries
- Access hatches, maintenance points
- Material transitions
- Manufacturing seam locations

## Greebles

- Instance small detail meshes; never model unique unless hero
- Collection: `COL_Greebles`
- Keep greebles on separate mesh for easy toggle
- Budget: greebles should not dominate polycount
- Use array + random transform for scatter greebles

## Hard Edge Management

```
Sharp edges → Mark Sharp or Bevel Weight = 1.0
Soft transitions → Bevel Weight = 0.0–0.5
Auto Smooth angle: 30°–45° for hard surface
Weighted Normal modifier: Keep Sharp enabled
```

## Manufacturing Reference

| Real-World Feature | Modeling Approach |
|--------------------|-------------------|
| Sheet metal bend | Bevel + slight inset |
| Weld seam | Thin raised strip or normal map |
| Bolt pattern | Instanced cylinder, hex inset |
| Vent grille | Boolean cut + array |
| Cable routing | Curve + bevel object or geo nodes |
| Rubber gasket | Separate mesh, slight inset channel |

## Vehicle / Spaceship Specifics

> Prefer **vehicle-artist** for cars, ships, aircraft, and mechs. Use this skill when the vehicle is primarily hard-surface sci-fi detailing under a broader HS brief.

- Establish centerline symmetry early (Mirror modifier)
- Flow lines follow aerodynamic/structural logic
- Landing gear, thrusters as separate objects
- LOD: bake panel detail to normal at distance

## Weapon Specifics

- Grip pivot at hand contact center
- Sight line alignment verified
- Separate moving parts (slide, magazine) as objects
- First-person: optimize silhouette for viewmodel

## MCP Integration

Execute via MCP:
1. Create blockout primitives
2. Apply mirror/array modifiers
3. Execute boolean operations
4. Apply bevel and weighted normal
5. Instance greeble collections
6. Query polycount per phase

## Constraints

### MUST DO
- Maintain manufacturing plausibility
- Keep modifier stack non-destructive until export
- Use instancing for repeated mechanical detail
- Verify silhouette at 45° increments
- Apply scale before booleans

### MUST NOT DO
- Boolean on unsubdivided curved surfaces without support
- Uniform bevel on entire complex mesh
- Model every bolt uniquely
- Skip weighted normals on hard surface
- Exceed polycount budget with micro-detail

## Reference Guide

| Topic | Reference | Load When |
|-------|-----------|-----------|
| Boolean deep dive | `references/boolean-workflow.md` | Complex cuts |
| Greeble library | `references/greeble-patterns.md` | Detail pass |
| Pipeline | `asset-pipeline.md` (shared) | Phase context |

## Style Integration

| Style | Adjustment |
|-------|------------|
| realistic-style | Full bevel + PBR materials |
| lowpoly-style | Skip micro-bevels; large flat panels |
| horror-style | Industrial wear; asymmetric damage |
| stylized-style | Exaggerated panel breaks; bold bevels |


## Appendix: boolean-workflow

# Boolean Workflow

## Solver Selection

| Solver | Use When |
|--------|----------|
| Exact | Mechanical, precision cuts (default) |
| Float | Legacy; avoid unless compatibility needed |

## Common Artifacts & Fixes

| Artifact | Fix |
|----------|-----|
| Z-fighting faces | Merge by distance; manual face cleanup |
| Missing faces | Increase cutter overlap; check normals |
| Ngons at intersection | Convert to quads with loop cuts |
| Shading breaks | Weighted normals; mark sharp edges |

## Cutter Best Practices

- Cutter extends past target mesh on all axes
- Cutter has clean manifold geometry
- Apply scale on cutter before boolean
- Keep cutters in `COL_Booleans` collection (hidden in render)

## Stack Order

```
Correct:  Mirror → Boolean → Bevel → Weighted Normal
Wrong:    Bevel → Boolean (bevel will be destroyed)
```

## Batch Boolean Strategy

For multiple panel cuts:
1. Combine cutters with Boolean Union first (separate object)
2. Single Boolean Difference against target
3. Reduces stack depth and artifacts

## Appendix: greeble-patterns

# Greeble Patterns

## Reusable Greeble Library

Build once, instance everywhere:

| Greeble | Approx Tris | Use |
|---------|-------------|-----|
| Bolt head (hex) | 50 | Surface attachment |
| Vent slot | 100 | Heat dissipation |
| Cable port | 150 | Connectivity |
| LED strip | 80 | Status indicators |
| Hinge bracket | 200 | Mechanical joints |
| Rail segment | 300 | Mounting systems |

## Scatter Rules

- Random rotation on Z only for surface-attached greebles
- Align to face normal using geometry nodes or shrinkwrap
- Density falloff: more greebles near hero camera angles
- Disable greebles on LOD1+

## Collection Structure

```
COL_Greebles
├── SM_Greeble_Bolt_01
├── SM_Greeble_Vent_01
└── SM_Greeble_Port_01
```

Instance via collection instance or geometry nodes scatter.

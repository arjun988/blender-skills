---
name: sculpting
description: Blender sculpting for organic and hard surface detail using Dyntopo, multiresolution, brushes, alpha workflow, wrinkles, and damage. Use when high-frequency surface detail is needed before retopology in Blender via MCP.
license: MIT
metadata:
  author: https://github.com/arjun988
  version: "1.0.0"
  domain: blender
  role: specialist
  triggers: sculpt, dyntopo, multires, brush, wrinkle, damage, organic detail, surface detail, alpha
  related-skills: retopology, character-artist, creature-artist, blender-modeler
---

# Sculpting

High-frequency surface detail pass. Know when to sculpt vs model vs bake.

## When to Sculpt

| Sculpt | Don't Sculpt |
|--------|--------------|
| Organic wrinkles, pores | Hard surface panel lines |
| Creature skin detail | Modular kit pieces |
| Damage, wear, dents | Anything needing clean UVs directly |
| Character likeness refinement | Lowpoly style assets |
| Hero asset micro-detail | Background props |

## Workflow

```
Base Mesh → Multires or Dyntopo → Primary Forms → Secondary Detail
    → Tertiary/Micro → Bake Maps → Retopology (if game asset)
```

## Dyntopo vs Multiresolution

| Method | Use When | Avoid When |
|--------|----------|------------|
| Multires | Controlled detail levels; bake workflow | Need to preserve base topology exactly |
| Dyntopo | Freeform exploration; damage pass | Need predictable polycount |
| Voxel Remesh | Reset topology mid-sculpt | Fine detail already established |

**Default:** Multires for production; Dyntopo for exploration passes only.

## Brush Selection

| Brush | Purpose |
|-------|---------|
| Draw | General buildup |
| Clay Strips | Muscle/form definition |
| Crease | Wrinkles, folds, hard lines |
| Grab | Large form adjustments |
| Inflate/Deflate | Volume control |
| Scrape | Planar flattening (hard surface sculpt) |
| Dam Standard | Sharp damage, scratches |
| Layer | Non-destructive detail (if available) |

## Detail Pass Order

1. **Primary** — Major form corrections (Grab, Clay)
2. **Secondary** — Muscle, folds (Clay Strips, Crease)
3. **Tertiary** — Skin texture, scales (Draw, Alpha)
4. **Micro** — Pores, fine scratches (Alpha, Dam Standard)

## Alpha Workflow

- Use tileable alphas for skin, leather, rock
- Stamp at consistent scale for texel coherence
- Combine alphas with different brush strengths
- Bake alpha detail to normal map for game assets

## Hard Surface Sculpting

- Scrape brush for planar surfaces
- Crease for panel line softening
- Dam Standard for impact damage
- Trim brushes for precise cuts (if addon available)
- Always retopologize or rebake after hard surface sculpt

## Damage & Wear

| Damage Type | Technique |
|-------------|-----------|
| Scratches | Dam Standard, light strokes |
| Dents | Inflate negative + smooth |
| Chipped edges | Scrape + Crease |
| Rust bubbles | Small Draw buildup |
| Fabric wear | Crease along stress points |

## Performance

- Hide unrelated objects during sculpt
- Use matcap for fast feedback
- Subdivide only active area (face, hands)
- Bake and reduce multires for viewport performance

## MCP Integration

1. Duplicate base mesh to sculpt collection via MCP
2. Add multires modifier via MCP
3. Query polycount at each subdivision level
4. Export high-poly for bake handoff
5. Keep sculpt mesh separate from game mesh

## Handoff to Retopology

Before retopo handoff provide:
- Final sculpt at highest multires level
- Decimated version for retopo reference
- List of deformation zones requiring clean loops
- Baked maps if bake-before-retopo workflow

## Constraints

### MUST DO
- Start from clean base mesh with good topology
- Work largest to smallest detail
- Duplicate before sculpt destructive changes
- Bake detail for game assets
- Match detail level to camera distance

### MUST NOT DO
- Sculpt lowpoly-style assets
- Skip retopology for animated game characters
- Subdivide entire mesh to level 6+ uniformly
- Leave dyntopo mesh as final game asset
- Sculpt without reference

## Reference Guide

| Topic | Reference | Load When |
|-------|-----------|-----------|
| Brush settings | `references/brush-guide.md` | Detail pass |
| Bake workflow | `../texture-workflow/SKILL.md` | Game asset handoff |

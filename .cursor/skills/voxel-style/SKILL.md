---
name: voxel-style
description: Voxel and Minecraft-adjacent art direction for Blender with block grid modeling, limited palettes, and chunk-friendly assets.
license: MIT
metadata:
  author: https://github.com/arjun988
  version: "1.0.0"
  domain: blender
  role: specialist
  triggers: voxel, Minecraft, blocky, cube world, pixel voxel, grid block, chunk
  related-skills: lowpoly-style, environment-artist, materials, geometry-nodes
---

# Voxel Style

Block grid language. Limited palette. Chunk-friendly forms.

## When to Use

- Minecraft-adjacent / voxel game assets
- Blockout aesthetic as final style
- Grid-snapped props and characters

## Core Tenets

1. **Grid snap** — Occupancy on explicit voxel size (e.g. 0.1 / 1.0m)
2. **No diagonal organic bevels** — Cubes and stepped forms
3. **Palette atlas** — Few colors; readable blocks
4. **Silhouette via steps** — Not smooth curves
5. **Chunk modularity** — Pieces fit tile sizes

## Workflow

```
Choose voxel size → Block occupancy → Merge cubes
  → Palette materials → Optional GN instance → Export
```

## Modeling Tips

- Start from cubes; boolean union / merge by distance
- Characters: stepped limbs, clear head block
- Avoid subdivision surface (breaks voxel language)
- Remesh to blocks only if converting from smooth

## Materials

- Flat colors or nearest-neighbor textures
- Atlas preferred
- Emission for glow blocks sparingly

## Vs lowpoly-style

- `lowpoly-style` allows irregular low tris / PS1 vibes
- `voxel-style` enforces grid occupancy aesthetic

## Constraints

### MUST DO
- Declare voxel size in brief
- Snap consistently
- Keep palette small

### MUST NOT DO
- Smooth shading that hides block edges (unless intentional glass)
- Organic sculpt detail


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

## Reference Guide

| Topic | Reference | Load When |
|-------|-----------|----------|
| Voxel Grid | `references/voxel-grid.md` | When needed |
| Voxel Characters | `references/voxel-characters.md` | When needed |


### Appendix: voxel-characters

# Voxel Characters

- Head block readable
- Limb thickness ≥ 1 voxel
- Silhouette from 4 orthos
- Avoid diagonal “smooth” cheating

### Appendix: voxel-grid

# Voxel Grid Spec

Declare size in brief (e.g. 0.1m or 1.0m).
Snap all occupancy. No smooth organic bevels.
Palette ≤ 16–32 colors for readable sets.

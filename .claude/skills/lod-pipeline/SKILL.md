---
name: lod-pipeline
description: Dedicated LOD generation, naming, screen-size targets, and validation for game meshes in Blender via MCP.
license: MIT
metadata:
  author: https://github.com/arjun988
  version: "1.0.0"
  domain: blender
  role: specialist
  triggers: LOD, LODs, level of detail, decimate, LOD0, LOD1, impostor, screen size
  related-skills: asset-optimization, export-pipeline, unity-export, unreal-export, collision-proxy
---

# LOD Pipeline

Intentional LOD chains. Preserve silhouette. Validate reductions.

## When to Use

- Game assets needing LOD0–N
- Batch LOD for modular kits
- Before Unity/Unreal/Godot export

## Workflow

```
Approve LOD0 → Generate LOD1..N → Fix silhouette breaks
  → Naming → Screen-size table → Export verify
```

## Typical Budgets (guide)

| LOD | Tris vs LOD0 | Keep |
|-----|--------------|------|
| LOD0 | 100% | Full detail |
| LOD1 | 40–60% | Major forms |
| LOD2 | 15–30% | Silhouette |
| LOD3 | 5–10% | Blob / impostor candidate |

Tune per asset importance and camera.

## Generation Methods

1. **Decimate (planar/collapse)** — fast props
2. **Manual retopo low** — hero characters/vehicles
3. **Delete interiors / small parts** — vehicles, buildings
4. **Bake normals from LOD0 → low** — when detail must move to texture

## Naming

```
SM_Asset_LOD0
SM_Asset_LOD1
SM_Asset_LOD2
```

Collection: `COL_LODs_[Asset]`

## Validation Checklist

- [ ] Silhouette matches at intended distance
- [ ] No major holes / inverted normals
- [ ] UVs still valid (or rebaked)
- [ ] Materials slots consistent across LODs
- [ ] Vertex colors/UVs needed by shader preserved
- [ ] LOD transitions planned (screen size %)

## Screen Size Starters

| LOD | Screen size (UE-like guide) |
|-----|-----------------------------|
| LOD0 | 1.0 – 0.5 |
| LOD1 | 0.5 – 0.25 |
| LOD2 | 0.25 – 0.1 |
| LOD3 | 0.1 – 0.0 |

## Constraints

### MUST DO
- Protect silhouette before poly reduction
- Keep LOD0 as source of truth
- Document budgets in production brief

### MUST NOT DO
- Blind decimate until unrecognizable
- Different material slot counts across LODs without reason

## Reference Guide

| Topic | Reference | Load When |
|-------|-----------|----------|
| Lod Budgets | `references/lod-budgets.md` | When needed |
| Lod Validation | `references/lod-validation.md` | When needed |

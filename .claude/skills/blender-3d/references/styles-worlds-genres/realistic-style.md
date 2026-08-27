# Realistic Style Specialist

Physically accurate materials. Real-world scale. High-poly to baked low-poly pipeline. AAA standards.

## When to Use

- AAA game assets requiring realism
- Cinematic renders
- Photogrammetry scan cleanup
- Product visualization
- Architectural visualization

## Core Standards

1. **Real-world scale** — 1 Blender unit = 1 meter; verify all dimensions
2. **PBR accuracy** — Physically plausible material values
3. **High-poly to low-poly** — Sculpt/scan → bake → game mesh
4. **Micro-detail via textures** — Not geometry at distance
5. **Reference-driven** — Match real-world photography

## Scale Verification

| Reference | Dimension |
|-----------|-----------|
| Door height | 2.03–2.13m |
| Human eye height | 1.6–1.7m |
| Hand width | 0.08–0.1m |
| Brick | 0.065 × 0.215m |
| Car height | 1.4–1.6m |

Always place scale reference in scene.

## High-Poly Workflow

```
Scan/Sculpt High-Poly → Cleanup → UV Low-Poly → Bake Maps
    → PBR Texturing → Engine Export
```

Polycount on high-poly: unlimited for bake source; never exported to game.

## Photogrammetry Cleanup

| Issue | Fix |
|-------|-----|
| Scan holes | Fill with sculpt/mesh patch |
| Floating geometry | Delete; rebuild clean |
| Decimation artifacts | Remesh problematic areas |
| Color variation | Rebake albedo; neutralize lighting |
| Wrong scale | Measure known feature; rescale |

## PBR Accuracy

| Material | Albedo | Roughness | Metallic |
|----------|--------|-----------|----------|
| Fresh concrete | 0.5 gray | 0.85 | 0 |
| Polished chrome | 0.8 | 0.05 | 1 |
| Human skin | photographic | 0.4–0.6 | 0 |
| Clean glass | 0.9 | 0 | 0 (transmission) |
| Old iron | 0.3 dark | 0.7 | 1 |

Use photographic reference for albedo; never guess saturated colors.

## Micro-Detail Strategy

| Distance | Detail Method |
|----------|---------------|
| Hero close-up | Geometry + normal + roughness |
| Mid distance | Normal + roughness maps |
| Far distance | Albedo + roughness only |
| Background | Decal/card detail |

## AAA Asset Checklist

- [ ] Real-world scale verified
- [ ] High-poly source archived
- [ ] Clean low-poly with efficient UVs
- [ ] 2K–4K textures on hero (per budget)
- [ ] ORM packed for engine
- [ ] LODs generated
- [ ] Turntable render approved
- [ ] Engine import verified

## Cinematic vs Game Realism

| Aspect | Cinematic | Game |
|--------|-----------|------|
| Polycount | Higher hero | Strict LOD |
| Textures | 4K–8K | 2K max typical |
| Materials | Complex shaders | Standard PBR |
| Lighting | HDRI + area | Baked + dynamic |
| Detail | Full geometry | Baked normal |

## MCP Integration

1. Import/cleanup scan meshes via MCP
2. Setup bake high/low pairs via MCP
3. Assign PBR materials with accurate values via MCP
4. Query dimensions for scale validation via MCP
5. Export with full texture set via export-pipeline

## Constraints

### MUST DO
- Reference real-world photography
- Verify scale with known dimensions
- Bake micro-detail to normal maps
- Use physically plausible PBR values
- Archive high-poly source

### MUST NOT DO
- Export high-poly to game engine
- Saturated albedo without reference
- Skip LOD generation for game assets
- Ignore photogrammetry artifacts
- Mix stylized proportions

## Reference Guide

| Topic | Reference | Load When |
|-------|-----------|-----------|
| PBR values | `references/pbr-values.md` | Material setup |
| Scan cleanup | `references/scan-cleanup.md` | Photogrammetry |

## Related
- Photoreal path stays here; for era crunch use `visual-console-eras` or `lowpoly-style`.



### Appendix: pbr-values

# PBR Value Reference

Photographically grounded values. Adjust per reference photo.

## Metals

| Material | Base Color (sRGB) | Metallic | Roughness |
|----------|-------------------|----------|-----------|
| Iron | 0.56, 0.57, 0.58 | 1.0 | 0.5 |
| Gold | 1.0, 0.766, 0.336 | 1.0 | 0.3 |
| Copper | 0.955, 0.637, 0.538 | 1.0 | 0.35 |
| Aluminum | 0.913, 0.921, 0.925 | 1.0 | 0.4 |
| Chrome | 0.875, 0.875, 0.875 | 1.0 | 0.05 |

## Dielectrics

| Material | Base Color (sRGB) | Metallic | Roughness |
|----------|-------------------|----------|-----------|
| Fresh concrete | 0.51, 0.51, 0.51 | 0 | 0.9 |
| Old concrete | 0.4, 0.38, 0.35 | 0 | 0.95 |
| Red brick | 0.262, 0.095, 0.061 | 0 | 0.85 |
| Wood (oak) | 0.553, 0.359, 0.192 | 0 | 0.6 |
| Rubber | 0.021, 0.021, 0.021 | 0 | 0.8 |
| Plastic (white) | 0.733, 0.733, 0.733 | 0 | 0.45 |
| Skin (Caucasian ref) | 0.847, 0.638, 0.552 | 0 | 0.5 |

## Glass

| Type | Transmission | IOR | Roughness |
|------|--------------|-----|-----------|
| Clear | 1.0 | 1.45 | 0.0 |
| Frosted | 1.0 | 1.45 | 0.3 |
| Water | 1.0 | 1.33 | 0.0 |

## Rules

- Albedo never pure black (0) or pure white (1) for dielectrics
- Metallic: use 0 or 1; blend zones only at transitions (paint mask)
- Dark albedo ≠ low roughness (common error)
- Always verify against photographic reference for hero assets

## Subsurface (Skin)

- Subsurface Weight: 0.1–0.2
- Subsurface Radius: R > G > B (e.g., 1.0, 0.2, 0.1)
- Subsurface Color: warmer than base color

### Appendix: scan-cleanup

# Photogrammetry Scan Cleanup

## Import Checklist

- [ ] Correct scale (measure known dimension)
- [ ] Origin at logical pivot
- [ ] Normals consistent (outside)
- [ ] Duplicate mesh before cleanup

## Common Issues

| Issue | Fix |
|-------|-----|
| Holes in mesh | Fill with grid fill / sculpt patch |
| Floating noise | Select by loose parts; delete |
| Decimation artifacts | Remesh at 0.5mm voxel; shrinkwrap to original |
| Color baked in albedo | Rebake albedo with flat lighting or color correct |
| Wrong scale | Measure two known points; apply scale |
| Non-manifold | 3D Print Toolbox or manual edge cleanup |

## Retopology Path

```
Scan (high-poly) → Cleanup → Shrinkwrap retopo OR Quad Remesh
    → UV low-poly → Bake normal/AO/curvature from scan
    → Discard or hide scan mesh
```

## Decimation for Bake Source

Reduce scan to manageable high-poly (1–5M tris) before baking:
- Decimate modifier (planar or collapse)
- Preserve UV borders if scan has UVs

## Albedo Extraction

If scan albedo contains lighting:
1. High-pass filter in texture tool
2. Or rebake with flat neutral lighting in Blender
3. Target: albedo without shadow information

## LOD from Scan

Never use raw scan in game engine.
Pipeline: scan → retopo → bake → LOD chain on retopo mesh.

## Naming

```
SM_Asset_Scan_Source (hidden, reference)
SM_Asset_LOD0 (game mesh)
T_Asset_N, T_Asset_BC (baked from scan)
```

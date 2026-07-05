---
name: realistic-style
description: Photorealistic AAA art direction for Blender including photogrammetry cleanup, real-world scale, high-poly workflows, PBR accuracy, and scan optimization. Use for cinematic and AAA game realism.
license: MIT
metadata:
  author: blender-skills
  version: "1.0.0"
  domain: blender
  role: specialist
  triggers: realistic, photoreal, AAA, photogrammetry, scan cleanup, PBR accurate, high poly, cinematic
  related-skills: texture-workflow, materials, rendering, hard-surface
---

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

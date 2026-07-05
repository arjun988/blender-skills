---
name: materials
description: Blender PBR and stylized material creation for metal, wood, concrete, fabric, glass, dirt, rust, and procedural shaders. Use for look development, material reuse, and production shading in Blender via MCP.
license: MIT
metadata:
  author: blender-skills
  version: "1.0.0"
  domain: blender
  role: specialist
  triggers: material, shader, PBR, procedural, metal, wood, fabric, glass, rust, moss, Principled BSDF
  related-skills: texture-workflow, rendering, stylized-style, realistic-style
---

# Materials

Production shading with material reuse. PBR-accurate or intentionally stylized. Minimal unique materials.

## When to Use

- Look development after UVs
- Procedural material creation
- Master material library setup
- Material variation from shared masters
- Engine export material preparation

## Workflow

```
Master Materials → Instance Variations → Object Assignment
    → Vertex Color/Mask Setup → Validation → Export Prep
```

## Master Material Library

Create reusable masters in `MAT_` prefix:

| Master | Base Setup |
|--------|------------|
| MAT_Metal_Base | Principled: Metallic 1, adjustable Roughness |
| MAT_Plastic_Base | Principled: Metallic 0, Specular 0.5 |
| MAT_Fabric_Base | Principled + Sheen |
| MAT_Glass_Base | Principled: Transmission 1, IOR 1.45 |
| MAT_Emissive_Base | Principled: Emission strength variable |
| MAT_Organic_Base | Subsurface scattering enabled |

Instance variations: duplicate master, adjust parameters only.

## PBR Value Ranges

| Material | Metallic | Roughness | Notes |
|----------|----------|-----------|-------|
| Polished metal | 1.0 | 0.1–0.3 | |
| Brushed metal | 1.0 | 0.4–0.6 | Anisotropic if available |
| Painted metal | 0.0 | 0.3–0.5 | Base color = paint |
| Plastic | 0.0 | 0.3–0.6 | |
| Rubber | 0.0 | 0.7–0.9 | |
| Concrete | 0.0 | 0.8–0.95 | |
| Wood (raw) | 0.0 | 0.5–0.7 | |
| Glass | 0.0 | 0.0 | Transmission 1 |
| Skin | 0.0 | 0.4–0.6 | Subsurface 0.1–0.3 |
| Fabric | 0.0 | 0.7–0.9 | Sheen |

## Procedural Material Patterns

**Wear mask:** Noise → ColorRamp → Lerp between clean/worn
**Edge wear:** Bevel node → Pointiness or Ambient Occlusion
**Dirt accumulation:** AO inverted → multiply with dirt color
**Rust:** Noise mask on metal → orange/brown color override

## Material Count Budget

| Asset Type | Max Materials |
|------------|---------------|
| Hero prop | 3–5 |
| Standard prop | 1–2 |
| Modular piece | 1 (atlas) |
| Character | 3–8 (body, cloth, eyes, hair) |
| Environment module | 1–2 |

## Vertex Color Usage

- RGB: variation masks (wear, moss, color variation)
- R: wear amount, G: dirt, B: wetness
- Document channel usage in material notes

## Stylized Materials

See stylized-style skill. Key differences:
- Flatten roughness range
- Hand-painted base color priority
- Rim light via Fresnel mix
- NPR toon shaders if project requires

## MCP Integration

1. Create material slots via MCP
2. Assign materials to objects via MCP
3. Set principled BSDF parameters via MCP
4. Query material count per scene
5. Verify material names follow convention

## Constraints

### MUST DO
- Reuse master materials; instance variations
- Name materials `MAT_[Surface]_[Descriptor]`
- Match PBR values to style skill direction
- Limit material count per asset budget
- Test materials in target lighting setup

### MUST NOT DO
- Unique material per object (unless hero)
- PBR values outside physically plausible range (realistic style)
- Skip vertex color masks for variation
- Leave default material names
- Finalize materials before UVs complete

## Reference Guide

| Topic | Reference | Load When |
|-------|-----------|-----------|
| Surface recipes | `references/surface-recipes.md` | Specific materials |
| Procedural nodes | `references/procedural-patterns.md` | Wear, dirt, variation |


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


## Appendix: procedural-patterns

# Procedural Material Patterns

## Edge Wear

```
Geometry: Pointiness or Bevel → ColorRamp → Mix with base color/roughness
Mask: Fresnel (high IOR) for edge-only wear
```

## Dirt Accumulation

```
AO (inverted) → Multiply with dirt brown
Combine with cavity mask from curvature
Apply to roughness increase, not albedo darkening alone
```

## Rust Overlay

```
Noise (scale 5–20) → ColorRamp threshold
Mix rust orange-brown over metal base
Increase roughness in rust areas
Metallic: 0 in rust zones
```

## Moss/Growth

```
AO + upward normal (Z+) → Moss green overlay
Roughness increase in moss areas
Subtle subsurface on moss if stylized-realistic
```

## Water Staining

```
Vertical gradient + noise → Darken albedo
Increase roughness slightly
Place on concrete, plaster, ceiling corners
```

## Panel Color Variation

```
Object Info (Random per object) → Hue Saturation Value
Subtle: ±5% hue, ±10% value
```

## Master Graph Pattern

Keep wear/dirt as reusable node groups plugged into master `MAT_*_Base` materials.

## Appendix: surface-recipes

# Surface Material Recipes

Quick Principled BSDF starting points. Adjust per reference.

## Painted Metal (Worn)

- Base Color: reference photo
- Metallic: 0
- Roughness: 0.5–0.7
- Procedural: edge wear mask on roughness

## Concrete (Weathered)

- Base Color: desaturated gray 0.4–0.5
- Roughness: 0.85–0.95
- Bump: subtle noise

## Wood (Oiled)

- Base Color: warm brown
- Roughness: 0.4–0.6
- Anisotropic rotation along grain if available

## Fabric (Cotton)

- Roughness: 0.8
- Sheen: 0.3
- Subsurface: 0.05 (optional)

## Glass (Standard)

- Transmission: 1
- IOR: 1.45
- Roughness: 0.02–0.1

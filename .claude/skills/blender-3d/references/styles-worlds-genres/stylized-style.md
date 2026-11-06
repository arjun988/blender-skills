# Stylized Style Specialist

Deliberate shape language. Exaggerated proportions. Color harmony. NPR rendering.

## When to Use

- Non-photorealistic games
- Hand-painted texture workflows
- Animated/stylized characters
- Fantasy environments with art direction
- Toon/cel-shaded rendering

## Core Principles

1. **Shape language** — Circles=friendly, squares=stable, triangles=danger
2. **Exaggeration** — Push proportions beyond realistic
3. **Color harmony** — Limited palette; intentional accent colors
4. **Silhouette clarity** — Strong readable shapes
5. **Detail in texture** — Not micro-geometry

## Shape Language

| Shape | Association | Use |
|-------|-------------|-----|
| Circle/Oval | Friendly, approachable | Heroes, cute creatures |
| Square/Rectangle | Stable, reliable | Architecture, guards |
| Triangle | Dynamic, dangerous | Villains, spikes, roofs |

Combine shapes consistently per character/faction.

## Proportion Exaggeration

| Feature | Stylized Approach |
|---------|-------------------|
| Head | 25–40% of height (chibi to semi-realistic) |
| Hands | Larger for expressiveness |
| Eyes | Enlarged for emotion |
| Limbs | Tapered; simplified joints |
| Weapons | Oversized for readability |

## Color Harmony

**Triadic:** Three equidistant hues — vibrant, balanced
**Complementary:** Opposite hues — high contrast accents
**Analogous:** Adjacent hues — harmonious environments

Rules:
- Limit palette to 3–5 core colors + neutrals
- Reserve saturated accents for interactive elements
- Desaturate backgrounds; saturate foreground subjects

## Material Approach

- Hand-painted albedo priority over PBR accuracy
- Flat or stepped roughness (not continuous PBR)
- Rim lighting built into texture (not just shader)
- Subsurface on skin: exaggerated warm tones
- No photoreal micro-detail

## NPR Rendering

Coordinate with rendering skill:
- Toon BSDF or Shader to RGB setups
- Stepped lighting (2–3 bands)
- Outline pass: inverted hull or Freestyle
- Bloom on emissive accents
- Flat ambient forbidden — maintain form readability

## Hand-Painted Texture Workflow

```
1. Flat base color blocks
2. Define light/shadow shapes (not gradients from bake)
3. Edge highlights (warm) and shadows (cool)
4. Detail pass: minimal; suggestive not literal
5. Ambient occlusion painted, not baked
```

## Character Stylization

- Simplified anatomy; avoid uncanny valley
- Hair as solid shapes or card clusters
- Clothing folds: painted, not simulated
- Facial features: large eyes, small nose (style dependent)

## Environment Stylization

- Exaggerated verticality in forests/mountains
- Architecture: oversized elements (doors, windows)
- Vegetation: puff/cloud shapes (not botanical accuracy)
- Water: stylized foam patterns

## MCP Integration

1. Block exaggerated proportions via MCP
2. Assign stylized materials via MCP
3. Configure NPR render settings via MCP
4. Validate silhouette with flat shading via MCP
5. Limit geometry detail per stylized budgets

## Constraints

### MUST DO
- Define shape language per asset/faction
- Maintain color palette consistency
- Exaggerate intentionally, not accidentally
- Paint detail in textures
- Test NPR render early

### MUST NOT DO
- Mix photoreal PBR with stylized shapes without intent
- Micro-detail geometry (use texture)
- Realistic proportions unless semi-stylized target
- Full PBR roughness accuracy
- Skip outline/rim if NPR project requires

## Reference Guide

| Topic | Reference | Load When |
|-------|-----------|-----------|
| NPR shader setup | `references/npr-shaders.md` | Rendering setup |
| Color palettes | `references/palette-examples.md` | Art direction |

## Related Style Packs
- `cartoon-style`, `anime-style`, `comic-book-style`, `manga-style`, `hand-painted-style`, `painterly-style`
- `chibi-style`, `pixel-art-style`, `hd-2d-style`, `stop-motion-craft-style`



### Appendix: npr-shaders

# NPR Shader Setups

## Cel Shader (Eevee/Cycles)

```
[Layer Weight or Fresnel] → [ColorRamp 3 stops] → [Mix with Base Color] → Output
Stops: Shadow (dark), Mid, Highlight (bright)
```

## Toon BSDF (If Available)

Direct toon shading with size parameter for light band width.

## Outline Pass

**Inverted Hull:**
```
Solidify: -0.02m
Flip Normals
Material: Emission black, backface culling off
```

Render as separate pass; composite over beauty.

## Rim Light Node

```
Fresnel (1.5) → Multiply → Add to Emission
Color: warm (#FFAA66) for heroes, cool for villains
```

## Specular Control

Reduce specular to 0–0.2 for flat stylized look.
Or use hard ColorRamp on specular output.

## Shadow Hardness

Sun size: 0° (hard shadow) for toon.
Area light size: small for sharp terminator.

## Stylized Skin

```
Base color (warm)
+ Subsurface (high radius, low weight)
+ Painted blush in vertex colors
+ Hard shadow terminator (ColorRamp on Lambert)
```

## Export to Game Engine

Bake NPR result to texture set if target engine lacks toon shaders.
Or export shader graph documentation for engine recreation.

### Appendix: palette-examples

# Palette Examples

## Heroic Fantasy (Triadic)

| Role | Color | Hex |
|------|-------|-----|
| Primary | Royal Blue | #2E5090 |
| Secondary | Gold | #D4A843 |
| Accent | Crimson | #8B2030 |
| Neutral | Warm Gray | #6B6560 |

## Cozy Stylized (Analogous)

| Role | Color | Hex |
|------|-------|-----|
| Primary | Sage Green | #7A9E7E |
| Secondary | Cream | #F0E6D3 |
| Accent | Terracotta | #C4724E |
| Shadow | Deep Green | #3D5A40 |

## Sci-Fi (Complementary)

| Role | Color | Hex |
|------|-------|-----|
| Primary | Cool Gray | #8899AA |
| Secondary | Orange Accent | #E87830 |
| Emissive | Cyan | #00DDFF |
| Background | Dark Blue-Gray | #1A2233 |

## Horror (Desaturated + Accent)

| Role | Color | Hex |
|------|-------|-----|
| Base | Gray-Green | #5A6058 |
| Shadow | Near Black | #0A0C0A |
| Accent (blood) | Dried Red | #4A1515 |
| Light | Sick Yellow-Green | #B8C4A0 |

## Usage Rules

- 70% neutral/dominant
- 20% secondary
- 10% accent (interactive elements, threats)
- Background desaturated vs foreground saturated

---
name: lighting
description: Cinematic and game lighting in Blender including three-point lighting, HDRI, horror lighting, volumetrics, rim lighting, and mood-driven illumination. Use for look development and scene atmosphere via MCP.
license: MIT
metadata:
  author: blender-skills
  version: "1.0.0"
  domain: blender
  role: specialist
  triggers: lighting, light, HDRI, three point, rim light, volumetric, fog, mood, cinematic, horror lighting
  related-skills: rendering, horror-style, environment-artist
---

# Lighting Artist

Mood-driven illumination. Guide player attention. Support art direction.

## When to Use

- Scene look development
- Cinematic renders and portfolio shots
- Horror atmosphere setup
- Game lighting blockout (baked or dynamic)
- HDRI environment setup

## Workflow

```
Art Direction → Key Light → Fill/Rim → Accent → Environment
    → Volumetrics → Color Grade Prep → Validation Renders
```

## Three-Point Lighting

| Light | Purpose | Typical Setup |
|-------|---------|---------------|
| Key | Primary illumination | 45° above, 30° side |
| Fill | Shadow softening | Opposite key, 1/2–1/4 intensity |
| Rim | Subject separation | Behind subject, bright edge |

Naming: `LGT_Key_Main`, `LGT_Fill_Soft`, `LGT_Rim_Back`

## Light Types

| Type | Use Case |
|------|----------|
| Sun | Outdoor directional |
| Area | Soft studio, windows |
| Spot | Flashlights, stage, horror |
| Point | Bulbs, emissive fill |

## Color Temperature

| Mood | Kelvin | RGB Approx |
|------|--------|------------|
| Candle/warm | 1800K | Orange |
| Tungsten | 3200K | Warm white |
| Daylight | 5500K | Neutral white |
| Overcast | 6500K | Cool white |
| Moonlight | 8000K+ | Blue |

Horror: mix warm interior tungsten with cold exterior moonlight.

## HDRI Workflow

```
1. Select HDRI matching mood (overcast for horror, clear for hero)
2. Rotate to place brightest area as key
3. Adjust strength (0.5–2.0 typical)
4. Supplement with area lights for subject separation
5. Hide HDRI in background if using solid color/fog
```

## Horror Lighting

See horror-style skill. Key techniques:
- High contrast; deep shadows
- Single source motivation (one visible lamp)
- Flicker via noise modifier on strength
- Volumetric fog for light shafts
- Avoid flat even illumination

## Volumetrics

```
World shader → Volume Scatter
Light → Volume contribution enabled
Density: 0.01–0.1 (subtle to heavy fog)
Anisotropy: 0.3–0.8 for visible light shafts
```

## Game vs Cinematic

| Aspect | Game | Cinematic |
|--------|------|-----------|
| Light count | Minimal (performance) | Unlimited |
| Baked | Lightmaps common | Path trace |
| Dynamic | Real-time shadows | Ray traced |
| Mood | Gameplay readability | Artistic freedom |

## MCP Integration

1. Create lights with naming convention via MCP
2. Set color, intensity, angle via MCP
3. Configure world HDRI via MCP
4. Query light count and types
5. Organize in `COL_Lights` collection

## Constraints

### MUST DO
- Motivate every light source (visible fixture or logical source)
- Name lights `LGT_[Role]_[Descriptor]`
- Test readability of gameplay-critical areas
- Match lighting to style skill (horror, realistic, etc.)
- Separate lighting collections from geometry

### MUST NOT DO
- Flat ambient without direction
- Over-light horror scenes
- Ignore color temperature consistency
- Place lights without purpose
- Skip volumetric consideration for mood scenes

## Reference Guide

| Topic | Reference | Load When |
|-------|-----------|-----------|
| Horror setups | `references/horror-lighting-setups.md` | Horror scenes |
| Cinematic rigs | `references/cinematic-light-rigs.md` | Portfolio renders |

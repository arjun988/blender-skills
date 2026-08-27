
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


## Appendix: cinematic-light-rigs

# Cinematic Light Rigs

## Three-Point Studio

```
LGT_Key: Area 1m², 45° elevation, 30° azimuth, 5500K, strength 500W
LGT_Fill: Area 2m², opposite side, 5500K, strength 150W (30% key)
LGT_Rim: Spot, behind subject 135°, 3200K warm, strength 300W
```

## Product Hero Shot

```
LGT_Key: Large area softbox simulation (2m²)
LGT_Rim: Two spots L/R behind for edge definition
Backdrop: Gradient world or seamless curve
Camera: 85mm, f/2.8 DOF on hero detail
```

## Environment Golden Hour

```
Sun: 3000K, angle 5° above horizon
Fill: Sky HDRI warm, strength 0.3
Volumetrics: Light density 0.01 for atmospheric haze
```

## Turntable Asset Preview

```
LGT_Key: Area, fixed relative to camera (parent to camera)
LGT_Fill: World HDRI studio neutral
LGT_Rim: Behind asset, subtle
Camera: Orbit empty 360° / 120 frames
Background: Mid-gray for PBR accuracy
```

## Render Settings Pairing

Cycles 256+ samples, Denoise ON, AgX view transform, Medium Contrast look.

## Appendix: horror-lighting-setups

# Horror Lighting Setups

## Fluorescent Corridor

```
LGT_Key: Area light, 6500K, strength 50W, size 1.2m × 0.1m (tube shape)
Position: Ceiling, every 3m
Flicker: Noise modifier on strength, random per fixture
Fill: None or 5% ambient only
Volumetrics: Density 0.03
```

## Single Bare Bulb Room

```
LGT_Key: Point light, 2800K, strength 100W
Position: Ceiling center, visible bulb mesh with emission
Fill: None
Shadows: Hard, high contrast
```

## TV Glow (Analog Horror)

```
LGT_Key: Area light, 5000K green tint, strength 20W
Position: Low, facing into room from TV mesh
Emission: MAT_Emissive_Screen on TV face
Room: Otherwise dark
```

## Emergency Exit

```
LGT_Accent: Spot, green, strength 30W, narrow angle
Position: Above exit sign mesh
Purpose: False safety before threat reveal
```

## Moonlight Through Window

```
World HDRI: Night, low strength 0.1
LGT_Rim: Area, 8000K, strength 20W through window opening
Interior: Near black except rim highlights
```

## Flicker Animation

```
Driver or noise on light energy:
Base: 1.0
Noise: scale 0.5, offset random per light
Amplitude: ±30% strength variation
```

Only flicker 1–2 lights — not all simultaneously.

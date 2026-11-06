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

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

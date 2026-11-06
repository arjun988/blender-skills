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

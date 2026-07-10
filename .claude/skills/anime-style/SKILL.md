---
name: anime-style
description: Anime and cel-shaded art direction for Blender with hard color breaks, toon shaders, clean silhouettes, and anime proportion language.
license: MIT
metadata:
  author: https://github.com/arjun988
  version: "1.0.0"
  domain: blender
  role: specialist
  triggers: anime, cel shade, toon shader, anime style, hard shadows, manga, Japanese animation look
  related-skills: stylized-style, materials, rendering, character-artist, compositing
---

# Anime Style

Hard color breaks. Clean silhouettes. Cel shading. Anime proportion language.

## When to Use

- Anime / cel-shaded characters and props
- Toon shader lookdev
- Hard shadow graphic looks (not soft PBR)

## Core Tenets

1. **Flat tonal regions** — 2–4 value steps max per material
2. **Hard shadow terminators** — Specular as graphic shapes
3. **Line / silhouette clarity** — Optional freestyle or inverted hull
4. **Proportion language** — Eyes, hair masses, simplified anatomy
5. **Palette discipline** — Limited hues; accent sparingly

## Shading Approach

| Method | Use |
|--------|-----|
| Shader Toon / ColorRamp on diffuse | Fast Eevee/Cycles toon |
| Emission + ramp | Graphic unlit regions |
| Freestyle / grease pencil lines | Contours |
| Solidify inverted hull | Thick outlines |

## Modeling Notes

- Simplify secondary forms; hair as masses
- Creases where color breaks need support
- Avoid noisy micro detail fighting flat shading

## Lighting

- Single clear key for graphic shadows
- Rim optional for separation
- Avoid heavy soft GI wash unless intentional

## Vs stylized-style

- `stylized-style` = broad NPR / hand-painted
- `anime-style` = cel breaks, anime proportions, toon stack

## Constraints

### MUST DO
- Limit value steps
- Keep silhouette iconic
- Test with toon lighting early

### MUST NOT DO
- Full PBR roughness noise as primary look
- Over-subsurface that melts cel breaks

## Reference Guide

| Topic | Reference | Load When |
|-------|-----------|----------|
| Cel Shader Setup | `references/cel-shader-setup.md` | When needed |
| Anime Proportion | `references/anime-proportion.md` | When needed |

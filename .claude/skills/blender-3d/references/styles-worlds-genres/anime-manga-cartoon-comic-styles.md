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


### Appendix: anime-proportion

# Anime Proportion Notes

| Feature | Typical push |
|---------|--------------|
| Eyes | Larger, simplified lids |
| Nose/mouth | Minimal |
| Hair | Masses, not strands |
| Hands | Stylized, readable |
| Body | Genre-dependent (shonen vs moe vs seinen) |

### Appendix: cel-shader-setup

# Cel Shader Setup

- Diffuse → ColorRamp (constant) 2–4 stops
- Specular as hard graphic shape or none
- Optional rim as flat band
- Outline: Freestyle / inverted hull / Grease Pencil

Test under single key light early.

---


# Manga Style

Value-first. Screentone feel. Panel staging. Distinct from full-color anime.

## Tenets
1. Design in grayscale values first
2. Screentone / hatch textures sparingly
3. Speed lines and emphasis FX
4. Expressive faces / eyes per demographic
5. Black-heavy compositions OK

## Vs anime-style
Anime = color cel; Manga = print value language (can still be 3D color with manga staging).


### Appendix: manga-value-design

# Manga Value Design
Block 3–5 value tiers. Reserve pure black for anchors.
Screen patterns for midtones; keep face values clean.

---


# Cartoon Style

Bold shapes. Graphic color. Readability over realism.

## When to Use
- Cartoon games / animated props and characters
- Exaggerated silhouettes and expressions
- When anime cel language is too specific

## Tenets
1. Silhouette first
2. Exaggerated proportions
3. Limited palette, bold accents
4. Soft or graphic shading (project choice)
5. Detail in shapes, not micro-PBR

## Handoff
`character-artist` / `prop-artist` → `materials` → `lookdev`

## Reference Guide
| Topic | Reference |
|-------|-----------|
| Shape language | `references/cartoon-shape-language.md` |


### Appendix: cartoon-shape-language

# Cartoon Shape Language
Circles = friendly; squares = stable; triangles = danger.
Exaggerated heads/hands. Overlap shapes for appeal.
Avoid noisy subdivision detail.

---


# Comic Book Style

Ink-ready contrast. Panel-friendly staging. Halftone optional.

## Tenets
1. High contrast lighting for ink read
2. Strong contour / crease support
3. Limited screentone / hatch language in textures or comp
4. Hero poses and camera angles
5. Speeds lines / impacts as FX meshes when needed

## Reference Guide
| Topic | Reference |
|-------|-----------|
| Ink & tone | `references/ink-tone.md` |


### Appendix: ink-tone

# Ink & Tone
Bake AO into graphic cavities. Use ColorRamp for 2–3 tone prints.
Compositor: optional halftone overlay; keep subtle for 3D readability.

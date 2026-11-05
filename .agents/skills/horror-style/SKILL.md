---
name: horror-style
description: Psychological horror art direction for Blender assets inspired by Silent Hill, Resident Evil, Chilla's Art, Fear to Fathom, and Iron Lung. Use for sparse industrial environments, analog aesthetics, and tension-driven lighting.
license: MIT
metadata:
  author: https://github.com/arjun988
  version: "1.0.0"
  domain: blender
  role: specialist
  triggers: horror, psychological horror, scary, Silent Hill, Resident Evil, Chilla's Art, Fear to Fathom, Iron Lung, creepy, unsettling
  related-skills: lighting, environment-artist, lowpoly-style, materials
---

# Horror Style Specialist

Psychological tension over jump scares. Environmental storytelling. Sparse detail. Industrial decay.

## When to Use

- Horror game environments and props
- Psychological tension scenes
- Analog/liminal aesthetic assets
- Industrial decay settings
- Limited visibility compositions

## Design Philosophy

Inspired by: Fear to Fathom, Chilla's Art, Puppet Combo, Silent Hill, Resident Evil, Iron Lung

**Core tenets:**
1. **Less is more** — Absence creates tension
2. **Familiar made wrong** — Recognizable spaces with subtle wrongness
3. **Light as enemy** — Darkness hides; light reveals uncomfortably
4. **Industrial analog** — CRT screens, fluorescent hum, concrete, rust
5. **Environmental narrative** — Story told through objects, not exposition

## Visual Language

| Element | Horror Treatment |
|---------|------------------|
| Architecture | Brutalist, institutional, repetitive |
| Materials | Stained concrete, peeling paint, rust, yellowed plastic |
| Lighting | Single source, flickering, cold fluorescent |
| Detail density | Sparse foreground, empty midground, obscured background |
| Color | Desaturated, sickly greens, cold blues, blood accent sparingly |
| Scale | Slightly wrong proportions (low ceilings, narrow corridors) |

## Modeling Guidelines

- **Corridors:** Narrow (1.2–1.5m) for claustrophobia
- **Ceilings:** Low (2.2–2.4m institutional)
- **Doors:** Slightly oversized or undersized — uncanny
- **Detail:** Concentrate on hero interactive objects; walls mostly bare
- **Damage:** Water stains > bullet holes; neglect > destruction
- **Technology:** 80s–90s analog — CRT monitors, tape recorders, rotary phones

## Sparse Detail Rule

```
Foreground: 1–2 narrative objects (key, note, blood stain)
Midground: Architectural structure only
Background: Fog/darkness obscures incomplete geometry
```

Do not over-model backgrounds visible only in darkness.

## Lighting (Horror)

Coordinate with lighting skill:
- High contrast ratio (8:1 minimum key:fill)
- Visible light source meshes (bare bulb, fluorescent tube)
- Volumetric fog mandatory for depth
- Color temperature clash: warm interior vs cold exterior
- Flicker animation on 1–2 lights only

## Audio-Visual Sync Points

Design geometry supporting:
- Long empty hallways (footstep echo)
- Door slow-open clearance
- Corner blind spots
- Mirror/reflection placements

## Material Palette

| Material | Parameters |
|----------|------------|
| Stained concrete | Roughness 0.9, desaturated gray-green |
| Peeling paint | Vertex color mask, exposed concrete under |
| Rust metal | Roughness 0.85, dark orange-brown |
| Yellowed plastic | Subsurface slight, warm yellow |
| CRT screen | Emission: green/phosphor, low intensity |
| Blood (sparingly) | Dark dried red, roughness 0.7 |

## Reference Mood Board Targets

- Empty school hallways after hours
- Abandoned medical facilities
- Submarine interiors (Iron Lung)
- Fog-shrouded streets with single streetlight
- Apartment with one room lit by TV glow

## Polycount Approach

Horror benefits from lowpoly-style efficiency:
- Simple geometry + strong lighting = effective horror
- See lowpoly-style for budget alignment
- Budget saved on geo → spend on lighting/volumetrics

## MCP Integration

1. Build sparse environment layouts via MCP
2. Place single-source lighting via MCP
3. Assign desaturated materials via MCP
4. Validate sightlines and blind corners via camera MCP
5. Keep background collections low-poly/hidden in fog

## Constraints

### MUST DO
- Prioritize atmosphere over detail
- Design readable paths with unsettling alternatives
- Use environmental storytelling objects sparingly
- Coordinate with lighting skill always
- Test scene from player eye height (1.6m)

### MUST NOT DO
- Over-detail every surface
- Bright even lighting
- Jump-scare gore everywhere
- Modern smartphone/tech unless anachronism intentional
- Dense vegetation (breaks institutional mood unless forest horror)

## Reference Guide

| Topic | Reference | Load When |
|-------|-----------|-----------|
| Environment layouts | `references/horror-layouts.md` | Level blockout |
| Analog props | `references/analog-props.md` | Prop list |

## Related Horror Packs
- `psx-horror-style`, `cosmic-eldritch-horror`, `body-horror-style`, `analog-found-footage-horror`
- `liminal-space-style`, `folk-horror-style`, `mascot-puppet-horror`, `dream-weirdcore-style`
- `indie-horror-aesthetics`


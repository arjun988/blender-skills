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



### Appendix: analog-props

# Analog Props (Horror)

Props that signal psychological horror through familiarity and decay.

## Technology (80s–90s)

| Prop | Mesh Notes | Material |
|------|------------|----------|
| CRT TV | Boxy; curved screen inset | MAT_Plastic_Beige + emissive screen |
| VHS player | Front slot, buttons | Yellowed plastic |
| Rotary phone | Handset separate object | Matte plastic + coiled cord (curve) |
| Cassette recorder | Visible buttons, tape door | Wear on corners |
| Fluorescent fixture | Visible tube geometry | Emission + metal housing |

## Institutional

| Prop | Narrative Signal |
|------|------------------|
| Wheelchair | Medical trauma |
| Hospital bed | Confinement |
| Metal locker | School/prison |
| Clipboard/paper | Bureaucratic dread |
| Fire extinguisher | False safety |

## Domestic Uncanny

| Prop | Placement |
|------|-----------|
| Single chair facing wall | Wrong behavior |
| Unmade bed | Recent presence |
| Kitchen clock stopped | Time distortion |
| Child toy alone | Innocence corrupted |
| Mirror | Use sparingly; reflection issues in engine |

## Modeling Rules

- Low poly sufficient — atmosphere from lighting
- Asymmetric wear (one corner more damaged)
- Visible dirt at touch points (handles, edges)
- Name: `SM_Prop_[Type]_[Variant]`

## Placement

One narrative prop per room maximum. Overcrowding kills tension.

### Appendix: horror-layouts

# Horror Layouts

## Corridor Types

| Type | Width | Length | Mood |
|------|-------|--------|------|
| Claustrophobic | 1.2m | 8–15m | Trapped |
| Institutional | 1.8m | 15–30m | Bureaucratic dread |
| Grand decay | 3m | 20m+ | Overwhelming emptiness |

## Room Flow

```
Entry (lit) → Transition (dim) → Reveal (dark + single source) → Payoff (narrative object)
```

## Blind Corners

Place at least one 90° turn before major story beats. Player cannot see payoff from entry.

## Vertical Compression

Low ceilings (2.2m) in tension zones. Slightly higher (2.8m) in false-safe rooms before scares.

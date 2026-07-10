---
name: hair-groom
description: Hair and fur grooming in Blender using curves, particle hair, geometry nodes, and game hair-card workflows. Use for characters, creatures, and real-time hair cards via MCP.
license: MIT
metadata:
  author: https://github.com/arjun988
  version: "1.0.0"
  domain: blender
  role: specialist
  triggers: hair, groom, fur, hair cards, particle hair, curves hair, scalp, bangs, beard, whiskers
  related-skills: character-artist, creature-artist, materials, texture-workflow, rendering
---

# Hair Groom

Believable hair flow. Scalp coverage. Cards for games. Curves/particles for cinematic.

## When to Use

- Character scalp hair, beards, brows
- Creature fur / mane / whiskers
- Game hair-card generation and placement
- Cinematic curve/particle grooms

## Path Decision

```
Target = Game / real-time  → Hair cards (+ optional proxy curves)
Target = Cinematic        → Curves or particle hair + materials
Target = Both             → High groom → bake cards / textures
```

## Workflow (Game Cards)

```
Scalp mesh → Guide curves → Card strips along flow
  → Atlas UVs → Alpha/normal hair texture → LOD cards → Export
```

## Workflow (Cinematic)

```
Scalp → Particle/curve groom → Clump/frizz/noise
  → Hair shader (melanin/roughness) → Render test → Cache if needed
```

## Groom Principles

1. **Flow first** — Primary direction before flyaways
2. **Density hierarchy** — Dense roots, controlled tips
3. **Clumps** — Hair reads as groups, not spaghetti
4. **Silhouette** — Outer shape more important than strand count
5. **Scalp bleed** — Avoid bald patches at hairline

## Card Guidelines

| LOD | Cards (guide) | Notes |
|-----|---------------|-------|
| Hero close-up | 80–200 | Layered shells |
| Standard | 30–80 | Main masses |
| Distant | 8–20 | Cap + few strips |

- Name: `SM_HairCard_[Region]`
- Atlas: `T_Hair_[Name]_RGBA` (alpha in A)
- Prefer opacity clip or hashed for Eevee preview

## Naming

- Guides: `CRV_HairGuide_[Region]`
- Cards: `SM_HairCard_[Region]`
- Collection: `COL_Hair_[Character]`

## Constraints

### MUST DO
- Establish hairline and parting early
- Match card UVs to atlas layout
- Test silhouette from game camera angles

### MUST NOT DO
- Uniform card width everywhere
- Skip root density near scalp
- Over-detail flyaways before primary masses


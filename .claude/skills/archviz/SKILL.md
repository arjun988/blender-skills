---
name: archviz
description: Architectural visualization in Blender for interiors/exteriors with real-world scale, camera composition, PBR materials, and still/animation delivery via MCP.
license: MIT
metadata:
  author: https://github.com/arjun988
  version: "1.0.0"
  domain: blender
  role: specialist
  triggers: archviz, architectural visualization, interior render, exterior render, real estate render, architecture viz
  related-skills: environment-artist, materials, lighting, camera-cinematography, rendering, compositing, lookdev
---

# Archviz

Real-world scale architecture. Clean cameras. Believable materials. Delivery stills.

## When to Use

- Interior/exterior architectural presentations
- Real-estate style stills and simple walkthroughs
- Material/lighting lookdev for spaces

## Workflow

```
CAD/scale check → Greybox → Final modeling → Materials
  → Cameras → Lighting (HDRI + practicals) → Render → Comp
```

## Scale & Modeling

- Millimeter–meter accuracy where specs exist
- Straight verticals; controlled bevels on visible edges
- Separate glass, frames, furniture collections

## Cameras

- Verticals corrected (shift) for exteriors when needed
- 24–35mm interiors common; avoid extreme wide unless intentional
- Use `camera-cinematography`

## Lighting

- HDRI for exteriors / window light
- Practical lamps as mesh lights
- Soft GI; avoid game-style single harsh key unless styled

## Delivery

- High-res stills; optional depth/mist for comp
- `compositing` for exposure polish
- Keep layered EXR for revisions

## Constraints

### MUST DO
- Verify real-world scale early
- Lock cameras before heavy grade
- Keep glass/IOR plausible

### MUST NOT DO
- Game lowpoly shortcuts on hero archviz plates
- Over-saturate materials



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

## Reference Guide

| Topic | Reference | Load When |
|-------|-----------|----------|
| Archviz Camera | `references/archviz-camera.md` | When needed |
| Archviz Lighting | `references/archviz-lighting.md` | When needed |


## Appendix: archviz-camera

# Archviz Camera

Correct verticals (shift) for exteriors.
24–35mm interiors common.
Eye height ~1.5–1.7m unless dramatic.

## Appendix: archviz-lighting

# Archviz Lighting

HDRI + window portals + practicals.
Soft GI. Accurate white balance.
Avoid game-style single harsh key unless styled.

# Isometric Style

Readable dioramas. True iso framing. Tile-aware assets.

## When to Use

- Strategy / sim / city-builder assets
- Isometric diorama renders
- Orthographic hero presentations

## Camera Setup

```
Camera type: Orthographic
Rotation: typically 54.736° / 30° patterns (true iso) OR project-specific dimetric
Scale: frame subject with padding for UI
CAM_Iso_[Shot]
```

Match project’s exact iso angles — do not invent per asset.

## Asset Rules

1. **Readable from iso angle first** — Not perspective hero camera
2. **Tile footprint** — Document cell size (e.g. 1×1, 2×2)
3. **Height clarity** — Vertical read without confusion
4. **Edge contrast** — Separate from ground plane
5. **LOD for dense maps** — Far tiles cheaper

## Modeling

- Avoid detail only visible from ground FPS view
- Strong top/side planes
- Anchor pivot to tile corner or center per kit standard

## Presentation

- Soft key + cool fill common for dioramas
- Slight AO / ground shadow for lift
- Optional `compositing` grade for portfolio

## Constraints

### MUST DO
- Lock camera angle for the set
- Document tile size and pivot rule
- Check readability at game ortho scale

### MUST NOT DO
- Detail undersides invisible in iso
- Mix perspective cameras into iso kits without reason

## Reference Guide

| Topic | Reference | Load When |
|-------|-----------|----------|
| Iso Camera | `references/iso-camera.md` | When needed |
| Tile Footprints | `references/tile-footprints.md` | When needed |


### Appendix: iso-camera

# Iso Camera

Orthographic. Lock angle for whole kit.
Common: true iso (~54.736° / 45°) or dimetric project standard.
Document tile size + pivot (corner vs center).

### Appendix: tile-footprints

# Tile Footprints

| Footprint | Use |
|-----------|-----|
| 1×1 | Props, small buildings |
| 2×2 | Houses, landmarks |
| 1×2 | Walls, roads |

Height in tile units for occlusion sorting if needed.

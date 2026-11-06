
# Cloth Sim

Garment blockout → sim → art-direct → bake. Stable pins. Engine-friendly caches/shape keys.

## When to Use

- Dresses, capes, coats, flags, banners
- Character clothing that needs drape
- Baking sim to shape keys or Alembic/USD caches
- Pre-roll settling before animation export

## Workflow

```
Garment mesh (quad-friendly) → Vertex groups (pin/collide)
  → Cloth modifier settings → Collision objects
  → Pre-roll settle → Sim pass → Art-direct fixes
  → Bake shape keys / cache → Cleanup → Export
```

## Mesh Prep

- Quads preferred; even density on deforming areas
- Avoid long skinny triangles on folds
- Apply scale before sim
- Separate garment from body collider

## Vertex Groups

| Group | Purpose |
|-------|---------|
| `PIN_Cloth` | Anchors (waist, shoulders, collar) |
| `COL_Ignore` | Optional non-colliding regions |
| `STIFF_High` | Belts, seams that should resist stretch |

## Settings Starters

| Look | Quality | Speed | Bending |
|------|---------|-------|---------|
| Soft dress | 8–12 | 1.0 | Low |
| Stiff coat | 5–8 | 1.0 | Higher |
| Flag/cape | 8–10 | 1.0–1.5 | Low–mid |

Tune mass and air viscosity for scale. Always run a settle pre-roll.

## Bake Targets

| Target | Use |
|--------|-----|
| Shape keys | Game poses / few frames |
| Alembic/USD | Cinematic caches |
| Armature weights | If converting to deform-only |

## Constraints

### MUST DO
- Apply scale; define pin groups before long sims
- Collide against simplified body capsule/mesh
- Art-direct after sim (sculpt/corrective keys)

### MUST NOT DO
- Sim hero cloth on ultra-dense sculpt meshes
- Skip pre-roll (starts mid-air / exploding)
- Export raw unstable caches

## Reference Guide

| Topic | Reference | Load When |
|-------|-----------|----------|
| Cloth Settings Presets | `references/cloth-settings-presets.md` | When needed |
| Pin And Collide | `references/pin-and-collide.md` | When needed |
| Bake Targets | `references/bake-targets.md` | When needed |


## Appendix: bake-targets

# Cloth Bake Targets

| Target | When |
|--------|------|
| Shape keys | Few poses / game LOD cloth |
| Alembic/USD | Cinematic shot caches |
| Armature only | After converting to deform clothing |
| Still final frame | Marketing stills |

## Appendix: cloth-settings-presets

# Cloth Settings Presets

| Preset | Quality Steps | Speed | Bending | Mass | Notes |
|--------|---------------|-------|---------|------|-------|
| Soft dress | 10 | 1.0 | 0.1–0.5 | Low–mid | Needs good pins |
| Stiff coat | 6 | 1.0 | 1–3 | Mid | Higher structure |
| Cape/flag | 8 | 1.2 | 0.05–0.3 | Low | Air viscosity up |
| Tablecloth | 8 | 1.0 | 0.5 | Mid | Large pin border |

Always apply scale. Pre-roll 20–60 frames.

## Appendix: pin-and-collide

# Pins & Collision

## Pins
- Collar, waistband, shoulder seams, belt loops
- Paint soft falloff — hard binary pins crease badly

## Colliders
- Simplified body (capsules or low mesh)
- Thickness margin scaled to character size
- Disable self-collision first; enable if needed carefully

## Bake Path
Settle → animated collide → corrective sculpt/shape keys → export

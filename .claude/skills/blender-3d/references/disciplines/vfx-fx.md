
# VFX / FX

Readable effects. Controlled simulation domains. Game sprites vs cinematic volumes.

## When to Use

- Smoke, fire, dust, sparks, debris
- Magic / sci-fi energy FX
- Muzzle flashes, trails, impacts
- Geometry Nodes driven particle systems

## Path Decision

```
Game real-time → Meshes/cards/ribbons + emissive mats (+ GN)
Cinematic     → Mantaflow / particles / GN → render → comp
Hybrid        → Sim in Blender → bake flipbooks/meshes for engine
```

## Workflow

```
Brief (silhouette + timing) → Proxy emitter → Sim/GN prototype
  → Art-direct motion → Materials/lights → Cache → Render/comp or export
```

## Effect Types

| Type | Blender Approach |
|------|------------------|
| Smoke/fire | Mantaflow domain + flow; keep domain tight |
| Sparks | Particle Newtonian + collision + trail |
| Debris | Rigid body shards (`physics-sim`) |
| Magic ribbons | Curves / GN extrude + emissive |
| Dust hit | Short particle burst + soft sprites |

## Domain Rules (Volume)

- Domain only as large as needed
- Resolution from low → high after motion approved
- Open borders intentionally; avoid wasted empty voxels
- Collection: `COL_FX_[Shot]`

## Naming

- Emitters: `FX_Emit_[Name]`
- Domains: `FX_Domain_[Name]`
- Caches: document frame range in brief

## Game Export Notes

- Prefer mesh cards / GN instances over volume export
- Atlas flipbooks when baking fire/smoke for engines
- Keep pivot at logical spawn point

## Constraints

### MUST DO
- Approve motion at low res before high-res sim
- Light FX intentionally (emissive + key)
- Cache before final render

### MUST NOT DO
- Huge empty domains
- Unbounded particle counts
- Skip timing brief (start/peak/end frames)

## Reference Guide

| Topic | Reference | Load When |
|-------|-----------|----------|
| Fx Timing Brief | `references/fx-timing-brief.md` | When needed |
| Volume Domain Rules | `references/volume-domain-rules.md` | When needed |
| Game Fx Export | `references/game-fx-export.md` | When needed |


## Appendix: fx-timing-brief

# FX Timing Brief Template

```
Shot:
Effect:
Start frame:
Anticipation:
Peak frame:
Tail / dissipate:
Camera: CAM_
Silhouette read (yes/no):
Game or cinematic:
```

Approve motion at low domain res / low particle count first.

## Appendix: game-fx-export

# Game FX Export Patterns

| Effect | Export |
|--------|--------|
| Fire/smoke | Flipbook atlas or mesh cards |
| Sparks | Particle meshes / trails |
| Magic ribbons | Curve meshes + emissive |
| Debris | Pre-sim shards as meshes |

Pivot at spawn point. Document lifetime frames.

## Appendix: volume-domain-rules

# Volume Domain Rules

- Domain tightly fits action + 10–20% margin
- Open borders only where smoke should escape
- Noise / dissolve for art direction after motion OK
- Lights: emissive fire + key rim for readability
- Cache before beauty render

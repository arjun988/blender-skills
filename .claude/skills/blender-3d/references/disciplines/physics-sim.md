
# Physics Sim

Stable rigid/soft body setups. Motivated destruction. Baked caches.

## When to Use

- Rigid body interactions and collapses
- Soft body jiggle / rubber / simple soft props
- Destruction and debris (cell fracture / pre-cut shards)
- Pre-vis physics before VFX polish

## Workflow

```
Simplify collision meshes → Assign rigid/soft bodies
  → Constraints → Passive settings → Bake → Art-direct → Export cache
```

## Rigid Body Quick Rules

| Role | Settings notes |
|------|----------------|
| Active | Moving debris / props |
| Passive | Floors, walls, heavy anchors |
| Convex hull | Fast, approximate |
| Mesh | Accurate, heavier |

- Apply scale before sim
- Use margin appropriate to scale
- Collection: `COL_Physics_[Shot]`

## Constraints

- Hinge / fixed / motor for mechanical links
- Breakable constraints for destruction beats
- Name: `RBCON_[Object]_[Type]`

## Destruction Approach

```
1. Pre-cut shards (cell fracture or manual)
2. Island meshes as active rigid bodies
3. Passive shell until trigger frame
4. Animate trigger (force / keyframed activation)
5. Bake → cleanup interpenetrations
```

## Soft Body

- Prefer for simple soft props; use `cloth-sim` for garments
- Goal weights to retain shape
- Soft + collision object required

## Bake / Export

- Bake to cache before render
- Alembic/USD for cinematic debris
- For games: bake key poses or flipbook; rarely live Blender physics

## Constraints

### MUST DO
- Apply scale; use simplified colliders
- Bake before final delivery
- Trigger destruction intentionally (frame)

### MUST NOT DO
- High-res sculpt meshes as active colliders
- Unbounded shard counts
- Leave sims unbaked for final renders

## Reference Guide

| Topic | Reference | Load When |
|-------|-----------|----------|
| Rigid Body Presets | `references/rigid-body-presets.md` | When needed |
| Destruction Pipeline | `references/destruction-pipeline.md` | When needed |
| Sim Bake Checklist | `references/sim-bake-checklist.md` | When needed |


## Appendix: destruction-pipeline

# Destruction Pipeline

1. Pre-fracture (cell fracture / manual islands)
2. Passive until trigger frame
3. Breakable constraints or animated activation
4. Bake
5. Cleanup penetrations
6. Export Alembic or mesh sequence

## Appendix: rigid-body-presets

# Rigid Body Presets

| Case | Shape | Mass | Friction | Bounce |
|------|-------|------|----------|--------|
| Crate | Box | Mid | 0.5 | Low |
| Barrel | Cylinder | Mid | 0.4 | Low |
| Debris shard | Convex | Low | 0.6 | Low |
| Ball | Sphere | Low | 0.3 | Mid–high |

Apply scale. Passive world for floors/walls.

## Appendix: sim-bake-checklist

# Sim Bake Checklist

- [ ] Scale applied
- [ ] Simplified colliders
- [ ] Trigger frame set
- [ ] Cache baked
- [ ] Viewport play stable
- [ ] Render uses cache

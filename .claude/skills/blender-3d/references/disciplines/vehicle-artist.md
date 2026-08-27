
# Vehicle Artist

Proportion-driven vehicles. Clear body language. Manufacturing panel flow. Engine-ready LODs.

## When to Use

- Cars, trucks, bikes, aircraft, boats, ships
- Mechs and large mechanical walkers
- Transit / industrial vehicles
- When vehicle work should not live under generic hard-surface

## Design Principles

1. **Proportion blockout first** — Wheelbase, cabin, mass distribution
2. **Centerline symmetry** — Mirror early; break only for damage/wear
3. **Panel flow** — Seams follow stamped/assembled construction
4. **Functional readability** — Lights, intakes, doors, wheels read clearly
5. **Separate systems** — Body, wheels, glass, interior, lights as objects

## Workflow

```
Ortho refs → Chassis blockout → Body volumes → Wheel/suspension
  → Panel breaks → Booleans/cutters → Bevels → Glass/lights
  → Interior (LOD-aware) → UVs → Materials → LODs → Collision → Export
```

## Blockout Checklist

- [ ] Overall length / width / height locked
- [ ] Wheel size and stance correct
- [ ] Cabin / canopy silhouette readable
- [ ] Ground clearance intentional
- [ ] Symmetry axis established

## Object Split (Game)

| Object | Why |
|--------|-----|
| `SM_Vehicle_Body` | Main shell |
| `SM_Vehicle_Wheel_*` | Spin / steer |
| `SM_Vehicle_Glass` | Transparency / sorting |
| `SM_Vehicle_Light_*` | Emissive materials |
| `SM_Vehicle_Interior` | Cull on distant LODs |

## LOD Guidance

| LOD | Focus |
|-----|-------|
| LOD0 | Full panels, interior if visible |
| LOD1 | Simplified panels, remove micro |
| LOD2 | Body + wheels + glass only |
| LOD3 | Impostor / ultra-low hull |

Use `lod-pipeline` for generation and validation.

## Collision

- Simple convex hulls per major volume
- Wheel capsules/cylinders separate if physics-driven
- See `collision-proxy`

## Constraints

### MUST DO
- Lock proportions before panel detail
- Keep wheels as separate objects when animated
- Plan LODs and collision with body

### MUST NOT DO
- Detail interior before exterior silhouette
- Boolean chaos without cutter collection
- Single merged mesh for all systems on game vehicles

## Reference Guide

| Topic | Reference | Load When |
|-------|-----------|----------|
| Proportion Blockout | `references/proportion-blockout.md` | When needed |
| Vehicle Object Split | `references/vehicle-object-split.md` | When needed |
| Vehicle Lod Targets | `references/vehicle-lod-targets.md` | When needed |


## Appendix: proportion-blockout

# Vehicle Proportion Blockout

## Cars / Trucks
1. Wheelbase length
2. Track width
3. Wheel diameter + stance
4. Cabin height vs hood
5. Overhang front/rear

## Aircraft
1. Fuselage length vs wingspan
2. Wing root thickness
3. Landing gear stance
4. Cockpit canopy silhouette

## Ships / Boats
1. Length overall / beam / draft
2. Superstructure mass
3. Waterline readability

## Mechs
1. Hip height / shoulder width
2. Limb segment ratios
3. Cockpit / head mass
4. Foot print for stability read

Lock these before panel detail.

## Appendix: vehicle-lod-targets

# Vehicle LOD Targets

| LOD | Goal |
|-----|------|
| 0 | Full panels, visible interior if cabin readable |
| 1 | Remove bolts/seals; simplify glass frames |
| 2 | Body + wheels + glass + lights |
| 3 | Hull blob + wheel discs |

Bake panel lines to normal from LOD0 → lower when needed.

## Appendix: vehicle-object-split

# Vehicle Object Split

| Object | Animate? | LOD keep until |
|--------|----------|----------------|
| Body | Rare | LOD3 |
| Wheels | Yes | LOD2 |
| Calipers | Optional | LOD1 |
| Glass | No | LOD2 |
| Lights | Emissive | LOD2 |
| Interior | No | LOD1 (drop after) |
| Wipers/mirrors | Optional | LOD0–1 |

Collision: body convex pieces + wheel cylinders/capsules.

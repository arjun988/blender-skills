
# Prop Artist

Grounded, readable props. Silhouette first. Real-world scale. Kitbash-friendly parts.

## When to Use

- Furniture, tools, containers, electronics, household objects
- Hero interactive props and background set dressing pieces
- Kitbash libraries (handles, brackets, panels, fasteners)
- When hard-surface sci-fi language would feel wrong

## Design Principles

1. **Real-world scale** — Measure against human (door 2.0–2.1m, chair seat ~0.45m)
2. **Silhouette readability** — Reads at game camera distance
3. **Wear hierarchy** — Contact edges dirty; protected faces cleaner
4. **Part logic** — Separate meshes where materials or LODs differ
5. **Pivot correctness** — Floor contact, grip, hinge, or socket as needed

## Workflow

```
Reference → Scale blockout → Primary volumes → Secondary forms
  → Edge bevels → Wear/damage → UVs → Materials → Optimize → Export
```

## Prop Tiers

| Tier | Tris (guide) | Detail | Use |
|------|--------------|--------|-----|
| Hero | 2k–8k | Full bevels, unique wear | Interactables, close-ups |
| Standard | 500–2k | Clean forms, shared mats | Midground |
| Background | 100–500 | Block forms, atlas mats | Far / dense dressing |

## Kitbash Rules

- Name parts `SM_KB_[Category]_[Part]`
- Keep origins at logical attach points
- Prefer modular dimensions (0.05 / 0.1 / 0.25m grid)
- Collection: `COL_Kitbash_[Set]`

## Material Guidance

- Limit unique materials; atlas where possible
- Separate glass / emissive / opaque when needed for engine
- Wear via roughness/AO, not only albedo dirt

## Handoff

- UVs → `uv-workflow`
- Look → `materials` / `lookdev`
- Placement → `set-dressing`
- Ship → `asset-optimization` → `export-pipeline` or engine export skill

## Constraints

### MUST DO
- Set real-world scale before detailing
- Place pivot intentionally
- Match prop tier to camera distance

### MUST NOT DO
- Over-greeble everyday objects
- Use sci-fi panel language on mundane props
- Skip collision planning for interactables

## Reference Guide

| Topic | Reference | Load When |
|-------|-----------|----------|
| Prop Tiers | `references/prop-tiers.md` | When needed |
| Kitbash Library | `references/kitbash-library.md` | When needed |
| Everyday Prop Checklist | `references/everyday-prop-checklist.md` | When needed |


## Appendix: everyday-prop-checklist

# Everyday Prop Checklist

- [ ] Real-world scale vs human reference
- [ ] Silhouette readable at game FOV
- [ ] Pivot correct for use case
- [ ] Bevels only on visible contact edges
- [ ] Material count within budget
- [ ] UVs: no obvious stretch on hero faces
- [ ] Collision proxy planned
- [ ] Naming `SM_` + collection `COL_`

## Appendix: kitbash-library

# Kitbash Library Spec

## Naming
`SM_KB_[Category]_[Part]_[Variant]`

Categories: `Handle`, `Bracket`, `Bolt`, `Panel`, `Pipe`, `Vent`, `Switch`, `Label`, `Foot`, `Hinge`

## Grid
- Base module: 0.05m
- Prefer 0.05 / 0.1 / 0.25 / 0.5m extents
- Origin at attach face center

## Collections
`COL_Kitbash_[SetName]` with subcollections per category.

## Export
Instance in scenes; do not unique-mesh every use unless hero.

## Appendix: prop-tiers

# Prop Tiers & Budgets

| Tier | Camera distance | Tris guide | Materials | Collision |
|------|-----------------|------------|-----------|-----------|
| Hero interactable | < 2m | 2k–8k | Unique or shared atlas + unique trim | Accurate convex / multi-UCX |
| Standard mid | 2–8m | 500–2k | Shared atlas | Simple box/convex |
| Background | > 8m | 100–500 | Atlas / trim sheet | Optional / none |
| Kitbash part | modular | 50–400 | Trim sheet | Attach-point only |

## Pivot Rules
- Floor props: origin at ground contact center
- Handheld: grip point
- Doors/drawers: hinge
- Wall mounts: wall contact plane

## Wear Map Priority
1. Handles, rims, corners
2. Floor-facing feet
3. Top dust catchers
4. Protected undersides (cleaner)

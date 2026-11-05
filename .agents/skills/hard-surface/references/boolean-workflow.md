# Boolean Workflow

## Solver Selection

| Solver | Use When |
|--------|----------|
| Exact | Mechanical, precision cuts (default) |
| Float | Legacy; avoid unless compatibility needed |

## Common Artifacts & Fixes

| Artifact | Fix |
|----------|-----|
| Z-fighting faces | Merge by distance; manual face cleanup |
| Missing faces | Increase cutter overlap; check normals |
| Ngons at intersection | Convert to quads with loop cuts |
| Shading breaks | Weighted normals; mark sharp edges |

## Cutter Best Practices

- Cutter extends past target mesh on all axes
- Cutter has clean manifold geometry
- Apply scale on cutter before boolean
- Keep cutters in `COL_Booleans` collection (hidden in render)

## Stack Order

```
Correct:  Mirror → Boolean → Bevel → Weighted Normal
Wrong:    Bevel → Boolean (bevel will be destroyed)
```

## Batch Boolean Strategy

For multiple panel cuts:
1. Combine cutters with Boolean Union first (separate object)
2. Single Boolean Difference against target
3. Reduces stack depth and artifacts

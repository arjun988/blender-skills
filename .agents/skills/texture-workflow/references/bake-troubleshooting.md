# Bake Troubleshooting

## Normal Map Artifacts

| Artifact | Cause | Fix |
|----------|-------|-----|
| Seams visible | Cage too tight/loose | Adjust cage extrusion 0.01–0.05m |
| Black spots | Overlapping high-poly | Fix intersecting geometry |
| Inverted normals | Flipped faces on high/low | Recalculate outside |
| Blurry detail | Low bake resolution | Increase to 2048+; increase margin |
| Stripes | Bad UV seams | Reposition seams to hidden edges |

## AO Issues

| Issue | Fix |
|-------|-----|
| Too dark | Reduce AO strength in shader; don't bake into albedo |
| Missing contact | Increase ray distance |
| Noise | Smooth AO in post or increase samples |

## Cage Setup

```
1. Duplicate low-poly → name SM_Asset_Cage
2. Solidify or shrinkwrap expand 0.02m outward
3. Select as cage object in bake settings
4. Delete cage after successful bake
```

## Ray Distance

Start at 0.01m for small props; 0.05m for characters. Increase if missing detail; decrease if artifacts.

## Margin

Minimum 16px at target resolution. Hero assets: 32px at 4K bake.

## Test Workflow

Bake single tile/region first before full atlas bake.

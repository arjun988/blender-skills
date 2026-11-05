# Scatter Systems

## Rock Scatter

```
Input: Cliff surface mesh
Density: 0.3–1.0 per m²
Scale: 0.5–2.0 (non-uniform 0.8–1.2)
Rotation: Random Z; align normal optional
Cull: Slope > 45° exclude
```

## Grass Scatter

```
Density: 5–20 per m² (adjust for target polycount)
Scale: 0.8–1.2
Only on upward-facing normals (Normal dot Z > 0.7)
```

## Debris Scatter

```
Clustered: Poisson disk minimum distance 0.3m
Seed-exposed for art iteration
Realize before export; cap instance count
```

## Performance Cap

Set maximum instance count input. Background: 500. Hero zone: 2000 max.

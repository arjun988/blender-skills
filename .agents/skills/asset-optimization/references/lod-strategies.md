# LOD Strategies

## Decimate Settings

| Asset Type | Decimate Type | Ratio LOD1 | Ratio LOD2 |
|------------|---------------|------------|------------|
| Hard surface | Planar | 0.5 | 0.25 |
| Organic | Collapse | 0.5 | 0.3 |
| Foliage | Collapse | 0.4 | 0.15 |

## Silhouette Preservation

After each LOD: rotate 360° and compare silhouette to LOD0. If identity lost, adjust decimate or hand-edit.

## Impostor LOD3

Billboard or octahedral impostor for distant trees/rocks. Replace geometry entirely at 50m+.

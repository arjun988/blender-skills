# PBR Value Reference

Photographically grounded values. Adjust per reference photo.

## Metals

| Material | Base Color (sRGB) | Metallic | Roughness |
|----------|-------------------|----------|-----------|
| Iron | 0.56, 0.57, 0.58 | 1.0 | 0.5 |
| Gold | 1.0, 0.766, 0.336 | 1.0 | 0.3 |
| Copper | 0.955, 0.637, 0.538 | 1.0 | 0.35 |
| Aluminum | 0.913, 0.921, 0.925 | 1.0 | 0.4 |
| Chrome | 0.875, 0.875, 0.875 | 1.0 | 0.05 |

## Dielectrics

| Material | Base Color (sRGB) | Metallic | Roughness |
|----------|-------------------|----------|-----------|
| Fresh concrete | 0.51, 0.51, 0.51 | 0 | 0.9 |
| Old concrete | 0.4, 0.38, 0.35 | 0 | 0.95 |
| Red brick | 0.262, 0.095, 0.061 | 0 | 0.85 |
| Wood (oak) | 0.553, 0.359, 0.192 | 0 | 0.6 |
| Rubber | 0.021, 0.021, 0.021 | 0 | 0.8 |
| Plastic (white) | 0.733, 0.733, 0.733 | 0 | 0.45 |
| Skin (Caucasian ref) | 0.847, 0.638, 0.552 | 0 | 0.5 |

## Glass

| Type | Transmission | IOR | Roughness |
|------|--------------|-----|-----------|
| Clear | 1.0 | 1.45 | 0.0 |
| Frosted | 1.0 | 1.45 | 0.3 |
| Water | 1.0 | 1.33 | 0.0 |

## Rules

- Albedo never pure black (0) or pure white (1) for dielectrics
- Metallic: use 0 or 1; blend zones only at transitions (paint mask)
- Dark albedo ≠ low roughness (common error)
- Always verify against photographic reference for hero assets

## Subsurface (Skin)

- Subsurface Weight: 0.1–0.2
- Subsurface Radius: R > G > B (e.g., 1.0, 0.2, 0.1)
- Subsurface Color: warmer than base color

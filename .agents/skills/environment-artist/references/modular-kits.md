# Modular Kit Design

## Minimum Viable Kit

Before hero pieces, ship:

| Piece | Quantity |
|-------|----------|
| Straight wall (2m) | 2 variants |
| Corner 90° | 2 (L + R or mirror) |
| Door frame | 1 |
| Window frame | 1–2 |
| Floor tile | 1 |
| Ceiling tile | 1 |

## Snap Point Convention

- Origin at grid corner (floor level)
- Positive Y = forward face (outward normal)
- Connection points at grid intersections
- Document snap grid in export README

## Trim Sheet Layout

```
[Corner trim | Edge trim | Fill panel | Window surround | Damage variants]
```

Shared 2048 trim sheet across entire kit.

## Variation Without Unique Geo

- Vertex color tints
- Material instance parameters
- Decal overlays
- 90° rotation of asymmetric pieces

## Kit Validation

Assemble test scene:
- Closed room from kit only
- L-shaped corridor
- T-junction
- Verify no gaps at 0.001m tolerance

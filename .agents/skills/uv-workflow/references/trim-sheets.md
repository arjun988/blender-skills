# Trim Sheets

## Layout Strategy

Single 2048 or 4096 texture shared across modular kit:

```
[Top edge trim | Corner trim | Panel fill | Window frame | Damage variants | Bolts/rivets]
```

## UV Assignment

- Each module UVs to assigned trim region
- Maintain consistent texel density across modules
- Leave 2–4px margin between trim regions

## Modeling Trim Geometry

- Bevel profile matches trim sheet cross-section
- Extrude along edges using trim UV coordinates
- Avoid unique trim geo per module — reuse UV regions

## Variation

| Method | Use |
|--------|-----|
| UV offset | Same trim, different region |
| Vertex color | Tint without new texture |
| Material instance | Roughness variation |

## Export Notes

Document trim sheet regions in production brief:

```
Region A (0.0–0.25 U): Wall panel standard
Region B (0.25–0.5 U): Wall panel damaged
Region C (0.5–0.75 U): Corner trim
Region D (0.75–1.0 U): Window surround
```

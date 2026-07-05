# Building Generators

## Parametric Inputs

| Input | Type | Example |
|-------|------|---------|
| floor_count | Integer | 3–20 |
| floor_height | Float | 3.0m |
| width | Float | 8.0m |
| depth | Float | 12.0m |
| window_rows | Integer | 2–4 |
| seed | Integer | Reproducible variation |

## Node Stack Pattern

```
Footprint (mesh plane) → Extrude Mesh (floors)
    → Set Position (window cuts via index selection)
    → Instance Window Module on selected faces
    → Set Material Index
    → Realize Instances (for export)
```

## Window Cut Pattern

```
Subdivide face grid → Delete random faces (seed-driven)
    → Inset remaining → Extrude inward
```

## Roof Variants

Switch node group input:
- `flat` — extrude top face
- `pitched` — edge split + rotate
- `parapet` — extrude low wall perimeter

## Output Structure

Separate objects per module for game kits:
- `SM_Env_Building_Wall_Module`
- `SM_Env_Building_Window_Module`
- `SM_Env_Building_Roof_Module`

## Performance

Realize and decimate before export. Cap floor_count for background buildings.

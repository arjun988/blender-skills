# Photogrammetry Scan Cleanup

## Import Checklist

- [ ] Correct scale (measure known dimension)
- [ ] Origin at logical pivot
- [ ] Normals consistent (outside)
- [ ] Duplicate mesh before cleanup

## Common Issues

| Issue | Fix |
|-------|-----|
| Holes in mesh | Fill with grid fill / sculpt patch |
| Floating noise | Select by loose parts; delete |
| Decimation artifacts | Remesh at 0.5mm voxel; shrinkwrap to original |
| Color baked in albedo | Rebake albedo with flat lighting or color correct |
| Wrong scale | Measure two known points; apply scale |
| Non-manifold | 3D Print Toolbox or manual edge cleanup |

## Retopology Path

```
Scan (high-poly) → Cleanup → Shrinkwrap retopo OR Quad Remesh
    → UV low-poly → Bake normal/AO/curvature from scan
    → Discard or hide scan mesh
```

## Decimation for Bake Source

Reduce scan to manageable high-poly (1–5M tris) before baking:
- Decimate modifier (planar or collapse)
- Preserve UV borders if scan has UVs

## Albedo Extraction

If scan albedo contains lighting:
1. High-pass filter in texture tool
2. Or rebake with flat neutral lighting in Blender
3. Target: albedo without shadow information

## LOD from Scan

Never use raw scan in game engine.
Pipeline: scan → retopo → bake → LOD chain on retopo mesh.

## Naming

```
SM_Asset_Scan_Source (hidden, reference)
SM_Asset_LOD0 (game mesh)
T_Asset_N, T_Asset_BC (baked from scan)
```


# Texture Workflow

Bake high-poly detail to efficient texture sets. Optimize memory. Engine-ready outputs.

## When to Use

- Baking sculpt detail to normal maps
- Creating texture atlases for modular kits
- PBR texture set generation
- Decal placement and blending
- Texture memory optimization

## Workflow

```
High/Low Poly Setup → Cage Setup → Bake Maps → Composite
    → Atlas Pack → Engine Format Export → Validation
```

## Standard PBR Texture Set

| Map | Format | Notes |
|-----|--------|-------|
| Base Color | sRGB PNG | No embedded AO |
| Normal | Linear PNG | OpenGL convention unless engine specifies |
| Roughness | Linear PNG | Single channel |
| Metallic | Linear PNG | Single channel |
| AO | Linear PNG | Multiply in shader, not base color |
| Height | Linear PNG | Optional parallax |
| Emission | sRGB PNG | Mask-based |
| ORM Packed | Linear PNG | R=AO, G=Roughness, B=Metallic (Unreal) |

Naming: `T_[Asset]_[Map]` per `naming-conventions.md` (shared)

## Bake Setup

```
1. Low-poly mesh with UVs (active)
2. High-poly mesh (sculpt or detail) — selected
3. Cage extrusion: 0.01–0.05m (adjust per asset scale)
4. Ray distance: match cage
5. Bake margin: 16px minimum
6. Anti-aliasing: enabled
```

## Maps to Bake

| Map | Source | Priority |
|-----|--------|----------|
| Normal | High→Low | Required |
| AO | High or low (cavity) | Required |
| Curvature | High sculpt | Wear masks |
| Position | High | Optional (blending) |
| Thickness | Subsurface meshes | Characters |

## Texture Atlas Strategy

Modular kits share one atlas:
```
1. All modules UV'd to shared 0–1 or UDIM space
2. Bake each module to atlas regions
3. Trim sheet areas for repeating detail
4. Single material references atlas
5. Document region map for artists
```

## Decals

- Decal mesh projected on surface
- Separate UV channel or atlas region
- Blend via alpha mask
- Limit decal overdraw in engine

## Memory Optimization

| Technique | Savings |
|-----------|---------|
| ORM packing | 3 textures → 1 |
| Shared atlas | N materials → 1 texture |
| Lower res on hidden surfaces | 50%+ memory |
| BC compression in engine | 4:1 or 6:1 |
| Trim sheets | Reuse detail across assets |

## Resolution Guidelines

See `polycount-budgets.md` (shared) texture section.

## MCP Integration

1. Setup bake objects via MCP
2. Configure bake settings via MCP if supported
3. Export baked images via MCP
4. Assign baked textures to materials via MCP
5. Query texture count and resolution

## Validation Checklist

- [ ] Normal map correct orientation (test in engine)
- [ ] No UV seams visible in bake
- [ ] AO not baked into base color
- [ ] Consistent texel density in final textures
- [ ] Texture resolution within budget
- [ ] Files named per convention
- [ ] sRGB vs Linear correctly assigned

## Constraints

### MUST DO
- Bake high-poly detail before discarding sculpt
- Use cage for clean normal bakes
- Pack ORM for engine efficiency
- Test normal map orientation in target engine
- Document atlas regions for modular kits

### MUST NOT DO
- Bake without cage on complex shapes
- Embed AO in base color (PBR standard)
- Exceed texture budget without LOD justification
- Use inconsistent normal map conventions
- Skip margin in bake settings

## Reference Guide

| Topic | Reference | Load When |
|-------|-----------|-----------|
| Bake troubleshooting | `references/bake-troubleshooting.md` | Bake artifacts |
| ORM packing | `references/orm-packing.md` | Unreal/Unity export |


## Appendix: bake-troubleshooting

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

## Appendix: orm-packing

# ORM Packing

Pack Occlusion, Roughness, Metallic into single texture for engine efficiency.

## Channel Assignment (Unreal Standard)

| Channel | Map |
|---------|-----|
| R | Ambient Occlusion |
| G | Roughness |
| B | Metallic |

## Blender Compositing

```
1. Bake or import AO, Roughness, Metallic as separate grayscale
2. Compositor: Combine RGB
   - R ← AO
   - G ← Roughness
   - B ← Metallic
3. Export as T_Asset_ORM.png (linear, no sRGB)
```

## Unity HDRP/URP

Similar ORM packing; verify shader expects same channel order.
Some Unity shaders use Metallic(R) + AO(B) — check target shader docs.

## Naming

`T_[Asset]_ORM` per naming conventions.

## Notes

- All channels linear color space
- AO should not be multiplied into albedo if using ORM shader
- Default roughness: 0.5 where no map painted
- Metallic: binary 0 or 1 for most surfaces; blend only at transitions

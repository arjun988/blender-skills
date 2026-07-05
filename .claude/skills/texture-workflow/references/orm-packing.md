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

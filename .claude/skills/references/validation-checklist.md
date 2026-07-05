# Asset Validation Checklist

Run before marking any asset complete. Query scene via Blender MCP when available.

## Scale & Transform

- [ ] Correct real-world scale (1 unit = 1 meter unless project specifies otherwise)
- [ ] Origin at logical pivot (floor contact, grip point, hinge axis)
- [ ] All transforms applied (scale 1,1,1 / rotation 0,0,0 where required)
- [ ] Object faces correct forward axis for target engine (typically -Y or +X)

## Topology

- [ ] Clean topology; no n-gons on deforming areas
- [ ] Quad-dominant mesh
- [ ] No duplicate vertices (merge threshold verified)
- [ ] No loose vertices/edges/faces
- [ ] No internal faces or non-manifold geometry
- [ ] Correct normals (no inverted faces)
- [ ] Hard edges use weighted normals or sharp edges as appropriate

## UVs

- [ ] Efficient UV layout; minimal wasted space
- [ ] Consistent texel density across visible surfaces
- [ ] Seams placed at hidden/construction edges
- [ ] No overlapping UVs (unless intentional mirroring)
- [ ] Lightmap UV channel if engine requires baked lighting

## Materials & Textures

- [ ] Minimal material count (target: 1-3 for props, per project spec)
- [ ] PBR values physically plausible or intentionally stylized
- [ ] Texture resolution matches budget (512/1024/2048/4096)
- [ ] No unused material slots
- [ ] Material names follow `MAT_` convention

## Organization

- [ ] Collections organized per `naming-conventions.md`
- [ ] Meaningful object names with `SM_` prefix
- [ ] Modifier stack documented or collapsed per export requirements
- [ ] Reference/blockout geometry in separate collections
- [ ] Collision meshes in `COL_Collision`

## Performance

- [ ] Polycount within budget (see `polycount-budgets.md`)
- [ ] Triangle count verified
- [ ] LODs created if required
- [ ] Instances used for repeated geometry
- [ ] Geometry nodes baked if runtime performance requires

## Export Readiness

- [ ] Export format confirmed (FBX/GLTF/USD/etc.)
- [ ] Animation/armature export tested if applicable
- [ ] Materials export or texture paths documented
- [ ] Pivot and scale verified in target engine
- [ ] Naming compatible with import pipeline

## Game Ready

- [ ] Readable silhouette at gameplay distance
- [ ] Collision proxy created and simplified
- [ ] No unnecessary high-poly detail on hidden surfaces
- [ ] Asset modular/reusable if part of kit
- [ ] Style consistent with project art direction

## Validation Output Template

```markdown
## Validation Report: [Asset Name]

**Status:** PASS / FAIL
**Polycount:** [tris] (budget: [target])
**Materials:** [count]
**UV Efficiency:** [%]
**Scale:** [dimensions]

### Issues Found
- [issue + fix applied]

### Screenshots
- Front / Side / Top / 3/4 views verified
```

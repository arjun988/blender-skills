
# UV Workflow

Efficient UV layouts with consistent texel density. Seams at hidden edges. Engine-ready.

## When to Use

- After topology locked, before texturing
- Modular kit UV atlas planning
- Lightmap UV channel setup
- UDIM workflows for hero assets

## Workflow

```
UV Planning → Seam Marking → Unwrap → Texel Density Check
    → Pack → Mirror/Overlap Decision → Lightmap UV (if needed) → Validation
```

## Seam Placement Rules

Place seams at:
- Back of head, spine centerline
- Inner arms, inner legs
- Bottom of chin, underside of objects
- Panel edges on hard surface (construction seams)
- Hidden areas under clothing/overlaps

Never place seams on:
- Face (front)
- Primary gameplay-visible surfaces
- Deforming joint centers (relocate to nearby hidden area)

## Texel Density

**Formula:** `Texel Density = Texture Resolution / UV Island Size in UV space`

Target consistency across visible surfaces:

| Asset Tier | Target TD (px/m) |
|------------|------------------|
| Hero | 512–1024 px/m |
| Standard | 256–512 px/m |
| Background | 128–256 px/m |

Use same density for modular kit pieces sharing atlas.

## Unwrap Methods

| Method | Use When |
|--------|----------|
| Smart UV Project | Quick blockout UVs only |
| Follow Active Quads | Strip UVs (roads, limbs) |
| Cube Project | Boxy hard surface |
| Lightmap Pack | Lightmap channel |
| Manual seam + Unwrap | Production default |

## UV Packing

- Margin: 0.002–0.01 UV units (engine dependent)
- Rotate islands for maximum packing efficiency
- Group islands by material ID
- Keep related islands near each other in UV space
- Use UVPackmaster or native pack for production

## Mirrored UVs

- Mirror UVs for symmetrical characters (save texture space)
- Offset mirrored islands slightly if engine requires unique bakes
- Mark mirrored halves in object naming: `_L` / `_R` meshes if separate

## UDIM Workflow

For hero assets exceeding single 4K texture:
- Tile 1001: head
- Tile 1002: torso
- Tile 1003: limbs
- Document tile assignment in production brief

## Lightmap UVs

Second UV channel requirements:
- No overlapping islands
- Consistent texel density less critical
- Larger margin (0.02+) for light bleed prevention
- Pack separately from texture UVs

## Modular UV Atlas

```
1. Plan shared atlas resolution (2048/4096)
2. Assign UV islands per module to atlas regions
3. Trim sheet regions for repeating detail
4. Vertex color variation for module differentiation
5. Document atlas layout for texture artist
```

## MCP Integration

1. Mark seams via MCP if supported
2. Execute unwrap via MCP
3. Query UV island count and pack efficiency
4. Assign UV channels via MCP
5. Validate no overlapping UVs (except intentional mirror)

## Validation Checklist

- [ ] No unintended overlapping UVs
- [ ] Consistent texel density on visible surfaces
- [ ] Seams hidden at gameplay angles
- [ ] UV islands within 0–1 (or UDIM tiles assigned)
- [ ] Lightmap channel separate if required
- [ ] Pack efficiency > 75%

## Constraints

### MUST DO
- Plan UVs before final modeling (topology informed by UV needs)
- Maintain texel density consistency
- Hide seams at logical construction edges
- Create lightmap UVs for baked lighting pipelines
- Document atlas layout for modular kits

### MUST NOT DO
- Smart UV Project as final production UVs
- Overlapping UVs on unique surface detail (unless mirrored)
- Inconsistent texel density on same asset tier
- Seams across faces or primary visible surfaces
- Skip packing margins

## Reference Guide

| Topic | Reference | Load When |
|-------|-----------|-----------|
| Texel density calc | `references/texel-density.md` | Hero assets |
| Trim sheets | `references/trim-sheets.md` | Modular kits |


## Appendix: texel-density

# Texel Density

## Calculation

```
Texel Density (px/m) = Texture Resolution / Physical Size (m)

Example: 2048px texture over 2m wall = 1024 px/m
```

## Matching Density

1. Select UV island for reference object
2. Scale all islands to match reference TD
3. Use UV sync tools or manual scaling from known UV-to-world ratio

## Hero vs Background

Same kit: hero modules 1024 px/m, background modules 512 px/m — acceptable if not adjacent in scene.

## UDIM

Each tile maintains independent TD. Document tile assignment per body region.

## Appendix: trim-sheets

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

# Universal Asset Pipeline

Every Blender asset follows this sequence. **Never skip planning.**

```
Reference Collection
        ↓
     Planning
        ↓
  Scale Planning
        ↓
  Primary Shapes
        ↓
 Secondary Shapes
        ↓
 Silhouette Review
        ↓
 Topology Strategy
        ↓
     Modeling
        ↓
      Cleanup
        ↓
    UV Planning
        ↓
  UV Unwrapping
        ↓
    Materials
        ↓
  Optimization
        ↓
 Rigging (if required)
        ↓
Animation (if required)
        ↓
Collision Planning (if game asset)
        ↓
      Export
        ↓
   Validation
```

## Phase Details

### Reference Collection
- Gather orthographic views, real-world dimensions, style references
- Identify modular pieces, hero vs background detail levels
- Note manufacturing/construction logic for hard surface

### Planning
- Define asset purpose: hero prop, modular kit piece, background filler
- Target platform: mobile, console, PC, cinematic-only
- Document polycount, texture resolution, LOD requirements
- Choose style skill: horror, lowpoly, stylized, realistic

### Scale Planning
- Establish scene scale (1 Blender unit = 1 meter default)
- Place human-scale reference (1.8m capsule or mannequin)
- Lock pivot/origin strategy before modeling

### Primary Shapes
- Block out largest readable forms first
- Focus on silhouette, not detail
- Use primitives, mirror, array, non-destructive modifiers

### Secondary Shapes
- Add functional subdivisions: panels, edges, structural breaks
- Maintain shape hierarchy: primary > secondary > tertiary

### Silhouette Review
- Rotate camera at 45° increments
- Check readability at gameplay/camera distance
- Fix silhouette before adding micro-detail

### Topology Strategy
- Plan edge flow for deformation (characters) or bevels (hard surface)
- Decide triangulation tolerance for target engine
- Plan UV islands before committing topology

### Modeling
- Execute discipline-specific workflow (hard surface, organic, modular)
- Prefer modifier stack over destructive edits
- Keep naming and collections organized from start

### Cleanup
- Merge by distance (threshold appropriate to scale)
- Remove doubles, loose geometry, interior faces
- Apply transforms before export prep
- Verify normals (weighted normals for hard surface)

### UV Planning
- Mark seams at hidden/construction edges
- Plan texel density relative to screen size
- Separate material IDs if needed for engine

### UV Unwrapping
- Unwrap with consistent texel density
- Pack efficiently; minimize wasted space
- Create lightmap UVs for baked lighting if required

### Materials
- PBR or stylized per art direction
- Reuse master materials; instance variations
- Limit unique material count for game assets

### Optimization
- Run asset-optimization validation
- Create LODs if required
- Collapse unnecessary subdivisions

### Rigging / Animation
- Only when asset requires deformation or motion
- Mechanical assets: constraints over weight painting
- Characters: animation-ready topology prerequisite

### Collision Planning
- Simple proxy meshes: box, capsule, convex hull
- Separate `COL_` collection; never export render mesh as collision

### Export
- Apply export-pipeline skill for target format
- Verify scale, axis, pivot, normals, animation

### Validation
- Run full checklist in `validation-checklist.md`
- Capture viewport renders from multiple angles
- Confirm game-ready status before delivery

## Pipeline by Asset Type

| Asset Type | Critical Phases | Typical Skills |
|------------|-----------------|----------------|
| Hard surface prop | Scale → Silhouette → Bevel → UV → PBR | hard-surface, materials, export-pipeline |
| Environment modular | Modular planning → Instances → Texel density | environment-artist, geometry-nodes, uv-workflow |
| Character | Anatomy → Topology → Retopo → Rig | character-artist, retopology, rigging |
| Creature | Anatomy → Sculpt → Retopo → Rig | creature-artist, sculpting, retopology |
| Procedural kit | Node design → Variation → Optimization | geometry-nodes, procedural-modeling |
| Cinematic set | Composition → Lighting → Rendering | lighting, rendering, realistic-style |
